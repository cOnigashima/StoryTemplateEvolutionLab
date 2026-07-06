# 主要概念・用語集

## TAKT

Workflow / persona / prompt / routing / review を実行するための基盤。

ここでの役割。

```text
TAKT = 制作ラインの実行エンジン
```

TAKT自体が物語理論やテンプレートを解決するわけではない。  
TAKTに渡す前段として、StoryTemplate / Adapter / Contract が必要。

---

## StoryTemplate / StoryaTemplate

物語設計の箱・観点・チェックリスト。

ここでは以下の3層に分ける。

```text
Universal Kernel:
  汎用的に使える薄い中核

Genre Overlay:
  ジャンル固有の期待・制約

Project Override:
  この作品固有の例外・美学・方針
```

---

## Framework Index

既存の創作フレームワークのカタログ。

目的。

```text
何を使うかを選ぶための索引
```

「全部統合して最強テンプレートにする」のではなく、必要に応じて Framework Lens として使う。

---

## Framework Lens

ある時点の問題に対して一時的に適用する視点。

例。

```text
Premise Lens
Three-act Lens
Snowflake-like Expansion Lens
Story Grid-like Scene Diagnosis Lens
Mystery Lens
Romance Lens
Thriller Lens
Voice / Literary Lens
```

---

## Adapter

自由な設計チャットや StoryTemplate の内容を、workflow 用の入力に変換する層。

変換先。

```text
scene_card
acceptance_contract
judge_contract
review_checklist
ledger_update_targets
packet_map
arc_map
```

---

## Domain Synthesis

自由なチャットの成果を構造化する処理。

分類。

```text
confirmed
tentative
open_questions
contradictions
author_decisions_needed
```

---

## Scene Card

Episode を書くための設計カード。

含むもの。

```text
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

---

## Acceptance Contract

judge が判定するための合格基準。

含むもの。

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

---

## Judge

品質ゲート。

```text
judge = contract に照らして通すか止める存在
```

判定。

```text
PASS
FAIL_AUTO_FIX
NEEDS_HUMAN
REJECT_AND_REGENERATE
```

judge は「面白さの神」ではない。

---

## Ledger

制作中の真実台帳。

入れるもの。

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

## Bible

作品の原典設定。

```text
キャラ設定
世界観
文体方針
テーマ
ジャンル方針
```

bible は初期設定寄り。  
ledger は執筆進行中の状態管理。

---

## Episode

1話単位。  
本文候補を作る基本単位。

主 workflow。

```text
episode-draft-tournament
```

---

## Packet

複数 Episode の制作・レビュー単位。  
章束。

見るもの。

```text
接続
重複
テンポ
局所因果
情報開示順
Packet末尾の引き
```

---

## Arc

Part 内の中規模構造。  
複数 Packet からなる。

見るもの。

```text
中期的な問い
反転
伏線と回収
関係性変化
中だるみ
Partへの貢献
```

---

## Part

第一部・第二部などの大区分。

見るもの。

```text
Part開始時と終了時の不可逆変化
主人公・世界・読者理解の変化
次Partへの接続
```

---

## Draft

単位名ではなく状態名。

```text
Episode draft
Packet draft
Arc revision plan
```

---

## Chapter

内部制作単位としては使わないことを推奨。  
読者向け表示名としては使ってよい。

理由。

```text
1話なのか、章束なのか、中規模まとまりなのか曖昧になりやすい
```

---

## Retro

振り返り。

対象。

```text
本文
writer persona
selection
judge
adapter
StoryTemplate
Framework Lens
ledger
human-in-the-loop
```

目的。

```text
効いたものを残す
邪魔だったものを捨てる
次のpilotに反映する
```
