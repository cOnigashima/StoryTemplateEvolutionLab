# current/ — 現在の正本

> **役割**: StoryTemplateEvolution の現在アクティブな成果物の格納域。
> **v4 採用日**: 2026-04-30
> **編集ルール**: 変更は Patch 経由（直接書き換えではなく、proposal/ 経由で議論してから反映）

---

## 配下のディレクトリ

| ディレクトリ | 役割 | v4 状態 |
|---|---|---|
| `WORKFLOW.md` | **★ 1 枚ガイド**（複製 → raw → 執筆の全体フロー、Claude/Agent onboarding） | v4 新設 |
| `adapter/` | Intake / Writing Adapter の generic prompt + format | intake_adapter_prompt.md は v4 化済み、folder_structure.md は supersede stub |
| `agents/` | **generic agent 18 本**（plotter / drafter / critic / continuity-checker / 他） | v4 注記済み、内部 dir 参照は v3 残存（Q-B-001） |
| `skills/` | **generic skill 7 本**（pitch / draft / critic / continuity / release / 他） | 同上 |
| `rules/` | **共通 rule 5 本**（drafter-preflight / file-growth / kakuyomu-policy / learning-capture / story-os-boundaries）+ intake-flow.md | story-os-boundaries.md と intake-flow.md は v4 化済み |
| `craft/` | 作品共通の Craft Library（Layer 3 道具箱） | README のみ、整備中（Q-B-003） |
| `docs/` | 設計仕様書 | vocabulary / dor_dod は supersede stub、kernel_spec / layer_facet_map / unit_taxonomy は v4 化 |
| `learning/` | StoryTemplate 横断 learning ログ | v3 から継承 |
| `prompts/` | session prompt 群 | v4 化は順次（Q-B-001） |
| `templates/` | 各 work で copy する雛形 | kernel.template.yaml は v4、bible facet 13 雛形は未作成 |
| `templates/.claude/` | **各 work の `.claude/` 雛形**（rules/agents/skills/settings） | v4 で新設、内容は generic |
| `templates/inbox/` | **各 work の `inbox/` 雛形**（README.template.md） | v4 で新設 |
| `templates/story/` | kernel.template.yaml | v4 schema |
| `checklists/` | チェックリスト集 | 補助 |
| `work_init/` | 新規 work 立ち上げ手順 | new-work-bootstrap.md (v4) 配置済 |

---

## 重要な参照導線

### 「v4 の正本どこ?」

- 用語・ドメイン: `../proposal/2026-04-30-zero-base-v4/02_domain_model.md`
- 物理配置: `../proposal/2026-04-30-zero-base-v4/03_storage_trinity.md`
- パイプライン: `../proposal/2026-04-30-zero-base-v4/04_pipeline_overview.md`
- 網羅項目: `../proposal/2026-04-30-zero-base-v4/05_intake_coverage_checklist.md`
- DoR: `../proposal/2026-04-30-zero-base-v4/06_bible_dor.md`
- 検証 prompt: `../proposal/2026-04-30-zero-base-v4/07_review_prompts/`

### 「actually 動かす生成 prompt は?」

- Intake Adapter: `adapter/intake_adapter_prompt.md`（v4 化済）
- Writing Adapter: `adapter/writing_adapter_prompt.md`（Phase 1.5 で v4 化、現状 v3）
- kernel 雛形: `templates/story/kernel.template.yaml`（v4）
- 新規 work bootstrap: `work_init/new-work-bootstrap.md`（v4）

---

## 編集ポリシー

1. **正本性が高いファイルは Patch 経由で変更**
   - kernel_spec.md / layer_facet_map.md / unit_taxonomy.md
2. **supersede stub は触らない**
   - vocabulary.md / dor_dod.md / folder_structure.md は proposal 配下を参照する stub のみ
3. **新しい craft / framework lens は craft/ に追加**
4. **新しい template は templates/ に追加**
5. **作品固有内容は templates/ に流入させない**

---

## v4 後追い作業（Phase 1.5 以降の TODO）

- [x] **agents/ 18 本** archive から restore + v4 注記追加（2026-04-30 完了）
- [x] **skills/ 7 本** archive から restore + v4 注記追加（2026-04-30 完了）
- [x] **rules/ 5 本** archive から restore + v4 化（2026-04-30 完了）
- [x] **templates/.claude/** generic 雛形（rules/agents/skills/settings） 配置（2026-04-30 完了）
- [x] **WORKFLOW.md** 1 枚ガイド作成（2026-04-30 完了）
- [x] **templates/inbox/** 新設（2026-04-30 完了）
- [ ] adapter/writing_adapter_prompt.md を v4 仕様に refactor（Q-B-001）
- [ ] adapter/field_mapping_template.yaml を v4 化（premise → logline）
- [ ] adapter/update_proposal_format.yaml を v4 化（86 項目 trace 必須）
- [ ] templates/bible/ の 13 ファイル新規作成（logline / promise / theme / cadence / system / timeline / samples 等）
- [ ] templates/{bible,design,state,arcs,packets}/README.template.md 作成
- [ ] prompts/ の v4 参照更新（00 / 02 / 04 / 05）
- [ ] craft/ の初期コンテンツ整備（rubric / framework-index / lenses 等）
- [ ] agents / skills の内部 dir 参照を v4 用語に書き換え（Q-B-001）

---

## 不変条件

1. **v3 系の生成 prompt（旧 intake_adapter_prompt.md 等）は archive にあり、current/ にはない**
2. **作品固有 facet は generic 雛形に流入させない**
3. **supersede stub を編集しない**
4. **proposal/ への参照を current/ から切らない**（dependency）
