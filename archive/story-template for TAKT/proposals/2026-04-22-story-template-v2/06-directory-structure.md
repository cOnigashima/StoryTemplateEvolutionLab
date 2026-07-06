# 提案ディレクトリ構造と命名規約

本ファイルは v2 完成時点の **template ディレクトリ構造**を定義する。既存構造との差分を明記し、各ファイルの存否区分（template / sample / runtime-optional / deprecated）を示す。

---

## 1. 全体構成

```
story-template/
├── README.md                                   [template]
├── CLAUDE.md                                   [template, 更新]
├── template.manifest.json                      [template, 更新]
│
├── story/
│   ├── promises.md                             [template]
│   ├── open-questions.md                       [template]
│   ├── design-debt.yaml                        [template]
│   ├── foreshadowing-map.md                    [template, 新規]
│   ├── canon-patch-proposals/
│   │   └── README.md                           [template]
│   ├── seeds/
│   │   ├── README.md                           [template]
│   │   ├── seed-index.yaml                     [template, 新規]
│   │   └── seed-template.md                    [template, 新規]
│   └── intake/
│       ├── README.md                           [template, 更新]
│       ├── raw-index.yaml                      [template, 新規]
│       ├── digest-index.yaml                   [template, 新規]
│       ├── provenance.yaml                     [template, 新規]
│       ├── reflection-ledger.md                [template, 新規]
│       ├── raw/
│       │   └── .gitkeep                        [template]
│       └── digests/
│           ├── .gitkeep                        [template]
│           └── digest-template.md              [template, 新規]
│
├── bible/
│   ├── world.md                                [template]
│   ├── characters.md                           [template]
│   ├── rules.md                                [template]
│   ├── glossary.md                             [template, 新規]    ← ドメイン語の正本
│   └── templates/                              [template, 新規]
│       ├── character-sheet.md
│       ├── relationship-sheet.md
│       └── world-sheet.md
│
├── arcs/
│   ├── series-overview.md                      [template]
│   └── arc-01.md                               [template]
│
├── packets/
│   ├── README.md                               [template]
│   ├── templates/                              [template, 新規]    ← 既存 packet-template.yaml の移設先
│   │   ├── packet-template.yaml
│   │   ├── packet-exploring-skeleton.md
│   │   ├── packet-scoped-skeleton.md
│   │   ├── packet-frozen-skeleton.md
│   │   └── packet-freeze-checklist.md
│   ├── exploring/
│   │   └── .gitkeep                            [template]          ← packet-template.yaml はここから除去
│   ├── scoped/
│   │   └── .gitkeep                            [template]
│   ├── frozen/
│   │   └── .gitkeep                            [template]
│   └── drafting/                               [template, 新規]    ← frozen のコピーを置いて改稿する場所
│       └── .gitkeep
│
├── scenes/
│   ├── README.md                               [template]
│   ├── seed/
│   │   └── scene-template.md                   [template]
│   ├── slotted/
│   │   └── .gitkeep                            [template]
│   └── superseded/
│       └── .gitkeep                            [template]
│
├── drafts/
│   ├── README.md                               [template, 新規]
│   └── .gitkeep                                [template]
│
├── reviews/
│   ├── README.md                               [template, 更新]
│   ├── typed-review-template.md                [template, 更新]
│   ├── bridge-review-template.md               [template]
│   ├── seed-to-macro-template.md               [template]
│   ├── continuity-review-template.md           [template, 新規]
│   ├── persona-review-template.md              [template, 新規]
│   ├── approval-template.md                    [template, 新規]
│   └── packet-freeze-template.md               [template, 新規]
│
├── learning/
│   ├── README.md                               [template, 新規]
│   ├── current-focus.yaml                      [template, 新規]
│   └── .gitkeep                                [template]
│
├── craft/                                       [template, 新規]    ← Craft Library 全体
│   ├── README.md
│   ├── principles.md
│   ├── scene-sequel.md
│   ├── want-need.md
│   ├── scope-management.md
│   ├── beat-sheets.md
│   ├── foreshadowing.md
│   ├── motif-operations.md
│   ├── rubric.md
│   ├── reader-personas.md
│   ├── cadence.md
│   ├── dialogue-craft.md
│   ├── description-craft.md
│   ├── pov-craft.md
│   ├── reveal-plan.md
│   ├── conflict-design.md
│   ├── character-design.md
│   ├── world-design.md
│   ├── theme-design.md
│   ├── genre-patterns.md
│   ├── editing-craft.md
│   ├── sanderson-laws.md
│   ├── knox-rules.md
│   ├── checklists/
│   │   ├── seed-check.md
│   │   ├── scoped-check.md
│   │   ├── frozen-check.md
│   │   ├── drafting-check.md
│   │   └── approval-check.md
│   └── worksheets/
│       ├── want-need-sheet.md
│       ├── beat-sheet-save-the-cat.md
│       ├── scene-sequel-sheet.md
│       ├── foreshadow-sheet.md
│       └── cadence-sheet.md
│
├── prompts/
│   ├── README.md                               [template, 更新]
│   ├── common-preamble.md                      [template]
│   ├── promises.md                             [template]
│   ├── world.md                                [template]
│   ├── characters.md                           [template]
│   ├── rules.md                                [template]
│   ├── series-overview.md                      [template]
│   ├── arc-01.md                               [template]
│   ├── packet-scoped.md                        [template]
│   ├── packet-freeze-check.md                  [template]
│   ├── scene-batch.md                          [template]
│   ├── intake/                                 [template, 新規]
│   │   ├── raw-submission.md
│   │   ├── digest-writer.md
│   │   ├── seed-extractor.md
│   │   ├── seed-to-macro-reviewer.md
│   │   └── pro-research-brief.md
│   └── review/                                 [template, 新規]
│       ├── part-a-per-scene.md
│       ├── part-b-dialogue-deep.md
│       ├── part-c-macro-structure.md
│       ├── persona-A.md
│       ├── persona-B.md
│       └── persona-C.md
│
├── approved/
│   └── .gitkeep                                [template]
│
├── published/
│   └── .gitkeep                                [template]
│
├── samples/                                     [template, 新規]    ← サンプル作品の断片（削除可）
│   ├── README.md
│   ├── sample-packet/
│   ├── sample-scene/
│   ├── sample-draft/
│   └── sample-review/
│
├── community/
│   └── README.md                               [template]
│
└── .claude/
    ├── agents/                                  [template]
    │   └── (既存 agents + 新設)
    ├── skills/                                  [template]
    │   └── (既存 skills + 新設: /seed-to-macro, /freeze-review, /critic-bridge, /audience-review)
    └── rules/                                   [template, 一部更新/新設]
        ├── learning-capture.md                  [既存]
        ├── drafter-preflight.md                 [既存、更新]
        ├── file-growth.md                       [既存]
        ├── story-os-boundaries.md               [既存]
        ├── kakuyomu-policy.md                   [既存]
        ├── intake-flow.md                       [新規]
        ├── review-system.md                     [新規]
        ├── vocabulary-lint.md                   [新規]
        └── monitoring-dictionary-generic.md     [新規]    ← 作品固有辞書の書き方ガイド
```

---

## 2. 削除または移送するもの

### 2.1 ルート直下

| 現状 | 処置 | 理由 |
|---|---|---|
| `actions/` | **runtime-optional に降格 or 削除** | W8。template 初期には要らない |
| `campaigns/` | 同上 | 同上 |
| `telemetry/` | 同上 | 同上 |
| `queue/` | **deprecated マーク** | story-os-boundaries §queue は projection |
| `backlog/` | **deprecated マーク or 廃止** | story-os-boundaries §backlog は legacy |

これらは `template.manifest.json` で `runtime_optional` / `deprecated` の区分に明示。

### 2.2 `packets/` 配下

| 現状 | 処置 |
|---|---|
| `packets/exploring/packet-template.yaml` | `packets/templates/packet-template.yaml` に移設 |
| `packets/scoped/packet-template.yaml` | 同上、exploring/scoped/frozen の 3 箇所にあるのを 1 箇所に集約 |
| `packets/frozen/packet-template.yaml` | 同上 |

### 2.3 story-os-boundaries の更新

v2 で追加する境界:

```diff
 - 物語の入口は `story/seeds/`。`backlog/` は legacy 資産であり、正規 intake とはみなさない
+- 物語の入口は `story/intake/raw/` → `story/intake/digests/` → `story/seeds/`。raw は原文を失わない、digest は batch 要約、seed は再利用核
+- provenance.yaml は raw / digest / seed / canon の繋がりを保持する正本
+- reflection-ledger.md は「未反映の inbox」。空欄は禁止
+- craft/ は一般知識の正本。bible/ は作品固有上書き
+- runtime artifacts (actions/, campaigns/, telemetry/, queue/) は default では存在しない。必要な作品のみ opt-in
```

---

## 3. 命名規約

### 3.1 ファイル命名

| 対象 | 規約 | 例 |
|---|---|---|
| Arc | `arc-NN.md`（NN は 01 から） | `arc-02.md` |
| Packet | `packet-NNN-{slug}.md` または `.yaml` | `packet-003-school-entry.yaml` |
| Episode draft | `drafts/packet-NNN/epNN.md` | `drafts/packet-003/ep17.md` |
| Scene card (slotted) | `packet-NNN-epNN-{slug}.md` | `packet-003-ep17-hallway-encounter.md` |
| Scene card (seed) | `scenes/seed/seed-{slug}.md` | `scenes/seed/seed-mirror-room.md` |
| Seed | `seed-NNN-{slug}.md` | `seed-042-magic-rebuild.md` |
| Raw | `raw/YYYY-MM-DD-{source}-{slug}/` | `raw/2026-04-22-pro-arc02-worldbuilding/` |
| Digest | `digests/YYYY-MM-DD-{source}-{slug}.md` | 同上 |
| Typed Review | `typed-review-packet-NNN-epNN.md` | `typed-review-packet-003-ep17.md` |
| Bridge Review | `bridge-review-packet-NNN-to-packet-MMM.md` | `bridge-review-packet-002-to-packet-003.md` |
| Continuity Review | `continuity-review-{range-slug}.md` | `continuity-review-packet-001-to-003.md` |
| Persona Review | `persona-review-{A/B/C}-{target-slug}.md` | `persona-review-A-packet-003-ep17.md` |
| Approval Review | `approval-packet-NNN-epNN.md` | `approval-packet-003-ep17.md` |
| Canon Patch | `patch-NNN-{slug}.md` | `patch-017-motif-bell-clarification.md` |
| Learning log | `YYYY-MM-DD-{slug}.md` | `2026-04-22-multi-pass-adoption.md` |
| Foreshadow id | `PF-NNN` | `PF-042` |

### 3.2 id/slug の使い分け

- **id**（数字）は `packet-NNN`, `seed-NNN`, `PF-NNN`, `patch-NNN` のように機械可読前提
- **slug**（英小文字 + ハイフン）は人間向けキーワード。半角英数字 + ハイフン
- id と slug はファイル名で必ずセット（`packet-003-school-entry.yaml`）

### 3.3 ディレクトリ命名

- 小文字 + ハイフン区切り
- `samples/` `templates/` `checklists/` `worksheets/` など機能語は複数形 or 慣例に従う
- `.gitkeep` は空ディレクトリの保存用、ユーザーは無視

### 3.4 前後比較のための supersede

- 旧版を残したい場合:
  - packet: `packet-NNN-{slug}-v1-superseded.yaml`（ファイル名）
  - scene: `scenes/superseded/packet-NNN-epNN-{slug}-v1.md`
- 履歴は必ず「**元ファイル** + 旧版別ファイル」の 2 本体制

---

## 4. artifact 区分（template.manifest.json 拡張）

新 manifest 構造:

```json
{
  "version": "2.0",
  "artifacts": {
    "template": [
      "CLAUDE.md",
      "README.md",
      "story/promises.md",
      "story/open-questions.md",
      "story/design-debt.yaml",
      "story/intake/**",
      "story/seeds/**",
      "story/canon-patch-proposals/**",
      "story/foreshadowing-map.md",
      "bible/**",
      "arcs/**",
      "packets/templates/**",
      "packets/{exploring,scoped,frozen,drafting}/.gitkeep",
      "scenes/**",
      "drafts/README.md",
      "drafts/.gitkeep",
      "reviews/**",
      "learning/README.md",
      "learning/current-focus.yaml",
      "craft/**",
      "prompts/**",
      "approved/.gitkeep",
      "published/.gitkeep",
      "community/**",
      ".claude/**"
    ],
    "samples": [
      "samples/**"
    ],
    "runtime_optional": [
      "actions/**",
      "campaigns/**",
      "telemetry/**",
      "story/job-packets/**",
      "story/run-ledger/**"
    ],
    "deprecated": [
      "queue/**",
      "backlog/**"
    ]
  },
  "init_rules": {
    "samples_delete_on_start": true,
    "runtime_optional_generate_on_demand": true,
    "deprecated_block_reference": true
  }
}
```

- **template**: 作品 init 時に必ず存在
- **samples**: 学習用。作品開始時に削除推奨
- **runtime_optional**: 作品が必要になったら opt-in で生成（init 時はゼロ）
- **deprecated**: 使わない（参照を block すべき、ただし既存 repo 互換で残す）

---

## 5. 作品 init 手順（想定）

```
1. story-template を git clone
2. samples/ を削除（samples_delete_on_start）
3. CLAUDE.md を作品情報で編集（一行要約、フォーカス Arc/Packet）
4. story/promises.md に作品約束を記入
5. bible/rules.md に文体・視点・時制・禁則を記入
6. bible/glossary.md の作品固有語を追記（必要なら）
7. arcs/arc-01.md を拡張、packets/templates/ から packet-001-{slug}.yaml を複製
8. learning/current-focus.yaml を初期状態で記入
9. CLAUDE.md の「執筆開始ライン」項目が全て埋まっていることを確認
10. 作品固有の motif を立てる場合のみ `.claude/rules/monitoring-dictionary.md` を新設（作品側）
```

---

## 6. file-growth との整合

`.claude/rules/file-growth.md` は既存。v2 では以下を追加する:

```diff
+ craft/ の成長
+ 新項目追加: works の learning から昇格した原理を author 承認で craft/ に追加
+ ディレクトリが 25 ファイル超えたらカテゴリ別 sub-directory を検討
+ craft/archive/ に廃止項目を移動（削除ではない）

+ story/intake/ の成長
+ raw が月 50 ファイル超えたら年月別 sub-directory（raw/2026-04/ 等）
+ reflection-ledger が 500 行超えたら年度別に split
+ provenance が 1000 entry 超えたら works 別 sub に分割検討

+ reviews/ の成長
+ typed-review が packet 数分溜まったら packet-NNN/ 別 sub 化
+ persona-review は sub 化せず persona 別ファイル名で区別
```

---

## 7. 変更サマリ（before / after 差分早見表）

| 領域 | before | after |
|---|---|---|
| Craft 知識 | 存在しない（know_how_explore が外部） | `craft/` として template 正典化 |
| Intake 機械可読 | raw/digests/seeds ディレクトリのみ | raw-index / digest-index / seed-index / provenance / reflection-ledger を追加 |
| 作品固有の Motif | monitoring-dictionary は villainess-coc のみ | template に generic 運用ガイド、作品側は固有辞書を持つ |
| Review 種別 | typed / bridge / seed-to-macro | + continuity / persona / approval / packet-freeze |
| Rubric | 存在しない | `craft/rubric.md` 25 項目（標準重み） |
| Runtime artifacts | 一部残存 | 物理的に削除 + manifest で区別 |
| Packet template | exploring/scoped/frozen 各ディレクトリ | `packets/templates/` に集約 |
| Grep 検証 | 作品固有（villainess-coc） | `.claude/rules/review-system.md` で template 正典化 |
| Current focus | 存在しない | `learning/current-focus.yaml` |
