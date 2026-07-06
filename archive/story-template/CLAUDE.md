# [作品タイトル]

この作品 repo の制作OS契約。別セッションの ChatGPT / Claude が入っても、
`raw input -> digest -> seed -> promises -> arc -> packet -> scene -> draft -> review -> canon reverse flow`
の接続が切れないようにする。

## 作品概要

- 一行要約: 未決定
- 現在のフォーカス Arc: `arc-01`
- 現在のフォーカス Packet: `packet-001-<slug>`

## 制作優先順位

1. `story/promises.md` の約束を壊さない
2. 巨大入力は `story/intake/raw/` と `story/intake/digests/` を経由させる
3. 次の 1〜2 packet の因果に効くものだけ先に固める
4. 空欄は禁止。未確定は必ず `未決定` と書く
5. Review は感想で終わらせず、必要なら上流へ戻す
6. Review では `issue level / return target / recommended next job / expected delta` を必ず残す

## 文体指針

- 視点: 未決定
- 時制: 未決定
- 文体: 未決定
- 一文の長さ: 未決定
- 地の文の温度: 未決定

## 禁則

- 絶対NG: 未決定
- 避ける: 未決定

## 執筆開始ライン

- `CLAUDE.md` が埋まっている
- `story/promises.md` に作品約束がある
- `bible/world.md` に現行 Arc に必要な制約がある
- `bible/characters.md` に主要キャラのドラマ情報がある
- `bible/rules.md` に文体ルールがある
- `arcs/arc-01.md` がある
- `packets/frozen/` に 1 本ある
- `scenes/` にその Packet の scene 群がある
- 今書く packet / first episode を止める blocker が `story/open-questions.md` に残っていない

## 参照ファイル

- 運用ガイド: `README.md`
- intake ガイド: `story/intake/README.md`
- raw intake: `story/intake/raw/`
- intake digests: `story/intake/digests/`
- 作品約束: `story/promises.md`
- 未解決論点: `story/open-questions.md`
- 設計負債: `story/design-debt.yaml`
- canon patch proposal: `story/canon-patch-proposals/`
- 種 inbox: `story/seeds/`
- 世界観: `bible/world.md`
- キャラクター: `bible/characters.md`
- 文体・禁則: `bible/rules.md`
- シリーズ概観: `arcs/series-overview.md`
- 現行 Arc: `arcs/arc-01.md`
- 章束: `packets/`
- シーン: `scenes/`
- 本文: `drafts/`
- レビュー: `reviews/`
- learning 自動キャプチャルール: `.claude/rules/learning-capture.md`
- ファイル成長ルール: `.claude/rules/file-growth.md`
- 学習ログ: `learning/`
- 公開準備: `approved/`
- 公開済み: `published/`
- ChatGPT prompt 集: `prompts/`
- 参考ノート: `community/`
- アクションパケット: `actions/`
- `queue/` は legacy projection。実行キューの正本ではない

## Story OS

- `source = story/intake/raw + story/intake/digests`
- `seed = story/seeds`
- `macro = story/promises + bible + arcs`
- `meso = packets`
- `micro = scenes + drafts + episodes`
- `meta = reviews + learning + design debt + canon patch proposals`
- `release = approved + published`

### 制作フロー

1. `story/intake/raw/` に巨大入力を保存する
2. `story/intake/digests/` で batch ごとに圧縮する
3. `story/seeds/` で再利用核に切る
4. `reviews/seed-to-macro-template.md` で反映先を整理する
5. `story/promises.md`, `bible/` で収束する
6. `arcs/` で変化線に変換する
7. `packets/` で実装可能単位に分解する
8. `scenes/` で局所衝突に落とす
9. `drafts/` で本文にする
10. `reviews/` で批評する
11. 必要なら `story/design-debt.yaml` と `story/canon-patch-proposals/` に返す

### Arc / Packet / Scene の基準

- Arc は `scoped` で Packet 開始:
  始点と終点、中核対立、主反転、読者フック、packet-001 / packet-002 の役割が見えていること
- Packet は `frozen` で Scene 開始:
  `purpose / episode_roles / end_hooks / disclose / withhold / guardrails` が埋まり、さらに `episodes:` に各話の `role / purpose / loss / gain / reveal / hooks / cliffhanger` が入っていて、scene 担当に渡しても戦略質問が返らないこと
- Scene は draft-ready:
  `packet_id`, `target_episode`, `purpose`, `desire`, `obstacle`, `turn`, `reveal`, `emotional_turn`, `canon delta`, `cliffhanger`, `next scene handoff`, `review memo` があること

### ユビキタス言語

- 正式語は `章束`、実装語は `packet`
- `作品の核` の正式語は `作品約束`
- `review` を単独で使わない。`typed review` と `approval review` を分ける
- `story/intake/` は巨大入力の source layer、`story/seeds/` は再利用核の inbox
- `backlog/` は legacy 資産。物語の入口正本は `story/intake/` と `story/seeds/`
- `Story Board`, `Loop Canvas`, `Run Ledger` は投影面であり、作品正本ではない

### Input Intake

- `story/intake/raw/` には長い会話ログ、設定投下、断片メモの原文を置く
- `story/intake/digests/` には raw を圧縮した batch summary を置く
- raw をいきなり `bible/` や `arcs/` に入れない
- digest から seed を作り、seed から必要最小限だけ macro へ昇格する
- seed の反映先整理には `reviews/seed-to-macro-template.md` を使う

### Bible の役割

- `bible/world.md`, `bible/characters.md`, `bible/rules.md` は「安定設定の索引」
- raw input や重複メモをそのまま入れる場所ではない
- 次の 1〜2 packet の意思決定に効かない情報は、無理に bible に入れない
- 差分案は bible に直接書かず、`story/canon-patch-proposals/`, `reviews/`, `story/design-debt.yaml` に置く
- bible への昇格は approval を通した canon patch で行う

### ファイルの成長

- Story OS のファイルは **1 ファイルで始めて、育ったら分割する**。テンプレートの初期構成は上限ではない
- bible, arcs, scenes, packets, reviews, prompts はすべて作品の成長に伴い増える
- 分割の判断基準・命名パターン・手順は `.claude/rules/file-growth.md` を参照する

### Reverse Flow

- prose 問題 -> `scenes/` または `drafts/`
- hook / pacing -> `packets/`
- 動機 / 関係性 -> `bible/characters.md`
- 開示順 / 反転点 -> `arcs/`
- 作品約束のズレ -> `story/promises.md`
- 長生きする構造問題 -> `story/design-debt.yaml`
- まだ確定していない設定変更 -> `story/canon-patch-proposals/`
- packet 切り替わりの齟齬 -> `reviews/bridge-review-template.md` を使ってから `packets/` へ返す

## Story OS Docs

`factory-platform` が隣にある構成では、詳細は次を参照する。

- `../factory-platform/docs/story-os-ubiquitous-language.md`
- `../factory-platform/docs/story-os-domain-map.md`
- `../factory-platform/docs/story-os-sources-of-truth.md`
- `../factory-platform/docs/story-os-workflows.md`
- `../factory-platform/docs/story-os-implementation-map.md`
- `../factory-platform/docs/story-os-audit-checklist.md`

## Skills

- `/pitch` - seed / packet 材料を作る
- `/draft` - frozen packet と scene 群から本文を起こす
- `/critic` - typed review を作り、必要なら上流へ返す
- `/critic` は `reviews/typed-review-template.md` を基準にする
- `/continuity` - 過去話との整合性チェック
- `/release` - 公開用に整形

## Agents

- `plotter` - promises / arc / packet 設計担当
- `drafter` - scene / draft 実装担当
- `critic` - typed review 担当
- `continuity-checker` - 連続性監視担当
