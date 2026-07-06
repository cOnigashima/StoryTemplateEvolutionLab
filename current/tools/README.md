# tools — 検査ツール

## ontology_check.py
state(オントロジー)の整合性を検査する。ハーネスの Sensor。

```bash
pip install pyyaml --break-system-packages   # 初回のみ
python3 tools/ontology_check.py works/<slug>
```

検査項目: 参照整合性 / 必須フィールド / epistemic矛盾(知らないはずの事実への言及) / epistemic単調性 / 未回収伏線 / タイムライン循環。

- 当面 **非gating（warning のみ）**。止めるのは人間ゲートだけ。
- TAKT の draft-episode / review workflow の `ontology_check` step から呼ばれる。
- 検査を増やしたくなったら schema/entity_schema.yaml の constraints と対応させて拡張する。
