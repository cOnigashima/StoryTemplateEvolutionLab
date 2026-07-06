# レビュー依頼プロンプト（別セッション用）

このファイルの本文を、新しいセッション（Claude Code / Cowork / codex 等）にそのまま貼って使う。
目的: 新 `workbench/current/` が「元 StoryTemplateEvolution を正しく踏襲しつつ、オントロジー/ループ/コア+オーバーレイを整合的に組めているか」を第三者視点で監査させる。

---

## ここから貼り付け ↓↓↓

あなたは Story OS テンプレートの監査レビュアーです。読み取り専用で作業してください（Read / Grep / Glob / bash の cat・ls のみ。ファイルは書き換えない。computer use・Finder は使わない）。要約に頼らず、必ず実ファイルを開いて根拠を引用してください。

### 対象
- 新正本（レビュー対象）: `kakuyomu_platrom_20260706_統合試作/workbench/current/`
- 設計提案: `kakuyomu_platrom_20260706_統合試作/workbench/proposal/2026-07-06-workbench-ontology-loop/`（PROPOSAL.md / COVERAGE.md / 00_現状把握マップ.md / 01_オントロジー適用の見立て.md）
- 比較元（旧正本）: `kakuyomu_platrom_20260706_統合試作/StoryTemplateEvolutionのコピー/current/` と `.../proposal/2026-04-30-zero-base-v4/`

### 前提
新 current は旧 STE current を**置換**するもの。旧資産は極力コピーで踏襲し、そこに「オントロジー基盤 / TAKTループ / コア+オーバーレイ / 人間は成果物だけ見るゲート」を足している。継承の主張は `current/INHERITANCE.md` と `proposal/.../COVERAGE.md` に書かれている。

### レビューしてほしい観点（各項目、PASS / PASS WITH NOTES / FAIL ＋ 根拠ファイル引用）

1. **踏襲の完全性**: COVERAGE.md の差分表は実態と合っているか。旧 current にあって新 current に無い/劣化した要素が他に無いか、独立に洗い出す。特に:
   - status 語彙（Field 11値・Judge 4値・Lock 5状態・遷移規則）が完全か
   - unit taxonomy（Manuscript→Beat、最小条件、サイズ、ID命名）
   - Layer 0-4+R × Facet マップ
   - kernel_spec の 11項目 MUST/SHOULD と judgement 木
   - DoR/DoD（A/B/C・E/P/A）と status×DoR 表
   - Bible Facet 17 の完全リスト
   - agents 18 / skills 7 / rules 6 / checklists 3 / prompts 7 / craft / v4 review prompts 7 / intake coverage 86項目
2. **整合性（内部矛盾）**: 重複や矛盾が無いか。特に DoR/DoD が複数箇所（`template/core/checklists/dor_dod.md` / `docs/dor_dod.md` / `docs/v4/06_bible_dor.md`）にあり正本がどれか曖昧でないか。kernel 記述の不一致。
3. **参照の生死**: コピーした旧ファイル内の相対リンク（`proposal/2026-04-30-zero-base-v4/...` 等）が新 current 内で解決するか。切れているものを列挙。
4. **新レイヤの妥当性**:
   - オントロジー: `template/core/schema/*` と `state/*` と `tools/ontology_check.py` が噛み合っているか。`python3 current/tools/ontology_check.py current/template/core` を実行し、検出内容が妥当か。
   - コア+オーバーレイ: core と overlay の境界宣言（`work.manifest`）が機能するか。作品固有(work-local)との三分が明確か。
   - 人間ゲート: G-Intake / G-Deliverable / G-Publish が旧 DoR/DoD と矛盾しないか。
   - TAKT（暫定）: workflow YAML が facet を正しく参照しているか。過剰設計でないか。
5. **「新作を1本立ち上げられるか」テスト**: `work_init/new-work-bootstrap.md` と `template/folder_structure.md` に従えば、迷いなく作品フォルダを作れるか。抜けている手順・雛形は何か。
6. **原則の維持**: 「ファイルが正本」「空欄禁止＝status明示」「raw直投入禁止」「1話に全bible渡さない」「レビューは採否まで」が新 current 全体で貫かれているか。

### 出力形式
```
## 監査サマリ（PASS/NOTES/FAIL の数）
## 観点別レビュー（1〜6、各: 判定＋根拠ファイル:行＋具体指摘）
## 新たに発見した欠落・劣化（COVERAGE未記載のもの）
## 切れている参照リンク一覧
## 優先度付き 修正提案（Must / Should / Nice）
```

最後に「この current は旧STEの正本を置換するに足るか」を一文で結論してください。
