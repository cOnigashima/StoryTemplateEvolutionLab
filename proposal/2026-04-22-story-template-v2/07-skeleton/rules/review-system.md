# Review System Rule

review 実施時の規範。詳細設計は `proposals/2026-04-22-story-template-v2/04-review-system.md` を参照。

---

## 1. Review Matrix

| 種別 | タイミング | template |
|---|---|---|
| Typed | draft 完了〜approval 前 | `reviews/typed-review-template.md` |
| Bridge | packet 切替時 | `reviews/bridge-review-template.md` |
| Continuity | 定期 / packet 完了時 | `reviews/continuity-review-template.md` |
| Persona (A/B/C) | approval 前 | `reviews/persona-review-template.md` |
| Approval | 公開直前 | `reviews/approval-template.md` |
| Seed-to-Macro | seed 起票後 | `reviews/seed-to-macro-template.md` |
| Packet Freeze | scoped → frozen 移行時 | `reviews/packet-freeze-template.md` |

---

## 2. MUST

1. 「該当なし」判定は **grep 結果の併記** を必須とする（記憶・meta 判定禁止）
2. `review` 単独語を使わず、種別を前置する（typed review / bridge review 等）
3. typed review には必ず:
   - PART A Hard Gate（因果 weight7 / 話者 weight3 / 文法 weight4 / 約束侵犯 weight5）
   - PART B Packet Fulfillment Audit（Gate B 4 block）
   - PART F Upstream Returns（issue level / return target / next job / expected delta）
   - PART G 25 項目 rubric 採点
4. approval review には kakuyomu-policy チェック項目を含める
5. persona review は A（没入）/ B（構造）/ C（離脱）の 3 本揃える

---

## 3. grep 検証ルール（villainess-coc §8.1 移植）

- canon motif / withhold / disclose の充足判定は draft 本文への grep を一次根拠
- grep キーワードは作品固有 `.claude/rules/monitoring-dictionary.md` または `craft/motif-operations.md` から採用
- hit count と対象行番号を review に記録
- prose / meta を分離（`---` より前=meta、後=prose）。withhold 違反判定対象は prose のみ

---

## 4. Upstream Returns 宛先

| 問題の性質 | 差し戻し先 |
|---|---|
| prose 問題 | `scenes/` または `drafts/` |
| hook / pacing | `packets/` |
| 動機 / 関係性 | `bible/characters.md` |
| 開示順 / 反転点 | `arcs/` |
| 作品約束ズレ | `story/promises.md` |
| 長生きする構造問題 | `story/design-debt.yaml` |
| 未確定設定 | `story/canon-patch-proposals/` |
| packet 切替齟齬 | bridge-review 実施 → `packets/` |

---

## 5. 起動 skill

- `/critic` — typed / continuity review
- `/critic-bridge` — bridge review（新設）
- `/audience-review` — persona A/B/C（新設）
- `/release` — approval review
- `/seed-to-macro` — seed 昇格判定（新設）
- `/freeze-review` — packet freeze review（新設）

---

## 6. 関連

- `.claude/rules/drafter-preflight.md`（drafter の Gate 0/A/C、multi-pass self-review）
- `craft/rubric.md`（25 項目の正本）
- `craft/reader-personas.md`（persona 定義）
- `craft/motif-operations.md`（generic motif grep ガイド）
- `proposals/2026-04-22-story-template-v2/04-review-system.md`（設計全体）
