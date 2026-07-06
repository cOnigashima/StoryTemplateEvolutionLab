# 既存 StoryTemplate 統合ガイド

## 目的

既存の StoryTemplate を捨てずに、ここまで議論した workflow / adapter / judge / ledger と統合する。

重要なのは、既存StoryTemplateを無理に全面改造することではない。  
まずは、既存StoryTemplateがどの役割を担っているかを分解する。

---

# 統合の基本方針

```text
既存StoryTemplate
  ↓
棚卸し
  ↓
項目分類
  ↓
不足・重複・過剰・曖昧さを確認
  ↓
Adapterとの接続点を定義
  ↓
Pilot Episodeで検証
```

---

# 既存StoryTemplateを分類する観点

既存項目を、以下のどれに属するか分類する。

## 1. Universal Kernel

多くの作品で汎用的に使う物語設計の中核。

例。

```text
premise
reader promise
protagonist want / need
conflict
stakes
change
causality
information design
emotional arc
style / voice
```

## 2. Genre Overlay

ジャンル固有の約束・チェックリスト。

例。

```text
ミステリー:
  clue
  red herring
  reveal schedule
  fair play

恋愛:
  attraction
  obstacle
  intimacy progression
  dark moment

スリラー:
  threat
  clock
  escalation
  reversal
```

## 3. Project Override

この作品固有の設計思想・例外・美学。

例。

```text
この作品では説明を遅らせる
主人公の自己理解を信用しない
沈黙と間を重視する
恋愛的解釈を曖昧に保つ
ジャンル約束を一部外す
```

## 4. Workflow Input

執筆ワークフローへ直接渡せる項目。

例。

```text
scene purpose
entry_state
exit_state
must_include
must_not_include
intended_unknowns
must_be_clear
reader_target
```

## 5. Review Checklist

レビューやjudgeで使う項目。

例。

```text
因果が通っているか
キャラ動機が成立しているか
伏線が目立ちすぎていないか
説明不足と意図的未開示を区別できているか
```

## 6. Ledger Target

本文完成後に台帳へ反映する項目。

例。

```text
canon fact
character knowledge
timeline event
foreshadowing status
open question
author decision
```

## 7. Framework Lens

固定テンプレートではなく、その時点だけ適用する視点。

例。

```text
三幕構成
Snowflake
Story Grid
Hero's Journey
ジャンル別テンプレート
```

---

# 統合時に見るべきこと

## 1. 既存StoryTemplateは厚すぎないか

厚すぎる場合の症状。

```text
全部埋めないと進めない
各作品に同じ問いを投げすぎる
テンプレ穴埋めが目的化する
ジャンルや作品固有の癖を潰す
```

対策。

```text
必須項目と任意項目に分ける
statusを持たせる
kernel / overlay / override に分類する
```

---

## 2. 項目の status を扱えるか

単なる「未記入」は不十分。

必要な status。

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

これがないと、AIは未記入をすべて欠落として扱う。

---

## 3. Chat から吸収できるか

既存StoryTemplateが「最初から穴埋めする」前提だと、自由な設計チャットと相性が悪くなる。

必要な接続。

```text
freeform chat
  ↓
domain synthesis
  ↓
StoryTemplate mapping
  ↓
gap / conflict / decision report
```

---

## 4. Workflow に渡せる小さな出力を作れるか

StoryTemplate 全体を writer に渡すと重すぎる。  
Adapter で小さい入力に変換する。

```text
StoryTemplate全体
  ↓
Adapter
  ↓
scene_card
acceptance_contract
judge_contract
```

---

## 5. 既存StoryTemplateの思想を明示する

テンプレートには必ず思想がある。

確認すること。

```text
プロット重視か
キャラ重視か
テーマ重視か
ジャンル約束重視か
文体・声重視か
読者体験重視か
設計トップダウンか
探索的執筆寄りか
```

思想が悪いわけではない。  
ただし、無自覚に全作品へ適用すると危険。

---

# 統合の推奨手順

## Step 1. 既存StoryTemplateの全項目を棚卸しする

成果物。

```text
existing_storytemplate_inventory.md
```

各項目について記録。

```text
field_name
description
current_usage
required_or_optional
layer
used_by
notes
```

---

## Step 2. 項目を分類する

分類先。

```text
Universal Kernel
Genre Overlay
Project Override
Workflow Input
Review Checklist
Ledger Target
Framework Lens
Unclear
```

成果物。

```text
storytemplate_field_mapping.yaml
```

---

## Step 3. 不足・重複・過剰を洗い出す

見るもの。

```text
不足:
  workflowに必要なのに項目がない

重複:
  複数項目が同じ意味を持つ

過剰:
  毎回必要ではないのに必須化されている

曖昧:
  項目の役割が不明

危険:
  作品固有の美学を潰しそう
```

成果物。

```text
storytemplate_gap_report.md
```

---

## Step 4. Adapter 接続を定義する

既存StoryTemplateのどの項目が、何に変換されるかを定義する。

```text
StoryTemplate field
  → scene_card field
  → acceptance_contract field
  → judge check
  → ledger update target
```

成果物。

```text
storytemplate_adapter_mapping.yaml
```

---

## Step 5. Pilot Episodeで検証する

1 Episode で以下を試す。

```text
freeform chat
  ↓
domain synthesis
  ↓
existing StoryTemplate mapping
  ↓
adapter
  ↓
scene_card / contract
  ↓
episode-draft-tournament
  ↓
judge / ledger
  ↓
retro
```

---

# 既存StoryTemplateを壊さず統合する考え方

既存StoryTemplateを全面的に置き換える必要はない。

おすすめは以下。

```text
既存StoryTemplate:
  今までの設計知を保持する

StoryaTemplate Kernel:
  汎用的な最小構造として抽出する

Adapter:
  既存StoryTemplateとworkflowをつなぐ

Framework Index:
  既存StoryTemplateに足りない視点を必要時に補う

Retro:
  実際に効いた項目だけ強化する
```

---

# 統合時の注意

```text
既存StoryTemplateを神格化しない
新しいStoryaTemplateで置き換えようとしない
まずは項目の役割を分類する
必須項目を増やしすぎない
未記入を即欠落扱いしない
ジャンル別項目を汎用kernelに混ぜない
作品固有ルールを一般理論にしない
```

---

# 目標

既存StoryTemplateを以下のように変換できる状態にする。

```text
考えるための箱
  +
不足検出チェックリスト
  +
workflow input generator
  +
review / judge support
  +
ledger update guide
```

ただし、作品を縛る絶対ルールにはしない。
