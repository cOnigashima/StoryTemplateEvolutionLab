# output_contract: review_ticket
# レビュー票の統一フォーマット。採否まで必ず出す。

```yaml
review:
  target: ep0NN or packet-0NN
  reviewer: critic / reader_immersion / ...
  round: 1
  rubric_score: { total: 0, gate_G1: 0, gate_G2: 0, gate_G3: 0 }
  findings:
    - id: f-001
      issue: "..."
      severity: high / mid / low
      verdict: adopt / conditional / reject / to_learning
      reverse_flow_target: draft / scene / packet / arc / bible / promises / design-debt
      reason: "..."
  promotion_candidates: []   # 複数回出た指摘 → rule/checklist/template 昇格候補
```

出力先: deliverables/reviews/
