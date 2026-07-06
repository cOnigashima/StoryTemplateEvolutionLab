# Story Template v2 改革提案パック

> **日付**: 2026-04-22
> **作成者**: Claude（本 Cowork セッション）
> **起点指示（taiji）**:
>   - 大量インプット（ChatGPT Pro 等で生成）を漏れなく反映する仕組みにしたい
>   - works / know_how_explore / evaluation-revolution-lab の学習を大切に吸い上げたい
>   - コンテキスト／ハーネスエンジニアリング相当の重装備を恐れずに行う
>   - ドメインを整理し、Canon / Bible / Arc / Promise / Plot / Packet / Scene / Seed / Draft / Pitch / Continuity / Patch / Cadence / Foreshadowing / Prose の包含関係を決める
>   - レビュー体系と創作ノウハウをプロンプト／チェックリスト化する
> **session goal**: 現状監査＋設計書＋骨格まで。改革は計画に落とす（本セッションで実装はしない）

---

## このパックの読み順

1. **`01-design-overview.md`** — 全体設計（現状課題・目標像・4層モジュール・移行方針）
2. **`02-domain-map.md`** — ユビキタス言語マップ（Canon / Bible / Arc / Promise / Packet / Scene / Seed / Intake / Draft / Prose / Continuity / Pitch / Cadence / Foreshadowing / Patch / Rubric / Motif）
3. **`03-intake-flow.md`** — 大量インプット受け入れフロー（raw → digest → seed → promises/bible/arcs / reflection ledger / provenance index / Pro 活用プロンプト）
4. **`04-review-system.md`** — レビュー体系（typed / bridge / continuity / approval / reader-persona / grep 検証 / Gate B / 25 項目 rubric / PART A/B/C）
5. **`05-craft-library.md`** — 創作ノウハウライブラリ（Scene/Sequel・Want/Need・scope・beat sheet・foreshadow・craft principles・反復 motif 運用）
6. **`06-directory-structure.md`** — 提案ディレクトリ構造と命名規約
7. **`07-skeleton/`** — 新規追加する骨格ファイル（テンプレート、空 yaml、prompt シェル）
8. **`08-reform-plan.md`** — 段階移行計画（Phase 0〜4）と廃止候補・横展開の段取り

各ファイルは単独で読めるように書いたが、依存関係は以下:

- `02` → `01`（ドメイン整理は全体設計に従属）
- `03` `04` `05` → `02`（3 テーマの実装はドメイン語を使う）
- `06` → `02` `03` `04` `05`（ディレクトリ構造は実装意図に従う）
- `07` → `06`（骨格はディレクトリ案を具現化する）
- `08` → 全部（移行計画は完成像を前提とする）

---

## 既存の重要資産（本提案と併走させる）

本パックは「ゼロから作る」ではなく、既存資産の**統合・昇格・補完**が軸。特に以下は本セッションでの起点:

- `reviews/2026-04-18-story-template-gap-analysis.md`（466 行） — P0/P1/P2 反省候補の4層アーキ案。本提案の土台
- `reviews/2026-04-18-story-template-intake-integration-proposal.md`（399 行） — 5層 intake アーキ案。`03-intake-flow.md` の下敷き
- `.claude/rules/drafter-preflight.md`（StoryTemplate 本体） — Gate 0/A/C と Multi-Pass Self-Review の正本
- `works/villainess-coc-survival-with-cheating/.claude/rules/*.md` — drafter-preflight（§10 canon citation / §8.1 grep 必須 / Gate C）・reviewer-gate-b（PART E 4 Block）・monitoring-dictionary（卓別辞書・motif 定義）の実戦版
- `works/one-man-statefall/story/learning-loop.md` + `learning/current-focus.yaml` — 学習ループの機械可読層
- `know_how_explore/` — 25 項目 rubric / PART A/B/C レビュープロンプト / 3 stage backlog prompt / Scene-Sequel 等
- `evaluation-revolution-lab/` — 評価系 revolution/evolution lane、criteria-discovery-loop

---

## 本提案の対象外（明示スコープ）

以下は**本パックでは触れない**。必要なら別提案で扱う。

- `factory-platform/` 側 docs の改訂（本提案は StoryTemplate 本体 + works / know_how_explore の成果物統合に集中）
- `one-man-statefall` が持つ job-packets / telemetry / actions / campaigns 周り（ops/runtime 層）
- 公開プラットフォーム（カクヨム等）連携の機能追加
- AI model 選定・RAG/LoRA/SFT 実装（know_how_explore には記述あるが実装は別レイヤ）

---

## 承認プロセス

本パックは**提案**。author（taiji）確認後、以下のいずれか:

- **full-accept** → `08-reform-plan.md` Phase 0 から実行
- **partial-accept** → 採否を per-file で指示、非採用部は `design-debt.yaml` に残す
- **revise** → コメントに基づき本 proposals/ 配下を改訂（新 revision フォルダで並走）
- **reject** → 本フォルダを archive 化し、別アプローチで再起

いずれの場合でも、本パックで引いた「ドメイン語」「レビュー観点」「創作ノウハウ」は `learning/` に要点を抽出して残す。

---

## 付録: このパック自身の品質確認

本パックの自己レビューは `09-self-review.md`（最後に追加）で実施する。チェック観点:

- 3 テーマ（大量入力 / ドメイン / レビュー＋ノウハウ）それぞれに具体的成果物があるか
- 既存ルール（`.claude/rules/*`）と衝突しないか
- 既存の2つの gap-analysis / intake-integration proposal の提言を漏れなく吸収しているか
- works 各作品の learning を遡及反映できる道筋が引かれているか
- kakuyomu-policy との整合（AI 利用タグ・投稿頻度）
- 実行計画が phase 単位で自己完結しているか（前 phase を待たず一部試せるか）
