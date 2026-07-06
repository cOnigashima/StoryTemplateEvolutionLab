# Framework Index 戦略

## 基本方針

小説創作ノウハウをすべて統合した「最強テンプレート」を作らない。  
代わりに、既存フレームワークを index 化し、その時点の問題に合う lens として使う。

```text
最強テンプレート
  ×

最強のフレームワーク選択・接合・振り返りシステム
  ○
```

---

# なぜ最強テンプレートを作らないか

物語フレームワークは、それぞれ何かを見やすくする代わりに、何かを見えにくくする。

リスク。

```text
テンプレートが作品を支配する
ジャンル固有の快感を潰す
実験的構造を欠陥扱いする
作者の癖や強みを平均化する
穴埋めが目的化する
実際の本文に効いているか分からない
```

---

# Framework Index の役割

各フレームワークについて、以下を記録する。

```yaml
framework_id: ""
name: ""
summary: ""
best_for:
  - ""
not_good_for:
  - ""
use_as:
  - planning_lens
  - diagnosis_lens
  - genre_lens
  - revision_lens
adapter_outputs:
  - ""
risks:
  - ""
when_to_apply:
  - ""
when_not_to_apply:
  - ""
related_workflows:
  - ""
retro_questions:
  - ""
status: candidate | active | archived | rejected
```

---

# Framework Lens の例

## Premise / Logline Lens

使う場面。

```text
企画初期
作品の核がぼやけているとき
読者への約束を短く言語化したいとき
```

出力。

```text
premise
reader promise
central conflict
stakes
```

---

## Three-act Lens

使う場面。

```text
全体構成
Part / Arc の大きな配置
転換点の確認
```

注意。

```text
すべての作品を三幕に押し込めない
```

---

## Snowflake-like Expansion Lens

使う場面。

```text
一文のアイデアから段階的に構造化したいとき
Part / Arc / Packet の骨格を作るとき
```

注意。

```text
設計が先に固まりすぎる可能性
探索的執筆とは相性が悪い場合がある
```

---

## Story Grid-like Scene Diagnosis Lens

使う場面。

```text
シーンやEpisodeの機能を診断したいとき
価値変化、対立、turning point を見たいとき
```

注意。

```text
診断には強いが、生成テンプレートとしては硬くなる可能性
```

---

## Mystery Lens

使う場面。

```text
謎、手がかり、誤誘導、情報開示を管理したいとき
```

出力。

```text
central question
clues
red herrings
reveal schedule
fair play constraints
```

---

## Romance Lens

使う場面。

```text
関係性進行、親密度、障害、感情的転換を管理したいとき
```

出力。

```text
attraction vector
obstacles
intimacy progression
dark moment
resolution mode
```

---

## Thriller Lens

使う場面。

```text
脅威、時間制限、圧力、エスカレーションを設計したいとき
```

出力。

```text
threat
clock
escalation
reversal
pressure points
```

---

## Voice / Literary Lens

使う場面。

```text
構造より声・モチーフ・語りの質感を重視したいとき
```

出力。

```text
narrative distance
image system
motifs
prose rhythm
silence / omission rules
```

---

# Lens Selection の判断基準

```yaml
lens_selection:
  current_problem: ""
  candidate_lenses:
    - lens_id: ""
      why_useful: ""
      risk: ""
      expected_output: ""
  selected_lens:
    id: ""
    reason: ""
  not_selected:
    - lens_id: ""
      reason: ""
  application_scope:
    unit: episode | packet | arc | part | manuscript
    duration: one_time | until_retro | project_wide
```

---

# Framework Lens の適用ルール

## 1. Lens は一時適用

作品全体を支配させない。

## 2. Project Override を優先

作品固有の美学・方針が lens と衝突したら、Project Override を優先する。

## 3. Retro で評価する

Lens が効いたかどうかを必ず振り返る。

## 4. 使わない lens を明示する

何を採用しないかも重要。

---

# Framework Index の初期セット

最初は少なくてよい。

```text
Premise / Logline Lens
Three-act Lens
Snowflake-like Expansion Lens
Story Grid-like Scene Diagnosis Lens
Genre Overlay Lens
Voice / Literary Lens
```

対象作品のジャンルに応じて、必要な overlay だけ追加する。

---

# 今すぐやらないこと

```text
全創作理論の網羅
全ジャンルoverlayの作成
作家別創作術の大量比較
文学理論の体系化
最強テンプレート化
```

---

# Framework Index の成功条件

```text
調査結果が制作判断に接続する
どの lens をいつ使うか分かる
使わない理由も記録される
Pilot / Retro で効果検証できる
StoryTemplate を過剰に肥大化させない
```
