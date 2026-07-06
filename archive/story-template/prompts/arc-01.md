# Prompt: arcs/arc-01.md

以下の素材から `arcs/arc-01.md` を作成してください。

[EXISTING PROMISES]
<<<PROMISES_MD>>>
ここに story/promises.md を貼る
<<<END_PROMISES_MD>>>

[EXISTING WORLD]
<<<WORLD_MD>>>
ここに bible/world.md を貼る
<<<END_WORLD_MD>>>

[EXISTING CHARACTERS]
<<<CHARACTERS_MD>>>
ここに bible/characters.md を貼る
<<<END_CHARACTERS_MD>>>

[EXISTING SERIES OVERVIEW]
<<<SERIES_OVERVIEW_MD>>>
ここに arcs/series-overview.md を貼る
<<<END_SERIES_OVERVIEW_MD>>>

要件:
- 出力は Markdown のみ
- Arc 1 だけを詳細化する
- ep01-06 程度を想定し、packet-001 と packet-002 に割れる粒度にする
- `Purpose` には Arc の終点と次 Arc へ渡すものを含める
- `Main Turn` には Loss / Gain / reversal を入れる
- `Reader Hooks` は ep01-ep03 を必ず書く
- scene 単位の演出には降りない
- 断定できないものは「未決定」

出力フォーマット:

```md
# Arc 1: [タイトル]

## メタ情報
- ID: arc-01
- Span: ep01-06
- ステータス: scoped

## Purpose
- この Arc で果たすこと: 未決定
- この Arc の終点: 未決定
- 次 Arc へ渡すもの: 未決定

## Main Turn
- 失うもの: 未決定
- 得るもの: 未決定
- 反転点: 未決定

## 主人公の Span
- 開始状態: 未決定
- 終了状態: 未決定

## Reader Hooks
- ep01: 未決定
- ep02: 未決定
- ep03: 未決定

## Packet 構成
- packet-001: 未決定
- packet-002: 未決定

## 依存関係
- depends_on_world:
  - 未決定
- depends_on_characters:
  - 未決定
- depends_on_rules:
  - 未決定

## 未決定
- blockers:
  - 未決定
- non_blockers:
  - 未決定
```
