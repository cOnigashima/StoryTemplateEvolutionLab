# 03 Storage Trinity — Bible / Design / State の物理構造

> **役割**: 02 で card 化された全概念を、各 work 配下の物理ディレクトリに落としたときの正本配置図。
> **依存**: 02_domain_model.md の Section 3（格納域）と Section 4-6（Bible Facet / Design / State）を前提とする。
> **適用対象**: 各 work（ia_society / ore_tueee_school_hell / fools-with-cheating / 新規作品）の repo ルート配下。

---

## 1. Trinity 概念図

```
┌──────────────────────────────────────────────────────┐
│  Bible             frozen 設計（書く前に決まる）       │
│  ─────             Patch 経由でしか変わらない          │
└──────────────────────────────────────────────────────┘
                          ↑ Patch を経由
┌──────────────────────────────────────────────────────┐
│  Design            揺れる設計（候補・open question）  │
│  ──────            author judgment 待ち                │
└──────────────────────────────────────────────────────┘
                          ↓ draft 進行で更新
┌──────────────────────────────────────────────────────┐
│  State             制作中に動く事実                    │
│  ─────             実装履歴・現在値・Ledger            │
└──────────────────────────────────────────────────────┘
```

3 層の関係:
- **Bible → Design**: Bible 改訂したい時は直接書き換えず Canon Patch Proposal を Design に置く
- **Design → Bible**: Patch が author 承認されると Bible に適用 + State の Canon Patch Log に記録
- **Bible / Design → State**: prose で書くと State に実装履歴が積まれる
- **State → Bible**: State の蓄積から Bible 改訂が必要になったら Canon Patch Proposal を起票

---

## 2. Bible 配下の物理構造

```
bible/
  README.md                       # facet 索引・読み順・分割ルール
  
  # === Kernel-tier facet（kernel.yaml と紐付く）===
  logline.md                      # Term: Logline (kernel #1, 旧 premise.md)
  promise.md                      # Term: Promise (kernel #2)
  theme.md                        # Term: Theme
  rules.md                        # Term: Rules
  style-voice.md                  # Term: Style Voice (kernel #10)
  
  # === Design intent facet（設計意図、肥大時に分割可）===
  cadence-plan.md                 # Term: Cadence
  foreshadowing-map.md            # Term: Foreshadowing Map
  reveal-plan.md                  # Term: Reveal Plan
                                  #   または reveal-budget.md（二層ファイル）
  motif-ladder.md                 # Term: Motif（設計）
                                  #   または二層ファイル
  plot.md                         # Term: Plot
                                  #   肥大時 plot/ ディレクトリに分割
  
  # === World-tier facet（世界・人物・制度・時間・声）===
  world/                          # Term: World
    README.md
    overview.md
    locations.md                  # 地理（過大化したら分離）
    society.md                    # 社会（過大化したら分離）
    physics.md                    # 物理（過大化したら分離）
  
  characters/                     # Term: Character
    README.md
    overview.md
    {char_slug}.md                # 個別シート
    relationships.md              # 関係性
    relationship-arcs.md          # facet × Arc 単位ビュー
  
  system/                         # Term: System ★新設 facet
    README.md
    institutions.md               # 制度
    abilities.md                  # 能力体系
    economics.md                  # 経済
    # 作品によって magic.md / technology.md など追加自由
  
  timeline/                       # Term: Timeline ★新設 facet
    README.md
    history.md                    # macro: 制度史・前史・全期
    day-by-day.md                 # micro: 本編日次・時刻単位
  
  samples/                        # Term: Sample Scene ★新設 facet
    README.md
    sample-scene-{slug}.md        # 試し場面
                                  # ※本編 prose は drafts/ のみ、ここは見本のみ
  
  # === 制約 facet（必要時のみ）===
  genre-overlay.md                # Term: Genre Overlay（任意）
  project-override.md             # Term: Project Override（任意）
  
  # === 案内資料（必要時のみ）===
  walkthroughs/                   # Term: Walkthrough（任意）
    reading-order.md
    character-introduction.md
    world-tour.md
```

### Bible 配下の不変条件

1. **Bible に Draft（本編 prose）を入れない**。Sample Scene のみ例外（`bible/samples/`）
2. **Bible は frozen**。改訂は Patch 経由のみ（直接書き換え禁止）
3. **作品固有 facet は generic 雛形に積まない**。各 work の bible に追加自由
4. **README.md は各サブディレクトリのトップに常設**
5. **kernel-tier facet（logline / promise / theme / rules / style-voice）は分割しない**（一覧性優先）
6. **design intent facet（cadence / foreshadowing-map / reveal-plan / motif-ladder / plot）はデフォルト 1 ファイル、肥大時に分割可**

---

## 3. Design 配下の物理構造

```
design/
  README.md                       # design 配下の運用説明
  
  open-questions.md               # Term: Open Question
  design-debt.yaml                # Term: Design Debt
  rejected-ideas.md               # Term: Rejected Idea
  
  canon-patch-proposals/          # Term: Canon Patch Proposal（複数可）
    README.md
    {patch_id}-{slug}.md          # 個別 proposal
  
  # === 作品固有の "揺れる設計" 置き場（任意）===
  project_principles.md           # 作品固有の作劇ルール（hard rule 化前）
  critical_intent.md              # 批評性メモ（fools-with-cheating 由来）
  audits/                         # 設計監査メモの一時置き場（review に上げる前）
```

### Design 配下の不変条件

1. **Design は author judgment 待ちのもの**。確定したら Bible に Patch 経由で移す
2. **Design に書いたものを直接 draft で参照しない**（参照したら Bible 化候補が遅延している兆候）
3. **Rejected Idea は append-only**（削除しない）
4. **Canon Patch Proposal は 1 patch = 1 ファイル**

---

## 4. State 配下の物理構造

```
state/
  README.md                       # state 配下の運用説明
  
  # === Ledger（append-only journal）===
  decision-log.yaml               # Term: Decision Log
  contradiction-log.yaml          # Term: Contradiction Log
  canon-patch-log.yaml            # Patch 適用履歴（Patch lifecycle の最終段階）
  
  # === 実装状況（現在値スナップショット + 履歴）===
  timeline-state.yaml             # Term: Timeline State
  character-states.yaml           # Term: Character State
  
  # === Implementation Ledger（Bible facet とペアで運用）===
  foreshadowing-implementation.yaml    # Bible.foreshadowing-map とペア
  reveal-implementation.yaml           # Bible.reveal-plan とペア（または二層）
  motif-status.yaml                    # Bible.motif-ladder とペア（または二層）
```

### State 配下の不変条件

1. **State は draft / review / Patch によって都度更新される**
2. **Ledger は append-only**（過去の entry を書き換えない）
3. **現在値スナップショット系は更新可能**（timeline-state / character-states）
4. **Bible.{facet} と State.{facet}-implementation はペアで参照される**

---

## 5. 単位主軸の場所（Bible 配下ではない）

Unit を主軸とした資料（純粋な構造設計、facet を持たない）は Bible 配下ではなく、専用の単位主軸ディレクトリに置く。

```
arcs/                             # Arc 単位の設計
  README.md
  series-overview.md              # シリーズ全体（Manuscript / Part 構造）
  manuscript-plan.md              # 制作ロードマップ（旧 actions/roadmap.md）
  arc-{NN}.md                     # 個別 Arc
  arc-{NN}-checkpoint-{slug}.md   # 中間チェックポイント

packets/                          # Packet 単位の設計
  README.md
  exploring/                      # 検討中の packet
  scoped/                         # 範囲が決まった packet
  frozen/                         # 凍結済み（drafting 開始可）
    packet-{NNN}-{slug}.yaml
  templates/                      # 雛形
    packet-frozen-checklist.md

scenes/                           # Scene Card（Episode の場面設計）
  README.md
  seed/                           # template
  slotted/                        # Episode 割り当て済み
    {ep_id}-{slug}.md             # Term: Scene Card
  superseded/                     # 旧版（archive）

drafts/                           # Term: Prose（本編原稿）
  README.md
  episodes/
    {ep_id}-{slug}.md             # 1 episode 1 ファイル
```

### 単位主軸の不変条件

1. **arcs/ packets/ scenes/ drafts/ は facet を持たない**（純粋に Unit 軸）
2. **drafts/ に置けるのは Prose のみ**（Sample Scene は bible/samples/）
3. **scenes/slotted/ の Scene Card は Writing Pack から生成される**
4. **packets/{exploring,scoped,frozen}/ の遷移は Packet Freeze Review を経る**

---

## 6. 並行配置（intake / synthesis / adapter / review / release / craft / backlog）

### Intake パイプライン 3 段（inbox / adapter / synthesis）

intake phase は次の 3 つのディレクトリの連携で動く。**それぞれ責務が違うので統合・吸収しない**:

| ディレクトリ | 役割 | 性質 |
|---|---|---|
| `inbox/` | **入力の受け口（raw 保存）** | noun, place |
| `adapter/` | **変換装置（prompt + 設定）** | noun, actor |
| `synthesis/` | **変換装置の出力（成果物）** | noun, result |

**"intake"** は phase 名・プロセス名であり、ディレクトリ名ではない（`intake/` は v4 で作らない）。

```
inbox/                            # Raw 入力の受付（noun, place）
  README.md
  planning_sessions/              # ChatGPT log / 設計 chat 等の原文ママ
    {date}_{slug}.md
  fragments/                      # 断片メモ
    {date}_{slug}.md

adapter/                          # 変換装置（noun, actor）— work 固有の override
  README.md                       # generic 参照先 + override 方針を記述
  field_mapping.yaml              # この work 用の項目 mapping
  source_mapping.yaml             # この work の raw 由来表（任意）
  intake_adapter_prompt.md        # 必要なら override（通常は generic を参照）
                                  # generic 正本は StoryTemplateEvolution/current/adapter/
                                  # ※ leading dot は付けない: 人が編集・参照する work-content
                                  #   隣接の位置付け。.claude/ や .takt/ のような auto-discover
                                  #   config とは性質が違うため

synthesis/                        # 変換装置の出力（noun, result）
  README.md
  session_digests/                # Term: Digest
    {date}_{slug}.md
  update_proposals/               # Term: Update Proposal
    {date}_{target}_proposal.md

story/                            # 作品メタ + seed
  README.md
  kernel.yaml                     # 11 項目 kernel（schema_version: v4）
  seeds/                          # Term: Seed
    {date}_{slug}.md

writing/                          # Writing Adapter の出力
  README.md
  episode_packs/                  # Term: Writing Pack
    {ep_id}/
      episode_brief.md
      scene_card.md               # Term: Scene Card のコピー or 参照
      context_pack.md
      acceptance_checklist.md     # Term: Acceptance Contract のコピー or 参照

reviews/                          # 全 Review 種別
  README.md
  contracts/                      # Term: Acceptance Contract（正本）
    {ep_id}.contract.yaml
  typed-review-{date}-{ep_id}.md
  bridge-review-{packet_a}-{packet_b}-{date}.md
  continuity-review-{scope}-{date}.md
  persona-review-{ep_id}-{date}.md
  packet-freeze-{packet_id}-{date}.md
  approval-{ep_id}-{date}.md
  audits/
    {date}-{scope}-design-audit.md      # Term: Design Audit（旧 actions/design-audit.md）
  templates/
    typed-review-template.md
    bridge-review-template.md
    ...

approved/                         # 承認済み prose（公開待ち）
  README.md
  episodes/
    {ep_id}-{slug}.md

published/                        # 公開済み prose
  README.md
  episodes/
    {ep_id}-{slug}.md

backlog/                          # Term: Backlog（旧 actions/）
  README.md
  {slug}.yaml                     # フラット構造、lifecycle subfolder なし
                                  # 内部タスク・計画・外部アクションすべて

craft/                            # Layer 3: 作品共通の Craft Library（StoryTemplate に置く想定）
  README.md
  rubric.md                       # Term: Rubric
  framework-index.md              # Term: Framework
  lenses/                         # Term: Framework Lens
    {framework_name}-{date}.md
  # 各種 craft 知識ファイル
  scene-sequel.md
  pov-design.md
  foreshadowing-craft.md

learning/                         # 制作 learning ログ（論点 1 で確定）
  README.md
  {date}-{slug}.md                # 失敗ログ・retro

community/                        # 任意：読者対応・SNS メモ
  README.md
  reading-notes/

campaigns/                        # 任意：プロモーション・コンテスト応募
  README.md
```

### 並行配置の不変条件

1. **inbox/ は raw 保存専用**。Intake Adapter にかける前の原文ママ
2. **adapter/ は work 固有の override 置き場**。generic 正本は `StoryTemplateEvolution/current/adapter/`、work 側は差分のみ保持。**leading dot は付けない**（人が編集・参照する work-content 隣接で、auto-discover config の `.claude/` `.takt/` とは性質が違うため）
3. **synthesis/ は Intake Adapter 出力専用**（Digest と Update Proposal の 2 種）
4. **inbox / adapter / synthesis は責務が違うので統合しない**。intake phase は 3 ディレクトリの連携で回る
5. **"intake/" ディレクトリは作らない**。"intake" は phase 名であってディレクトリ名ではない
6. **story/seeds/ が物語の入口**（旧 v1 の `backlog/` 用法は禁止）
7. **writing/episode_packs/ は drafter の入力**。本書では bible 全体を渡さない
8. **reviews/ は全 Review 種別を集約**。種別ごとにファイル prefix で識別
9. **approved/ → published/ は片道**。公開後の編集は Patch 経由
10. **backlog/ はフラット**。lifecycle subfolder（proposed / executed / archived）を作らない
11. **craft/ は StoryTemplate 共通**。各 work から copy せずリンク参照

---

## 7. 二層ファイル形式（Bible + State 同居）

論点 3 で確定した、Bible facet と State Implementation Ledger を 1 ファイルに同居させる形式。

### 形式

```markdown
# {Facet Name} Sheet

## === Section A: 設計意図（Bible 由来）===

（ここは bible/{facet}.md と同等の内容。frozen、Patch 経由でしか変えない）

## === Section B: 実装状況（State 由来）===

（ここは state/{facet}-implementation.yaml と同等の内容。draft 進行で更新）
```

### 適用対象

- **Reveal Budget Sheet** = `bible/reveal-plan.md` + `state/reveal-implementation.yaml`
- **Motif Ladder Sheet** = `bible/motif-ladder.md` + `state/motif-status.yaml`
- **Foreshadowing Sheet**（任意）= `bible/foreshadowing-map.md` + `state/foreshadowing-implementation.yaml`

### 物理位置

- 二層ファイルは **Bible 側に置く**（`bible/reveal-budget.md` 等）
- State 側にコピーは置かない（参照は Bible ファイル単一）
- export 時に Section A / Section B を分離可能にする（YAML front-matter または明示セパレータで識別）

### 使い分けルール

- 設計意図と実装状況の参照頻度が高く、別ファイルだと往復コストが高い場合 → **二層ファイル**
- 設計意図のみ、または実装状況のみを参照する場合が多い → **分離（Bible / State 別ファイル）**

---

## 8. ファイル成長ルール（既存 `.claude/rules/file-growth.md` 継承）

各ディレクトリの肥大化に対する分割方針:

1. **1 ファイルが 300 行を超えた、または関心軸が 2 つ以上混在しているなら分割を検討**
2. **分割しても元ファイルは索引（README.md）として残す**
3. **新ファイル命名は既存パターンに揃える**
4. **分割は author 承認後**

特に以下のファイルは肥大時に分割する想定:
- `bible/world/overview.md` → `bible/world/locations.md` + `bible/world/society.md` + `bible/world/physics.md`
- `bible/plot.md` → `bible/plot/{arc_NN}.md`
- `bible/timeline/history.md` → `bible/timeline/{era_slug}.md`
- `bible/foreshadowing-map.md` → `bible/foreshadowing-map/{thread_slug}.md`

肥大しても分割してはいけない:
- `CLAUDE.md`（制作 OS 契約）
- `README.md` 系（索引）
- `bible/promise.md`（一覧性優先）
- `bible/logline.md`（1 文）

---

## 9. 命名規則（既存 `.claude/rules/naming-conventions.md` 継承）

### 基本原則

- ハイフン (`-`): 人間が読む部分（slug、説明的な名前）
- アンダースコア (`_`): 機械的にパースする部分（タイムスタンプ、連番）
- 小文字のみ
- 拡張子: `.md`（本文）、`.yaml`（構造データ）

### 識別子

- **Episode**: `ep{NN}` （`ep01`, `ep072`）
- **Packet**: `packet-{NNN}` （3 桁）
- **Arc**: `arc-{NN}`
- **Patch**: `patch-{NNN}`
- **Foreshadowing**: `FS-{NNN}`
- **Reveal**: `RV-{NNN}`
- **Motif**: `MT-{slug}`
- **Contradiction**: `X-{NNN}`
- **Open Question**: `Q-{NNN}` または `AD-{NNN}`（needs_author_decision）
- **Decision**: `D-{NNN}`
- **Rejected**: `R-{NNN}`
- **Hidden item**: `H-{NNN}`
- **Confirmed**: `C-{NNN}`（intake digest 用）
- **Tentative**: `T-{NNN}`（intake digest 用）

### タイムスタンプ

- 日付のみ: `YYYYMMDD`
- 日時: `YYYYMMDD_HHMMSS`

### ディレクトリ別パターン（v3 継承 + 本提案で追加）

| ディレクトリ | 形式 |
|---|---|
| `inbox/planning_sessions/` | `{date}_{slug}.md` |
| `synthesis/session_digests/` | `{date}_{slug}.md` |
| `synthesis/update_proposals/` | `{date}_{target}_proposal.md` |
| `story/seeds/` | `seed-{YYYYMMDDHHMMSS}.md` または `{date}_{slug}.md` |
| `arcs/` | `arc-{NN}.md`, `series-overview.md`, `manuscript-plan.md` |
| `packets/{stage}/` | `packet-{NNN}-{slug}.yaml`, draft 中は `packet-{NNN}-draft.yaml` |
| `scenes/slotted/` | `scene-{ep_id}-{slug}.md` |
| `drafts/episodes/` | `draft_{ep_id}_{timestamp}.md` |
| `approved/episodes/` | `release_{ep_id}_{timestamp}.md` |
| `published/episodes/` | `release_{ep_id}_{timestamp}.md` |
| `reviews/` | `{type}-{date}-{ep_id}.md` または `{type}-{scope}-{date}.md` |
| `reviews/contracts/` | `{ep_id}.contract.yaml` |
| `reviews/audits/` | `{date}-{scope}-design-audit.md` |
| `design/canon-patch-proposals/` | `{patch_id}-{slug}.md` |
| `state/` | `{facet-name}-{state\|log}.yaml` |
| `backlog/` | `{slug}.yaml` または `{date}_{slug}.yaml` |
| `learning/` | `{date}-{slug}.md` |

---

## 10. 全体ツリー（圧縮版）

```
{work_root}/
├── CLAUDE.md                     # 制作 OS 契約（分割禁止）
├── README.md                     # repo 入口（分割禁止）
├── story/
│   ├── kernel.yaml               # 11 項目 kernel
│   └── seeds/                    # 物語の入口
├── inbox/                        # raw 入力（noun, place）
├── adapter/                      # 変換装置 work 固有 override（noun, actor）
├── synthesis/                    # Intake Adapter 出力（noun, result）
├── bible/                        # frozen 設計（17 facet）
├── design/                       # 揺れる設計
├── state/                        # 動的事実
├── arcs/                         # Arc 単位設計 + manuscript-plan
├── packets/                      # Packet 単位設計
├── scenes/                       # Scene Card
├── writing/                      # Writing Adapter 出力
├── drafts/                       # 本編 prose
├── reviews/                      # 全 review 種別 + audits/
├── approved/                     # 承認済 prose
├── published/                    # 公開済 prose
├── backlog/                      # 全 task（フラット）
├── learning/                     # 制作 learning
├── community/                    # 任意：読者対応
├── campaigns/                    # 任意：プロモ
└── .claude/                      # rules / agents / skills
    ├── rules/
    ├── agents/
    └── skills/
```

外部参照（各 work には置かない、StoryTemplate 共通）:

```
StoryTemplateEvolution/
├── adapter/                      # generic Adapter 正本（work の adapter/ から参照）
│   ├── intake_adapter_prompt.md
│   ├── writing_adapter_prompt.md
│   ├── folder_structure.md
│   ├── field_mapping_template.yaml
│   ├── update_proposal_format.yaml
│   ├── writing_pack_format.yaml
│   └── human_approval_policy.md
│
├── craft/                        # 作品共通の Craft Library
│   ├── rubric.md
│   ├── framework-index.md
│   └── lenses/
│
└── learning/                     # 横断 learning（作品横断の retro）
```

各 work の `adapter/` は **差分のみ** を持つ（`field_mapping.yaml` 等）。プロンプト本体は generic を参照する。
