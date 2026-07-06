# loop_monitors — 堂々巡り検出の設計

review⇄revise のようなループが「進捗せず同じ所を回っている」状態を検出して打ち切る仕組み。

## 判定基準（supervisor persona が評価）
- 指摘の数が周回ごとに減っているか
- 同じ指摘の堂々巡りになっていないか
- 修正が実際に反映されているか

いずれも NO なら `ABORT` し、`design/open-questions.md` に「人間判断が要る論点」として記録して人間ゲートへ回す。

## 設定
各 workflow の `loop_monitors:` で `watch`（監視するstep群）と `threshold`（周回上限）を指定。

| workflow | watch | threshold |
|---|---|---|
| draft-episode | ontology_check / self_review / revise | 3 |
| review-multipass | persona_round1 / adjudicate1 / persona_round2 | 2 |

## 思想
機械が創作判断を握りつぶさないよう、打ち切りは「人間ゲートへ渡す」で終える。ABORT は失敗でなく「人間に返すべき」の合図。
