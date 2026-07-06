# 08-fools_with_cheating — 作品固有 facet の保持 + generic 雛形への流入抑止

> **対象**: `works/fools-with-cheating/`
> **状態**: raw 35 ファイル + bible 充実 + adapter 整備済 + 作品固有 facet（三層対応 / 章末資料 / 批評性）
> **検証目的**: 充実した bible を持つ work で「作品固有 facet を template に流入させない」判断ができるか。

---

## 1. 現状サマリ

```
works/fools-with-cheating/
├── CLAUDE.md                                  # ✓ v3 形式、詳細
├── README.md                                  # ✓
├── .claude/                                   # ✓
│   ├── rules/
│   │   ├── drafter-preflight.md
│   │   ├── file-growth.md
│   │   ├── learning-capture.md
│   │   ├── kakuyomu-policy.md
│   │   └── story-os-boundaries.md
│   ├── agents/
│   └── skills/
├── .adapter/                                  # ★ work 固有 adapter（v4 では .adapter → adapter）
│   ├── intake_adapter_prompt.md
│   ├── folder_structure.md
│   ├── source_mapping.yaml
│   └── update_proposal_format.yaml
├── bible/
│   ├── premise.md                             # 旧名（→ logline.md）
│   ├── reader_promise.md                      # 旧名（→ promise.md）
│   ├── theme.md                               # ✓
│   ├── genre.md                               # 旧名（→ genre-overlay.md）
│   ├── style_guide.md                         # 旧名（→ style-voice.md + rules.md）
│   ├── characters/                            # ✓ 充実
│   │   ├── protagonist_renji.md
│   │   ├── satellites_10.md
│   │   ├── antagonists_15.md
│   │   ├── individual/                        # 32 ファイル
│   │   └── renji_voice_catalog.md
│   ├── world/
│   │   ├── three_layer_principle.md           # ★ 作品固有 facet
│   │   ├── ability_seitouka_ken.md            # 正当化圏（System 寄り）
│   │   ├── locations.md
│   │   └── maou_territory.md
│   ├── plot/
│   │   ├── arc_map.md
│   │   ├── promotion_route.md
│   │   ├── episode_plan.md
│   │   ├── episode_details_arc2-6.md
│   │   ├── three_layer_table.md               # ★ 作品固有 facet
│   │   ├── scene_cards.md
│   │   └── scene_cards_arc2-6.md
│   └── in_world_documents/                    # ★ 作品固有 facet（章末資料）
│       ├── samples.md
│       ├── samples_arc2-6.md
│       └── placement_table_arc2-6.md
├── design/
│   ├── project_principles.md
│   ├── critical_intent.md                     # ★ 作品固有 facet（批評性シート）
│   ├── editorial_notes.md
│   ├── checklists.md
│   ├── idea_provenance.md
│   ├── timeline_state_policy.md
│   └── audits/                                # 6 ファイル
├── state/
│   ├── timeline.yaml
│   ├── character_states.yaml
│   ├── foreshadowing.yaml
│   ├── three_layer_status.yaml                # ★ 作品固有
│   ├── continuity_notes.yaml
│   ├── open_questions.md
│   └── rejected_ideas.md
├── raw/                                       # ★ 35 ファイル（旧 renji_novel_bible）
├── synthesis/                                 # 構造のみ（中身少ない）
├── arcs/                                      # 構造のみ
├── packets/
├── scenes/
├── drafts/
│   └── episodes/
├── reviews/
├── writing/
│   └── episode_packs/                         # ep001 〜 ep072 の skeleton
├── prompts/
├── learning/
└── inbox/
    └── planning_sessions/
```

**特徴**:
- 既に v3 構造に近い形（`bible/` `design/` `state/` 分離済み）
- raw/ に 35 ファイルが**保持**されている（典型的な intake source）
- `.adapter/`（dot あり、v4 では `adapter/`）
- 作品固有 facet が 4 つある: 三層対応 / 章末資料 / 正当化圏 / 批評性シート
- 個別キャラシート 32 ファイル（充実）
- writing/episode_packs/ の skeleton が 72 ep 分既に存在

---

## 2. DoR-A 判定（06 適用）

```yaml
bible_readiness_review:
  work_root: "works/fools-with-cheating"
  
  directory_structure:
    pass: false
    missing:
      - "{work}/approved/"
      - "{work}/published/"
      - "{work}/backlog/"  # 不在 or 未活用
    rename_required:
      - ".adapter/" → "adapter/"
      - "bible/premise.md" → "bible/logline.md"
      - "bible/reader_promise.md" → "bible/promise.md"
      - "bible/genre.md" → "bible/genre-overlay.md"
      - "bible/style_guide.md" → "bible/style-voice.md" + "bible/rules.md"
  
  kernel_completeness:
    pass: false
    schema_version: "missing"  # kernel.yaml そのものが不在
    must_filled: 0/28
  
  bible_facet_completeness:
    must_facets:
      logline: △  # bible/premise.md → リネーム
      promise: △  # bible/reader_promise.md → リネーム
      theme: ✓
      rules: △  # style_guide.md と分離要
      style_voice: △  # 同上
      plot: △  # bible/plot/ あり、bible/plot.md に集約 or 維持
      world: ✓
      characters: ✓ (充実、個別シート 32)
    should_facets:
      system: △  # ability_seitouka_ken / 章末資料制度 → bible/system/ に集約可
      timeline: ✗  # 不在、要構築（raw/20_時系列_昇進年表 から）
      cadence: ✗
      foreshadowing_map: ✗  # 未作成、raw から構築要
      reveal_plan: ✗  # 未作成
      motif: △  # 章末資料が事実上 motif として機能しているが、明示なし
      sample_scene: △  # raw/26_本文文体サンプル集 → bible/samples/ に移行可
    
    work_specific_facets_detected:
      - "三層対応（real / 認識 / 公的記録）"
      - "章末資料制度（in_world_documents）"
      - "正当化圏仕様（System 寄り、作品固有装置）"
      - "批評性シート（design/critical_intent.md）"
  
  consistency:
    contradiction_high: 要確認（design/audits/ にレポートあり）
  
  dor_a_pass: false
  
  blockers:
    critical:
      - "kernel.yaml v4 schema 作成"
      - "bible/premise → logline 等のリネーム"
      - "bible/style_guide → style-voice + rules 分割"
      - "foreshadowing-map / reveal-plan / cadence-plan / motif-ladder 構築"
    deferred_acceptable:
      - "Timeline → raw から構築（後追いで OK）"
      - "Sample Scene → raw/26 を移行"
    work_specific_handling:
      - "三層対応は作品固有 facet として bible/three-layer/ に独立 facet 化"
      - "章末資料は bible/in-world-documents/ に独立 facet 化"
      - "批評性シートは design/critical-intent.md 維持"
```

---

## 3. Intake Coverage（05 適用、86 項目スコア）

```yaml
intake_coverage_review:
  total_items_checked: 86
  
  status_distribution:
    filled: 65  # bible 充実度高い
    tentative: 8
    deferred: 4
    not_applicable: 0
    intentionally_hidden: 6  # raw/14 三層対応で意図的非開示が多数
    missing: 3
  
  must_coverage: 40/42  # 高い
  should_coverage: 22/32
  may_coverage: 9/12
  
  per_section:
    kernel_11:
      logline: { status: filled, content_in: "bible/premise.md" → リネーム }
      promise: { status: filled, content_in: "bible/reader_promise.md" → リネーム }
      protagonist_vector: { status: filled, content_in: "bible/characters/protagonist_renji.md" }
      conflict: { status: filled, content_in: "raw/22_正当な対抗者" }
      stakes: { status: filled }
      change_model: { status: filled, content_in: "raw/03_人物設定" }
      causality: { status: filled }
      information_design: { status: filled, intended_unknowns: "三層対応で大量" }
      emotional_arc: { status: tentative }
      style_voice: { status: filled }
      unit_tree: { status: filled }  # 6 アーク × 12 話 = 72 ep
    
    bible_facets:
      world: { coverage: 7/7 }
      characters: { coverage: 6/6, individual_sheets: 32 }
      system: { coverage: 5/6, source: "ability_seitouka_ken / 章末資料制度" }
      foreshadowing_map: { coverage: 0/3, source_in_raw: "raw/15 + 19" }
      reveal_plan: { coverage: 0/3, source_in_raw: "raw/14 + 28" }
      motif: { coverage: 1/3, source_in_raw: "章末資料 = motif" }
      
      # 作品固有
      three_layer: { coverage: 充実、bible/world/three_layer_principle.md + bible/plot/three_layer_table.md }
      in_world_documents: { coverage: 充実、bible/in_world_documents/ }
      critical_intent: { coverage: 充実、design/critical_intent.md }
  
  dor_a_eligible: false（リネーム + 不足 facet 構築必要）
```

→ **fools-with-cheating は 86 項目のうち 65 が filled**。コア部分は揃っているが、リネーム作業と不足 facet（foreshadowing-map / reveal-plan）の構築が必要。

---

## 4. 物理再配置マップ

| 旧位置 | 新位置 | 種別 |
|---|---|---|
| `.adapter/` | `adapter/`（dot 削除）| rename |
| `bible/premise.md` | `bible/logline.md` | rename |
| `bible/reader_promise.md` | `bible/promise.md` | rename |
| `bible/genre.md` | `bible/genre-overlay.md` | rename |
| `bible/style_guide.md` | **分割**: `bible/style-voice.md` + `bible/rules.md` | split |
| `bible/theme.md` | keep | keep |
| `bible/world/three_layer_principle.md` | `bible/three-layer/principle.md`（作品固有 facet として独立）| move |
| `bible/world/ability_seitouka_ken.md` | `bible/system/ability_seitouka_ken.md`（System facet 配下）| move |
| `bible/world/locations.md` | keep（in `bible/world/locations.md`）| keep |
| `bible/world/maou_territory.md` | `bible/world/locations/maou_territory.md`（locations 配下に）| move |
| `bible/characters/protagonist_renji.md` | keep | keep |
| `bible/characters/satellites_10.md` | keep | keep |
| `bible/characters/antagonists_15.md` | keep | keep |
| `bible/characters/individual/`（32 ファイル）| keep | keep |
| `bible/characters/renji_voice_catalog.md` | `bible/characters/voice-catalog.md`（slug 統一）| rename |
| `bible/plot/arc_map.md` | `arcs/arc-map.md`（Bible から arcs/ へ）| move |
| `bible/plot/promotion_route.md` | `bible/system/promotion-route.md`（出世制度 = System）| move |
| `bible/plot/episode_plan.md` | `arcs/episode-plan.md` | move |
| `bible/plot/episode_details_arc2-6.md` | `arcs/episode-plan.md` に統合 or `arcs/episode-details-arc2-6.md` | move |
| `bible/plot/three_layer_table.md` | `bible/three-layer/table.md`（作品固有）| move |
| `bible/plot/scene_cards.md` `bible/plot/scene_cards_arc2-6.md` | `scenes/slotted/`（個別 ep 単位）| split |
| `bible/in_world_documents/samples.md` | `bible/in-world-documents/samples.md`（作品固有 facet 維持）| move |
| `bible/in_world_documents/samples_arc2-6.md` | 同上 | move |
| `bible/in_world_documents/placement_table_arc2-6.md` | `bible/in-world-documents/placement.md` + `state/in-world-documents-placement.yaml`（二層化）| split |
| `design/project_principles.md` | keep | keep |
| `design/critical_intent.md` | keep（作品固有 facet）| keep |
| `design/editorial_notes.md` | keep | keep |
| `design/checklists.md` | keep | keep |
| `design/idea_provenance.md` | keep | keep |
| `design/timeline_state_policy.md` | `bible/timeline/policy.md` または `design/` keep | keep or move |
| `design/audits/` | `reviews/audits/` に移動 | move |
| `state/timeline.yaml` | `state/timeline-state.yaml`（slug 統一）| rename |
| `state/character_states.yaml` | `state/character-states.yaml` | rename |
| `state/foreshadowing.yaml` | `state/foreshadowing-implementation.yaml` | rename |
| `state/three_layer_status.yaml` | `state/three-layer-status.yaml`（作品固有）| rename |
| `state/continuity_notes.yaml` | `state/contradiction-log.yaml` に統合 or 維持 | merge |
| `state/open_questions.md` | `design/open-questions.md` に移動 | move |
| `state/rejected_ideas.md` | `design/rejected-ideas.md` に移動 | move |
| `raw/`（35 ファイル）| `inbox/planning_sessions/2026-04-XX_renji_legacy/` または `raw/` keep（既に inbox 相当）| keep |
| `synthesis/` | keep | keep |

新規作成:
- `story/kernel.yaml`（v4）
- `bible/cadence-plan.md`
- `bible/foreshadowing-map.md`（raw/15, raw/19 から構築）
- `bible/reveal-plan.md`（raw/14, raw/28 から構築）
- `bible/motif-ladder.md`（章末資料を motif として明示化）
- `bible/samples/`（raw/26 から構築）
- `bible/timeline/`（raw/20 から構築）
- `state/decision-log.yaml` `state/canon-patch-log.yaml`
- 各 README.md

---

## 5. 作品固有 facet の扱い

fools-with-cheating の作品固有装置を **template に流入させず**、work bible 内に独立 facet として保持:

| 作品固有概念 | 配置 | template 流入 |
|---|---|---|
| **三層対応**（真実 / 認識 / 公的記録） | `bible/three-layer/principle.md` + `bible/three-layer/table.md` + `state/three-layer-status.yaml`（作品固有 facet） | **NO**（generic に持ち上げない） |
| **章末資料制度**（in-world documents） | `bible/in-world-documents/` 配下 | **NO** |
| **正当化圏仕様**（ability_seitouka_ken） | `bible/system/ability_seitouka_ken.md`（System facet の作品固有実装）| **NO**（System は generic facet だが中身は作品固有） |
| **批評性シート**（critical_intent） | `design/critical_intent.md` | **NO**（design 配下の作品固有メモ） |
| **促進路 promotion_route** | `bible/system/promotion-route.md` | **NO**（System の作品固有実装） |
| **POV 運用表 18_POV運用表.md** | `bible/style-voice.md` の "POV 運用" セクション + 必要時 `bible/style/pov-rules.md` 分割 | **PARTIAL**（POV 運用は generic 概念だが本作の表は固有） |
| **レンジ嫌悪モノローグ 21** | `bible/style-voice.md` の "voice samples" セクションまたは `bible/samples/voice-samples-renji.md` | **NO** |
| **害悪パターン 08** | `bible/rules.md` の "forbidden voice patterns" | **PARTIAL** |

**結論**: fools-with-cheating の固有装置は強力だが、generic template には流入させない。各装置は work の bible / design 内に独立 facet として残置する。

---

## 6. Migration Step 順序

### Step 1: 退避

```bash
cp -r works/fools-with-cheating/ archive/2026-04-30-fools-pre-v4/
```

### Step 2: ディレクトリ作成 + リネーム

```bash
cd works/fools-with-cheating/
mkdir -p approved published backlog
mkdir -p bible/system bible/timeline bible/samples bible/walkthroughs bible/three-layer bible/in-world-documents
mkdir -p reviews/contracts reviews/audits reviews/templates
mv .adapter adapter
```

### Step 3: bible リネーム群

```bash
mv bible/premise.md bible/logline.md
mv bible/reader_promise.md bible/promise.md
mv bible/genre.md bible/genre-overlay.md
# style_guide は分割（手作業）
```

### Step 4: style_guide.md の分割

`bible/style_guide.md` を読み:
- 「目指す声」「POV」「tense」「register」「sentence length」「temperature」→ `bible/style-voice.md`
- 「禁則」「forbidden words」「forbidden situations」「dialogue conventions（禁則部分）」→ `bible/rules.md`

旧 style_guide.md を `archive/2026-04-30-fools-style-guide.md` に退避。

### Step 5: bible/world/ と bible/plot/ の整理

- `bible/world/three_layer_principle.md` → `bible/three-layer/principle.md`
- `bible/world/ability_seitouka_ken.md` → `bible/system/ability_seitouka_ken.md`
- `bible/plot/arc_map.md` → `arcs/arc-map.md`
- `bible/plot/episode_plan.md` → `arcs/episode-plan.md`
- `bible/plot/three_layer_table.md` → `bible/three-layer/table.md`
- `bible/plot/scene_cards.md` → `scenes/slotted/` に分割（手作業 or scripts）
- `bible/plot/promotion_route.md` → `bible/system/promotion-route.md`

### Step 6: in_world_documents の整理

- `bible/in_world_documents/` → `bible/in-world-documents/`（slug 統一）
- `placement_table_arc2-6.md` を **二層ファイル化**（`bible/in-world-documents/placement.md` + `state/in-world-documents-placement.yaml`）

### Step 7: state リネーム

```bash
mv state/timeline.yaml state/timeline-state.yaml
mv state/character_states.yaml state/character-states.yaml
mv state/foreshadowing.yaml state/foreshadowing-implementation.yaml
mv state/three_layer_status.yaml state/three-layer-status.yaml
mv state/open_questions.md design/open-questions.md
mv state/rejected_ideas.md design/rejected-ideas.md
# state/decision-log.yaml と state/canon-patch-log.yaml を新規作成
touch state/decision-log.yaml state/canon-patch-log.yaml state/contradiction-log.yaml
```

### Step 8: design/audits の移動

```bash
mv design/audits reviews/audits-fools-design
# 各ファイルを reviews/audits/{date}-{scope}.md にリネーム
```

### Step 9: 不足 facet 構築

raw からの抽出で:
- `bible/foreshadowing-map.md` 作成（raw/15, raw/19 を Intake Adapter 経由で）
- `bible/reveal-plan.md` 作成（raw/14, raw/28 から）
- `bible/motif-ladder.md` 作成（章末資料を motif として明示）
- `bible/cadence-plan.md` 作成（簡略でも可）
- `bible/timeline/history.md` 作成（raw/20 から）
- `bible/samples/` 構築（raw/26 から）

### Step 10: kernel.yaml 作成

v4 schema、bible facet と sync。

### Step 11: 検証

`07_review_prompts/bible-readiness-review.md` で DoR-A 判定。

---

## 7. 想定リスク

| リスク | 対策 |
|---|---|
| **作品固有 facet（三層 / 章末資料 / 批評性）が generic template に流入** | 移行ガイドに明記、template への取り込み禁止を確認 |
| **個別キャラシート 32 ファイルの参照断** | リネーム時に grep で参照確認 |
| **scene_cards.md 100 枚の分割で手作業負荷大** | LLM script で auto split + 検証 |
| **二層ファイル化で format 変換ミス** | template に従って書き直し、diff 検証 |
| **renji 命名が固有名（renji_voice_catalog 等）に残る** | slug 統一は段階的に、参照断を防ぐため |
| **raw/ を inbox に移動するか raw/ keep するか** | 既存 raw/ は keep（既に inbox 相当として機能、変更コスト > 利益）|
| **三層対応で intentionally_hidden 多数 → kernel.information_design に大量登録** | 6+ 件を整理して kernel に登録、bible 本文には書かない |

---

## 8. 完了条件

- ✅ DoR-A 通過
- ✅ `.adapter/` → `adapter/` リネーム完了
- ✅ bible/premise → logline 等のリネーム完了
- ✅ style_guide → style-voice + rules 分割完了
- ✅ 作品固有 facet が `bible/three-layer/` `bible/in-world-documents/` 配下に独立配置
- ✅ generic template に作品固有概念が流入していない（要 audit）
- ✅ kernel.yaml v4 で全 MUST 28 項目埋まり

完了所要時間目安: **6-12 時間**（個別キャラシート 32 + scene_cards 100 の参照確認に時間がかかる）。
