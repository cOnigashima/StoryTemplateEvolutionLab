# 05 Intake Coverage Checklist — raw → bible の網羅チェックリスト

> **役割**: Intake Adapter が raw を取り込むときに「何を抽出すべきか」「何が抜けているか」「何が衝突しているか」を機械的に検出する正本。
> **依存**: 02_domain_model.md（用語） / 03_storage_trinity.md（物理配置） / 04_pipeline_overview.md（フロー Phase 1）。
> **対象読者**: Intake Adapter prompt 実行時の reviewer（人間 / LLM）/ 既存 work の bible audit を回す reviewer。
> **粒度**: B (standard) — kernel 11 + facet ごと 5-10 項目で計 86 項目。

---

## 0. 使い方

### 0.1 いつ使うか

- **新規作品 bootstrap 時**: ChatGPT 企画 chat / 設計メモを Intake Adapter にかけたあと、出力（Digest）が本書を網羅しているかを検証
- **既存 work の bible audit 時**: 既に書かれている bible / design / state を本書のチェックリストで点検し、欠落 / 矛盾 / 重複を発見
- **外部完成 bible package の取り込み時**: ia_society の `bible/ia_story_bible_v2/` 50 ファイルのような外部完成物を、本書で「何が canon、何が design、何が state、何が drafts」に分配するか判定

### 0.2 出力すべきもの

本書で点検した結果は、Intake Adapter の出力（Digest）に次の形で記録する:

```yaml
intake_coverage_report:
  source: "{date}_{slug}"
  total_items_checked: 86
  filled: 0
  tentative: 0
  deferred: 0
  intentionally_blank: 0
  intentionally_hidden: 0
  not_applicable: 0
  genre_not_applicable: 0
  project_override: 0
  contradiction: 0
  needs_author_decision: 0
  missing: 0
  rejected: 0
  
  per_section:
    kernel:
      logline: { status: ..., source: ..., notes: ... }
      promise: { status: ..., items_count: 0, ... }
      ...
    bible_facets:
      world: { coverage: 7/7, missing: [], contradictions: [] }
      ...
  
  contradictions: []
  missing_critical: []
  needs_author_decision: []
  ready_for_dor_a: false
```

### 0.3 通過判定（Intake 完了判定）

最終的に **DoR-A 通過**するためには:
- MUST 項目すべてが `filled` / `tentative` / `intentionally_blank` / `intentionally_hidden` / `not_applicable` / `project_override` のいずれかで埋まっている
- `contradiction` ゼロ
- `needs_author_decision` ゼロ（または author が解決済み）
- `missing` ゼロ（MUST 項目に限る）

詳細は `06_bible_dor.md` 参照。

---

## 1. Kernel 11 項目（必須核）

`story/kernel.yaml` に格納される 11 項目。**すべて MUST**。

### 1.1 Logline (kernel #1)

| 項目 | 必須度 | 検出方法 | status 候補 |
|---|---|---|---|
| **logline 本文** (1-2 文) | MUST | raw に「〜の物語」「〜が〜する話」のような単文要約があるか / 暗黙なら author に確認 | filled / tentative / needs_author_decision |
| **出典 trace** | MUST | どの raw のどの行から抽出したか（`source: inbox/.../...md:L12-15`） | （メタ）|
| **Egri-Premise との混同回避** | SHOULD | "premise" と書かれていても thematic argument を意味するなら Theme に振り分ける | （振り分け）|

### 1.2 Promise (kernel #2)

| 項目 | 必須度 | 検出方法 | status 候補 |
|---|---|---|---|
| **promise items（最低 3 つ）** | MUST | raw に「絶対に〜しない」「〜を守る」「〜は破らない」等の宣言があるか | filled / tentative |
| **各 promise の violation 検出条件** | SHOULD | promise を破ったときに review でどう検出するか | filled / tentative / deferred |
| **各 promise の implementation target** | SHOULD | どの packet / arc で読者に示すか（`evidence_target: arc-01`） | filled / tentative / deferred |
| **promise vs Genre Overlay の整合性** | SHOULD | promise がジャンル期待に反する場合、Project Override として明示されているか | filled / project_override |

### 1.3 Protagonist Vector (kernel #3)

| 項目 | 必須度 | 検出方法 | status 候補 |
|---|---|---|---|
| **primary_protagonist.character_id** | MUST | 主人公の名前 / id | filled |
| **want** | MUST | 主人公が表面的に求めているもの | filled / tentative |
| **need** | MUST | 主人公が真に必要としているもの（want と異なることが多い） | filled / tentative / needs_author_decision |
| **wound_or_misbelief** | SHOULD | 主人公の内的傷 / 誤った信念 | filled / tentative / deferred |
| **secondary_protagonists**（任意） | MAY | 副主人公 | filled / not_applicable |

### 1.4 Conflict (kernel #4)

| 項目 | 必須度 | 検出方法 | status 候補 |
|---|---|---|---|
| **external conflict** | MUST | 外部対立（社会・敵・状況） | filled |
| **internal conflict** | SHOULD | 内的対立（want vs need、信念の揺らぎ） | filled / tentative |
| **relational conflict** | SHOULD | 人間関係の対立 | filled / tentative / deferred |
| **3 軸の重なり / 階層** | SHOULD | 3 つの conflict がどう絡むか | filled / tentative |

### 1.5 Stakes (kernel #5)

| 項目 | 必須度 | 検出方法 | status 候補 |
|---|---|---|---|
| **if_protagonist_fails** | MUST | 失敗したら何を失うか | filled |
| **if_protagonist_succeeds_but_pays** | SHOULD | 成功してもどんな代償があるか | filled / tentative |
| **why_reader_cares** | MUST | なぜ読者が結果を気にすべきか | filled / tentative |

### 1.6 Change Model (kernel #6)

| 項目 | 必須度 | 検出方法 | status 候補 |
|---|---|---|---|
| **arc_shape** | MUST | growth / fall / flat / circular / mixed | filled |
| **direction_of_change** | MUST | 何から何に向かう変化か | filled / tentative |
| **end_state_relative_to_start** | MUST | 開始状態と比較した終了状態 | filled / tentative |
| **transformation curve（character 別）** | SHOULD | 各キャラの変化形 | filled / tentative / deferred |

### 1.7 Causality (kernel #7)

| 項目 | 必須度 | 検出方法 | status 候補 |
|---|---|---|---|
| **time_order_policy** | MUST | linear / nonlinear / multi_pov / flashback_heavy | filled |
| **knowledge_state_monotonicity** | MUST | strict / relaxed / per_pov | filled |
| **rationalization_vocabulary_policy** | SHOULD | "つまり" "要するに" 等の使用方針 | filled / tentative |

### 1.8 Information Design (kernel #8)

| 項目 | 必須度 | 検出方法 | status 候補 |
|---|---|---|---|
| **must_be_clear** リスト | MUST | 読者に必ず伝わるべき事実 | filled |
| **intended_unknowns** リスト | SHOULD | 意図的に隠す情報（裏に値あり） | filled / tentative / intentionally_hidden |
| **disclose_policy** | SHOULD | 開示の基本方針 | filled / tentative |
| **withhold_policy** | SHOULD | 隠匿の基本方針 | filled / tentative |

### 1.9 Emotional Arc (kernel #9)

| 項目 | 必須度 | 検出方法 | status 候補 |
|---|---|---|---|
| **overall_curve** | MUST | 感情の全体カーブ | filled / tentative |
| **target_reader_emotion_at_end** | MUST | 読み終えたときの読者感情の目標 | filled |
| **cadence_baseline** | SHOULD | tension:release 比率の基準 | filled / tentative |

### 1.10 Style Voice (kernel #10)

| 項目 | 必須度 | 検出方法 | status 候補 |
|---|---|---|---|
| **pov** | MUST | first_person / third_person_limited / omniscient / epistolary / mixed | filled |
| **tense** | MUST | present / past / mixed | filled |
| **register** | SHOULD | literary / conversational / rough / formal / mixed | filled / tentative |
| **sentence_length_baseline** | SHOULD | short / medium / long / varied | filled / tentative |
| **narrative_temperature** | SHOULD | cold / neutral / warm / hot | filled / tentative |
| **forbidden_words** リスト | SHOULD | 禁止語彙 | filled / tentative / deferred |
| **style_references** | MAY | 参考作品 / 文体 | filled / not_applicable |

### 1.11 Unit Tree (kernel #11)

| 項目 | 必須度 | 検出方法 | status 候補 |
|---|---|---|---|
| **has_part** | MUST | true / false | filled |
| **planned_part_count** | MUST(if has_part) | Part 数 | filled / tentative |
| **planned_arc_count_per_part** | MUST | 各 Part の Arc 数 | filled / tentative / deferred |
| **planned_packet_count_per_arc** | SHOULD | 各 Arc の Packet 数 | filled / tentative / deferred |
| **planned_episode_count_per_packet** | SHOULD | 各 Packet の Episode 数 | filled / tentative / deferred |
| **target_total_episodes** | MUST | 全 Episode 数の目標 | filled / tentative |
| **serial_or_complete** | MUST | serial / complete | filled |

**Kernel 小計**: 41 項目（MUST 28 / SHOULD 11 / MAY 2）

---

## 2. Bible Facet 別の網羅項目（17 facet × 5-10 項目）

### 2.1 Theme（主題）

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **central_question**（中核問い） | MUST | "〜とは何か？" "〜は誰のものか？" |
| **work_answer_or_argument**（任意） | MAY | Egri-premise 的な命題 |
| **theme_to_motif_mapping** | SHOULD | 主題が反復される具体物 |
| **theme_violation_detection** | SHOULD | 主題に逆行する場面の検出基準 |

### 2.2 Rules（文体・禁則）

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **pov_rule** | MUST | POV 固定 / 切替条件 |
| **tense_rule** | MUST | tense 固定 / 切替条件 |
| **forbidden_vocabulary** | MUST | 禁止語句リスト |
| **dialogue_conventions** | SHOULD | 会話末ルール / 役割語禁止 等 |
| **description_constraints** | SHOULD | 描写の濃度・温度・モード制約 |
| **narrative_temperature** | SHOULD | 地の文の温度 |
| **forbidden_situations** | SHOULD | 暴力グロテスク / 性的越境 等の禁則 |

### 2.3 World（世界観）

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **geography** | MUST | 舞台の地理 |
| **time_period** | MUST | 時代 / 年 |
| **society_structure** | MUST | 社会構造 / 階層 / 経済の概要 |
| **physics_or_metaphysics** | SHOULD | 物理法則 / 超自然要素 |
| **named_locations** | SHOULD | 主要な場所（複数） |
| **cultural_context** | SHOULD | 文化的背景 / 風習 |
| **what_can_or_cannot_happen** | SHOULD | "世界の中で何ができて何ができないか" の境界 |

### 2.4 Character（人物）

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **protagonist** (kernel #3 と同期) | MUST | 主人公 |
| **primary_antagonist_or_opposition** | MUST | 主要な対抗者 |
| **supporting_characters** | SHOULD | 取り巻き / レギュラー（3-10 名） |
| **relationship_hub** | SHOULD | 主要な関係性のマップ |
| **voice_register_per_character** | SHOULD | キャラごとの声 |
| **character_count_planned** | MAY | 主要キャラ総数の目安 |

### 2.5 System（制度・能力体系）★ 新設

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **institutions_glossary** | MUST(genre依存) | 制度・組織・用語集 |
| **abilities_or_magic** | MUST(genre依存) | 能力 / 魔法 / 技術体系 |
| **rules_of_operation** | SHOULD | システムが動作するルール |
| **limits_or_costs** | SHOULD | 限界 / 代償 / 副作用 |
| **examples_in_use** | SHOULD | 具体例（誰が何を使うか） |
| **system_to_world_link** | SHOULD | World との接続点 |

> System が `not_applicable` になる作品もある（純粋な日常系等）。その場合は `not_applicable` 明示。

### 2.6 Timeline（時系列）★ 新設・2 階層

**Macro 層（前史 / 制度史）**:

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **pre_history** | SHOULD | Manuscript 開始前の歴史 |
| **institutional_history** | SHOULD | 制度の成立・変遷 |
| **manuscript_opening_anchor** | MUST | 物語開始時点の anchor（年・月日） |

**Micro 層（本編日次）**:

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **manuscript_period_span** | MUST | 物語の期間（◯日 / ◯ヶ月 / ◯年） |
| **day_by_day_chronology** | SHOULD | 日次イベント表 |
| **time_anchors_per_episode** | SHOULD | 各 Episode の時刻 anchor |

### 2.7 Sample Scene（試し場面）★ 新設

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **voice_calibration_scene** (1 つ以上) | SHOULD | 文体の声を確定する見本 1 場面 |
| **critical_moment_sample**（重要場面の見本） | MAY | 重要場面の事前ドラフト |
| **ng_sample**（ダメな例） | MAY | 「こう書かない」という反面教師 |

### 2.8 Plot

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **inciting_incident** | MUST | 事件の発端 |
| **major_reversal** | MUST | 主反転 |
| **climax** | MUST | クライマックス |
| **ending_state** | MUST | 終了状態 |
| **causal_chain** | SHOULD | 3-7 ステップの因果連鎖 |

### 2.9 Foreshadowing Map

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **foreshadowing_items** | SHOULD | 各伏線（id / 内容） |
| **lifecycle_per_item**（植 / 補強 / 回収） | SHOULD | 各伏線の ep 位置 |
| **type_per_item** | MAY | Chekhov / red herring / motif 等 |

### 2.10 Reveal Plan

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **reveal_items** | SHOULD | 各 reveal（id / 内容 / target ep） |
| **withhold_list** | SHOULD | 隠す情報の一覧 |
| **disclose_schedule** | SHOULD | 開示順 |

### 2.11 Motif

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **motif_items** | SHOULD | 各 motif（具体物 / 反復 phrase / gesture） |
| **lifecycle_per_motif**（起点 / 変奏 / 回収） | SHOULD | 各 motif の ep 位置 |
| **theme_link_per_motif** | MAY | Theme との関連 |

### 2.12 Cadence

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **tension_release_ratio** | SHOULD | 緊張弛緩比 |
| **peak_frequency** | SHOULD | 大波の頻度 |
| **arc_end_temperature** | MAY | Arc 末尾の温度 |

### 2.13 Logline (Bible Facet 側、kernel と重複参照)

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| logline 本文 | MUST | （kernel 1.1 と同期） |

### 2.14 Promise (Bible Facet 側、kernel と重複参照)

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| promise items | MUST | （kernel 1.2 と同期） |

### 2.15 Style Voice (Bible Facet 側、kernel と重複参照)

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| Style Voice 全項目 | MUST | （kernel 1.10 と同期） |

### 2.16 Genre Overlay（任意）

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **genre_name** | MAY | "異世界転生" "ダークファンタジー" 等 |
| **genre_conventions** | MAY | 必須要素 / 期待要素 |
| **reader_expectations** | MAY | 想定読者の期待 |
| **platform_specifics** | MAY | カクヨム / なろう 固有制約 |
| **forbidden_by_genre** | MAY | ジャンル禁忌 |

### 2.17 Project Override（任意）

| 項目 | 必須度 | 検出方法 |
|---|---|---|
| **override_items** | MAY | 各 override（normally / this work / rationale） |
| **override_strength** | MAY | hard / soft |
| **violation_consequence** | MAY | 破った場合の扱い |

**Bible Facet 小計**: 45 項目（MUST 14 / SHOULD 21 / MAY 10）

---

## 3. 抜け漏れ検出（Missing Detection）

### 3.1 検出ルール

Intake Adapter は次のすべてを実行して `missing` を検出する:

1. **Section 1（Kernel 11）の MUST 項目**を 1 つずつ raw 内検索（キーワード + 文脈推論）
2. **Section 2（Bible Facet 17）の MUST 項目**を facet ごとに検索
3. 見つからなかったものは `missing` として明示
4. **暗黙的に推論できる**ものは `tentative` で埋め、`source_inferred: true` を付ける
5. **deferred / not_applicable で済ませてよい**ものは author に確認を促す

### 3.2 missing を許容する条件（intentionally_blank への昇格）

次の条件で `missing` を `intentionally_blank` に降格できる:

- author が「この作品ではこの項目は不要」と明示
- ジャンル特性として該当しない（例: 純粋日常系で System なし）
- 短編で Part / Arc が不要

降格には **必ず author confirm を経る**。Adapter 単独で降格しない。

### 3.3 missing 検出時のアクション

| missing の重さ | アクション |
|---|---|
| MUST 項目が missing | DoR-A 通過不可。author に raise |
| SHOULD 項目が missing | needs_author_decision として open-questions.md に append |
| MAY 項目が missing | intentionally_blank として処理可 |

---

## 4. 矛盾検出（Contradiction Detection）

### 4.1 検出種別

3 種類の矛盾を区別する:

#### Type A: raw 内の自己矛盾

raw 内で同一項目について複数の主張がある:
- 例: ChatGPT chat の前半で「主人公 25 歳」、後半で「主人公 30 歳」

#### Type B: raw vs 既存 bible

raw の主張が既存 bible と衝突する:
- 例: raw が「真耕特区は東北」、bible は「東海」と書いている

#### Type C: facet 間の整合性

異なる facet の主張が論理的に整合しない:
- 例: Promise「和解で閉じない」 vs Plot「ラストで主人公と対抗者が和解」
- 例: Genre Overlay「異世界転生 = チート無双期待」 vs Project Override「チート無双禁止」 → これは矛盾ではなく Project Override として明示すれば OK

### 4.2 矛盾検出時のアクション

すべての contradiction は:
1. **`X-XXX` として ID 付与**
2. **`state/contradiction-log.yaml` に append**（Adapter が直接書かず Update Proposal 経由）
3. **claim_a / claim_b / source / severity を記録**
4. **needs_author_decision を立てる**（Adapter が勝手に解消しない）

severity 判定:
- **high**: canon 破壊 / promise 違反 → DoR-A 通過不可
- **mid**: 手戻り発生 / 一部 ep 修正必要 → 起票 + author 解決待ち
- **low**: 改善機会 → backlog/ に追加

---

## 5. 重複検出（Duplicate Detection）

### 5.1 検出ルール

raw の項目が既存 bible にすでに存在する場合:

| 関係 | アクション |
|---|---|
| **完全一致** | duplicate として記録、bible 側を維持、raw 側は no-op |
| **部分一致 + 補完情報あり** | bible 側に補完を Patch として提案 |
| **部分一致 + 矛盾** | Type B contradiction として処理 |
| **新規追加** | bible に Update Proposal で追加 |

### 5.2 既存 bible 全体スキャンの順序

Intake Adapter は raw を読む前に bible を 1 度スキャンして既存項目をインデックスする:
1. `bible/logline.md` `bible/promise.md` `bible/theme.md` を読む
2. `bible/world/` `bible/characters/` `bible/system/` 配下を読む
3. `bible/timeline/` を読む
4. その他 facet を読む

スキャン結果はメモリ内インデックスとして持ち、raw の各項目について重複チェックする。

---

## 6. Status 振り分け規則

### 6.1 11 status 値の判定フロー

```
raw の項目が見つかった
   ├── 明示的 + 矛盾なし → filled
   ├── 暗黙的 / 解釈幅あり → tentative
   ├── 明示的に「ここは決めない、後で」 → deferred
   ├── 明示的に「この作品は該当しない」 → not_applicable
   ├── 明示的に「ここは空欄が意図」 → intentionally_blank
   ├── 明示的に「裏に値あり、隠す」 → intentionally_hidden
   ├── ジャンル例外を明示 → project_override
   ├── 他項目と衝突 → contradiction
   ├── 候補が複数 → needs_author_decision
   ├── author が rejected → rejected

raw の項目が見つからない
   ├── MUST → missing（DoR-A 不通過）
   ├── SHOULD → missing（DoR-A 通過可、後で詰める）
   ├── MAY → intentionally_blank（許容）
```

### 6.2 status の昇格・降格

intake 後の運用:
- `tentative` → `filled`: 後の draft / review で確証が取れたら昇格
- `deferred` → `tentative` → `filled`: deferred 期限が来たら詰める
- `needs_author_decision` → `filled` / `rejected`: author 決定後に昇格
- `contradiction` → `filled` / `rejected`: Patch lifecycle で解消

### 6.3 Adapter が勝手にやってはいけないこと

- `contradiction` を勝手に解消しない（必ず author judgment）
- `needs_author_decision` を勝手に決めない
- `intentionally_hidden` を bible 本文に書かない（kernel.information_design.intended_unknowns に追加するのみ）
- `rejected` の判定を勝手にしない（author rejected と raw に明示があるときのみ）

---

## 7. Intake 完了判定

### 7.1 DoR-A 通過の最低条件

```
□ Section 1（Kernel 11）の MUST 28 項目すべてが
   filled / tentative / intentionally_blank / intentionally_hidden / not_applicable / project_override
   のいずれか
   
□ Section 2（Bible Facet 17）の MUST 14 項目（kernel 重複除く）すべてが同上
   
□ Section 3 の missing が「MUST 項目について」ゼロ
□ Section 4 の contradiction が severity=high についてゼロ
□ Section 5 の重複処理が完了
□ Section 6 の status 振り分けが完了

□ author confirm を経た Update Proposal が synthesis/update_proposals/ に存在
```

### 7.2 DoR-A 通過不可で先に進める条件

次のいずれかが満たされれば、DoR-A 不完全でも次 phase（packet freeze）に **限定的に**進める:

- MUST 項目の 80% 以上が埋まり、残り 20% が `deferred` で author confirm 済み
- `contradiction` severity=high が `state/contradiction-log.yaml` に起票され、解決計画が `design/canon-patch-proposals/` に存在

ただし **drafting には進まない**。Episode draft 開始は DoR-B（`06_bible_dor.md`）の通過が前提で、DoR-B は DoR-A の完全通過を前提とする。

### 7.3 Intake Coverage Report の最終出力

Intake Adapter は最後に次を必ず出力する:

```yaml
intake_coverage_summary:
  total_items: 86
  filled: 0
  tentative: 0
  deferred: 0
  intentionally_blank: 0
  intentionally_hidden: 0
  not_applicable: 0
  genre_not_applicable: 0
  project_override: 0
  contradiction: 0
  needs_author_decision: 0
  missing: 0
  rejected: 0
  
  must_coverage: 0/42      # MUST 項目の埋まり率
  should_coverage: 0/32
  may_coverage: 0/12
  
  dor_a_eligible: false    # DoR-A 通過可能か
  dor_a_blockers:          # 通過を妨げているもの
    - "..."
  
  recommended_next_actions:
    - "Q-001 を author confirm（white space 制度を通年か月次か）"
    - "X-001 を解決（湊の身長 170/175 矛盾）"
    - "ep01 draft 開始は DoR-A 完了後"
```

---

## 8. 実行例: ia_society の bible package を intake する

ia_society の `bible/ia_story_bible_v2/` 50 ファイル超を本書で intake する場合の expected behavior。

### Step 1: Raw 配置

```
inbox/planning_sessions/2026-04-30_ia_society_bible_v2_import.md
```
（50 ファイルを連結 or 索引付き 1 ファイル化）

### Step 2: Intake Adapter 実行

`adapter/intake_adapter_prompt.md` を呼び出し、本書（05_intake_coverage_checklist.md）を参照させる。

### Step 3: 期待される検出

#### Section 1 Kernel
| 項目 | 期待 status | source |
|---|---|---|
| logline | filled | `01_CORE_CANON.md` の "ひとことでの核" |
| promise | filled | `00_README.md` "迷ったら..." + `06_OPPOSITION_AND_JUSTICE.md` |
| protagonist (史弥) | filled | `05_CHARACTERS_MAIN_NOVEL.md` |
| conflict | filled | `06_OPPOSITION_AND_JUSTICE.md` |
| stakes | filled | `01_CORE_CANON.md` |
| ... | ... | ... |

#### Section 2 Facet
| facet | 期待 status | source |
|---|---|---|
| World | filled | `02_WORLD_SOCIAL_MODEL.md` |
| Character | filled | `05_CHARACTERS_MAIN_NOVEL.md` + 取り巻き |
| System | filled | `04_INSTITUTIONS_GLOSSARY.md` |
| Timeline (macro) | filled | `03_TIMELINE_AND_HISTORY.md` |
| Timeline (micro) | filled | `15_DAY_BY_DAY_CHRONOLOGY.md` |
| Sample Scene | filled | `11_SAMPLE_SCENES.md` |
| Plot | filled | `08_PLOT_3ACT_AND_20EP.md` |
| Foreshadowing Map | filled | `07_TRUTH_AND_CLUE_MAP.md` |
| Reveal Plan | filled | `28_REVEAL_BUDGET_SHEET.md` (上半分) |
| Motif | filled | `29_OBJECT_MOTIF_LADDER.md` (上半分) |
| Style Voice / Rules | filled | `10_WRITING_GUIDE_AND_VOICE.md` |
| Cadence | tentative | `08_PLOT_3ACT_AND_20EP.md` から推論 |
| Theme | filled | `01_CORE_CANON.md` 暗黙 + `06_OPPOSITION_AND_JUSTICE.md` |
| Genre Overlay | tentative | `00_README.md` "ジャンル" |
| Project Override | filled | `06_OPPOSITION_AND_JUSTICE.md` 等の独特な制約 |

#### 振り分け先

| ia_society の旧位置 | 新位置 |
|---|---|
| `01_CORE_CANON.md` | bible/logline.md + bible/theme.md + (kernel 多数) |
| `02_WORLD_SOCIAL_MODEL.md` | bible/world/society.md |
| `03_TIMELINE_AND_HISTORY.md` | bible/timeline/history.md |
| `04_INSTITUTIONS_GLOSSARY.md` | bible/system/institutions.md |
| `05_CHARACTERS_MAIN_NOVEL.md` | bible/characters/ 個別シート群 |
| `07_TRUTH_AND_CLUE_MAP.md` | bible/foreshadowing-map.md |
| `08_PLOT_3ACT_AND_20EP.md` | bible/plot.md + arcs/series-overview.md（分割） |
| `10_WRITING_GUIDE_AND_VOICE.md` | bible/style-voice.md + bible/rules.md（分割） |
| `11_SAMPLE_SCENES.md` | bible/samples/ |
| `13_DECISION_LOG_AND_OPEN_QUESTIONS.md` | design/open-questions.md + state/decision-log.yaml（**分割**） |
| `14_RELATIONSHIP_ARCS.md` | bible/characters/relationship-arcs.md |
| `15_DAY_BY_DAY_CHRONOLOGY.md` | bible/timeline/day-by-day.md |
| `19_LINE_LEVEL_CLUE_PAYOFF_TABLE.md` | state/foreshadowing-implementation.yaml |
| `22-49_EPISODE_FULL_DRAFT.md` | drafts/episodes/ （**bible から剥がす**） |
| `25_REVIEW_OPERATIONS_AND_GATES.md` | reviews/ + .claude/rules/ に分割 |
| `26_CANON_PATCH_LOG.md` | state/canon-patch-log.yaml |
| `27_CONTRADICTION_LOG.md` | state/contradiction-log.yaml |
| `28_REVEAL_BUDGET_SHEET.md` | bible/reveal-budget.md（**二層ファイル**: 上 Bible / 下 State） |
| `29_OBJECT_MOTIF_LADDER.md` | bible/motif-ladder.md（**二層ファイル**） |
| `50_BACKLOG_CONSTRAINT_MEMO.md` | design/design-debt.yaml |
| `23_DETAILED_DESIGN_TASK_BACKLOG.md` | backlog/ |
| `24_ACTIVE_QUEUE.md` | backlog/（active 部分のみ） |
| `53/54/55 KAKUYOMU 系` | reviews/ + .claude/rules/kakuyomu-policy.md + community/ |

#### 期待される結果

```yaml
ia_society_intake_summary:
  total_items: 86
  filled: 70
  tentative: 8
  intentionally_hidden: 4    # 湊の正体 / 兄妹の真相 等
  not_applicable: 2          # 該当なし
  contradiction: 1           # X-001 等
  needs_author_decision: 1   # AD-001
  missing: 0
  
  must_coverage: 42/42       # MUST 全達成
  
  dor_a_eligible: true（X-001 解決後）
```

### Step 4: Update Proposal 群

各 facet ごとに分割して Update Proposal を生成:

- `synthesis/update_proposals/2026-04-30_bible-world_proposal.md`
- `synthesis/update_proposals/2026-04-30_bible-characters_proposal.md`
- `synthesis/update_proposals/2026-04-30_bible-timeline_proposal.md`
- ... 計 17 facet 分

各 Update Proposal は 1 facet 内のみ扱い、author が facet 単位で承認 / 却下できるようにする。

---

## 9. 不変条件（まとめ）

1. **本書の項目を勝手に増やさない** — 追加は canon patch 相当の手続きを要する
2. **Adapter は raw を bible に直接書かない** — 必ず Update Proposal を経る
3. **contradiction を Adapter が勝手に解消しない**
4. **intentionally_hidden を bible 本文に書かない** — kernel.information_design.intended_unknowns のみ
5. **missing を勝手に intentionally_blank に降格しない** — author confirm 必須
6. **作品固有 facet は本書のチェック対象外** — 各 work が独自に追加する
7. **本書は Intake 完了判定のみ**。drafting 開始の DoR-B は別書（06_bible_dor.md）

---

## 10. 関連参照

- **使い方の流れ**: `04_pipeline_overview.md` Phase 1
- **物理配置**: `03_storage_trinity.md`
- **用語の正本**: `02_domain_model.md`
- **DoR-A の完全条件**: `06_bible_dor.md`
- **本書を機械的に回す prompt**: `../../adapter/review_prompts/intake-coverage-review.md`
- **3 作品での試走結果**: `08_pilot_validation/`
