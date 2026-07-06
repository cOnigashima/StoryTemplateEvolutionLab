# 設計詳細: 作品ライフサイクルの接合とTAKT境界

> 作品の立ち上げ → 執筆 → Lab への還元、の各接合点をハーネスに載せる設計。
> TAKT の深掘り（workflow YAML 確定・loop_monitors 実装）は**別セッション**。ここでは境界（インターフェース）だけ固定する。

## 1. ライフサイクル全体図とハーネス接点

```
[立ち上げ]   /new-work (Lab skill)      → works/{slug}/ 生成 + G-Intake
     ↓
[執筆ループ] /pitch → /draft → /critic → /continuity → /review-meeting
             （対話的・単発 = Claude Code ハーネス）
             takt -w draft-episode 等（無人ループ = TAKT）→ G-Deliverable
     ↓
[公開]       /release → G-Publish
     ↓
[還元]       /retro-meeting（作品側）→ runtime/logs/learning/
             /improve-from-work (Lab skill) → proposal → current 更新
     ↓
[追随]       /apply-to-work (Lab skill) → 既存 work へ current 更新を適用提案
```

原則: **人間ゲート 3 つ（G-Intake / G-Deliverable / G-Publish）はどのハーネスからも自動通過しない**。skill は「ゲート前で止まり、人間に確認を求める」ところまでを自分の DoD に含む。

## 2. 立ち上げのハーネス化 — Lab skill `/new-work`

`work_init/new-work-bootstrap.md` の手順 1-8 を skill 化する（手順書は正本として残し、skill はそれを実行する）。

```markdown
---
name: new-work
description: >
  新作品フォルダを立ち上げる。「新作を始めたい」「作品を立ち上げて」で起動。
  current/template を複製し、manifest・kernel・.claude/ を初期化、
  ontology_check まで通して G-Intake の確認事項を人間に提示して止まる。
---
```

この skill は手順書のコピーではなく**対話プロトコル**（04_design_guidance.md §5）: 人は事前に「何が必要か」を知らなくてよく、skill が質問し、チェックを回し、不足を status 集計から自動生成して提示する。

skill の実行内容（bootstrap 手順 + 今回の追加分）:

1. slug / タイトル / overlay 選択 / 置き場所を人間に質問（AskUserQuestion 相当）
2. `current/template/` から core / overlay / runtime を複製、`work.manifest.json`・`core/kernel.yaml` へリネーム
3. **`template/core/.claude/` → 作品ルート `.claude/` へ複製し、CLAUDE.md の {{placeholder}} を置換**（Phase 1 成果物との接合）
4. manifest 記入: slug / `uses_core_version` / overlays / deviations（空で開始）
5. `python3 tools/ontology_check.py works/{slug}/core` 実行、warning を要約提示
6. DoR-A チェックリストを提示し、**G-Intake の判断材料を並べて停止**（承認は人間）

## 3. 立ち上げ後の接合 — work ↔ Lab の同期

### 3.1 バージョン固定と追随

- 作品は複製時点の current を固定して使う（`uses_core_version`）。current が進化しても作品は勝手に変わらない
- 追加提案: manifest に `template_snapshot_date` を追記（"0.1" だけでは複製時点が特定できないため）
- current 更新後の追随は Lab skill `/apply-to-work`（prompts/04 由来）が担当: 対象 work の manifest を読み、current との差分から「適用提案リスト」を作って人間に提示。**自動適用はしない**（deviations と衝突しうるため）

### 3.2 還元（進化ループ）の skill 接合

| 接合点 | 作品側 | Lab 側 |
|---|---|---|
| 学びの記録 | `/retro-meeting` が `runtime/logs/learning/` に learning を出力（learning-capture rule 準拠） | — |
| 昇格候補の抽出 | — | `/improve-from-work`（prompts/01 由来）が learning を読み、generic 化できるものを選別 |
| 汎用化 | — | `/extract-pattern`（prompts/03 由来）で作品固有語を除去 → 56語 Card 準拠か検査 |
| 正本反映 | — | `/new-proposal` で proposal 化 → 人間承認 → current へ Patch |

reverse-flow rule の「packet 以上の遡上は learning + proposal に送る」が作品→Lab の受け渡し規約。skill 側は learning の出力フォーマットに **「昇格候補フラグ + 根拠（何話で効いたか）」** を必須フィールド化し、`/improve-from-work` が機械的に拾えるようにする。

### 3.3 セッション接合 — `/handoff`（作品側 skill、8本目）

`adapter/session_handoff.template.md` を skill 化: セッション終了時に CURRENT / OPEN / DELIVERABLES待ち / 直近 run を埋めて `runtime/logs/sessions/` に保存。次セッションの CLAUDE.md 参照順に「最新 handoff を最初に読む」を追記。これで**セッションを跨ぐ接合**もハーネスに載る。

## 4. TAKT との境界（本提案で固定する範囲）

### 4.1 責務分界

| | Claude Code ハーネス（本提案） | TAKT（別セッション） |
|---|---|---|
| 性格 | 対話的・単発作業 | 無人ループ実行（見張り番の廃止） |
| 実体 | .claude/ skills / agents / rules | workflows/*.yaml + facets |
| 使いどころ | pitch・単発 draft・個別レビュー・retro・release・handoff | draft→検査→review→修正の反復、packet-cycle |
| 人間 | skill がゲート前で停止 | deliverables/ 出力時のみ（G-Deliverable） |

**同じ工程の 2 実装**（例: /draft と draft-episode.yaml）は「skill = 手動運転、TAKT workflow = 自動運転」の関係。内容の正は skill 側（＝旧 skills/ 手順書）に置き、facet はそこから派生する。乖離は harness_map の「同期ペア」列 + retro でチェック。

### 4.2 本提案で固定するインターフェース（TAKT 側実装は触らない）

1. **起動**: skill から TAKT に渡すときは「`takt -w {workflow} "{task}"` を提示して人間に実行させる」まで。skill が takt を勝手に起動しない（無人ループ開始は人間の判断）
2. **ログ共有**: TAKT の `runs_dir` は作品の `runtime/logs/runs/` を指す（config.example.yaml の `../logs/runs` を folder_structure と整合させる）。`/handoff` と `/retro-meeting` はここを読む
3. **成果物**: TAKT の出力は `runtime/drafts/` `runtime/reviews/` に落ち、G-Deliverable は人間が見る。skill 側（/critic 等）は TAKT 出力も同じフォーマットで受け取れること（output_contracts/review_ticket と review skill の票形式を一致させる）
4. **facets 同期ペア**: harness_map §2 の対応表で宣言（persona:drafter ↔ agent:drafter、policies/review_gate ↔ rules/review-gate 等）

### 4.3 別セッションに送るもの（deferred）

- workflows/*.yaml の確定（現状「叩き台」宣言のまま）
- loop_monitors の実装・打ち切り閾値
- config.yaml の正本化・step別モデル戦略（クロスレビュー）
- 未整備 facet（continuity / retro / release 系）の追加
- skill ↔ facet の自動同期（生成）を仕組み化するか

## 5. 本設計による PROPOSAL への追加分

- Phase 1 に追加: 作品側 skill 8本目 `/handoff`、CLAUDE.md 雛形の参照順に「最新 handoff」追加、manifest テンプレに `template_snapshot_date`
- Phase 2 に追加: Lab skill `/new-work`、learning フォーマットへの昇格候補フラグ追加（learning-capture rule 更新）、config.example.yaml の runs_dir 整合確認
- harness_map §2 に「同期ペア」列（4.2-4 の宣言場所）
