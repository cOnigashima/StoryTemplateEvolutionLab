# ドメイン整理 — ユビキタス言語マップ

本ファイルは Story OS が扱う全概念の **包含関係・本籍ファイル・粒度・ライフサイクル** を 1 枚に整理する。author（taiji）が挙げた語をすべて含む:

Canon / Arc / ビートシート / promise（作品約束） / plot / packet（章束） / scene / seed / draft / pitch / continuity / patch / cadence / rhythm / consolidate / foreshadowing-map / prose / bible / world / character / walkthrough

本マップは `bible/glossary.md`（新設）に昇格する想定。

---

## 1. 一覧表（正式語・実装語・粒度・本籍・ライフサイクル）

| 正式語 | 実装語 / 別名 | 粒度 | 本籍ファイル | ライフサイクル | 一文定義 |
|---|---|---|---|---|---|
| **作品約束** | promise / 作品の核 | 作品全体 | `story/promises.md` | 作品の生涯 | 読者との「約束」。壊すと作品の輪郭が壊れる |
| **Canon** | canon / 正典 | 作品全体 | `bible/*`, `arcs/*`, `packets/frozen/*`, 既公開 drafts | 作品の生涯（追加＋凍結） | 作品内で「正しい」と確定した事実・ルール。変更は patch を通す |
| **Bible** | - | 作品全体（設計情報の索引） | `bible/world.md`, `bible/characters.md`, `bible/rules.md`, （育ったら）`bible/glossary.md`, `bible/dialogue-bible.md`, `bible/system-bible.md` 等 | 作品の生涯 | 安定設定の索引。raw 入力の置き場ではない。bible は Canon の **一部** |
| **World** | 世界観 | bible 配下 | `bible/world.md` | 作品の生涯 | 地理・文化・制度・物理則・超自然則 |
| **Character** | characters / 人物 | bible 配下 | `bible/characters.md`（+ `character-sheets.md`） | 作品の生涯 | 主要キャラの Want/Need / 声／関係／開示順 |
| **Rules** | style rules / 禁則 | bible 配下 | `bible/rules.md` | 作品の生涯 | 文体・視点・時制・禁則の正本 |
| **Arc** | - | 長い単位（複数 packet） | `arcs/series-overview.md`, `arcs/arc-NN.md` | 作品の生涯（漸進的に埋まる） | 始点→終点・中核対立・主反転・読者フック・packet 配分 |
| **Packet** | 章束（正式語） / bundle（禁止語） | 数話単位（通常 3〜7 話） | `packets/exploring/`, `packets/scoped/`, `packets/frozen/`, `packets/drafting/` | 設計→凍結→実装→完了 | 作品実装単位。episode_roles / disclose / withhold / guardrails / end_hooks が入る |
| **Episode** | ep / 話 | 1 話 | `drafts/packet-NNN/epNN.md` | 草稿→review→approved→published | 読者が 1 回で読む単位 |
| **Scene** | scene card | ビート集合（1 ep 内 1〜N 個） | `scenes/seed/`, `scenes/slotted/`, `scenes/superseded/` | seed→slotted→draft に消化 | 局所衝突の単位。purpose/desire/obstacle/turn/reveal/emotional_turn |
| **Beat** | ビート | scene 内部 | scene card の `beats` リスト or draft 内の段落集合 | scene 作成時に分解、draft で展開 | scene を動かす最小単位（行動・反応・開示の一拍） |
| **Beat Sheet** | ビートシート | 作品〜packet | `arcs/arc-NN.md` or `packets/*/beat-sheet.md` | 設計段階で定義、実装で参照 | Save the Cat 等の型。作品全体 or packet 単位の拍の並び |
| **Seed** | - | 再利用核（packet〜arc 単位の素材） | `story/seeds/seed-NNN-{slug}.md` | inbox→反映先整理→昇格 or 廃棄 | digest から切り出した再利用可能な設計核 |
| **Intake / Raw** | raw input / 生ログ | 大量入力 | `story/intake/raw/` | 保存→digest→（原則削除しない） | ChatGPT Pro 出力、会話ログ、断片メモの原文 |
| **Intake / Digest** | digest / 要約 | batch 単位 | `story/intake/digests/` | raw 収集後 → seed 抽出に使う | raw を batch ごとに圧縮した要約 |
| **Promise** | = 作品約束（上段と同じ） | - | - | - | - |
| **Plot** | 筋 / 展開 | arc〜packet | `arcs/arc-NN.md` §plot, `packets/*.yaml` §purpose / episode_roles | 設計→凍結 | 因果を時間順に繋いだ線。fabula（出来事）と syuzhet（提示順）の両方 |
| **Pitch** | - | 作品〜packet | `prompts/pitch.md` + `/pitch` skill 出力 | 企画期 | seed / packet の材料を売り込み形に圧縮した短い提案 |
| **Draft** | 本文 / 散文 | 1 ep | `drafts/packet-NNN/epNN.md` | 草稿→review→公開 | Prose の実体 |
| **Prose** | 散文 | draft の記述粒度 | `drafts/` 配下 | - | 本文そのもの。meta ではない |
| **Continuity** | 連続性 | 作品横断 | `.claude/skills/continuity.md`, `.claude/agents/continuity-checker.md` | 新 ep 毎に起動 | 過去話との整合。物証・関係・motif・知識状態の持ち越し整合 |
| **Patch** | canon patch / 修正提案 | canon への差分 | `story/canon-patch-proposals/patch-NNN-{slug}.md` | 提案→approval→canon 反映 | 既存 canon に差分を当てる提案。approval を経て canon 化 |
| **Design Debt** | 設計負債 | 横断 | `story/design-debt.yaml` | 起票→解消 or 棚卸 | 長生きする構造問題の台帳 |
| **Open Question** | 未解決論点 | 横断 | `story/open-questions.md` | 起票→解消 or canon 化 | 今確定しないが保留する論点 |
| **Cadence** | リズム / テンポ | packet〜作品 | `craft/cadence.md`（new）, packet の `guardrails` | 設計時 + review 時 | ビート配分のリズム。静と動、緊張と弛緩の比率 |
| **Rhythm** | ≈ cadence 下位 | packet 内 | 同上 | - | 文の長短、段落の密度。cadence のミクロ版 |
| **Consolidate** | 集約 / 整理 | 横断 | `consolidate-memory` skill / `reviews/consolidation-*.md` | 定期（arc 完了・learning 過多時） | 重複統合・古い論点の棚卸し |
| **Foreshadowing Map** | 伏線マップ | 作品横断 | `story/foreshadowing-map.md`（育ったら） | 伏線設置→回収の台帳 | どの ep で何を仕込み、どの ep で回収するかの台帳 |
| **Motif** | 反復モチーフ | 作品固有 | 作品側 `.claude/rules/monitoring-dictionary.md`（作品固有） + `craft/motif-operations.md`（generic） | 設計→実装→grep 検証 | 反復することで意味を獲得する記号（例: villainess-coc の紅茶5段） |
| **Reveal Plan** | 開示計画 | arc〜packet | `arcs/arc-NN.md` §reveal-plan, `packets/*.yaml` §disclose/withhold | 設計段階 | 何をいつ開示し、いつまで伏せるかの計画 |
| **Review (typed)** | typed review | 章/draft 単位 | `reviews/typed-review-NNN.md` | draft 完了後 | 本パック §4 参照 |
| **Review (bridge)** | bridge review | packet 切替時 | `reviews/bridge-review-NNN.md` | packet 切替時 | packet N 出口と packet N+1 入口の整合 |
| **Review (continuity)** | continuity review | 横断 | `reviews/continuity-review-NN.md` | 定期 | 連続性の横断検査 |
| **Review (persona)** | persona review / 読者レビュー | draft/packet | `reviews/persona-review-{A,B,C}-*.md` | approval 前 | 没入型／構造型／離脱型の 3 persona |
| **Review (approval)** | approval review | 公開前 | `reviews/approval-NNN.md` | 公開直前 | 公開可否判定 |
| **Rubric** | 評価基準 | 横断 | `craft/rubric.md`（know_how_explore 25 項目を移植） | 常駐 | 25 項目 0-4 anchored、hard gate 付き |
| **Walkthrough** | 実装ガイド / 手順書 | skill 別 | `.claude/skills/*.md` の実行手順部分 | 運用時 | 「この skill をどう回すか」の手順。drafter-walkthrough / critic-walkthrough 等 |
| **Reflection Ledger** | 反映台帳 | intake〜macro | `story/intake/reflection-ledger.md`（new） | intake 反映の度に追記 | raw→digest→seed→macro のどこに反映済み／未反映かを追う台帳 |
| **Provenance Index** | 出自索引 | intake〜draft | `story/intake/provenance.yaml`（new） | 常駐 | 各 canon 要素の出自（どの raw / どの Pro 対話から）を遡れる yaml |
| **Current Focus** | 現在地 | 作業状態 | `learning/current-focus.yaml`（new） | daily 更新 | 今作業中の arc / packet / ep / blocker を機械可読で持つ |
| **Task Context Pack** | タスク文脈 | 1 ep / 1 packet | `drafts/*/task-context.yaml` or `packets/*/task-context.yaml`（new） | ep 毎 | drafter/critic に渡す最小限の文脈圧縮パック |

---

## 2. 包含関係図（1 枚）

```
作品 (Work)
 ├── 作品約束 (Promise)  ← 最上位の約束。壊れれば作品が壊れる
 ├── Canon ──┐
 │           ├── Bible/
 │           │    ├── world
 │           │    ├── characters
 │           │    ├── rules
 │           │    ├── glossary (new)
 │           │    └── (growth: dialogue-bible, system-bible, ...)
 │           ├── Arcs/
 │           │    ├── series-overview
 │           │    └── arc-NN ── reveal plan / beat sheet
 │           ├── Packets (章束)/
 │           │    ├── exploring → scoped → frozen → drafting
 │           │    └── episodes (ep-role map, disclose/withhold, end_hooks)
 │           ├── Scenes/
 │           │    ├── seed → slotted
 │           │    └── beats
 │           └── Drafts/
 │                ├── prose (本文)
 │                └── task-context.yaml
 │
 ├── Meta (review/learning/debt/patch)
 │    ├── Reviews/ {typed, bridge, continuity, persona, approval, seed-to-macro}
 │    ├── Learning/ + current-focus.yaml
 │    ├── Canon Patch Proposals/
 │    ├── Design Debt
 │    └── Open Questions
 │
 ├── Intake (source)
 │    ├── raw/ → digests/
 │    ├── seeds/
 │    ├── provenance.yaml (new)
 │    └── reflection-ledger.md (new)
 │
 ├── Craft Library (new, generic knowledge)
 │    ├── scene-sequel.md
 │    ├── want-need.md
 │    ├── scope-management.md
 │    ├── beat-sheets.md
 │    ├── foreshadowing.md
 │    ├── motif-operations.md
 │    ├── rubric.md
 │    ├── reader-personas.md
 │    └── craft-principles.md
 │
 └── Release
      ├── approved/
      └── published/
```

### 2.1 包含規則

- **Promise ⊃ Canon**: 作品約束は Canon の上位拘束。Canon が約束を破ってはならない
- **Canon ⊇ Bible ⊇ World/Character/Rules**: Canon の一部が Bible、その内訳が World/Character/Rules
- **Canon ⊇ Arc ⊇ Packet ⊇ Episode ⊇ Scene ⊇ Beat**: 実装粒度の階層
- **Plot ∈ Arc/Packet の記述**: Plot は arc.md / packet.yaml 内に書かれる属性であってファイル種別ではない
- **Motif ⊂ Craft Library（generic） + 作品固有辞書**: Motif 運用 know-how は template（generic）、具体 motif キーワード辞書は作品固有
- **Foreshadowing Map ⊂ Canon（設置履歴） + Review（回収確認）**: 設置は canon、回収確認は review 側
- **Patch → Canon**: Patch は approval を経てから Canon へ。それまでは提案状態

---

## 3. 「同じ語に見えて違うもの」一覧（用語混同防止）

| 語 A | 語 B | 違い |
|---|---|---|
| Canon | Bible | Canon は「正しいとされる事実全体」、Bible はその **索引ファイル群**。Canon ⊇ Bible |
| Promise | Canon | Promise は読者との **約束**（書かないことも含む）、Canon は **事実**。Promise は Canon より上位 |
| Plot | Story | Plot は因果（A だから B）、Story は出来事の列（fabula）。syuzhet（提示順）は Arc が決める |
| Arc | Packet | Arc は「物語変化線」、Packet は「実装単位」。Arc ⊇ Packet |
| Packet | Episode | Packet = 数話束ね、Episode = 1 話。ep は packet の `episodes:` に属する |
| Scene | Beat | Scene は「1 つの局所衝突」、Beat は scene を動かす「一拍」 |
| Draft | Prose | Draft はファイル単位、Prose は記述粒度（meta と対置） |
| Seed | Digest | Seed は再利用核（ユニット化済み）、Digest は raw の batch 要約 |
| Review (typed) | Critic | typed review は成果物、critic は役割／agent／skill 名 |
| Patch | Canon Patch Proposal | Patch は差分そのもの、canon-patch-proposal は approval 前の提案状態 |
| Walkthrough | Skill | Skill は定義、Walkthrough は実行手順。skill ファイル内に walkthrough が書かれる |
| Consolidate | Continuity | Consolidate は重複統合、Continuity は連続性検査。前者はメタ整理、後者は作品整合 |
| Cadence | Rhythm | Cadence は長いスパンのリズム（packet/arc）、Rhythm は段落・文レベル。Cadence ⊃ Rhythm |
| Motif | Foreshadowing | Motif は反復で意味を得る記号、Foreshadowing は伏線。Motif が伏線機能を持つこともあるが一致しない |
| Reveal plan | Foreshadowing map | Reveal plan は「何をいつ開示するか」、Foreshadowing map は「何をいつ仕込み、いつ回収するか」の台帳 |

---

## 4. 禁止語・注意語（既存 story-os-boundaries.md 踏襲＋追加）

| 語 | 扱い | 理由 |
|---|---|---|
| bundle | **使わない**。`packet` を使う | story-os-boundaries.md §正式語 |
| backlog | **legacy 扱い**。正規 intake は `story/seeds/` | story-os-boundaries.md |
| queue | **projection、正本でない**。実行キューは将来別定義 | story-os-boundaries.md |
| review（単独） | **使わない**。`typed review` / `approval review` / `bridge review` 等 | story-os-boundaries.md |
| 章 | ambiguous、**避ける**。`packet` または `arc` と明示 | 新規（本提案） |
| 原稿 | ambiguous、**draft** と明示（ただし公開語としては可） | 新規 |
| ストーリー | ambiguous、**plot / arc / draft** の意味で使わない | 新規 |

---

## 5. lint 観点（用語一貫性チェックリスト）

v2 の review template で使う用語 lint 観点:

- [ ] `review` が typed/bridge/continuity/persona/approval のどれかに前置されているか
- [ ] `packet` / `章束` は混在しない（英語ドキュメントでは packet、日本語正式記述では 章束）
- [ ] `bundle` を使っていないか
- [ ] `queue` を正本として参照していないか
- [ ] `chapter` の訳は `arc`（単位の文脈）か `ep`（章節の文脈）か迷わないか
- [ ] Canon と Bible を互換に使っていないか
- [ ] Promise と Canon を互換に使っていないか
- [ ] Scene と Beat を混用していないか

これを `.claude/rules/vocabulary-lint.md`（新設候補）に移し、review で self-check 可能にする。

---

## 6. 粒度の目安（ページ数とビート数）

| 粒度 | 目安 | 根拠 |
|---|---|---|
| Beat | 散文 0.3〜2 ページ / ビート | know_how_explore Scene/Sequel |
| Scene | 散文 2〜8 ページ、ビート 3〜8 | Swain, Scene/Sequel |
| Episode | 散文 8〜20 ページ、scene 1〜4 | 作品標準 |
| Packet | 3〜7 ep、作品標準 | 既存 packet-template.yaml ep01..ep03 から ep01..ep07 |
| Arc | 3〜8 packet | 作品規模による |
| 作品 | 複数 arc | - |

数字は目安。作品の `bible/rules.md` で上書き可能。

---

## 7. このマップの更新規則

- 新語を使いたくなったら本ファイルに追加してから使う。勝手造語禁止
- 語の定義を変えるときは `canon-patch-proposals/` に patch を切ってから反映
- 語が 2 箇所以上で異なる意味で使われていたら `consolidate-memory` skill で統合
- 本マップは `bible/glossary.md` として昇格する想定（v2 移行 Phase 1）
