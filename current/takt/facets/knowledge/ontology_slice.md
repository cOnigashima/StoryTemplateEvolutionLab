# knowledge: ontology_slice
# Writing Adapter が抽出した「この単位に効く部分グラフ」を step に渡す。

step に渡すのは全 bible ではなく、以下の k-hop 抽出結果:
- 登場 entity（起点）とその1〜2hop近傍
- 各 entity の **この時点の knowledge_state**（誰が何を知っているか）
- 関わる **未回収の伏線**
- 直近の timeline / 直前話の exit_state

生成元: adapter/writing_adapter.md の抽出手順 → context_pack.md。
