# output_contract: draft_format
# draft 本文の出力フォーマット。

```
---
ep: ep0NN
title: ...
meta:
  因果一段落: ...
  知識状態の更新: [ {who, fact, valid_at, source} ]
  gate_0_A_C: passed
---

（本文）
```

- meta は製作用。reader-export では除去する。
- 出力先: deliverables/drafts/ep0NN-{slug}.md
