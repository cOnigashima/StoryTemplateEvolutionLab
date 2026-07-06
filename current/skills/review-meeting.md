# /review-meeting

> **v4 注記 (2026-04-30)**: 本 skill 定義は v4 generic 雛形。
> 各 work で実行する際は work 固有の `bible/` `state/` を参照。
> v4 のフロー全体: `proposal/2026-04-30-zero-base-v4/04_pipeline_overview.md`
> 旧 v3 の `scenes/drafted/` 等の dir 参照は v4 で更新あり（書き換え TODO、Q-B-001）。
> Drafter は `drafter-preflight.md` rule の適用必須。

---


Agent Team を起動して、複数視点の typed review をまとめ、packet review gate の入力を作る。

## 概要

3人のチームメイトが draft / packet を批評し、`reviews/` に統合レビューを残す。
目的はスコアを出すことではなく、`continue / replan / blocked / human_review_required` の判断材料を揃えること。
必要なら `story/design-debt.yaml` や `story/canon-patch-proposals/` に返す。

通常の draft review では `reviews/typed-review-template.md`、packet 切り替わりでは `reviews/bridge-review-template.md` を参照する。

## チーム構成

| Teammate | 役割 |
|----------|------|
| critic | Promise を守れているかを見る |
| editor | 文体・テンポ・読みやすさの改善案 |
| continuity-guard | packet / scene / past canon との整合性を見る |

## 実行手順

1. 対象の `drafts/` と関連する `packets/`, `scenes/`, `story/promises.md`, `bible/`, `approved/`, `published/` を読む
2. critic が Promise / Arc / Packet とのズレを見る
3. editor が prose / pacing / readability の改善案を出す
4. continuity-guard が canon 矛盾、issue level、return target を特定する
5. 3人で議論し、hard gate / diagnosis / next actions を統合する
6. `packet review gate` の suggested outcome を付けて `reviews/` に出す

## 出力

`reviews/review-meeting-YYYYMMDD-HHMMSS.md` に以下を保存:

```markdown
# Review Meeting YYYY-MM-DD

## 対象
- draft:
- packet:
- episode:

## Hard Gate
- result: pass | warning | fail
- reasons:

## Diagnosis

### strengths
- 

### defects
- 

### required changes
- 

## Packet Review Gate
- suggested outcome: continue | replan | blocked | human_review_required
- rationale:

## Issue Routing
- issue level: none | local | meso | macro
- return target:
- recommended next job:
- expected delta:

## 改善点リスト

### 優先度: 高
1. [箇所]: [問題] -> [提案]

### 優先度: 中
1. [箇所]: [問題] -> [提案]

### 優先度: 低
1. [箇所]: [問題] -> [提案]

## 議論メモ

[レビュー議論の要点]

## 上流へ返すべき項目
- design debt:
- canon patch:
- local rewrite:
- bridge review needed:

## 次 sprint へ持ち越す learning 候補
- 
```

## 起動コマンド例

```
drafts/draft_epXX_XXXXXXXX.md をレビューするため Agent Team を作って。
3人にして:
- critic: Promise と Arc のズレを指摘
- editor: 文体・テンポ・読みやすさの改善案
- continuity-guard: packet / scene / past canon との整合性チェック

議論して、hard gate / diagnosis / packet review gate / 改善リストを reviews/review-meeting-YYYYMMDD-HHMMSS.md にまとめて。
長生きする問題は story/design-debt.yaml や story/canon-patch-proposals/ に返す候補も書いて。
```
