# 段階移行計画

本提案を実装する順序。Phase 0〜4 で段階的に進める。各 Phase は前 Phase を待たずに **一部試せる** ように設計する。

> **前提**: 本提案は「設計＋骨格＋計画」。実装は本計画に沿って次セッション以降で行う。
>
> **担当**: author（taiji）＋ plotter / critic / drafter agent（既存）＋ 必要に応じて新設 agent。

---

## Phase 0: 下地整理（〜0.5 日）

既存の 2 prior audit（gap-analysis / intake-integration-proposal）の未完タスクと、runtime artifact の隔離を片付ける。

### 作業項目

| # | 作業 | 担当 | 目安 |
|---|---|---|---|
| P0-1 | `packets/exploring/`, `scoped/`, `frozen/` 配下の `packet-template.yaml` を `packets/templates/` に移設 | plotter | 30 分 |
| P0-2 | `actions/`, `campaigns/`, `telemetry/`, `queue/`, `backlog/` を template から削除（deprecated に明示） | author | 30 分 |
| P0-3 | `template.manifest.json` v2 に更新（artifact 区分を明示） | author | 30 分 |
| P0-4 | `CLAUDE.md` の「参照ファイル」セクションに craft/ / intake index / current-focus / review templates（未作成でも参照先として）を追加 | author | 30 分 |
| P0-5 | `.claude/rules/story-os-boundaries.md` に intake / craft / runtime-opt-in の境界を追記 | author | 30 分 |

### 完了条件

- `ls story-template/` で runtime artifacts が消えている（deprecated 除く）
- `packets/exploring|scoped|frozen/` が `.gitkeep` のみ
- `template.manifest.json` v2 が commit されている

---

## Phase 1: Layer 2 Review 系 + rule 追加（〜1 日）

review 体系と review-system rule を template 正典化する。運用はここから始められる。

### 作業項目

| # | 作業 | 担当 | 目安 |
|---|---|---|---|
| P1-1 | `reviews/typed-review-template.md` に PART B（Gate B）と PART G（25 項目 rubric）追加 | critic | 1h |
| P1-2 | `reviews/continuity-review-template.md` 新設（skeleton 展開） | critic | 1h |
| P1-3 | `reviews/persona-review-template.md` 新設 | critic | 30 分 |
| P1-4 | `reviews/approval-template.md` 新設 | editor | 30 分 |
| P1-5 | `reviews/packet-freeze-template.md` 新設 | plotter | 1h |
| P1-6 | `.claude/rules/review-system.md` 新設（skeleton 展開） | author | 30 分 |
| P1-7 | `.claude/rules/vocabulary-lint.md` 新設 | author | 30 分 |
| P1-8 | `.claude/skills/critic-bridge.md`, `audience-review.md`, `freeze-review.md`, `seed-to-macro.md` 新設 | author | 1h |
| P1-9 | `prompts/review/{part-a,part-b,part-c,persona-A,persona-B,persona-C}.md` 移植（know_how_explore + skeleton） | author | 1h |

### 完了条件

- review matrix の 7 種（typed/bridge/continuity/persona/approval/seed-to-macro/packet-freeze）全てにテンプレが揃う
- 25 項目 rubric で 1 本 draft を採点できる
- grep 検証ルールが template 正典になっている

### 早期試行

- Phase 1 完了時点で、works/villainess-coc の最新 draft に template 正典のレビューを当てられるか試す
- うまく運用できれば他 works にも展開

---

## Phase 2: Layer 3 Craft Library 新設（〜2 日）

know_how_explore を template 正典化。

### 作業項目

| # | 作業 | 担当 | 目安 |
|---|---|---|---|
| P2-1 | `craft/` ディレクトリ新設、README 設置 | author | 30 分 |
| P2-2 | `craft/principles.md`, `scene-sequel.md`, `want-need.md`, `scope-management.md`, `beat-sheets.md` 新設（know_how_explore より移植） | author | 3h |
| P2-3 | `craft/foreshadowing.md`, `motif-operations.md`, `rubric.md`, `reader-personas.md` 新設 | author | 2h |
| P2-4 | `craft/cadence.md`, `dialogue-craft.md`, `description-craft.md`, `pov-craft.md`, `reveal-plan.md` 新設 | author | 3h |
| P2-5 | `craft/conflict-design.md`, `character-design.md`, `world-design.md`, `theme-design.md` 新設 | author | 2h |
| P2-6 | `craft/genre-patterns.md`, `editing-craft.md`, `sanderson-laws.md`, `knox-rules.md` 新設 | author | 2h |
| P2-7 | `craft/checklists/*.md`, `craft/worksheets/*.md` 新設 | author | 2h |
| P2-8 | `CLAUDE.md` / `bible/rules.md` から craft/ への参照リンク張り | author | 30 分 |

### 完了条件

- 21 craft ファイル + checklists + worksheets が揃う
- 新人 drafter（別 Claude セッション）が craft だけ読んで Scene/Sequel / Want/Need を実装できるか確認

### 早期試行

- Phase 2 進行中でも個別 craft ファイルから試用可（例: scene-sequel を完成させたら即 review で活用）

---

## Phase 3: Layer 0 Intake 整備（〜1 日）

大量入力の正規フローを正典化。

### 作業項目

| # | 作業 | 担当 | 目安 |
|---|---|---|---|
| P3-1 | `story/intake/raw-index.yaml`, `digest-index.yaml`, `provenance.yaml`, `reflection-ledger.md` 新設（skeleton 展開） | author | 30 分 |
| P3-2 | `story/intake/digests/digest-template.md` 新設 | author | 30 分 |
| P3-3 | `story/seeds/seed-index.yaml`, `seed-template.md` 新設 | author | 30 分 |
| P3-4 | `prompts/intake/{raw-submission, digest-writer, seed-extractor, seed-to-macro-reviewer, pro-research-brief}.md` 新設 | author | 2h |
| P3-5 | `.claude/rules/intake-flow.md` 新設（skeleton 展開） | author | 30 分 |
| P3-6 | `story/intake/README.md` 更新（フロー図・index.yaml 説明） | author | 30 分 |
| P3-7 | `learning/current-focus.yaml` 新設 | author | 15 分 |
| P3-8 | one-man-statefall の intake 実装を反映ベースに、template で実運用を 1 周する（dry-run 相当） | author | 2h |

### 完了条件

- raw-index / digest-index / seed-index / provenance / reflection-ledger が揃う
- Pro で生成した 1 つの素材を raw → digest → seed → canon（または design-debt）まで通せる
- reflection-ledger の「未反映」行が空または理由付きで残っている

### 早期試行

- Phase 3 完了前でも、raw 保存だけは template 動作で即始められる（indexing は後追いで良い）

---

## Phase 4: ドメイン整理・集約・横展開（〜1 日）

- ユビキタス言語マップの `bible/glossary.md` への昇格
- works 側への横展開（template の新ルールを各 works に反映）
- works からの昇格候補の整理

### 作業項目

| # | 作業 | 担当 | 目安 |
|---|---|---|---|
| P4-1 | `02-domain-map.md` を元に `bible/glossary.md` template を完成 | author | 1h |
| P4-2 | works/villainess-coc の `reviewer-gate-b.md`, `monitoring-dictionary.md` 改訂（template 側 rule への参照に） | author | 1h |
| P4-3 | works/one-man-statefall の `learning-loop.md` / `current-focus.yaml` を template 形式に揃える（or 作品固有差分を明示） | author | 1h |
| P4-4 | works/villainess-coc の learning/ 全ログを読み、template 昇格候補を `learning/` 候補として列挙 | critic | 2h |
| P4-5 | consolidate-memory skill で全 learning / review を棚卸し | author | 1h |
| P4-6 | 旧 `reviews/2026-04-18-*.md` の gap-analysis / intake-integration-proposal の消化状況を annotate | author | 30 分 |
| P4-7 | `CLAUDE.md` に v2 完成宣言（「執筆開始ライン」条件更新など） | author | 15 分 |

### 完了条件

- `bible/glossary.md` が全ドメイン語を含む
- works/villainess-coc の rules が template を参照する形に軽量化
- works の learning から template 昇格候補が 1 覧化
- 既存 2 prior audit の P0/P1/P2 項目が全て annotate されている（消化 or 未消化の理由）

---

## 並行作業可能性（Phase 依存図）

```
P0 (下地整理)
 │
 ├──→ P1 (Review 系)         ← P0 完了で開始可
 │
 ├──→ P2 (Craft Library)     ← P0 完了で開始可、P1 と並行可
 │
 ├──→ P3 (Intake)            ← P0 完了で開始可、P1/P2 と並行可
 │
 └──→ P4 (整理・横展開)       ← P1 / P2 / P3 が全て半分以上進んだら開始可
```

---

## 合計見積 / マイルストーン

| Phase | 合計 | マイルストーン |
|---|---|---|
| P0 | 0.5 日 | 下地整理完了、manifest v2 |
| P1 | 1 日 | review 系 + rule、grep 検証正典化 |
| P2 | 2 日 | craft library 21 件新設 |
| P3 | 1 日 | intake 正典化 |
| P4 | 1 日 | ドメイン整理・横展開 |
| **合計** | **5.5 日** | v2 完成宣言 |

並行化すれば 3 日程度に圧縮可能（P0 → P1/P2/P3 並行 → P4）。

---

## 廃止候補リスト（明示）

本計画で明示的に**廃止 or 降格**するもの:

- `packets/exploring/packet-template.yaml` 等 living template 複製 → `packets/templates/` に集約
- `actions/`, `campaigns/`, `telemetry/`, `queue/`, `backlog/`（template 初期状態から） → runtime-optional or deprecated
- 単独 `review` 語（文書内） → typed / bridge / continuity / persona / approval 前置
- `review` 種別のうち未使用のもの（あれば） → `reviews/archive/` へ移動

---

## 横展開チェック（works 側）

本計画の影響を受ける works を列挙し、影響範囲を明示:

| work | 影響 | 対応 |
|---|---|---|
| villainess-coc | 大（reviewer-gate-b / monitoring-dictionary / drafter-preflight が template 側と参照関係変化） | P4-2 で軽量化改訂 |
| one-man-statefall | 大（learning-loop / current-focus / task-context が template 正典化） | P4-3 で揃える、差分を作品固有として残す |
| designer-reborn | 中（seed-to-macro review が template 正典化） | P4 で該当 review の書式だけ揃える |
| ia_society | 小 | 影響最小、craft/ 参照追加のみ |
| ore_tueee_school_hell | 小 | 同上 |
| sample-story | 大（samples/ 整備の参考にする） | P2 で sample 化の方向で整理 |

---

## リスクと緩和

| リスク | 緩和策 |
|---|---|
| craft/ 肥大化（21 項目 × 多 sub） | file-growth.md の 300 行ルール遵守、archive/ で廃止項目保存 |
| intake index の運用漏れ | reflection-ledger の棚卸しを週次固定、30 日超 pending は debt 移送 |
| works 側の既存ルール書き換えで既存 draft 影響 | works 側ルールは template 参照化するが、作品固有節は残す |
| runtime-optional が必要になった作品の手順 | `template.manifest.json` を見て opt-in、手順を README に書く |
| 本計画の承認遅延 | proposals/ として残し、承認部分から段階的に実装する |

---

## 承認後の起動

1. author が本 proposal を `full-accept` / `partial-accept` / `revise` / `reject` で返す
2. `full-accept` or `partial-accept` の場合:
   - Phase 0 から順次実装（または並列化）
   - 各 Phase 完了時点で author 確認
3. `revise` の場合:
   - 本 proposals/ 配下を新 revision で更新
   - 元フォルダは残す（archive 相当）
4. `reject` の場合:
   - 本フォルダを `proposals/archive/2026-04-22-story-template-v2/` に移動
   - 主要知見は `learning/` に抽出

---

## 付録: 本計画の Definition of Done

- [ ] CLAUDE.md 参照ファイルセクションが v2 構成を指す
- [ ] `ls story-template/` で runtime artifacts が初期状態で存在しない
- [ ] `craft/` に 21+ ファイル、checklists / worksheets あり
- [ ] `reviews/` に 7 種 template あり、grep 検証ルール正典化
- [ ] `story/intake/` に index.yaml 3 本 + provenance + reflection-ledger
- [ ] `prompts/intake/` に 5 本、`prompts/review/` に 6 本以上
- [ ] `.claude/rules/` に 5（既存）+ 3（intake-flow / review-system / vocabulary-lint）+ 1（monitoring-dictionary-generic）
- [ ] 新人 drafter が 10 分で作品 init できる
- [ ] Pro 素材 1 本を intake → canon まで通せる
- [ ] works/villainess-coc が template 正典を参照する形に軽量化
