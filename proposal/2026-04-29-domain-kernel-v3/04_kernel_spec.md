# Kernel 仕様 v3

> **目的**: Layer 1 kernel を「ガチガチに薄く」固定する。11 項目だけを必須とし、それぞれの必須度・記述形式・サンプルを field-by-field で確定する。
> **ガチガチ度**: 11 項目とその必須度は本 v3 で固定。記述形式は推奨（作品ジャンルで微調整可）。
> **配置**: 各作品の `story/kernel.yaml`。1 作品 1 ファイル。

---

## 1. 設計方針

- **薄い**: 11 項目以上に増やさない。増やしたい項目は overlay / lens / bible / craft に出す
- **必須**: 11 項目すべてに必ず何かが入っている（status を含む）
- **status 区別**: 空欄禁止。値が無いときは status で理由を示す（`05_status_vocabulary.md`）
- **生成しない**: kernel は author + plotter が固める。AI は提案するが author 承認なしに kernel を確定しない
- **作品支配しない**: kernel は「執筆を始められる」最低条件。kernel の項目だけで作品を縛らない（craft / framework_lens は別途使う）

---

## 2. kernel.yaml 全体構造

```yaml
# story/kernel.yaml
kernel:
  schema_version: "v3"
  work_id: ""                # work slug
  last_updated: ""           # YYYY-MM-DD
  
  # 1. premise — 1〜2 文の作品要約
  premise:
    value: ""
    status: filled | tentative | needs_author_decision
    note: ""
  
  # 2. promise — 読者への約束 3〜5 項目
  promise:
    items:
      - id: ""
        claim: ""
        status: filled | tentative | needs_author_decision
        evidence_target: ""    # この約束がどの packet で実装されるか
    overall_status: ""
  
  # 3. protagonist_vector
  protagonist_vector:
    primary_protagonist:
      character_id: ""
      want: 
        value: ""
        status: ""
      need:
        value: ""
        status: ""
      wound_or_misbelief:
        value: ""
        status: ""
    additional_pov_characters:
      - character_id: ""
        want: ""
        need: ""
        wound_or_misbelief: ""
  
  # 4. conflict
  conflict:
    external:
      value: ""
      status: ""
    internal:
      value: ""
      status: ""
    relational:
      value: ""
      status: ""
  
  # 5. stakes
  stakes:
    if_protagonist_fails: ""
    if_protagonist_succeeds_but_pays: ""
    why_reader_cares: ""
    status: ""
  
  # 6. change_model
  change_model:
    arc_shape: growth | fall | flat | circular | mixed
    direction_of_change: ""
    end_state_relative_to_start: ""
    status: ""
  
  # 7. causality
  causality:
    time_order_policy: linear | nonlinear | multi_pov | flashback_heavy
    knowledge_state_monotonicity: strict | relaxed | per_pov
    rationalization_vocabulary_policy: avoid | allowed_with_check
    status: ""
  
  # 8. information_design
  information_design:
    must_be_clear:
      - ""
    intended_unknowns:
      - id: ""
        claim: ""
        intended_reveal_unit: episode | packet | arc | part | manuscript
        intended_reveal_id: ""
    disclose_policy: ""
    withhold_policy: ""
    status: ""
  
  # 9. emotional_arc
  emotional_arc:
    overall_curve: ""           # 例: 「平穏 → 焦燥 → 諦観 → 再起 → 静寂」
    target_reader_emotion_at_end: ""
    cadence_baseline:
      tension_to_release_ratio: "6:4"
    status: ""
  
  # 10. style_voice
  style_voice:
    pov: first_person | third_person_limited | third_person_omniscient | epistolary | mixed
    tense: present | past | mixed
    register: literary | conversational | rough | formal | mixed
    sentence_length_baseline: short | medium | long | varied
    narrative_temperature: cold | neutral | warm | hot
    forbidden_words:
      - ""
    style_references:
      - ""
    status: ""
  
  # 11. unit_tree
  unit_tree:
    has_part: true | false
    planned_part_count: 0
    planned_arc_count_per_part: 0
    planned_packet_count_per_arc: 0
    planned_episode_count_per_packet: 0
    target_total_episodes: 0
    serial_or_complete: serial | complete
    status: ""
```

---

## 3. 各項目の詳細仕様

### 3.1 premise

**役割**: 作品全体を 1〜2 文で言える形にする。kernel の出発点。

**必須度**: **MUST**。これ無しに何も始まらない。

**記述形式**:
- 1 〜 2 文。3 文以上は分解不足
- 「誰が」「何を」「どうする」（できれば「なぜ」「何のために」も）
- 抽象論禁止。具体的な動詞と対象を含む

**サンプル**:
```yaml
premise:
  value: |
    幼少期に天才と呼ばれた青年が、家族の不在を埋めるために
    AI 工房を開き、自分が書けなくなった物語を AI に書かせる中で、
    自分が本当に書きたかったものを取り戻す。
  status: filled
```

**反例（やり直し）**:
- 「友情と裏切りの物語」 ← 抽象すぎ
- 「主人公が成長する話」 ← 主語と動詞だけ
- premise が 5 行以上 ← 分解不足

---

### 3.2 promise

**役割**: 読者に対する明示的・暗示的な約束。守られないと裏切りになる。

**必須度**: **MUST**。最低 3 項目。多くて 5 項目。

**記述形式**:
- 各 item は「読者が何を期待してよいか」を 1 文で
- ジャンル約束（romance なら結ばれる、mystery なら解決する 等）も項目化
- 各 item に `evidence_target`（どの packet で実装するか）を付ける（書き始めは未定でも可）

**サンプル**:
```yaml
promise:
  items:
    - id: "p1"
      claim: "主人公が AI と協働で 1 本の長編を完成させる"
      status: filled
      evidence_target: "packet-final"
    - id: "p2"
      claim: "AI と人間の境界に関する明確な姿勢を示す"
      status: filled
      evidence_target: "arc-02 全体"
    - id: "p3"
      claim: "家族関係の癒着が解消される（または明確に拒絶される）"
      status: filled
      evidence_target: "packet-006"
  overall_status: filled
```

**反例**:
- 「面白くする」 ← 約束になっていない
- 8 項目以上 ← 守れない
- ジャンル約束を書かない ← 必須の暗黙約束を見落とす

---

### 3.3 protagonist_vector

**役割**: 主人公（と必要なら追加 POV）の want / need / wound を固定する。物語の駆動力と着地点を決める。

**必須度**: **MUST**（want / need のみ。wound は SHOULD）。

**記述形式**:
- want: 表面の目標。物語を動かす。1 文
- need: 深層の必要。キャラアークの帰着点。1 文
- wound: 過去の傷 or 誤信念。need を埋めるための障害。1 文
- want と need は **基本的にぶつかる**（一致したらアークが生まれない）

**サンプル**:
```yaml
protagonist_vector:
  primary_protagonist:
    character_id: "ch-protagonist"
    want:
      value: "AI 工房を成功させて、家族に評価される"
      status: filled
    need:
      value: "他者の評価ではなく、自分のために物語を書く"
      status: filled
    wound_or_misbelief:
      value: "幼少期の家族離散で、評価されないと存在しないと思い込んでいる"
      status: filled
```

**反例**:
- want と need が一致 ← アークなし
- want が抽象 ← 駆動力にならない
- wound 無し ← need を埋める必然性が不在

---

### 3.4 conflict

**役割**: 中核対立。external / internal / relational の 3 軸。

**必須度**: **MUST**（最低 1 軸）。3 軸全部埋まっているのが理想。

**記述形式**:
- external: 外部の対立要素（敵対者・障害状況）
- internal: 主人公内部の葛藤
- relational: 関係性の対立（仲間内・恋愛・親子等）

**サンプル**:
```yaml
conflict:
  external:
    value: "出版業界の AI 利用に対する保守的な反発"
    status: filled
  internal:
    value: "AI に書かせている自分は本当に作家か?"
    status: filled
  relational:
    value: "AI 否定派の家族と工房継続派の主人公"
    status: filled
```

---

### 3.5 stakes

**役割**: 失敗時に何が失われるか。読者の関心を支える。

**必須度**: **MUST**。

**記述形式**:
- if_protagonist_fails: 完全失敗時の損失
- if_protagonist_succeeds_but_pays: 勝つけど代償を払う場合の代償
- why_reader_cares: 読者が「読むのを止められない」理由

**サンプル**:
```yaml
stakes:
  if_protagonist_fails: "工房破綻 + 自己肯定感の最後の足場喪失"
  if_protagonist_succeeds_but_pays: "家族との完全断絶"
  why_reader_cares: "AI 時代の自己定義という普遍問題に投影できる"
  status: filled
```

---

### 3.6 change_model

**役割**: キャラアークの形と方向を決める。

**必須度**: **MUST**。

**記述形式**:
- arc_shape: growth（成長）/ fall（堕落）/ flat（不変）/ circular（円環）/ mixed
- direction_of_change: 1 文で「どこからどこへ」
- end_state_relative_to_start: 開始時と終了時の差分

**サンプル**:
```yaml
change_model:
  arc_shape: mixed
  direction_of_change: "他者承認依存から、自己表現の意志へ"
  end_state_relative_to_start: "外的成功は不確定、内的態度は反転"
  status: filled
```

---

### 3.7 causality

**役割**: 時間順・因果順・知識状態の単調性に関する作品方針。drafter-preflight の前提となる。

**必須度**: **MUST**。

**記述形式**:
- time_order_policy: 時間軸の方針
- knowledge_state_monotonicity: focal character が「知る」ことの単調性
- rationalization_vocabulary_policy: 「つまり」「要するに」等の合理化語彙の扱い

**サンプル**:
```yaml
causality:
  time_order_policy: linear
  knowledge_state_monotonicity: strict
  rationalization_vocabulary_policy: avoid
  status: filled
```

---

### 3.8 information_design

**役割**: 何を読者に開示し、何を意図的に隠すかの作品方針。intended_unknowns の正本。

**必須度**: **MUST**。

**記述形式**:
- must_be_clear: 読者に必ず分かるべきこと（list）
- intended_unknowns: 意図的に伏せていること（id 付き list）。各項目に reveal 予定の unit を付ける
- disclose_policy: 何を積極開示するか
- withhold_policy: 何を伏せ続けるか

**サンプル**:
```yaml
information_design:
  must_be_clear:
    - "主人公の現在の心境"
    - "AI 工房の経済状況"
    - "家族との物理的距離"
  intended_unknowns:
    - id: "iu1"
      claim: "AI が書いた部分と人間が書いた部分の境界"
      intended_reveal_unit: arc
      intended_reveal_id: "arc-03"
    - id: "iu2"
      claim: "家族離散の本当の原因"
      intended_reveal_unit: packet
      intended_reveal_id: "packet-009"
  disclose_policy: "現在進行形の事実は全て開示"
  withhold_policy: "過去の真相と内面の真の核は段階開示"
  status: filled
```

---

### 3.9 emotional_arc

**役割**: 作品全体の感情曲線。cadence の baseline。

**必須度**: **MUST**。

**記述形式**:
- overall_curve: 矢印で繋いだ感情遷移
- target_reader_emotion_at_end: 読了時の読者感情
- cadence_baseline: 緊張弛緩比率の baseline

**サンプル**:
```yaml
emotional_arc:
  overall_curve: "焦燥 → 高揚 → 動揺 → 諦観 → 静かな決意"
  target_reader_emotion_at_end: "余韻ある肯定"
  cadence_baseline:
    tension_to_release_ratio: "6:4"
  status: filled
```

---

### 3.10 style_voice

**役割**: 文体・声・POV の作品方針。

**必須度**: **MUST**。

**記述形式**:
- pov / tense / register / sentence_length_baseline / narrative_temperature を選ぶ
- forbidden_words: 作品禁則語
- style_references: 影響元の作家・作品

**サンプル**:
```yaml
style_voice:
  pov: third_person_limited
  tense: past
  register: literary
  sentence_length_baseline: varied
  narrative_temperature: warm
  forbidden_words:
    - "やはり"
    - "なんと"
    - "ガッツポーズ"
  style_references:
    - "村上春樹『ノルウェイの森』"
    - "川上未映子『ヘヴン』"
  status: filled
```

---

### 3.11 unit_tree

**役割**: この作品の構造計画。Manuscript / Part / Arc / Packet / Episode の予定数。

**必須度**: **MUST**（推定でよい）。

**記述形式**:
- has_part: Part を持つか
- 各層の予定数（短編は全 0、長編は全部）
- target_total_episodes: 目標 episode 数（kakuyomu 想定なら 50〜200）
- serial_or_complete: 連載か一括か

**サンプル**:
```yaml
unit_tree:
  has_part: true
  planned_part_count: 3
  planned_arc_count_per_part: 2
  planned_packet_count_per_arc: 3
  planned_episode_count_per_packet: 8
  target_total_episodes: 144
  serial_or_complete: serial
  status: tentative
```

---

## 4. kernel に「入れない」もの（再確認）

`03_layer_facet_map.md` §6 の通り、以下は kernel に入れない:

- bible 詳細（characters / world / rules）
- genre_overlay（mystery clues / romance dark moment 等）
- project_override（作品固有美学）
- packet 詳細
- episode 詳細
- scene card / acceptance contract
- foreshadowing_map（設計時の伏線配置）
- reveal_plan（fabula / syuzhet 対応）
- cadence_plan（packet 別緊張弛緩）
- ledger（実装中の状態）
- review 各種
- craft 原理
- framework lens の中身

これらは Layer 1 の他のファイル、または Layer 2/3 にある。

---

## 5. kernel.yaml の更新ルール

- **凍結後の変更**: 一度 filled になった項目を変更する場合、`story/canon-patch-proposals/` に proposal を立てる
- **status 変更**: tentative → filled は plotter 判断で可、filled → tentative は author 承認必須
- **追加項目禁止**: 11 項目以上に増やさない。増やしたい項目は overlay / lens / bible に出す（`08_open_questions.md` に提起）
- **削除禁止**: 11 項目を減らさない
- **timestamp 必須**: `last_updated` は変更時に必ず更新

---

## 6. 各項目の必須度サマリ

| 項目 | 必須度 | 空のときの status |
|---|---|---|
| premise | MUST | needs_author_decision |
| promise | MUST（最低 3 項目） | needs_author_decision |
| protagonist_vector.want | MUST | needs_author_decision |
| protagonist_vector.need | MUST | needs_author_decision |
| protagonist_vector.wound_or_misbelief | SHOULD | tentative or needs_author_decision |
| conflict（最低 1 軸） | MUST | needs_author_decision |
| stakes | MUST | needs_author_decision |
| change_model | MUST | tentative |
| causality | MUST | tentative |
| information_design.must_be_clear | MUST | tentative |
| information_design.intended_unknowns | SHOULD | tentative |
| emotional_arc | MUST | tentative |
| style_voice.pov | MUST | needs_author_decision |
| style_voice.tense | MUST | needs_author_decision |
| style_voice.register | SHOULD | tentative |
| unit_tree | MUST（推定でよい） | tentative |

**MUST が全部埋まらないと DoR を満たさない**（→ `06_setup_dor.md`）。

---

## 7. kernel が完成したかの判定

```yaml
kernel_complete:
  all_must_filled: true
  all_status_explicit: true
  internal_consistency_checked: true
  promise_evidence_targets_assigned: true
  unit_tree_consistent_with_serial_plan: true
```

これら 5 つが全て true になったら kernel は「執筆開始可能」状態。

---

## 8. kernel.yaml サンプル全体

実際のサンプルは `09_pilot_setup.md` に新規作品 bootstrap 例として掲載する。
