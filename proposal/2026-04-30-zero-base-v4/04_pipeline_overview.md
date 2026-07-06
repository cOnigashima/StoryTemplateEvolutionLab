# 04 Pipeline Overview — raw → publish の全体フロー

> **役割**: 02 で card 化された全概念と 03 で配置された全ディレクトリを動かしたとき、何がどう流れるかを 1 ページにまとめる。
> **依存**: 02_domain_model.md（用語）と 03_storage_trinity.md（物理配置）を前提とする。
> **対象読者**: 各セッションの最初に「今どこにいるか」を確認する author / drafter / reviewer。

---

## 1. パイプライン全体図

```
                    ┌──────────────────────────┐
                    │   外部世界                │
                    │   - 企画 chat            │
                    │   - 既存 bible package   │
                    │   - 設計メモ・断片        │
                    └───────────┬──────────────┘
                                │
                                ▼
                    ┌──────────────────────────┐
                    │   inbox/                 │  Raw 保存（原文ママ）
                    │   planning_sessions/     │
                    │   fragments/             │
                    └───────────┬──────────────┘
                                │
                    [Intake Adapter Prompt]
                                │
                                ▼
            ┌─────────────────────────────────────┐
            │   synthesis/                        │
            │   ├── session_digests/   (Digest)   │  構造化要約
            │   └── update_proposals/  (Update    │  反映指示書
            │                          Proposal)  │
            └───────────┬─────────────────────────┘
                        │
                  [Human Approval]
                        │
                        ▼
   ┌────────────────────────────────────────────────────┐
   │   bible/        Design/        State/             │  確定反映
   │   - kernel      - open-q       - decision-log    │
   │   - facets      - design-debt  - contradiction   │
   │   - logline     - patch-prop   - timeline-state  │
   │   - promise     - rejected     - char-states     │
   │   ...           ...            - impl-ledger     │
   │                                                    │
   │   story/seeds/  arcs/  packets/  scenes/          │
   └───────────┬────────────────────────────────────────┘
               │
               │ ← Patch lifecycle: design/canon-patch-proposals/
               │   → human approval → bible 改訂 + state/canon-patch-log
               │
               │ ← Packet Freeze: packets/scoped/ → frozen/
               │   → Packet Freeze Review
               │
               ▼
        [Writing Adapter Prompt]
               │
               ▼
   ┌────────────────────────────────────────────────┐
   │   writing/episode_packs/{ep}/                 │  圧縮 Pack
   │   ├── episode_brief.md                         │
   │   ├── scene_card.md                            │ ← Term: Scene Card
   │   ├── context_pack.md                          │
   │   └── acceptance_checklist.md                  │ ← Term: Acceptance Contract
   │                                                │
   │   scenes/slotted/{ep_id}.md                   │ ← 正本 Scene Card
   │   reviews/contracts/{ep_id}.contract.yaml     │ ← 正本 Acceptance Contract
   └───────────┬────────────────────────────────────┘
               │
        [Drafter / 執筆 — drafter-preflight 適用]
               │
               ▼
   ┌────────────────────────────────────────────────┐
   │   drafts/episodes/{ep_id}-{slug}.md           │  Prose（本編原稿）
   └───────────┬────────────────────────────────────┘
               │
        [Multi-Pass Self-Review (drafter)]
        [Typed / Persona / Continuity Review (critic)]
        [Bridge Review (packet 切替時)]
               │
               ▼
   ┌────────────────────────────────────────────────┐
   │   reviews/                                     │
   │   - typed-review-...                           │
   │   - persona-review-...                         │
   │   - continuity-review-...                      │
   │   - bridge-review-...                          │
   │   - audits/                                    │
   └───────────┬────────────────────────────────────┘
               │
       [Approval Review — DoD-E]
               │
               ▼
   ┌────────────────────────────────────────────────┐
   │   approved/episodes/{ep_id}-{slug}.md         │  公開待ち
   └───────────┬────────────────────────────────────┘
               │
       [公開実施]
               │
               ▼
   ┌────────────────────────────────────────────────┐
   │   published/episodes/{ep_id}-{slug}.md        │  公開済
   └───────────┬────────────────────────────────────┘
               │
        [State 更新]  → state/timeline-state.yaml
                      → state/character-states.yaml
                      → state/{facet}-implementation.yaml
                      → state/decision-log.yaml


並行回路:
   ┌──────────────────────┐
   │   backlog/           │  全 task フラット
   │   - 内部タスク        │  （writing / design / review / release / 外部）
   │   - 計画              │
   │   - 外部アクション     │
   └──────────────────────┘

   ┌──────────────────────┐
   │   learning/          │  制作 learning
   │   {date}-{slug}.md   │  失敗ログ・retro
   └──────────────────────┘
```

---

## 2. Phase 1: Intake — raw を bible に流す前の搬送

**入力**: 外部世界の raw（企画 chat / 既存 bible package / 設計メモ）
**出力**: `bible/` `design/` `state/` の確定反映
**Adapter**: Intake Adapter（`adapter/intake_adapter_prompt.md`）

### 1.1 Raw 保存（inbox/）

外部から来た資料は **必ず inbox/ に原文ママで保存**。直接 bible に流し込まない。

```
inbox/
  planning_sessions/{date}_{slug}.md     ← ChatGPT log 等
  fragments/{date}_{slug}.md             ← 断片メモ
```

**禁止事項**:
- raw を bible に直接書かない
- raw を inbox/ に残さず捨てない
- 大量入力を 1 ファイルに丸ごと保存しない（batch ごとに分ける）

### 1.2 Intake Adapter 実行

`adapter/intake_adapter_prompt.md` を LLM に渡し、inbox/ の raw を消費させる。Intake Adapter は次の順序で動く:

1. **全体把握**: 入力全体を 1 度通読、5〜10 行で要約
2. **項目化**: 抽出して各に ID 付与
   - 確定（confirmed）→ `C-XXX`
   - 暫定（tentative）→ `T-XXX`
   - 未決（open）→ `Q-XXX`
   - 矛盾（contradiction）→ `X-XXX`
   - author 判断要 → `AD-XXX`
   - 後で決める → `D-XXX`
   - 意図的非開示 → `H-XXX`
   - 没案 → `R-XXX`
3. **振り分け先の決定**:
   - 確定設定（執筆に直接効く）→ `bible/`
   - 仮設・候補・author 判断待ち → `design/`
   - 制作中に動く事実 → `state/`
   - 没案 → `design/rejected-ideas.md`
   - 1 話分の執筆指示 → `writing/episode_packs/`（ただし Writing Adapter の領域なので Intake Adapter ではこれを作らない）
4. **既存ファイルとの照合**: bible / design / state にすでにあるファイルと衝突しないかチェック。衝突は `contradictions:` に積む（**勝手に解消しない**）
5. **Update Proposal 生成**
6. **Writing readiness 判定**
7. **出力**:
   - `synthesis/session_digests/{date}_{slug}.md`（Digest）
   - `synthesis/update_proposals/{date}_{target}_proposal.md`（Update Proposal）

### 1.3 Human Approval

Update Proposal は **必ず human approval を経て** から bible/design/state に反映する。Adapter が直接書き換えない。

- `confirmed` 項目は author confirm 後に bible/ へ
- `tentative` 項目は design/ へ（後日 Patch で bible に昇格）
- `contradiction` 項目は contradiction-log に append + author 解決待ち
- `needs_author_decision` 項目は open-questions.md に append
- `intentionally_hidden` 項目は kernel.information_design.intended_unknowns に追加（bible 本文には書かない）

### 1.4 反映

承認された Update Proposal の差分を bible/design/state に適用。Bible への書き込みは **新規追加 or Patch 経由の改訂**のみ。

---

## 3. Phase 2: Design Freeze — Bible から Packet を凍らせる

**入力**: bible / design / state
**出力**: `packets/frozen/packet-{NNN}-{slug}.yaml` + `scenes/slotted/{ep_id}.md`
**Gate**: Packet Freeze Review（DoR-C）

### 2.1 Arc 設計

`arcs/series-overview.md` で Manuscript / Part 構造を確定。`arcs/arc-{NN}.md` で各 Arc を `scoped` 状態に持っていく:
- 始点と終点
- 中核対立
- 主反転
- 読者フック
- 含む Packet の役割

### 2.2 Packet を frozen に進める

`packets/scoped/packet-{NNN}-{slug}.yaml` の必須項目を埋める:
- `purpose`
- `entry_state` / `exit_state`
- `episode_roles`
- `end_hooks`
- `disclose` / `withhold`
- `guardrails`
- 各 episode の `role` / `loss` / `gain` / `reveal` / `hooks` / `cliffhanger`

### 2.3 Packet Freeze Review

`reviews/packet-freeze-{packet_id}-{date}.md` で凍結判定:
- 全項目埋まっているか
- 直前 packet の `exit_state` と整合しているか
- 内 episode 間の知識状態遷移が単調か
- promise.items のうち本 packet で実装するものが列挙されているか
- contradiction 残存ゼロか

通過したら `packets/scoped/` → `packets/frozen/` に移動。

### 2.4 Scene Card 生成

frozen packet を Writing Adapter が読み取り、各 episode 用の Scene Card を `scenes/slotted/{ep_id}.md` に生成。これは Phase 3 と統合運用される。

---

## 4. Phase 3: Writing — Writing Pack から Prose へ

**入力**: bible / state / `scenes/slotted/{ep_id}.md` / `reviews/contracts/{ep_id}.contract.yaml`
**出力**: `drafts/episodes/{ep_id}-{slug}.md`（Prose）
**Adapter**: Writing Adapter（`adapter/writing_adapter_prompt.md`）

### 3.1 Writing Adapter 実行

Writing Adapter は 1 episode 単位で動き、次の 4 ファイルを `writing/episode_packs/{ep_id}/` に生成:

- `episode_brief.md`: purpose / entry_state / exit_state / what_happens
- `scene_card.md`: focal character / scene goal / conflict / turn / reveal / end_state / beat sequence（Scene Card のコピー）
- `context_pack.md`: disclose / withhold / guardrails / 関連 Bible facet の抜粋
- `acceptance_checklist.md`: must_satisfy / must_not_violate / quality_gates（Acceptance Contract のコピー）

**bible 全体は drafter に渡さない**。Writing Pack だけで draft できる状態に圧縮する。

### 3.2 Drafter Preflight（drafter-preflight rule 適用）

drafter は prose を書き始める前に以下を draft ファイルの meta 欄に書き下ろす:

1. **因果一段落**: focal character の知識状態遷移を 1 段落に圧縮
2. **知識状態台帳**: append-only の単調性チェック
3. **合理化語彙 self-check**: 「つまり」「要するに」等の出現確認

加えて運用 Gate:
- **Gate 0**: 直前散文照合（series opener 以外 MUST）
- **Gate A**: Writing Pack 要件マッピング
- **Gate C**: 前振りチェック（クライマックスあるなら）

### 3.3 Drafting

`drafts/episodes/{ep_id}-{slug}.md` に prose を書く。

### 3.4 Multi-Pass Self-Review

drafter が typed review に渡す前に最低 3 パス:
- Pass 1: 因果・認知チェック
- Pass 2: Writing Pack / Canon 反映チェック
- Pass 3: 読者シミュレーション
- Pass 4: 横断チェック（3 話以上まとめ書き時 MUST）

---

## 5. Phase 4: Review — 品質ゲート

**入力**: `drafts/episodes/{ep_id}-{slug}.md`
**出力**: `reviews/{type}-...{ep_id}-{date}.md`

### 4.1 種別ごとの Review

| Review 種別 | タイミング | 観点 | 出力先 |
|---|---|---|---|
| **Typed Review** | 各 episode draft 完了後 | Rubric 全軸 | `reviews/typed-review-{date}-{ep_id}.md` |
| **Continuity Review** | 横断検査 / 矛盾発見時 | 知識状態 / timeline / 物理事実 | `reviews/continuity-review-{scope}-{date}.md` |
| **Persona Review** | 重要 episode（推奨） | 没入 A / 構造 B / 離脱 C | `reviews/persona-review-{ep_id}-{date}.md` |
| **Bridge Review** | packet / arc 切替時 MUST | entry/exit state 整合 | `reviews/bridge-review-{packet_a}-{packet_b}-{date}.md` |
| **Approval Review** | 公開直前 MUST | acceptance / kakuyomu policy | `reviews/approval-{ep_id}-{date}.md` |
| **Packet Freeze Review** | packet を frozen にする時 | DoR-C | `reviews/packet-freeze-{packet_id}-{date}.md` |
| **Design Audit** | 設計が空疎ではないか定期 | bible / design 整合性 | `reviews/audits/{date}-{scope}-design-audit.md` |

### 4.2 Reverse Flow

Review で発見した問題は **必ず上流に戻す**:

| 問題層 | 戻し先 |
|---|---|
| prose 問題 | `drafts/` または `scenes/slotted/` |
| hook / pacing 問題 | `packets/` |
| 動機 / 関係性 問題 | `bible/characters/` |
| 開示順 / 反転点 問題 | `arcs/` |
| 作品約束のズレ | `bible/promise.md` |
| 長生きする構造問題 | `design/design-debt.yaml` |
| まだ確定していない設定変更 | `design/canon-patch-proposals/` |
| packet 切替の齟齬 | `packets/` への bridge review |

---

## 6. Phase 5: Release — 承認・公開

**入力**: typed review 通過済み draft + acceptance contract 充足
**出力**: `approved/episodes/` → `published/episodes/`
**Gate**: Approval Review（DoD-E）

### 5.1 Approval Review

公開直前の最後の gate:

- ✅ Acceptance Contract の must_satisfy 全 ✓
- ✅ must_not_violate ゼロ
- ✅ intended_unknowns が prose で意図通り隠されている
- ✅ must_be_clear が読者に伝わっている
- ✅ Quality bar（rubric ≥60 等）
- ✅ kakuyomu policy 適合（AI タグ / 投稿頻度 / 禁止コンテンツ）
- ✅ Author 承認（hard_lock）

### 5.2 approved/ に移動

`drafts/episodes/{ep_id}-{slug}.md` を `approved/episodes/{ep_id}-{slug}.md` にコピー（リネーム不可、`release_{ep_id}_{timestamp}.md` 形式）。

### 5.3 公開実施

カクヨム等への投稿。投稿頻度ルール（1 日 3 ep / 4h 間隔 / 週 15 ep）を遵守。

### 5.4 published/ に反映

公開後に `published/episodes/{ep_id}-{slug}.md` にコピー。State の以下を更新:

- `state/timeline-state.yaml`: 公開済 episode を append
- `state/character-states.yaml`: 公開済 episode 終了時点の現在値
- `state/{facet}-implementation.yaml`: 該当 facet の実装履歴 append
- `state/decision-log.yaml`: 公開判断の記録

---

## 7. 同期回路（横断的なプロセス）

### 7.1 Patch Lifecycle

Bible を改訂したい場面で動く回路。直接書き換えは禁止。

```
[Bible に改訂したい論点が発生]
        ↓
design/canon-patch-proposals/{patch_id}-{slug}.md  作成
        ↓
[Author Approval]
        ↓
bible/{target}.md  改訂適用
        ↓
state/canon-patch-log.yaml  に entry 追加（Ledger pattern）
```

Patch は **必ず一塊（atomic）**で適用。複数 facet にまたがる Patch は分割して個別 patch 化する。

### 7.2 Contradiction Triage

矛盾を発見したときに動く回路。

```
[Continuity Review / Design Audit / drafter で矛盾発見]
        ↓
state/contradiction-log.yaml  に X-XXX として append
        ↓
[Severity 判定]
   ├── high (canon 破壊 / promise 違反): Open Question 昇格 + Patch lifecycle
   ├── mid (手戻り発生): drafter or scene card 修正
   └── low (改善機会): backlog/ に追加
        ↓
[解決]
        ↓
state/contradiction-log.yaml  に resolution 追記（削除しない）
```

### 7.3 Pitch → Seed → Bible 昇格

新規アイデアの取り込み。

```
[アイデア発生]
        ↓
[/pitch skill 実行] → backlog/{slug}.yaml （未採用は backlog）
        ↓
[Author 採用判断]
        ├── 採用: story/seeds/{date}_{slug}.md に格納（Term: Seed）
        ├── 却下: design/rejected-ideas.md に append
        └── 保留: design/open-questions.md に append
        ↓
[Seed が Bible 昇格に値する判断]
        ↓
synthesis/update_proposals/  経由で bible に反映
```

### 7.4 Reverse Flow（既述）

Review → 上流の修正、と Phase 4.2 で説明済み。

---

## 8. 並行回路: Backlog / Learning

### 8.1 Backlog

`backlog/` は全 task のフラット置き場。lifecycle subfolder を作らない。

| task 種別 | backlog/ 内の表現 |
|---|---|
| 内部タスク（書く・直す・review 実施） | `backlog/{slug}.yaml` |
| 計画タスク（Manuscript-plan の細分化） | 同上 |
| 外部アクション（kakuyomu like / SNS 投稿） | 同上、`channel:` フィールドで識別 |
| 設計タスク（"foreshadowing-map 更新"） | 同上、または `design/open-questions.md` で管理 |

### 8.2 Learning

`learning/` は制作中の失敗・気づきを `{date}-{slug}.md` で append。

- 設計失敗 → 即 retro として記録
- 方法論の改良 → learning に append、繰り返し参照されるなら `.claude/rules/` に昇格
- author フィードバック → 同上

`learning-capture.md` rule に従う（既存 rule 継承）。

---

## 9. ゲート一覧（DoR / DoD）

### DoR（着手前）

| Gate | 対象 | 通過条件 |
|---|---|---|
| **DoR-A** | 新規作品 bootstrap | kernel 11 項目 / bible 最低限 / arcs/arc-01 / packets/scoped/packet-001 |
| **DoR-B** | Episode draft 開始 | scene_card / acceptance_contract / Gate 0 / Gate A / Gate C / 因果一段落 / 知識状態台帳 |
| **DoR-C** | Packet frozen 化 | packet.yaml 全項目 / contradiction ゼロ / entry/exit state 整合 / Packet Freeze Review 通過 |

詳細は `06_bible_dor.md` 参照。

### DoD（次に進める前）

| Gate | 対象 | 通過条件 |
|---|---|---|
| **DoD-E** | Episode 公開直前 | Multi-Pass / acceptance / typed review / approval review / kakuyomu policy / hard_lock |
| **DoD-P** | Packet release | 全 ep が DoD-E / packet-assembly review / promise 紐付け検証 / bridge review |
| **DoD-A** | Arc / Part 完結 | 全 packet が DoD-P / arc-through review / 主反転実装 / 中だるみなし / 伏線回収 |

---

## 10. 1 セッションの典型的フロー

新規セッション開始時の動き方の例:

### Case 1: 「企画 chat を持ち込んだ」

```
1. inbox/planning_sessions/{date}_{slug}.md に保存
2. adapter/intake_adapter_prompt.md を LLM に渡す
3. synthesis/session_digests/ + synthesis/update_proposals/ を確認
4. Author Approval
5. bible/ design/ state/ に反映
```

### Case 2: 「ep10 を書きたい」

```
1. DoR-A 確認（kernel / bible / arcs / packets/frozen に packet-001 等）
2. ep10 の Writing Pack を生成: adapter/writing_adapter_prompt.md
3. writing/episode_packs/ep10/ + scenes/slotted/ep10-{slug}.md を確認
4. drafter-preflight 実施（meta 欄記入）
5. drafts/episodes/ep10-{slug}.md に prose 執筆
6. Multi-Pass Self-Review
7. Typed Review + （必要なら） Continuity Review
8. Approval Review
9. approved/ → 公開 → published/
10. State 更新
```

### Case 3: 「公開済 ep03 と新 ep10 で矛盾を発見」

```
1. state/contradiction-log.yaml に X-XXX として append
2. Severity 判定
3. high なら design/canon-patch-proposals/ に Patch 起票
4. Author Approval → bible 改訂 → state/canon-patch-log.yaml
5. ep10 draft を改訂 contradiction を踏まえて再 draft
6. learning/{date}-contradiction-recovery.md に retro
```

---

## 11. パイプラインの不変条件（まとめ）

1. **raw を直接 bible に流さない** — Intake Adapter 経由必須
2. **bible 全体を drafter に渡さない** — Writing Adapter で圧縮
3. **bible を直接書き換えない** — Patch 経由必須
4. **Update / Patch は human approval 必須**
5. **Review は種別必須** — "Review" 単独使用禁止
6. **Reverse Flow を必ず開ける** — review が感想で終わらない
7. **State Ledger は append-only** — 履歴を削除しない
8. **drafts は drafts/ のみ** — bible に同居させない（Sample Scene 例外）
9. **作品固有 facet は generic 雛形に流入させない**
10. **Backlog はフラット** — lifecycle subfolder を作らない
