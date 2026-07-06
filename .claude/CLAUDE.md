# StoryTemplateEvolution — Claude Code Instruction

> このリポジトリは **StoryTemplate そのものを開発するメタリポジトリ**。
> 各作品（works/{slug}/）と同じ階層にあるが、作品ではなく **template 開発** が主目的。

---

## このリポジトリで Claude が従うべきこと

### 1. 三本柱を守る

```
StoryTemplateEvolution/
├── current/          ← 現在の正本（編集可、Patch 推奨）
├── proposal/         ← 提案（履歴 + アクティブ）
└── archive/          ← 凍結された旧資産（編集禁止）
```

- **archive/ を編集しない**。snapshot として永続保存。
- **current/ の編集は Patch 経由が望ましい**（直接書き換えではなく、proposal/ で議論してから反映）。
- **新しい提案は proposal/{date}-{slug}/ に作る**。

### 2. 正本の層構造（2026-07-06 統合後）

- **構造・運用の正本**: `current/`（2026-07-06 に workbench 版で全面置換。旧 current は `archive/2026-04-31-integreated/` に凍結）
  - 置換の根拠: `proposal/2026-07-06-workbench-ontology-loop/PROPOSAL.md`
- **ドメイン語彙の正本**: `proposal/2026-04-30-zero-base-v4/`（採用済み・現役）

不明点があれば最初に読むべきもの:
- `current/WORKFLOW.md` — 1 枚ガイド
- `current/CLAUDE.md` — 運用契約（人間ゲート・core/overlay・オントロジー）
- `current/INHERITANCE.md` — 継承マップ（何が踏襲で何が新規か）
- `proposal/2026-04-30-zero-base-v4/02_domain_model.md` — 56 語の Card（用語の正本）
- `current/template/folder_structure.md` — 物理配置（core+overlay）

### 3. supersede stub に注意

`current/docs/vocabulary.md`、`current/docs/dor_dod.md` は **supersede stub**。これらは編集せず、内容は `proposal/2026-04-30-zero-base-v4/` を参照。

### 4. 各 work と StoryTemplate の境界を守る

- 作品固有内容（三層対応 / 章末資料 / 批評性 等）を `current/template/` に積まない。core / overlay / work-local の三分は `current/CLAUDE.md` §3 に従う
- 共通 rule / agent / skill は `current/{agents,skills,template/core/rules}/` に集約
- 作品側の逸脱は work.manifest の `deviations_from_core` に理由付きで明示

### 5. 統合後の TODO（COVERAGE §3 / INHERITANCE 未完節）

- DoR/DoD 正本の一本化（stub は v4 06_bible_dor.md を指す。`template/core/checklists/dor_dod.md` との関係整理）
- agents / skills ↔ TAKT facets 対応表の作成
- design/ 実体テンプレ4本と `state/rejected_ideas.md` 雛形の追加
- 17 facet 中未整備の System / Timeline / Sample Scene テンプレ追加
- craft/ rubric 実体化

詳細: `proposal/2026-07-06-workbench-ontology-loop/COVERAGE.md` Section 3。

---

## このリポジトリで Claude が **やってはいけない**

- archive/ 配下のファイルを編集する（`archive/2026-04-31-integreated/` の旧 current 含む）
- proposal/ の旧提案（v2 / v3 / pilot-driven 等）を編集する（履歴）
- current/template/ に作品固有 facet を積む
- kernel.template.yaml の `schema_version: "v4"` を変える（破壊的変更）
- supersede stub を直接書き換える（proposal/.../ 側で議論する）
- 人間ゲート（G-Intake / G-Deliverable / G-Publish）を AI 判断で通過させる

---

## 関連参照

- `README.md` — リポジトリ全体の三本柱説明
- `current/README.md` — 現在の正本一覧
- `current/WORKFLOW.md` — 複製 → raw → 執筆の全体図
- `proposal/README.md` — 提案 status 表
- `archive/README.md` — 凍結された旧資産
