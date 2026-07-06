# 01 Supersession Map — 現行構造の取捨

> **役割**: StoryTemplateEvolution の現行ファイルを `keep` / `refactor` / `supersede` / `archive` の 4 区分に分類し、移行マップを定義。
> **対象**: `docs/` `adapter/` `templates/` `prompts/` 配下の現行ファイル。
> **依存**: 02 / 03 / 04 / 05 / 06 / 07 を本提案として書いた後の整理。

---

## 0. 4 区分の定義

| 区分 | 意味 | アクション |
|---|---|---|
| **keep** | そのまま維持。本提案の内容と整合 | 何もしない |
| **refactor** | 内容は維持、本提案に合わせて軽微修正 | 該当箇所のみ書き換え |
| **supersede** | 本提案のドキュメントが置き換える | 旧ファイルは archive、参照は新提案に向ける |
| **archive** | 用途終了、退避 | `archive/2026-04-30-pre-v4/` に移動 |

退避先: **`StoryTemplateEvolution/archive/2026-04-30-pre-v4/`**（新規作成）

---

## 1. docs/ 配下

| 現行ファイル | 区分 | 移行先 / 備考 |
|---|---|---|
| `docs/README.md` | refactor | v4 の構成に合わせて proposal 参照を更新 |
| `docs/vocabulary.md` | **supersede** | `proposal/2026-04-30-zero-base-v4/02_domain_model.md` が置き換え。3 列表 → 8 フィールド card 書式 |
| `docs/kernel_spec.md` | **refactor** | schema_version: v3 → v4 / `premise:` → `logline:` リネーム |
| `docs/dor_dod.md` | **supersede** | `proposal/.../06_bible_dor.md` が置き換え |
| `docs/layer_facet_map.md` | **refactor** | 二軸モデル（案 Z）に合わせて単位 × facet を明示。`bible/plot/` 廃止 |
| `docs/unit_taxonomy.md` | refactor | Transformation Curve を Arc 同名衝突回避として追加 |
| `docs/status_vocabulary.md` | keep | 11 値は本提案でも継承 |

archive 候補: なし（すべて refactor or supersede で対応）

---

## 2. adapter/ 配下

| 現行ファイル | 区分 | 移行先 / 備考 |
|---|---|---|
| `adapter/README.md` | refactor | v4 の物理位置（leading dot なし）と 7 review prompt への参照を追加 |
| `adapter/intake_adapter_prompt.md` | **refactor** | 本提案の `02_domain_model.md` `05_intake_coverage_checklist.md` を参照する形に再構成。output 形式は `update_proposal_format.yaml` に従う |
| `adapter/writing_adapter_prompt.md` | refactor | Writing Pack 4 ファイル形式は維持、bible facet 17 体制に合わせて context_pack の参照範囲を調整 |
| `adapter/folder_structure.md` | **supersede** | `proposal/.../03_storage_trinity.md` が置き換え |
| `adapter/field_mapping_template.yaml` | refactor | premise → logline、`.adapter/` → `adapter/`、Bible facet 17 体制への mapping 例を追加 |
| `adapter/update_proposal_format.yaml` | refactor | 86 項目チェックリスト（05）への trace を必須化、status 11 値を明示 |
| `adapter/writing_pack_format.yaml` | keep | 4 ファイル構成は維持 |
| `adapter/human_approval_policy.md` | keep | 不変条件は維持 |

archive 候補: なし

---

## 3. templates/ 配下

| 現行ファイル | 区分 | 移行先 / 備考 |
|---|---|---|
| `templates/bible/premise.template.md` | **archive** + **新規作成** | `bible/logline.template.md` を新規作成、旧 premise.template.md は archive |
| `templates/bible/reader_promise.template.md` | refactor | `promise.template.md` にリネーム、内容は維持 |
| `templates/bible/theme.template.md` | keep | |
| `templates/bible/genre.template.md` | refactor | `genre-overlay.template.md` にリネーム |
| `templates/bible/style_guide.template.md` | **refactor + 分割** | `style-voice.template.md` と `rules.template.md` に分割 |
| `templates/bible/characters/protagonist.template.md` | keep | |
| `templates/bible/characters/individual.template.md` | keep | |
| `templates/bible/world/locations.template.md` | refactor | `bible/world/` 配下のサブ分割（locations / society / physics）に対応 |
| `templates/bible/plot/arc_map.template.md` | refactor | `arcs/series-overview.template.md` に移動（Bible 配下から arcs/ 配下へ） |
| `templates/bible/plot/episode_plan.template.md` | refactor | `arcs/episode-plan.template.md` または `packets/{packet}/episode-plan.template.md` |
| `templates/bible/plot/scene_cards.template.md` | refactor | `scenes/seed/scene-template.md` に移動 |
| `templates/bible/in_world_documents/samples.template.md` | refactor | 作品固有 facet として generic 雛形から外す（fools-with-cheating 固有） |
| `templates/design/project_principles.template.md` | keep | |
| **新規作成必要** | — | `bible/system.template.md`、`bible/timeline/history.template.md`、`bible/timeline/day-by-day.template.md`、`bible/samples/sample-scene.template.md`、`bible/foreshadowing-map.template.md`、`bible/reveal-plan.template.md`、`bible/motif-ladder.template.md`、`bible/cadence-plan.template.md`、`bible/plot.template.md`、`bible/project-override.template.md` |
| **新規 README** | — | `templates/bible/README.template.md` `templates/design/README.template.md` `templates/state/README.template.md` `templates/arcs/README.template.md` `templates/packets/README.template.md` |

archive 候補: `templates/bible/premise.template.md`（logline に置き換え後）

---

## 4. prompts/ 配下

| 現行ファイル | 区分 | 移行先 / 備考 |
|---|---|---|
| `prompts/README.md` | refactor | v4 の構成と新 review prompt への参照を追加 |
| `prompts/00_session_start.md` | refactor | 4 論点の決着 + 56 語 card pass を踏まえた起動文に更新 |
| `prompts/01_improve_from_new_work.md` | keep | |
| `prompts/02_audit_gaps.md` | refactor | `../../adapter/review_prompts/design-audit-prompt.md` との連動を明記 |
| `prompts/03_extract_pattern.md` | keep | |
| `prompts/04_apply_to_new_work.md` | refactor | 新規 work bootstrap 手順を v4（DoR-A）に合わせて更新 |
| `prompts/05_consistency_check.md` | refactor | `../../adapter/review_prompts/intake-coverage-review.md` との連動を明記 |

archive 候補: なし

---

## 5. proposal/ 配下（旧 proposals/）

| 現行 proposal | 区分 | 備考 |
|---|---|---|
| `proposal/2026-04-22-story-template-v2/` | **archive** | 参照資産として残す（archive ではないが「過去の design 履歴」として `proposal/` 配下に温存） |
| `proposal/2026-04-29-domain-kernel-v3/` | keep | 本提案 v4 が継承、v3 は履歴として残す |
| `proposal/2026-04-29-pilot-driven-evolution/` | keep | 本提案 v4 が継承 |
| `archive/proposal/storytemplate_workflow_handoff_pack_takt/` | **archive** | TAKT 連携 Pack。Layer R は opt-in 方針継承、本提案では使わない |
| `proposal/2026-04-30-zero-base-v4/` | **本提案** | 新規作成 |

archive 先候補: `archive/proposal/`

---

## 6. その他のトップレベルファイル / ディレクトリ

| 現行 | 区分 | 備考 |
|---|---|---|
| `README.md` | refactor | v4 採用後に更新（構成変更を反映） |
| `learning/2026-04-29-renji-pilot-retro.md` | keep | 履歴 |
| `learning/2026-04-29-template-extraction-method.md` | keep | 履歴 |
| `learning/2026-04-29-handoff-to-next-session.md` | keep | 履歴 |
| `work_init/` | refactor | v4 の DoR-A に合わせて bootstrap 手順を更新 |
| `checklists/` | refactor or **supersede** | 本提案の 06 + 07 が一部置き換える |
| `rules/` | keep | `.claude/rules/` への追加候補集 |
| `craft/` | keep（または新規） | 現状空の場合は新規作成、Layer 3 として整備 |

---

## 7. 集計

```
docs/        : keep 1 / refactor 4 / supersede 2 / archive 0
adapter/     : keep 2 / refactor 5 / supersede 1 / archive 0
templates/   : keep 3 / refactor 7 / supersede 0 / archive 1（premise）
              + 新規 13 ファイル必要
prompts/     : keep 2 / refactor 5 / supersede 0 / archive 0
proposal/   : keep 3 / archive 1（v2-fat / handoff）
top-level    : refactor 2 / keep 4
```

合計:
- **keep**: 14 ファイル
- **refactor**: 23 ファイル
- **supersede**: 3 ファイル
- **archive**: 3 ファイル（v2-fat proposal / handoff proposal / premise.template.md）
- **新規作成**: 13 template ファイル + 5 README template

---

## 8. 移行作業の優先順位

採用承認後の作業順:

### Priority 1: 不可逆な構造変更
- archive ディレクトリ作成（`archive/2026-04-30-pre-v4/`）
- v2-fat / handoff proposal を archive に移動
- v3 の `premise:` フィールドを v4 の `logline:` に rename

### Priority 2: 主要 supersession
- `docs/vocabulary.md` を本提案 02 で置き換え（旧版 archive）
- `docs/dor_dod.md` を本提案 06 で置き換え（旧版 archive）
- `adapter/folder_structure.md` を本提案 03 で置き換え（旧版 archive）

### Priority 3: refactor 群
- `docs/kernel_spec.md`、`docs/layer_facet_map.md`、`docs/unit_taxonomy.md` 更新
- `adapter/intake_adapter_prompt.md` の prompt body を v4 仕様に書き直し
- `adapter/writing_adapter_prompt.md` 更新
- `templates/bible/style_guide.template.md` を `style-voice.template.md` + `rules.template.md` に分割
- `templates/bible/reader_promise.template.md` を `promise.template.md` にリネーム

### Priority 4: 新規 template 作成
- 13 ファイル新規作成
- 5 README template 新規作成

### Priority 5: 各 work への適用
- `10_migration_plan.md` で詳述

---

## 9. rollback 戦略

万一 v4 採用後に問題が発覚した場合:

1. `archive/2026-04-30-pre-v4/` から旧ファイルを復元
2. `proposal/2026-04-30-zero-base-v4/` の supersede 指示を無効化
3. 各 work では `bible/logline.md` → `bible/premise.md` リネームの逆を実行
4. `adapter/intake_adapter_prompt.md` を v3 版に戻す

復元手順は `10_migration_plan.md` Section "rollback" で詳述。

---

## 10. 不変条件（移行作業中）

1. **archive 先のファイルは削除しない** — 履歴として永続保存
2. **作業中は v3 と v4 が並行して読める状態を維持** — supersede 期間中は両方残す
3. **既存 work の本文（prose）には影響を与えない** — ファイル名 / 構造のみ変更
4. **kernel.yaml の schema 変更は一括で行わない** — 各 work ごとに段階移行
5. **作業ログは `learning/` に残す**


---

## Phase 1 実施報告（2026-04-30 完了）

本 supersession map は v4 採用と同時に Phase 1 で実行された。実施結果:

### 物理操作の実績

```
StoryTemplateEvolution/
├── README.md                           # ★ v4 採用版に書き換え
├── archive/                            # ★ 新設
│   ├── README.md                       # ★ 新設
│   ├── 2026-04-30-pre-v4/              # ★ 旧 docs/adapter/templates/prompts/etc の snapshot
│   │   ├── README.md.snapshot          # 旧トップ README
│   │   ├── docs/ adapter/ templates/ prompts/ checklists/ rules/ learning/ work_init/
│   └── proposal/                       # ★ 新設
│       └── storytemplate_workflow_handoff_pack_takt/  # ★ proposal から archive へ移動
├── current/                            # ★ 新設
│   ├── README.md                       # ★ 新設
│   ├── adapter/                        # 旧トップ adapter から移動 + intake_adapter_prompt.md は v4 化
│   ├── craft/                          # ★ 新設（Q-B-003 整備中）
│   │   ├── README.md
│   │   └── lenses/
│   ├── docs/                           # 旧トップ docs から移動 + 一部 supersede stub 化
│   │   ├── vocabulary.md               # ★ supersede stub
│   │   ├── dor_dod.md                  # ★ supersede stub
│   │   ├── kernel_spec.md              # ★ refactor (premise → logline、schema_version v4)
│   │   ├── layer_facet_map.md          # ★ refactor (二軸モデル、三本柱)
│   │   ├── unit_taxonomy.md            # ★ refactor (Transformation Curve 追記)
│   │   └── status_vocabulary.md        # keep
│   ├── templates/                      # 旧トップ templates から移動
│   │   └── story/kernel.template.yaml  # ★ 新規配置（v4 schema）
│   ├── work_init/
│   │   └── new-work-bootstrap.md       # ★ 新規配置（v4）
│   ├── prompts/ checklists/ rules/ learning/  # 旧トップから移動
│   └── adapter/folder_structure.md     # ★ supersede stub
└── proposal/                           # ★ 旧 proposals/ から rename（複数形 → 単数形）
    ├── README.md                       # ★ 新設（status 表）
    ├── 2026-04-22-story-template-v2/   # historic
    ├── 2026-04-29-domain-kernel-v3/    # historic
    ├── 2026-04-29-pilot-driven-evolution/  # historic / methodology
    └── 2026-04-30-zero-base-v4/        # ★ ADOPTED
```

### 数値実績

- 旧資産 snapshot: archive/2026-04-30-pre-v4/ に 81 ファイル退避
- current/ 配下: 61 ファイル（旧トップから移動 + v4 化更新 + 新規 README + craft/ 整備）
- proposal/2026-04-30-zero-base-v4/: 24 ファイル（11 設計文書 + 7 review prompt + 3 pilot walkthrough + 3 artifact + 各 README）

### 未完了（マニュアル待ち）

- ✗ `archive/story-template-v1/` 配下: 旧 `../story-template for TAKT/` の物理移動
  - 本セッションのマウント外のため bash 不可
  - user マニュアル実行手順は `archive/README.md` を参照

### v3 提案の status 更新（実施後の表）

| 提案 | 旧位置 | 新位置 | status |
|---|---|---|---|
| 2026-04-22-story-template-v2 | proposals/ | proposal/ | historic / partially-absorbed |
| 2026-04-29-domain-kernel-v3 | proposals/ | proposal/ | historic / superseded by v4 |
| 2026-04-29-pilot-driven-evolution | proposals/ | proposal/ | historic / methodology |
| storytemplate_workflow_handoff_pack_takt | proposals/ | **archive/proposal/** | archived |
| 2026-04-30-zero-base-v4 | （新規） | proposal/ | **★ ADOPTED** |
