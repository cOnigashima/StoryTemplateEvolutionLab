# 大量インプット受け入れフロー

本ファイルは **テーマ 1「大量インプットの受け入れ」** の設計。ChatGPT Pro など別環境で生成された大量の設計メモ・調査結果・ブレスト・プロンプト結果を、漏れなく Story OS に流し込み、必要部分を canon 化するまでの経路を定義する。

既存の `reviews/2026-04-18-story-template-intake-integration-proposal.md`（399 行）を下敷きに、運用細部・prompt 骨格・自動化ポイントを足す。

---

## 1. 5 層アーキテクチャ（再整理）

```
Layer A — Source Intake             story/intake/raw/
                                    story/intake/raw-index.yaml        (new)
                                    story/intake/provenance.yaml       (new)
     │
     ▼  batch 圧縮（手順化 prompt）
Layer B — Digest                    story/intake/digests/
                                    story/intake/digest-index.yaml     (new)
     │
     ▼  seed 抽出（再利用核へ切る）
Layer C — Reusable Seed             story/seeds/seed-NNN-{slug}.md
                                    story/seeds/seed-index.yaml        (new)
     │
     ▼  seed-to-macro review（reviews/seed-to-macro-template.md）
Layer D — Stable Canon / Live Impl  story/promises.md / bible / arcs / packets / scenes / drafts
     │
     ▼  反映完了 or 未反映を記録
Layer E — Reflection Ledger         story/intake/reflection-ledger.md  (new)
                                    story/canon-patch-proposals/
                                    story/design-debt.yaml
                                    story/open-questions.md
```

---

## 2. 各層の定義と運用

### 2.1 Layer A — Source Intake (raw)

**目的**: 入力の原文を失わないこと。文脈を失ったら digest からは復元できない。

**配置**:
- `story/intake/raw/YYYY-MM-DD-{source}-{slug}/` をディレクトリ単位で切る
- 単発なら `story/intake/raw/YYYY-MM-DD-{slug}.md` 単ファイル
- Pro 画像、pdf、csv 等は同ディレクトリに `attachments/` を作って同梱

**記録**: 各 raw 投入時に `story/intake/raw-index.yaml` に 1 行追加する

```yaml
# story/intake/raw-index.yaml
entries:
  - id: raw-20260422-pro-arc02-worldbuilding
    date: 2026-04-22
    source: chatgpt-pro
    model: gpt-pro-research
    prompt_ref: prompts/intake/pro-arc02-worldbuilding.md
    path: story/intake/raw/2026-04-22-pro-arc02-worldbuilding/
    size_bytes: 184213
    topics: [arc-02, world, magic_system, antagonist]
    digest_status: pending
    seed_candidates: []
    notes: |
      Pro 対話 3h、arc-02 の魔法系再設計 + 敵役背景を中心にまとめ上げ。
```

**禁止**:
- raw を `bible/` や `arcs/` に直接書き込む
- raw を要約せずに seeds へ昇格する

**provenance 初記録**: `story/intake/provenance.yaml` にも同時に 1 行追加

```yaml
# story/intake/provenance.yaml
records:
  - id: raw-20260422-pro-arc02-worldbuilding
    origin_type: raw
    path: story/intake/raw/2026-04-22-pro-arc02-worldbuilding/
    descendants: []   # digest / seed / canon への反映が進むと追記
```

### 2.2 Layer B — Digest

**目的**: raw を「batch 単位の要約」に圧縮する。後段で seed を切る際の地図。

**配置**: `story/intake/digests/YYYY-MM-DD-{source}-{slug}.md`（原則 1 ファイル）

**digest テンプレ**（新設 `story/intake/digests/digest-template.md`）:

```markdown
# Digest: {slug}

> raw: story/intake/raw/...
> 日付: YYYY-MM-DD
> 担当: {human or agent name}
> 所要時間: N 時間

## 1 行要約
（この batch 全体を 1 行で）

## topics（3〜7 個）
- topic-1: ...
- topic-2: ...

## 収穫
- 使える核 × N 件
- 問い（未決定）× N 件
- 反証・矛盾 × N 件（既 canon との衝突）

## 収穫一覧（seed 候補）
| # | slug | topic | 一言要約 | 反映先仮候補 | 優先度 |
|---|---|---|---|---|---|
| 1 | seed-00X-... | arc-02 | ... | bible/world.md §魔法系 | 高 |

## 捨てる判断
（意図的に seed 化しない raw 内容。理由も記す）

## 未解決論点
（seed にもならないが保留する問い。`story/open-questions.md` 候補）
```

**digest-index.yaml**（新設）: digest 1 本毎に 1 エントリ。seed 候補の id を cross-link。

### 2.3 Layer C — Seed（再利用核）

**目的**: macro（promises/bible/arcs）や meso（packets/scenes）に昇格させる候補のユニット化。

**配置**: 既存 `story/seeds/seed-NNN-{slug}.md`

**seed テンプレ**（既存あるはず。無ければ作る）:

```markdown
# seed-NNN-{slug}

> 出自: digests/{path}
> raw: raw-index.yaml の entry id
> 起票: YYYY-MM-DD
> 反映候補先: [promises / bible/world / bible/characters / arcs/arc-NN / packets/... / design-debt / open-questions]

## 内容（2〜5 段落）

## なぜ残すか（再利用性）

## 反映先整理（seed-to-macro-template.md を使って更新）
- promises: yes / no / partial（理由）
- bible/world: ...
- arcs/arc-NN: ...
- packets: ...
- design-debt / open-questions: ...

## ステータス
- [ ] seed-to-macro review 完了
- [ ] 反映済み（反映先ファイルと commit への link）
- [ ] 却下（理由は design-debt / open-questions へ）
```

**seed-index.yaml**（新設）: seed 1 本毎に状態を一覧。

### 2.4 Layer D — Stable Canon & Live Implementation

**目的**: seed から昇格した情報を正本へ定着させる。

**昇格手順**:
1. seed の `反映候補先` を元に `reviews/seed-to-macro-template.md` を埋める
2. reviewer（人間 or critic agent）が承認
3. 反映先ファイルに書き込む。**書き込み時に provenance 記録を更新**
4. 該当 canon 要素の YAML front-matter or 末尾脚注に `provenance: seed-NNN-{slug}` を残す

**provenance 更新（反映完了時）**:
```yaml
# provenance.yaml の当該 raw レコードに descendants を追加
records:
  - id: raw-20260422-pro-arc02-worldbuilding
    descendants:
      - digest: digests/2026-04-22-pro-arc02-worldbuilding.md
      - seed: seeds/seed-042-magic-system-rebuild.md
      - canon:
          - file: bible/world.md
            section: §魔法系
            commit: abc1234
            date: 2026-04-25
```

### 2.5 Layer E — Reflection Ledger（反省台帳）

**目的**: 「raw で入れた要素が全部反映先にたどり着いたか」を横断で追う。漏れの検出。

**配置**: `story/intake/reflection-ledger.md`

**構造**:

```markdown
# Reflection Ledger

> 本台帳は intake → canon までの反映状況を追う。`provenance.yaml` と併読する。

## 未反映（pending）

| raw id | digest 済み | seed 化 | 未反映理由 | 次アクション | 期限 |
|---|---|---|---|---|---|
| raw-20260422-pro-arc02-worldbuilding | ✅ | 一部 (42/55) | 13 件は反映先未定 | open-questions 起票 | 2026-04-29 |

## 却下（dropped）

| raw id / seed id | 却下理由 | 参照先 |
|---|---|---|
| seed-018-... | Promise と矛盾 | canon-patch-proposals 不採用 |

## 反映完了（done）
（直近 N 件のみ）
```

**運用**:
- digest 完了時・seed 起票時・反映完了時・却下時に必ず追記
- 週次 consolidate で「未反映」行が古くなっていないかチェック
- **未反映が設計負債化**したら `design-debt.yaml` へ移送
- **未反映が論点化**したら `open-questions.md` へ移送

---

## 3. Pro 等外部環境で使う intake 用 prompt（テンプレ）

本セクションの prompt は `prompts/intake/` に置く（新設）。

### 3.1 `prompts/intake/raw-submission.md`（Pro → ここへの投げ方）

Pro や別 Claude で研究・設計した結果を raw に入れる前に author 自身が整える作業用 prompt。

```
# Raw 投入前プリセット
ChatGPT Pro 等の出力を StoryTemplate の raw に入れる前に、以下を揃える。

1. source: どの AI / モデル / 人間会議か
2. date: 実施日
3. duration: 実施時間
4. scope: どの arc / packet / 領域（world / character / plot）が主題か
5. inputs: 投げた prompt ファイルへのリンク
6. outputs: 得た生成結果（そのまま全文保存、要約しない）
7. known_collisions: 既 canon と衝突しそうな点（気づいた範囲で）
8. 一次印象: 使えそうな核 / 捨てたい部分
```

### 3.2 `prompts/intake/digest-writer.md`（raw → digest）

```
# 役割
あなたは StoryTemplate の digest writer。raw を読み、digest-template.md の形に落とす。

# 入力
- raw path
- raw-index.yaml の該当 entry

# 出力フォーマット（digest-template.md に従う）
- 1 行要約 / topics / 収穫 / 捨てる判断 / 未解決論点

# 規則
- raw に無い事実を digest に書かない（creative embellishment 禁止）
- seed 候補の「反映先仮候補」は当該 bible/arcs/packets を検索した根拠に基づく
- 反映先不明の核は「捨てる判断」ではなく「未解決論点」に分類
- digest は prose より箇条書き中心で可（後で seed に展開される前提）
```

### 3.3 `prompts/intake/seed-extractor.md`（digest → seed）

```
# 役割
あなたは StoryTemplate の seed extractor。digest の「収穫一覧」を 1 件ずつ seed に展開する。

# 入力
- digest path
- 対象行の slug

# 手順
1. digest の該当核について、再利用性の観点で 2〜5 段落に書き起こす
2. 反映候補先を探索する（現在の promises / bible / arcs / packets を読む）
3. seed-{slug}.md に書き出す（テンプレ §2.3 参照）
4. seed-index.yaml に追加
5. reflection-ledger に「seed 化済」を記録

# 規則
- seed は「再利用核」。ある 1 回の ep でしか使えないような話はむしろ scene card 側に行くべき
- 反映候補先が 3 つ以上の macro を触る場合、seed 内で分割するか迷わず seed-to-macro-template を先に埋める
```

### 3.4 `prompts/intake/seed-to-macro-reviewer.md`（seed → canon 昇格判定）

```
# 役割
あなたは StoryTemplate の seed→macro reviewer。reviews/seed-to-macro-template.md を使い、seed を canon に昇格するか判定する。

# 入力
- seed path
- 関連 promises / bible / arcs / packets

# 手順
1. seed の主張と既存 canon の衝突点を列挙
2. 反映候補先ごとに「promote / hold / patch」を判定
3. hold / patch は理由と次アクションを明記
4. 完了後、reflection-ledger と provenance を更新
```

### 3.5 `prompts/intake/pro-research-brief.md`（Pro 研究の調査指示書）

know_how_explore `2026-04-18_ChatGPT_Pro_調査プロンプト集.md` を原型に、以下の 5 つの **事前決定**（pre-decisions）を必ず書かせる:

1. **テーマ境界** — 何の arc / packet / 概念を研究するか
2. **レイヤ** — Promise / Canon / Bible / Arc / Packet のどの層に入れるか
3. **Source 強度** — 引用必須か、合成可か、ブレスト可か
4. **成果物形式** — raw にそのまま入れる素材か、digest 形式か
5. **深さ** — 広く浅く / 狭く深く

prompt 骨格:

```
# StoryTemplate — Pro 調査指示書（ver-1）

## メタ情報
- 作品: {work slug}
- 対象: {arc / packet / 概念}
- 日付: {date}

## 5 つの事前決定
1. テーマ境界: ...
2. レイヤ: ...
3. Source 強度: ...
4. 成果物形式: ...
5. 深さ: ...

## 既 canon 抜粋（衝突検出の基礎）
（promises.md / bible/*.md / arcs/*.md の該当セクションをコピペ）

## 調査タスク
1. {tasks}

## 出力規則
- 事実と推測を分けて書く（[FACT] / [SPECULATION] ラベル）
- 既 canon との衝突は [COLLISION] ラベルで明示
- 使えそうな核は [CORE] ラベル
- 回収すべき問いは [QUESTION] ラベル

## 終了後
raw に保存する。raw-index.yaml / provenance.yaml に 1 行追加する。
```

---

## 4. 機械可読レイヤ（current-focus.yaml 等）

one-man-statefall の learning-loop を参考に、intake と同期する機械可読ファイルを template に入れる。

### 4.1 `learning/current-focus.yaml`

```yaml
# learning/current-focus.yaml
updated_at: 2026-04-22
working_arc: arc-01
working_packet: packet-003
working_ep: ep18
blockers:
  - id: blocker-arc02-magic-rebuild
    severity: high
    linked_open_question: story/open-questions.md §Q-014
    linked_raw: raw-20260422-pro-arc02-worldbuilding
focus_seeds:
  - seed-042-magic-system-rebuild
unresolved_intake_count: 13
last_review: reviews/typed-review-packet-003-ep17.md
next_job: ep18 draft with Gate 0/A/C
```

### 4.2 `drafts/packet-NNN/ep-NN/task-context.yaml`

drafter/critic が ep 着手時に参照する圧縮文脈パック。one-man-statefall `task-context.yaml` 由来。

```yaml
# drafts/packet-003/ep18/task-context.yaml
ep: ep18
packet: packet-003
focal_character: {name}
carryover_from_prev_ep: [...]
packet_requirements:
  - {requirement ids with implementation beat}
canon_motifs_active: [...]
withhold_keywords: [...]
disclose_keywords: [...]
related_foreshadow_ids: [...]
referenced_seeds: [seed-042-magic-system-rebuild]
```

---

## 5. 運用リズム（recommended）

| リズム | 内容 |
|---|---|
| 入力発生時 | raw 投入 → raw-index に 1 行 → provenance に 1 行 |
| 数時間以内 | digest に圧縮（prompt §3.2） |
| 1 日以内 | seed 候補を切る（prompt §3.3） |
| 2-3 日以内 | seed-to-macro review（prompt §3.4） |
| 週次 | reflection-ledger 棚卸し、未反映 14 日超を open-questions / design-debt へ |
| arc 完了時 | consolidate-memory skill で intake → canon の反映履歴を圧縮整理 |

---

## 6. 既存ファイルへの影響

新設:
- `story/intake/raw-index.yaml`
- `story/intake/digest-index.yaml`
- `story/seeds/seed-index.yaml`
- `story/intake/provenance.yaml`
- `story/intake/reflection-ledger.md`
- `story/intake/digests/digest-template.md`
- `prompts/intake/*.md`（5 本）
- `learning/current-focus.yaml`
- `packets/*/task-context.yaml`（packet freeze 時に作る）
- `.claude/rules/intake-flow.md`（本ファイルを元に）

既存の更新:
- `story/intake/README.md` にフロー図と index.yaml の説明を追記
- `CLAUDE.md` 参照ファイルセクションに上記を追加
- `reviews/seed-to-macro-template.md` に provenance / reflection-ledger 更新ステップを追記

---

## 7. よくある漏れパターンとその検出

| 漏れパターン | 検出 | 修復 |
|---|---|---|
| Pro で生成したが raw に保存せず「頭で覚えた」 | raw-index の entry 不在 | 遡って raw 化、または open-questions に「出自不明」として記録 |
| digest 化せず seed にいきなり書く | seed の「出自: digests/...」が空欄 | 後から digest を補う（raw が残っていれば） |
| seed 化はしたが反映先判定していない | reflection-ledger に「未反映」として残り続ける | 14 日超で warning、30 日超で design-debt へ |
| 反映したが provenance 更新せず | provenance.descendants に canon 行がない | arc 完了時の consolidate で補う |
| 同じ主題の raw を 2 回入れて両方 digest 化 | digest-index で同 topic の重複 | 週次 consolidate で merge |

---

## 8. 拡張候補（将来）

- **intake dashboard**: raw/digest/seed/反映状況を table で見るツール（本提案外）
- **auto digest**: raw を自動で digest 化する skill（精度次第、まずは人間 or ChatGPT Pro 主導）
- **Pro との双方向連携**: provenance の逆方向（canon → raw）も引けるようにする
- **multi-work 横断 intake**: 複数作品の raw を共有する場合の共有 seeds（本提案では単作品範囲）
