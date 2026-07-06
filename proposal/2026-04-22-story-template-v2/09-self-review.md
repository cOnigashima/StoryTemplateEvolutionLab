# Proposal Pack 自己レビュー

> **対象**: 本 proposals/2026-04-22-story-template-v2/ 配下 00〜08 + 07-skeleton/*
> **観点**: `00-README.md` §付録 の 6 項目
> **判定**: 各観点について `適合 / 軽微懸念 / 要修正` を付す

---

## S1. 3 テーマそれぞれに具体的成果物があるか

| テーマ | 主ドキュメント | 骨格 (07-skeleton) | プロンプト | ルール | 判定 |
|---|---|---|---|---|---|
| 大量入力受け入れ | `03-intake-flow.md` | `story/intake/raw-index.yaml`, `provenance.yaml`, `reflection-ledger.md`, `digest-template.md`, `digest-index.yaml` | `prompts/intake/` 5 本（raw-submission / digest-writer / seed-extractor / seed-to-macro-reviewer / pro-research-brief） | `rules/intake-flow.md` | **適合** |
| ドメイン整理 | `02-domain-map.md`, `06-directory-structure.md` | `manifest/template.manifest.v2.json` | — | `rules/vocabulary-lint.md`, `rules/monitoring-dictionary-generic.md` | **適合** |
| レビュー体系＋創作ノウハウ | `04-review-system.md`, `05-craft-library.md` | `reviews/continuity-review-template.md`, `persona-review-template.md`, `approval-template.md`, `packet-freeze-template.md`, `craft/README.md` | `prompts/review/` 6 本（persona A/B/C + PART A/B/C） | `rules/review-system.md` | **適合** |

各テーマに「設計書 + 骨格 + プロンプト + ルール」の 4 点セットが揃っており、手を入れる起点は十分。

欠けているもの（**軽微懸念**）:

- craft/ 以下の個別 craft ファイル（`scene-sequel.md`, `want-need.md`, `beat-sheets.md` 等）は `05-craft-library.md` の §3 で仕様を示したが、骨格ファイルは未生成。**Phase 2 で埋める前提**として 08-reform-plan.md §P2 で明記されているため本パックでは許容。
- `reviews/typed-review-template.md` の v2 化（既存 template の上書き）は `04-review-system.md` §2 で構成を示したが、骨格ファイルは未生成。これも Phase 1 で行う前提。

→ **許容。Phase 1/2 の work item 化は確認済み**

---

## S2. 既存ルール（`.claude/rules/*`）と衝突しないか

既存 5 ルールと本パックの対応:

| 既存ルール | 本パックでの扱い | 衝突 |
|---|---|---|
| `learning-capture.md` | そのまま維持。本パックは上位レイヤ（intake / review）を増築するのみで、learning/ の扱いは変更しない。`03-intake-flow.md` §5 で「反映完了 seed を learning に昇格」とする言及があるが、既存の4キャプチャ対象（インシデント/方法論/フィードバック/テンプレ）と整合 | なし |
| `drafter-preflight.md` | そのまま維持。本パックの `04-review-system.md` §2.2 Gate B は「drafter が Gate A で宣言した計画を reviewer が検収する」という既存構造をそのまま踏襲。`05-craft-library.md` の craft は preflight の「補助読み物」として位置付け、preflight の MUST/SHOULD は上書きしない | なし |
| `file-growth.md` | そのまま維持。本パックの 07-skeleton は「初期最小構成」として file-growth.md の原則（1 ファイルで始め、育ったら分割）と整合。craft/ のファイル群は「必要に応じて作る」運用と明記（05-craft-library §14） | なし |
| `story-os-boundaries.md` | **追記が必要**（本パックで境界を拡張）。`06-directory-structure.md` §2 で diff を明示: ①intake の正本を `story/intake/raw + digests + seeds` に更新 ②runtime-optional 物の位置を定義 ③`Craft Library` を正本群に追加。既存の禁句（`backlog / bundle / queue 正本化`）はそのまま維持 | **拡張あり・衝突なし** |
| `kakuyomu-policy.md` | そのまま維持。本パックは公開フロー（approved → published）の改訂に踏み込まないため変更不要。`04-review-system.md` §5 Approval Review のチェックリストに「kakuyomu-policy 適合（AI本文利用タグ / 頻度）」を明示項目として組み込み済 | なし |

新規追加ルール 3 + ガイド 1（`rules/intake-flow.md`, `rules/review-system.md`, `rules/vocabulary-lint.md`, `rules/monitoring-dictionary-generic.md`）は既存 5 ルールとスコープが重ならない（intake / review workflow / 語彙 / 作品固有監視辞書のガイド）。

→ **適合。既存を壊さず、境界だけ追記**

---

## S3. 既存 2 つの gap-analysis / intake-integration 提言を漏れなく吸収しているか

### `reviews/2026-04-18-story-template-gap-analysis.md`（4 層アーキ案 / P0-P2）

| gap-analysis の提言 | 本パックでの吸収先 | 状態 |
|---|---|---|
| 4 層アーキテクチャ（Intake / Core Authoring / Review-Learning / Release） | `01-design-overview.md` §2 で 4+1 層に拡張（Craft Library を Layer 3 に追加、Runtime を Layer R に分離） | 吸収・拡張 |
| Review 体系の強化（typed / bridge / continuity / approval） | `04-review-system.md` §1 で Review Matrix 7 種として再整理。persona / packet-freeze を追加 | 吸収・拡張 |
| 創作ノウハウのテンプレ正典化 | `05-craft-library.md` 全体で Layer 3 として独立化 | 吸収 |
| Runtime artifact の曖昧さ（one-man-statefall 伝染リスク） | `06-directory-structure.md` §1 で `template / samples / runtime_optional / deprecated` を manifest で分離。§2 で物理的削除/移動リストを提示 | 吸収 |
| P0 着手候補（ドメイン整理 / ルール昇格） | `08-reform-plan.md` Phase 0 で下地整理として落ちている | 吸収 |

### `reviews/2026-04-18-story-template-intake-integration-proposal.md`（5 層 intake）

| intake-integration の提言 | 本パックでの吸収先 | 状態 |
|---|---|---|
| 5 層 intake（source / digest / seed / canon+impl / reflection） | `03-intake-flow.md` §1 で 5 層アーキとして正典化。A/B/C/D/E のレイヤ ID を付与 | 吸収 |
| digest-index.yaml / raw-index.yaml / provenance.yaml | `07-skeleton/story/intake/*.yaml` として骨格生成済 | 吸収 |
| Reflection Ledger | `07-skeleton/story/intake/reflection-ledger.md` として骨格生成。未反映/却下/反映完了/棚卸し履歴の4セクション | 吸収 |
| Pro 活用プロンプト | `07-skeleton/prompts/intake/pro-research-brief.md` 等 5 本で FACT/SPECULATION/COLLISION/CORE/QUESTION ラベル運用を含め正典化 | 吸収 |
| seed-to-macro の反映トリアージ | `07-skeleton/prompts/intake/seed-to-macro-reviewer.md` で promote/hold/patch/reject の 4 判定に標準化 | 吸収 |

→ **適合。両 proposal の提言は漏れなく吸収（拡張を伴う）**

---

## S4. works 各作品の learning を遡及反映できる道筋が引かれているか

`08-reform-plan.md` §横展開チェック で各作品の影響度を記載済：

| 作品 | 影響度 | 本パックでの遡及反映経路 |
|---|---|---|
| villainess-coc-survival-with-cheating | 大 | ①§10 canon citation / §8.1 grep 必須 / Gate C の先行資産は本パック `rules/review-system.md` + `04-review-system.md` §2.3 で template canon に昇格。作品側は template 参照に差し替え可能 ②reviewer-gate-b の 4 Block は `typed-review-template v2` §PART B に generic 化。作品側は 卓 specific 部分だけ残す ③monitoring-dictionary は `rules/monitoring-dictionary-generic.md` で作品固有ファイル条件を提示、作品側の辞書はそのまま保持 |
| one-man-statefall | 大 | ①learning-loop.md / current-focus.yaml の機械可読層は `07-skeleton/learning/current-focus.yaml` と `packets/task-context-template.yaml` で generic 化 ②Runtime 残存物（job-packets / telemetry 等）は 06 §2 で `runtime_optional` にタグ分離、template に流入させない |
| designer-reborn | 中 | packet / scene / draft 構造は既に準拠。本パックの craft library を後発適用できる（任意） |
| ia_society | 小 | 現状の sample 的位置付けを維持。06 §5 の「work init 10 steps」に倣って再 init 可能 |
| ore_tueee_school_hell | 小 | 同上。特別な遡及項目なし |
| sample-story | 大 | template の init canon として扱う。本パック後の template 更新に同期で入れ替え予定（08 §P0 に明記） |

→ **適合。works 各作品の遡及経路は定義済、実行は Phase 1/2/4 に割り当て**

---

## S5. kakuyomu-policy との整合

既存 `kakuyomu-policy.md` の主要条項と本パックの関係：

- **AI 本文利用タグ必須** → `07-skeleton/reviews/approval-template.md` の必須チェック項目に組み込み済
- **1日3話 / 週15話 / 最小4h間隔** → Approval Review のチェックに「投稿頻度」の項目を明示（本パック 04 §5）
- **禁止コンテンツ / コンテスト応募時条件** → Approval Review §公開前チェックに組み込み済
- **工場生成原稿は「AI本文利用」** → 本パックで生成物の扱いを変更しないため自動準拠

新たな衝突リスク:

- `05-craft-library.md` の genre-patterns（悪役令嬢 / 異世界 等）で過度な暴力/性的描写の推奨になっていないかを確認 → craft ファイルは原則の記述のみで具体描写基準には踏み込まない設計。禁則は `bible/rules.md` + `kakuyomu-policy.md` 側で一元管理する運用は維持

→ **適合**

---

## S6. 実行計画が phase 単位で自己完結しているか

`08-reform-plan.md` 各 phase の独立性確認：

| Phase | 前提 | アウトプット | 他 phase なしに価値を出せるか |
|---|---|---|---|
| P0 下地整理（0.5日） | なし（本提案承認のみ） | manifest v2 / story-os-boundaries 更新 / deprecated 移動 | **Yes**。ここで止めても「ディレクトリが整頓された template」になる |
| P1 Review+rule（1日） | P0（任意）、並行可 | typed-review-template v2, persona/continuity/approval/packet-freeze templates, prompts/review/* | **Yes**。既存 draft に対してすぐ review を流せる |
| P2 Craft Library（2日） | なし（独立） | craft/* 21 ファイル + checklists + worksheets | **Yes**。drafter / plotter の参照道具箱として単独機能 |
| P3 Intake（1日） | P0（任意） | raw-index / digest-index / provenance / reflection-ledger 実データ | **Yes**。既存作品の raw inputs をここで受け止められる |
| P4 ドメイン整理・横展開（1日） | P0〜P3 の一部 | works 側の参照差し替え、vocabulary-lint 適用 | **Partial**。P1/P2 の成果物があると意味が増すが、P0 単独でも lint は回せる |

依存関係は **P0 が唯一の gating**、残りは並行可能（08 §並行作業可能性）。Phase ごとに「ここで止めても得がある」設計になっている。

→ **適合**

---

## 総合判定

| 観点 | 判定 |
|---|---|
| S1. 3 テーマそれぞれの具体性 | 適合（軽微懸念は Phase 化済） |
| S2. 既存ルールとの非衝突 | 適合 |
| S3. 既存 2 proposal の吸収 | 適合 |
| S4. works 遡及反映経路 | 適合 |
| S5. kakuyomu-policy 整合 | 適合 |
| S6. phase 自己完結性 | 適合 |

**総合**: 本パックは author レビューに進める状態。要修正項目なし、軽微懸念は Phase 1/2 で自然に埋まる設計のため明示的ハンドリング不要。

---

## 発見した改善余地（本パック外で対応）

本セッションでは実施せず、author 判断に委ねる論点：

1. **craft/ 以下個別ファイルの先行生成**: 本パックは `05-craft-library.md` §3 で仕様と目次を固め、個別の 21 craft ファイルは Phase 2 に委ねた。author 指示があれば本パックに追加生成も可能
2. **reviews/typed-review-template.md の v2 上書き骨格**: §2 の全文（PART A-G）を 07-skeleton に置くかどうか。現状は仕様のみ。ここも author 指示で追加可能
3. **factory-platform docs 側の改訂**: 00 §対象外で除外しているが、ubiquitous language / domain map / sources-of-truth / workflows の4 docs は本パックの `02-domain-map.md` と同期させる必要がある。別セッション / 別提案で扱う
4. **one-man-statefall の runtime artifact の扱い方針**: 本パックは「template に持ち込まない」までは決めたが、one-man-statefall 内での継続使用可否は作品 author 判断
5. **Monitoring Dictionary の generic canon 化の範囲**: 本パックは `rules/monitoring-dictionary-generic.md` として「作品固有辞書の最低構成とガイド」に留めた。villainess-coc の motif 運用原理のうち、どこまでを generic 化して craft/motif-operations.md に昇格させるかは Phase 2 で再判定

---

## 自己レビュー手順メモ（再実行用）

将来 revision 時に同じ自己レビューを回すための手順：

1. `00-README.md` §付録 6 項目を観点とする
2. 各観点を `適合 / 軽微懸念 / 要修正` の 3 値で判定する
3. 既存ルール 5 本（learning-capture / drafter-preflight / file-growth / story-os-boundaries / kakuyomu-policy）とのマトリクスは毎回作り直す
4. 既存 2 proposal（gap-analysis / intake-integration）の提言リストと吸収状態の対応表を更新する
5. works 各作品の影響度表を更新する
6. phase 自己完結性は「ここで止めても得があるか」を各 phase に問う
7. 総合判定で「要修正」があれば 00-README の読み順に戻して当該ドキュメントを改訂する

---

## 結論

**本パックは approval 可の状態**。taiji から採否判断（full-accept / partial-accept / revise / reject）を受けた後、`08-reform-plan.md` Phase 0 起動 or 指定 phase 先行で実行に入る。
