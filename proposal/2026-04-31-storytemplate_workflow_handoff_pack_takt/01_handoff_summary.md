# ここまでの議論の俯瞰まとめ

## 一言でいうと

最初は TAKT を使った小説制作ワークフローの話だったが、議論は次第に、**自由な企画・設計チャットと、実際の執筆ワークフローをどう接合するか**という問題に広がった。

最終的には、以下の構造が見えてきた。

```text
自由な企画・設計チャット
  ↓
Domain Synthesis
  ↓
StoryTemplate / StoryaTemplate Kernel
  ↓
Framework Lens Selection
  ↓
Adapter
  ↓
scene_card / acceptance_contract / judge_contract / ledger targets
  ↓
episode-draft-tournament
  ↓
review / selection-synthesis / judge / ledger
  ↓
retro
```

つまり、目指すべきものは「AIに小説を書かせる」ではなく、  
**AIに複数の可能性を出させ、人間が方向を制御し、judge と ledger で制作状態を安定化させる長編小説制作システム**である。

---

# 議論の大きな流れ

## 1. TAKTを使った制作ワークフロー

最初の問題意識は、TAKTを使って以下をどう回すかだった。

```text
設定がある程度固まった小説を書く
レビューを大量に回す
パケット単位・章束単位で作り上げる
人間に詰める論点を抽出する
矛盾・不足・過剰を議論する
```

ここで、TAKTは単なる執筆ツールではなく、以下をオーケストレーションする基盤として捉えた。

```text
writer persona
reviewer persona
selection-synthesis
judge
ledger keeper
human decision gate
```

---

## 2. 単位の整理

当初は `packet` や `chapter` の意味が揺れていた。

最終的に、内部制作単位は以下のように整理した。

```text
Episode:
  1話。本文候補を作る基本単位。

Packet:
  複数 Episode の制作・レビュー単位。章束。

Arc:
  Part 内の中規模まとまり。複数 Packet からなる。

Part:
  第一部・第二部などの大区分。

Manuscript:
  全体。
```

重要な判断。

```text
Draft:
  単位名ではなく、Episode / Packet / Arc などの状態名。

Chapter:
  内部制作単位としては使わない。
  公開上の表示名としては使ってよい。
```

---

## 3. 1000タスク方式から候補生成方式へ

一時期、レビュー込みで1000個程度のタスクを洗い出してキックする方式が話題になった。

そのまま実行キューにするのは危険だと整理した。

理由。

```text
後続タスクがすぐ古くなる
レビューが前倒しされすぎる
作者判断が爆発する
レビュー同士が競合する
本文が委員会作文になる
```

ただし、1000タスクの洗い出し自体は悪くない。  
実行キューではなく、以下として扱うのがよい。

```text
task catalog
review catalog
test catalog
framework catalog
```

その後、「1000タスクはいったん忘れる」とし、より重要な方式として `episode-draft-tournament` が出てきた。

---

## 4. episode-draft-tournament

大きな転換点。

1本のドラフトを大量レビューで磨くのではなく、最初から複数の writer persona に候補ドラフトを書かせる。

```text
scene card
  ↓
faithful writer
emotional writer
dialogue writer
plot-drive writer
risky writer
  ↓
selection-synthesis
  ↓
integrated episode draft
  ↓
judge
  ↓
ledger update
```

重要ルール。

```text
base draft は必ず1本選ぶ
他案から借りる要素は最大数個
借りるのは基本的に文章片ではなく設計意図
do_not_borrow を明示する
最終本文は single integration reviser が一本の声に戻す
```

この方式により、ワークフローの意味が明確になった。

```text
writer:
  可能性を広げる

reviewer:
  問題を検出する

selection-synthesis:
  複数候補から採択方針を作る

reviser:
  一本に統合する

judge:
  合意基準で通すか止める

ledger:
  確定状態を記録する
```

---

## 5. Packet / Arc / Part の扱い

Episode では本文候補を競わせる。

一方、Packet / Arc / Part では全文候補を毎回複数書かせるのはやりすぎ。

整理。

```text
Episode:
  本文候補を競わせる

Packet:
  複数 Episode の接続・重複・テンポ・局所矛盾を見る

Arc:
  構成方針・改稿戦略を競わせる

Part:
  大局的な通しレビューと revision planning を行う
```

Arc では、複数の architect / editor persona に構造案を出させるのが有効。

```text
conservative architect
pacing architect
emotional arc architect
mystery / information architect
veteran restructuring architect
```

ただし、全文ではなく構成戦略を競わせる。

---

## 6. Judge と Ledger

AIにガリガリ進めさせるには、judge と ledger が必要。

### Judge

judge は「面白さの絶対判定者」ではない。

```text
judge = acceptance contract に照らして、次へ進めてよいか判定する品質ゲート
```

判定。

```text
PASS
FAIL_AUTO_FIX
NEEDS_HUMAN
REJECT_AND_REGENERATE
```

### Ledger

ledger は制作中の真実台帳。

```text
bible:
  作品の原典設定

ledger:
  執筆が進む中で確定・発生・保留された状態
```

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

重要なのは、AIが以下を忘れないようにすること。

```text
誰が何を知っているか
読者に何が未開示か
どの伏線が植えられているか
どの作者判断が確定済みか
何が没案で、何がcanonか
```

---

## 7. 設定・設計と執筆の接合

ワークフローだけでは足りないことが分かった。

企画や設計はチャットベースで自由に進む。  
一方で、執筆ワークフローに渡すには、ある程度構造化された入力が必要。

そこで必要になったのが Adapter。

```text
Freeform Chat
  ↓
Domain Synthesis
  ↓
StoryTemplate / StoryaTemplate
  ↓
Adapter
  ↓
scene_card / acceptance_contract / judge_contract / ledger targets
```

Adapter は、自由な創作議論を壊さずに、workflow が使える形へ変換する接合層。

---

## 8. StoryTemplate / StoryaTemplate の受け入れ方

既存の StoryTemplate との整合が重要になってきた。

ただし、ここでの結論は、巨大な「最強StoryTemplate」を作ることではない。

むしろ、StoryTemplate は以下のように扱うべき。

```text
StoryTemplate:
  物語設計の箱・観点・チェックリスト

StoryaTemplate Kernel:
  汎用的に使う薄い中心構造

Genre Overlay:
  ジャンル固有の読者期待・制約

Project Override:
  この作品固有の設計思想・例外・美学

Framework Lens:
  その時点の問題に応じて一時的に適用する創作フレームワーク
```

重要なのは、StoryTemplate を作品制作の支配者にしないこと。  
あくまで、自由な設計と workflow を接続するための受け入れ箱・チェックリスト・変換器として扱う。

---

## 9. フレームワーク選択の最適化

Evernote系テンプレート、Novel Software系テンプレート、Snowflake Method、Story Grid、三幕構成、Hero's Journey、ジャンル別テンプレートなど、創作ノウハウは大量にある。

しかし、全てを統合した「最強テンプレート」を作るのは危険。

理由。

```text
各フレームワークには思想と癖がある
汎用テンプレートは厚くすると作品を縛る
ジャンル固有の快感を潰す可能性がある
テンプレ穴埋めが目的化する
実際の本文に効いているか分からなくなる
```

方針。

```text
最強テンプレートを作らない
Framework Index を作る
その時点の問題に合う Framework Lens を選ぶ
Adapter に一時接続する
Pilot と Retro で効いたか確認する
```

---

# 現時点の最重要結論

## 結論1

TAKTのワークフロー設計だけでは不十分。  
自由な設計チャットと執筆ラインを接合する Adapter が必要。

## 結論2

StoryTemplate は巨大化させず、薄い kernel + genre overlay + project override + framework lens として扱う。

## 結論3

Episode では複数 writer に本文候補を書かせる `episode-draft-tournament` が有効。

## 結論4

Judge / Acceptance Contract / Ledger がないと、AIに自律的に作業を進めさせるのは危険。

## 結論5

すぐにやるべきことは、全体システムの完成ではなく、1 Episode の pilot。

```text
StoryTemplate Integration Review
  ↓
StoryaTemplate Kernel v0
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
