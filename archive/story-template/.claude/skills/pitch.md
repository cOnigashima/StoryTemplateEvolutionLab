# /pitch

Seed-first で次の着想や packet 材料を作る。

## 入力

- raw notes または「次に何を考えるか」という自然言語指示
- 必要に応じて `story/seeds/`, `story/promises.md`, `bible/`, `arcs/`, `packets/`

## 手順

1. `story/promises.md`, `bible/`, `arcs/`, 直近の `packets/` を読んで現在地を把握する
2. まだ行き先未定なら `story/seeds/` に seed を作る
3. 既存 seed を束ねられるなら、`promises / bible / arc / packet` のどこへ送るべきかを示す
4. `backlog/` ではなく `story/seeds/` を入口正本として扱う

## 出力フォーマット

seed を作る場合は以下:

```markdown
# Seed: [一言タイトル]

## 思いつき
- 何が浮かんだか:
- どの感情がいいと思ったか:
- どの絵が見えたか:

## まだ荒い仮説
- 主人公:
- 対立:
- 舞台:
- フック:

## 関連しそうな先
- related arcs:
- related packets:
- promote to: macro | meso | 未決定

## 未決定
- 
```

## 保存先

`story/seeds/seed-YYYYMMDD-HHMMSS.md`
