# Layer × Facet マップ

> Layer 0-4+R + Adapter 2 分割。
> 各概念の置き場とファイル配置。
> 詳細は v3 `03_layer_facet_map.md`。

---

## Layer 構成

```
Layer 0   Intake             大量入力受付（raw / digest / seed）
Layer 1   Core Authoring     物語の中身（kernel + bible + structure）
Layer 1.5 Adapter            kernel + state → workflow 入力への変換 ★
Layer 2   Review-Learning    レビュー + 学習
Layer 3   Craft              創作原理（道具箱）+ Framework Lens カタログ
Layer 4   Release            公開準備 + 公開済
Layer R   Runtime            TAKT 実行・候補・選抜・統合・台帳（opt-in 隔離）
```

Layer R の opt-in 隔離原則: TAKT 不在でも Layer 0-4 で完結する。

---

## Adapter 2 分割（v3 → v3+ 更新）

```
Layer 1.5: Adapter
  ├─ Intake Adapter:
  │    自由 chat / raw → bible/design/state 更新案
  │    
  └─ Writing Adapter:
       bible/state → 1 episode 用 Writing Pack
```

- Intake Adapter は **書く前の取り込み**
- Writing Adapter は **書く前の圧縮**
- 両方とも human approval を経る

---

## TAKT facet との対応

TAKT prompt は 4 facet に分解:

| facet | 役割 | Story Template での source |
|---|---|---|
| persona | エージェント役割（writer / judge 等） | prompts/personas/ |
| policy | MUST / 禁則 | .claude/rules/ + bible/rules.md |
| knowledge | 参照する事実・原理・設定 | bible/* + craft/* + ledger/* |
| instruction | この step で何をするか | scene_card + acceptance_contract |

---

## Layer × ファイル位置マトリクス（要点）

| Layer | 主概念 | ファイル位置 |
|---|---|---|
| L0 | Raw | inbox/planning_sessions/ |
| L0 | Digest | synthesis/session_digests/ |
| L0 | Update Proposal | synthesis/update_proposals/ |
| L1 | Kernel | story/kernel.yaml |
| L1 | Promise | story/promises.md |
| L1 | Bible | bible/ 配下全部 |
| L1 | Genre Overlay | bible/genre-overlay.md |
| L1 | Project Override | bible/project-override.md |
| L1 | Arc / Packet / Episode 設計 | arcs/, packets/, scenes/, drafts/ |
| L1 | Foreshadowing Map | bible/plot/foreshadowing_map.md |
| L1.5 | Adapter 出力 (scene_card) | scenes/slotted/ |
| L1.5 | Adapter 出力 (acceptance_contract) | reviews/contracts/ |
| L2 | Reviews 各種 | reviews/ |
| L2 | Rubric | craft/rubric.md |
| L3 | Craft Library | craft/ |
| L3 | Framework Index/Lens | craft/framework-index.md, craft/lenses/ |
| L4 | Approved | approved/ |
| L4 | Published | published/ |
| LR | Workflow YAML | .takt/workflows/ |
| LR | Persona / Facet | .takt/facets/ |
| LR | Task / Run | .takt/tasks/, .takt/runs/ |
| LR | Ledger | ledger/ |

---

## kernel と非 kernel の境界

### kernel に入る（Layer 1 の中でも特に薄い核）

11 項目のみ（→ `kernel_spec.md`）

### kernel に入らない（Layer 1 の他）

bible 全部 / overlay / override / packet / episode 詳細 / scene_card / contract / foreshadowing_map / reveal_plan / cadence_plan / ledger

### kernel に絶対入らない（Layer 2/3/4/R 全般）

review 各種 / craft / framework / 公開済本文 / TAKT yaml / 候補 / 選抜 / 統合

---

## 「どこに置く?」迷ったとき

| 情報の性質 | 行先 |
|---|---|
| 安定した作品設定 | `bible/` |
| 制作中に確定する状態 | `state/` (= ledger) |
| 設計時の意図台帳 | `bible/plot/{foreshadowing_map, reveal_plan}.md` |
| 作品 1 文要約・約束 | `story/promises.md` + `story/kernel.yaml` |
| 中規模設計 | `arcs/` |
| 章束設計 | `packets/` |
| Episode 設計 | `scenes/slotted/` |
| 本文 | `drafts/` |
| 公開準備 / 公開済 | `approved/`, `published/` |
| 評価軸・原理 | `craft/` |
| MUST / 禁則 | `.claude/rules/` |
| 実行 yaml | `.takt/workflows/` |
| 反省・学び | `learning/` |
| 大量入力 | `inbox/` |
| 構造化 digest | `synthesis/` |
| 揺れる設計 | `design/` |
```

---

## Adapter は本リポジトリのどこ?

- **設計書（汎用）**: `StoryTemplateEvolution/adapter/`
- **作品ごとの利用設定**: 各作品の `.adapter/` (renji の場合 `works/renji/.adapter/`)

設計書は generic、利用は作品 local。
