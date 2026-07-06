# origin: STE-v4
# bible/ — frozen設計（書く前に確定するもの。直接編集せず design→承認→反映で更新）

各 facet を1ファイルで持つ。最小項目を埋める。空欄は status で明示。

## facet 一覧（新作はこの stub を埋める）
- `logline.md` — kernel #1 の展開
- `promise.md` — 読者への約束（3項目以上）
- `theme.md` — 主題（問い→仮説→反証→結論の4段）
- `rules.md` — 世界のルール・禁則
- `style_voice.md` — POV / 時制 / レジスタ / 文長 / 叙述温度 / 禁止語彙
- `world.md` — 世界設定
- `characters.md` — 人物（state/entities.yaml と ID を対応させる）
- `system.md` — 能力・制度など（該当作品のみ）
- `timeline.md` — 年表（state/timeline.yaml の設計側マスター）
- `foreshadowing-map.md` — 伏線設計（state/foreshadowing.yaml の設計側マスター）

> 実体ファイルは新作 bootstrap 時に生成する。ここでは facet の一覧と役割のみ定義。
