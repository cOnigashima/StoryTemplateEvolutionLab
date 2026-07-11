# 2026-07-11 — 正本からの実験コードネーム "workbench" 除去

> origin: workbench-term-cleanup（proposal/2026-07-11-workbench-term-cleanup/）

## 何が起きていたか

実験のコードネーム `workbench`（＝俺TUEEE学園を回すための gitignore された**非正本サンドボックス**）が、正本層 `current/` に **26 箇所 / 16 ファイル**混入していた。特に §2 見出し「workbench でTAKTが担うもの」のように、**正本の運用環境そのものを実験名で名乗る**箇所があった。

## 原因（single point of failure）

- workbench 自身の掟は「2系統を混ぜない／StoryTemplate へ昇格するのは**抽象化したワークフロー・facet・policy の学びのみ**／workbench は正本性を持たない」（`proposal/2026-07-06-takt-deep-dive/old/PROPOSAL.md`）。
- ところが commit `213ebbe "chore: refresh story template workspace"` が **139 ファイル / 9,381 行を全部 `A`（新規）一括ダンプ**（`current/` だけで 106 ファイル）。差分マージではなく丸ごと投入。
- 結果、**「抽象化して昇格」すべきところを「chore で一括置換」が素通り**し、実験名が schema/state 雛形の1行目まで浸透した。
- **workbench が自分で掲げたルールを、workbench を正本化する操作が破った。**

## 対処（proposal 経由・author 承認済み 2026-07-11）

| 区分 | 扱い |
|---|---|
| B. 実験フレーミング漏れ（5箇所） | 中立語へ全置換（例: 「★このworkbenchの肝」→「★この運用の肝」／「workbench でTAKTが担う」→「StoryTemplate 運用でTAKTが担う」） |
| C-2. 「workbench 統合」呼称（3箇所） | 「正本統合」に言い換え |
| A. 履歴・パス参照 | 残す（proposal フォルダ名・learning 決着記録は固有名詞） |
| C-1. `origin:` タグ（8ファイル） | 残す（由来メタ。触ると schema 全体が動き実害に見合わない） |

適用後 `grep -rn workbench current/` は 26→17（A+C-1 のみ）。

## 再発防止（教訓）

1. **「置換（whole-replace）」でも昇格ルートを通す。** current/ への大量投入を `chore: refresh` で行わない。実験名・作品固有語が混じっていないかを投入前に grep で検査する。
2. **正本語彙は実験から中立に保つ。** 実験のコードネームは proposal/ に閉じる。current/ の見出し・本文に実験名が出たら赤信号。
3. **`origin:` タグは例外**として実験名を由来ラベルに使ってよい（機能的メタ）。ただし本文の運用語彙とは区別する。

## 関連

- `proposal/2026-07-11-workbench-term-cleanup/00_README.md` — 本件の Patch 提案（根拠）
- `2026-07-06-workbench-integration.md` — 混入元となった統合の決着記録
- `.claude/rules/repository-discipline.md` — MUST#2/#4/#6（境界維持・stub・facet 流入防止）
