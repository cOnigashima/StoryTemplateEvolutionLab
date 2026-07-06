# 新規作品 Bootstrap 手順

> StoryTemplateEvolution の templates/ から新規作品を init する step-by-step。
> renji pilot から抽象化（2026-04-29）。

---

## 前提

- StoryTemplateEvolution が `write_read_novel_manufacture/StoryTemplateEvolution/` に存在
- 新規作品の置き場が決まっている（推奨: `Works/{slug}/` または `works/{slug}/`）
- 旧 `story-template/.claude/rules/` 5 本を継承する

---

## Step 1. ディレクトリ作成

```bash
WORK_SLUG="..."   # 例: "my_novel"
WORK_PATH="path/to/Works/${WORK_SLUG}"

mkdir -p "${WORK_PATH}"/{
  inbox/planning_sessions,
  synthesis/{session_digests,update_proposals},
  story/{seeds,canon-patch-proposals},
  bible/{characters/individual,world,plot,in_world_documents},
  design,
  state,
  arcs,
  packets/{exploring,scoped,frozen},
  scenes/{seed,slotted},
  writing/episode_packs,
  drafts/episodes,
  reviews/contracts,
  approved,
  published,
  learning
}
mkdir -p "${WORK_PATH}/.claude/agents"
mkdir -p "${WORK_PATH}/.adapter"
```

---

## Step 2. .claude/rules/ 継承

旧 story-template の 5 ルールをコピー:

```bash
TEMPLATE_RULES="<旧 story-template>/.claude/rules"

cp "${TEMPLATE_RULES}/learning-capture.md" "${WORK_PATH}/.claude/rules/"
cp "${TEMPLATE_RULES}/drafter-preflight.md" "${WORK_PATH}/.claude/rules/"
cp "${TEMPLATE_RULES}/file-growth.md" "${WORK_PATH}/.claude/rules/"
cp "${TEMPLATE_RULES}/kakuyomu-policy.md" "${WORK_PATH}/.claude/rules/"
cp "${TEMPLATE_RULES}/story-os-boundaries.md" "${WORK_PATH}/.claude/rules/"
```

新規ルール（StoryTemplateEvolution/rules/）も追加:

```bash
EVOLUTION_RULES="<path>/StoryTemplateEvolution/rules"

cp "${EVOLUTION_RULES}/intake-flow.md" "${WORK_PATH}/.claude/rules/"
```

---

## Step 3. .adapter/ コピー

```bash
EVOLUTION_ADAPTER="<path>/StoryTemplateEvolution/adapter"

cp "${EVOLUTION_ADAPTER}"/*.md "${WORK_PATH}/.adapter/"
cp "${EVOLUTION_ADAPTER}"/*.yaml "${WORK_PATH}/.adapter/"
```

これで作品の `.adapter/` に Intake / Writing Adapter 設計が揃う。

---

## Step 4. CLAUDE.md 作成

```bash
touch "${WORK_PATH}/CLAUDE.md"
```

内容: 旧 story-template の CLAUDE.md を母体に、作品固有情報を埋める。

---

## Step 5. inbox/ に初期素材を配置

企画チャット / 既存資料 / メモを `${WORK_PATH}/inbox/planning_sessions/` に置く。

```bash
cp <既存資料> "${WORK_PATH}/inbox/planning_sessions/"
```

---

## Step 6. Intake Adapter 実行

`.adapter/intake_adapter_prompt.md` の手順で Intake Adapter Editor を起動。

入力: `${WORK_PATH}/inbox/planning_sessions/` の素材

出力:
- `${WORK_PATH}/synthesis/session_digests/{date}_{slug}.md`
- `${WORK_PATH}/synthesis/update_proposals/{date}_{target}_proposal.md`

---

## Step 7. Human Approval

author が update_proposal を読み、approve / partial / revise / reject を判断。

---

## Step 8. bible/design/state 反映

承認分のみを以下に反映:

### bible 反映時の templates 利用

```bash
EVOLUTION_TEMPLATES="<path>/StoryTemplateEvolution/templates"

# 必要な template をコピーして埋める
cp "${EVOLUTION_TEMPLATES}/bible/premise.template.md" "${WORK_PATH}/bible/premise.md"
cp "${EVOLUTION_TEMPLATES}/bible/reader_promise.template.md" "${WORK_PATH}/bible/reader_promise.md"
cp "${EVOLUTION_TEMPLATES}/bible/theme.template.md" "${WORK_PATH}/bible/theme.md"
cp "${EVOLUTION_TEMPLATES}/bible/genre.template.md" "${WORK_PATH}/bible/genre.md"
cp "${EVOLUTION_TEMPLATES}/bible/style_guide.template.md" "${WORK_PATH}/bible/style_guide.md"
# ... 必要な分を継続
```

template の `<!-- ... -->` ヒントに従って中身を埋める。承認済 update_proposal の内容を投入。

### design 反映

```bash
cp "${EVOLUTION_TEMPLATES}/design/project_principles.template.md" "${WORK_PATH}/design/project_principles.md"
cp "${EVOLUTION_TEMPLATES}/design/critical_intent.template.md" "${WORK_PATH}/design/critical_intent.md"
cp "${EVOLUTION_TEMPLATES}/design/editorial_notes.template.md" "${WORK_PATH}/design/editorial_notes.md"
cp "${EVOLUTION_TEMPLATES}/design/checklists.template.md" "${WORK_PATH}/design/checklists.md"
```

### state 初期化

```bash
cp "${EVOLUTION_TEMPLATES}/state/timeline.template.yaml" "${WORK_PATH}/state/timeline.yaml"
cp "${EVOLUTION_TEMPLATES}/state/character_states.template.yaml" "${WORK_PATH}/state/character_states.yaml"
cp "${EVOLUTION_TEMPLATES}/state/foreshadowing.template.yaml" "${WORK_PATH}/state/foreshadowing.yaml"
cp "${EVOLUTION_TEMPLATES}/state/rejected_ideas.template.md" "${WORK_PATH}/state/rejected_ideas.md"
```

state は **空 or seed のみ** の状態で OK。執筆中に ledger-keeper が更新。

---

## Step 9. story/kernel.yaml の作成

`StoryTemplateEvolution/docs/kernel_spec.md` のスキーマで kernel.yaml を作る:

```bash
touch "${WORK_PATH}/story/kernel.yaml"
```

11 項目を埋める。`StoryTemplateEvolution/docs/kernel_spec.md` の判定基準を参照。

---

## Step 10. DoR-A チェック

`StoryTemplateEvolution/docs/dor_dod.md` §DoR-A のチェックリストを通す。

全 ✓ で「Episode draft フェーズに入れる」状態。

---

## Step 11. arc-1 / packet-001 の最小設計

```bash
cp "${EVOLUTION_TEMPLATES}/bible/plot/arc_map.template.md" "${WORK_PATH}/bible/plot/arc_map.md"
cp "${EVOLUTION_TEMPLATES}/bible/plot/episode_plan.template.md" "${WORK_PATH}/bible/plot/episode_plan.md"
cp "${EVOLUTION_TEMPLATES}/bible/plot/scene_cards.template.md" "${WORK_PATH}/bible/plot/scene_cards.md"
```

arc-1 と packet-001 の最低限を埋める（少なくとも ep001 を draft できる程度）。

---

## Step 12. ep001 Writing Pack 生成

Writing Adapter（`.adapter/writing_adapter_prompt.md`）を実行:

```bash
mkdir -p "${WORK_PATH}/writing/episode_packs/ep001"

cp "${EVOLUTION_TEMPLATES}/writing/episode_pack/episode_brief.template.md" \
   "${WORK_PATH}/writing/episode_packs/ep001/episode_brief.md"
cp "${EVOLUTION_TEMPLATES}/writing/episode_pack/scene_card.template.md" \
   "${WORK_PATH}/writing/episode_packs/ep001/scene_card.md"
cp "${EVOLUTION_TEMPLATES}/writing/episode_pack/context_pack.template.md" \
   "${WORK_PATH}/writing/episode_packs/ep001/context_pack.md"
cp "${EVOLUTION_TEMPLATES}/writing/episode_pack/acceptance_checklist.template.md" \
   "${WORK_PATH}/writing/episode_packs/ep001/acceptance_checklist.md"
```

各 template を埋める。ep001 用に bible/state から必要情報を抽出して投入。

---

## Step 13. DoR-B チェック

`StoryTemplateEvolution/docs/dor_dod.md` §DoR-B のチェックリストを通す。

全 ✓ で drafter は prose を書き始められる。

---

## Step 14. 執筆開始

drafter（人 or AI）が ep001 の prose を書く。完了したら DoD-E チェック → 公開検討。

---

## bootstrap 完了の DoD

```
□ work directory が存在
□ .claude/rules/ + .adapter/ コピー済
□ inbox/ + synthesis/ + bible/ + design/ + state/ + writing/ ディレクトリあり
□ kernel.yaml 11 項目すべて filled or 適切 status
□ DoR-A 全 ✓
□ ep001 Writing Pack 4 ファイル揃い
□ DoR-B 全 ✓
□ author 確認
```

---

## renji の実例

renji は本手順を **逆順で実行**（既存資料を ingest した）した:

1. renji_novel_bible/ の 35 既存ファイルを inbox 相当に置いた
2. .adapter/ を直接作った（template 化前）
3. ep001 Writing Pack を直接作った（bible 実体化前）
4. その後で bible/design/state を実体化（Phase A）

新規作品では Step 1〜14 の順序で進めるのが推奨。

renji の bootstrap 例: `../../story-template for TAKT/works/renji/`
