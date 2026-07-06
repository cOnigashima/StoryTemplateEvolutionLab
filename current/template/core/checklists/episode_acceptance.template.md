# origin: STE-v4 / fools（2026-07-06 復元マージ: 旧121行版の verifiable_by 表形式を復元、renji 固有項目は除去）
# 1話の受け入れ基準（Writing Adapter がこの雛形を ep ごとに具体化する）

## この話の目的

- entry_state（開始時点の状態）:
- exit_state（終了時点の状態）:
- what_happens（起こる出来事1〜3行）:

## 1. must_satisfy（必達 / 全 ✓ で公開可）

各項目に id / claim / verifiable_by / source を付与する。

```markdown
| ID | 項目 | verifiable_by | source |
|---|---|---|---|
| MS-01 |  | prose / meta / reviewer / reader_simulation | bible/{path} or scene_card 由来 |
```

典型項目: 主要登場人物の登場 / 主要事件の発生 / POV 方針の遵守 / 字数範囲 / 次話への引き / ID 整合（packet_id / scene_card_id 等）/ 作品固有装置の整合（work-local で追加）

## 2. must_not_violate（違反禁止 / critical 1 件でも該当 → REJECT）

```markdown
| ID | 項目 | severity | source |
|---|---|---|---|
| MNV-01 |  | low/medium/high/critical | design/project_principles.md or 他 |
```

典型項目: style_voice の POV / 時制違反 / 禁止語彙 / メタ語の本文使用 / センシティブガイド違反 / 知識状態台帳に無い情報を「既に知っている」ように書く / 台帳にある既知情報を「初めて知る」ように書く

## 3. intended_unknowns（意図的に隠す）

読者に明かさないことのリスト。漏洩防止のために明示。

## 4. must_be_clear（読者に明確に伝える）

読者に必ず伝えることのリスト。説明不足判定の基準。

## 5. acceptable_ambiguity（曖昧でよい範囲）

判定対象外の領域。

## 6. quality_gates（drafter-preflight 準拠）

```markdown
| ID | gate | check |
|---|---|---|
| QG-01 | 因果一段落 |  |
| QG-02 | 知識状態台帳の単調性 |  |
| QG-03 | POV 切替 / 話者識別 |  |
| QG-04 | 禁則語チェック |  |
| QG-05 | センシティブガイド |  |
| QG-06 | 文法・統語 |  |
| QG-07 | 字数 |  |
| QG-08 | ontology_check（epistemic 矛盾なし） |  |
| QG-09 | カクヨムポリシー |  |
```

## 7. auto_fix_allowed

AI 自動修正できる範囲。文法 / 句読点 / 禁則語提案 等。

## 8. human_required_if

人間判断必須の条件（`adapter/human_approval_policy.md` §5 のシグナル含む）。

## 9. ignore_or_defer

今回は問わない範囲。

## 10. references

review 時に参照する file の一覧。

## 判定サマリ

```markdown
| カテゴリ | 件数 | 全 ✓ なら |
|---|---:|---|
| must_satisfy | N | 必達満足 |
| must_not_violate | N | 違反なし |
| quality_gates | 9 | 客観チェック通過 |
```

全カテゴリ ✓ で公開判定可（Judge: PASS）。
critical 1 件 → REJECT_AND_REGENERATE。
human_required_if 該当 → NEEDS_HUMAN。
