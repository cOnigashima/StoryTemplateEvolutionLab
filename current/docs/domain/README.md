# docs/domain/ — ドメイン正本（用語・格納・パイプライン・DoR）

StoryTemplate の**ドメイン教義の生きた正本**。用語が分からない・どこに置くか迷う・DoR を判定したい、はまずここ。

> **出典**: `StoryTemplateEvolutionLab/proposal/2026-04-30-zero-base-v4/`（v4 提案。採用時スナップショットとして凍結）。
> 2026-07-06 に生きた正本を本フォルダへ移管（旧名 `docs/v4/` → 意味が通る `docs/domain/` に改名）。
> 番号は v4 提案の読み順を踏襲。ファイル内の `proposal/2026-04-30-zero-base-v4/...` 表記は採用時の史実。

## 中身

| ファイル | 何が分かるか |
|---|---|
| `00_README.md` | 全体の入口・読み順 |
| `01_supersession_map.md` | v3 → v4 で何が置き換わったか（史実） |
| `02_domain_model.md` | ★**56語のユビキタス言語 Card**（用語の正本。status 12値含む） |
| `03_storage_trinity.md` | bible / design / state の三分（どこに何を置くか） |
| `04_pipeline_overview.md` | intake → design → writing → review → publish の動作正本 |
| `05_intake_coverage_checklist.md` | ★86項目の網羅チェックリスト（intake 時に照らす） |
| `06_bible_dor.md` | ★DoR-A/B/C・DoD、status×DoR 表、reverse flow |
| `08_pilot_validation/` | 3作品（ia_society / ore_tueee / fools）の実装 walkthrough |
| `09_open_questions.md` | v4 時点の未決論点 |
| `10_migration_plan.md` | v3→v4 移行手順（史実） |

※ `07_review_prompts` は `../../adapter/review_prompts/` が生きた正本（12値対応済み）。

## コンパクト版との関係

`../`（docs/ 直下）の kernel_spec / unit_taxonomy / status_vocabulary / layer_facet_map は**要約版**。詳細・根拠は本フォルダ。status 語彙だけは例外で `../status_vocabulary.md` が12値の正本（本フォルダ 02 の Section 12 と同期）。
