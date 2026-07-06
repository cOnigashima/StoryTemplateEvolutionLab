# 07-skeleton — 骨格ファイル雛形

本ディレクトリは、v2 で新規追加または大幅更新するファイルの **骨格（skeleton）** を保持する。本提案が承認されたら、これらを template の該当パスにコピー展開して初期状態を作る。

## ディレクトリ対応表

| skeleton ファイル | 展開先 |
|---|---|
| `manifest/template.manifest.v2.json` | `template.manifest.json` |
| `rules/intake-flow.md` | `.claude/rules/intake-flow.md` |
| `rules/review-system.md` | `.claude/rules/review-system.md` |
| `rules/vocabulary-lint.md` | `.claude/rules/vocabulary-lint.md` |
| `rules/monitoring-dictionary-generic.md` | `.claude/rules/monitoring-dictionary-generic.md` |
| `story/intake/raw-index.yaml` | `story/intake/raw-index.yaml` |
| `story/intake/digest-index.yaml` | `story/intake/digest-index.yaml` |
| `story/intake/provenance.yaml` | `story/intake/provenance.yaml` |
| `story/intake/reflection-ledger.md` | `story/intake/reflection-ledger.md` |
| `story/intake/digest-template.md` | `story/intake/digests/digest-template.md` |
| `learning/current-focus.yaml` | `learning/current-focus.yaml` |
| `packets/task-context-template.yaml` | `packets/templates/task-context-template.yaml` |
| `prompts/intake/*.md` | `prompts/intake/*.md` |
| `prompts/review/*.md` | `prompts/review/*.md` |
| `reviews/*.md` | `reviews/*.md` |
| `craft/README.md` | `craft/README.md` |
| `craft/*.md` | `craft/*.md`（本 skeleton では目次 + 入口 1 枚のみ、各章の詳細は別パッケージで埋める） |

## 注意

本 skeleton は **最小実行可能な骨** を目指す。実際の運用で肉付けが必要:

- craft/*.md の本文は `know_how_explore/` から移植。本 skeleton には README と目次のみ置く
- review-system.md / intake-flow.md / vocabulary-lint.md は本提案 `04`/`03`/`02` ファイルの要約版
- skeleton ファイル内の `<TODO>` は展開時に作品固有情報で埋める
