# StoryTemplateEvolution

> AI 支援の長編小説制作のための、次世代 Story Template。
> 開始日: 2026-04-29 / v4 採用日: 2026-04-30 / **workbench 統合日: 2026-07-06**（current を全面置換。旧 current は `archive/2026-04-31-integreated/` に凍結）

---

## 三本柱 + 補助 2 つ

このリポジトリは **3 つのトップディレクトリ + 2 つの補助** に分かれます:

| ディレクトリ | 役割 | 編集可否 |
|---|---|---|
| **`current/`** | 現在の正本（v4 + 2026-07-06 workbench 統合済み）。**`WORKFLOW.md` から読むと最短** | ✓ 編集可（変更は Patch 経由推奨） |
| **`proposal/`** | 提案（履歴 + アクティブ） | ✓ 編集可（提案ごとに） |
| **`archive/`** | 凍結された旧資産 | ✗ 編集禁止（参照のみ） |
| `.claude/` | StoryTemplate 自身の Claude Code 設定（**リポジトリ開発時の rule**） | ✓ 編集可 |
| `improvement_request_inbox/` | **StoryTemplate 自身**への改善要望・作品 retro からの汎用知見の受付（v5 への素材）。raw のまま投入可 | ✓ raw 投入 |

> **重要**: 各 work（`works/{slug}/`）の `.claude/` や作品側 inbox とは別物。これらはリポジトリ自体のもの。作品固有の raw は作品側へ。
> 反映フロー: `improvement_request_inbox/` → 検討（proposal/ 化 or Patch）→ current 反映 → 決着を `current/learning/` に記録。

---

## いま正本はどこ?

**正本は `current/` 配下です**（2026-07-06 に workbench 版へ全面置換）。具体的に:

| 内容 | 場所 | 備考 |
|---|---|---|
| 運用契約（人間ゲート・core/overlay・オントロジー） | `current/CLAUDE.md` | 2026-07-06 新設 |
| 継承マップ（何が踏襲で何が新規か） | `current/INHERITANCE.md` | 2026-07-06 新設 |
| 用語・ドメインモデル | `current/docs/domain/02_domain_model.md` | current/docs/vocabulary.md は supersede stub。proposal v4 は凍結スナップショット |
| 物理配置仕様 | `current/template/folder_structure.md` | core+overlay の完全ツリー。背景は `current/docs/domain/03_storage_trinity.md` |
| パイプライン | `current/docs/domain/04_pipeline_overview.md` | |
| 網羅チェックリスト | `current/docs/domain/05_intake_coverage_checklist.md` | |
| DoR | `current/docs/domain/06_bible_dor.md` | current/docs/dor_dod.md は supersede stub |
| 検証 prompt | `current/adapter/review_prompts/` | v4 の 07_review_prompts 由来 |
| Intake Adapter (生成) | `current/adapter/intake_adapter.md` | 2026-07-06 再編 |
| kernel 雛形 | `current/template/core/kernel.template.yaml` | v4 schema |
| Bootstrap 手順 | `current/work_init/new-work-bootstrap.md` | |
| 置換の根拠 | `proposal/2026-07-06-workbench-ontology-loop/PROPOSAL.md` | オントロジー / TAKT ループ / core+overlay |

「正本どっち?」と迷ったら `current/WORKFLOW.md` → `current/CLAUDE.md` から入る。ドメイン語彙の正本は `current/docs/domain/00_README.md`（proposal v4 は採用時の凍結スナップショット）。

---

## 新規作品を立ち上げるには

最初に **`current/WORKFLOW.md`** を読む。1 ページで全体像が分かる。

```
1. current/WORKFLOW.md（全体図）を読む
2. current/work_init/new-work-bootstrap.md（手順書）に従う
3. current/template/folder_structure.md に従い作品フォルダを作成（core を複製 + overlay を選択）
4. work.manifest で core version / overlay / 逸脱を宣言
5. current/adapter/intake_adapter.md で初回 intake
6. current/adapter/review_prompts/ で検証
7. DoR-A 通過 → runtime/drafts/ で執筆をガリガリ進める
```

---

## 既存 work を v4 に移行するには

3 作品（ia_society / ore_tueee_school_hell / fools-with-cheating）の walkthrough が用意されています:

- `current/docs/domain/08_pilot_validation/ia_society_zero_state.md`
- `current/docs/domain/08_pilot_validation/ore_tueee_school_hell_partial.md`
- `current/docs/domain/08_pilot_validation/fools_with_cheating_complete.md`

実行手順は `current/docs/domain/10_migration_plan.md` Phase 2 を参照。

---

## 設計原則（v1 → v4 で継承）

1. **kernel は薄く保つ**: 11 項目以内、増やさない
2. **bible / design / state を分離**: 安定設定 / 揺れる設計 / 動的状態
3. **Intake Adapter は raw を直接 bible に流さない**: Update Proposal を経由
4. **Writing Adapter は bible 全体を writer に渡さない**: 1 単位に圧縮
5. **status を 12 値で区別**: filled / tentative / deferred / intentionally_blank / intentionally_hidden / not_applicable / genre_not_applicable / project_override / contradiction / needs_author_decision / missing / rejected（2026-07-06 に 11→12 値へ拡張。正本は `current/docs/status_vocabulary.md`）
6. **fat-by-design は Layer 2/3 のみ**: kernel は薄く、レビュー道具・craft は厚く
7. **template は実走から生む**: 設計室で先に作らず、pilot 実走から抽象化
8. **作品固有装置は generic 化しない**: template に積まない
9. **Bible に Draft（本編 prose）を入れない**: drafts/ のみ（v4 で確定）
10. **Premise → Logline**: kernel #1 を改名（v4 で確定）

---

## 進化方針

- **Pull 型**: 新作品で必要になったときに template を引き出す
- **Retro 駆動**: 各作品 / 各 arc で retro を回し、効いた template を残す
- **凍結禁止**: 「最強テンプレ完成」を目指さない。常に v0 ベース
- **作品固有はコピーしない**: 別作品が「これ採用する」と決めたら個別コピー、template には積まない

本提案 v4 もまた、3 作品の実走から抽象化された v0 であり、v5 への置き換えを前提とする。

---

## 隣接ドキュメント

- **`current/WORKFLOW.md`** — ★ 1 枚ガイド（複製 → raw → 執筆の全体図）
- `current/README.md` — 現在の正本一覧
- `proposal/README.md` — 提案 status 一覧
- `archive/README.md` — 凍結された旧資産
- `.claude/CLAUDE.md` — StoryTemplate 自身の編集ルール
- `improvement_request_inbox/README.md` — StoryTemplate 自身への改善 input 受付
- `current/learning/README.md` — template 進化の決着記録（作品 retro からのフィードバックフロー）

---

## ライセンス・著作権

各 work の作品設定・本文・固有名詞などは作者 (taiji) の著作物。本テンプレートは構造の抽象化のみを抽出し、各 work 固有内容は templates/ には含めない。
