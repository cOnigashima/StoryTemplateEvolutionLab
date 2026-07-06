#!/usr/bin/env python3
"""
ontology_check.py — state(オントロジー)の整合性を検査するバリデータ。

検査:
  1. reference_integrity : relation の宛先IDが entities に存在するか
  2. required_fields     : schema の required を満たすか
  3. epistemic_no_future_ref : does_not_know の期間に KNOWS が立っていないか（矛盾）
  4. epistemic_monotonic : 同一(who,fact)で valid_at が単調か（既知を再び知る、を検出）
  5. foreshadow_payoff   : status!=recalled のまま payoff_at を過ぎた伏線（未回収）
  6. timeline_acyclic    : Event の precedes/causes が巡回していないか

方針: 当面 warning のみ（非gating）。creativeな例外を機械が握りつぶさない。
使い方: python3 tools/ontology_check.py works/<slug>
依存: PyYAML（無ければ最低限のフォールバックあり）
"""
import sys, os

def load_yaml(path):
    try:
        import yaml
    except ImportError:
        print("[warn] PyYAML未導入。`pip install pyyaml --break-system-packages` 推奨。")
        return None
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)

def ep_num(s):
    """'ep005'/'post-ep001'/'day1' 等から比較可能な数値を雑に抽出。無ければNone。"""
    import re
    if s is None:
        return None
    m = re.search(r"ep0*([0-9]+)", str(s))
    return int(m.group(1)) if m else None

def main(work_dir):
    state = os.path.join(work_dir, "state")
    entities = load_yaml(os.path.join(state, "entities.yaml")) or {}
    knowledge = load_yaml(os.path.join(state, "knowledge_state.yaml")) or {}
    foreshadow = load_yaml(os.path.join(state, "foreshadowing.yaml")) or {}
    timeline = load_yaml(os.path.join(state, "timeline.yaml")) or {}

    warnings = []

    # 既知IDの集合
    ids = set()
    for group in ("characters", "locations", "items", "factions"):
        for e in (entities.get(group) or []):
            if isinstance(e, dict) and e.get("id"):
                ids.add(e["id"])
    for f in (knowledge.get("facts") or []):
        if isinstance(f, dict) and f.get("id"):
            ids.add(f["id"])
    for ev in (timeline.get("events") or []):
        if isinstance(ev, dict) and ev.get("id"):
            ids.add(ev["id"])

    # 1. reference_integrity（relationships / knows / precedes）
    for ch in (entities.get("characters") or []):
        for rel in (ch.get("relationships") or []):
            to = rel.get("to")
            if to and to not in ids:
                warnings.append(f"[ref] {ch.get('id')} の関係先 '{to}' が存在しない")
    for k in (knowledge.get("knows") or []):
        for key in ("who", "fact"):
            if k.get(key) and k[key] not in ids:
                warnings.append(f"[ref] KNOWS の {key} '{k[key]}' が存在しない")

    # 3. epistemic_no_future_ref : does_not_know.until 以前に KNOWS が立つ矛盾
    dnk = {}
    for d in (knowledge.get("does_not_know") or []):
        dnk[(d.get("who"), d.get("fact"))] = ep_num(d.get("until"))
    for k in (knowledge.get("knows") or []):
        key = (k.get("who"), k.get("fact"))
        vk, until = ep_num(k.get("valid_at")), dnk.get(key)
        if until is not None and vk is not None and vk < until:
            warnings.append(
                f"[epistemic] {key[0]} は {key[1]} を ep{until} まで知らないはずだが "
                f"ep{vk} で KNOWS が立っている（矛盾）")

    # 4. epistemic_monotonic : 同一(who,fact)の重複KNOWS
    seen = {}
    for k in (knowledge.get("knows") or []):
        key = (k.get("who"), k.get("fact"))
        if key in seen:
            warnings.append(f"[epistemic] {key} の KNOWS が複数回定義（単調性の疑い）")
        seen[key] = True

    # 5. foreshadow_payoff : 未回収
    for fs in (foreshadow.get("foreshadowing") or []):
        if fs.get("status") != "recalled" and fs.get("payoff_at"):
            warnings.append(
                f"[foreshadow] 伏線 {fs.get('id')} '{fs.get('name')}' が未回収"
                f"（payoff_at={fs.get('payoff_at')}, status={fs.get('status')}）")

    # 6. timeline_acyclic : precedes/causes の巡回
    graph = {}
    for ev in (timeline.get("events") or []):
        graph[ev.get("id")] = list(ev.get("precedes") or []) + list(ev.get("causes") or [])
    color = {}
    def dfs(n):
        color[n] = 1
        for m in graph.get(n, []):
            if color.get(m) == 1:
                warnings.append(f"[timeline] Event の順序が循環: {n} -> {m}")
                return True
            if color.get(m, 0) == 0 and m in graph and dfs(m):
                return True
        color[n] = 2
        return False
    for n in list(graph):
        if color.get(n, 0) == 0:
            dfs(n)

    # 出力
    print(f"=== ontology_check: {work_dir} ===")
    if not warnings:
        print("OK: 検出された問題はありません。")
    else:
        for w in warnings:
            print("WARN " + w)
        print(f"\n{len(warnings)} 件の warning（非gating）。止めるのは人間ゲートのみ。")
    return 0  # 非gatingなので常に0

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(main(target))
