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

### 2. v4 を正本とする

**現在の正本提案**: `proposal/2026-04-30-zero-base-v4/`

不明点があれば最初に読むべきもの:
- `proposal/2026-04-30-zero-base-v4/00_README.md` — 提案の入口
- `proposal/2026-04-30-zero-base-v4/02_domain_model.md` — 56 語の Card（用語の正本）
- `proposal/2026-04-30-zero-base-v4/03_storage_trinity.md` — 物理配置
- `proposal/2026-04-30-zero-base-v4/04_pipeline_overview.md` — 動作正本
- `current/WORKFLOW.md` — 1 枚ガイド

### 3. supersede stub に注意

`current/docs/vocabulary.md`、`current/docs/dor_dod.md`、`current/adapter/folder_structure.md` は **supersede stub**。これらは編集せず、内容は proposal/.../ を参照。

### 4. 各 work と StoryTemplate の境界を守る

- 作品固有内容（三層対応 / 章末資料 / 批評性 等）を `current/templates/` に積まない
- 共通 rule / agent / skill は `current/{rules,agents,skills,templates/.claude/}/` に集約
- 作品横断の learning は `current/learning/`

### 5. 採用後の TODO（90 日以内）

- writing_adapter_prompt.md の v4 化（Q-B-001）
- update_proposal_format.yaml / field_mapping_template.yaml の v4 化
- bible/ facet 雛形 13 ファイル新規作成
- prompts/00-05 の参照更新
- craft/ コンテンツ整備（Q-B-003）
- agents / skills の dir 参照を v4 に書き換え

詳細: `proposal/2026-04-30-zero-base-v4/09_open_questions.md` Section 2-3。

---

## このリポジトリで Claude が **やってはいけない**

- archive/ 配下のファイルを編集する
- proposal/ の旧提案（v2 / v3 / pilot-driven 等）を編集する（履歴）
- current/templates/ に作品固有 facet を積む
- kernel.template.yaml の `schema_version: "v4"` を変える（破壊的変更）
- supersede stub を直接書き換える（proposal/.../ 側で議論する）

---

## 関連参照

- `README.md` — リポジトリ全体の三本柱説明
- `current/README.md` — 現在の正本一覧
- `current/WORKFLOW.md` — 複製 → raw → 執筆の全体図
- `proposal/README.md` — 提案 status 表
- `archive/README.md` — 凍結された旧資産
