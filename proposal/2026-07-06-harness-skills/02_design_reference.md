# 設計詳細: リファレンス整備（README / オントロジー導線 / harness_map）

> PROPOSAL.md Phase 2 の具体設計。

## 1. current/docs/harness_map.md（新規・COVERAGE §3 TODO #4 消化）

構成:

### §1 機構ガイド「何がいつ動くか」

| 機構 | 実体 | 起動タイミング |
|---|---|---|
| CLAUDE.md | 作品 `.claude/CLAUDE.md` | セッション開始時に常時読込 |
| rules | 作品 `.claude/rules/*.md` | 常時読込（執筆規律） |
| skill | 作品 `.claude/skills/*/SKILL.md` | ユーザー/AI が作業単位で起動（/draft 等） |
| agent | 作品 `.claude/agents/*.md` | skill またはメインループが subagent として委譲 |
| TAKT facet | `takt/facets/**` | TAKT workflow YAML がプロンプト合成時に読込 |
| TAKT workflow | `takt/workflows/*.yaml` | ループ実行（packet-cycle 等） |

### §2 対応表（skills × agents × facets × rules × workflows）

| skill | 委譲先 agents | 対応 TAKT facet/workflow | 常時 rules |
|---|---|---|---|
| pitch | plotter, strategist | facets/knowledge/ontology_slice | story-os-boundaries |
| draft | drafter | personas/drafter + policies/drafter_preflight + workflows/draft-episode | drafter-preflight |
| critic | critic | personas/critic + output_contracts/review_ticket | review-gate |
| continuity | continuity-checker | （facet 未整備 → 乖離注意） | — |
| review-meeting | critic, editor, continuity-guard | policies/review_gate + workflows/review-multipass | review-gate |
| retro-meeting | analyst, strategist, experimenter | （facet 未整備） | learning-capture 参照 |
| release | packaging-agent, policy-checker | （facet 未整備） | kakuyomu-policy 参照 |

（実作成時に 18 agents 全行を埋める。「同期が必要なペア」列を設け、retro 時の乖離チェック対象を明示）

### §3 supersede stub 一覧

docs/dor_dod.md / docs/vocabulary.md / skills/（変換後）/ agents/（変換後）/ prompts/（変換後）→ それぞれの正本パス

## 2. ルート README.md への追記

「リファレンス（迷ったらここ）」節を新設:

| 知りたいこと | 正本 |
|---|---|
| 用語の定義（56語 Card） | proposal/2026-04-30-zero-base-v4/02_domain_model.md |
| status 語彙（12値）・Lock・Judge | current/docs/status_vocabulary.md |
| オントロジー schema（entity / relation） | current/template/core/schema/ |
| 単位階層（Manuscript〜Beat） | current/docs/unit_taxonomy.md |
| kernel 11項目仕様 | current/docs/kernel_spec.md |
| Layer × Facet 対応 | current/docs/layer_facet_map.md |
| skills / agents / facets の接続 | current/docs/harness_map.md（新規） |
| DoR / DoD | proposal/2026-04-30-zero-base-v4/06_bible_dor.md |

## 3. current/README.md への追記

- 正本一覧表に `.claude/`（template/core/.claude/: 作品複製用ハーネス資産）行を追加
- 「skills/ agents/ prompts/ は supersede stub。正本は template/core/.claude/ とルート .claude/skills/」の注記

## 4. current/docs/README.md への追記

- supersede stub の一覧と正本パス（harness_map §3 と同内容の短縮版）

## 5. Lab 用 .claude/CLAUDE.md への追記

- 「ハーネス資産の所在」節: Lab skill 一覧（new-proposal / audit-gaps / consistency-check / ontology-check 等）と使いどころ
- 「作品側 .claude/ は template/core/.claude/ から複製される。Lab の .claude/ とは別物」の明記（混同防止）

## 6. proposal/README.md への追記

- status 表に本提案の行を追加（draft → 承認後 adopted）
