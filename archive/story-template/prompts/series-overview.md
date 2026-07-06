# Prompt: arcs/series-overview.md

以下の素材から `arcs/series-overview.md` を作成してください。

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

要件:
- 出力は Markdown のみ
- Arc 1 は詳細化前提、Arc 2 は中密度、Arc 3 以降は骨子だけでよい
- Arc の分割基準は、belief / 敵対圧 / disclose-withhold / 到達地点 / packet 設計原理 の変化を優先する
- Arc 数は 2〜4 本
- 断定できないものは「未決定」

出力フォーマット:

```md
# シリーズ概観

## 全体構成

| Arc | Episodes | 中心テーマ | Packet |
|---|---|---|---|
| 1 | ep01-06 | 未決定 | packet-001, packet-002 |
| 2 | ep07-12 | 未決定 | packet-003, packet-004 |

## Arc の密度ルール
- Arc 1 は詳細に作る
- Arc 2 は中密度で作る
- Arc 3 以降は骨子だけ置く

## 主人公の長期変化
- 開始: 未決定
- 中盤: 未決定
- 終了: 未決定

## 重要な問い
- 未決定
- 未決定

## 先に置く伏線
- 未決定
- 未決定

## 開示ロードマップ
- Arc 1 で明かすこと: 未決定
- Arc 2 で明かすこと: 未決定
- Arc 3 以降へ持ち越すこと: 未決定

## 未決定
- 未決定
```
