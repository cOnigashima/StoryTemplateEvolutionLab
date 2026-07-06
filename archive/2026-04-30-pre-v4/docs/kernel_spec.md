# Kernel 仕様（薄い 11 項目）

> 1 作品 1 ファイル: `story/kernel.yaml`
> これ以上に項目を増やさない。増やしたい項目は overlay / lens / bible / craft に出す。
> 詳細は v3 `04_kernel_spec.md`。

---

## kernel.yaml 全体構造

```yaml
kernel:
  schema_version: "v3"
  work_id: ""
  last_updated: "YYYY-MM-DD"
  
  # 1
  premise:
    value: ""
    status: filled | tentative | needs_author_decision
  
  # 2
  promise:
    items:
      - id: "p1"
        claim: ""
        status: ""
        evidence_target: ""    # どの packet/arc で実装するか
  
  # 3
  protagonist_vector:
    primary_protagonist:
      character_id: ""
      want: { value: "", status: "" }
      need: { value: "", status: "" }
      wound_or_misbelief: { value: "", status: "" }
  
  # 4
  conflict:
    external: { value: "", status: "" }
    internal: { value: "", status: "" }
    relational: { value: "", status: "" }
  
  # 5
  stakes:
    if_protagonist_fails: ""
    if_protagonist_succeeds_but_pays: ""
    why_reader_cares: ""
    status: ""
  
  # 6
  change_model:
    arc_shape: growth | fall | flat | circular | mixed
    direction_of_change: ""
    end_state_relative_to_start: ""
    status: ""
  
  # 7
  causality:
    time_order_policy: linear | nonlinear | multi_pov | flashback_heavy
    knowledge_state_monotonicity: strict | relaxed | per_pov
    rationalization_vocabulary_policy: avoid | allowed_with_check
    status: ""
  
  # 8
  information_design:
    must_be_clear: [""]
    intended_unknowns:
      - id: ""
        claim: ""
        intended_reveal_unit: episode | packet | arc | part | manuscript
        intended_reveal_id: ""
    disclose_policy: ""
    withhold_policy: ""
    status: ""
  
  # 9
  emotional_arc:
    overall_curve: ""
    target_reader_emotion_at_end: ""
    cadence_baseline:
      tension_to_release_ratio: "6:4"
    status: ""
  
  # 10
  style_voice:
    pov: first_person | third_person_limited | third_person_omniscient | epistolary | mixed
    tense: present | past | mixed
    register: literary | conversational | rough | formal | mixed
    sentence_length_baseline: short | medium | long | varied
    narrative_temperature: cold | neutral | warm | hot
    forbidden_words: []
    style_references: []
    status: ""
  
  # 11
  unit_tree:
    has_part: true | false
    planned_part_count: 0
    planned_arc_count_per_part: 0
    planned_packet_count_per_arc: 0
    planned_episode_count_per_packet: 0
    target_total_episodes: 0
    serial_or_complete: serial | complete
    status: ""
```

---

## 必須度サマリ

| 項目 | 必須度 |
|---|---|
| premise | MUST |
| promise（最低 3 項目） | MUST |
| protagonist_vector.want | MUST |
| protagonist_vector.need | MUST |
| protagonist_vector.wound | SHOULD |
| conflict（最低 1 軸） | MUST |
| stakes | MUST |
| change_model | MUST |
| causality | MUST |
| information_design.must_be_clear | MUST |
| information_design.intended_unknowns | SHOULD |
| emotional_arc | MUST |
| style_voice.pov | MUST |
| style_voice.tense | MUST |
| style_voice.register | SHOULD |
| unit_tree | MUST |

MUST 全 ✓ かつ contradiction / needs_author_decision なしで DoR-A 満足。

---

## kernel に「入れない」もの

- bible 詳細（characters / world / rules）
- genre_overlay
- project_override
- packet 詳細
- episode 詳細
- scene_card / acceptance_contract
- foreshadowing_map / reveal_plan / cadence_plan
- ledger（実装中の状態）
- review / rubric / craft / framework

---

## 判定基準（新フィールドが提案されたら）

```
Q1. このフィールド無しに執筆を 1 文字も始められないか?
  Yes → kernel 候補
  No  → bible / overlay / lens / craft / state / design

Q2. 作品ジャンル不問で必要か?
  Yes → kernel 候補
  No  → genre_overlay or framework_lens

Q3. 作品固有の例外・美学か?
  Yes → project_override
  No  → 他

Q4. 制作中に発生する状態か?
  Yes → state (ledger)
  No  → 他

Q5. レビュー時の判定軸か?
  Yes → rubric / craft
  No  → 他
```

---

## サンプル

renji の実例: `../../story-template for TAKT/works/renji/bible/` (本セッション後に realized)
