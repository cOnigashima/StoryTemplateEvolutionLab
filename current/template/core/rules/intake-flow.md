# Intake Flow Rule

> **追加候補**: 本ファイルは `.claude/rules/intake-flow.md` として各作品 repo の `.claude/rules/` に追加する候補。
> **起源**: renji pilot で抽象化（2026-04-29）。

---

## このルールの本旨

大量入力（企画チャット / 既存設計資料 / 断片メモ）を受け入れるとき、**raw を直接 bible に流さない**。必ず以下の順序で精製する。

```
inbox/  →  synthesis/session_digests/  →  synthesis/update_proposals/
                                                  ↓
                                           Human Approval
                                                  ↓
                                bible/ design/ state/ への確定反映
```

---

## MUST

1. **大量 raw 入力は inbox/ に保存する**。bible/ に直接書き込まない
2. **Intake Adapter Prompt を経由する**（adapter/intake_adapter.md）
3. **session_digest は synthesis/session_digests/ に**（加工後の構造化）
4. **更新案は synthesis/update_proposals/ に**（反映前の差分）
5. **bible への反映は必ず human approval を経る**（adapter/human_approval_policy.md）
6. **status を必ず付ける**（12 値、docs/status_vocabulary.md）
7. **trace を残す**（全項目に source 参照）

## SHOULD

1. **更新案を作るときに「現在の bible / state / design に対する差分」を明示する**
2. **contradiction は解消せず、author に上げる**
3. **intentionally_hidden と missing を区別する**
4. **rejected を明示的に記録する**（state/rejected_ideas.md）
5. **作品固有装置（三層対応 等）を generic 化しない**

## 禁止

1. inbox を空にする / 削除する
2. bible に raw 入力をそのまま貼る
3. 推測で bible を埋める（「自然な解釈」を確定として書く）
4. update_proposal を作らずに bible を直接書き換える
5. status 区別を省く
6. trace 参照を省く

---

## 違反した場合の対応

- bible に raw が混入していたら → synthesis/ 経由でやり直し
- 推測値が bible に書かれていたら → status: tentative に格下げ + design/open_design_questions.md に論点として記録
- contradiction を解消した結果が canon になっていたら → rollback + author 判断を仰ぐ

---

## ワークフロー（標準）

```
1. 企画チャット / 既存資料 / 断片メモ を inbox/planning_sessions/ に保存
2. Intake Adapter Prompt を実行
3. session_digest が synthesis/session_digests/ に出力される
4. update_proposal が synthesis/update_proposals/ に出力される
5. author が読む
6. approve / partial-approve / revise / reject の判断
7. approved 分のみを bible/design/state に反映
8. ledger-keeper が必要に応じて state を更新
9. retrospective を learning/ に記録
```

---

## 関連ファイル

- `adapter/intake_adapter.md` — 入口プロンプト
- `adapter/update_proposal_format.yaml` — 反映案フォーマット
- `adapter/human_approval_policy.md` — 自動 / 人間境界
- `docs/status_vocabulary.md` — 12 status（正本）


---

## v4 での更新（2026-04-30）

- 86 項目の Intake Coverage Checklist を必ず通す → `proposal/2026-04-30-zero-base-v4/05_intake_coverage_checklist.md`
- 12 status 値（filled / tentative / deferred / intentionally_blank / intentionally_hidden / not_applicable / genre_not_applicable / project_override / contradiction / needs_author_decision / missing / rejected）— 正本は `docs/status_vocabulary.md`（基底 11 値は `proposal/2026-04-30-zero-base-v4/02_domain_model.md` Section 12、2026-07-06 に 12 値へ拡張）
- Intake Adapter prompt は v4 化済 → `current/adapter/intake_adapter.md`
- 7 review prompt で intake 出力を機械検証 → `proposal/2026-04-30-zero-base-v4/07_review_prompts/`
- Bible Facet 17 体制（System / Timeline / Sample Scene 新設）→ intake で各 facet に振り分ける際に注意
- 採用後の正本フロー: `proposal/2026-04-30-zero-base-v4/04_pipeline_overview.md`
