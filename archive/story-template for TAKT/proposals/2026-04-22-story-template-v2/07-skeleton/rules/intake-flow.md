# Intake Flow Rule

raw / digest / seed / canon の反映フローを管理する規範。詳細設計は `proposals/2026-04-22-story-template-v2/03-intake-flow.md` を参照。

---

## 1. Layer 定義

- **Layer A (raw)**: `story/intake/raw/` — 原文を失わない
- **Layer B (digest)**: `story/intake/digests/` — batch 圧縮
- **Layer C (seed)**: `story/seeds/` — 再利用核
- **Layer D (canon)**: `story/promises.md`, `bible/`, `arcs/`, `packets/`
- **Layer E (reflection)**: `story/intake/reflection-ledger.md` — 反映漏れを追う

---

## 2. MUST

1. raw を直接 bible / arcs / packets に書かない
2. raw 投入時に `raw-index.yaml` に 1 エントリ追加、`provenance.yaml` に 1 レコード追加
3. digest 完了時に `digest-index.yaml` 追加、reflection-ledger 更新
4. seed 起票時に `seed-index.yaml` 追加、reflection-ledger 更新
5. canon 反映時に `provenance.descendants` を更新、reflection-ledger を done に
6. Pro 等外部環境で研究する場合は `prompts/intake/pro-research-brief.md` を起点にする

---

## 3. 禁止

1. raw を要約せずに seed に昇格させる
2. digest 化せずに seed を起票する（raw が失われる）
3. seed-to-macro review なしで canon（bible/arcs/packets）を書き換える
4. provenance.yaml / reflection-ledger を更新せず反映完了とする
5. reflection-ledger の「未反映」行を 30 日以上放置（30 日で design-debt に移送する）

---

## 4. 起動 skill / prompt

- `/pitch` — seed から packet 材料を作る
- `/seed-to-macro` — seed の昇格判定を走らせる（新設）
- `prompts/intake/*.md` — raw-submission / digest-writer / seed-extractor / seed-to-macro-reviewer / pro-research-brief

---

## 5. 更新リズム

| タイミング | アクション |
|---|---|
| 入力発生時 | raw 投入 + index 更新 |
| 数時間以内 | digest 化 |
| 1 日以内 | seed 候補切り出し |
| 2-3 日以内 | seed-to-macro review |
| 週次 | reflection-ledger 棚卸し |
| Arc 完了時 | provenance の consolidate |

---

## 6. 関連

- `.claude/rules/story-os-boundaries.md`（入口定義）
- `.claude/rules/learning-capture.md`（learning との役割分担）
- `proposals/2026-04-22-story-template-v2/03-intake-flow.md`（設計全体）
