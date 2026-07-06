# Vocabulary Lint Rule

ユビキタス言語の一貫性を守る。詳細は `proposals/2026-04-22-story-template-v2/02-domain-map.md` 参照。

---

## 1. 正式語 / 実装語

- 正式語: 作品約束 / Canon / Bible / Arc / 章束（packet） / Scene / Seed / Episode / Draft / Prose
- 実装語: promise / canon / bible / arc / packet / scene / seed / ep / draft / prose

日本語文中では原則 **正式語**、ファイル名・yaml key・英語文中では実装語を使う。

---

## 2. 禁止語

| 禁止語 | 代替 | 理由 |
|---|---|---|
| bundle | packet / 章束 | story-os-boundaries |
| 章（単独） | arc / packet / ep（文脈で選ぶ） | 曖昧 |
| review（単独） | typed review / bridge review / continuity review / persona review / approval review | story-os-boundaries |
| backlog | story/seeds / story/intake | legacy |
| queue（正本として） | projection 扱いのみ | story-os-boundaries |
| chapter | arc（単位）/ ep（章節）で文脈明示 | 曖昧 |

---

## 3. 混同注意語（定義違い）

- Canon ≠ Bible（Canon ⊇ Bible）
- Promise ≠ Canon（Promise は Canon より上位）
- Plot ≠ Story（Plot = 因果、Story = 出来事列）
- Arc ≠ Packet（Arc ⊇ Packet）
- Scene ≠ Beat（Scene ⊇ Beat）
- Draft ≠ Prose（Draft はファイル、Prose は記述粒度）
- Seed ≠ Digest（Seed は再利用核、Digest は raw 要約）
- Motif ≠ Foreshadowing（overlap はあるが同義ではない）
- Cadence ≠ Rhythm（Cadence ⊃ Rhythm、粒度違い）

---

## 4. lint チェックリスト（review self-check）

- [ ] `review` が種別前置されているか
- [ ] `bundle` `backlog` `chapter` を使っていないか
- [ ] Canon / Bible / Promise の階層が混同されていないか
- [ ] Packet と Arc を互換に使っていないか
- [ ] Scene と Beat を互換に使っていないか
- [ ] Seed と Digest を互換に使っていないか

---

## 5. 新語追加手順

1. `bible/glossary.md` に定義を追記
2. `02-domain-map.md`（本提案）または後継の `bible/glossary.md` §1 に一行要旨を追加
3. 既存語と衝突する場合は `consolidate-memory` skill で整理

---

## 6. 関連

- `bible/glossary.md`（ドメイン語の正本）
- `.claude/rules/story-os-boundaries.md`
- `proposals/2026-04-22-story-template-v2/02-domain-map.md`（本ファイル下敷き）
