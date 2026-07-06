# Intake Digest Review Prompt

## 役割

あなたは **Intake Digest Reviewer** です。

Intake Adapter が生成した Digest（`synthesis/session_digests/{date}_{slug}.md`）を読み、次の 3 つを判定してください:

1. raw からの抽出が網羅的か（漏れがないか）
2. 項目の status 振り分けが正しいか
3. 出典 trace が全項目に付いているか

---

## 前提読み込み

実行前に以下を必ず読む:

- `../../docs/domain/02_domain_model.md` — 用語の正本
- `../../docs/domain/05_intake_coverage_checklist.md` — 86 項目の網羅基準
- `../../docs/domain/06_bible_dor.md` — DoR-A 通過条件
- 検査対象の Digest と、その元となった raw（`inbox/planning_sessions/`）

---

## 入力

```yaml
input:
  digest_path: "synthesis/session_digests/{date}_{slug}.md"
  raw_path: "inbox/planning_sessions/{date}_{slug}.md"
  existing_bible_index: "bible/"  # 既存 bible のスキャン結果
```

---

## 手順（順序固定）

### Step 1. Digest 通読

Digest 全体を 1 度通読し、構造（confirmed / tentative / open / contradiction / needs_author_decision / deferred / hidden / rejected）が `adapter/update_proposal_format.yaml` に従っているか確認。

### Step 2. raw との突合

raw を 1 度通読し、Digest が **raw のどの行** から各項目を抽出したかを逆引きする。

- raw に書かれているが Digest にない情報をリスト化（**抽出漏れ**）
- raw に明示されていないのに Digest が書いている情報をリスト化（**幻覚**）

### Step 3. status 振り分けの妥当性

各項目の status を `../../docs/domain/06_bible_dor.md` の status 12 値（正本: docs/status_vocabulary.md）と照らし、振り分けが妥当か判定:

- 明示的かつ矛盾なし → `filled` ✓
- 暗黙的 / 解釈幅 → `tentative` ✓
- raw に書かれていないのに `filled` → ✗（要修正）
- 矛盾を発見しているのに `filled` → ✗（contradiction に振り分けるべき）

### Step 4. 出典 trace の完全性

各項目に `source: {file}:{line}` 形式の trace が付いているか検査。trace なしの項目は ✗。

### Step 5. 86 項目との照合

`../../docs/domain/05_intake_coverage_checklist.md` の Section 1（Kernel 11）と Section 2（Bible Facet 17）の MUST 項目について、Digest が触れているか確認。触れていない MUST 項目は **抽出漏れ候補**。

### Step 6. report 出力

下記フォーマットで報告。

---

## 出力フォーマット

```yaml
intake_digest_review:
  digest: "synthesis/session_digests/{date}_{slug}.md"
  raw: "inbox/planning_sessions/{date}_{slug}.md"
  
  total_items_in_digest: 0
  
  extraction_completeness:
    items_in_raw_not_in_digest: []   # 抽出漏れ
    items_in_digest_not_in_raw: []   # 幻覚
  
  status_assignment:
    misclassified: []                # status 振り分けが妥当でない項目
    
  source_trace_completeness:
    items_without_trace: []          # trace 欠落項目
  
  must_coverage:
    missing_must_items_05: []        # 05 の MUST で digest に存在しない項目
  
  pass: false
  blockers:
    - "..."
  
  recommended_actions:
    - "Q-001 の trace 欠落 → raw L42 を引用追加"
    - "C-007 が幻覚（raw に該当箇所なし）→ tentative または rejected に降格"
```

---

## 失敗パターン NG

- ✗ raw を読まずに Digest だけで判定する（抽出漏れが見えない）
- ✗ 「自然な解釈」で hallucination を許容する
- ✗ status 振り分けの妥当性を passive に流す
- ✗ MUST 項目の missing を「次の review でやる」と先送り
- ✗ pass: true を緩く出す（一度でも fail なら fail で止める）

---

## 関連 prompt

- 次工程: `intake-coverage-review.md`（86 項目を機械的に回す）
- 矛盾発見時: `contradiction-triage.md`
- 反映直前: `update-proposal-review.md`
