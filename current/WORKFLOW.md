# WORKFLOW — StoryTemplate 全体フロー（1枚ガイド）

> **役割**: 「StoryTemplate を複製したい」「raw を入れる場所は?」「どこで執筆?」に 1 ページで答える、Claude / Agent / 人間共通の onboarding ガイド。
> **詳細**: 運用契約は `CLAUDE.md`、ドメイン教義は `docs/domain/`。
> **更新日**: 2026-07-06（正本統合・core+overlay 構造）

---

## 1. 全体図（鳥瞰）

```
┌──────────────────────────────────────────────────────────────┐
│ StoryTemplateEvolutionLab/   （StoryTemplate 開発リポジトリ） │
│                                                              │
│  current/                ← 現在の正本（自己完結）             │
│    ├── WORKFLOW.md       ← このファイル（1枚ガイド）          │
│    ├── CLAUDE.md         ← AI運用契約（人間ゲート・大原則）   │
│    ├── INHERITANCE.md    ← 継承マップ                        │
│    ├── docs/             ← 仕様の要約版（kernel_spec 等）     │
│    │   └── domain/       ← ★ドメイン正本（56語/86項目/DoR）  │
│    ├── template/         ← ★新作がコピーする雛形             │
│    │   ├── core/  overlay/  runtime/  inbox/  synthesis/     │
│    │   └── folder_structure.md（作品の完全構造定義）          │
│    ├── adapter/          ← intake/writing/handoff + 検証7本   │
│    ├── agents/(18) skills/(7) prompts/ craft/                │
│    ├── takt/             ← ループ実装（暫定）                 │
│    ├── tools/            ← ontology_check.py                 │
│    ├── learning/         ← template 進化の決着記録            │
│    └── work_init/        ← bootstrap 手順                    │
│                                                              │
│  proposal/               ← 提案（出典・凍結スナップショット） │
│  archive/                ← 凍結された旧資産                   │
│  improvement_request_inbox/ ← STE 自身への改善受付            │
└──────────────────────────────────────────────────────────────┘
                    ↓ 新規 work 立ち上げ時、current/template/ から copy
┌──────────────────────────────────────────────────────────────┐
│ works/{your-slug}/       ← あなたの作品（current の外・独立） │
│                                                              │
│  work.manifest.json      ← 構造宣言（core version/overlay/逸脱）│
│                                                              │
│  inbox/                  ★ raw を入れる場所                   │
│    ├── planning_sessions/   企画 chat / 既存 bible package    │
│    └── fragments/           断片メモ                          │
│                                                              │
│  synthesis/              ← Intake Adapter 出力                │
│    ├── session_digests/     Digest（読み物）                  │
│    └── update_proposals/    反映指示書 = G-Intake の承認対象   │
│                                                              │
│  core/                   ← 全作品共通の背骨                   │
│    ├── kernel.yaml       ★ 作品の核（11項目・12値status）     │
│    ├── bible/            ★ 安定設定（17 facet）               │
│    ├── design/           ← 揺れる設計（open-questions 等）    │
│    ├── state/            ★ オントロジー（entities/knowledge/  │
│    │                        foreshadowing/timeline）          │
│    ├── checklists/ rules/ schema/                             │
│                                                              │
│  (overlay 展開)          ← manifest で選んだ執筆単位構造       │
│    ├─ episode-pack:  writing/episode_packs/{ep}/（4ファイル） │
│    └─ packet-2stage: packets/{状態}/ + scenes/{状態}/          │
│                                                              │
│  runtime/                ★ 作業ログ・成果物                   │
│    ├── drafts/           ★ 執筆をガリガリ進める場所           │
│    ├── reviews/            レビュー票（採否判定付き）          │
│    ├── approved/ → published/  承認済 → 公開済               │
│    ├── reader-export/      公開用テキスト（メタ除去）          │
│    └── logs/{runs,sessions,learning}/                        │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. 「StoryTemplate を複製する」3つの起点

### 起点 A: 新規作品をゼロから始める

```
1. works/{slug}/ を新規作成（current の外）
2. current/work_init/new-work-bootstrap.md の手順を踏む
   （core+inbox+synthesis+runtime を copy、kernel/manifest をリネーム）
3. inbox/planning_sessions/ に企画 chat を入れる
4. Intake Adapter → G-Intake → bible に反映
5. DoR-A 通過 → drafting 開始
```

### 起点 B: 既存作品（v3/旧v4 形式）を移行

```
1. 作品側 archive/ にスナップショット
2. core+overlay 構造を作成（bootstrap 手順 1-5）
3. 既存ファイルを core/bible/{facet} に再配置、kernel.yaml 更新（premise → logline）
4. DoR-A 検証
```
→ 実例: `docs/domain/08_pilot_validation/`（3作品の walkthrough）、手順: `docs/domain/10_migration_plan.md`

### 起点 C: 外部完成 bible package を取り込む

```
1. 外部生成された bible package を inbox/planning_sessions/ に保存
2. Intake Adapter で 86項目チェックリスト（docs/domain/05）に照らして分割
3. 本文 prose が混在していれば bible から runtime/drafts/ に剥がす
4. facet 別 update_proposal を生成 → G-Intake 承認 → bible/design/state に分配
```

---

## 3. raw → 公開までの実走ループ（Phase 別）

### Phase 1: Intake（raw → bible）　…ゲート: **G-Intake**

```
[企画 chat / 既存資料]
  → inbox/planning_sessions/{date}_{slug}.md   ★raw はここで止まる
  → [adapter/intake_adapter.md 実行]（86項目 + 12値 status 付与）
  → synthesis/session_digests/ ＋ synthesis/update_proposals/
  → [adapter/review_prompts/ で検証]（digest / coverage / contradiction / proposal）
  → [G-Intake 人間承認] → core/{bible,design,state} に確定反映
  → [bible-readiness-review で DoR-A 判定]
```

### Phase 2: 設計（bible → 執筆単位）　…DoR-B/C

overlay により分岐。**episode-pack**: scene card + acceptance contract を作る。**packet-2stage**: packet を scoped → frozen（DoR-C = packet freeze review）→ scene slotting。

### Phase 3: Writing（Writing Pack → 公開）　…ゲート: **G-Deliverable / G-Publish**

```
[adapter/writing_adapter.md] bible 全体でなく「1話分」に圧縮
  ＋ ontology k-hop 抽出（state/ から当該話の関係だけ）
  → Writing Pack（brief / scene_card / context_pack / acceptance_checklist）
  → [core/rules/drafter-preflight.md] Gate 0/A/C + 因果一段落 + 知識状態台帳
  → runtime/drafts/ で draft
     ↺ [takt/workflows/draft-episode.yaml] draft → ontology_check →
        multi-pass review → 修正（loop_monitor が堂々巡りを打切り）
  → runtime/reviews/ にレビュー票（採否判定まで）
  → [G-Deliverable 人間承認] → runtime/approved/
  → [G-Publish 人間承認]（kakuyomu-policy 適合確認）→ 投稿 → runtime/published/
  → state 更新（knowledge_state / foreshadowing / timeline）+ retro を logs/learning/
```

---

## 4. onboarding（新セッションの AI が読む順）

1. **本ファイル**（全体図）
2. **`CLAUDE.md`** — 運用契約（人間ゲート・大原則・core/overlay 三分）
3. **`docs/domain/02_domain_model.md`** — 56語の用語
4. **`template/folder_structure.md`** — 物理配置
5. **`docs/domain/04_pipeline_overview.md`** — 動作の詳細
6. 目的別 deep-dive: 立ち上げ→`work_init/new-work-bootstrap.md` / intake→`adapter/intake_adapter.md`+`docs/domain/05` / DoR→`docs/domain/06` / drafting→`template/core/rules/drafter-preflight.md` / ループ→`takt/README.md`

---

## 5. 役割別の入口

| あなたの役割 | 最初に読む |
|---|---|
| 新規 work を立ち上げる | `work_init/new-work-bootstrap.md` |
| 既存 work を移行する | `docs/domain/08_pilot_validation/` + `10_migration_plan.md` |
| raw を inbox に入れた | `adapter/intake_adapter.md` |
| Drafter | `agents/drafter.md` + `template/core/rules/drafter-preflight.md` |
| Plotter | `agents/plotter.md` |
| Critic / Reviewer | `agents/critic.md` + `adapter/review_prompts/` + `template/core/rules/review-gate.md` |
| Continuity Checker | `agents/continuity-checker.md` + `tools/ontology_check.py` |
| ループを回す | `takt/README.md` + `takt/workflows/` |
| StoryTemplate 自体を編集する | `../.claude/CLAUDE.md` + `../proposal/README.md` |

---

## 6. 重要な不変条件（Top 10）

1. **raw を直接 bible に流さない** — inbox → Intake Adapter → synthesis 経由必須
2. **bible 全体を drafter に渡さない** — Writing Adapter で1話分に圧縮
3. **bible を直接書き換えない** — update_proposal / canon patch 経由必須
4. **人間ゲート（G-Intake / G-Deliverable / G-Publish）を AI 判断で通過させない**
5. **Review は種別必須・採否まで** — "Review" 単独使用禁止、レビュー票は採用/条件付/却下/learning送りまで書く
6. **State は append-only** — 履歴を削除しない（知識状態の単調性）
7. **drafts は runtime/drafts/ のみ** — bible に prose を同居させない（Sample Scene 例外）
8. **作品固有 facet は generic 雛形（template/）に流入させない** — 逸脱は work.manifest に理由付き宣言
9. **空欄禁止 = status 明示** — 全 field に 12値 status（`docs/status_vocabulary.md`）
10. **archive / 凍結 proposal を編集しない**

---

## 7. 困ったときの参照順

```
迷ったら:
  ├── 用語が分からない       → docs/domain/02_domain_model.md
  ├── どこに置く?            → template/folder_structure.md（背景: docs/domain/03）
  ├── 何をする順序?          → docs/domain/04_pipeline_overview.md
  ├── 何を埋める?            → docs/domain/05_intake_coverage_checklist.md
  ├── DoR 通過してる?        → docs/domain/06_bible_dor.md
  ├── どの検証 prompt?       → adapter/review_prompts/README.md
  ├── AI がどこまで自律?     → adapter/human_approval_policy.md
  ├── 既存 work の例は?      → docs/domain/08_pilot_validation/
  ├── 迷った時の遡上先       → template/core/rules/reverse-flow.md
  └── 歴史・出典を見たい     → ../proposal/（凍結）・../archive/（凍結）
```

---

## 8. 「今なにをしたい？」→ どこを見るか

| やりたいこと | 入口 |
|---|---|
| 運用ルールを知る | `CLAUDE.md` |
| 新作を立ち上げる | `work_init/new-work-bootstrap.md` |
| 企画を作品に流し込む | `adapter/intake_adapter.md` |
| 1話書く | `adapter/writing_adapter.md` → `takt/workflows/draft-episode.yaml` |
| レビューを回す | `takt/workflows/review-multipass.yaml` |
| 整合性を検査する | `tools/ontology_check.py works/{slug}/core` |
| TAKT を理解する | `takt/README.md`（暫定） |
| 置換の根拠を読む | `../proposal/2026-07-06-workbench-ontology-loop/PROPOSAL.md`（出典） |
