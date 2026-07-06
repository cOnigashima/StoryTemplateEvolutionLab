# Story Template Intake Integration Proposal

- date: 2026-04-18
- scope:
  - `story-template/`
  - `works/one-man-statefall/`
  - `works/designer-reborn/`
  - `works/villainess-coc-survival-with-cheating/`
- purpose: 大量の設定・会話ログ・断片メモを `story-template` にどう受け入れ、どこまで反映し切るかを定義する

## 結論

`story-template` の次の改善軸は `factory-platform` との整合ではない。
主題は **input intake の公式化** である。

いまの template は `story/seeds/` から先の Story OS には強いが、
その手前にある

- 長い会話ログ
- 大量の設定投下
- 断片的な敵案、世界観案、構成案
- まだ矛盾や重複を含む raw input

を受け止める層がない。

したがって、あるべき姿は

`raw input -> digest -> seed -> canon -> packet`

を template 本体で明示し、
「全部を canon に入れる」のではなく、
**各 input に行き先を与えて取りこぼさない** ことを反映完了の定義にすること。

## 1. いま何が起きているか

## 1-1. `story-template` は seed 以降の OS

`story-template/README.md` と `story-template/CLAUDE.md` は

- `Promise -> Arc -> Packet -> Scene -> Draft`
- `Review -> Canon reverse flow`

を明確に持っている。

一方で入口は実質 `story/seeds/` から始まっており、
巨大入力をそのまま受ける source layer はまだない。

## 1-2. `one-man-statefall` は intake layer を先に必要とした

`works/one-man-statefall/learning/storytemplate-init-intake-20260405.md` と
`works/one-man-statefall/story/intake/README.md` は、
template の弱点をかなりはっきり言っている。

要点は次の通り。

- `story/seeds/` は raw input の置き場ではない
- raw を毎回全部 prompt context に載せる運用はしない
- 先に `story/intake/raw/` と `story/intake/digests/` を作る
- digest から seed を作り、seed から canon へ昇格する

つまり `one-man-statefall` が解いたのは automation 以前に
**入力を Story OS に変換する前処理問題** だった。

## 1-3. `designer-reborn` は seed 以降の反映整理をすでに持っている

`works/designer-reborn/reviews/seed-to-macro-20260402013243.md` は、
1 つの seed を

- `story/promises.md`
- `bible/world.md`
- `bible/characters.md`
- `arcs/`
- `story/design-debt.yaml`

のどこへ返すかを layer ごとに判定している。

これは `story-template` に今いちばん足りない
**反映先の仕分けプロトコル** の原型になっている。

## 1-4. `villainess` は reverse flow の後半を強くしている

`works/villainess-coc-survival-with-cheating/` では、
draft 後の review が

- typed review
- learning
- canon patch
- bible / scene 修正

へ返っている。

これは downstream の reverse flow として重要だが、
今回の主題はその手前、
**raw input をどう seed / canon に持ち上げるか** である。

## 2. 反映し切るとは何か

「反映し切る」を
「全部 bible に書く」と定義すると失敗する。

正しい定義は次。

> 受け入れた input の各要素に、現在の最適な行き先が割り当てられている状態

この行き先は canon だけではない。

- stable promise なら `story/promises.md`
- stable world / character / rule なら `bible/*`
- 長期変化線なら `arcs/*`
- 近接実装の束なら `packets/*`
- まだ再利用したい核なら `story/seeds/`
- 未確定論点なら `story/open-questions.md`
- 長生きする構造問題なら `story/design-debt.yaml`
- canon 差分案なら `story/canon-patch-proposals/`
- まだ source として保持すべきなら `story/intake/raw/` または `story/intake/digests/`

つまり、**昇格** と **保留** と **差分提案** を明示できれば、
input は取りこぼされていない。

## 3. あるべき StoryTemplate の層

core template では、少なくとも次の 5 層を明示した方がよい。

### A. source intake layer

- `story/intake/raw/`
- `story/intake/digests/`

役割:

- raw input の保存
- batch ごとの圧縮
- provenance の保持

ここは runtime が直接読まない。
人間と執筆エージェントの source layer。

### B. reusable seed layer

- `story/seeds/`

役割:

- digest から切り出した再利用単位の保持
- 行き先未定だが作品に効く核の保管

seed は raw の保管庫ではなく、圧縮された再利用単位。

### C. stable canon layer

- `story/promises.md`
- `bible/world.md`
- `bible/characters.md`
- `bible/rules.md`
- `arcs/`

役割:

- 次の 1〜2 packet の因果に効く安定設定の索引

### D. live implementation layer

- `packets/`
- `scenes/`
- `drafts/`

役割:

- canon を実装可能単位に落とす

### E. reflection / reverse flow layer

- `reviews/`
- `learning/`
- `story/open-questions.md`
- `story/design-debt.yaml`
- `story/canon-patch-proposals/`

役割:

- intake の未確定点と、draft 後の差分を上流へ返す

## 4. intake の公式フロー

`story-template` の入口を次の順で定義するのがよい。

1. raw batch を `story/intake/raw/` に保存する
2. batch digest を `story/intake/digests/` に作る
3. digest から reusable seed を `story/seeds/` に切る
4. seed ごとに `seed-to-macro` 判定を行う
5. 必要最小限だけ `promises / bible / arcs` に昇格する
6. 実装が見えたものだけ `packets/` に落とす
7. draft / review 後の差分を reverse flow で返す

重要なのは、
`raw -> digest -> seed`
の圧縮と、
`seed -> macro`
の反映判定を分けること。

## 5. 受け入れる方法の具体化

大量 input を受けるとき、template 側は 1 batch ごとに最低限これを持つべき。

### raw

raw file には以下があればよい。

- batch id
- 日付
- 入力の原文
- 必要なら source note

raw はきれいにしない。
重複や矛盾を含んでよい。

### digest

digest は raw を圧縮し、少なくとも次を持つべき。

- この batch で強く出た核
- 今は固定しないもの
- 既存 canon との衝突候補
- seed 候補
- 反映候補の行き先

要するに digest は要約ではなく
**昇格判定の前室** であるべき。

### seed

seed は 1 個の premise / desire / tension / reveal candidate など、
再利用できる単位へ切る。

seed に持たせたいのは

- 何が作品に効くか
- どの layer に上がりうるか
- まだ何が未決定か

であって、raw の全文ではない。

## 6. 反映し切る方法の具体化

ここがいちばん重要。

seed または digest を処理したら、
最後に必ず **reflection ledger** を残す。

最低限の項目は次でよい。

| item | decision | target | note |
|---|---|---|---|
| A | promote | `story/promises.md` | 作品約束に効く |
| B | promote | `bible/world.md` | stable world rule |
| C | hold | `story/open-questions.md` | 未確定なので保留 |
| D | patch | `story/canon-patch-proposals/...` | 既存 canon の差分提案 |
| E | keep | `story/intake/digests/...` | 今は seed に切らない |

この ledger があれば、
「まだ canon に入っていない」ことと
「取りこぼしている」ことを分離できる。

## 7. template に入れるべき review / prompt

今回の主題では、review は draft の後だけでなく、
input を上流へ持ち上げるときにも必要になる。

core template に最低限ほしいのは次。

### 7-1. intake README

- `story/intake/README.md`
- raw / digest / seed / canon の違い
- 推奨フロー

### 7-2. intake digest template

- raw batch を digest に圧縮するひな型
- fixed / unresolved / candidate target を書ける形

### 7-3. seed-to-macro review template

`designer-reborn` で実質使われているものを一般化し、

- story
- world
- characters
- rules
- arcs
- packet
- open questions
- design debt
- canon patch

のどこに返すかを layer 別に判定する template を持つ。

### 7-4. provenance / index の最小帳簿

これは optional だが価値が高い。

候補:

- `story/intake/index.yaml`

最低限の追跡項目:

- batch id
- raw file
- digest file
- derived seeds
- reflection review
- current status

## 8. core template と optional module の境界

ここを混ぜると重くなる。

### core に入れるべきもの

- `story/intake/raw/`
- `story/intake/digests/`
- intake README
- digest template
- seed-to-macro review template
- raw -> digest -> seed -> canon の説明

### optional に切るべきもの

- automation queue
- `tasks/`
- workflow runner
- telemetry
- platform 固有 runtime

理由は単純で、
input intake はほぼ全作品に効くが、
automation runtime は作品ごとの差が大きいから。

## 9. この設計で何がよくなるか

### 9-1. seed の前が整理される

今までは `story/seeds/` が

- 発想の置き場
- 大量 input の避難先
- 再利用核の保管庫

を兼ねやすかった。

intake layer を切ると、
`story/seeds/` は再利用核に専念できる。

### 9-2. canon が太りすぎない

大量設定を全部 `bible/*` に入れないで済む。
stable canon だけを index として保てる。

### 9-3. input の取りこぼしと未昇格を分けられる

ledger があれば、
「まだ上げていない」だけなのか、
「どこにも返していない」のかを区別できる。

### 9-4. automation と切り離しても成立する

`one-man-statefall` の学びを使いつつ、
automation 固有の runtime contract は core へ持ち込まずに済む。

## 10. 次の具体アクション

template 改修に進むなら順番はこれがよい。

1. `story-template/story/intake/` を新設する
2. `story-template/README.md` と `CLAUDE.md` に intake layer を追記する
3. digest template を追加する
4. `reviews/seed-to-macro-template.md` を追加する
5. `story/seeds/` の説明を「巨大入力の置き場」から明確に切り離す

## 結論

今回 `story-template` に足すべきなのは、
新しい platform contract ではない。

足すべきなのは

- 大量 input を置く場所
- それを圧縮する場所
- seed へ切る方法
- canon への反映先を仕分ける方法
- 反映保留を取りこぼしと混同しない ledger

である。

言い換えると、
`story-template` の次の一手は
`story/seeds/` を増強することではなく、
**seed の手前に公式 intake layer を生やすこと** である。
