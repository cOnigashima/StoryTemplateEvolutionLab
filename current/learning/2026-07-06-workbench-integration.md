# 2026-07-06 — workbench 統合の決着記録

## 何をしたか

`proposal/2026-07-06-workbench-ontology-loop/` の採用により、workbench で試作した新 current がリポジトリ直下 `current/` を全面置換。旧 current は `archive/2026-04-31-integreated/` に凍結。

## 統合時の決定（根拠は COVERAGE.md §5 と本ファイル）

1. **docs/v4 コピーは削除** — `proposal/2026-04-30-zero-base-v4/` が同一リポジトリに実在するため正本を一本化。53 件の相対参照は統合により自然解決。
2. **status 語彙 11→12 値** — `rejected` と `genre_not_applicable` を両立。正本は `current/docs/status_vocabulary.md`。
3. **痩せた4ファイルの復元マージ** — workbench 圧縮版で消えたディテールを archive から復元:
   - `drafter-preflight.md`（216→25→復元）: Multi-Pass Self-Review・meta欄テンプレ・focalizer規則
   - `human_approval_policy.md`（196→16→復元）: 操作カテゴリ別 AUTO/HUMAN マトリクス・status別判定（12値化）・影響度判定・エスカレーション
   - `episode_acceptance.template.md`（121→23→復元）: ID/verifiable_by/source 表・severity・QG-01〜09・判定サマリ
   - `kakuyomu-policy.md`（63→8→復元）: AI利用タグ3種の具体名・頻度数値・コンテスト注意（2025-11 時点キャベット付き）
   - 教訓: **要約再構築はディテールを落とす**。圧縮した場合は「何を捨てたか」を COVERAGE に明記する。
4. **learning 二層構造** — 作品retro は `works/{slug}/runtime/logs/learning/`、STE 側の決着記録は `current/learning/`（本フォルダ復活、旧retro 4本コピー復元）。
5. **inbox → improvement_request_inbox 改名** — 作品側 inbox 概念との混同を防ぐ。

## 残TODO（次に効くもの）

- DoR-A の新構造対応版（v4 の35項目ディレクトリ検査が core+overlay 配置と不整合）→ DoR/DoD 一本化と同時に
- bible facet 命名の一本化（README ⇄ _facet_templates ⇄ v4 17 facet）+ System/Timeline/Sample Scene テンプレ
- design/ 4雛形・state/rejected_ideas 雛形・packet-2stage overlay の実体
- ontology_check.py の宣言済み constraints 実装（required_fields / Event 参照整合 / relation 語彙 / state 不在時のエラー化）
- prompts/00_session_start.md の旧環境前提の全面書き直し
