# Layer × TAKT Facet × ファイル位置マップ v3

> **目的**: 各概念がどの Layer に属し、どの TAKT facet に流れ、どのファイルに住むかを 1 枚で見えるようにする。kernel と非 kernel の境界線をここで明文化する。
> **ガチガチ度**: Layer 帰属とファイル位置は本 v3 で固定。facet 割り当ては TAKT 実装で微調整あり得る。

---

## 1. Layer 構成（4+1 → 4+1+1.5）

Pack A の 4+1 Layer に **Layer 1.5（Adapter）** を本 v3 で正式追加した。

```
Layer 0  Intake             - 大量入力受付
Layer 1  Core Authoring     - 物語の中身（kernel + bible + structure）
Layer 1.5 Adapter           - kernel + bible → workflow 入力 への変換 ★本 v3 新設
Layer 2  Review-Learning    - レビュー + 学習
Layer 3  Craft              - 創作原理 + framework lens
Layer 4  Release            - 公開準備 + 公開済
Layer R  Runtime            - TAKT 実行・候補・選抜・統合・台帳（opt-in 隔離）
```

**Layer R の opt-in 隔離原則**: TAKT 不在でも Layer 0-4 で執筆は完結する。Layer R は TAKT を持ち込んだ作品にだけ存在する。Pack A の `runtime_optional` 思想を継承。

---

## 2. TAKT Facet との対応

TAKT は prompt を 4 facet に分解する。本 v3 では Story Template の各概念をどの facet にマップするかを固定する。

| TAKT facet | 役割 | Story Template での source |
|---|---|---|
| **persona** | エージェントの役割（faithful_writer / judge 等） | `prompts/personas/` + `.claude/agents/` |
| **policy** | MUST / 禁則 / ガードレール | `.claude/rules/` の rules + bible/rules.md |
| **knowledge** | 参照する事実・原理・設定 | bible/* + craft/* + ledger/* + arcs/* |
| **instruction** | この step で何をするかの具体指示 | scene_card + acceptance_contract（Adapter 出力） |

---

## 3. 全体マップ

| Layer | 主概念 | ファイル位置 | TAKT facet |
|---|---|---|---|
| **L0** | Raw | `story/intake/raw/` | - |
| L0 | Digest | `story/intake/digests/` | knowledge（参照のみ） |
| L0 | Seed | `story/seeds/` | knowledge |
| L0 | Domain Synthesis | `story/intake/domain-synthesis/` | knowledge + instruction |
| L0 | Reflection Ledger | `story/intake/reflection-ledger.md` | - |
| L0 | Provenance Index | `story/intake/provenance.yaml` | - |
| **L1** | Kernel | `story/kernel.yaml`（★ 新設） | knowledge |
| L1 | Promise | `story/promises.md` | policy + knowledge |
| L1 | Open Questions | `story/open-questions.md` | knowledge |
| L1 | Design Debt | `story/design-debt.yaml` | knowledge |
| L1 | Patch（canon patch proposal） | `story/canon-patch-proposals/` | knowledge（pending） |
| L1 | Bible (World) | `bible/world.md` | knowledge |
| L1 | Bible (Characters) | `bible/characters.md` | knowledge |
| L1 | Bible (Rules) | `bible/rules.md` | policy |
| L1 | Genre Overlay | `bible/genre-overlay.md`（★ 新設） | policy + knowledge |
| L1 | Project Override | `bible/project-override.md`（★ 新設） | policy（最高優先） |
| L1 | Manuscript | （ディレクトリ全体） | - |
| L1 | Part | `arcs/parts/part-NN.md` または `arcs/series-overview.md` 内 | knowledge |
| L1 | Arc | `arcs/arc-NN.md` | knowledge |
| L1 | Packet | `packets/{stage}/packet-NNN-{slug}.yaml` | knowledge + instruction |
| L1 | Episode（設計） | `scenes/slotted/packet-NNN-epMM-{slug}.md` | knowledge |
| L1 | Episode（本文） | `drafts/packet-NNN-epMM-{slug}.md` | - |
| L1 | Scene Card | scenes/ 内（episode 設計と同居） | instruction |
| L1 | Foreshadowing Map | `story/foreshadowing-map.md` | knowledge |
| L1 | Reveal Plan | `story/reveal-plan.md` | knowledge |
| L1 | Cadence Plan | `arcs/cadence-plan.md` | knowledge |
| **L1.5** | Adapter（実装） | `.takt/adapter/` または `prompts/adapter/`（次セッション） | step（faceted） |
| L1.5 | Acceptance Contract | `reviews/contracts/packet-NNN-epMM-{slug}.contract.yaml` | instruction（judge 用） |
| L1.5 | Judge Contract | acceptance_contract に内包 | instruction（judge 用） |
| **L2** | Typed Review | `reviews/typed-review-{date}-{target}.md` | - |
| L2 | Bridge Review | `reviews/bridge-review-{date}-{target}.md` | - |
| L2 | Continuity Review | `reviews/continuity-review-{date}-{target}.md` | - |
| L2 | Persona Review | `reviews/persona-review-{date}-{target}.md` | - |
| L2 | Packet Freeze Review | `reviews/freeze-review-{date}-{target}.md` | - |
| L2 | Approval Review | `reviews/approval-{date}-{target}.md` | - |
| L2 | Rubric | `craft/rubric.md`（→ L3 にも置く） | knowledge |
| L2 | Reader Persona | `craft/reader-personas.md` | knowledge（persona の素） |
| L2 | Learning | `learning/{date}-{slug}.md` | knowledge（再利用時） |
| **L3** | Craft Library | `craft/*.md` | knowledge |
| L3 | Framework Index | `craft/framework-index.md` | knowledge（メタ情報） |
| L3 | Framework Lens（個別） | `craft/lenses/{name}.md` | knowledge（lens 採用時） |
| L3 | Motif Operations | `craft/motif-operations.md` | knowledge |
| L3 | Worksheets / Checklists | `craft/worksheets/` `craft/checklists/` | knowledge |
| **L4** | Approved | `approved/packet-NNN-epMM-{slug}.md` | - |
| L4 | Published | `published/packet-NNN-epMM-{slug}.md` | - |
| L4 | Kakuyomu Policy | `.claude/rules/kakuyomu-policy.md` | policy |
| **LR** | Workflow（TAKT yaml） | `.takt/workflows/*.yaml` | - |
| LR | Persona（TAKT facet 実装） | `.takt/facets/personas/*.md` | persona |
| LR | Policy（TAKT facet 実装） | `.takt/facets/policies/*.md` | policy |
| LR | Knowledge（TAKT facet 実装） | `.takt/facets/knowledge/*.md` | knowledge |
| LR | Instruction（TAKT facet 実装） | `.takt/facets/instructions/*.md` | instruction |
| LR | Task | `.takt/tasks/*.yaml` | - |
| LR | Run | `.takt/runs/*.ndjson` | - |
| LR | Candidate | `drafts/candidates/packet-NNN-epMM/{persona}.md` | - |
| LR | Selection Report | `drafts/candidates/packet-NNN-epMM/_selection.md` | - |
| LR | Integrated Draft | `drafts/packet-NNN-epMM-{slug}.md`（最終一本） | - |
| LR | Ledger（live state） | `ledger/`（★ 新設） | knowledge（読み）+ instruction（更新時） |

---

## 4. Ledger 配置（新設詳細）

Pack B 由来の Ledger は本 v3 で正式に配置を確定する:

```
ledger/
├── README.md                    - Ledger の使い方・更新タイミング
├── canon-facts.yaml             - 確定事実
├── timeline.yaml                - 時系列イベント
├── character-states/
│   └── {char-id}.yaml           - キャラ毎の知識状態・関係温度
├── foreshadowing-status.yaml    - 各伏線の現状（仕込/匂/強/回収済）
├── open-questions.yaml          - 制作中に出た未解決問い
├── author-decisions.yaml        - author が下した判断ログ
└── rejected-ideas.yaml          - 没案保存（誤って canon 化しないため）
```

**Bible との分離原則**:

- Bible は **書き始める前に決まっている安定設定**
- Ledger は **書きながら確定・更新される実装状況**
- 同じ事実が両方にある場合、Bible が先 / Ledger が後（後発の発見・確定）

---

## 5. .takt/ 配置（TAKT 用）

```
.takt/
├── config.yaml                  - プロジェクト設定（provider / model / language）
├── workflows/
│   ├── episode-draft-tournament.yaml
│   ├── packet-assembly-review.yaml
│   ├── arc-strategy-tournament.yaml
│   └── ...
├── facets/
│   ├── personas/
│   │   ├── faithful-writer.md
│   │   ├── emotional-writer.md
│   │   ├── plot-drive-writer.md
│   │   ├── reviser.md
│   │   ├── judge.md
│   │   ├── ledger-keeper.md
│   │   └── reader-persona-{a,b,c}.md
│   ├── policies/
│   │   └── （`.claude/rules/*.md` と `bible/rules.md` への参照）
│   ├── knowledge/
│   │   └── （craft/* / bible/* / ledger/* への参照）
│   └── instructions/
│       └── （scene_card / acceptance_contract への参照テンプレ）
├── tasks/
│   └── {task-id}.yaml          - 積まれたタスク
└── runs/
    └── {run-id}.ndjson          - 実行履歴
```

> **重要**: `.takt/facets/policies/` `.takt/facets/knowledge/` は **本体ではなく参照**。本体は `.claude/rules/` `bible/` `craft/` 側にあり、`.takt/` 側はそれをロードするポインタのみ。**二重管理を防ぐ**。

---

## 6. kernel と非 kernel の境界線

### kernel に入る（Layer 1 の中でも特に薄い核）

`story/kernel.yaml` に入るもの = 11 項目だけ:

1. premise
2. promise（reader_promise）
3. protagonist_vector（want / need / wound）
4. conflict（external / internal / relational）
5. stakes
6. change_model
7. causality
8. information_design（must_be_clear / intended_unknowns）
9. emotional_arc
10. style_voice
11. unit_tree

詳細は `04_kernel_spec.md`。

### kernel に入らない（Layer 1 の他のもの）

- bible 全部（characters / world / rules）
- genre_overlay
- project_override
- packet 詳細
- episode 詳細
- scene card / acceptance contract（Adapter 出力で kernel から派生）
- foreshadowing_map / reveal_plan / cadence_plan
- ledger（実装中の状態）

### kernel に絶対入らない（Layer 2/3/4/R 全般）

- review 各種
- craft / framework
- 公開済本文
- TAKT workflow yaml
- 候補 draft / 選抜報告 / 統合 draft

---

## 7. 「kernel に入れるか入れないか」の判定基準

新しいフィールドが提案されたとき、以下を順に問う:

```
Q1. このフィールドが無いと、執筆を 1 文字も始められないか?
    Yes → kernel 候補
    No  → bible / overlay / lens / craft のどれか

Q2. このフィールドは作品ジャンルに関係なく必要か?
    Yes → kernel 候補
    No  → genre_overlay or framework_lens

Q3. このフィールドは作品固有の例外・美学の話か?
    Yes → project_override
    No  → 他

Q4. このフィールドは制作中に発生する状態か?
    Yes → ledger
    No  → 他

Q5. このフィールドは review 時の判定軸か?
    Yes → rubric / craft
    No  → 他

Q6. このフィールドは特定の創作流派（Snowflake / Story Grid 等）固有か?
    Yes → framework_lens
    No  → 他
```

**全ての No が Q1〜Q3 で続いた → kernel に入れない**。kernel は薄く保つ。

---

## 8. ファイル位置の判断ガイド

迷ったら:

| 内容 | 置き場所 |
|---|---|
| 安定した作品設定 | `bible/` |
| 制作中に確定する状態 | `ledger/` |
| 設計時の意図台帳 | `story/{foreshadowing-map, reveal-plan}.md` |
| 作品 1 文要約・約束 | `story/promises.md` + `story/kernel.yaml` |
| 中規模設計 | `arcs/` |
| 章束設計 | `packets/` |
| Episode 設計 | `scenes/slotted/` |
| 本文 | `drafts/` |
| 公開準備 | `approved/` |
| 公開済 | `published/` |
| 評価軸・原理 | `craft/` |
| MUST / 禁則 | `.claude/rules/` |
| 実行 yaml | `.takt/workflows/` |
| 反省・学び | `learning/` |
| 大量入力 | `story/intake/` |
| 再利用核 | `story/seeds/` |
| 未解決論点 | `story/open-questions.md` |
| 設計負債 | `story/design-debt.yaml` |
| Bible 改訂提案 | `story/canon-patch-proposals/` |
| Adapter 設定（次セッション） | `.takt/adapter/` または `prompts/adapter/` |

---

## 9. Pack A / Pack B からの差分

### Pack A 4+1 → 本 v3 4+1.5+1

- Layer 1.5（Adapter）を新設
- Layer R は維持

### Pack B からの統合

- Adapter / Domain Synthesis / Acceptance Contract / Judge / Ledger を Layer 配置済
- Framework Index / Framework Lens を Layer 3 craft 配下に新設

### TAKT facet の組み込み

- 4 facet（persona / policy / knowledge / instruction）が Layer R 内で機能
- 既存の Layer 1-4 の本体は変えず、`.takt/facets/` は参照のみ

---

## 10. 既存 Pack A v2 の 28 骨格ファイルとの関係

Pack A v2 の `07-skeleton/` の骨格ファイルは本 v3 に以下のように対応:

| Pack A v2 骨格 | 本 v3 での扱い |
|---|---|
| `manifest/template.manifest.v2.json` | そのまま使用 |
| `rules/intake-flow.md` | そのまま使用 |
| `rules/review-system.md` | そのまま使用 |
| `rules/vocabulary-lint.md` | 本 v3 `01_vocabulary.md` に整合させてアップデート |
| `rules/monitoring-dictionary-generic.md` | そのまま使用 |
| `story/intake/*.yaml`, `digest-template.md`, `reflection-ledger.md` | そのまま使用 |
| `learning/current-focus.yaml` | そのまま使用 |
| `packets/task-context-template.yaml` | TAKT task と統合検討（次セッション） |
| `reviews/*-template.md` | そのまま使用 |
| `prompts/intake/*.md` | そのまま使用 |
| `prompts/review/*.md` | そのまま使用 |
| `craft/README.md` | そのまま使用、craft library 中身は Phase 2 で埋める |

**重複・衝突なし**。本 v3 は Pack A v2 の骨格を素直に使える。
