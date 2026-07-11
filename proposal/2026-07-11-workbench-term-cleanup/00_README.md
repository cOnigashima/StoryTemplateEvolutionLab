# Proposal: 正本からの実験コードネーム "workbench" 除去

- **Status**: adopted（2026-07-11 承認・適用済み。B 5箇所＋C-2 3箇所を置換、A/C-1 据え置き。retro=`current/learning/2026-07-11-workbench-term-cleanup.md`）
- **Date**: 2026-07-11
- **Slug**: workbench-term-cleanup
- **前提**: current/ は 2026-07-06 workbench 統合後の正本。本提案は current/ への Patch 案であり、承認（人間ゲート）まで current/ は変更しない。
- **規律**: `.claude/rules/repository-discipline.md` MUST#4「supersede stub を直接書き換えない」/ MUST#2「三本柱の境界維持」に対応。current/ の編集は本 proposal 経由。

---

## 1. 課題

実験のコードネーム **`workbench`** が、正本層 `current/` に混入している（全 **26 箇所 / 16 ファイル**）。

### workbench の本来の定義（＝正本性を持たない実験場）

`proposal/2026-07-06-takt-deep-dive/old/PROPOSAL.md`:

> - **2系統を混ぜない**: 作品への reverse flow …は workbench 内で完結。StoryTemplate へ昇格するのは**ワークフロー・facet・policy の学びのみ**
> - workbench は .gitignore 済み。**正本性を持たない実験場**として維持

`proposal/2026-07-06-takt-deep-dive/00_README.md:9`:

> **workbench** = 俺TUEEE を作る場所。具体・底がある。実体化・執筆・実走はここ。

→ workbench は定義上、**俺TUEEE学園という特定作品を回すための gitignore された非正本サンドボックス**。

### 混入した瞬間（single point of failure）

- 昇格の掟は「抽象化した **ワークフロー・facet・policy の学びのみ** を current へ」。
- ところが実際は commit `213ebbe "chore: refresh story template workspace"` で **139 ファイル / 9,381 行を全部 `A`（新規）** 一括ダンプ（`current/` だけで 106 ファイル）。`current/takt/README.md` はこのコミット以前に存在しない＝差分マージではなく**まっさら→丸ごと投入**。
- 結果、**抽象化ステップを飛ばして** workbench 語が schema/state 雛形の1行目まで浸透。

**要点**: workbench 自身が掲げた「2系統を混ぜない／正本性を持たない」というルールが、workbench を正本化する操作（chore 一括ダンプ）によって破られた。

### なぜ危険か

- 正本 `current/` は本来どの実験からも中立であるべき。実験名が正本のアイデンティティを名乗ると、後続セッション/AI が **「正本＝workbench の一実装」** と誤読する。
- 特に `template/core/schema/*` は各作品にコピーされて拡散するため、実験名が全作品に伝播する。

---

## 2. 方針（author 確認済み: 2026-07-11）

出現 26 箇所を性質で3分し、扱いを変える。

| 区分 | 内容 | 扱い | author 判断 |
|---|---|---|---|
| **A. 履歴・パス参照** | proposal フォルダ名 `2026-07-06-workbench-ontology-loop`、learning 決着記録 | **残す**（固有名詞・出典） | 確定 |
| **B. 実験フレーミング漏れ** | 「今の運用環境そのもの」を workbench と呼ぶ箇所 | **全置換**（中立語へ） | ✅ 確定 |
| **C-1. `origin:` 統制語彙** | `origin: workbench`（由来メタ、8ファイル） | **残す (a)**（由来ラベルとして実害小・触ると schema 全部動く） | ✅ 確定 |
| **C-2. 「workbench 統合」イベント呼称** | 過去の統合イベントの名前（3箇所） | **(b) 言い換え**（「正本統合」へ） | ✅ 確定（2026-07-11） |

---

## 3. Patch 詳細

### B. 全置換（確定）

| file:line | before | after |
|---|---|---|
| `current/CLAUDE.md:29` | `## 2. 人間確認ポリシー（★このworkbenchの肝）` | `## 2. 人間確認ポリシー（★この運用の肝）` |
| `current/takt/README.md:20` | `## 2. workbench でTAKTが担うもの` | `## 2. StoryTemplate 運用でTAKTが担うもの` |
| `current/takt/README.md:31` | `| 概念 | 意味 | workbench での置き場 |` | `| 概念 | 意味 | 作品ワークスペースでの置き場 |` |
| `current/takt/README.md:77` | `## 6. workbench 同梱の workflow` | `## 6. 同梱の workflow` |
| `current/takt/config.example.yaml:6` | `# 実行ログ・レポートの出力先（workbench の logs に集約）` | `# 実行ログ・レポートの出力先（作品側の logs に集約）` |

### A. 残す（確定・無変更）

- `current/CLAUDE.md:70` / `INHERITANCE.md:4` / `README.md:36` / `WORKFLOW.md:213` — パス参照
- `current/learning/2026-07-06-workbench-integration.md`（:1 :5 :12 ＋ファイル名） — 決着記録（append-only）
- `current/learning/README.md:31` — 上記への索引

### C-1. `origin:` タグ（確定・無変更）

以下は由来メタとして残す:
- `current/CLAUDE.md:71`（タグ定義 `STE-v4 / workbench / fools / villainess`）
- `current/INHERITANCE.md:9` / `template/README.md:40`
- `template/core/schema/entity_schema.yaml:1` / `relations.yaml:1`
- `template/core/state/entities.yaml:1` / `knowledge_state.yaml:1` / `timeline.yaml:1`
- `adapter/human_approval_policy.md:1`

### C-2. 「workbench 統合」呼称（✅ (b) 確定 2026-07-11）

「workbench 統合」→「正本統合」に言い換え。

| file:line | before（該当語） | after 案 (b) |
|---|---|---|
| `current/INHERITANCE.md:8` | `… **workbench で**新規/再編` | `… 2026-07-06 の**正本統合で**新規/再編` |
| `current/WORKFLOW.md:5` | `更新日: 2026-07-06（**workbench 統合**・…）` | `更新日: 2026-07-06（**正本統合**・…）` |
| `current/docs/status_vocabulary.md:6` | `2026-07-06 の **workbench 統合**で rejected を加え` | `2026-07-06 の **正本統合**で rejected を加え` |

---

## 4. DoD（採用判断の基準）

- [ ] B の 5 箇所を置換後、`grep -rn "workbench" current/` の残存が **A + C-1（＋C-2 の author 判断次第）** のみになる
- [ ] `origin:` 統制語彙（`CLAUDE.md:71` の4値）は不変。schema/state 雛形の1行目も不変
- [ ] 置換により current/ 内の相互参照・見出しリンクが壊れていない（`/consistency-check` 相当）
- [ ] C-2 の可否が author 判断で確定している

## 5. 適用手順（承認後）

1. B の 5 箇所を Edit で置換。
2. C-2 が (b) 承認なら 3 箇所を追加置換。
3. `learning/2026-07-11-workbench-term-cleanup.md` に retro 記録（原因＝抽象化スキップの一括ダンプ、再発防止＝「置換」でも昇格ルートを通す）。
4. 本 proposal の status を adopted に更新し、`proposal/README.md` 台帳に反映。
