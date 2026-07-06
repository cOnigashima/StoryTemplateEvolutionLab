# proposal/ — 提案（履歴 + アクティブ）

> **役割**: StoryTemplateEvolution への過去・現在の設計提案を保管する場所。
> **採用 / 未採用**: 各提案の status は下表で管理。

---

## 提案 status 一覧

| 提案 | 日付 | status | 備考 |
|---|---|---|---|
| `2026-04-22-story-template-v2/` | 2026-04-22 | **historic / partially-absorbed** | v2-fat。Layer 構造と Review Matrix の発想を v3/v4 に継承 |
| `2026-04-29-domain-kernel-v3/` | 2026-04-29 | **historic / superseded by v4** | kernel 11 項目・status 11 値・DoR DoD は v4 が継承。v4 採用後は archive 候補 |
| `2026-04-29-pilot-driven-evolution/` | 2026-04-29 | **historic / methodology** | 「pilot から抽象化する」方針。v4 もこの方法論に乗る |
| `2026-04-30-zero-base-v4/` | 2026-04-30 | **★ ADOPTED (2026-04-30)** | ドメイン語彙・DoR・pipeline の正本として現役。構造・運用面は 2026-07-06 提案が置換 |
| `2026-04-31-storytemplate_workflow_handoff_pack_takt/` | 2026-04-31 | **historic / partially-absorbed** | TAKT 接合 Pack。v4 採用時は見送り → 2026-07-06 提案が TAKT ループを暫定採用し部分継承 |
| `2026-07-06-workbench-ontology-loop/` | 2026-07-06 | **★ ADOPTED (2026-07-06)** | current を全面置換（オントロジー基盤 / TAKT ループ / core+overlay / 人間ゲート）。旧 current は `archive/2026-04-31-integreated/` へ |

---

## status の意味

| status | 意味 | アクション |
|---|---|---|
| **proposed** | 提案中、author レビュー前 | author に raise |
| **under_review** | author レビュー中 | author 判断待ち |
| **adopted** | 採用済み（current の根拠になっている） | current 配下と sync 維持 |
| **historic** | 採用後に置き換えられた、または部分採用 | 履歴として保存、編集禁止 |
| **rejected** | 却下 | archive に下ろす |
| **archived** | 用途終了 | `../archive/proposal/` へ |

---

## 各提案の概要

### 2026-04-22-story-template-v2/ — v2-fat

- 4+1 Layer 構造（Source / Authoring / Review / Craft / Runtime）
- 25 項目 rubric、Craft Library 提案
- 重装備すぎて単独採用は見送り、要素は v3/v4 に分散吸収

### 2026-04-29-domain-kernel-v3/ — v3-kernel

- 「kernel を薄く保つ」方針
- 11 項目 kernel、status 11 値、DoR DoD、Adapter 2 分割
- 用語整理（vocabulary.md の元）
- v4 が直接継承

### 2026-04-29-pilot-driven-evolution/ — 方法論提案

- 「設計室で完成させない、pilot 実走から抽象化する」
- renji を最初の pilot として運用
- v4 では pilot を ia_society / ore_tueee / fools の 3 作品に拡大

### 2026-04-30-zero-base-v4/ — ADOPTED ★

- 4 論点（Learning / 二軸モデル / Bible vs Ledger / 設計と本文配置）の決着
- 56 語の Card 書式によるユビキタス言語
- Bible Facet 17 体制（System / Timeline / Sample Scene 新設）
- 三本柱（current / proposal / archive）の物理構造
- 86 項目の Intake Coverage Checklist
- DoR-A / DoR-B / DoR-C の機械的判定
- 7 本の review prompt
- 3 作品の pilot validation walkthrough

→ **2026-04-30 に正式採用**。ドメイン語彙（56 語 Card）・DoR/DoD・intake checklist の正本として現役。
→ 構造・運用面（ディレクトリ / ループ / ゲート）は 2026-07-06 提案が置換。

### 2026-04-31-storytemplate_workflow_handoff_pack_takt/ — historic

- TAKT 実行エンジンとの接合 Pack（Adapter / Judge / Ledger 概念、Framework Index 戦略）
- v4 採用時は「TAKT は opt-in」で見送り
- 2026-07-06 提案が TAKT ループを暫定採用し、発想を部分継承

### 2026-07-06-workbench-ontology-loop/ — ADOPTED ★

- 旧 current を**全面置換**する新 current（workbench で試作 → 統合）
- オントロジー基盤（`template/core/schema` + `state` + `tools/ontology_check.py`、非gating）
- TAKT ループ（`takt/`、暫定）＋人間は成果物だけ見るゲート（G-Intake / G-Deliverable / G-Publish）
- core + overlay + work.manifest（作品ごとの執筆単位差を吸収、逸脱は理由付き明示）
- 継承の主張は `../current/INHERITANCE.md` と `COVERAGE.md`
- status 語彙を 11→12 値に拡張（rejected + genre_not_applicable 両立、2026-07-06 決定）

→ **2026-07-06 に採用**。旧 current は `archive/2026-04-31-integreated/` に凍結。

---

## 採用 / 却下 / archive のフロー

```
[新規提案]
    ↓
proposal/{date}-{slug}/ に置く
    ↓
[author レビュー]
    ├── 採用 → status: adopted、current/ に反映、Phase 1/2/3 実行
    ├── 却下 → status: rejected → archive/proposal/ へ移動
    └── 部分採用 → status: historic、要素が current/ に分散吸収

[時間経過 + 別の提案で置き換え]
    ↓
status: historic → archived（archive/proposal/ へ移動）
```

---

## 提案執筆規約

新しい提案を追加する場合:

- ディレクトリ名: `{YYYY-MM-DD}-{slug}/`
- 必須ファイル: `00_README.md`（提案の入口）
- 番号 prefix で読み順を示す（00_ / 01_ / 02_ / ...）
- 採用判断のための DoD を明示
- 4 論点形式（議論ポイント + 決着）を推奨
- archive 候補となった旧提案への supersede 関係を明記

---

## 関連参照

- `../README.md` — リポジトリ全体の三本柱説明
- `../current/README.md` — 現在の正本
- `../archive/README.md` — 凍結された旧資産
