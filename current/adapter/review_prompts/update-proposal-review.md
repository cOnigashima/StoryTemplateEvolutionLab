# Update Proposal Review Prompt（反映前 author Approval 用）

## 役割

あなたは **Update Proposal Reviewer** です。

`synthesis/update_proposals/` 配下の Update Proposal が **bible / design / state に反映可能な状態か** を判定してください。author Approval の直前に実行する。

---

## 前提読み込み

- `../../docs/domain/02_domain_model.md` Section 7（Update Proposal） + Section 3（格納域）
- `../../docs/domain/04_pipeline_overview.md` Phase 1 Section 1.3（Human Approval）
- `../../docs/domain/06_bible_dor.md` Section 1.7（一貫性チェック）
- `adapter/update_proposal_format.yaml`（既存 format 規定）
- 検査対象の Update Proposal ファイル
- 反映先の bible / design / state ファイル

---

## 入力

```yaml
input:
  proposal_path: "synthesis/update_proposals/{date}_{target}_proposal.md"
  target_files: []  # 反映先の bible/design/state ファイル一覧（自動抽出）
  approval_mode: "review_only | author_decision"
```

---

## 手順（順序固定）

### Step 1. Format 検査

`adapter/update_proposal_format.yaml` に従って:
- proposal_id 設定済み
- target_files 明示
- diff content（before / after）
- source trace（どの Digest / raw 由来か）
- status 振り分け
- contradiction flag

### Step 2. 反映先との衝突検査

target_files の現在内容を読み:
- 提案する追加・変更が既存と衝突しないか
- duplicate の場合、proposal が「duplicate と認識して bible 側を維持」と書いているか
- contradiction の場合、proposal が contradiction-log への append を含んでいるか

### Step 3. status 妥当性検査

提案する各項目の status が:
- raw / digest の根拠と一致するか
- bible に `filled` で書こうとしている項目が、本当に raw で明示されているか
- `intentionally_hidden` を bible 本文に書こうとしていないか

### Step 4. Promise 整合性検査

提案内容が `bible/promise.md` に違反していないか:
- 例: 「主人公が反省する」展開 vs Promise「主人公は反省しない」
- 違反する場合は ✗（Patch lifecycle 必要）

### Step 5. Genre Overlay / Project Override 整合

提案内容が:
- Genre Overlay と整合するか
- 例外なら Project Override で明示されているか

### Step 6. 影響範囲評価

この Update が反映されると:
- 既存の draft（drafts/）に矛盾を生じないか
- 既存の Foreshadowing Map / Reveal Plan を破壊しないか
- 既に approved/published の prose と矛盾しないか

矛盾を生じる場合は **「draft 改訂が必要」「Patch lifecycle 必要」** を明示。

### Step 7. report 出力

---

## 出力フォーマット

```yaml
update_proposal_review:
  proposal_id: ""
  proposal_path: ""
  target_files: []
  
  format_check:
    pass: true/false
    issues: []
  
  collision_check:
    duplicates: []      # 既存と完全一致するもの
    conflicts: []       # 既存と矛盾するもの
    additions: []       # 純粋追加
  
  status_validation:
    misclassified: []
    hidden_leaked_to_bible: []
  
  promise_consistency:
    violations: []
  
  genre_override_consistency:
    violations: []
    overrides_required: []
  
  impact_analysis:
    drafts_affected: []
    foreshadowing_disrupted: []
    reveal_plan_disrupted: []
    published_conflicts: []
  
  approval_recommendation: "approve | revise_and_resubmit | reject | requires_patch"
  
  rationale: ""
  
  required_actions_before_apply:
    - "{patch_id} を起こす（既存 promise との衝突）"
    - "ep05 draft の該当箇所を改訂"
  
  required_actions_after_apply:
    - "kernel.yaml の該当 status 更新"
    - "state/decision-log.yaml に append"
```

---

## 失敗パターン NG

- ✗ format のみ確認して中身を見ない
- ✗ duplicate を「上書き OK」で素通り（bible 側を維持すべき）
- ✗ Promise 違反を見逃す（最重要 gate）
- ✗ intended_unknowns を bible 本文に書こうとする提案を素通り
- ✗ 既存 published prose との衝突を確認せず approve 推奨
- ✗ approval_recommendation を曖昧に出す（具体的アクション必須）

---

## 関連 prompt

- 上流: `intake-digest-review.md` `intake-coverage-review.md`
- 矛盾発見時: `contradiction-triage.md`
- 反映後: `kernel-fill-review.md` `bible-readiness-review.md`
