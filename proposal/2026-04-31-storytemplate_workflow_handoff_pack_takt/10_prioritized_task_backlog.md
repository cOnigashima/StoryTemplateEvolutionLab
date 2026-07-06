# 優先タスクリスト

## P0: すぐ取り掛かるべきこと

### P0-01. 既存StoryTemplateの棚卸し

目的。

```text
既存StoryTemplateの項目を把握し、どの層に属するか分類する
```

成果物。

```text
existing_storytemplate_inventory.md
storytemplate_field_mapping.yaml
```

---

### P0-02. 用語・階層を仮確定する

確定案。

```text
Episode = 1話
Packet = 章束
Arc = 部内中規模単位
Part = 第一部・第二部
Draft = 状態名
Chapter = 内部用語としては使わない
```

成果物。

```text
unit_taxonomy.md
```

---

### P0-03. StoryTemplate Kernel v0 を作る

既存StoryTemplateから、汎用kernelとして残す項目を抽出する。

候補。

```text
premise
reader promise
protagonist vector
conflict
stakes
change model
causality
information design
emotional arc
style / voice
unit tree
```

成果物。

```text
storytemplate_kernel_v0.md
storytemplate_kernel.schema.yaml
```

---

### P0-04. Domain Synthesis Prompt v0 を作る

自由なチャットを構造化する prompt。

出力。

```text
confirmed_design
tentative_design
open_questions
contradictions
author_decisions_needed
storytemplate_mapping
framework_lens_candidates
workflow_ready_status
```

成果物。

```text
domain_synthesis_prompt.md
```

---

### P0-05. Framework Index Card schema を作る

調査結果を制御するためのカード形式。

成果物。

```text
framework_index_card.schema.yaml
```

---

### P0-06. Framework Index v0 を作る

最初は少数でよい。

```text
Premise / Logline Lens
Three-act Lens
Snowflake-like Expansion Lens
Story Grid-like Scene Diagnosis Lens
Genre Overlay Lens
Voice / Literary Lens
```

成果物。

```text
framework_index_v0.md
```

---

### P0-07. Adapter v0 を作る

StoryTemplate / Domain Synthesis / Framework Lens から workflow input へ変換する。

成果物。

```text
storytemplate_adapter.md
adapter_mapping_rules.yaml
```

---

### P0-08. Scene Card schema を作る

Episode執筆用の入力。

成果物。

```text
scene_card.schema.yaml
```

---

### P0-09. Episode Acceptance Contract schema を作る

judge用の合格基準。

成果物。

```text
episode_acceptance_contract.schema.yaml
```

---

### P0-10. episode-draft-tournament v0 を作る

最初は最小構成。

```text
faithful writer
emotional writer
plot-drive writer
selection-synthesis
integrated reviser
episode judge
ledger keeper
```

成果物。

```text
episode_draft_tournament.workflow.md
writer_prompts/
selection_synthesis_prompt.md
episode_judge_prompt.md
ledger_keeper_prompt.md
```

---

### P0-11. Ledger minimal schema を作る

成果物。

```text
ledger.schema.yaml
```

---

### P0-12. Pilot Episode を1本選ぶ

条件。

```text
重要すぎない
感情・情報開示・次への引きがある
ledger更新が少し発生する
真相開示の制御が必要
```

成果物。

```text
pilot_episode_pack/
```

---

### P0-13. Retro Protocol v0 を作る

Pilot後に何を見るかを決める。

成果物。

```text
retro_protocol.md
```

---

## P1: Pilot 後にやること

### P1-01. Writer persona を増やす

追加候補。

```text
dialogue writer
risky writer
```

---

### P1-02. Candidate Diversity Judge を作る

候補ドラフトが似すぎる問題を検出する。

---

### P1-03. Packet workflow を作る

```text
packet-assembly-review
packet-unit-tests
packet-synthesis
packet-judge
```

---

### P1-04. Unit Test Suite を整える

```text
ContinuityTest
CausalityTest
CharacterKnowledgeTest
CanonCoverageTest
ExpositionBalanceTest
StyleDialogueRhythmTest
RedundancyTest
ForeshadowingTest
```

---

### P1-05. Human-in-the-loop policy を作る

人間の介入条件を定義する。

---

### P1-06. Style Guide schema を作る

文体・視点・セリフ・声を管理する。

---

### P1-07. Framework Index を対象作品向けに拡張する

必要なジャンルだけ追加。

---

## P2: しばらく後でよいこと

```text
arc-through-review workflow
arc-strategy-tournament workflow
part-through-review workflow
genre overlay library
full manuscript review
TAKT full implementation
```

---

## P3: 今やらないこと

```text
全創作理論のdeep research
最強StoryTemplate完全版
全ジャンル対応
1000タスクの完全整理
全workflowのTAKT実装
全レビューの完全自動化
精密スコアリング体系
```

---

# 最短実行ルート

```text
1. 既存StoryTemplateを棚卸しする
2. Kernel / Overlay / Override / Workflow Input に分類する
3. Domain Synthesis Prompt v0 を作る
4. Adapter v0 を作る
5. 1 Episode 用の scene_card / contract を生成する
6. episode-draft-tournament を最小構成で回す
7. Retro で改善する
```
