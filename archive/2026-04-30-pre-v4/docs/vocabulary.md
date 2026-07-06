# 統一語彙表

> 1 概念 = 1 正式語。同義語禁止。混同しやすい語は別物として明示分離。
> 詳細は `../../story-template for TAKT/proposals/2026-04-29-domain-kernel-v3/01_vocabulary.md`

---

## メタ語（リポジトリ・運用）

| 正式語 | 実装語 | 一行定義 |
|---|---|---|
| Story Template | story-template | 物語制作の正本ディレクトリ集合 |
| Work | work | 1 個の作品。1 work = 1 ディレクトリ |
| Layer | layer | 0 (Intake) / 1 (Core) / 1.5 (Adapter) / 2 (Review) / 3 (Craft) / 4 (Release) / R (Runtime) |
| Adapter | adapter | kernel + state → workflow 入力への変換層。Intake / Writing の 2 種 |

---

## 物語の核（Layer 1 kernel）

| 正式語 | 実装語 | 一行定義 |
|---|---|---|
| Premise | premise | 作品の 1〜2 文要約 |
| Promise | reader_promise | 読者への約束（3〜5 項目） |
| Protagonist Vector | protagonist_vector | 主人公の want / need / wound |
| Conflict | conflict | external / internal / relational |
| Stakes | stakes | 失敗時の損失 |
| Change Model | change_model | growth / fall / flat / circular / mixed |
| Causality | causality | 時間順・知識状態の単調性方針 |
| Information Design | information_design | must_be_clear / intended_unknowns |
| Emotional Arc | emotional_arc | 感情曲線・cadence |
| Style Voice | style_voice | POV / tense / register |
| Unit Tree | unit_tree | Manuscript/Part/Arc/Packet/Episode 構造計画 |

---

## 構造単位（Layer 1）

| 正式語 | 実装語 | 一行定義 |
|---|---|---|
| Manuscript | manuscript | 作品全体 |
| Part | part | 第一部・第二部 |
| Arc | arc | Part 内の中規模・複数 Packet |
| Packet | packet | 章束・複数 Episode |
| Episode | episode | 1 話・公開単位 |
| Scene | scene | Episode 内局所衝突・複数 Beat |
| Beat | beat | 最小 story moment |

> Chapter は内部禁止。公開表示にのみ可。

---

## 設定群（Layer 1 + 周辺）

| 正式語 | 一行定義 |
|---|---|
| Bible | 安定設定の索引（書く前に決まる） |
| Genre Overlay | ジャンル固有制約 |
| Project Override | 作品固有の例外・美学（最強拘束） |
| Foreshadowing Map | 設計時の伏線配置 |
| Reveal Plan | 開示順設計 |
| Cadence Plan | 緊張弛緩リズム |

---

## 接合・実行（Layer 1.5 + R）

| 正式語 | 一行定義 |
|---|---|
| Intake Adapter | 自由 chat / raw → bible/design/state 更新案 |
| Writing Adapter | bible/state → 1 episode 用 Writing Pack |
| Scene Card | 1 episode の場面設計 |
| Acceptance Contract | judge 用合格基準 |
| Judge | acceptance_contract 充足判定 |
| Persona | TAKT エージェント役割 |
| Run | TAKT 実行履歴 |

---

## レビュー（Layer 2）

| 正式語 | 一行定義 |
|---|---|
| Typed Review | 25 項目 rubric 全埋め総合レビュー |
| Bridge Review | packet 切替の継ぎ目 |
| Continuity Review | 時系列・知識状態の連続性 |
| Persona Review | 没入 A / 構造 B / 離脱 C の 3 視点 |
| Packet Freeze Review | 凍結判定 |
| Approval Review | 公開前最終 |
| Rubric | 25 項目評価軸 |

> `Review` 単独使用禁止。必ず種別を付ける。

---

## 状態管理（Layer 1 + R）

| 正式語 | 一行定義 |
|---|---|
| Ledger | 制作中の真実台帳（執筆中に動く） |
| Continuity | 連続性の概念 |
| Patch | bible 改訂提案 |
| Design Debt | 構造的負債 |
| Open Question | 未決論点 |

> **Bible** = 書く前の安定設定 / **Ledger** = 書きながら更新 / **Continuity** = レビュー視点。3 つは別物。
> **Foreshadowing Map** = 設計意図 / **Ledger.foreshadowing_status** = 実装状況。別物。

---

## ノウハウ（Layer 3）

| 正式語 | 一行定義 |
|---|---|
| Craft | 作品不問の創作原理（常設道具箱） |
| Framework | 既存の創作フレームワーク（lens 化） |
| Framework Lens | framework の一時適用視点 |
| Motif | 作品固有の反復モチーフ |

> Craft = 常設 / Framework = 一時 lens。境界明示。

---

## 混同警告（同じ語が違う意味）

| 単語 | 区別 |
|---|---|
| Scene / Scene Card | story unit / 設計成果物 |
| Draft | 状態名のみ。単位名禁止 |
| Chapter | 内部禁止、公開表示のみ |
| Review | 単独禁止、typed/bridge/... を付ける |
| Bible | 安定設定 / 神格化禁止の比喩 |
| Persona | reader_persona / TAKT persona は別物 |
| Want, Need | kernel 項目（一般用語と区別） |

---

## 禁止語

bundle / chapter（内部） / backlog（intake として） / draft（単位として） / review（単独） / 「最強テンプレ」

---

## 詳細

完全版・サンプル・遷移ルール等は v3 `01_vocabulary.md` 参照。
