# Pro 調査指示書テンプレート

ChatGPT Pro / 別 Claude / その他の深い調査環境に投げる時の **事前準備 + 調査指示** テンプレート。know_how_explore `2026-04-18_ChatGPT_Pro_調査プロンプト集.md` を下敷きに本 template 用に整理。

---

## メタ情報（記入）

- 作品: {work slug}
- 対象: {arc / packet / 概念}（複数可）
- 日付: YYYY-MM-DD
- 調査主体: ChatGPT Pro / Claude / 他
- 期限: N 時間以内 / N 日以内

---

## 5 つの事前決定（必須）

### 1. テーマ境界

何を調べるか、1 行で。境界外は触らない。

> 例: 「arc-02 の魔法系再設計、ただし既公開 ep01-ep14 と矛盾しない範囲で」

### 2. レイヤ

Promise / Canon（Bible / Arc / Packet）のどこへ反映するか。

> 例: 「主に bible/world.md、派生で arcs/arc-02.md」

### 3. Source 強度

- [ ] 引用必須（既存研究・小説からの参照を求める）
- [ ] 合成可（既存論点の組み合わせ）
- [ ] ブレスト可（新規発想）

### 4. 成果物形式

- [ ] raw にそのまま保存する素材（長文・会話ログ）
- [ ] digest 相当の圧縮済み要約
- [ ] seed 候補一覧（すぐ seed 化できるユニット）

### 5. 深さ

- [ ] 広く浅く（20 topic 表層）
- [ ] 狭く深く（3 topic 深堀り）

---

## 既 canon 抜粋（衝突検出の基礎）

（`story/promises.md` / `bible/*.md` / `arcs/*.md` の該当セクションを該当 path 付きでコピペ）

```
# story/promises.md §...
...

# bible/world.md §...
...

# arcs/arc-NN.md §...
...
```

---

## 調査タスク

1. {task-1}
2. {task-2}
3. {task-3}

---

## 出力規則

出力は以下のラベルを付けた段落集合にする:

- `[FACT]` — 出典可能な事実（ソース明記）
- `[SPECULATION]` — 推測
- `[COLLISION]` — 既 canon との衝突候補（該当箇所引用）
- `[CORE]` — 使えそうな核（seed 候補）
- `[QUESTION]` — 回収すべき問い

1 つの段落に複数ラベル可。

---

## 終了後（ここからは work 側で行う）

1. 出力を `story/intake/raw/YYYY-MM-DD-{source}-{slug}/` に保存
2. `story/intake/raw-index.yaml` に 1 entry 追加
3. `story/intake/provenance.yaml` に 1 record 追加
4. 数時間以内に `prompts/intake/digest-writer.md` を起動して digest 化

---

## 関連

- `prompts/intake/digest-writer.md`
- `prompts/intake/seed-extractor.md`
- `prompts/intake/seed-to-macro-reviewer.md`
- `.claude/rules/intake-flow.md`
