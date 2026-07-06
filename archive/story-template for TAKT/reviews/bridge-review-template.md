# Bridge Review Template

上流 artifact の `exit state` と、下流 artifact の `entry state` を照合するための template。

主用途:

- `packet-N -> packet-(N+1)` の接続監査
- packet freeze 前の齟齬洗い出し
- packet 切り替わり直後の first episode 着手前確認

これは summary ではなく **接続監査**。何を持ち越し、何が齟齬で、どこへ返すかを固定する。

## Metadata

- date: YYYY-MM-DD
- reviewer:
- review_type: bridge check
- upstream:
  - artifact:
  - scope:
- downstream:
  - artifact:
  - scope:
- purpose:

## 1. Verdict Summary

- verdict: `pass / conditional_pass / fail`
- summary:
- freeze_gate: `safe / update_downstream_first / replan_required`
- primary_issue_level: `none / local / meso / macro`
- return_target:
- recommended_next_job:
- expected_delta:

## 2. Upstream Exit Carryover

上流の終点から、下流へ持ち越す canon / object / wound / relationship / hook を列挙する。

| carryover | type | upstream evidence | must_continue? | note |
|---|---|---|---|---|
|  | `canon / object / wound / relationship / hook / unresolved_question` |  | `yes / no` |  |

## 3. Downstream Entry Assumptions

下流が開始時点で前提にしている状態を書く。

| assumption | source | downstream location | note |
|---|---|---|---|
|  |  |  |  |

## 4. Alignment Check

| item | status | issue | route |
|---|---|---|---|
| physical transition | `aligned / mismatch / missing` |  |  |
| protagonist state | `aligned / mismatch / missing` |  |  |
| world state | `aligned / mismatch / missing` |  |  |
| relationship state | `aligned / mismatch / missing` |  |  |
| object / evidence carryover | `aligned / mismatch / missing` |  |  |
| unresolved hooks | `aligned / mismatch / missing` |  |  |
| rule / phase / mode carryover | `aligned / mismatch / missing` |  |  |

## 5. Mismatch Register

優先度順に書く。1 件ごとに戻し先を固定する。

| id | priority | mismatch | why_it_matters | return_target | recommended_next_job | note |
|---|---|---|---|---|---|---|
| B-1 | `must / should / nice` |  |  |  |  |  |

## 6. Already Aligned

- 

## 7. Required Carryover Actions

| priority | file / artifact | action | reason |
|---|---|---|---|
| must |  | `update / patch / no_change` |  |

## 8. Issue Routing

- issue_level:
- return_target:
- recommended_next_job:
- expected_delta:
- can_downstream_freeze_now: `yes / no`

## 9. Conclusion

- must_fix_before_next_step:
- can_wait:
- next_review_point:

## 10. Output Files

1. `reviews/bridge-review-YYYYMMDD-<upstream>-to-<downstream>.md`
2. 必要なら更新した downstream packet / scene
3. 必要なら `story/canon-patch-proposals/` または `story/design-debt.yaml`
