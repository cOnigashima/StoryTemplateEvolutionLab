# 統一語彙表 v3

> **目的**: Pack A / Pack B / TAKT で揺れていた用語を 1 セットに固定する。1 概念 = 1 正式語。同義語禁止。混同しやすい語は別物として明示分離する。
> **ガチガチ度**: 本 v3 で固定。以降のセッション・作品・ドキュメントは本表に従う。
> **変更ルール**: 用語追加・改名は author 承認 + `08_open_questions.md` 経由のみ。

---

## 0. 表の読み方

| 列 | 意味 |
|---|---|
| 正式語 | 公式に使う唯一の語。これ以外は禁止 |
| 実装語 | コード／ファイル名で使う英語表現 |
| Layer | 帰属する Layer（→ `03_layer_facet_map.md`） |
| 一行定義 | この概念が指すもの |
| 出典 | Pack A / Pack B / TAKT / 本 v3 新設 |

---

## 1. 設計レイヤ語彙（メタ）

| 正式語 | 実装語 | Layer | 一行定義 | 出典 |
|---|---|---|---|---|
| Story Template | story-template | meta | 物語制作の正本ディレクトリ集合 | A |
| Story Template Repository | template-repo | meta | Story Template を実装した git リポジトリ。新規作品はここから派生する | 本 v3 |
| Work | work | meta | 1 個の作品。1 work = 1 ディレクトリ。Story Template を init して作る | 本 v3 |
| Pack | pack | meta | 提案書群を束ねた discrete な改善案。`proposals/{date}-{slug}/` 形式 | A |
| Layer | layer | meta | 0 (Intake) / 1 (Core Authoring) / 2 (Review) / 3 (Craft) / 4 (Release) / R (Runtime) | A |
| Facet | facet | meta | TAKT prompt の独立側面。persona / policy / knowledge / instruction の 4 種 | TAKT |

---

## 2. 物語の中身語彙（Layer 1 Core Authoring）

### 2.1 作品全体の核

| 正式語 | 実装語 | Layer | 一行定義 | 出典 |
|---|---|---|---|---|
| Premise | premise | 1 (kernel) | 作品を 1〜2 文で言う最小要約。誰が何をする話か | A/B |
| Promise | reader_promise | 1 (kernel) | 読者に対する明示的・暗示的な約束。3〜5 項目 | A |
| Protagonist Vector | protagonist_vector | 1 (kernel) | 主人公の want / need / wound (or misbelief) の 3 ベクトル | B |
| Want | want | 1 (kernel) | 主人公が表面で追っている目標。物語の駆動力 | B+craft |
| Need | need | 1 (kernel) | 主人公が深層で必要としているもの。キャラアークの帰着点 | B+craft |
| Wound | wound | 1 (kernel) | 主人公の傷・誤信念。need を埋める障害となる過去 | B |
| Conflict | conflict | 1 (kernel) | 中核対立。external / internal / relational の 3 軸 | A/B |
| Stakes | stakes | 1 (kernel) | 失敗時に何が失われるか。読者の関心を支える | B |
| Change Model | change_model | 1 (kernel) | キャラアークの形（成長 / 堕落 / 不変 / 円環）と変化の方向 | B |
| Causality | causality | 1 (kernel) | 時間順と因果順、知識状態の単調性に関する作品方針 | A+drafter-preflight |
| Information Design | information_design | 1 (kernel) | 何を読者に開示し、何を意図的に隠すか。must_be_clear / intended_unknowns | B |
| Emotional Arc | emotional_arc | 1 (kernel) | 作品全体の感情曲線 | B |
| Style Voice | style_voice | 1 (kernel) | POV / 時制 / 一人称か三人称か / 文体の温度 / 一文の長さ | A+B |
| Unit Tree | unit_tree | 1 (kernel) | この作品の Manuscript / Part / Arc / Packet / Episode 構成計画 | B |

### 2.2 設定群

| 正式語 | 実装語 | Layer | 一行定義 | 出典 |
|---|---|---|---|---|
| Bible | bible | 1 | 作品の安定設定の索引。`bible/world.md`, `characters.md`, `rules.md` ほか | A |
| World | world | 1 | 世界観・地理・歴史・社会システム | A |
| Character | character | 1 | 登場人物の設定。声・関係・背景 | A |
| Rules | rules | 1 | 文体ルール・禁則・固有制約 | A |
| Genre Overlay | genre_overlay | 1 | ジャンル固有の約束・チェックリスト。kernel と分離する | B |
| Project Override | project_override | 1 | この作品固有の例外・美学・方針。Genre Overlay より強い | B |

### 2.3 構造単位（→ 詳細は `02_unit_taxonomy.md`）

| 正式語 | 実装語 | Layer | 一行定義 | 出典 |
|---|---|---|---|---|
| Manuscript | manuscript | 1 | 作品全体 | B |
| Part | part | 1 | 第一部・第二部などの大区分 | B |
| Arc | arc | 1 | Part 内の中規模まとまり。複数 Packet からなる | A/B |
| Packet | packet | 1 | 章束。複数 Episode の制作・レビュー単位 | A/B |
| Episode | episode | 1 | 1 話。本文候補を作る基本単位。公開単位 | B |
| Scene | scene | 1 | Episode 内の局所衝突単位。複数 Beat からなる | A |
| Beat | beat | 1 | 最小の story moment。Scene を構成する単位 | craft |

### 2.4 設計成果物

| 正式語 | 実装語 | Layer | 一行定義 | 出典 |
|---|---|---|---|---|
| Scene Card | scene_card | 1 | 1 Episode を書くための設計カード。Adapter の主出力 | B |
| Acceptance Contract | acceptance_contract | 2 | judge が判定するための合格基準。Episode ごとに発行 | B |
| Judge Contract | judge_contract | 2 | judge の判定ロジック。PASS / FAIL_AUTO_FIX / NEEDS_HUMAN / REJECT_AND_REGENERATE | B |
| Foreshadowing Map | foreshadowing_map | 1 | 設計時の伏線配置計画。**意図** の正本 | A |
| Reveal Plan | reveal_plan | 1 | fabula（時間順事実）と syuzhet（提示順）の対応表 | A+craft |
| Cadence Plan | cadence_plan | 1 | packet 単位の緊張弛緩リズム計画（基準 6:4） | A |
| Reader Persona | reader_persona | 2 | レビュー視点の架空読者。A 没入 / B 構造 / C 離脱 | A |

### 2.5 本文・実装

| 正式語 | 実装語 | Layer | 一行定義 | 出典 |
|---|---|---|---|---|
| Draft | draft | 1 | 本文の状態名（**単位名ではない**）。Episode draft / Packet draft 等 | B |
| Prose | prose | 1 | 散文本文そのもの。draft の中身 | A |
| Candidate | candidate | R | 1 つの Episode に対する複数 writer による draft 候補のうち 1 本 | B |
| Selection Report | selection_report | R | 候補から base draft 選定と借用要素を整理した報告 | B |
| Integrated Draft | integrated_draft | R | selection-synthesis を経て reviser が一本化した本文 | B |

---

## 3. 入力フロー語彙（Layer 0 Intake）

| 正式語 | 実装語 | Layer | 一行定義 | 出典 |
|---|---|---|---|---|
| Intake | intake | 0 | 大量入力を受け止めて精製していく入口層 | A |
| Raw | raw | 0 | 長文・会話ログ・設定投下の原文。`story/intake/raw/` | A |
| Digest | digest | 0 | raw を batch 圧縮した中間サマリ。`story/intake/digests/` | A |
| Seed | seed | 0 | 再利用可能な核に切り出された設計種。`story/seeds/` | A |
| Domain Synthesis | domain_synthesis | 0 | 自由 chat を構造化する処理。confirmed / tentative / open / contradiction / decision_needed に分類 | B |
| Reflection Ledger | reflection_ledger | 0 | 反映完了 / 却下 / 棚卸し履歴を追う台帳。`story/intake/reflection-ledger.md` | A |
| Provenance Index | provenance_index | 0 | raw → digest → seed → canon の継承を追う YAML 索引 | A |

> **注意**: Pack B の `Domain Synthesis` は freeform chat の構造化、Pack A の `Digest` は raw の batch 圧縮。**両者は別物**。Domain Synthesis は会話を構造化、Digest は記録物を圧縮。本 v3 では両方並存。

---

## 4. 接合・実行語彙（Layer R Runtime + 接合面）

| 正式語 | 実装語 | Layer | 一行定義 | 出典 |
|---|---|---|---|---|
| Adapter | adapter | 1.5 | kernel + bible + framework lens + ledger から scene_card / acceptance_contract / judge_contract を生成する変換層 | B |
| Workflow | workflow | R | TAKT で実行する制作ライン。episode-draft-tournament 等 | TAKT/B |
| Step | step | R | TAKT workflow の単一実行単位。persona + policy + knowledge + instruction の 4 facet を組み合わせる | TAKT |
| Persona | persona | R | エージェントの役割定義。faithful_writer / emotional_writer / reviser / judge 等 | TAKT/B |
| Routing Rule | routing_rule | R | TAKT step の `condition → next` 分岐 | TAKT |
| Run | run | R | workflow 1 回の実行履歴。`.takt/runs/` に NDJSON で残る | TAKT |
| Task | task | R | TAKT に積まれる仕様 yaml。`.takt/tasks/` | TAKT |
| Repertoire | repertoire | R | TAKT の外部パッケージ配布形式。Story Template を repertoire 化して新規作品に init する | TAKT |

---

## 5. レビュー語彙（Layer 2 Review-Learning）

| 正式語 | 実装語 | Layer | 一行定義 | 出典 |
|---|---|---|---|---|
| Review | review | 2 | （単独使用禁止。typed / bridge / continuity / persona / freeze / approval のいずれかを必ず付ける） | A |
| Typed Review | typed_review | 2 | 25 項目 rubric を全埋めする総合レビュー | A |
| Bridge Review | bridge_review | 2 | packet 切替の継ぎ目を見るレビュー | A |
| Continuity Review | continuity_review | 2 | 時系列・知識状態・物的証拠の連続性を見るレビュー | A |
| Persona Review | persona_review | 2 | A 没入 / B 構造 / C 離脱の 3 視点で読むレビュー | A |
| Packet Freeze Review | freeze_review | 2 | packet を frozen 状態に進めてよいか判定するレビュー | A |
| Approval Review | approval_review | 2 | 公開前の最終チェック。kakuyomu policy 適合含む | A |
| Rubric | rubric | 2 | 25 項目の評価軸（G1-G3 hard gate / M1-M6 文体 / D1-D4 対話 / S1-S6 構成 / F1-F3 伏線 / C1-C2 キャラ / W1-W2 世界） | A |
| Judge | judge | R | 自動品質ゲート。Acceptance Contract に照らして PASS/FAIL_AUTO_FIX/NEEDS_HUMAN/REJECT_AND_REGENERATE を返す | B |

> **重要**: `Review` は人間 reviewer が読む批評ドキュメント、`Judge` は自動ゲート。**両者は別物**。同じ rubric を共有することはあるが、出力形態と消費者が違う。

---

## 6. 状態管理語彙（Layer 1 + Layer 2 跨ぎ）

| 正式語 | 実装語 | Layer | 一行定義 | 出典 |
|---|---|---|---|---|
| Ledger | ledger | 1+R | 制作中の真実台帳。canon_facts / timeline / character_states / foreshadowing_status / open_questions / author_decisions / rejected_ideas | B |
| Continuity | continuity | 2 | 連続性の概念そのもの。Continuity Review はこれを検査する | A |
| Patch | patch | 1 | bible への変更提案。`story/canon-patch-proposals/` | A |
| Design Debt | design_debt | 1 | 構造的な未解決問題の負債台帳。`story/design-debt.yaml` | A |
| Open Question | open_question | 1 | まだ決まっていない論点。`story/open-questions.md` | A |

> **重要**: `Bible` は安定した源典設定（書く前に決める）、`Ledger` は実装中に発生する状態（書きながら更新する）、`Continuity` はレビュー時にこの 2 つの整合を見る視点。**3 つは別物**。

> **重要**: `Foreshadowing Map`（設計意図）と `Ledger.foreshadowing_status`（実装状況）は別物。設計時に Map に置き、書きながら Ledger でステータス更新。

---

## 7. ノウハウ語彙（Layer 3 Craft）

| 正式語 | 実装語 | Layer | 一行定義 | 出典 |
|---|---|---|---|---|
| Craft | craft | 3 | 作品不問の創作原理。Scene/Sequel・Want/Need・Beat sheets 等。常設の道具箱 | A |
| Craft Library | craft_library | 3 | craft の正典置場。`craft/` ディレクトリ | A |
| Framework | framework | 3 | 既存の創作フレームワーク（三幕構成・Snowflake・Story Grid・Hero's Journey 等） | B |
| Framework Index | framework_index | 3 | framework のカタログ。「いつ使うか」「何を見るか」のメタ情報付き | B |
| Framework Lens | framework_lens | 3 | framework を一時適用する視点。常設しない | B |
| Motif | motif | 1 | 作品固有の反復モチーフ。3/5 段階運用 | A+craft |
| Motif Operations | motif_operations | 3 | motif の運用原理（generic）。craft library 内 | A |

> **境界**: `Craft` は常設の道具箱（読まれる前提）、`Framework` は適用案件ごとに lens として呼ぶ（読まれない前提）。**両者は別物**。Framework が常設化したら Craft に昇格、Craft が作品固有に堕ちたら作品 bible に降格。

---

## 8. 公開語彙（Layer 4 Release）

| 正式語 | 実装語 | Layer | 一行定義 | 出典 |
|---|---|---|---|---|
| Approved | approved | 4 | 公開承認済の本文。`approved/` | A |
| Published | published | 4 | 公開済の本文。`published/` | A |
| Kakuyomu Policy | kakuyomu_policy | 4 | カクヨム公開時の制約。AI タグ・頻度・禁則 | A |
| AI Tag | ai_tag | 4 | カクヨムの AI 利用タグ（AI本文利用 / 一部利用 / 補助利用） | A |

---

## 9. 状態値語彙（→ 詳細は `05_status_vocabulary.md`）

| 正式語 | 実装語 | 範疇 | 一行定義 |
|---|---|---|---|
| filled | filled | field status | 値が入っている |
| missing | missing | field status | 値が空で、本来埋まるべき |
| tentative | tentative | field status | 値はあるが暫定 |
| deferred | deferred | field status | 後で埋める予定 |
| intentionally_blank | intentionally_blank | field status | 意図的に空 |
| intentionally_hidden | intentionally_hidden | field status | 値は決まっているが読者非開示 |
| not_applicable | not_applicable | field status | 本作には該当しない |
| genre_not_applicable | genre_not_applicable | field status | このジャンルには該当しない |
| project_override | project_override | field status | 作品固有方針で kernel 推奨を上書き |
| contradiction | contradiction | field status | 別フィールドと矛盾している |
| needs_author_decision | needs_author_decision | field status | author 判断が必要 |
| PASS | pass | judge | 公開可 |
| FAIL_AUTO_FIX | fail_auto_fix | judge | 自動修正で通せる |
| NEEDS_HUMAN | needs_human | judge | 人間判断が必要 |
| REJECT_AND_REGENERATE | reject_and_regenerate | judge | 候補を捨てて再生成 |
| soft_lock | soft_lock | lock | Episode 単位の暫定確定 |
| packet_soft_lock | packet_soft_lock | lock | Packet 単位の暫定確定 |
| hard_lock | hard_lock | lock | author 承認後の確定 |

---

## 10. 同じ単語が違う意味を持つ語（混同警告）

以下は **意識的に区別** する。混同したら本 v3 違反。

| 単語 | 意味 A | 意味 B | 区別 |
|---|---|---|---|
| Scene | Episode 内の局所衝突単位（story unit） | scene_card という設計成果物 | story unit を `Scene`、設計成果物を `Scene Card` と呼ぶ |
| Draft | 本文の状態名 | （Pack A 旧用法）原稿全体 | **状態名のみ**。原稿の単位名としては禁止 |
| Chapter | 公開時の表示用区切り | 内部制作単位 | **内部単位として禁止**。公開表示のみ可 |
| Review | typed/bridge/continuity/persona/freeze/approval のいずれか | 一般的な「批評」 | **単独使用禁止**。必ず種別を付ける |
| Bible | 作品源典設定（安定） | 「神聖視できない物」の比喩 | 前者のみ。Pack B `05_storytemplate_integration_guide` の「神格化しない」は後者の用法を否定する文 |
| Foreshadowing | 伏線そのもの | foreshadowing_map（設計意図）/ ledger.foreshadowing_status（実装状況） | 前者は概念、後の 2 つは管理台帳。台帳を指すときは必ず full name |
| Promise | reader_promise（kernel 項目） | 一般用語の「約束」 | **正式語は kernel 項目を指す**。一般用語と区別したいときは `reader_promise` |
| Want | want（protagonist_vector の表面動機） | 一般用語の「欲しい」 | 前者のみ。kernel 項目 |
| Need | need（protagonist_vector の深層動機） | 一般用語の「必要」 | 前者のみ。kernel 項目 |
| Persona | reader_persona（レビュー視点） | TAKT persona（エージェント役割） | 前者は読者視点、後者は AI 役割。**完全に別物**。コンテキストで判別。曖昧な場合は full name |
| Run | TAKT 実行履歴 | 一般用語の「走る」 | 正式語は TAKT 実行履歴。一般動詞用法は文中で許容 |

---

## 11. 禁止語（使用しない）

| 禁止語 | 理由 | 代替 |
|---|---|---|
| bundle | packet と紛らわしい | packet |
| chapter（内部単位として） | episode/packet/arc と曖昧化 | episode / packet / arc を文脈で使い分け |
| backlog（intake として） | legacy 資産の名残 | intake / seeds |
| review（単独） | 種別が曖昧 | typed_review / bridge_review / continuity_review / persona_review / freeze_review / approval_review |
| draft（単位名として） | 状態名なのに単位扱いされる | 単位は episode / packet / arc、状態は draft |
| 文章片を借りる | borrow は設計意図ベース | 設計意図を借りる |
| 最強テンプレート | 思想に反する | 適切な lens 選択 |
| AI 自動執筆 | 法務・倫理・ポリシーで誤解を生む | AI 本文利用（kakuyomu 用語） |

---

## 12. 注意語（使用時に文脈明示）

| 注意語 | 注意点 |
|---|---|
| story | `story/` ディレクトリと一般語の「物語」の両方で使う。ディレクトリ参照は必ず `story/` プレフィクス |
| design | 一般語として広い。具体化すべき場面では `design_debt` `design_overview` のように接尾辞で区別 |
| context | 「文脈」と「TAKT context」を区別。TAKT 文脈なら `task_context_pack` |
| state | 「状態」「state machine の state」「ledger の state」がある。必ず修飾 |
| patch | `bible patch` / `canon patch` / 一般 patch を区別 |

---

## 13. 用語追加・改名の手順

1. `08_open_questions.md` に新語の必要性を記述
2. author に承認を依頼
3. 承認後、本 `01_vocabulary.md` の該当セクションに追記
4. 同セッション中で関連する他ファイルにも反映
5. 既存の同義語があれば「禁止語」表に移動

---

## 14. Pack A / Pack B との対応

本 v3 で固定した語彙が、Pack A / Pack B のどの語をどう吸収したか:

### Pack A から継承

- 4+1 Layer / Intake 5 段 / Review Matrix 6 種 / Craft / Patch / Design Debt / Bible / Promise / Foreshadowing Map / Cadence Plan

### Pack B から継承

- Episode / Packet / Arc / Part / Manuscript / Adapter / Ledger / Acceptance Contract / Judge / Domain Synthesis / Framework Index / Framework Lens / Status 11 種 / Judge 4 値

### 衝突解決

- Pack A の `Scene`（Episode 内 unit） vs Pack B の `Scene Card`（設計成果物） → **両方残す**。前者は story unit、後者は design artifact
- Pack A の `Bible/Foreshadowing Map`（設計） vs Pack B の `Ledger`（実装） → **両方残す**。設計と実装を分離管理
- Pack A の `Craft Library`（常設） vs Pack B の `Framework Index`（一時 lens） → **両方残す**。Craft は generic 原理、Framework は genre/method 別 lens
- Pack A の typed `Review`（人間 reviewer） vs Pack B の `Judge`（自動ゲート） → **両方残す**。同じ rubric を別出力で消費
- Pack A の `Packet`（章束） + Pack B の `Episode/Packet/Arc/Part` → Pack B 寄せ。Pack A の packet=章束 を継続使用

### TAKT から導入

- Persona / Facet（persona/policy/knowledge/instruction）/ Step / Routing Rule / Run / Task / Repertoire

### 本 v3 で新設

- Story Template Repository / Work / Pack（メタ語）/ Lock 状態（soft / packet_soft / hard）/ Layer 1.5（Adapter の所属層）

---

## 15. 索引

頻出参照が必要なときの一行ガイド:

- 「kernel に何が入る?」→ §2.1 と `04_kernel_spec.md`
- 「単位の入れ子は?」→ §2.3 と `02_unit_taxonomy.md`
- 「Bible と Ledger の違いは?」→ §6 + 注意書き
- 「Review と Judge の違いは?」→ §5 + §10
- 「Craft と Framework の違いは?」→ §7 + 境界注
- 「禁止語は?」→ §11
- 「曖昧語は?」→ §10 + §12
