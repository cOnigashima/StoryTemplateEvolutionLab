# docs/ — 用語・仕様・原理集

本ディレクトリは StoryTemplateEvolution の **言語と契約** を固定する。

| ファイル | 役割 |
|---|---|
| `vocabulary.md` | 用語 1 覧（1 概念 1 語、混同警告、禁止語） |
| `unit_taxonomy.md` | 単位階層（Manuscript/Part/Arc/Packet/Episode/Scene/Beat） |
| `kernel_spec.md` | 薄い kernel 11 項目の field-by-field 仕様 |
| `status_vocabulary.md` | 12 status / Judge 4 値 / Lock 5 状態 |
| `dor_dod.md` | Definition of Ready ／ Definition of Done（3 段ずつ） |
| `layer_facet_map.md` | Layer 0-4+R + Adapter 2 分割 |

これらは旧 Pack v3 (`../../proposal/2026-04-29-domain-kernel-v3/`、v1時代の原本は `../../archive/story-template for TAKT/proposals/`) を母体として、renji pilot で得た知見を反映したコンパクト版。詳細仕様が要るときは v3 docs を参照。

## 使い方

- 議論で語彙が揺れたら **vocabulary.md** に従う
- 単位がぶれたら **unit_taxonomy.md** に従う
- 「kernel に入れるか?」迷ったら **kernel_spec.md** §判定基準
- 「空欄って何?」迷ったら **status_vocabulary.md**
- 「執筆して良い? 公開して良い?」は **dor_dod.md**
- 「どこに置く?」は **layer_facet_map.md**
