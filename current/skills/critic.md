# /critic

> **v4 注記 (2026-04-30)**: 本 skill 定義は v4 generic 雛形。
> 各 work で実行する際は work 固有の `bible/` `state/` を参照。
> v4 のフロー全体: `proposal/2026-04-30-zero-base-v4/04_pipeline_overview.md`
> 旧 v3 の `scenes/drafted/` 等の dir 参照は v4 で更新あり（書き換え TODO、Q-B-001）。
> Drafter は `drafter-preflight.md` rule の適用必須。

---


draft を typed review として批評し、packet review / replan に返す。

## 入力

- `drafts/` にある原稿ファイル
- 関連する `packets/`, `scenes/`, `story/promises.md`, `bible/`, `approved/`, `published/`
- 必要なら直近の `reviews/` と `learning/`

## 手順

1. 指定された原稿または最新の原稿を読む
2. 対応する packet / scene / promises / rules を照合する
3. hard gate と diagnosis を分けて確認する
4. 問題を `local / meso / macro` に分け、`return target` を特定する
5. `reviews/` に typed review を出す
6. Canon 問題や長生きする構造問題があれば、`story/canon-patch-proposals/` または `story/design-debt.yaml` に返す候補を明記する

基本フォーマットは `reviews/typed-review-template.md` を使う。

## 批評観点

### Hard gate
- continuity fail
- rule conflict
- speaker confusion
- fatal coherence issue

### Packet Fulfillment
- disclose / withhold / guardrails
- episode role の達成
- packet 要件の未達

### Shared Craft
- protagonist drive
- causal chain
- relationship heat
- world operation

### Prose / Scene
- scene function
- dialogue clarity
- prose clarity
- rhythm control

## 出力フォーマット

```markdown
# Typed Review: [scope]

## Metadata
- date:
- reviewer:
- review_type: typed review
- draft:
- packet:
- episode:
- source scenes:

## Verdict Summary
- hard_gate:
- packet_review_gate:
- summary:
- primary_issue_level:
- return_target:
- recommended_next_job:
- expected_delta:

## Hard Gate
- category:
- result:
- evidence:

## Packet Fulfillment Audit
- requirement:
- verdict:
- note:

## Shared Craft Diagnosis
- protagonist_drive:
- causal_chain:
- relationship_heat:
- world_operation:

## Prose / Scene Diagnosis
- scene_function:
- dialogue_clarity:
- prose_clarity:
- rhythm_control:

## Issue Routing
- issue:
- severity:
- issue level: none | local | meso | macro
- return target:
- recommended next job:
- expected delta:

## 上流へ返すべき項目
- design debt:
- canon patch:
- learning candidate:
- local rewrite:
```

## 保存先

`reviews/typed-review-YYYYMMDD-<scope>.md`
