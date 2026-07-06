# current — 新 StoryTemplate 正本

これは StoryTemplateEvolution の `current/` を置き換える新しい正本。
新セッションのAIは `WORKFLOW.md`（1枚ガイド）→ `CLAUDE.md`（運用契約）の順で読む。

## 正本一覧

| 場所 | 役割 | 由来 |
|---|---|---|
| `WORKFLOW.md` | ★1枚ガイド。全体像と1周の流れ | 更新 |
| `CLAUDE.md` | AI運用契約（人間確認・共通化・統合・オントロジー） | 新規 |
| `INHERITANCE.md` | 元STEからの継承マップ（何が踏襲で何が新規か） | 新規 |
| `docs/` | 仕様の正本（kernel_spec / unit_taxonomy / status_vocabulary / layer_facet_map）。ドメインモデル詳細（56語 / storage_trinity / pipeline / DoR-DoD / intake checklist 86項目）は `../proposal/2026-04-30-zero-base-v4/` が正本 | ★STE踏襲 |
| `work_init/new-work-bootstrap.md` | 新作の立ち上げ（current をコピー→別フォルダ） | 再編 |
| `template/` | 新作がコピーする雛形（core＋overlay＋runtime）。完全構造は `template/folder_structure.md` | 再編＋踏襲 |
| `adapter/` | チャット→セッション引き渡し（intake/writing/handoff/approval）＋フォーマット3種＋`review_prompts/`（7本） | 再編＋★STE踏襲 |
| `agents/` | generic エージェント18本（plotter/drafter/critic…） | ★STE踏襲（TAKT facetへ写像予定） |
| `skills/` | generic スキル7本（draft/critic/continuity/release…） | ★STE踏襲（同上） |
| `prompts/` | テンプレ進化メタ手順（session_start / improve / audit / extract / apply / consistency） | ★STE踏襲 |
| `craft/` | 創作原理の道具箱（rubric / framework lens） | ★STE踏襲 |
| `takt/` | ループ実装。**暫定・別セッションで確定** | 新規 |
| `tools/` | 検査ツール（ontology_check.py） | 新規 |

## 旧 StoryTemplateEvolution/current との対応

- 旧 `templates/` `docs/` `adapter/` → 本 `template/` `adapter/`（core+overlay で再編）
- 旧 `agents/` `skills/` → 本 `agents/` `skills/` に**温存**（TAKT `takt/facets/personas/` への写像は予定・暫定。実体は移動していない）
- 旧 `rules/` `checklists/` → `template/core/rules` `template/core/checklists`（中身入りで再整備）
- 新規: `template/core/schema` `template/core/state`（オントロジー基盤）、`tools/ontology_check.py`

置換の根拠は `../proposal/2026-07-06-workbench-ontology-loop/PROPOSAL.md`。
