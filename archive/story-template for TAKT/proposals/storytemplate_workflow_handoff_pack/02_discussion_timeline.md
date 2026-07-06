# 議論の時系列レビュー

## 0. 出発点

出発点は、TAKTを使って、ある程度設定が固まった小説をドラフトし、レビューを大量に回し、章束ごとに作り上げるワークフローをどう組むかという問いだった。

初期の関心。

```text
小説ドラフトを書く
レビューをガンガン回す
ペルソナを複数使う
設定反映や整合性を見る
章束・パケットごとに作る
作者に詰める論点を整理する
```

---

## 1. 最初のワークフロー案

最初は、1つのドラフトを作り、複数レビューで改稿する案だった。

```text
draft
  ↓
parallel review
  ├─ reader persona
  ├─ editor
  ├─ veteran writer
  ├─ style/dialogue
  ├─ canon coverage
  └─ continuity
  ↓
synthesis
  ↓
revise
  ↓
judge
  ↓
ledger update
```

この段階では、TAKTは小説制作の品質管理ラインとして捉えられていた。

---

## 2. Packet / Episode の用語修正

ユーザー側の用語では、`packet` は複数ドラフトが集まった章束に近い。  
僕が当初言っていた `packet` は、むしろ scene card / episode draft に近かった。

修正。

```text
Episode / Draft:
  1話単位

Packet:
  複数 Episode の章束
```

この修正により、単位の整理が必要になった。

---

## 3. 1000タスク方式の検討

レビュー込みで1000個ほどのタスクを洗い出し、それらをキックしていく方式が話題になった。

この方式の問題。

```text
後続タスクが古くなる
レビューが過剰に増える
作者判断が爆発する
各レビューが競合する
実行キューが巨大化する
```

提案された扱い。

```text
1000タスク = 実行キューではなく catalog
```

ただし、その後、より重要な発想として `episode-draft-tournament` が出てきたため、1000タスクは一時的に脇へ置いた。

---

## 4. episode-draft-tournament の発見

複数ペルソナにドラフトを書かせ、それを採択する方式にしたほうが workflow の意味が出る、という発見があった。

これが大きな転換点。

```text
scene card
  ↓
writer candidates
  ├─ faithful
  ├─ emotional
  ├─ dialogue
  ├─ plot-drive
  └─ risky
  ↓
selection-synthesis
  ↓
integrated draft
```

ここで、レビューは単なる欠点探しではなく、候補選抜のための判断材料になる。

---

## 5. 章束・Arc・Part の議論

Episode の次の単位として、Packet / Arc / Part を整理した。

```text
Episode:
  本文候補を競わせる

Packet:
  複数 Episode を束ねて、接続・重複・テンポ・局所矛盾を見る

Arc:
  Part 内の中規模構造を見る

Part:
  第一部・第二部として見る
```

ここで、`chapter` は内部用語として使わない方がよいと整理した。

---

## 6. 章そのものを複数に任せるか

章、つまり Packet / Arc 単位でも複数に任せるかが議論された。

結論。

```text
Episode:
  複数 writer に本文候補を書かせる

Packet:
  基本は統合・レビュー・接続調整

Arc:
  複数 architect に構造案・改稿戦略を出させる

Part:
  通しレビューと revision planning
```

つまり、上位単位では「本文」ではなく「構成戦略」を競わせる。

---

## 7. Ledger の整理

ledger とは何かを整理した。

定義。

```text
ledger = 制作中の真実台帳
```

bible との違い。

```text
bible:
  作品の原典設定

ledger:
  執筆が進む中で確定・発生・保留された状態
```

対象。

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

## 8. Judge / Acceptance Contract の整理

AIにガリガリ進めさせるには、judge が必要という話になった。

judge は好みや絶対的な面白さを判定する存在ではない。

```text
judge = 合意済み acceptance contract に照らした品質ゲート
```

判定。

```text
PASS
FAIL_AUTO_FIX
NEEDS_HUMAN
REJECT_AND_REGENERATE
```

これにより、AIが自動修正できる範囲と、人間判断が必要な範囲を分ける。

---

## 9. StoryTemplate / Domain整理への拡張

次に、ワークフローだけではなく、設計と執筆の接合が問題になった。

自由なチャットで企画・設計することには価値がある。  
一方、workflow に渡すには、受け入れ側の箱・チェックリスト・contract が必要。

そこで、StoryTemplate / StoryaTemplate と Adapter の話が出てきた。

```text
Freeform Chat
  ↓
Domain Synthesis
  ↓
StoryTemplate
  ↓
Adapter
  ↓
scene_card / acceptance_contract
  ↓
workflow
```

---

## 10. 既存StoryTemplateとの統合課題

既存の StoryTemplate があるなら、それを無視して新しいものを作るべきではない。

やるべきこと。

```text
既存StoryTemplateの項目を棚卸しする
普遍kernel / genre overlay / project override / workflow input に分類する
不足・重複・過剰・曖昧さを見つける
Adapterで吸収する
```

---

## 11. フレームワーク選択の最適化

小説創作ノウハウを deep research して最強テンプレートを作るのは微妙、という話になった。

理由。

```text
各フレームワークには思想と癖がある
万能ではない
汎用的に厚くすると薄い作品になる
テンプレ穴埋めが目的化する
```

その代わりに、以下を作る。

```text
Framework Index
Framework Lens
Lens Selection
Adapter
Retro
```

つまり、

```text
最強テンプレートではなく、
最強のテンプレート選択・接合・振り返りシステム
```

を作る。

---

## 12. 現時点の収束方針

巨大設計に走らず、まず小さく接合する。

```text
StoryTemplate Integration Review
  ↓
Kernel v0
  ↓
Domain Synthesis Prompt v0
  ↓
Framework Index Card v0
  ↓
Adapter v0
  ↓
Pilot Episode
  ↓
Retro
```

これが現時点の最短ルート。
