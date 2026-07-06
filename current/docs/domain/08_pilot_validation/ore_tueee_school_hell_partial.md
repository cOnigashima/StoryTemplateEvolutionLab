# 08-ore_tueee_school_hell — 中間状態のマージ + v3→v4 リネーム

> **対象**: `works/ore_tueee_school_hell/`
> **状態**: seed 8 ファイル + bible v1（4-6 ファイル）+ packets/000-003 frozen + handover_v2 構造
> **検証目的**: v3 で書き始めた中間状態の work を v4 にスムーズに移行できるか。

---

## 1. 現状サマリ

```
works/ore_tueee_school_hell/
├── CLAUDE.md                                  # ✓ 既存（v3 形式）
├── README.md                                  # ✓
├── 企画書v0.9.md                              # ★ work-root に企画書（変則）
├── .claude/                                   # ✓ rules / skills 一通り
│   └── rules/                                 # 5 本（craft-methodology / drafter-preflight /
│                                              #   file-growth / kakuyomu-policy /
│                                              #   story-os-boundaries）
├── bible/
│   ├── characters.md                          # 旧 v3
│   ├── world.md                               # 旧 v3
│   ├── rules.md                               # 旧 v3
│   ├── series-bible-v1.md                     # ★ 1 枚版
│   ├── system-bible-v1.md                     # ★ 制度バイブル 1 枚版
│   ├── character-sheets-v1.md                 # ★ キャラフルシート
│   ├── world-regulars-v1.md                   # ★ 7 世界レギュラー
│   ├── dialogue-bible-v1.md                   # ★ 会話バイブル
│   └── templates/                             # 雛形群
├── arcs/
│   ├── series-overview.md
│   ├── arc-01.md / arc-02.md / arc-03.md
│   ├── 100ep-chapter-list.md
│   └── arc-01-checkpoint-ep30.md
├── packets/
│   ├── frozen/packet-000 〜 003                # ★ 4 つ frozen 済み
│   ├── scoped/
│   ├── exploring/
│   └── templates/
├── scenes/
│   └── seed/scene-template.md
├── story/
│   ├── promises.md                            # v3 形式
│   ├── open-questions.md
│   ├── design-debt.yaml
│   ├── seeds/                                 # 8 ファイル
│   ├── canon-patch-proposals/
│   ├── foreshadowing-ledger.md                # 既存
│   └── handover_v2/                           # ★ 移行用構造
│       ├── canon/
│       ├── archive/
│       └── working/
├── reviews/
├── learning/                                  # craft methodology 関連
├── community/
├── actions/                                   # 旧名
│   ├── roadmap.md
│   └── design-audit.md
└── prompts/                                   # work 固有
```

**特徴**:
- bible/ に v1 形式（`*-bible-v1.md` の 1 枚版）が混在
- packets/000-003 が frozen 済み = 既に Packet 設計が進んでいる
- handover_v2/ で前回セッション間の引き継ぎ構造あり
- `企画書v0.9.md` が work-root に変則配置

---

## 2. DoR-A 判定（06 適用）

```yaml
bible_readiness_review:
  work_root: "works/ore_tueee_school_hell"
  
  directory_structure:
    pass: false
    missing:
      - "{work}/inbox/"
      - "{work}/adapter/"
      - "{work}/synthesis/"
      - "{work}/design/"  # story/ 内にあるが design/ ディレクトリは別建て必要
      - "{work}/state/"   # 同上
      - "{work}/drafts/"
      - "{work}/approved/"
      - "{work}/published/"
      - "{work}/backlog/"  # actions/ をリネーム
  
  kernel_completeness:
    pass: false
    schema_version: "missing"  # kernel.yaml そのものが不在
    must_filled: 0/28
  
  bible_facet_completeness:
    must_facets:
      logline: ✗  # 企画書v0.9.md に "1行ログライン" あり、要切り出し
      promise: △  # story/promises.md → bible/promise.md に移動
      theme: ✗   # 企画書から抽出
      rules: △   # bible/rules.md あり、要 v4 化
      style_voice: ✗  # rules.md と分離要
      plot: ✗   # arcs/100ep-chapter-list.md と series-bible-v1 から構成
      world: △   # world.md + world-regulars-v1.md 統合
      characters: △  # characters.md + character-sheets-v1.md 統合
    should_facets:
      system: △   # system-bible-v1.md → bible/system/
      timeline: ✗  # 不在 or not_applicable
      cadence: ✗
      foreshadowing_map: △  # story/foreshadowing-ledger.md あり
      reveal_plan: ✗
      motif: ✗
      sample_scene: ✗  # 未作成、deferred 可
  
  consistency:
    contradiction_high: 要確認
    open_questions_blockers: 要確認
  
  dor_a_pass: false
  
  blockers:
    critical:
      - "story/kernel.yaml 作成（v4 schema）"
      - "v1 形式の `*-bible-v1.md` 群を facet 別に分割"
      - "actions/ を backlog/ にリネーム"
      - "design/ と state/ ディレクトリ作成"
      - "premise → logline リネーム"
    deferred_acceptable:
      - "Sample Scene → SHOULD なので deferred 可"
      - "Timeline → not_applicable 可（学園もので時系列重要度低い場合）"
```

---

## 3. Intake Coverage（05 適用、86 項目スコア）

```yaml
intake_coverage_review:
  total_items_checked: 86
  
  status_distribution:
    filled: 50  # 中程度
    tentative: 15
    deferred: 5
    not_applicable: 3
    missing: 13
  
  must_coverage: 30/42
  should_coverage: 18/32
  may_coverage: 5/12
  
  per_section:
    kernel_11:
      logline: { status: missing, content_in: "企画書v0.9.md" }
      promise: { status: tentative, content_in: "story/promises.md" }
      protagonist_vector: { status: filled, content_in: "character-sheets-v1.md" }
      conflict: { status: filled, content_in: "series-bible-v1.md" }
      stakes: { status: tentative }
      change_model: { status: filled }
      causality: { status: tentative }
      information_design: { status: tentative }
      emotional_arc: { status: tentative }
      style_voice: { status: filled (in dialogue-bible-v1 + rules.md) }
      unit_tree: { status: filled (100 ep 3 arc 構造) }
    
    bible_facets:
      world: { coverage: 5/7 }
      characters: { coverage: 5/6 }
      system: { coverage: 5/6 (system-bible-v1) }
      foreshadowing_map: { coverage: 2/3 (foreshadowing-ledger) }
      ...
  
  dor_a_eligible: false（v4 化作業必要）
```

---

## 4. 物理再配置マップ

| 旧位置 | 新位置 | 種別 |
|---|---|---|
| `企画書v0.9.md`（work-root 変則） | **分割**: `bible/logline.md` + `bible/promise.md` 補強 + `bible/theme.md` + kernel.yaml の複数項目 + `design/genesis-doc.md`（記録として archive） | split |
| `bible/characters.md` + `bible/character-sheets-v1.md` | **統合 + 分割**: `bible/characters/{slug}.md` 個別シート群 | merge & split |
| `bible/world.md` + `bible/world-regulars-v1.md` | **統合 + 分割**: `bible/world/overview.md` + `bible/world/regulars.md` | merge & split |
| `bible/rules.md` | **分割**: `bible/style-voice.md` + `bible/rules.md`（禁則のみ） | split |
| `bible/series-bible-v1.md` | **解体**: 各 facet に分配（logline / promise / theme / world / characters / plot に再配分）+ `bible/walkthroughs/series-overview-v1.md`（履歴として残す） | split & archive |
| `bible/system-bible-v1.md` | `bible/system/overview.md` + 分割した sub-facets | split |
| `bible/dialogue-bible-v1.md` | `bible/style-voice.md` の "dialogue conventions" セクション + `bible/samples/dialogue-samples.md` | split |
| `bible/templates/` | `bible/templates/` 維持、ただし v4 形式に refactor | refactor |
| `arcs/series-overview.md` | keep | keep |
| `arcs/arc-01.md` `arcs/arc-02.md` `arcs/arc-03.md` | keep | keep |
| `arcs/100ep-chapter-list.md` | `arcs/episode-plan.md` または `bible/plot.md` に格上げ | move |
| `arcs/arc-01-checkpoint-ep30.md` | keep | keep |
| `packets/frozen/packet-000 〜 003` | keep（DoR-C 通過済み）| keep |
| `packets/templates/` | keep | keep |
| `scenes/seed/scene-template.md` | keep | keep |
| `story/promises.md` | `bible/promise.md` に rename + 移動 | move + rename |
| `story/open-questions.md` | `design/open-questions.md` に移動 | move |
| `story/design-debt.yaml` | `design/design-debt.yaml` に移動 | move |
| `story/seeds/`（8 ファイル） | keep | keep |
| `story/canon-patch-proposals/` | `design/canon-patch-proposals/` に移動 | move |
| `story/foreshadowing-ledger.md` | `bible/foreshadowing-map.md` + `state/foreshadowing-implementation.yaml`（二層化）| split |
| `story/handover_v2/` | `archive/2026-04-30-handover-v2/` に退避（用途終了） | archive |
| `actions/roadmap.md` | `arcs/manuscript-plan.md` に移動 | move |
| `actions/design-audit.md` | `reviews/audits/{date}-design-audit.md` に移動 | move |
| `actions/` | **`backlog/`** にリネーム（中身は基本空） | rename |
| `learning/craft/*` | keep | keep |

新規作成必要:
- `story/kernel.yaml`（v4 schema）
- `bible/logline.md` `bible/theme.md` `bible/cadence-plan.md` `bible/reveal-plan.md` `bible/motif-ladder.md` `bible/plot.md`
- `bible/timeline/`（または not_applicable 明示）
- `bible/samples/`（または deferred 明示）
- `inbox/` `adapter/` `synthesis/`
- `design/rejected-ideas.md`
- `state/decision-log.yaml` `state/contradiction-log.yaml` `state/canon-patch-log.yaml` `state/timeline-state.yaml` `state/character-states.yaml`
- `drafts/` `reviews/contracts/` `reviews/audits/` `reviews/templates/`
- `approved/` `published/`

---

## 5. 作品固有 facet の扱い

ore_tueee_school_hell は v4 generic に整合する作品で、独自 facet は少ない:

| 概念 | 扱い |
|---|---|
| **企画書 v0.9** | bible に分配 + 履歴として `design/genesis-doc.md` または `archive/` |
| **handover_v2 構造** | 用途終了 → archive |
| **craft methodology**（`learning/craft/`） | 作品横断方法論として `learning/` に残置、`StoryTemplateEvolution/current/learning/` への昇格を検討 |
| **`*-v1.md` 形式の bible** | v4 facet 別に分割、v1 ファイルは履歴として `archive/2026-04-30-bible-v1/` に退避 |
| **6 アーク × 12 話 × 100 ep の構造** | World ではなく Plot facet。v4 で違和感なく扱える |

---

## 6. Migration Step 順序

### Step 1: 退避

```bash
cp -r works/ore_tueee_school_hell/ archive/2026-04-30-ore_tueee-pre-v4/
```

### Step 2: ディレクトリ作成 + リネーム

```bash
cd works/ore_tueee_school_hell/
mkdir -p inbox adapter synthesis design state drafts approved published
mkdir -p bible/world bible/characters bible/system bible/timeline bible/samples bible/walkthroughs
mkdir -p design/canon-patch-proposals
mkdir -p reviews/contracts reviews/audits reviews/templates
mv actions/ backlog/
```

### Step 3: 既存 facet の単純 move

```bash
mv story/promises.md bible/promise.md
mv story/open-questions.md design/open-questions.md
mv story/design-debt.yaml design/design-debt.yaml
mv story/canon-patch-proposals design/canon-patch-proposals
mv actions/roadmap.md arcs/manuscript-plan.md  # actions のリネーム前なら
mv actions/design-audit.md reviews/audits/2026-04-XX-design-audit.md
```

### Step 4: bible v1 形式の分解

#### 4-1. series-bible-v1.md の解体

各セクションを切り出して:
- logline → `bible/logline.md`
- promise → `bible/promise.md` に追記
- theme → `bible/theme.md`
- premise of world → `bible/world/overview.md`
- characters core → `bible/characters/`
- plot core → `bible/plot.md`

旧版を `archive/2026-04-30-bible-v1/series-bible-v1.md` に退避。

#### 4-2. character-sheets-v1.md の分解

各キャラのセクションを `bible/characters/{slug}.md` に切り出し。

#### 4-3. system-bible-v1.md の分解

facet として `bible/system/overview.md` に基幹、必要なら `bible/system/abilities.md` 等に分割。

#### 4-4. dialogue-bible-v1.md の解体

会話ルール → `bible/style-voice.md` の "dialogue conventions"
会話サンプル → `bible/samples/dialogue-samples.md`

#### 4-5. world-regulars-v1.md → `bible/world/regulars.md`

### Step 5: rules.md の分割

`bible/rules.md`（既存）の内容を:
- 文体 / POV / tense → `bible/style-voice.md`
- 禁則 → `bible/rules.md`（残す、内容を絞る）

### Step 6: 企画書 v0.9 の分配

`企画書v0.9.md` から該当箇所を bible に分配。
原本は `design/genesis-doc.md` または `archive/` に退避。

### Step 7: kernel.yaml 作成

v4 schema で 11 項目を埋める。bible facet との sync を取る。

### Step 8: 不在 facet の処理

- `bible/cadence-plan.md` 新規作成（または tentative で簡略）
- `bible/motif-ladder.md` `bible/foreshadowing-map.md`（後者は story/foreshadowing-ledger を変換）
- `bible/timeline/` not_applicable 明示 or 簡略作成
- `bible/samples/` deferred 明示

### Step 9: state 系の初期化

`state/decision-log.yaml` 等を空ファイルで作成。
`story/foreshadowing-ledger.md` を `bible/foreshadowing-map.md` + `state/foreshadowing-implementation.yaml` に二層化。

### Step 10: handover_v2 の archive

```bash
mv story/handover_v2 archive/2026-04-30-handover-v2/
```

### Step 11: 検証

`07_review_prompts/bible-readiness-review.md` で DoR-A 判定。

---

## 7. 想定リスク

| リスク | 対策 |
|---|---|
| **v1 bible の分解で情報欠落** | 解体前に `archive/` に full copy、解体後に diff 検証 |
| **packets/frozen/000-003 が新 facet 構造と不整合** | packet.yaml の依存先参照を新パスに更新 |
| **企画書 v0.9 の "work-root 変則配置" を bible に分配後、参照が断つ** | grep で `企画書v0.9.md` 参照を検索、置換 |
| **handover_v2/ archive で意図的非開示情報が露出する** | archive 自体は private、git 管理範囲を確認 |
| **6 アーク × 12 話 × 100 ep 構造の Unit Tree mapping** | kernel.unit_tree で has_part: false / target_total: 100 / planned_arc_count: 6 / planned_episode_count_per_arc: ~17（端数調整）|
| **craft methodology rule が generic に流入** | `.claude/rules/craft-methodology.md` は work 固有 rule として残置 |

---

## 8. 完了条件

- ✅ DoR-A 通過
- ✅ v1 形式 bible が分解され archive 済み
- ✅ packets/frozen の 000-003 が DoR-C を引き続き満たす
- ✅ kernel.yaml v4 で全 MUST 28 項目埋まり
- ✅ actions/ → backlog/ リネーム完了
- ✅ design/ と state/ ディレクトリ運用開始

完了所要時間目安: **4-8 時間**（ia_society より小規模なので短い）。
