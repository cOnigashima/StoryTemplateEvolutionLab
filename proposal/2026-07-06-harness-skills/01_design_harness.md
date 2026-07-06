# 設計詳細: ハーネス形式への変換

> PROPOSAL.md Phase 1-2 の具体フォーマット。内容は既存資産から変えず、形式のみ移行する。

## 1. Skill 変換フォーマット

`current/skills/draft.md` → `current/template/core/.claude/skills/draft/SKILL.md`

```markdown
---
name: draft
description: >
  frozen packet / scene_cards から本編 prose を執筆する。
  「本文を書いて」「◯話を執筆」「draft して」等で起動。
  前提: Writing Pack が G-Intake 承認済みであること。
---

# /draft — 本文執筆

（以下、既存 current/skills/draft.md の本文をそのまま移植。
 v4 注記「work 固有の bible/ state/ を参照」は残す）

## 参照
- rules: .claude/rules/drafter-preflight.md
- agent: drafter（長い執筆は drafter subagent に委譲可）
- TAKT: takt/workflows/draft-episode.yaml と同一工程（対応表: docs/harness_map.md）
```

変換規則:

1. frontmatter の `description` に**起動トリガー**（ユーザーの言い回し）と**前提条件**を必ず書く。ハーネスはこの description だけを見て skill を選ぶため、ここが品質の要
2. 本文は既存手順書をそのまま。出力フォーマット指定・チェック観点は削らない
3. 末尾に「参照」節: 関連 rule / agent / TAKT workflow へのポインタ（harness_map と整合させる）
4. 補助資料が大きい場合は `skills/{name}/references/*.md` に分離し SKILL.md からリンク（SKILL.md 本体は 500行以内目安）
5. **Preflight 必須**（04_design_guidance.md §3）: 本文の最初のセクションは `## Preflight`。自分の前提（DoR）を検査し、欠ける場合は作業せず不足リストを status 集計付きで報告して停止する

7本の description 案（トリガー要約）:

| skill | description の骨子 |
|---|---|
| pitch | seed-first 構想。「アイデア出し」「新作の種」→ seed 形式で出力、packet 昇格まで |
| draft | packet → prose 執筆。前提: frozen packet |
| critic | draft への typed review。hard_gate 判定と issue routing |
| continuity | 過去話との整合性チェック 12観点。canon level 別 routing |
| review-meeting | critic / editor / continuity-guard の 3 subagent 合議 → gate 判定 |
| retro-meeting | analyst / strategist / experimenter の 3 subagent で振り返り → learning 出力 |
| release | 公開前整形。draft → approved。最終 12 チェック |

## 2. Agent 変換フォーマット

`current/agents/drafter.md` → `current/template/core/.claude/agents/drafter.md`

```markdown
---
name: drafter
description: >
  本文執筆担当。初稿の執筆・文体統一・会話文・情景描写を行う。
  /draft skill から、または長い執筆の委譲先として使う。
tools: Read, Write, Edit, Glob, Grep
---

あなたは本文を書く担当。実際の原稿を書く。

## 役割
（既存 current/agents/drafter.md の本文をそのまま）

## 制限
- プロット変更はしない / 設定を勝手に追加しない / 禁則を守る

## 参照ファイル
- core/bible/（style_voice・characters）
- runtime/approved/ 直近3話
```

変換規則:

1. `tools` は最小権限: 読み専門 agent（critic / continuity-checker / analyst 等）は `Read, Glob, Grep` のみ。書く agent（drafter / editor）のみ Write / Edit を付与
2. `description` に「どの skill から呼ばれるか」を書く（review-meeting → critic / editor / continuity-guard 等）
3. 参照パスは作品フォルダ基準（`core/bible/` 等）に書き換える（旧 `bible/rules.md` 形式は v3 パスなので修正）

Q2（PROPOSAL §6）: 優先変換 8本 = drafter / critic / editor / continuity-checker / plotter / analyst / strategist / experimenter（skill 7本が参照する面々）。残り 10本（sns-copy / kakuyomu-launch 等の運用系）は判断待ち。

## 3. Rules 配置

- `.claude/rules/` 移設対象（常時読込・執筆中いつでも効くべきもの）: story-os-boundaries / drafter-preflight / review-gate / file-growth
- `template/core/rules/` 残留（特定工程でのみ参照）: intake-flow / reverse-flow / learning-capture / kakuyomu-policy
- 移設は「移動」とし重複コピーを作らない。folder_structure.md と各参照元を更新

## 4. 作品用 CLAUDE.md / AGENTS.md 雛形

`current/template/core/.claude/CLAUDE.md`（雛形、placeholder は bootstrap で置換）:

```markdown
# {{work_title}} — 運用契約

この作品は StoryTemplate v4 に準拠する。逸脱は work.manifest.json の
deviations_from_core に理由付きで宣言済みのもののみ有効。

## Story OS 原則（要約）
ファイルが正本 / 空欄は明示 status / raw 直投入禁止 /
全体を 1 単位に流さない / レビューは採否判定まで / state は append-only

## 人間ゲート — AI 判断で通過しない
G-Intake（構想の承認）/ G-Deliverable（成果物の確認）/ G-Publish（公開）

## 参照順
1. core/kernel.yaml（作品の背骨）
2. core/bible/（設定正本）・core/state/（オントロジー: entities / timeline / foreshadowing / knowledge_state）
3. work.manifest.json（overlay 選択・逸脱宣言）
4. 用語に迷ったら: {{lab_path}}/proposal/2026-04-30-zero-base-v4/02_domain_model.md（56語 Card）

## 作業の入口
/pitch → /draft → /critic → /continuity → /review-meeting → /release → /retro-meeting
```

`AGENTS.md` は 2行のポインタのみ: 「本作品の運用契約は .claude/CLAUDE.md を参照。skills / agents / rules も .claude/ 配下にある。」

## 5. Lab 側 `.claude/skills/`（Phase 2）

| skill | 元 | 内容 |
|---|---|---|
| new-proposal | 新規 | `proposal/{YYYY-MM-DD}-{slug}/` の雛形生成（PROPOSAL.md + status 行を proposal/README.md に追記） |
| improve-from-work | prompts/01 | 実走作品の learning から current/ への昇格候補を抽出 |
| audit-gaps | prompts/02 | COVERAGE / INHERITANCE の未完項目を点検 |
| extract-pattern | prompts/03 | 作品側の工夫を generic pattern 化 |
| apply-to-work | prompts/04 | current/ の更新を既存 work に適用提案 |
| consistency-check | prompts/05 | current/ 内の相互参照・用語整合チェック（56語 Card 準拠） |
| ontology-check | tools/ | `tools/ontology_check.py` を実行し warning を要約 |

`current/prompts/` は supersede stub 化（正本 = ルート `.claude/skills/`）。ただし prompts/00_session_start.md は Lab CLAUDE.md に吸収。

## 6. bootstrap 追記（work_init/new-work-bootstrap.md）

Step 追加: 「`current/template/core/.claude/` を作品ルート直下 `.claude/` に複製し、CLAUDE.md の {{placeholder}}（work_title / lab_path 等）を埋める。AGENTS.md はそのまま置く。」
