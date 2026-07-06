# inbox/ — StoryTemplate 自身への改善 input 受付

> **役割**: StoryTemplateEvolution リポジトリ自体への **改善要望 / 議論ログ / 設計フィードバック** を raw のまま受け付ける場所。
> **対象**: template の改善議論。各作品（works/{slug}/inbox/）とは別物。

---

## 何を入れる場所か

- StoryTemplate 改善のための ChatGPT chat ログ
- v5 / v6 への改善案断片
- 作品制作中に出た「StoryTemplate のここが使いにくい」というフィードバック
- 学術的な創作論メモ（後に craft/ 昇格を検討）

---

## 何を入れない

- ✗ 各作品の raw（→ 該当 work の `works/{slug}/inbox/` に）
- ✗ 各作品の bible 改訂（→ `works/{slug}/synthesis/update_proposals/` 経由）
- ✗ 機密情報（git public 化前提、commit する前に確認）

---

## ファイル命名

```
inbox/{YYYY-MM-DD}_{slug}.md
```

---

## 配下構造（任意）

肥大したらサブ分割可:

```
inbox/
├── README.md（本ファイル）
├── 2026-04-30_v4-feedback.md
├── 2026-05-15_craft-library-ideas.md
└── archived/    ← 古いものを退避（任意）
```

---

## inbox → proposal への昇格

inbox の raw が proposal に昇格する流れ:

```
inbox/{date}_{slug}.md
        ↓ 整理 / 議論
proposal/{new-date}-{slug}/  に新規提案として起票
        ↓ author 採用判断
[ADOPTED]: current/ に反映
[REJECTED]: archive/proposal/ に下ろす
```

---

## 関連参照

- リポジトリ全体: `../README.md`
- 提案 status: `../proposal/README.md`
- 開発 rule: `../.claude/CLAUDE.md`
