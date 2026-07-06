# Workflow 設計まとめ

## 原則

```text
1 workflow = ひとつの成果物を次のロック可能状態まで進める単位
```

人間が読んだかどうかではなく、成果物が次状態に進んだかを終点にする。

---

# 1. episode-draft-tournament

## 目的

1 Episode を、Packet に入れられる状態まで進める。

## 入力

```text
scene_card
acceptance_contract
packet_map
relevant_bible
relevant_ledger
style_guide
```

## 出力

```text
candidate drafts
selection report
integrated episode draft
judge report
ledger update proposal
episode soft lock
```

## 流れ

```text
prepare-context
  ↓
contract-check
  ↓
candidate-drafts
    ├─ faithful writer
    ├─ emotional writer
    ├─ plot-drive writer
    ├─ dialogue writer
    └─ risky writer
  ↓
quick-triage
  ↓
selection-synthesis
  ↓
integrated-rewrite
  ↓
episode-judge
  ↓
auto-fix-loop
  ↓
ledger-update
  ↓
soft-lock
```

## 初期運用では3 writerでよい

```text
faithful writer
emotional writer
plot-drive writer
```

3案で明確な差が出なければ、5案に増やしても意味が薄い。

---

# 2. packet-assembly-review

## 目的

複数 Episode を、Arc に渡せる Packet として整える。

## 入力

```text
soft-locked episodes
packet_map
packet_acceptance_contract
bible
ledger
style_guide
```

## 出力

```text
packet draft
packet review reports
packet synthesis
packet revised draft
packet judge report
ledger update proposal
packet soft lock
```

## 流れ

```text
assemble-packet
  ↓
through-reader-review
  ↓
packet-unit-tests
    ├─ continuity
    ├─ causality
    ├─ character knowledge
    ├─ canon coverage
    ├─ exposition balance
    └─ style/dialogue/rhythm
  ↓
packet-synthesis
  ↓
packet-revision
  ↓
packet-judge
  ↓
ledger-update
  ↓
packet-soft-lock
```

---

# 3. arc-through-review

## 目的

複数 Packet からなる Arc が、Part 内で機能しているか確認する。

## 流れ

```text
arc-through-reader-panel
  ↓
arc-unit-tests
  ↓
arc-diagnosis
  ↓
if structural_issue:
    arc-strategy-tournament
    ↓
    arc-selection-synthesis
  ↓
arc-revision-map
  ↓
arc-judge
```

---

# 4. arc-strategy-tournament

## 目的

Arc の構造問題に対して、複数の構成案を競わせる。

## 候補 persona

```text
conservative architect
pacing architect
emotional arc architect
mystery / information architect
veteran restructuring architect
```

## 出力

全文ではなく構造案。

```text
Packet順序
情報開示の前後
どのEpisodeを強めるか
どこを削るか
伏線と回収の位置
感情曲線
Reader promise / payoff
```

---

# 5. part-through-review

## 目的

Part が作品全体の中で役割を果たしているか確認する。

## 見るもの

```text
Part開始時と終了時の差分
主人公・世界・読者理解の変化
テーマへの寄与
次Partへの接続
読者疲労
Part末尾の満足感と引き
```

---

# 6. manuscript-final-review

後回しでよい。  
全体がある程度できてから。

見るもの。

```text
全体構造
伏線回収
キャラアーク
テーマ
文体統一
読後感
```

---

# 人間が入る場所

初期。

```text
contract approval
selection review
judge review
lock approval
```

中期。

```text
low-risk episode はAIに任せる
packet lock は人間が見る
NEEDS_HUMAN のみ対応
```

後期。

```text
arc / part 単位で人間が見る
```

---

# Workflow の注意

```text
writer と judge を同じ役にしない
selection と reviser を分ける
judge は本文を書き換えない
ledger keeper は本文を書き換えない
Packet / Arc では全文候補を毎回競わせない
```
