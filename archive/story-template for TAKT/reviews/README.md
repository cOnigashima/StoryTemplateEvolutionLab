# Reviews

`reviews/` はスコア置き場ではなく、診断と reverse flow の置き場。

原則:

- 感想で終わらせない
- hard gate と diagnosis を混ぜない
- 必ず `issue level / return target / recommended next job / expected delta` を残す
- 長生きする問題は `story/design-debt.yaml` または `story/canon-patch-proposals/` に返す

## Base Templates

- `typed-review-template.md`
  draft / episode / packet の通常診断。`hard gate`, `Packet Fulfillment Audit`, `Issue Routing` を持つ
- `bridge-review-template.md`
  `upstream exit -> downstream entry` の接続監査。packet 切り替わり前後で使う
- `seed-to-macro-template.md`
  seed を story / bible / arc / packet のどこへ昇格するか整理する

## Typical Outputs

- `typed-review-YYYYMMDD-<scope>.md`
- `bridge-review-YYYYMMDD-<upstream>-to-<downstream>.md`
- `design-review-*.md`
- `character-review-*.md`
- `world-review-*.md`
- `serial-review-*.md`
- `prose-review-*.md`
- `seed-to-macro-*.md`
- `return-map-*.md`
- `backprop-*.md`
