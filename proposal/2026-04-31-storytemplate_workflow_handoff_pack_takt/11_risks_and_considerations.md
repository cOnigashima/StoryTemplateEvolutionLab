# 考慮すべきリスト・リスク一覧

## 1. 創作上のリスク

### テンプレートが作品を支配する

症状。

```text
テンプレ穴埋めが目的化する
作品固有の歪みや魅力が消える
ジャンル外しが欠陥扱いされる
```

対策。

```text
StoryTemplate は薄い kernel にする
Genre Overlay と Project Override を分ける
Framework は lens として一時適用する
```

---

### レビューで尖りが削られる

症状。

```text
違和感がすべて修正される
謎が説明不足扱いされる
キャラの欠点が消される
文体の癖が均される
```

対策。

```text
intended_unknowns を明示する
TASTE と FAIL を分ける
do_not_fix を synthesis に入れる
Project Override を優先する
```

---

### 候補統合で平均化する

症状。

```text
A案の冒頭、B案の会話、C案の締めを混ぜる
声が継ぎ接ぎになる
無難な本文になる
```

対策。

```text
base draft は1本だけ選ぶ
borrow elements は最大3つ
borrow は文章片ではなく設計意図中心
single integration reviser が一本に戻す
```

---

## 2. Workflow上のリスク

### AIが止まりすぎる

原因。

```text
human_required_if が広すぎる
judge が保守的すぎる
contract が曖昧
```

対策。

```text
FAIL_AUTO_FIX と NEEDS_HUMAN を明確に分ける
auto_fix_allowed を広めに定義する
pilot で judge を校正する
```

---

### AIが勝手に重要設定を変える

原因。

```text
writer に権限を与えすぎる
ledger / bible が不足している
must_not_violate が曖昧
```

対策。

```text
重要設定・真相・キャラ動機の変更禁止
human_required_if を明記
ledger を渡す
judge で検出
```

---

### レビューが増えすぎる

原因。

```text
全reviewerを毎回呼ぶ
全unit testを毎Episodeで回す
```

対策。

```text
通常Episodeは最小構成
重要Episodeだけ拡張
Packet / Arcで重いレビューを回す
```

---

## 3. 情報管理上のリスク

### Knowledge / Project Design / Production State が混ざる

危険。

```text
一般ノウハウが作品制約になる
没案がcanonになる
仮説が確定事実になる
```

対策。

```text
3層を分ける
confirmed / tentative を分ける
visibility を付ける
rejected_ideas を分離する
```

---

### Ledger が肥大化する

原因。

```text
細かい描写まで全て記録する
毎Episodeで過剰にcharacter_statesを更新する
```

対策。

```text
ledger登録条件を決める
minor detailは除外
Packet単位更新も検討
```

---

### Ledger が足りない

症状。

```text
キャラが知るはずのない情報を知る
伏線が消える
読者未開示情報が漏れる
```

対策。

```text
character_states
open_questions
foreshadowing
author_decisions
を最低限維持
```

---

## 4. 調査上のリスク

### Deep research が沼になる

症状。

```text
創作理論を調べ続ける
Framework Indexが巨大化する
実際に書かない
```

対策。

```text
調査結果はFramework Index Cardに限定
今使うlensだけ調べる
Pilot後に必要なものだけ追加
```

---

### 最強テンプレートを作りたくなる

危険。

```text
万能化しようとして厚くなる
ジャンル固有項目が汎用kernelに混ざる
作品を縛る
```

対策。

```text
Kernelは薄く
Overlay / Lens / Overrideを分ける
Retroで効いた項目だけ残す
```

---

## 5. 人間側のリスク

### 全部見たくなる

対策。

```text
人間は不可逆判断に集中する
細かい文体修正は後回し
low-riskはAIに任せる
```

---

### 全部決めてから書こうとする

対策。

```text
Pilot Episodeを早く回す
設計はv0でよい
Retroで育てる
```

---

### AI案を捨てきれない

対策。

```text
rejected_ideasに保存する
今回は採用しない、と明示する
採用数に上限を設ける
```

---

# 重要な考慮ポイント一覧

```text
StoryTemplateは薄く保つ
Adapterで柔軟に吸収する
Framework Lensは一時適用する
Project Overrideを優先する
Episodeでは本文候補を競わせる
Packet / Arcでは構成・レビュー中心にする
Judgeは品質ゲートに限定する
Ledgerで状態管理する
Retroで増えた要素を削る
最初はPilot Episodeに集中する
```
