# Typed Review Template

作品の draft / episode / packet を診断し、`continue / replan / blocked / human_review_required` を決めるための base template。

この template は **点数置き場ではない**。主目的は:

- hard gate を分離する
- issue を `local / meso / macro` に routing する
- `returnTarget / recommendedNextJob / expectedDelta` を固定する
- 必要なら `story/design-debt.yaml` と `story/canon-patch-proposals/` に返す

work-local canon がある場合は、ここに作品固有 section を足してよい。

## Metadata

- date: YYYY-MM-DD
- reviewer:
- review_type: typed review
- scope:
  - draft:
  - packet:
  - episode:
  - related_scenes:
- read_order:
  - `story/promises.md`
  - top-level index (`bible/world.md`, `bible/characters.md`, `bible/rules.md`)
  - target packet / target draft
  - relevant subfiles
  - related `reviews/`, `learning/`, `story/design-debt.yaml`, `story/canon-patch-proposals/`

## 1. Verdict Summary

- hard_gate: `pass / warning / fail`
- packet_review_gate: `continue / replan / blocked / human_review_required`
- summary:
- primary_issue_level: `none / local / meso / macro`
- return_target:
- recommended_next_job:
- expected_delta:

## 2. Hard Gate

致命的な破綻だけをここに書く。感想や好みは混ぜない。

| category | result | evidence | route |
|---|---|---|---|
| continuity | pass |  |  |
| rule conflict | pass |  |  |
| speaker confusion | pass |  |  |
| fatal coherence issue | pass |  |  |

## 3. Packet Fulfillment Audit (Gate B)

Gate A で drafter が宣言した実装計画、または frozen packet の要件に対して、本文が何を達成したかを確認する。

| # | packet requirement | source | expected beat / scene | draft implementation | verdict | note |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  | `OK / PARTIAL / MISS` |  |

判定ルール:

- `MISS` が 1 件でもあれば、最低でも `warning`
- packet の中核要件が `MISS` の場合、`replan` または `blocked`
- `PARTIAL` が複数ある場合は、scene 修正で閉じるか packet へ返すかを下で切り分ける

## 4. Shared Craft Diagnosis

以下は template の shared cue。作品固有 canon が別の観点を要求する場合は、差し替えまたは追加してよい。

### protagonist_drive

- observed evidence:
- defect:
- route:

### causal_chain

- observed evidence:
- defect:
- route:

### relationship_heat

- observed evidence:
- defect:
- route:

### world_operation

- observed evidence:
- defect:
- route:

## 5. Prose / Scene Diagnosis

### scene_function

- observed evidence:
- defect:
- route:

### dialogue_clarity

- observed evidence:
- defect:
- route:

### prose_clarity

- observed evidence:
- defect:
- route:

### rhythm_control

- observed evidence:
- defect:
- route:

## 6. Issue Routing

| issue | severity | issue_level | return_target | recommended_next_job | expected_delta | owner |
|---|---|---|---|---|---|---|
|  | `minor / major / critical` | `local / meso / macro` |  |  |  |  |

routing の原則:

- prose だけで閉じるなら `local`
- packet purpose / disclose / withhold / hook に返るなら `meso`
- promises / bible / arc の前提を壊すなら `macro`

## 7. Upstream Returns

### local rewrite candidates

- 

### design debt candidates

- 

### canon patch candidates

- 

### learning candidates

- 

## 8. Decision

- next_action_now:
- do_not_do_now:
- human_gate_needed:
- note:

## 9. Output Files

1. `reviews/typed-review-YYYYMMDD-<scope>.md`
2. 必要なら更新対象の draft / scene / packet
3. 必要なら `story/design-debt.yaml` または `story/canon-patch-proposals/`
