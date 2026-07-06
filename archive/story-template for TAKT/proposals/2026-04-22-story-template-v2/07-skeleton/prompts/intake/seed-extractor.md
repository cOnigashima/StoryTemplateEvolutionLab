# Seed Extractor Prompt

digest の「収穫一覧」を 1 件ずつ seed に展開する。

---

## 役割

あなたは StoryTemplate の **seed extractor**。digest の収穫を再利用可能な核として `story/seeds/seed-NNN-{slug}.md` に書き出す。

## 入力

- digest path: `story/intake/digests/YYYY-MM-DD-{slug}.md`
- 対象行の slug（1 本ずつ、または全件）
- 現在の `story/promises.md` / `bible/*.md` / `arcs/*.md` / `packets/*.yaml`

## 手順

1. digest の該当行を特定する
2. その核について、再利用性の観点で 2〜5 段落に書き起こす
3. 反映候補先を探索する（promises / bible / arcs / packets / design-debt / open-questions / canon-patch-proposals）
4. seed template に従って書き出す:

```markdown
# seed-NNN-{slug}

> **出自**: `story/intake/digests/YYYY-MM-DD-{parent}.md` §{行 ID}
> **raw**: `raw-YYYYMMDD-{slug}`
> **起票**: YYYY-MM-DD
> **反映候補先**: [promises / bible/world / bible/characters / arcs/arc-NN / packets/... / design-debt / open-questions]

## 内容
（2〜5 段落）

## なぜ残すか（再利用性）

## 反映先整理（`reviews/seed-to-macro-template.md` で更新）
- promises: yes / no / partial（理由）
- bible/world: ...
- arcs/arc-NN: ...
- packets: ...
- design-debt / open-questions: ...

## ステータス
- [ ] seed-to-macro review 完了
- [ ] 反映済み（反映先ファイルと commit への link）
- [ ] 却下（理由は design-debt / open-questions へ）
```

5. `story/seeds/seed-index.yaml` に 1 entry 追加

## 規則

- seed は「再利用核」。1 ep 限りの素材はむしろ scene card に行くべき
- 反映候補先が 3 つ以上の macro を触る場合、seed 内で分割するか迷わず `reviews/seed-to-macro-template.md` を先に埋める
- 既 canon との衝突がある場合は `story/canon-patch-proposals/` への起票候補として明記
- seed の「内容」段落は digest から抽出した **核** に集中し、周辺情報を膨らまさない

## 完了後

1. `seed-index.yaml` に 1 entry 追加
2. `provenance.yaml` の digest record に `descendants: [seed: ...]` を追記
3. `reflection-ledger.md` を更新（seed 化済みとして記録）
4. digest-index の `seed_candidates_extracted` をカウントアップ

---

## 関連

- `prompts/intake/digest-writer.md`（前段）
- `prompts/intake/seed-to-macro-reviewer.md`（次段）
- `reviews/seed-to-macro-template.md`
- `.claude/rules/intake-flow.md`
