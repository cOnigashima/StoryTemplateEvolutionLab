# Story Template

この template は、創作の会話ログをそのまま本文にしないための Story OS です。
正本は会話ではなく repo の各ファイルに置きます。

この template が目指している接続は次の通りです。

- `Raw Input -> Digest -> Seed`
- `Promise -> Arc -> Packet -> Scene -> Draft`
- `Review -> Canon reverse flow`

つまり、

- 作品の核が固定されている
- 今書く単位まで分解されている
- 本文が上流へトレースできる
- レビュー結果を上流へ返せる

この 4 点が揃えば機能します。

## どのアシスタントを使うか

どれでも構いません。重要なのは「会話」ではなく「ファイル」を正本にすることです。

- ChatGPT / Claude の Web UI を使う場合:
  `prompts/` の prompt を順番に使い、出力を対象ファイルへ貼る
- Codex / Claude Code のように repo に入れる場合:
  `README.md`, `CLAUDE.md`, 各 starter を読ませて直接ファイルを埋める
- どのツールでも共通:
  `CLAUDE.md` はファイル名が歴史的にそうなっているだけで、実質は repo の制作契約

## まず何をどこまで決めればいいか

先に固めるのは「次の 1〜2 packet の因果に効くもの」だけで十分です。

今決めるべきもの:

- 主人公の欲望と欠落
- 敵対圧
- 世界のハードルール
- 禁忌
- この Arc の終点
- 直近 Packet の `disclose / withhold`
- 文体ルール

まだ決めなくてよいもの:

- 3 Arc 先の細部
- 現在出ない地名一覧
- 今出ない脇役の全履歴
- 世界史の完全年表
- 将来使うかも不明な設定

判断基準はこれです。

- その情報がないと、キャラの選択が決まらないか
- その情報がないと、世界の因果が破綻するか
- 後で変えると、既存 Draft を壊すか

長い会話ログや大量設定投下は、先に `story/intake/raw/` に置きます。
raw を圧縮した batch summary は `story/intake/digests/` に置きます。
そのうえで、まだ未確定の論点だけ `story/open-questions.md` に逃がします。

## ディレクトリの見方

### 契約層

- `CLAUDE.md`
- `template.manifest.json`

制作ルールと runtime contract。

### Source / Intake 層

- `story/intake/raw/`
- `story/intake/digests/`
- `story/intake/README.md`

巨大入力の保管と圧縮の場所。
runtime は直接読まず、人間と執筆エージェントの source layer として使います。

### Canon / Macro 層

- `story/promises.md`
- `story/open-questions.md`
- `story/design-debt.yaml`
- `story/seeds/`
- `story/canon-patch-proposals/`
- `bible/world.md`
- `bible/characters.md`
- `bible/rules.md`
- `arcs/`

作品の核と安定設定。
bible は初期 3 ファイルから、作品の成長に応じて分割・追加してよい（例: `character-sheets.md`, `dialogue-bible.md`, `system-bible.md`）。
arcs も `arc-01.md` だけで止まらず、設計シートやキャラ出現マップなどを追加してよい。
成長の判断基準と手順は `.claude/rules/file-growth.md` を参照。

### Planning / Meso 層

- `packets/`

Arc を数話単位の実装可能な粒度に落とす場所。
`exploring/` → `scoped/` → `frozen/` の 3 ステージが基本。ドラフト中に packet を修正する場合は `drafting/` を追加してよい。

### Execution / Micro 層

- `scenes/`
- `drafts/`

局所衝突と本文。
scenes はエピソードに割り当てたら `slotted/` へ、改訂で不要になったら `superseded/` へ移動してよい。

### Feedback / Release 層

- `reviews/`
- `learning/`
- `approved/`
- `published/`

評価し、戻し、公開する場所。
reviews はレビュー手法ごとにテンプレートを増やしてよい（例: typed-review, 3pass-design-review, reader-review-personas）。

`reviews/` はスコア置き場ではなく、`continue / replan / blocked / human_review_required` を判断するための診断置き場です。
`learning/` は読み物ではなく、次 packet / 次 sprint の context に戻す再利用ルール置き場です。

### 運用オプション層

- `actions/`
- `community/`
- `campaigns/`
- `metrics/`
- `queue/`

必須コアではありません。`queue/` は legacy projection です。

## 推奨フロー

1. 大量 input を `story/intake/raw/` に保存する
2. 1 batch ごとに `story/intake/digests/` へ圧縮する
3. digest から `story/seeds/` を作る
4. `reviews/seed-to-macro-template.md` を使って seed の反映先を整理する
5. `story/promises.md`, `bible/world.md`, `bible/characters.md`, `bible/rules.md` で安定設定に収束する
6. `arcs/series-overview.md` で長期変化を切る
7. `arcs/arc-01.md` で今の変化線を scoped にする
8. `packets/exploring/` か `packets/scoped/` で packet を作る
9. `packets/frozen/` に上げる
10. `scenes/` に first episode を書ける scene 群を作る
11. `drafts/` で本文化する
12. `reviews/` で typed review と packet review gate の判断材料を作り、必要なら `story/design-debt.yaml` と `story/canon-patch-proposals/` に返す
13. `learning/` に次 sprint へ持ち越すルールを残す

## どのファイルが何を担うか

- `story/intake/raw/`
  会話ログ、設定投下、断片メモの生データ
- `story/intake/digests/`
  raw を圧縮した batch summary と seed 候補
- `story/promises.md`
  作品の約束。何を絶対に壊してはいけないか
- `story/seeds/*.md`
  digest から切り出した再利用核
- `bible/world.md`
  物語の因果に効く世界制約
- `bible/characters.md`
  主要キャラのドラマ圧
- `bible/rules.md`
  文体、視点、禁則
- `arcs/series-overview.md`
  長期変化の見取り図
- `arcs/arc-01.md`
  今の Arc の骨
- `packets/*.yaml`
  数話単位の実装仕様。v2 starter では `episodes:` に各話の role / purpose / loss / gain / reveal / hooks / cliffhanger を持つ
- `scenes/*.md`
  scene card。本文ではない。v2 starter では `cliffhanger / next scene handoff / bridge note / review memo` を持つ
- `drafts/*.md`
  本文
- `reviews/*.md`
  typed review
- `reviews/typed-review-template.md`
  draft / packet 診断の base template
- `reviews/bridge-review-template.md`
  packet 切り替わりの接続監査 template
- `reviews/seed-to-macro-template.md`
  seed を story / bible / arcs / debt / patch のどこへ返すか整理する template
- `story/canon-patch-proposals/*.yaml`
  Canon 修正案

## Packet の使い分け

- `packets/exploring/`
  まだ論点が荒い段階。entry / exit や disclose / withhold の仮説を立てる
- `packets/scoped/`
  役割、入口、出口、依存関係が見えている段階
- `packets/frozen/`
  scene 担当に渡しても「この話は何のためにあるのか」と聞かれない段階

原則:

- Arc は `scoped` で Packet 開始
- Packet は `frozen` で Scene 開始
- packet starter v2 では `episodes:` を空配列で放置せず、各話の役割と handoff まで埋める

## 執筆開始ライン

少なくともここまで揃っていれば本文を書き始めてよいです。

- `CLAUDE.md` がある
- `story/promises.md` に作品約束がある
- `bible/world.md` に現行 Arc に必要な制約がある
- `bible/characters.md` に主要キャラのドラマ情報がある
- `bible/rules.md` に文体ルールがある
- `arcs/arc-01.md` がある
- `packets/frozen/` に 1 本ある
- `scenes/` にその Packet の scene 群がある
- 今書く packet / first episode を止める blocker が `story/open-questions.md` に残っていない

注意:
template を配った瞬間には、ここまでは埋まっていません。starter を埋めて初めて開始ラインに乗ります。

## 完了ライン

- `drafts/` に公開対象の draft がある
- `reviews/` に typed review がある
- 必要な Canon 修正が `bible/` に反映されている
- 未反映のものが `story/canon-patch-proposals/` にある
- 長期課題が `story/design-debt.yaml` にある
- `approved/` に承認済み成果物がある
- `published/` に公開物がある

## 具体的な入り方

### ChatGPT / Claude Web で進める

1. 長い input がある場合は先に `story/intake/raw/` へ保存する
2. `prompts/common-preamble.md` を先頭に付ける
3. raw を圧縮して `story/intake/digests/` を作る
4. `prompts/promises.md` から順番に使う
5. 出力を対象ファイルへそのまま貼る
6. `reviews/seed-to-macro-template.md` で反映先を整理する
7. `packet-scoped.md` で packet を作り、`packet-freeze-check.md` で frozen 判定をかける
8. `scene-batch.md` で first episode の scene 群を作る
9. draft 後は `reviews/typed-review-template.md` をベースに typed review を作る
10. packet 切り替わり時は `reviews/bridge-review-template.md` で exit / entry の接続を監査する

### Codex / Claude Code で進める

1. この `README.md` と `CLAUDE.md` を読ませる
2. 大量 input がある場合は `story/intake/raw/` と `story/intake/digests/` から始めさせる
3. 対象 starter を直接埋めさせる
4. 必要なら `prompts/` を素材として流用する
5. `.claude/skills/` が使える環境では `/pitch`, `/draft`, `/critic`, `/review-meeting`, `/retro-meeting` を補助に使う

## Skill 運用メモ

`.claude/skills/` は episode-first の単発運用より、packet-first の loop で使う方が安定します。

- `/draft`: frozen packet と scene 群に加え、直近 `learning/` の carryover を見る
- `/critic`: hard gate, issue level, return target, expected delta を残す
- `/review-meeting`: packet review gate の判断材料を作る。packet 切り替わりでは bridge review を併用する
- `/retro-meeting`: learning を次 sprint に返す

## 関連ファイル

- 制作契約: `CLAUDE.md`
- intake ガイド: `story/intake/README.md`
- prompt 集: `prompts/README.md`
- review 運用: `reviews/README.md`
