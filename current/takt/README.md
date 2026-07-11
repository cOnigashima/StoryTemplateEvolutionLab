# takt — ループエンジニアリング実装（初見向け・二確用）

> **STATUS: 暫定（PROVISIONAL）。** TAKT部分は別セッションで詰める。ここの workflow / facet は
> 「こう組めるはず」という叩き台で、正本として未確定。確定するまで参考実装として扱う。

TAKT が初めてでも、ここを読めば「何のためか / どう回るか / どう叩くか」が分かるように書く。

---

## 1. TAKTとは（30秒）

TAKT = AIエージェントの**オーケストレーションOSS**（nrslib製、`npm install -g takt`）。
思想は **「AIの見張り番をやめる」= 決定権をAIから workflow に移す**。
「書く→検査する→レビューする→直す」の流れを YAML で宣言し、AIがその流れに**従わざるを得ない**ようにする。レビューを"お願い"でなく"仕組み"で強制する。

なぜ効くか: 同じAIの自己レビューは自己強化バイアスで甘くなる。役割(persona)を分け、時にモデルも分けることで、取りこぼしを減らす。

---

## 2. StoryTemplate 運用でTAKTが担うもの

CLAUDE.md の「人間は成果物だけ見る」を実現する実行エンジン。
- 途中の判断（draft→検査→レビュー→修正）は workflow が自動で回す。
- 堂々巡りは `loop_monitors` が検出して打ち切る。
- 人間が止まるのは `deliverables/` に成果物が出た時だけ（G-Deliverable）。

---

## 3. 4つの概念（これだけ覚える）

| 概念 | 意味 | 作品ワークスペースでの置き場 |
|---|---|---|
| **workflow** | 仕事の流れ全体（YAML）。step の連なり | `workflows/*.yaml` |
| **step** | 1工程。persona・edit権限・遷移rule を持つ | workflow内 |
| **facet** | プロンプトを関心事で分解した部品（下記5種） | `facets/*/` |
| **run** | workflowの実行1回。ログとレポートが残る | `../logs/runs/` |

### 5 facet（Faceted Prompting）
| facet | 定義するもの | 小説での例 |
|---|---|---|
| Persona | 役割・専門性 | 著者 / レビュアー / 編集者 |
| Policy | 規約・品質基準・禁止 | style_voice・禁則・review-gate |
| Instruction | そのstepの手順 | 「この話をdraftせよ」 |
| Knowledge | 参照する知識 | bible・Writing Pack・ontology抽出 |
| Output Contract | 出力フォーマット | draft形式・レビュー票形式 |

facet を分けると、各stepに必要な分だけ渡せて context 肥大を防げる（context engineering）。

---

## 4. 遷移とループの仕組み

- step の `rules` に `condition`（人間可読な条件文）と `next`（次step）を書く。TAKTが出力を判定して分岐。
- 終端は `COMPLETE`（成功）/ `ABORT`（失敗）。
- `review → 修正 → review` のループは YAML に書けば**強制**される。
- `loop_monitors`: 反復が閾値（例3周）を超えたら supervisor が「進捗しているか」を評価し、堂々巡りなら ABORT（`loop_monitors.md` 参照）。
- 前step出力は `{previous_response}`、元タスクは `{task}` で次stepに自動注入。

---

## 5. 叩き方（基本コマンド）

```bash
npm install -g takt          # 初回のみ
# 初回に対話で provider/model/language を設定 → config.yaml 生成
takt                         # 対話モードで計画を詰める → /go で実行
takt run                     # tasks に積んだタスクを自律実行
takt -w draft-episode "ep005を書く"   # workflow を指定して実行
takt list                    # takt が作ったブランチ確認
```

- `config.example.yaml` を `config.yaml` にコピーして provider/model を設定。
- step ごとに model を変えられる（設計=上位モデル / 実装=標準 / レビュー=別系統でクロスレビュー）。

---

## 6. 同梱の workflow

| workflow | 何をするか | 人間ゲート |
|---|---|---|
| `workflows/draft-episode.yaml` | Writing Pack → draft → ontology_check → self-review → 修正ループ | 出力後 G-Deliverable |
| `workflows/review-multipass.yaml` | typed review + persona 2ラウンド → 採否判定 | 出力後 G-Deliverable |
| `workflows/packet-cycle.yaml` | overlay=packet-2stage 用。freeze→dry-run→再freeze→本draft | freeze前/後 |

---

## 7. 注意（TAKTを過信しない）

- **最終レビューの人間判断は自動化しない**（作者本人が `deliverables/` を見る）。
- validator/loop_monitor は warning 主体。creativeな例外を機械が握りつぶさない。
- workflow は最初は単純に。重装より「動く最小」を組み合わせる。
