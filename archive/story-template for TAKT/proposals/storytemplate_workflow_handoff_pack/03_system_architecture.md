# 全体アーキテクチャ

## 基本構造

```text
Knowledge Layer
  ↓
Framework Index
  ↓
StoryTemplate / StoryaTemplate Kernel
  ↓
Project Design
  ↓
Freeform Chat
  ↓
Domain Synthesis
  ↓
Adapter
  ↓
Workflow
  ↓
Production State
  ↓
Retro
```

---

# 1. Knowledge Layer

一般的な創作ノウハウ、物語理論、ジャンル知識、既存フレームワークを置く層。

例。

```text
三幕構成
Snowflake Method
Story Grid
Hero's Journey
Save the Cat 系
ジャンル別テンプレート
シーン設計理論
キャラクターアーク理論
編集・レビュー手法
```

注意。

```text
Knowledge Layer の情報は、そのまま作品制約にしない。
```

---

# 2. Framework Index

既存フレームワークを「いつ使うか」「何を見るか」「何を見えにくくするか」で整理するカタログ。

目的。

```text
最強テンプレートを作るのではなく、
その時点の問題に合う lens を選ぶ
```

記録する情報。

```text
best_for
not_good_for
use_as
adapter_outputs
risks
when_to_apply
when_not_to_apply
related_workflow
```

---

# 3. StoryTemplate / StoryaTemplate Kernel

物語設計の薄い中核。

厚くしすぎない。

最小項目案。

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

---

# 4. Project Design

この作品で採用された設計。

例。

```text
作品のpremise
ジャンル方針
作品固有の美学
キャラ設定
世界観
文体方針
読者への約束
テーマ
```

これは Knowledge Layer より強い制約。

---

# 5. Freeform Chat

自由な企画・設計・議論の場。

重要。

```text
ここでは最初からテンプレート穴埋めにしない。
発想の自由度を保つ。
```

ただし、チャット終了時に Domain Synthesis で構造化する。

---

# 6. Domain Synthesis

自由なチャットを整理する層。

出力。

```text
confirmed_design
tentative_design
open_questions
contradictions
author_decisions_needed
story_template_mapping
framework_lens_candidates
workflow_ready_status
```

役割。

```text
自由な議論を失わず、次の制作入力へ渡せる形にする
```

---

# 7. Adapter

もっとも重要な接合層。

入力。

```text
Domain Synthesis
StoryTemplate
Framework Lens
Project Design
Ledger
```

出力。

```text
scene_card
acceptance_contract
judge_contract
review_checklist
ledger_update_targets
packet_map
arc_map
```

Adapter の役割。

```text
設計情報を、writer / reviewer / judge が扱える小さな入力に変換する
```

---

# 8. Workflow

実際に作業を回す層。

主な workflow。

```text
episode-draft-tournament
packet-assembly-review
arc-through-review
arc-strategy-tournament
part-through-review
```

TAKT はここを実行する基盤として使う。

---

# 9. Production State

実際に制作が進む中で生まれる状態。

```text
draft
candidate
selection report
review report
judge report
ledger update
soft lock
hard lock
```

ここで ledger が重要になる。

---

# 10. Retro

振り返りの層。

見るもの。

```text
StoryTemplate は役に立ったか
Framework Lens は効いたか
Adapter は正しく変換したか
writer 候補に差が出たか
selection は妥当だったか
judge は止めすぎなかったか
ledger は次回に役立ったか
```

Retro がないと、テンプレート・レビュー・プロンプトが肥大化する。

---

# 情報の3層分離

大量の情報を制御するために、以下を分ける。

## Knowledge

一般ノウハウ。

```text
創作理論
既存テンプレート
ジャンル知識
```

拘束力は弱い。

## Project Design

この作品で採用した設計。

```text
作品方針
bible
style guide
project-specific rule
```

拘束力は中〜強。

## Production State

本文で確定した状態。

```text
ledger
draft
judge result
author decision
```

拘束力は強い。

---

# やってはいけない混同

```text
一般ノウハウを作品制約にしてしまう
没案を canon にしてしまう
Project Design と Production State を混ぜる
StoryTemplate の項目不足を必ず欠陥扱いする
Ledger に何でも入れて肥大化させる
```

---

# 推奨アーキテクチャの一文要約

```text
StoryTemplate は考える箱、
Adapter は制作入力への変換器、
Workflow は実行ライン、
Judge は品質ゲート、
Ledger は状態台帳、
Retro は改善機構。
```
