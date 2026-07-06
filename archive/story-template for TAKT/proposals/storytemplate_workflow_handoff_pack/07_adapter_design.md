# Adapter 設計

## Adapter とは

Adapter は、自由な企画・設計チャットや StoryTemplate の情報を、実際の執筆 workflow が使える入力に変換する層。

```text
Freeform Chat
StoryTemplate
Framework Lens
Project Design
Ledger
  ↓
Adapter
  ↓
scene_card
acceptance_contract
judge_contract
review_checklist
ledger_update_targets
```

---

# なぜ Adapter が必要か

## 1. 自由な設計チャットを壊さないため

最初からテンプレート穴埋めにすると、発想が小さくなる。

## 2. StoryTemplate 全体を writer に渡すと重すぎるため

writer には、今の Episode に必要な情報だけ渡す。

## 3. Judge には contract が必要なため

judge は「面白いか」ではなく「合意基準を満たすか」を見る。

## 4. Ledger 更新には状態管理が必要なため

本文で確定した事実と、設計上の仮説を分ける。

---

# Adapter の入力

```text
domain_synthesis
existing_storytemplate_mapping
storya_kernel
framework_lens_selection
project_design
current_ledger
target_unit
```

---

# Adapter の出力

## 1. scene_card

writer に渡す。

```text
episode_id
purpose
entry_state
exit_state
must_include
must_not_include
intended_unknowns
must_be_clear
reader_target
style_constraints
dependencies
```

## 2. acceptance_contract

judge に渡す。

```text
must_satisfy
must_not_violate
intended_unknowns
acceptable_ambiguity
must_be_clear
quality_bar
auto_fix_allowed
human_required_if
ignore_or_defer
```

## 3. judge_contract

判定ロジック。

```text
PASS
FAIL_AUTO_FIX
NEEDS_HUMAN
REJECT_AND_REGENERATE
```

## 4. review_checklist

reviewer に渡す。

```text
reader experience
continuity
canon coverage
causality
character knowledge
style / dialogue / rhythm
exposition balance
```

## 5. ledger_update_targets

ledger keeper に渡す。

```text
canon_facts
timeline
character_states
foreshadowing
open_questions
author_decisions
rejected_ideas
```

---

# Adapter の処理手順

## Step 1. Domain Synthesis を受け取る

分類。

```text
confirmed
tentative
open_questions
contradictions
author_decisions_needed
```

## Step 2. StoryTemplate に写像する

各項目に status を付ける。

```text
filled
missing
tentative
deferred
intentionally_blank
intentionally_hidden
not_applicable
genre_not_applicable
project_override
contradiction
needs_author_decision
```

## Step 3. Framework Lens を選ぶ

必要なら一時的な lens を適用する。

例。

```text
mystery lens
romance lens
story grid scene lens
snowflake expansion lens
```

## Step 4. Target Unit を決める

```text
Episode
Packet
Arc
Part
```

## Step 5. Workflow Input に変換する

target unit に応じて、scene_card / packet_map / arc_map などを作る。

## Step 6. Risk を出す

```text
missing critical info
contradiction
human decision needed
template overreach
genre mismatch
```

---

# Adapter の重要ルール

## 1. 不明なことを勝手に確定しない

`tentative` や `deferred` を保持する。

## 2. 意図された謎を説明不足として扱わない

`intended_unknowns` と `must_be_clear` を分ける。

## 3. 作品固有ルールを優先する

Project Override は一般テンプレートより強い。

## 4. Writer に渡す情報を絞る

writer に大量の抽象設計を渡しすぎると、本文が硬くなる。

## 5. Judge には明確な contract を渡す

judge に曖昧な美学判断を任せすぎない。

---

# Adapter 出力フォーマット案

```yaml
adapter_output:
  target_unit: "episode"
  target_id: "pt01-ar01-pk01-ep01"

  source_summary:
    from_chat:
      - ""
    from_storytemplate:
      - ""
    from_framework_lens:
      - ""
    from_ledger:
      - ""

  scene_card:
    purpose:
      - ""
    entry_state: {}
    exit_state: {}
    must_include:
      - ""
    must_not_include:
      - ""
    intended_unknowns:
      - ""
    must_be_clear:
      - ""
    reader_target:
      - ""

  acceptance_contract:
    must_satisfy:
      - ""
    must_not_violate:
      - ""
    auto_fix_allowed:
      - ""
    human_required_if:
      - ""

  review_checklist:
    - id: ""
      purpose: ""

  ledger_update_targets:
    - type: ""
      expected_update: ""

  risks:
    - id: ""
      severity: low | medium | high
      claim: ""
      needs_human: false

  workflow_ready:
    status: ready | ready_with_risks | not_ready
    missing:
      - ""
```

---

# Adapter の成功条件

```text
自由なチャットの内容を失わない
StoryTemplateの箱に無理やり押し込めない
writer が書ける scene_card になる
judge が判定できる contract になる
reviewer が見るべき観点が明確になる
ledger keeper が更新対象を理解できる
人間判断が必要な箇所が明示される
```

---

# Adapter の失敗条件

```text
テンプレート穴埋めが目的化する
writer に渡す情報が多すぎる
intended_unknowns が潰れる
human_required が多すぎてAIが止まる
judge が抽象的な好み判定になる
ledger に入れる情報が肥大化する
```
