# 提案: Zero-Base Domain Redesign v4 — Intake Coverage と Bible DoR

> **日付**: 2026-04-30
> **位置付け**: v3-kernel（2026-04-29）と pilot-driven-evolution（2026-04-29）の上に立ち、ia_society / ore_tueee_school_hell / fools-with-cheating の 3 作品の実体を素材として、ゼロベースでドメインを整理し直す提案。
> **承認**: 本提案は author (taiji) と本セッションで合意した 4 論点 + 56 語の card pass を基盤とする。

---

## この提案が解決する問題

v3 kernel + 雛形 12 ファイルは、**現実の Bible package**（ia_society の `bible/ia_story_bible_v2/` 50 ファイル超、fools-with-cheating の `raw/` 35 ファイル）の厚みを受け止めきれていなかった。具体的に:

- v3 vocabulary に未登場の facet が複数あった: System（制度・能力体系）/ Timeline（2 階層）/ Sample Scene / Reveal Plan / Motif Ladder / Relationship Arc 等
- 単位軸（Manuscript / Part / Arc / Packet / Episode / Scene / Beat）と facet 軸（World / Characters / Rules ...）が同列に並んでいて衝突を捌き切れない
- "Premise" / "Backlog" / "Review" / "Plot" などが overloaded で、ファイル名・ディレクトリ名・概念名が混ざって運用が破綻
- intake 側の網羅チェックと Bible 受け入れ DoR が薄く、「raw → bible」の搬送品質が担保できない
- レビュープロンプトが intake stage に存在しない（draft 以降にしかない）

本提案はこれらに対して **(A) zero-base のドメインモデル**、**(B) intake 網羅チェックリスト**、**(C) Bible 受け入れ DoR**、**(D) intake-stage 用レビュープロンプト群** を提供する。

---

## 本提案の核

### 1. Card 書式によるユビキタス言語の格上げ

v3 の `docs/vocabulary.md`（3 列表）から、**8 フィールドの Card 書式**（英名 / Category / Definition / Role / Boundary / Examples / Lives in / Cousins）に格上げ。56 語を card 化し、衝突する語を Boundary 欄で明示的に切り分ける。

### 2. 単位 × Facet の二軸モデル（案 Z）

Bible は **Facet 主軸**で持つ。Unit を従属軸として facet の中にネストすることを許容し、Unit 主軸の資料は `arcs/ packets/ scenes/ drafts/` に出す。Facet only / Unit only / Facet × Unit 交差の 3 タイプすべてに自然な居場所を与える。

### 3. Bible / Design / State の三本柱

- **Bible** = frozen な設計（書く前に決まる、Patch 経由でしか変えない）
- **Design** = 揺れる設計（候補・open question・proposal）
- **State** = 制作中に動く事実（実装履歴・現在値・Ledger）

「設計意図は Bible、実装履歴は State」の境界を厳密化。Reveal Budget Sheet / Motif Ladder のような半 Bible 半 State 資料は **二層ファイル形式**（上半分 Bible、下半分 State）として扱う。

### 4. 不変条件: Bible に Draft を入れない

ia_society が `bible/ia_story_bible_v2/` 配下に `EPISODE_FULL_DRAFT` を 28 本同居させていた構造は、intake 時に剥がす対象。Bible 配下に許容するのは **Sample Scene のみ**（文体キャリブレーション資産として）。本編 prose は `drafts/` のみ。

### 5. Intake / Writing Adapter の 2 分割

- **Intake Adapter**: raw → Digest + Update Proposal（bible に直接流さない gatekeeper）
- **Writing Adapter**: bible / state → Writing Pack（bible 全体を drafter に渡さない圧縮器）

両者ともに human approval を経由する。

### 6. Action Packet 廃止 / Backlog 一本化

外部アクション（kakuyomu like / SNS 等）を独立 packet 化する案は撤回し、内部タスク・計画・外部アクションすべて **`backlog/{slug}.yaml` のフラット構造**に統合。`actions/` ディレクトリは `backlog/` にリネーム。

### 7. Premise → Logline へリネーム

Kernel #1 を "Premise"（overloaded で Egri 用法と衝突）から **Logline**（業界標準で 1-2 文の販売向け要約を一義的に指す）に変更。Premise は deprecated 宣言。

### 8. 作品固有 facet は generic 雛形に積まない

fools-with-cheating の三層対応 / 章末資料配置 / 批評性シート、ia_society の Relationship Arc / Voice Sample / Three-Layer State 等の作品固有 facet は、各 work の `bible/` に追加自由だが、**StoryTemplate の generic 雛形には流入させない**。

---

## 本提案の Definition of Done

- [ ] `proposal/2026-04-30-zero-base-v4/` 配下の全 11 ファイル + `07_review_prompts/` 配下の 7 ファイルが揃う
- [ ] 56 語の Card が `02_domain_model.md` に集約される
- [ ] Bible / Design / State の物理構造が `03_storage_trinity.md` に図示される
- [ ] raw → publish の全パイプラインが `04_pipeline_overview.md` で 1 ページに収まる
- [ ] `05_intake_coverage_checklist.md` を ia_society / ore_tueee / fools の 3 作品で試走可能な精度に到達
- [ ] `06_bible_dor.md` で 11 status 値 × DoR 通過可否表が完成
- [ ] `07_review_prompts/` 7 本がそれぞれ独立して LLM に貼り付けて使える状態
- [ ] `08_pilot_validation/` で 3 作品それぞれの walkthrough が記録される
- [ ] `01_supersession_map.md` で現行 docs/ adapter/ templates/ の retire / refactor 判定が完了
- [ ] `10_migration_plan.md` で採用後の移行手順 + rollback 手順が明文化

---

## 本提案の構成

| ファイル | 内容 | 役割 |
|---|---|---|
| `00_README.md` | 本ファイル | 入口 |
| `01_supersession_map.md` | 現行 docs/ adapter/ templates/ の取捨 | 移行マップ |
| `02_domain_model.md` | 56 語の Card 集約 | 正本ドメインモデル |
| `03_storage_trinity.md` | Bible / Design / State の物理構造 | 物理配置正本 |
| `04_pipeline_overview.md` | raw → publish 全体フロー | 動作正本 |
| `05_intake_coverage_checklist.md` | raw → bible の網羅チェックリスト | **主要成果物 1** |
| `06_bible_dor.md` | Bible 受け入れ DoR + 埋めるべき項目 | **主要成果物 2** |
| `07_review_prompts/` | 7 本の intake-stage レビュープロンプト | **主要成果物 3** |
| `08_pilot_validation/` | 3 作品での試走結果 | 妥当性検証 |
| `09_open_questions.md` | 未決論点 | 棚上げ管理 |
| `10_migration_plan.md` | 採用後の移行手順 + rollback | 運用手順 |

---

## 議論履歴と決着（4 論点）

本提案は次の 4 論点をすべて閉じてから書かれている。

### 論点 1: Learning は Bible 配下に置くか
**結論**: Bible 配下には置かない。
- (a) 作品横断の制作 learning（失敗ログ・retro）→ 各 work の `learning/` と、横断は `StoryTemplateEvolution/current/learning/`
- (d) 設計過程で出る learning ログ → 作品ごとの `design/` 配下

### 論点 4: 単位 × facet の二軸モデル
**結論**: 案 Z 採用。Bible は Facet 主軸、Unit は従属軸として facet の中にネスト。Unit 主軸の資料は `arcs/ packets/ scenes/ drafts/` に出す。判定ルール: 「その資料が消えたら、まず困るのは facet の理解か、unit の構造か」。

### 論点 3: Bible vs Ledger の境界
**結論**: Bible = frozen / State = 実装履歴 / Design = 揺れ / Patch を経由。`26_CANON_PATCH_LOG` `27_CONTRADICTION_LOG` `19_LINE_LEVEL_CLUE_PAYOFF_TABLE` などは State Ledger に再配置。Reveal Budget Sheet / Motif Ladder は二層ファイル。

### 論点 2: 設計と本文（drafts）の物理配置
**結論**: Bible に Draft を入れない。ia_society の `EPISODE_FULL_DRAFT` 同居は intake 時の剥がし対象。Sample Scene のみ Bible に許容（A 採用）。

### 追加決着事項

- **カード書式**: 英名 + Category + Definition + Role + Boundary + Examples + Lives in + Cousins
- **Transformation Curve**: Arc（単位）と Change Shape（変化形）の同名衝突を解消する命名
- **`bible/plot.md`**: デフォルト 1 ファイル、肥大時 `bible/plot/` ディレクトリに分割
- **Canon / Bible 二分法**: Canon = 性質（"これは canon である"）/ Bible = 場所
- **Premise → Logline リネーム**: Kernel #1 を改名、Premise は deprecated
- **Action Packet 廃止 / Backlog 一本化**: `backlog/{slug}.yaml` フラット
- **作品固有 facet 不流入**: generic 雛形に積まない
- **二層ファイル**: Reveal Budget / Motif Ladder は上半分 Bible / 下半分 State 同居許容
- **物理ディレクトリ名**: `actions/` → `backlog/` にリネーム

---

## 関連ファイル（参照素材）

### 現行 StoryTemplateEvolution
- `README.md`
- `docs/vocabulary.md` `docs/kernel_spec.md` `docs/dor_dod.md` `docs/layer_facet_map.md` `docs/unit_taxonomy.md` `docs/status_vocabulary.md`
- `adapter/intake_adapter_prompt.md` `adapter/writing_adapter_prompt.md` `adapter/folder_structure.md` `adapter/field_mapping_template.yaml` `adapter/update_proposal_format.yaml` `adapter/writing_pack_format.yaml` `adapter/human_approval_policy.md`
- `prompts/00_session_start.md` ほか 7 本
- `templates/bible/` `templates/design/` `templates/state/` `templates/writing/episode_pack/`

### 旧提案
- `proposal/2026-04-22-story-template-v2/`
- `proposal/2026-04-29-domain-kernel-v3/`
- `proposal/2026-04-29-pilot-driven-evolution/`
- `archive/proposal/storytemplate_workflow_handoff_pack_takt/`

### Pilot 作品
- `works/ia_society/bible/ia_story_bible_v2/` 50 ファイル超
- `works/fools-with-cheating/raw/` 35 ファイル
- `works/ore_tueee_school_hell/bible/` v1 完成済 + `story/seeds/` 8 ファイル

---

## 採用後の影響

- 現行 `docs/vocabulary.md` は本提案の `02_domain_model.md` に supersede される
- 現行 `docs/kernel_spec.md` の Kernel #1 `premise:` フィールドが `logline:` にリネームされる
- 現行 `docs/dor_dod.md` の DoR-A は本提案の `06_bible_dor.md` に supersede される
- 現行 `adapter/intake_adapter_prompt.md` は本提案の `07_review_prompts/intake-coverage-review.md` 等を参照する形に再構成される
- 既存 work の `actions/` は段階的に `backlog/` にリネーム
- 既存 work の `bible/premise.md` は段階的に `bible/logline.md` にリネーム

詳細は `10_migration_plan.md` を参照。

---

## 進化方針（継承）

v1 → v2-fat → handoff → v3-kernel → pilot-driven-evolution の進化方針を継承する:

- **Pull 型**: 新作品で必要になったときに template を引き出す
- **Retro 駆動**: 各作品 / 各 arc で retro を回し、効いた template を残す
- **凍結禁止**: 「最強テンプレ完成」を目指さない。常に v0 ベース
- **作品固有はコピーしない**: 別作品が「これ採用する」と決めたら個別コピー、template には積まない

本提案 v4 もまた、**ia_society / ore_tueee / fools-with-cheating の実走から抽象化された v0** であり、v5 への置き換えを前提とする。
