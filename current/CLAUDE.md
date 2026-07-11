# CLAUDE.md — 新StoryTemplate 運用契約

このファイルは current/(新正本) の下で作業するAI（Claude Code / codex / TAKT のエージェント）が従う契約。
これは StoryTemplateEvolution の `current/CLAUDE.md` を置き換える。
新セッションは `WORKFLOW.md` → 本ファイル → 該当作業の README の順で読む。

---

## 0. 大原則（Story OS）

1. **ファイルが正本。会話ログは正本ではない。** 決定はファイルに書いて初めて確定する。
2. **空欄を作らない。** 未確定は status（`tentative` / `deferred` / `needs_author_decision` / `contradiction` / `missing` …）で明示。
3. **raw を直接 bible に流さない。** 必ず `adapter/` の Intake を経由し、update proposal → 承認 → 反映。
4. **1話に全 bible を渡さない。** `adapter/` の Writing で1単位分に圧縮してから書く。
5. **レビューは感想で終わらせない。** 採否判定（採用/条件付/却下/learning送り）と反映先まで出す。
6. **状態は append-only。** state の履歴は消さず、無効化は上書きでなく無効フラグで表す。

---

## 1. 正本と作品の関係（重要）

- **current/ は正本（テンプレ本体）**。ここでは実作品の本文を書かない。
- **作品(work)は current/ をコピーした外部フォルダ**として作る（`work_init/new-work-bootstrap.md`）。
- 作業ログ・成果物（drafts/reviews/approved/published/logs）は**作品フォルダ側**に生まれる。current/ 直下には置かない。その空フォルダ雛形が `template/runtime/`。
- 作品フォルダの完全な構造は `template/folder_structure.md` が定義する。

---

## 2. 人間確認ポリシー（★この運用の肝）

方針: **人間は成果物だけを見る。工程の途中判断はループとバリデータに委ねる。**

### 人間ゲート（ここだけ止まる）

| ゲート | 位置 | 人間が見るもの |
|---|---|---|
| **G-Intake** | 企画をbibleに反映する前 | update proposal（反映案） |
| **G-Deliverable** | draft＋レビュー1サイクル後 | 本文＋レビュー票＋validator結果（作品側 runtime） |
| **G-Publish** | 公開直前 | approved 本文＋公開メタ |

### AIが人間を待たず進めてよいこと（自動）
Writing Pack圧縮 / draft生成 / ontology_check / multi-pass self-review / レビュー票作成 / loop_monitor打切り / reader-export / logs記録。

**不可逆な創作判断**（プロット根本変更・約束破棄・キャラの死）は自動確定せず `design/canon-patch-proposals/` に proposal 化 → G-Deliverable で提示。判断式: 「取り返しがつくか？」YES=自律 / NO=proposal化。

---

## 3. 共通化方針（コア＋オーバーレイ）

**背骨(core)は全作品が従い、作品固有の構造(overlay)は各作品が manifest で宣言して上書きする。**

- **core（共通・必須）**: kernel / bible・design・state / state のオントロジー対応 / レビューパイプライン / DoR-DoD / rules / 逆方向フロー。
- **overlay（作品選択）**: 執筆単位（`unit-episode-pack`＝fools流 / `unit-packet-2stage`＝villainess流）。
- **work-local（作品固有）**: CoCの卓ルール等。core に積まない。

### 明記ルール（← 悩んでいた点への回答）
各作品は `work.manifest.json` に必ず宣言する:
```json
{ "uses_core_version": "0.1", "overlays": ["unit-packet-2stage"],
  "work_local_extensions": ["coc-table-rules"],
  "deviations_from_core": [ { "rule": "review.persona_rounds", "override": 2, "reason": "..." } ] }
```
- core からの逸脱は禁止ではなく、`deviations_from_core` に理由付きで明記すれば許可。**暗黙の逸脱を禁止する。**
- 「どこまで共通化するか」の答え: **共通化は core に固定、独自化は overlay/work-local で明示宣言。**

---

## 4. StoryTemplateEvolution との統合方針

- この current/ は StoryTemplateEvolution の current/ を**置換**するもの（`../proposal/2026-07-06-workbench-ontology-loop/PROPOSAL.md` が根拠）。
- 各ファイル冒頭の `origin:` タグ（`STE-v4` / `workbench` / `fools` / `villainess`）で由来を残し、差分マージを容易にする。
- 進化ループ: 実走(作品) → retro(logs/learning) → 抽象化 → current/template 昇格。効いた工夫だけを正本へ。

---

## 5. オントロジー基盤（state の扱い）

- `state/` はプロパティグラフとして扱う。entity に安定ID、relation は `schema/relations.yaml` の統制語彙のみ。
- draft・freeze の前後で `tools/ontology_check.py` を回し、参照整合性・epistemic矛盾・未回収伏線・タイムライン循環を検出。
- 検出は当面 **warning（非gating）**。止めるのは human ゲートのみ。
