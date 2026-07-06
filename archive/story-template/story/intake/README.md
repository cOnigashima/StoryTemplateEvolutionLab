# Input Intake

このディレクトリは、Story OS の canon へ昇格する前の source layer です。
長い会話ログや大量の設定投下を、そのまま `bible/` や `arcs/` に入れないために使います。

runtime は `story/intake/` を直接読みません。
ここは人間と執筆エージェントのための保管・圧縮レイヤです。

## 役割

- `raw/`
  会話ログ、設定投下、引用、断片メモの生データを置く
- `digests/`
  raw を 1 batch ごとに圧縮した summary を置く
- `story/seeds/`
  digests から切り出した再利用核を置く
- `story/promises.md`, `bible/*`, `arcs/*`
  seed からさらに昇格した安定 canon を置く

## 使い分け

### raw に置くもの

- 長い会話ログ
- まだ矛盾や重複を含む設定投下
- 一度に大量投入された敵案、世界観案、構成案
- 後で provenance が必要になりそうな原文

### digests に置くもの

- raw を 1 batch 単位で圧縮した summary
- その batch で強く出た核
- 今は固定しないこと
- 既存 canon と衝突しそうな点
- seed 候補
- 反映候補の行き先

### seeds に置くもの

- digests から切り出した premise
- 再利用したい desire / tension / reveal candidate
- 行き先未定だが作品に効く核

## 推奨フロー

1. 大量 input を `raw/` に保存する
2. 1 batch ごとに `digests/` へ圧縮する
3. digest から `story/seeds/` を作る
4. `reviews/seed-to-macro-template.md` で反映先を整理する
5. seed から必要最小限だけ `promises / bible / arcs` へ昇格する
6. 実装が見えたものだけ `packets/` へ落とす

## 大事なルール

- 生ログをいきなり `bible/*` に入れない
- `bible/*` は索引と安定設定だけにする
- raw は削らず、digest と seed で圧縮していく
- prompt context に毎回 raw 全部を読ませる運用はしない
- `story/seeds/` は raw input の倉庫ではなく、圧縮済みの再利用核に保つ

## ファイル名の目安

- raw:
  `20260418-batch-01-user-input.md`
- digest:
  `digest-20260418-batch-01.md`

## 補足

すべての作品が最初から `story/intake/` を必要とするわけではありません。
ただし、別所で大量に育った設定群を template へ統合するときは、
`story/intake/` を経由した方が canon を太らせずに済みます。
