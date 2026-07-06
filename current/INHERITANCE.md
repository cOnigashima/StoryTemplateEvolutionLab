# INHERITANCE — 元StoryTemplateEvolution からの継承マップ

この new current は StoryTemplateEvolution/current を**置換**する。置換にあたり、元の資産は極力そのまま継承した。
このファイルは「何が元から来て、新レイヤとどう噛み合うか」を示す。差分の詳細は `../proposal/2026-07-06-workbench-ontology-loop/COVERAGE.md`。

## 由来の見分け方
- `docs/`, `agents/`, `skills/`, `prompts/`, `craft/`, `adapter/review_prompts/`, `adapter/*_format.yaml` … **元STEからのコピー（踏襲）**。
- `template/`（core+overlay+runtime）, `tools/ontology_check.py`, `takt/`, `WORKFLOW.md` の一部 … **workbench で新規/再編**。
- 各ファイル冒頭の `origin:` タグ（STE-v4 / workbench / fools / villainess）も参照。

## 元STE current → new current 対応

| 元 STE current/ | new current/ | 関係 |
|---|---|---|
| docs/（kernel_spec, unit_taxonomy, status_vocabulary, layer_facet_map, dor_dod, vocabulary） | docs/（同名でコピー） | 仕様の正本。踏襲 |
| （v4 proposal の 00-10） | `../proposal/2026-04-30-zero-base-v4/`（正本のまま参照） | STE 統合により docs/v4 コピーは廃止（2026-07-06） |
| adapter/（prompt + format類） | adapter/（intake/writing は再編、format類はコピー） | 混在。format は踏襲 |
| agents/（18） | agents/（18コピー） | 温存。TAKT persona へ写像予定 |
| skills/（7） | skills/（7コピー） | 温存。TAKT workflow へ写像予定 |
| rules/（6） | template/core/rules/（6：2再編+4コピー） | 踏襲 |
| checklists/（3） | template/core/checklists/（3） | 踏襲 |
| prompts/（7） | prompts/（7コピー） | テンプレ進化メタ手順。踏襲 |
| craft/ | craft/ | 踏襲 |
| templates/ | template/core・overlay | 再編（core+overlay）＋実体テンプレをコピー |
| work_init/ | work_init/ | 再編 |
| WORKFLOW.md | WORKFLOW.md | 更新 |

## 新レイヤとの噛み合わせ
- **オントロジー**（tools/ + template/core/state + schema）は、元の state（character_states/foreshadowing/timeline）を **ID + relation語彙で formalize** したもの。情報は包含し、検査可能性を足した。
- **TAKT**（takt/）は、元の agents/skills/rules を **persona/policy/knowledge/instruction/output_contract の facet** に写して、ループ実行できるようにする層。**暫定**。元 agents/skills は消さず温存。
- **コア+オーバーレイ**は、元の「単一 v4 構造」を、作品ごとの執筆単位差（episode-pack / packet-2stage）を吸収できるよう2層化したもの。kernel・DoR/DoD・facet・status語彙といった芯は共通(core)に据える。

## 未完（COVERAGE 第3節に対応）
DoR-DoD 正本の一本化（stub は `proposal/2026-04-30-zero-base-v4/06_bible_dor.md` を指す。checklists/dor_dod.md との関係整理が残） / agents↔facets 対応表 / craft rubric 実体化。
※ 相対リンク張り替えは STE リポジトリ統合（2026-07-06）で解消 — `proposal/2026-04-30-zero-base-v4/` が同一リポジトリに実在するため、53 件の参照はそのまま生きる。
