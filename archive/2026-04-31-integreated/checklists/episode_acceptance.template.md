# Episode Acceptance Checklist Template

> 各 episode の Writing Pack 中の acceptance_checklist.md は本テンプレートに従う。
> renji ep001 の `works/renji/writing/episode_packs/ep001/acceptance_checklist.md` が実例。

---

## 1. must_satisfy（必達 / 全 ✓ で公開可）

各項目に id / claim / verifiable_by / source を付与。

```markdown
| ID | 項目 | verifiable_by | source |
|---|---|---|---|
| MS-01 |  | prose / meta / reviewer / reader_simulation | bible/{path} or scene_card 由来 |
```

典型項目:
- 主要登場人物の登場
- 主要事件の発生
- POV 方針の遵守
- 字数範囲
- 章末資料の配置
- 次話への引き
- 三層 / 装置の整合（作品固有）
- ID 整合（packet_id / scene_card_id 等）

---

## 2. must_not_violate（違反禁止 / 1 件でも該当 → REJECT）

```markdown
| ID | 項目 | severity | source |
|---|---|---|---|
| MNV-01 |  | low/medium/high/critical | design/project_principles.md or 他 |
```

典型項目（severity critical は作劇ルール由来）:
- 主人公を賢く / 面白く描く（作品により）
- 反対者を貶める
- 主人公の反省 / 自己懐疑
- メタ語の本文使用
- 復讐期待の煽り
- センシティブガイド違反
- 異世界要素の混入（renji 等）

---

## 3. intended_unknowns（意図的に隠す）

読者に明かさないことのリスト。漏洩防止のために明示。

---

## 4. must_be_clear（読者に明確に伝える）

読者に必ず伝えることのリスト。説明不足判定の基準。

---

## 5. acceptable_ambiguity（曖昧でよい範囲）

判定対象外の領域。

---

## 6. quality_gates（drafter-preflight 準拠）

```markdown
| ID | gate | check |
|---|---|---|
| QG-01 | 因果一段落 |  |
| QG-02 | 知識状態台帳の単調性 |  |
| QG-03 | POV 切替 |  |
| QG-04 | 禁則語チェック |  |
| QG-05 | センシティブガイド |  |
| QG-06 | 装置整合 |  |
| QG-07 | 字数 |  |
| QG-08 | 章末資料独立性 |  |
| QG-09 | カクヨムポリシー |  |
```

---

## 7. auto_fix_allowed

AI 自動修正できる範囲。文法 / 句読点 / 禁則語提案 等。

---

## 8. human_required_if

人間判断必須の条件。

---

## 9. ignore_or_defer

今回は問わない範囲。

---

## 10. references

review 時に参照する file の一覧。

---

## 判定サマリ

```markdown
| カテゴリ | 件数 | 全 ✓ なら |
|---|---:|---|
| must_satisfy | N | 必達満足 |
| must_not_violate | N | 違反なし |
| quality_gates | 9 | 客観チェック通過 |
```

全カテゴリ ✓ で公開判定可。  
critical 1 件 → REJECT_AND_REGENERATE。  
human_required_if 該当 → NEEDS_HUMAN。
