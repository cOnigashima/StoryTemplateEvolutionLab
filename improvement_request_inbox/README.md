# improvement_request_inbox/ — StoryTemplate 自身への改善 input 受付

> 旧名 `inbox/`（2026-07-06 改名: 作品側 inbox 概念との混同を防ぐため）

> **役割**: StoryTemplateEvolution リポジトリ自体への **改善要望 / 議論ログ / 設計フィードバック** を raw のまま受け付ける場所。
> **対象**: template の改善議論。**各作品の raw 受付とは別物**（作品固有は作品側へ）。

---

## 何を入れる場所か

- StoryTemplate 改善のための ChatGPT chat ログ
- v5 / v6 への改善案断片
- 作品制作中に出た「StoryTemplate のここが使いにくい」というフィードバック
- **作品 retro（works/{slug}/runtime/logs/learning/）から抽出した汎用知見**
- 学術的な創作論メモ（後に craft/ 昇格を検討）

---

## 何を入れない

- ✗ 各作品の raw（→ 該当 work の `works/{slug}/inbox/` に）
- ✗ 各作品の bible 改訂（→ 作品側の update proposal 経由、`current/adapter/intake_adapter.md`）
- ✗ 機密情報（git public 化前提、commit する前に確認）

---

## ファイル命名

```
improvement_request_inbox/{YYYY-MM-DD}_{slug}.md
```

---

## 配下構造（任意）

肥大したらサブ分割可:

```
improvement_request_inbox/
├── README.md（本ファイル）
├── 2026-04-30_v4-feedback.md
├── 2026-05-15_craft-library-ideas.md
└── archived/    ← 古いものを退避（任意）
```

---

## 昇格フロー

raw が current に反映されるまで:

```
improvement_request_inbox/{date}_{slug}.md
        ↓ 整理 / 議論
proposal/{new-date}-{slug}/  に新規提案として起票（軽微なら直接 Patch）
        ↓ author 採用判断
[ADOPTED]: current/ に反映 → 決着を current/learning/{date}-{slug}.md に記録
[REJECTED]: archive/proposal/ に下ろす（棄却理由も learning に残してよい）
```

---

## 関連参照

- リポジトリ全体: `../README.md`
- 提案 status: `../proposal/README.md`
- 開発 rule: `../.claude/CLAUDE.md`
- 決着記録: `../current/learning/README.md`
