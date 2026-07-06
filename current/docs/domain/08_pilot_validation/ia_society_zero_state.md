# 08-ia_society — 大量既存資料の再配置 + Bible→drafts 剥がし

> **対象**: `works/ia_society/`
> **状態**: bible/ia_story_bible_v2/ に 50+ ファイル + 18 EPISODE_FULL_DRAFT 同居
> **検証目的**: 外部完成 bible package を v4 構造に取り込む実走。

---

## 1. 現状サマリ

```
works/ia_society/
├── CLAUDE.md                                  # ✓ 既存
├── README.md                                  # ✓ 既存
├── .claude/                                   # ✓ rules / agents / skills 一通り
│   ├── rules/                                 # 6 本（drafter-preflight / file-growth /
│   │                                          #   learning-capture / kakuyomu-policy /
│   │                                          #   story-os-boundaries /
│   │                                          #   reviewer-gate-b + monitoring-dictionary）
│   ├── agents/                                # 18 本
│   └── skills/                                # 7 本
├── bible/                                     # ✓ 一部
│   ├── characters.md                          # 旧 v3 形式
│   ├── world.md                               # 旧 v3 形式
│   ├── rules.md                               # 旧 v3 形式
│   └── ia_story_bible_v2/                     # ★ 50+ ファイル（外部完成 package）
│       ├── 00_README.md
│       ├── 01_CORE_CANON.md
│       ├── ... (49 + α)
│       └── 22-49_EPISODE_FULL_DRAFT.md (18 本)
├── arcs/                                      # ✓ series-overview + arc-01
├── packets/                                   # ✓ exploring/scoped/frozen
├── community/                                 # ✓
├── learning/                                  # ✓
├── actions/                                   # 旧名（v4 では backlog/）
│   └── proposed/like-template.yaml
├── campaigns/                                 # ✓
└── prompts/                                   # work 固有 prompt
```

**致命的な状態**:
- `bible/ia_story_bible_v2/` 配下に **EPISODE_FULL_DRAFT が 18 本同居**（論点 2 違反）
- v4 で要求されるディレクトリの一部不在: `inbox/` `adapter/` `synthesis/` `design/` `state/` `drafts/` `reviews/` `approved/` `published/` `backlog/`（actions/ から rename 必要）
- `story/kernel.yaml` 不在
- 50+ ファイルが 1 ディレクトリに混在

---

## 2. DoR-A 判定（06 適用）

`07_review_prompts/bible-readiness-review.md` を回した結果:

```yaml
bible_readiness_review:
  work_root: "works/ia_society"
  
  directory_structure:
    pass: false
    missing:
      - "{work}/inbox/"
      - "{work}/adapter/"
      - "{work}/synthesis/"
      - "{work}/design/"
      - "{work}/state/"
      - "{work}/drafts/"
      - "{work}/reviews/"
      - "{work}/approved/"
      - "{work}/published/"
      - "{work}/backlog/"  # actions/ をリネーム
      - "{work}/scenes/"
  
  kernel_completeness:
    pass: false
    schema_version: "missing"
    must_filled: 0/28
    issues: ["story/kernel.yaml が存在しない"]
  
  bible_facet_completeness:
    must_facets:
      logline: ✗  # ia_story_bible_v2/01_CORE_CANON.md に "ひとことでの核" あり、要切り出し
      promise: ✗  # 同上
      theme: ✗   # 暗黙、要明文化
      rules: △   # 旧 bible/rules.md あり、要 v4 化 + style-voice 分離
      style_voice: ✗
      plot: ✗   # ia_story_bible_v2/08_PLOT_3ACT_AND_20EP.md あり、要切り出し
      world: △   # 旧 bible/world.md + 02_WORLD_SOCIAL_MODEL.md、要 world/ 分割
      characters: △  # 旧 bible/characters.md + 05_CHARACTERS_MAIN_NOVEL.md、要分割
    should_facets:
      system: ✗  # 04_INSTITUTIONS_GLOSSARY.md → bible/system/
      timeline: ✗  # 03 + 15 → bible/timeline/
      cadence: ✗  # 暗黙、要明文化
      foreshadowing_map: ✗  # 07_TRUTH_AND_CLUE_MAP.md → bible/foreshadowing-map.md
      reveal_plan: ✗  # 28_REVEAL_BUDGET_SHEET.md → 二層ファイル化
      motif: ✗  # 29_OBJECT_MOTIF_LADDER.md → 二層ファイル化
      sample_scene: ✗  # 11_SAMPLE_SCENES.md → bible/samples/
  
  consistency:
    contradiction_high: 1  # X-001（湊 170/175 等、27_CONTRADICTION_LOG.md より）
    drafts_in_bible: 18    # 22-49 EPISODE_FULL_DRAFT、★ 致命的
  
  dor_a_pass: false
  
  blockers:
    critical:
      - "story/kernel.yaml 作成必要（v4 schema）"
      - "bible/ia_story_bible_v2/22-49_EPISODE_FULL_DRAFT を drafts/episodes/ に剥がす"
      - "X-001 を Patch lifecycle で解決"
      - "v4 ディレクトリ構造 11 個作成"
      - "ia_story_bible_v2/ 配下 50+ ファイルを bible/ + design/ + state/ に再配置"
```

---

## 3. Intake Coverage（05 適用、86 項目スコア）

```yaml
intake_coverage_review:
  total_items_checked: 86
  
  status_distribution:
    filled: 60  # 既存 ia_story_bible_v2 の充実度は高い（書き出し前の状態として）
    tentative: 8
    intentionally_hidden: 4  # 湊の正体 / 兄妹真相 / 4-2 真意 等
    not_applicable: 0
    contradiction: 1  # X-001
    missing: 13  # 主に物理ファイル不在によるもの（内容は揃っている）
  
  must_coverage: 38/42  # 物理ファイル不在で 4 件 missing
  should_coverage: 22/32
  may_coverage: 8/12
  
  per_section:
    kernel_11:
      logline: { status: missing, content_exists_in: "bible/ia_story_bible_v2/01_CORE_CANON.md" }
      promise: { status: missing, content_exists_in: "bible/ia_story_bible_v2/00_README.md + 06" }
      protagonist_vector: { status: filled (in source) }
      conflict: { status: filled (in source) }
      stakes: { status: filled }
      change_model: { status: filled }
      causality: { status: tentative, source: "10_WRITING_GUIDE_AND_VOICE.md 暗黙" }
      information_design: { status: filled, intended_unknowns: 4件あり }
      emotional_arc: { status: tentative }
      style_voice: { status: filled (in 10_WRITING_GUIDE) }
      unit_tree: { status: filled (in 08_PLOT_3ACT_AND_20EP) }
    
    bible_facets:
      logline: { coverage: 0/1, content_in_source: true }
      promise: { coverage: 0/3, content_in_source: true }
      theme: { coverage: 0/4 }
      rules: { coverage: 4/7 }
      world: { coverage: 5/7 }
      characters: { coverage: 4/6 }
      system: { coverage: 5/6, source: "04_INSTITUTIONS_GLOSSARY.md" }
      timeline_macro: { coverage: 3/3, source: "03_TIMELINE_AND_HISTORY.md" }
      timeline_micro: { coverage: 3/3, source: "15_DAY_BY_DAY_CHRONOLOGY.md" }
      sample_scene: { coverage: 3/3, source: "11_SAMPLE_SCENES.md" }
      plot: { coverage: 4/5, source: "08_PLOT_3ACT_AND_20EP.md" }
      foreshadowing_map: { coverage: 3/3, source: "07_TRUTH_AND_CLUE_MAP.md" }
      reveal_plan: { coverage: 3/3, source: "28_REVEAL_BUDGET_SHEET.md" }
      motif: { coverage: 3/3, source: "29_OBJECT_MOTIF_LADDER.md" }
  
  dor_a_eligible: false
  dor_a_blockers:
    - "Intake Adapter による物理再配置必須"
    - "X-001 解決必須"
    - "EPISODE_FULL_DRAFT 18 本の剥がし"
```

→ **内容としては 86 項目のうち 60+ が source に存在**。問題は物理配置 + drafts 剥がし + kernel 作成。

---

## 4. 物理再配置マップ

`bible/ia_story_bible_v2/` 50+ ファイルの v4 物理位置:

| 旧 | 新 | 種別 |
|---|---|---|
| `00_README.md` | `bible/README.md`（再生成）+ `bible/walkthroughs/reading-order.md` | refactor |
| `01_CORE_CANON.md` | **分割**: `bible/logline.md` + `bible/promise.md` + `bible/theme.md` + kernel.yaml の複数項目 | split |
| `02_WORLD_SOCIAL_MODEL.md` | `bible/world/society.md` | move |
| `03_TIMELINE_AND_HISTORY.md` | `bible/timeline/history.md` | move |
| `04_INSTITUTIONS_GLOSSARY.md` | `bible/system/institutions.md` | move |
| `05_CHARACTERS_MAIN_NOVEL.md` | `bible/characters/{slug}.md` 個別シート群（史弥 / 乃々 / 湊 / 九堂 / 五十嵐 / 水無瀬 / 凪 / 真田 / 茅野） | split |
| `06_OPPOSITION_AND_JUSTICE.md` | `bible/characters/opposition.md` または各キャラシートの "antagonist_logic" セクション | split |
| `07_TRUTH_AND_CLUE_MAP.md` | `bible/foreshadowing-map.md` + kernel.information_design.intended_unknowns | split |
| `08_PLOT_3ACT_AND_20EP.md` | `bible/plot.md` + `arcs/series-overview.md` + `arcs/arc-01.md` etc. | split |
| `09_ACT1_SCENE_CARDS.md` | `scenes/slotted/ep01-{slug}.md` 〜 `ep05-{slug}.md` | split |
| `10_WRITING_GUIDE_AND_VOICE.md` | **分割**: `bible/style-voice.md` + `bible/rules.md` | split |
| `11_SAMPLE_SCENES.md` | `bible/samples/{slug}.md` 個別 | split |
| `12_WORLD_ASSET_POOL_AND_SPINOFFS.md` | `design/world-spinoff-assets.md`（揺れる設計、別作品候補） | move |
| `13_DECISION_LOG_AND_OPEN_QUESTIONS.md` | **分割**: `design/open-questions.md` + `state/decision-log.yaml` | split |
| `14_RELATIONSHIP_ARCS.md` | `bible/characters/relationship-arcs.md`（作品固有 facet として残置可） | move |
| `15_DAY_BY_DAY_CHRONOLOGY.md` | `bible/timeline/day-by-day.md` | move |
| `16_ACT2_ACT3_SCENE_SEEDS.md` | `scenes/slotted/ep06-{slug}.md` 〜 `ep20-{slug}.md`（seed 形式から scene card に格上げ） | split |
| `17_PACKAGE_REVIEW_AND_GAPS.md` | `reviews/audits/2025-XX-XX-package-review.md` | move |
| `18_DRAFT_FLOW_AND_LOCKS.md` | `.claude/rules/drafter-preflight.md` 補強 + `bible/walkthroughs/draft-flow.md` | split |
| `19_LINE_LEVEL_CLUE_PAYOFF_TABLE.md` | `state/foreshadowing-implementation.yaml` | convert |
| `20_PLATFORM_HANDOFF_GUIDE.md` | `bible/walkthroughs/platform-handoff.md` | move |
| `21_PACKAGE_AUDIT_V3.md` | `reviews/audits/2025-XX-XX-audit-v3.md` | move |
| `22-49_EPISODE_FULL_DRAFT.md` (18 本) | **`drafts/episodes/{ep_id}-{slug}.md`** | move（Bible から剥がす） |
| `23_DETAILED_DESIGN_TASK_BACKLOG.md` | `backlog/`（個別 task 化） | split |
| `24_ACTIVE_QUEUE.md` | `backlog/active.yaml` または `backlog/`（active 部分のみ） | move |
| `25_REVIEW_OPERATIONS_AND_GATES.md` | **分割**: `.claude/rules/review-operations.md` + `reviews/templates/` | split |
| `26_CANON_PATCH_LOG.md` | `state/canon-patch-log.yaml` | move |
| `27_CONTRADICTION_LOG.md` | `state/contradiction-log.yaml` | move |
| `28_REVEAL_BUDGET_SHEET.md` | `bible/reveal-budget.md`（**二層ファイル**: 上 Bible / 下 State） | convert |
| `29_OBJECT_MOTIF_LADDER.md` | `bible/motif-ladder.md`（**二層ファイル**） | convert |
| `30_EP19_REPORT_DRAFT.md` | `drafts/episodes/ep19-report.md`（**剥がし**） | move |
| `50_BACKLOG_CONSTRAINT_MEMO.md` | `design/design-debt.yaml` | convert |
| `51_PUBLISHED_PACKAGE_PREP.md` | `bible/walkthroughs/release-prep.md` | move |
| `52_PUBLISHED_PACKAGE_CLOSEOUT.md` | `bible/walkthroughs/release-closeout.md` | move |
| `53_KAKUYOMU_POSTING_PROJECT.md` | `community/kakuyomu-posting.md` + `backlog/` 個別タスク | split |
| `54_KAKUYOMU_PERSONA_REVIEW_PROMPTS.md` | `reviews/templates/persona-review-template.md`（既存 template に統合） | move |
| `55_KAKUYOMU_REVIEW_INTEGRATION_LEDGER.md` | `state/kakuyomu-review-integration.yaml` | convert |
| `99_MANIFEST.md` | `bible/walkthroughs/manifest.md` または不要（README で代替） | optional |
| `PACKAGE_MANIFEST.json` | 不要（archive） | archive |
| `IA_STORY_BIBLE_MASTER.md` | 不要（分割版が正本になるため） | archive |

合計:
- move: 約 18 ファイル
- split: 約 12 ファイル → 30+ ファイル
- convert（フォーマット変換）: 約 6 ファイル
- archive: 3 ファイル

---

## 5. 作品固有 facet の扱い

ia_society 固有の概念を template に流入させない:

| 概念 | 扱い |
|---|---|
| **Relationship Arcs** | 作品固有として `bible/characters/relationship-arcs.md` に残置（Character facet 拡張） |
| **章末公文書 / 4-2 の空欄** | `bible/in-world-documents/`（作品固有 facet）に残置、template に積まない |
| **白紙日カウントダウン** | World facet 内、template には積まない |
| **147 / 適性値** | World facet 内、template には積まない |
| **真耕特区 / 県営勤養施設 / 生身接触施設 / 劇務圏** | World 内 locations、template には積まない |
| **三層対応**（仮にあれば） | 作品固有、template に流入禁止 |
| **Reveal Budget の二層運用** | template に積む（汎用パターン）、運用は作品依存 |

---

## 6. Migration Step 順序

### Step 1: 退避（不可逆操作の前に）

```bash
# 既存全体を archive（safety net）
cp -r works/ia_society/ archive/2026-04-30-ia_society-pre-v4/
```

### Step 2: ディレクトリ作成

不在ディレクトリを 11 個作成:
```bash
cd works/ia_society/
mkdir -p inbox adapter synthesis design state drafts reviews approved published backlog
mkdir -p bible/world bible/characters bible/system bible/timeline bible/samples bible/walkthroughs
mkdir -p design/canon-patch-proposals
mkdir -p reviews/contracts reviews/audits reviews/templates
mkdir -p scenes/seed scenes/slotted scenes/superseded
```

### Step 3: actions/ → backlog/ リネーム

```bash
mv actions/ backlog/
# proposed/ サブを解体してフラット化
mv backlog/proposed/* backlog/
rmdir backlog/proposed/
```

### Step 4: bible/ia_story_bible_v2/ の Intake Adapter 実行

```bash
# 50+ ファイルを inbox に複製
cp -r bible/ia_society_v2/* inbox/planning_sessions/2026-04-30_v2_import/

# Intake Adapter prompt 実行（手動）
# → synthesis/session_digests/2026-04-30_v2_import.md 生成
# → synthesis/update_proposals/ に facet 別 proposal 群生成
```

### Step 5: kernel.yaml 作成

`StoryTemplateEvolution/current/templates/story/kernel.template.yaml` をコピーして:
- schema_version: "v4"
- 11 項目を `01_CORE_CANON.md` 由来で埋める
- intentionally_unknowns 4 件を information_design に追記

### Step 6: 物理再配置（Section 4 のマップに従う）

facet ごとに段階的に実行:
1. world 系（02 + 旧 world.md → bible/world/）
2. characters 系（05 + 06 + 旧 characters.md → bible/characters/）
3. system 系（04 → bible/system/）
4. timeline 系（03 + 15 → bible/timeline/）
5. plot 系（08 → bible/plot.md + arcs/）
6. style / rules（10 → bible/style-voice.md + bible/rules.md）
7. samples（11 → bible/samples/）
8. foreshadowing / reveal / motif（07, 28, 29 → 二層ファイル化）

### Step 7: EPISODE_FULL_DRAFT 18 本の剥がし

```bash
# 22-49 を drafts に移動（リネーム必要）
mv bible/ia_society_v2/22_EPISODE_01_FULL_DRAFT.md drafts/episodes/ep01-tsuchi-wo-suteinai.md
mv bible/ia_society_v2/33_EPISODE_02_FULL_DRAFT.md drafts/episodes/ep02-{slug}.md
# ... 18 本
```

各 draft の冒頭に meta 欄（drafter-preflight 準拠）を追記。

### Step 8: 各種 log の移行

- 26 → state/canon-patch-log.yaml
- 27 → state/contradiction-log.yaml
- 13 を 2 分割 → design/open-questions.md + state/decision-log.yaml
- 50 → design/design-debt.yaml
- 19 → state/foreshadowing-implementation.yaml

### Step 9: X-001 の Patch lifecycle

`design/canon-patch-proposals/patch-001-X001-resolution.md` 起票 → author Approval → bible 反映。

### Step 10: 検証

`07_review_prompts/bible-readiness-review.md` を実行し DoR-A 通過判定。

---

## 7. 想定リスク

| リスク | 対策 |
|---|---|
| **物理再配置で参照リンク断**（旧パス参照が drafts や reviews に残る） | grep で旧パス検索、置換後に検証 |
| **ia_society_v2 の 50 ファイル全 archive 漏れ** | Step 1 で必ず archive を取る |
| **二層ファイル化（28, 29）で情報欠落** | format 変換 script を書いて diff 検証 |
| **18 EPISODE_FULL_DRAFT の meta 欄未記入** | 各 draft で drafter-preflight を遡及適用 |
| **X-001 解決中に他の contradiction が顕在化** | contradiction-log を定期 audit |
| **kernel.yaml の status 振り分けミス** | `kernel-fill-review.md` を全項目に適用 |
| **作品固有 facet（章末文書 / 三層）が template に流入** | 移行ガイドに明記、generic template への流入を禁止 |

---

## 8. 完了条件

- ✅ DoR-A 通過（`bible-readiness-review.md` が pass: true）
- ✅ X-001 解決済み（state/canon-patch-log に entry）
- ✅ 全 EPISODE_FULL_DRAFT が drafts/ にあり、bible に存在しない
- ✅ ia_society_v2/ ディレクトリが空（中身なし）か archive 済み
- ✅ 物理ファイル数が概ね v4 に整合（bible facet 17 体制）
- ✅ kernel.yaml v4 schema で全 MUST 28 項目埋まり

完了所要時間目安: **8-16 時間**（人間 + LLM 協働）。Intake Adapter を batch 実行できれば短縮可。
