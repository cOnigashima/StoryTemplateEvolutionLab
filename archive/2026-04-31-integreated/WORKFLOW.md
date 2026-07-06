# WORKFLOW — StoryTemplate v4 全体フロー（1 枚ガイド）

> **役割**: 「StoryTemplate を複製したい」「raw 入れる場所は?」「どこで執筆?」に **1 ページで** 答える Claude / Agent / 人間共通の onboarding ガイド。
> **詳細**: 各セクションから `proposal/2026-04-30-zero-base-v4/` の該当文書にリンク。
> **更新日**: 2026-04-30 (v4 採用)

---

## 1. 全体図（鳥瞰）

```
┌─────────────────────────────────────────────────────────────────┐
│ StoryTemplateEvolution/  （StoryTemplate 開発リポジトリ）       │
│                                                                 │
│  current/                  ← 現在の正本（雛形 + generic 設定）  │
│    ├── adapter/            ← Intake / Writing Adapter prompt    │
│    ├── agents/             ← generic agent role 18 本           │
│    ├── skills/             ← generic skill 7 本                 │
│    ├── rules/              ← 共通 rule 5 本                     │
│    ├── templates/          ← 各 work が copy する雛形           │
│    │   ├── .claude/        ← work の .claude/ 雛形              │
│    │   ├── inbox/          ← work の inbox 雛形                 │
│    │   ├── story/          ← kernel.template.yaml               │
│    │   └── bible/ design/ state/ ...                            │
│    ├── docs/               ← 仕様書（一部 supersede stub）       │
│    └── work_init/          ← bootstrap 手順                     │
│                                                                 │
│  proposal/                 ← 提案（履歴 + アクティブ）          │
│    └── 2026-04-30-zero-base-v4/  ★ ADOPTED                     │
│                                                                 │
│  archive/                  ← 凍結された旧資産                   │
└─────────────────────────────────────────────────────────────────┘
                              ↓ 新規 work 立ち上げ時
                              ↓ current/templates/ から copy
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ works/{your-slug}/         ← あなたの作品ディレクトリ           │
│                                                                 │
│  CLAUDE.md                 ← 制作 OS 契約                       │
│  README.md                                                      │
│                                                                 │
│  .claude/                  ← Claude Code 設定（templates から） │
│    ├── rules/              5 本（drafter-preflight 等）         │
│    ├── agents/             18 本（plotter / drafter / critic 等）│
│    └── skills/             7 本（pitch / draft / critic 等）    │
│                                                                 │
│  inbox/                    ★ raw を入れる場所                    │
│    ├── planning_sessions/  企画 chat / 既存 bible package        │
│    └── fragments/          断片メモ                              │
│                                                                 │
│  adapter/                  ← work 固有 override（任意）          │
│  synthesis/                ← Intake Adapter 出力                 │
│    ├── session_digests/    Digest                                │
│    └── update_proposals/   反映指示書                            │
│                                                                 │
│  story/                                                         │
│    ├── kernel.yaml         ★ 作品の核（11 項目）                 │
│    └── seeds/              再利用可能な核                        │
│                                                                 │
│  bible/                    ★ 安定設定（17 facet）                │
│    ├── logline.md / promise.md / theme.md / rules.md            │
│    ├── style-voice.md / cadence-plan.md / plot.md               │
│    ├── world/ characters/ system/ timeline/ samples/             │
│    ├── foreshadowing-map.md / reveal-plan.md / motif-ladder.md  │
│    └── (任意) genre-overlay.md / project-override.md            │
│                                                                 │
│  design/                   ← 揺れる設計                          │
│    ├── open-questions.md / design-debt.yaml / rejected-ideas.md │
│    └── canon-patch-proposals/                                   │
│                                                                 │
│  state/                    ← 制作中の動的事実                    │
│    ├── decision-log.yaml / contradiction-log.yaml                │
│    ├── canon-patch-log.yaml / timeline-state.yaml               │
│    └── character-states.yaml / *-implementation.yaml            │
│                                                                 │
│  arcs/ packets/ scenes/    ← 単位主軸の設計                      │
│  writing/episode_packs/    ← Writing Adapter 出力                │
│                                                                 │
│  drafts/episodes/          ★ 執筆をガリガリ進める場所             │
│  reviews/                  ← typed/persona/continuity/approval   │
│  approved/ → published/    ← 承認済 → 公開済                    │
│                                                                 │
│  backlog/                  ← 全 task（フラット）                 │
│  learning/                 ← 制作 retro                          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. 「StoryTemplate を複製する」3 つの起点

### 起点 A: 新規作品をゼロから始める

```
1. works/{your-slug}/ を新規作成
2. current/work_init/new-work-bootstrap.md の手順を踏む
3. current/templates/ から雛形を copy
4. inbox/ に企画 chat を入れる
5. Intake Adapter で bible に反映
6. DoR-A 通過 → drafting 開始
```

→ 詳細: `current/work_init/new-work-bootstrap.md`

### 起点 B: 既存作品（v3 形式）を v4 に移行

```
1. archive/ に既存 work をスナップショット
2. v4 ディレクトリ群を作成
3. 既存ファイルを bible/{facet}/ に再配置
4. kernel.yaml v4 化（premise → logline）
5. DoR-A 検証
```

→ 詳細: `proposal/2026-04-30-zero-base-v4/08_pilot_validation/` の各 walkthrough、および `proposal/2026-04-30-zero-base-v4/10_migration_plan.md` Phase 2

### 起点 C: 外部完成 bible package を取り込む

```
1. 外部生成された bible package を inbox/planning_sessions/ に保存
2. Intake Adapter で 86 項目チェックリストに照らして分割
3. EPISODE_FULL_DRAFT 等が混在していれば bible から drafts/ に剥がす
4. facet 別 Update Proposal を生成 → author Approval
5. bible/ design/ state/ に分配反映
```

→ 詳細: `proposal/2026-04-30-zero-base-v4/08_pilot_validation/ia_society_zero_state.md`

---

## 3. raw → 執筆 までの実走ループ（Phase 別）

### Phase 1: Intake（raw → bible）

```
[企画 chat / 既存資料]
        ↓
inbox/planning_sessions/{date}_{slug}.md   ★ ここに raw 配置
        ↓
[Intake Adapter Prompt 実行]
   = current/adapter/intake_adapter_prompt.md を LLM に貼る
   + proposal/2026-04-30-zero-base-v4/02 / 05 / 06 を context に
   + inbox の raw を input に
        ↓
synthesis/session_digests/{date}_{slug}.md   ← Digest（読み物）
synthesis/update_proposals/{date}_{target}_proposal.md   ← 反映指示書
        ↓
[7 review prompts で検証]
   - intake-digest-review.md
   - intake-coverage-review.md
   - contradiction-triage.md（矛盾発見時）
   - update-proposal-review.md
        ↓
[Human Approval]
        ↓
bible/ design/ state/ に確定反映
        ↓
[bible-readiness-review.md で DoR-A 判定]
```

**目標**: DoR-A 通過 = 「Packet 設計フェーズに進めて良い」状態。

### Phase 2: Design Freeze（bible → frozen packet → scene）

```
arcs/series-overview.md / arc-{NN}.md（scoped）
        ↓
packets/scoped/packet-{NNN}-{slug}.yaml
        ↓
[Packet Freeze Review = DoR-C 検査]
        ↓
packets/frozen/packet-{NNN}-{slug}.yaml
        ↓
scenes/slotted/{ep_id}-{slug}.md     ← Scene Card 生成
reviews/contracts/{ep_id}.contract.yaml   ← Acceptance Contract
```

**目標**: Episode draft に進める状態 = DoR-B の前提クリア。

### Phase 3: Writing（Writing Pack → drafts/）

```
[Writing Adapter Prompt 実行]
   = current/adapter/writing_adapter_prompt.md（v3 のまま、Q-B-001 で v4 化予定）
   + 該当 frozen packet と scene_card を context に
        ↓
writing/episode_packs/{ep_id}/   ← Writing Pack 4 ファイル
   ├── episode_brief.md
   ├── scene_card.md
   ├── context_pack.md
   └── acceptance_checklist.md
        ↓
[drafter-preflight 適用]
   - Gate 0: 直前散文照合
   - Gate A: Writing Pack 要件マッピング
   - Gate C: 前振りチェック
   - 因果一段落 / 知識状態台帳 / 合理化語彙 self-check
        ↓
drafts/episodes/{ep_id}-{slug}.md   ★ ここで執筆をガリガリ進める
        ↓
[Multi-Pass Self-Review (drafter)]
        ↓
[Typed / Persona / Continuity / Bridge Review (critic)]
        ↓
[Approval Review = DoD-E]
        ↓
approved/episodes/{ep_id}-{slug}.md
        ↓
[公開実施 → カクヨム等]
        ↓
published/episodes/{ep_id}-{slug}.md
        ↓
[State 更新（character-states / timeline-state / *-implementation）]
```

**目標**: Episode 公開 + State 反映。

---

## 4. Claude / Agent への onboarding（最初に読む順）

新セッションの Claude / Agent が StoryTemplate を理解するための最短ルート:

1. **本ファイル** (`current/WORKFLOW.md`) — 全体図
2. **`proposal/2026-04-30-zero-base-v4/00_README.md`** — 提案の入口
3. **`proposal/2026-04-30-zero-base-v4/02_domain_model.md`** — 56 語の用語
4. **`proposal/2026-04-30-zero-base-v4/03_storage_trinity.md`** — 物理配置
5. **`proposal/2026-04-30-zero-base-v4/04_pipeline_overview.md`** — 動作正本
6. **`current/.claude/CLAUDE.md`** — リポジトリ自身の rule
7. **目的別の deep-dive**:
   - 新規 work 立ち上げ → `current/work_init/new-work-bootstrap.md`
   - intake → `current/adapter/intake_adapter_prompt.md` + `proposal/2026-04-30-zero-base-v4/05_intake_coverage_checklist.md`
   - DoR 判定 → `proposal/2026-04-30-zero-base-v4/06_bible_dor.md`
   - 検証 → `proposal/2026-04-30-zero-base-v4/07_review_prompts/`
   - drafting → `current/.claude/rules/drafter-preflight.md`（または各 work の `.claude/rules/`）

---

## 5. 役割別の入口

| あなたの役割 | 最初に読む |
|---|---|
| **新規 work を立ち上げる人** | `current/work_init/new-work-bootstrap.md` |
| **既存 work を v4 移行する人** | `proposal/2026-04-30-zero-base-v4/08_pilot_validation/` |
| **raw を inbox に入れた人** | `current/adapter/intake_adapter_prompt.md` |
| **Drafter（drafting する人 / agent）** | `current/agents/drafter.md` + `current/rules/drafter-preflight.md` |
| **Plotter（設計する人 / agent）** | `current/agents/plotter.md` |
| **Critic（review する人 / agent）** | `current/agents/critic.md` + `proposal/2026-04-30-zero-base-v4/07_review_prompts/` |
| **Continuity Checker** | `current/agents/continuity-checker.md` + `proposal/2026-04-30-zero-base-v4/07_review_prompts/contradiction-triage.md` |
| **StoryTemplate そのものを編集する人** | `current/.claude/CLAUDE.md` + `proposal/README.md` |

---

## 6. 重要な不変条件（Top 10）

1. **raw を直接 bible に流さない** — Intake Adapter 経由必須
2. **bible 全体を drafter に渡さない** — Writing Adapter で圧縮
3. **bible を直接書き換えない** — Patch 経由必須
4. **Update / Patch は human approval 必須**
5. **Review は種別必須** — "Review" 単独使用禁止
6. **State Ledger は append-only** — 履歴を削除しない
7. **drafts は drafts/ のみ** — bible に同居させない（Sample Scene 例外）
8. **作品固有 facet は generic 雛形に流入させない**
9. **Backlog はフラット** — lifecycle subfolder を作らない
10. **archive を編集しない**

---

## 7. v4 採用後の TODO（90 日以内）

- writing_adapter_prompt.md の v4 化
- update_proposal_format.yaml / field_mapping_template.yaml の v4 化
- bible/ facet 雛形 13 ファイル新規作成（logline.template.md 等）
- prompts/00-05 の v4 参照更新
- agents / skills の dir 参照を v4 に書き換え
- craft/ コンテンツ整備（rubric / framework-index 等）

詳細: `proposal/2026-04-30-zero-base-v4/09_open_questions.md`

---

## 8. 困ったときの参照順

```
迷ったら:
  ├── 用語が分からない         → proposal/2026-04-30-zero-base-v4/02_domain_model.md
  ├── どこに置く?              → proposal/2026-04-30-zero-base-v4/03_storage_trinity.md
  ├── 何をする順序?            → proposal/2026-04-30-zero-base-v4/04_pipeline_overview.md
  ├── 何を埋める?              → proposal/2026-04-30-zero-base-v4/05_intake_coverage_checklist.md
  ├── DoR 通過してる?          → proposal/2026-04-30-zero-base-v4/06_bible_dor.md
  ├── どの prompt 使う?        → proposal/2026-04-30-zero-base-v4/07_review_prompts/
  ├── 既存 work の例は?        → proposal/2026-04-30-zero-base-v4/08_pilot_validation/
  ├── 未決論点は?              → proposal/2026-04-30-zero-base-v4/09_open_questions.md
  ├── v3 ではどうだった?       → archive/2026-04-30-pre-v4/
  └── 旧提案を見たい           → proposal/2026-04-22-... / 2026-04-29-... / archive/proposal/
```
