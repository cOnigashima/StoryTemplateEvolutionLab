# 状態語彙 v3

> **目的**: 「未記入＝欠落」と単純化せずに、空欄の理由を 11 種類で区別する。Judge 4 値と Lock 状態も同じ語彙系統に組み込む。
> **ガチガチ度**: 状態名は本 v3 で固定。意味と enum 値は変更禁止。新しい状態を増やすときは `08_open_questions.md` 経由。

---

## 1. なぜ状態を区別するか

AI（特に reviewer / judge）に「空欄」を渡すと、全部「欠落」扱いされる。だが実際には:

- 「決まっているが意図的に隠している」
- 「ジャンル上不要」
- 「作者が意図的に空にしている」
- 「決めるのは後の Phase」
- 「他フィールドと矛盾している」

など、空欄には **理由のグラデーション** がある。これを区別しないと:

- 必要な情報が「missing」に紛れて気づかれない
- 意図的非開示が「missing」と判定されて埋めるよう促される
- 作品固有の例外が一般欠落扱いされる
- AI が暴走して空欄を勝手に埋める

本 v3 では 11 状態で区別する。

---

## 2. Field Status 11 値

各値は **kernel フィールド / bible フィールド / scene_card フィールド / acceptance_contract フィールド** のいずれの「空に見える状態」も区別できる。

### 2.1 filled

**意味**: 値が入っており、確定済み。

**例**:
```yaml
premise:
  value: "...あらすじ..."
  status: filled
```

**取り扱い**:
- reviewer: そのまま使う
- judge: そのまま参照
- AI: 変更禁止（変更したいなら patch proposal）

---

### 2.2 missing

**意味**: 値が空で、本来は埋まるべき。これは本物の欠落。

**例**:
```yaml
stakes:
  if_protagonist_fails: ""
  status: missing
```

**取り扱い**:
- reviewer: 「埋めてください」と返す
- judge: kernel の MUST 項目が missing なら DoR 不満足、執筆停止
- AI: 候補を提案してよい（author 承認必須）

---

### 2.3 tentative

**意味**: 値はあるが暫定。確定ではない。

**例**:
```yaml
unit_tree:
  target_total_episodes: 144
  status: tentative
```

**取り扱い**:
- reviewer: 「暫定値が想定範囲内か」だけチェック
- judge: tentative でも DoR は満足とする（filled 同等）
- AI: 提案を更新してよい（status を tentative のまま、値だけ差し替え可）

---

### 2.4 deferred

**意味**: 後で埋める予定。今は埋めない方針。

**例**:
```yaml
foreshadowing_map:
  arc_03_foreshadow:
    items: []
    status: deferred
    deferred_until: "after-packet-002-frozen"
```

**取り扱い**:
- reviewer: deferred_until が来るまで言及しない
- judge: deferred なら参照対象外
- AI: 触らない

---

### 2.5 intentionally_blank

**意味**: 意図的に空。埋める予定もない。

**例**:
```yaml
genre_overlay.mystery:
  red_herrings: []
  status: intentionally_blank
  reason: "本作はミステリではないため不使用"
```

**取り扱い**:
- reviewer: 言及禁止
- judge: 参照対象外
- AI: 触らない

---

### 2.6 intentionally_hidden

**意味**: 値は決まっているが、読者には開示しない。author / plotter / drafter には見える。

**例**:
```yaml
information_design.intended_unknowns:
  - id: "iu1"
    claim: "AI が書いた部分と人間が書いた部分の境界"
    actual_truth: "..."
    status: intentionally_hidden
    visible_to: [author, plotter, drafter]
    hidden_from: [reader, judge_in_reader_mode]
```

**取り扱い**:
- reviewer: visible_to に含まれていれば参照可
- judge: visible_to に reader_simulation が無ければ「読者には不明」と判定
- AI: 漏洩禁止
- prose: 開示しない

---

### 2.7 not_applicable

**意味**: 本作には該当しない。

**例**:
```yaml
genre_overlay.romance:
  intimacy_progression: ""
  status: not_applicable
  reason: "本作は無 romance 路線"
```

**取り扱い**:
- reviewer: 言及禁止
- judge: 参照対象外
- AI: 触らない

---

### 2.8 genre_not_applicable

**意味**: このジャンルには該当しない（not_applicable のサブタイプ）。

**例**:
```yaml
mystery_lens.fair_play_constraints:
  status: genre_not_applicable
  reason: "ホラー作品のためミステリ fair play は適用外"
```

**取り扱い**:
- not_applicable と同等。`reason` で genre 文脈を明示する点だけ違う

---

### 2.9 project_override

**意味**: 作品固有方針で kernel / overlay の推奨を上書きしている。

**例**:
```yaml
style_voice.sentence_length_baseline:
  value: long
  status: project_override
  override_target: "kernel default 'medium'"
  reason: "本作は長文体を採用、語りの呼吸を優先"
```

**取り扱い**:
- reviewer: project_override は最高優先で尊重
- judge: project_override に違反する prose を書いたら FAIL
- AI: 触らない（変更したいなら author 経由）

---

### 2.10 contradiction

**意味**: 別フィールドと矛盾している。要解決。

**例**:
```yaml
protagonist_vector.want:
  value: "AI を完全否定する"
  status: contradiction
  conflicts_with:
    - field: "premise"
      reason: "premise は AI 工房の運営"
```

**取り扱い**:
- reviewer: 矛盾の解消を最優先で促す
- judge: contradiction 残存中は DoR 不満足、執筆停止
- AI: 解消案を提案してよい（author 承認必須）

---

### 2.11 needs_author_decision

**意味**: author 判断が必要。AI / plotter では決められない。

**例**:
```yaml
promise.items[2]:
  claim: "主人公が AI 工房を継続するか閉じるかが結末で確定する"
  status: needs_author_decision
  decision_options:
    - "継続"
    - "閉じる"
    - "曖昧なまま終わる"
  recommendation: "継続"
```

**取り扱い**:
- reviewer: author に上げる
- judge: needs_author_decision は kernel MUST フィールドだと DoR 不満足
- AI: option を提案してよいが confirm は author

---

## 3. Field Status 11 値の Decision Tree

新しいフィールド or 状態判定で迷ったとき:

```
Q1. 値が入っているか?
  Yes → Q2
  No  → Q3

Q2. 確定したか?
  Yes → filled
  No  → tentative

Q3. 本来埋まるべきか?
  Yes → Q4
  No  → Q5

Q4. 後で埋めるか?
  Yes → deferred
  No  → Q6

Q5. なぜ空なのか?
  ジャンル上不要 → not_applicable / genre_not_applicable
  意図的に空 → intentionally_blank
  読者には隠している（裏で値あり） → intentionally_hidden
  作品固有方針で推奨を外している → project_override

Q6. 矛盾しているか?
  Yes → contradiction
  No  → Q7

Q7. author 判断が必要か?
  Yes → needs_author_decision
  No  → missing
```

---

## 4. Judge 4 値

Acceptance Contract に対する Judge の判定値。

### 4.1 PASS

**意味**: 合格。次へ進める。

**取り扱い**:
- workflow: 次 step へ自動遷移
- ledger: 更新提案を反映
- author: 通知のみ（必要なら）

---

### 4.2 FAIL_AUTO_FIX

**意味**: 不合格だが、auto_fix_allowed の範囲内。AI が自動修正できる。

**取り扱い**:
- workflow: auto_fix_loop へ遷移
- ledger: 修正後に再 judge
- author: 通知のみ

**例**: 文法エラー / 軽微な合理化語彙 / 参考文献誤記

---

### 4.3 NEEDS_HUMAN

**意味**: 不合格で、human_required_if に該当。author 判断が必要。

**取り扱い**:
- workflow: 停止。author に通知
- ledger: 「pending human」状態
- author: 確認・判断・指示

**例**: 重要設定変更 / promise 違反疑い / project_override との衝突

---

### 4.4 REJECT_AND_REGENERATE

**意味**: 候補そのものが基準を満たさない。捨てて再生成。

**取り扱い**:
- workflow: tournament の次ラウンドへ。candidate を破棄
- ledger: rejected_ideas に保存
- author: 通知のみ

**例**: hard_gate（causality / 話者識別 / 文法）が 0 / candidate 全体が方針と乖離

---

## 5. Lock 状態

成果物が「次へ進める」状態を段階で表す。

### 5.1 unlocked

**意味**: まだ確定していない。drafting 中 or review 中。

**取り扱い**:
- 自由に変更可
- 公開不可

---

### 5.2 soft_lock

**意味**: Episode 単位の暫定確定。Judge PASS 後の状態。

**取り扱い**:
- packet 完成までは小修正可
- 他 Episode との接続調整で変更され得る
- 公開不可

---

### 5.3 packet_soft_lock

**意味**: Packet 全体としての暫定確定。packet-assembly-review PASS 後。

**取り扱い**:
- arc 全体調整で変更され得る
- Episode 単位の接続調整は完了
- 公開検討可

---

### 5.4 hard_lock

**意味**: author 承認後の確定。変更禁止（変更したいなら canon patch proposal）。

**取り扱い**:
- 公開可
- 変更は patch proposal 経由のみ
- ledger に確定情報として登録

---

### 5.5 published

**意味**: hard_lock + 公開済み。

**取り扱い**:
- 変更時は読者影響大の周知が必要
- canon patch proposal の影響範囲が広い

---

## 6. 状態遷移ルール

### 6.1 Field Status 遷移

```
許可される遷移:
  missing → tentative → filled
  tentative → contradiction（矛盾発見時）
  filled → contradiction（後発で矛盾発見時）
  any → needs_author_decision（author 介入要請時）
  needs_author_decision → filled / tentative（author 判断後）
  contradiction → filled / tentative（解消後）
  
禁止される遷移:
  filled → missing（埋まったものを「無かった」にしない。canon patch proposal 経由）
  intentionally_blank → filled（意図的空を後から埋めない。再度 author 承認）
  intentionally_hidden → filled（読者開示するなら reveal_plan 経由）
```

### 6.2 Judge 遷移

```
PASS → soft_lock
FAIL_AUTO_FIX → auto_fix_loop → 再 judge
NEEDS_HUMAN → 停止 → author 介入 → 手動修正 → 再 judge
REJECT_AND_REGENERATE → tournament 次ラウンド → 再 judge
```

### 6.3 Lock 遷移

```
unlocked → soft_lock（Episode judge PASS）
soft_lock → packet_soft_lock（packet-assembly-review PASS）
packet_soft_lock → hard_lock（author approval）
hard_lock → published（公開実施）
hard_lock → canon_patch_pending（patch proposal 提出）→ hard_lock（承認後）
```

---

## 7. status と DoR / DoD の関係

### 7.1 DoR 判定への影響

| status | DoR への影響 |
|---|---|
| filled | DoR ✓ |
| tentative | DoR ✓（暫定でよい） |
| deferred | フィールドが MUST なら DoR ✗、SHOULD なら DoR ✓ |
| intentionally_blank | DoR ✓（意図的） |
| intentionally_hidden | DoR ✓（裏に値あり） |
| not_applicable / genre_not_applicable | DoR ✓ |
| project_override | DoR ✓ |
| contradiction | DoR ✗（解消必須） |
| needs_author_decision | フィールドが MUST なら DoR ✗ |
| missing | フィールドが MUST なら DoR ✗ |

### 7.2 DoD 判定への影響

| status | DoD への影響 |
|---|---|
| filled / tentative（low risk） | DoD ✓ |
| その他 | DoD 判定は per case |

---

## 8. AI / 人間の役割境界

| status 値 | AI の権限 | 人間の権限 |
|---|---|---|
| filled | 参照のみ | 変更可 |
| missing | 候補提案 | 確定 |
| tentative | 候補提案・提案更新 | 確定昇格 |
| deferred | 触らない | deferred_until 変更可 |
| intentionally_blank | 触らない | 状態変更可 |
| intentionally_hidden | 参照可（visible_to 内のみ） | 開示判断可 |
| not_applicable | 触らない | 適用判断可 |
| project_override | 触らない | 変更可 |
| contradiction | 解消案提案 | 解消決定 |
| needs_author_decision | option 提案 | 確定 |

**原則**: AI は status を勝手に上げ下げしない。candidate 提案までで止める。確定は author or plotter。

---

## 9. status のサンプル運用

新規作品の bootstrap 直後（kernel.yaml）:

```yaml
kernel:
  premise: { value: "...", status: filled }
  promise:
    items:
      - { id: "p1", claim: "...", status: filled }
      - { id: "p2", claim: "...", status: tentative }
      - { id: "p3", claim: "...", status: needs_author_decision }
  protagonist_vector:
    primary_protagonist:
      want: { value: "...", status: filled }
      need: { value: "...", status: tentative }
      wound_or_misbelief: { value: "", status: deferred, deferred_until: "after-packet-001" }
  conflict:
    external: { value: "...", status: filled }
    internal: { value: "", status: tentative }
    relational: { value: "", status: not_applicable }
  ...
```

この状態で:
- kernel MUST の missing は無いが、`needs_author_decision` が 1 件
- DoR 判定: ✗（needs_author_decision がある）
- author の介入で `p3` を確定 → DoR ✓
- 執筆開始可能
