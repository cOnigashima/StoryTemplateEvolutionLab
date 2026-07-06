# Proposal: ハーネス対応 Skill/Agent 化とリファレンス整備

- **Status**: draft（G-Intake 待ち）
- **Date**: 2026-07-06
- **Slug**: harness-skills
- **前提**: current/ は 2026-07-06 workbench 統合後の正本。本提案は current/ への Patch 案であり、承認（人間ゲート）まで current/ は変更しない。

---

## 1. 課題

現状の skills / agents はハーネス（Claude Code / Cowork の実行機構）に載らない。

| 資産 | 現状 | 問題 |
|---|---|---|
| `current/skills/*.md`（7本） | `# /draft` 形式のプレーン手順書 | `.claude/skills/{name}/SKILL.md` + frontmatter でないため skill として起動できない |
| `current/agents/*.md`（18本） | ペルソナ文書 | `.claude/agents/*.md` の YAML frontmatter がなく subagent として委譲できない |
| `current/template/core/rules/` | プレーン rule 8本 | 作品側でハーネスが自動読込する配置（`.claude/rules/`）が未定義 |
| 作品側 CLAUDE.md | 雛形なし | bootstrap 手順に `.claude/` の言及なし。作品ごとに手書き |
| Lab 側 `.claude/` | CLAUDE.md + rules 1本のみ | prompts/00-05 相当の定型セッションが skill 化されていない |

また、リファレンス性の課題:

- skills / agents / TAKT facets / rules が「どのハーネス機構で・いつ動くか」の接続ガイドがない
- 56語 Card（ドメインモデル）・オントロジー（entity_schema / status_vocabulary）への導線が README から弱い
- COVERAGE §3 の TODO（dor_dod 3重複、agents↔facets 対応表、craft rubric 等）が未消化

## 2. 方針（決定事項）

1. **skills / agents / TAKT facets は併存**。役割が異なるため一本化しない。
   - **skill** = 人間または AI が起動する作業手順（`/draft` 等）。ハーネスの skill 機構に載せる
   - **agent** = subagent として委譲実行されるペルソナ。ハーネスの agent 機構に載せる
   - **TAKT facet** = TAKT workflow YAML がプロンプトに合成する素材。現状形式のまま
   - 三者の対応関係は **対応表**（`current/docs/harness_map.md`、新規）で明示 → COVERAGE §3 TODO #4 を兼ねる
2. **配置は両方整備**:
   - **作品複製用**: `current/template/core/.claude/`（skills / agents / rules / CLAUDE.md 雛形）。bootstrap で作品ルートへ複製
   - **Lab 開発用**: リポジトリルート `.claude/skills/`（proposal 運用・昇格・監査などの Lab 定型作業）
3. 変換は**内容を変えない形式移行**を原則とする（origin タグで由来追跡、旧ファイルは supersede stub 化）

## 3. スコープ（3フェーズ）

### Phase 1 — ハーネス化（作品側）

`current/template/core/.claude/` を新設:

```
current/template/core/.claude/
├── CLAUDE.md                     # 作品用運用契約の雛形（新規、§4参照）
├── AGENTS.md                     # 他ハーネス向け薄いポインタ（CLAUDE.md を参照せよ、のみ）
├── skills/
│   ├── pitch/SKILL.md            # ← current/skills/pitch.md を変換
│   ├── draft/SKILL.md
│   ├── critic/SKILL.md
│   ├── continuity/SKILL.md
│   ├── review-meeting/SKILL.md
│   ├── retro-meeting/SKILL.md
│   ├── release/SKILL.md
│   └── handoff/SKILL.md          # ← adapter/session_handoff.template.md を skill 化（新規、03参照）
├── agents/                       # ← current/agents/ 18本を frontmatter 付きに変換
│   ├── drafter.md / critic.md / continuity-checker.md / ...（18本）
└── rules/                        # ハーネスが常時読むべき規律のみ
    ├── story-os-boundaries.md / drafter-preflight.md / review-gate.md / file-growth.md
    └── （残り: intake-flow / reverse-flow / learning-capture / kakuyomu-policy は要判断 → Q1）
```

- 変換フォーマットの詳細は `01_design_harness.md`
- `current/skills/` と `current/agents/` の旧ファイルは supersede stub 化（正本は `.claude/` 側）
- `work_init/new-work-bootstrap.md` に「`.claude/` を作品ルートへ複製し CLAUDE.md の {{placeholder}} を埋める」ステップを追記
- `template/folder_structure.md` に `.claude/` を追記
- `work.manifest.template.json` に `template_snapshot_date` を追加（複製時点の固定、`03_design_lifecycle.md` §3.1）

### Phase 2 — ハーネス化（Lab 側）+ リファレンス整備

- ルート `.claude/skills/` を新設（Lab 定型作業の skill 化。`current/prompts/01-05` を基に変換）:
  - `new-work`（作品立ち上げ、`work_init/new-work-bootstrap.md` を実行する skill、03参照）
  - `new-proposal` / `improve-from-work`（←01）/ `audit-gaps`（←02）/ `extract-pattern`（←03）/ `apply-to-work`（←04）/ `consistency-check`（←05）/ `ontology-check`（tools/ontology_check.py 実行）
- ライフサイクル接合（`03_design_lifecycle.md`）: learning フォーマットに昇格候補フラグ追加（learning-capture rule 更新）、TAKT との境界固定（責務分界・runs_dir 整合・同期ペア宣言。TAKT 実装の深掘りは別セッション）
- `current/docs/harness_map.md` 新規: skills ↔ agents ↔ TAKT facets ↔ rules の対応表 + 「どのハーネス機構でいつ動くか」ガイド + **同期ペア列**（COVERAGE §3 TODO #4 消化）
- README 導線整備（詳細は `02_design_reference.md`）:
  - ルート README: 「リファレンス」節を追加（56語 Card / status_vocabulary / entity_schema / harness_map への導線）
  - `current/README.md`: `.claude/` 資産の節を追加
  - `current/docs/README.md`: supersede stub の一覧を明示
  - `.claude/CLAUDE.md`（Lab 用）: ハーネス資産の所在と Lab skill の使い方を追記

### Phase 3 — COVERAGE §3 TODO 消化（残り）

| TODO | 対応 |
|---|---|
| #2 dor_dod 3重複 | 正本 = v4 `06_bible_dor.md`。`template/core/checklists/dor_dod.md` を stub 化（`docs/dor_dod.md` は既に stub）。一本化は「機械判定分を ontology_check の DoR-A モードへ、残りを文書へ」の分割として実施（04 §2） |
| #3 kernel 簡略表記の統一 | 全 doc を grep し完全版表記に統一 |
| #5 craft rubric 実体化 | `current/craft/lenses/` に rubric 実体を追加（critic skill から参照） |
| design 実体テンプレ 4本 + `state/rejected_ideas.md` 雛形 | `template/core/design/` に追加 |
| 未整備 facet テンプレ（System / Timeline / Sample Scene） | `template/core/bible/_facet_templates/` に追加 |

Phase 3 は分量が大きいため、Phase 1-2 の承認・反映後に着手判断（分割 proposal 化も可）。

## 4. 作品用 CLAUDE.md 雛形の設計要点

- Story OS 6原則（current/CLAUDE.md §0）の作品向け要約
- 人間ゲート 3つ（G-Intake / G-Deliverable / G-Publish）— AI 判断で通過しない
- 参照導線: `core/kernel.yaml` → `core/bible/` → `core/state/`、overlay は `work.manifest.json` を見よ
- `deviations_from_core` の宣言義務
- {{work_slug}} 等の placeholder を bootstrap で埋める

## 5. DoD（検収基準）

- Phase 1: 新規作品を bootstrap → Claude Code で `/draft` `/critic` `/handoff` 等が skill として認識・起動できる。subagent 一覧に drafter / critic 等が出る
- Phase 2: `/new-work` で works/{slug} が G-Intake 提示まで自動で立ち上がる。harness_map.md から 8 skills × agents × facets の対応（同期ペア含む）が引ける。ルート README から 56語 Card に 1 クリックで到達
- Phase 3: dor_dod の正本が 1 箇所。ontology_check.py が rubric / design テンプレの存在を warning しない
- 全フェーズ: archive/ 無変更・旧 proposal 無変更・kernel schema_version "v4" 不変

## 6. Open Questions

- **Q1**: rules 8本のうち `.claude/rules/`（常時読込）に置く範囲。案: 執筆時に常時効くべき 4本（story-os-boundaries / drafter-preflight / review-gate / file-growth）のみ。残りは skill 本文から参照
- **Q2**: agents 18本すべて変換するか、TAKT 側で使う主要 8本程度に絞るか（残りは参考実装として温存）
- **Q3**: 既存 work（ia_society 等）への遡及適用。案: 今回は新規作品のみ。migration は v4 10_migration_plan.md の枠で別途
- **Q4**: `/new-work` skill が bootstrap のコピー作業まで自動実行してよいか、コマンド提示に留めるか。案: 作品フォルダは Lab の外に作るため、まずはコマンド提示 + 人間実行。フォルダアクセスがある環境では自動実行可

## 8. 設計ドキュメント

- `01_design_harness.md` — skill / agent / rule / CLAUDE.md の変換フォーマット
- `02_design_reference.md` — README・オントロジー導線・harness_map の設計
- `03_design_lifecycle.md` — 作品立ち上げ〜還元の接合と TAKT 境界（TAKT 深掘りは別セッション）
- `04_design_guidance.md` — 設計原則: 信頼性3層（pull / push / enforce）の割り当て、skill Preflight 規約、「次の一手」ポインタ、status 集計による不足リスト生成

## 7. リスクと規律整合

- supersede stub の増加 → harness_map.md と docs/README の stub 一覧で迷子を防ぐ
- 二重管理（`.claude/skills/` と TAKT facets）→ 対応表で「同期が必要なペア」を明示し、retro で乖離チェック
- 本提案は archive/ に触れない。current/ への反映は承認後に Patch として実施
