# Story Template v2 — 全体設計

## 1. 現状評価（監査要旨）

### 1.1 強み（維持するもの）

- **Story OS フロー** (`raw → digest → seed → promises/bible/arcs → packet → scene → draft → review → reverse flow`) が言語化されている
- **.claude/rules/** 5 本（`learning-capture` / `drafter-preflight` / `file-growth` / `story-os-boundaries` / `kakuyomu-policy`）が作品横断の共通契約になっている
- **drafter-preflight の 3 原則 + Gate 0/A/C + Multi-Pass Self-Review** が因果順矛盾・知識状態単調性・合理化語彙 tell 検知まで拾える構造
- **file-growth.md** が「テンプレートは上限ではない」と宣言し、育て方のパターンを持っている
- **prior audits 2 本**（`2026-04-18-story-template-gap-analysis.md` / `2026-04-18-story-template-intake-integration-proposal.md`）が P0/P1/P2 と 5 層 intake 案まで既に言語化している

### 1.2 弱み（本提案で解決する）

| # | 弱み | 根拠 | 解決先 |
|---|---|---|---|
| W1 | **大量インプット（Pro 研究・長文設計メモ）の正規 intake が未整備**。raw/digests/seeds は存在するが「どこに何を分解するか」の手順・provenance・reflection ledger が未定義 | `intake-integration-proposal` §1, `one-man-statefall/story/intake` の実装が先行 | `03-intake-flow.md` |
| W2 | **ドメイン語の包含関係が曖昧**。Canon / Bible / Arc / Promise / Patch / Motif / Cadence / Foreshadowing が一覧で示されていない | `CLAUDE.md` 用語セクションが列挙のみ、関係図なし | `02-domain-map.md` |
| W3 | **レビュー体系が typed-review 1 種のみ**。bridge / continuity / persona / approval / grep 検証 / 25 項目 rubric が works 側にしかない | `works/villainess-coc/.claude/rules/reviewer-gate-b.md`, `know_how_explore/小説レビュープロンプト.md` | `04-review-system.md` |
| W4 | **創作ノウハウが template 側に無い**。Scene/Sequel、Want/Need、scope、beat sheet、foreshadowing、反復 motif 運用が know_how_explore にしかない | `know_how_explore/小説執筆ノウハウ総覧.md` | `05-craft-library.md` |
| W5 | **作品横断の learning 吸い上げが手動**。works/*/learning の中で StoryTemplate に昇格すべきものを自動抽出する仕組みがない | 既存 learning-capture.md は単作品内のみ | `08-reform-plan.md` Phase 1 |
| W6 | **機械可読な状態トラッキング**が無い。`current-focus.yaml`, `task-context.yaml` が one-man-statefall にしかない | `one-man-statefall/story/learning-loop.md` | `03-intake-flow.md` + `04-review-system.md` |
| W7 | **packet-template.yaml の置き場所**が `packets/exploring/`, `packets/scoped/`, `packets/frozen/` 配下の生きた場所にある（ステージそのものに living template が混入） | `2026-04-18-story-template-gap-analysis.md` P0 | `06-directory-structure.md` + `07-skeleton/` |
| W8 | **runtime artifacts（telemetry / actions / campaigns / queue）がテンプレート初期状態に残っている**（one-man-statefall init 事故の源） | `template.manifest.json` が legacy projection を示唆、しかし物理的に消えていない | `06-directory-structure.md` + `08-reform-plan.md` Phase 0 |

### 1.3 保留（本提案では結論しない）

- **AI モデル／RAG／LoRA／SFT** の運用設計（know_how_explore に記述はあるが template 範囲外）
- **factory-platform 側 docs** の改訂（本提案は template 本体）
- **カクヨム投稿自動化**（kakuyomu-policy 以外の自動化）

---

## 2. 目標像（v2 Story Template の輪郭）

### 2.1 アーキテクチャ（4 層 + intake）

既存の `2026-04-18-story-template-gap-analysis.md` で提案されている **Core Authoring / Review-Learning / Intake / Automation-Runtime** の 4 層を引き継ぎ、intake を第 5 層として独立させる。

```
┌──────────────────────────────────────────────────┐
│ Layer 0: Intake (source)                          │  raw / digest / seed
│   story/intake/raw/                               │
│   story/intake/digests/                           │
│   story/seeds/                                    │
│   story/intake/provenance.yaml                    │ ← new
│   story/intake/reflection-ledger.md               │ ← new
├──────────────────────────────────────────────────┤
│ Layer 1: Core Authoring (macro/meso/micro)        │
│   story/promises.md, open-questions, design-debt  │
│   bible/{world,characters,rules,...}              │
│   arcs/{series-overview,arc-NN,...}               │
│   packets/{exploring,scoped,frozen,drafting}/     │
│   scenes/{seed,slotted,superseded,...}/           │
│   drafts/                                         │
├──────────────────────────────────────────────────┤
│ Layer 2: Review-Learning (meta)                   │
│   reviews/{typed,bridge,continuity,persona,       │
│            approval,seed-to-macro,packet-audit}/  │
│   learning/ + current-focus.yaml   ← machine-readable layer
│   story/canon-patch-proposals/                    │
│   story/design-debt.yaml                          │
├──────────────────────────────────────────────────┤
│ Layer 3: Craft Library (knowledge base)    ← new  │
│   craft/{scene-sequel, want-need, scope,          │
│          beat-sheets, foreshadow, rubric,         │
│          reader-personas, motif-operations}/      │
├──────────────────────────────────────────────────┤
│ Layer 4: Release (approved / published)           │
│   approved/ / published/                          │
├──────────────────────────────────────────────────┤
│ Layer R: Runtime Contracts (opt-in, not default)  │
│   （template.manifest.json で declared、作品が必要なら opt-in） │
│   actions/, campaigns/, telemetry/, queue/        │
└──────────────────────────────────────────────────┘
```

### 2.2 テンプレート契約（template vs runtime）

**template 起動時に存在すべきファイル**:
- Layer 0 の raw/digests/seeds 空ディレクトリ + provenance.yaml テンプレ
- Layer 1 の promises/bible/arcs/packets/scenes/drafts 全スケルトン
- Layer 2 の reviews/ テンプレ一式 + learning/ 空 + canon-patch-proposals/ 空
- Layer 3 の craft/ 全項目（読めば分かる状態で）
- Layer 4 の approved/ + published/ 空
- `.claude/rules/` 5 本（既存）+ 新規 1-2 本（`intake-flow.md`, `review-system.md` ※後述）

**template 起動時に存在してはいけないもの**（W8 対応）:
- `actions/`, `campaigns/`, `telemetry/`, `queue/`, `story/job-packets/queued/` 等の runtime artifacts
- 実データが入った `packet-001-*.md`, `ep01.md` 等の作品固有ファイル（ただしサンプルは `/samples/` 下に隔離して置く）

**template.manifest.json 拡張**（既存）:
```yaml
artifacts:
  template: [...]      # 初期状態で必ず存在する
  samples: [...]       # サンプル／学習用、作品開始時に削除可
  runtime_optional: [...]  # 作品が必要なら opt-in で生やす
  deprecated: [queue/]    # legacy projection、使わない
```

### 2.3 3 テーマの実装戦略

| テーマ | 鍵となる成果物 | 既存資産の活用 |
|---|---|---|
| **大量インプット受け入れ** | raw→digest→seed→macro フロー、provenance.yaml、reflection-ledger.md、Pro 用 intake prompt 集 | intake-integration-proposal を下敷きに、one-man-statefall 実装を参考 |
| **ドメイン整理** | 1 枚のユビキタス言語マップ、包含図、各語の「本籍ファイル」表、用語一貫 lint リスト | CLAUDE.md 用語セクションを `bible/glossary.md` に昇格 |
| **レビュー体系＋創作ノウハウ** | typed/bridge/continuity/persona/approval review templates、grep 検証、25 項目 rubric、PART A/B/C prompts、craft/ ライブラリ、反復 motif 運用方法（monitoring-dictionary の generic 化） | works/villainess-coc の reviewer-gate-b.md / monitoring-dictionary.md を generic 化、know_how_explore のプロンプト資産をほぼそのまま吸収 |

---

## 3. 方針原則

1. **Fat by design, not by accident**: 重装備で守る。ただし 1 ファイル 300 行ルール（file-growth.md）は維持。育ったら分割、索引は残す。
2. **Template は最小起動、Craft/Review は最大装備**: 作品初期で迷わない最小スケルトン（Layer 1）と、知識として常駐する最大装備（Layer 2/3）を分ける。
3. **works → template 昇格は双方向**: works の learning を「候補」として集約、author 承認 → template/ 昇格 → works は補足のみ残す。逆は template → works へ自動継承（作品 init 時に snapshot）。
4. **機械可読と散文の両持ち**: yaml / table（タスクランナー・lint 向け）と散文（人間理解向け）を常に併置。どちらかだけで済ませない。
5. **grep は正本の友**: 記憶・meta での判定を禁じ、本文 grep を一次根拠にする運用（villainess-coc §8.1 起源）を template の review 側に移植。
6. **provenance を失わない**: raw input → digest → seed → macro の反映履歴を yaml で繋ぐ。反映先が空なら reflection-ledger に「未反映」として残し、いずれ扱う。
7. **Opt-in runtime**: runtime artifacts は自動で生やさない。必要になった作品が template.manifest.json を見て opt-in する。one-man-statefall init 事故の再発防止。

---

## 4. 成功判定（Definition of Done）

v2 完成とみなせる条件:

1. **新規作品 init が 10 分で終わる**。template を clone し、CLAUDE.md の「執筆開始ライン」条件（promises / bible / arcs / packets/frozen 1 本 / scenes 該当分）を埋めるのに必要なファイル・順序・prompt が全部揃っている
2. **Pro で生成した 50 ページの設計メモが raw → digest → seed に通せる**。手順化された prompt があり、reflection-ledger に反映先が記録される
3. **draft 1 本を書く前に 4 つの gate（0/A/B/C）と Multi-Pass Self-Review が起動できる**。reviewer 側 PART E 4 block も template で起動可能
4. **craft/ を参照するだけで Scene/Sequel, Want/Need, scope, beat sheet, foreshadowing が実装できる**。新人 drafter（あるいは別 Claude）が読んで同じ品質で書ける
5. **works/villainess-coc / one-man-statefall の既存 learning の 80% 以上**が template に昇格 or 作品固有として明確に区分されている
6. **kakuyomu-policy と衝突しない**。AI 利用タグ運用・投稿頻度制限が release 側で遵守される

---

## 5. 変更の性格（Revolution vs Evolution）

本提案は `evaluation-revolution-lab` 用語で言えば **evolution 基調 + 局所 revolution**:

- **Evolution**: 既存 5 rules、Story OS 流れ、4 層概念は維持
- **Revolution**:
  - Layer 3 Craft Library の新設（know_how_explore を template 正典化）
  - Layer 0 intake に provenance + reflection-ledger を導入
  - `.claude/rules/` に `review-system.md` `intake-flow.md` を追加
  - runtime artifacts を template から物理的に切り離し
  - `current-focus.yaml` 等の機械可読層を正典化
