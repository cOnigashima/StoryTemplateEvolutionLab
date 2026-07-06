# origin: fools
# overlay: unit-episode-pack — 全話を先に Writing Pack 化する（規模重視・自動化向き）

manifest で `"overlays": ["unit-episode-pack"]` と宣言した作品が使う。

## 執筆単位
`Arc → Episode(公開単位) → Scene`。packet の2段freezeは持たない。

## Writing Pack（各 ep が4ファイル）
- `episode_brief.md` — 何を書くか（目的・entry/exit・出来事）
- `scene_card.md` — 場面設計（goal/conflict/turn/end/beats）
- `context_pack.md` — この話に必要な最小context（ontology k-hop抽出）
- `acceptance_checklist.md` — must_satisfy / must_not_violate / quality_gates

## 特徴
全 ep を先に pack 化しておき、draft を量産的に回す。TAKT の `draft-episode` workflow と相性が良い。

## いつ選ぶか
話数が多く（50話以上）、アーク構造が規則的で、速く完走したい作品。
