# Design Audit Prompt（Bible 設計監査）

## 役割

あなたは **Design Auditor** です。

drafts ではなく、**Bible / Design / State の設計成果物そのもの** を監査対象とし、次の 4 つの破綻を検出してください:

1. **空疎**（埋まっているが内容がない）
2. **矛盾**（facet 間の論理破綻）
3. **管理破綻**（intentionally_hidden の管理ミス、Promise 違反、Patch 漏れ）
4. **整合性破綻**（kernel と bible の sync 不全、bible と State Implementation の乖離）

実行タイミング:
- 定期（packet 1 つ完了ごと、Arc 完了時）
- Patch 適用直後
- DoR-A 判定の前段（最終確認）
- bible audit 要求時

---

## 前提読み込み

- `02_domain_model.md` 全部
- `03_storage_trinity.md`（物理配置）
- `05_intake_coverage_checklist.md`
- `06_bible_dor.md`
- 検査対象の `bible/` `design/` `state/` 全体

---

## 入力

```yaml
input:
  work_root: "{work directory}"
  audit_scope: "full | bible_only | facet:{name}"
  triggered_by: "scheduled | post_patch | pre_dor_a | manual"
  prev_audit_log: "reviews/audits/{previous_date}-design-audit.md"  # 任意
```

---

## 手順（順序固定）

### Step 1. ファイル inventory

work_root の bible / design / state を walk し、ファイル一覧と更新日を取得。前回監査からの変更点を抽出。

### Step 2. 空疎検査（Emptiness Audit）

各 Bible facet ファイルについて:
- ファイル存在するが行数 < 10 → 要警告
- セクション headers のみ、本文 1 段落未満 → 要警告
- placeholder（"TODO" "未決定" "後で書く"）が大量 → 要警告

特に:
- `bible/promise.md` の items が `claim: ""` のまま → ✗
- `bible/theme.md` が question 1 つだけ → 要内容追加
- `bible/world/overview.md` が 3 行未満 → ✗

### Step 3. facet 間整合性検査

#### Promise vs Plot
- Plot の事象連鎖が Promise の項目を実際に守っているか
- 例: Promise「和解で閉じない」 vs Plot ending「和解する」

#### Promise vs Genre Overlay vs Project Override
- Promise が Genre 期待を破る場合、Project Override で明示されているか

#### Foreshadowing Map vs Reveal Plan vs Plot
- 伏線の植え位置 vs 開示位置の論理整合
- 伏線 X が ep18 で回収予定なのに、Reveal Plan が ep15 で公開している → 矛盾

#### Motif vs Theme
- Motif が Theme と関連しているか
- 関連なし → 削除候補 or Theme 補強

#### Bible.Foreshadowing-Map vs State.foreshadowing-implementation
- 設計と実装の乖離（設計は ep18 回収だが実装が ep15 で打ってる等）

#### Bible.Reveal-Plan vs State.reveal-implementation
- 同様の乖離検査

### Step 4. 管理破綻検査

#### intentionally_hidden の管理
- kernel.information_design.intended_unknowns に列挙されているものが
- bible 本文に「うっかり書かれていない」か
- Reveal Plan に「reveal 予定」として登録されているか
- 全 reveal 予定が prose 内で実装されているか

#### Promise 違反検査（過去 prose）
- approved/published の prose を grep し、Promise 違反らしき箇所がないか
- 例: Promise「主人公は反省しない」 vs ep05「主人公が泣きながら謝罪」

#### Patch 漏れ検査
- bible に修正が入った形跡があるが state/canon-patch-log.yaml に entry がない → ✗（Patch 経由ルール違反）

### Step 5. 整合性破綻検査

#### kernel ↔ bible sync
- kernel.logline.value vs bible/logline.md
- kernel.promise.items vs bible/promise.md
- kernel.style_voice vs bible/style-voice.md
- kernel.protagonist_vector vs bible/characters/{protagonist}.md
- 不一致を検出

#### Bible facet 内 sync
- bible/theme.md と bible/promise.md の主題整合
- bible/style-voice.md と bible/rules.md の禁則重複 / 矛盾

### Step 6. ファイル成長検査

`.claude/rules/file-growth.md` 規定で:
- 1 ファイル 300 行超 → 分割候補
- 関心軸が 2 つ以上混在 → 分割候補
- README が更新されず索引が古い → 要更新

### Step 7. 旧称・禁止語検査

- `premise:` フィールド残存（v3 → v4 未移行）
- `bundle` 単語混入
- `chapter`（内部）混入
- `Review` 単独使用
- `.adapter/` (dot あり、v4 では dot なし)

### Step 8. report 出力

---

## 出力フォーマット

```yaml
design_audit:
  audit_date: "YYYY-MM-DD"
  scope: "full"
  triggered_by: "pre_dor_a"
  
  inventory:
    bible_files: 0
    design_files: 0
    state_files: 0
    files_changed_since_last_audit: []
  
  emptiness:
    empty_or_thin_files: []
    placeholder_heavy_files: []
    issues:
      - file: "bible/promise.md"
        problem: "items に claim:'' が 2 件"
  
  facet_consistency:
    promise_vs_plot:
      status: ✓/✗
      violations: []
    promise_vs_genre_override:
      status: ✓/✗
      missing_overrides: []
    foreshadowing_vs_reveal_vs_plot:
      status: ✓/✗
      logical_conflicts: []
    motif_vs_theme:
      status: ✓/✗
      orphan_motifs: []
    bible_vs_state_implementation:
      foreshadowing_drift: []
      reveal_drift: []
      motif_drift: []
  
  management_integrity:
    intentionally_hidden:
      leaked_to_bible: []
      not_in_reveal_plan: []
      not_implemented_in_prose: []
    promise_violations_in_published:
      items: []
    patch_lineage:
      bible_changes_without_patch_log: []
  
  sync_integrity:
    kernel_bible_mismatch:
      logline: ✓/✗
      promise: ✓/✗
      style_voice: ✓/✗
      protagonist: ✓/✗
    bible_internal_sync:
      theme_promise_mismatch: []
      rules_style_voice_overlap: []
  
  file_growth:
    files_over_300_lines: []
    multi_concern_files: []
    stale_readmes: []
  
  legacy_naming:
    premise_field_remains: true/false
    bundle_word: []
    chapter_internal: []
    review_standalone: []
    dot_adapter: false
  
  overall:
    severity_high_count: 0
    severity_mid_count: 0
    severity_low_count: 0
    pass: false
  
  recommended_actions:
    immediate:
      - "bible/promise.md の items を埋める（claim 空 2 件）"
      - "kernel.style_voice と bible/style-voice.md の sync 修正"
    soon:
      - "bible/world/overview.md を 10 行以上に拡充"
    later:
      - "bible/foreshadowing-map.md を facet 別に分割（350 行超）"
  
  next_audit_due: "YYYY-MM-DD"
```

---

## 失敗パターン NG

- ✗ ファイル数だけ見て中身を見ない（emptiness 監査の skip）
- ✗ facet 間矛盾を「Patch でやる」と先送り（具体 Patch ID を出す）
- ✗ Promise 違反を「prose 改訂すれば良い」と軽視
- ✗ kernel ↔ bible sync を「自然に追従する」と勝手に処理
- ✗ recommended_actions の severity を曖昧にする（immediate / soon / later 区別必須）
- ✗ 過去 audit との差分を見ず、毎回同じ警告を繰り返す

---

## 関連 prompt

- 並走: `bible-readiness-review.md`（DoR-A 全体）
- 検出した矛盾の処理: `contradiction-triage.md`
- kernel 単独: `kernel-fill-review.md`
- 反映前: `update-proposal-review.md`
