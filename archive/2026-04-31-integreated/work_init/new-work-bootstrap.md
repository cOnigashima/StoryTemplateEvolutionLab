# New Work Bootstrap — 新規作品の立ち上げ手順（v4）

> **役割**: 新規 work を作って DoR-A 通過まで持っていく step-by-step。
> **依存**: `02_domain_model.md` `03_storage_trinity.md` `06_bible_dor.md` を読了済み前提。
> **所要時間**: 30 分（手作業のみ）+ Intake Adapter 実行時間（raw 量に依存、典型 30 分-2 時間）

---

## 0. 前提

実行前に決まっているべきこと:

```
□ 作品 slug（kebab-case、例: "ia-society"）
□ 作品の logline（1-2 文、tentative でも可）
□ 公開予定プラットフォーム（kakuyomu / 自家サイト / 非公開）
□ 既存資料の有無（企画 chat / 設計メモ / 旧 bible package）
```

決まっていなくても進められるが、後で書き戻し作業が増える。

---

## 1. Step 1: ディレクトリ作成

`works/{slug}/` の下に v4 構造を作る。

### 1.1 work root と必須ファイル

```bash
SLUG="your-work-slug"
cd works/
mkdir -p ${SLUG}
cd ${SLUG}
```

### 1.2 トップレベル文書

```bash
# CLAUDE.md と README.md は手で書く
# StoryTemplateEvolution/current/templates/work/CLAUDE.template.md
# StoryTemplateEvolution/current/templates/work/README.template.md
# を copy して作品名と slug を埋める
```

### 1.3 v4 標準ディレクトリ群（一括作成）

```bash
mkdir -p inbox/{planning_sessions,fragments}
# inbox README を copy
cp ../../StoryTemplateEvolution/current/templates/inbox/README.template.md inbox/README.md
mkdir -p adapter
mkdir -p synthesis/{session_digests,update_proposals}

mkdir -p story/seeds
mkdir -p bible/{world,characters,system,timeline,samples,walkthroughs}
mkdir -p design/canon-patch-proposals
mkdir -p state

mkdir -p arcs
mkdir -p packets/{exploring,scoped,frozen}
mkdir -p scenes/{seed,slotted,superseded}

mkdir -p drafts/episodes
mkdir -p reviews/{contracts,audits,templates}
mkdir -p approved/episodes
mkdir -p published/episodes

mkdir -p backlog
mkdir -p learning
mkdir -p community
mkdir -p campaigns

mkdir -p .claude/{rules,agents,skills}
```

### 1.4 各ディレクトリの README.md

各サブディレクトリに README.md を置く（StoryTemplate 共通の `current/templates/{dir}/README.template.md` から copy）:

```bash
# 必須 README（既存 templates から copy）
cp ../../StoryTemplateEvolution/current/templates/bible/README.template.md  bible/README.md
cp ../../StoryTemplateEvolution/current/templates/design/README.template.md design/README.md
cp ../../StoryTemplateEvolution/current/templates/state/README.template.md  state/README.md
cp ../../StoryTemplateEvolution/current/templates/arcs/README.template.md   arcs/README.md
cp ../../StoryTemplateEvolution/current/templates/packets/README.template.md packets/README.md
```

### 1.5 .claude/ 配下の継承

Story Template 共通の rules / agents / skills を一括 copy（v4 では `templates/.claude/` から）:

```bash
mkdir -p .claude
cp -r ../../StoryTemplateEvolution/current/templates/.claude/rules    .claude/
cp -r ../../StoryTemplateEvolution/current/templates/.claude/agents   .claude/
cp -r ../../StoryTemplateEvolution/current/templates/.claude/skills   .claude/
cp ../../StoryTemplateEvolution/current/templates/.claude/settings.template.json .claude/settings.json
# settings.json の "project_name" / "project_description" を作品 slug で書き換え
```

これにより各 work が以下を持つ:
- `.claude/rules/` 5 本: drafter-preflight / file-growth / kakuyomu-policy / learning-capture / story-os-boundaries
- `.claude/agents/` 18 本: plotter / drafter / critic / continuity-checker / 他
- `.claude/skills/` 7 本: pitch / draft / critic / continuity / release / 他
- `.claude/settings.json`

**copy 後の作品固有 refactor は自由**（generic 雛形は出発点、各 work で成長させる）。

### 1.6 verify

```bash
# DoR-A 1.1 の 35 項目が揃っているか確認
ls -la
# → bible/, design/, state/, arcs/, packets/, scenes/, drafts/, reviews/,
#   approved/, published/, backlog/, learning/, inbox/, adapter/, synthesis/,
#   story/, .claude/ が見えること
```

---

## 2. Step 2: kernel.yaml の初期化

```bash
cp ../../StoryTemplateEvolution/current/templates/story/kernel.template.yaml story/kernel.yaml
```

`story/kernel.yaml` を編集:

1. `work_id` に slug を入れる
2. `last_updated` に今日の日付
3. **必須**: `logline.value` に決まっている範囲で書く（tentative 可）
4. **最低限**: `promise.items` に 3 項目（少なくとも 1 つは tentative or filled、他は missing でも可）
5. それ以外は `missing` のまま開始

完全に埋める必要はない。Intake Adapter が raw を読んで tentative / filled に昇格させていく。

---

## 3. Step 3: bible 雛形の copy

Bible facet の雛形を 17 個 copy（必要時のみで OK、最低限は MUST 8 個）:

### MUST 8 個（必ず copy）

```bash
cp ../../StoryTemplateEvolution/current/templates/bible/logline.template.md       bible/logline.md
cp ../../StoryTemplateEvolution/current/templates/bible/promise.template.md       bible/promise.md
cp ../../StoryTemplateEvolution/current/templates/bible/theme.template.md         bible/theme.md
cp ../../StoryTemplateEvolution/current/templates/bible/rules.template.md         bible/rules.md
cp ../../StoryTemplateEvolution/current/templates/bible/style-voice.template.md   bible/style-voice.md
cp ../../StoryTemplateEvolution/current/templates/bible/plot.template.md          bible/plot.md
cp ../../StoryTemplateEvolution/current/templates/bible/world/overview.template.md bible/world/overview.md
# bible/characters/ は作品固有なのでテンプレなし、character-individual.template.md を必要数 copy
```

### SHOULD 8 個（必要時 copy）

```bash
cp ../../StoryTemplateEvolution/current/templates/bible/cadence-plan.template.md   bible/cadence-plan.md
cp ../../StoryTemplateEvolution/current/templates/bible/foreshadowing-map.template.md bible/foreshadowing-map.md
cp ../../StoryTemplateEvolution/current/templates/bible/reveal-plan.template.md    bible/reveal-plan.md
cp ../../StoryTemplateEvolution/current/templates/bible/motif-ladder.template.md   bible/motif-ladder.md
cp ../../StoryTemplateEvolution/current/templates/bible/timeline/history.template.md bible/timeline/history.md
cp ../../StoryTemplateEvolution/current/templates/bible/system/institutions.template.md bible/system/institutions.md
cp ../../StoryTemplateEvolution/current/templates/bible/samples/sample-scene.template.md bible/samples/sample-scene-001.md
```

該当しない facet は **`not_applicable` 明示**（`design/open-questions.md` に理由付きで append）。

### MAY（任意）

```bash
# 必要時のみ
cp ../../StoryTemplateEvolution/current/templates/bible/genre-overlay.template.md  bible/genre-overlay.md
cp ../../StoryTemplateEvolution/current/templates/bible/project-override.template.md bible/project-override.md
```

---

## 4. Step 4: design / state 初期化

design / state の **空ファイル**を作成（DoR-A 1.4 / 1.5 で必須）:

```bash
touch design/open-questions.md
touch design/design-debt.yaml
touch design/rejected-ideas.md

touch state/decision-log.yaml
touch state/contradiction-log.yaml
touch state/canon-patch-log.yaml
touch state/timeline-state.yaml
touch state/character-states.yaml
```

各ファイルの先頭に YAML / Markdown の最小ヘッダを書く（後で `kernel-fill-review.md` 等が format 検査する）:

```yaml
# state/decision-log.yaml
entries: []
```

```markdown
# design/open-questions.md
（空。新規作品立ち上げ時、Open Question なし）
```

---

## 5. Step 5: arcs / packets / scenes の最小成立

```bash
# arcs/series-overview.md は手で書く（最低 manuscript 構造概要 3 行）
touch arcs/series-overview.md
touch arcs/manuscript-plan.md  # 制作ロードマップ

# arcs/arc-01.md（scoped 状態で開始）
touch arcs/arc-01.md
# → 「最初の Arc」の中核問い + 主反転 + 含む Packet 一覧（最低 1 つ）

# packets/scoped/packet-001-{slug}.yaml（scoped 状態）
touch packets/scoped/packet-001-{slug}.yaml

# scenes/seed/scene-template.md
cp ../../StoryTemplateEvolution/current/templates/scenes/scene-template.md scenes/seed/scene-template.md
```

---

## 6. Step 6: 初回 Intake（raw がある場合）

既存資料があるなら inbox に配置 → Intake Adapter 実行。

### 6.1 raw を inbox に配置

```bash
# 企画 chat / 既存設計メモ等を inbox に保存（原文ママ）
cp /path/to/your/planning-chat.md inbox/planning_sessions/2026-04-30_initial.md
```

### 6.2 Intake Adapter 実行

```
LLM に以下を渡す:
1. StoryTemplateEvolution/current/adapter/intake_adapter_prompt.md
2. proposal/2026-04-30-zero-base-v4/02_domain_model.md
3. proposal/2026-04-30-zero-base-v4/05_intake_coverage_checklist.md
4. proposal/2026-04-30-zero-base-v4/06_bible_dor.md
5. inbox/planning_sessions/2026-04-30_initial.md（raw）
6. story/kernel.yaml と bible/* の現状（空でも）

出力:
- synthesis/session_digests/2026-04-30_initial.md
- synthesis/update_proposals/2026-04-30_*_proposal.md（facet 別）
```

### 6.3 出力の検証

```
LLM に以下を渡す:
1. proposal/2026-04-30-zero-base-v4/07_review_prompts/intake-digest-review.md
2. synthesis/session_digests/2026-04-30_initial.md
3. inbox/planning_sessions/2026-04-30_initial.md
```

抽出漏れ / 幻覚 / status 妥当性 / 出典 trace を検査。pass: false なら Adapter を再実行。

### 6.4 Author Approval

`synthesis/update_proposals/` の各 facet proposal を author が承認 / 修正 / 却下。

```
LLM に以下を渡す:
1. proposal/2026-04-30-zero-base-v4/07_review_prompts/update-proposal-review.md
2. synthesis/update_proposals/{facet}_proposal.md
```

承認された proposal を bible/design/state に反映（手作業 or Adapter の apply 機能）。

---

## 7. Step 7: 初回 DoR-A 検証

```
LLM に以下を渡す:
1. proposal/2026-04-30-zero-base-v4/07_review_prompts/bible-readiness-review.md
2. proposal/2026-04-30-zero-base-v4/06_bible_dor.md
3. work_root のスキャン結果（ls -laR の出力）
4. story/kernel.yaml の中身
5. bible/ design/ state/ の主要ファイル
```

`bible_readiness_review` の `dor_a_pass` が true になるまで以下を繰り返す:

1. `blockers.critical` を解消
2. 必要なら Intake Adapter 再実行（追加 raw or facet 補完）
3. 再 review

---

## 8. Step 8: 完了確認

DoR-A 通過 = bootstrap 完了。次の作業に進む:

- **arcs/arc-01.md を scoped 状態に**
- **packets/scoped/packet-001 を scoped → frozen に進める**（Packet Freeze Review = DoR-C）
- **frozen packet 内の最初の episode の Writing Pack 生成**（Writing Adapter）
- **drafter-preflight + drafting 開始**（DoR-B）

---

## 9. トラブルシューティング

### Q: kernel.yaml の status が大量に missing で進めない

→ tentative で良いので埋める。raw に該当する記述があれば Adapter が自動的に tentative に昇格させる。完全な missing は Intake Adapter で確認後、author 判断で deferred / not_applicable / intentionally_blank に降格できる。

### Q: bible facet が大量に not_applicable になる

→ 短編・中編なら正常。長編で大量 not_applicable は要見直し（System / Timeline / Foreshadowing Map など長編に効く facet が落ちていないか）。

### Q: Intake Adapter が raw に書かれていないことを bible に書こうとする

→ `intake-digest-review.md` で「幻覚」として検出される。Adapter を再実行 + 出力に対して厳しく review。

### Q: 既存 work から v4 に移行したい

→ 本書は新規 bootstrap 用。既存 work の移行は `proposal/2026-04-30-zero-base-v4/08_pilot_validation/` の各 walkthrough と `proposal/2026-04-30-zero-base-v4/10_migration_plan.md` を参照。

---

## 10. 不変条件

1. **CLAUDE.md / README.md なしで bootstrap 完了とみなさない**
2. **kernel.yaml は schema_version: "v4" 必須**
3. **MUST facet 8 個のいずれかが実体不在で DoR-A 通過は不可**
4. **raw を inbox に置かずに直接 bible に書かない**
5. **kernel.yaml と bible/logline.md `bible/promise.md` `bible/style-voice.md` は sync 必須**
6. **作品固有 facet は generic 雛形に流入させない**

---

## 11. 関連参照

- 用語: `proposal/2026-04-30-zero-base-v4/02_domain_model.md`
- 物理構造: `proposal/2026-04-30-zero-base-v4/03_storage_trinity.md`
- フロー: `proposal/2026-04-30-zero-base-v4/04_pipeline_overview.md`
- 網羅項目: `proposal/2026-04-30-zero-base-v4/05_intake_coverage_checklist.md`
- DoR: `proposal/2026-04-30-zero-base-v4/06_bible_dor.md`
- Intake Adapter prompt: `StoryTemplateEvolution/current/adapter/intake_adapter_prompt.md`
- Review prompts: `proposal/2026-04-30-zero-base-v4/07_review_prompts/`
- 既存 work 移行: `proposal/2026-04-30-zero-base-v4/08_pilot_validation/`
