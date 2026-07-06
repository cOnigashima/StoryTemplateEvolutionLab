# 抽象化されたもの一覧

> 本セッションで renji 実走から StoryTemplateEvolution に抽象化された項目。

---

## 1. ドメイン語彙（docs/）

v3-kernel から継承 + renji 実走で確認:

- 用語表 11 カテゴリ（meta / kernel / 単位 / 設定 / 接合 / レビュー / 状態管理 / ノウハウ / 公開 / 状態値）
- 単位階層（Manuscript / Part / Arc / Packet / Episode / Scene / Beat）
- Layer 4+1.5 マップ
- kernel 11 項目仕様
- 11 status 値
- Judge 4 値 / Lock 5 状態
- DoR 3 段 / DoD 3 段

---

## 2. Adapter 設計（adapter/）

renji の `.adapter/` から汎用化:

- folder_structure.md（bible/design/state/writing 4 層）
- intake_adapter_prompt.md（自由 chat → update_proposal）
- writing_adapter_prompt.md（bible/state → Writing Pack）★ 本セッションで分離
- field_mapping_template.yaml（30+ フィールド → Layer 帰属）
- update_proposal_format.yaml
- writing_pack_format.yaml
- human_approval_policy.md

---

## 3. Bible 構造 template（templates/bible/）

renji bible 11 ファイルから抽象化:

- premise.template.md
- reader_promise.template.md
- theme.template.md
- genre.template.md
- style_guide.template.md
- characters/protagonist.template.md
- characters/individual.template.md
- world/locations.template.md
- plot/arc_map.template.md
- plot/episode_plan.template.md
- plot/scene_cards.template.md
- in_world_documents/samples.template.md

---

## 4. Design 構造 template（templates/design/）

- project_principles.template.md（作劇ルール構造）
- critical_intent.template.md（批評性構造）
- editorial_notes.template.md（レビュー視点）
- checklists.template.md

---

## 5. State 構造 template（templates/state/）

- timeline.template.yaml
- character_states.template.yaml
- foreshadowing.template.yaml
- rejected_ideas.template.md

---

## 6. Writing Pack 構造 template（templates/writing/episode_pack/）

ep001 Writing Pack から:

- episode_brief.template.md
- scene_card.template.md
- context_pack.template.md
- acceptance_checklist.template.md

---

## 7. Checklists（checklists/）

- work_dramatic_principles.template.md（renji 7 ルールから汎用化した「作劇ルール構造」）
- episode_acceptance.template.md
- packet_freeze.template.md

---

## 8. Rules（rules/）

- intake-flow.md（raw を bible に直接流さない）

---

## 9. Work Init（work_init/）

- README.md
- new_work_bootstrap.md（renji bootstrap の逆順を template 化）

---

## 10. Learning / 方法論（learning/）

- 2026-04-29-renji-pilot-retro.md
- 2026-04-29-template-extraction-method.md
- 2026-04-29-handoff-to-next-session.md

---

## 抽象化された原則

実装ファイルではないが、本セッションで確立された原則:

1. **Pilot-driven Template Extraction** — 設計室で先に作らず、実走から抽出
2. **作品固有 / 汎用の境界判断** — 各 1 ファイルごとに「他作品で使うか?」を問う
3. **Adapter 2 分割** — Intake / Writing で機能分離
4. **bible / design / state / writing の 4 層分離**
5. **status 区別の徹底** — 11 値で空欄理由を区別
6. **kernel 薄く / Layer 2/3 厚く**
7. **template と実例の対** — template は「埋めるべき項目」、実例は「埋まったらどう見えるか」
