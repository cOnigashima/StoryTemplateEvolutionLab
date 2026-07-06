# Prompt: scoped -> frozen packet check

以下の `packets/scoped/packet-001-<slug>.yaml` をレビューし、
Scene に切ったときに戦略上の質問が残らない状態なら `status: frozen` に変更した完成版 YAML を出してください。
残る場合は `status: scoped` のまま、足りない点を YAML 内の値として補ってください。

[INPUT PACKET]
<<<PACKET_YAML>>>
ここに scoped packet を貼る
<<<END_PACKET_YAML>>>

[REFERENCE ARC]
<<<ARC_01_MD>>>
ここに arcs/arc-01.md を貼る
<<<END_ARC_01_MD>>>

判定基準:
- purpose が一文で明確か
- entry / exit の差が episode 群で支えられているか
- 各 episode に role / loss / gain / cliffhanger があるか
- disclose / withhold / guardrails が scene 設計に使えるか
- dependencies が解決されているか
- first episode を書くのに blocker が残っていないか

ルール:
- 出力は YAML のみ
- key は増減させない
- 不足情報は `未決定`
- `status` 以外も、必要なら修正してよい
- `status: frozen` にする場合は `open_questions.blocker` を空にし、`freeze_check` をすべて `true` にする
