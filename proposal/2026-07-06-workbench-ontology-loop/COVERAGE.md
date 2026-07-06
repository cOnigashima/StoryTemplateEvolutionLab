# COVERAGE — 元StoryTemplateEvolution/current の踏襲チェック

作成: 2026-07-06 / 目的: 新 current が元 STE current（+v4提案）を取りこぼしていないかの突き合わせ結果。
判定は要約でなく**実ファイル**で行った。

---

## 0. 総評

初版の新 current は「新しい思想（オントロジー / ループ / コア+オーバーレイ / 人間ゲート）」はよく入っていたが、
**元STEの精密資産をかなり取りこぼしていた**（要約からの再構築によるドリフト）。
本コミットで、元ファイルを**そのままコピーして継承**し、欠落を解消した。以下がその記録。

---

## 1. 差分表（初版 → 継承後）

| 元STEの要素 | 初版での状態 | 対応 | 継承後の場所 |
|---|---|---|---|
| status 語彙（Field 11値 / Judge 4値 / Lock 5状態 / 決定木 / 権限境界 / 遷移規則） | ✗ 部分（5値のみ言及） | 元docsをコピー | `current/docs/status_vocabulary.md` |
| unit taxonomy（Manuscript→Beat、最小条件、サイズ、ID命名、Scene Card警告） | △ overlayで暗示のみ | コピー | `current/docs/unit_taxonomy.md` |
| Layer 0-4+R × Facet マップ、置き場マトリクス | ✗ 欠落 | コピー | `current/docs/layer_facet_map.md` |
| kernel_spec（全11項目schema・MUST/SHOULD・kernel除外・判定木） | △ 簡略版（ドリフト） | 元の完全版に差替 | `current/docs/kernel_spec.md` + `template/core/kernel.template.yaml` |
| DoR/DoD 完全版（A/B/C・E/P/A、status×DoR表、reverse flow） | △ E中心・簡略 | v4正本をコピー | `current/docs/v4/06_bible_dor.md` |
| Bible Facet 17体制の完全リスト | △ 約10facet | v4/domain_model + facetテンプレ | `current/docs/v4/02_domain_model.md` + `template/core/bible/_facet_templates/` |
| agents 18本 | △ 約7に集約 | 18本コピー | `current/agents/` |
| skills 7本 | ✗ workflowに吸収 | 7本コピー | `current/skills/` |
| rules 6本（file-growth/intake-flow/learning-capture/story-os-boundaries 欠落） | △ 2本のみ | 欠落4本コピー | `current/template/core/rules/` |
| checklists 3本（packet_freeze / work_dramatic_principles 欠落） | △ 1本 | 2本コピー | `current/template/core/checklists/` |
| adapter フォーマット（update_proposal / writing_pack / field_mapping） | ✗ 欠落 | 3種コピー | `current/adapter/` |
| v4 review prompts 7本 | ✗ 欠落 | コピー | `current/adapter/review_prompts/` |
| intake coverage checklist（86項目） | ✗ 欠落 | コピー | `current/docs/v4/05_intake_coverage_checklist.md` |
| template-evolution meta prompts（session_start 他6本） | ✗ 欠落 | コピー | `current/prompts/` |
| craft（rubric / framework lens） | ✗ 欠落 | コピー | `current/craft/` |
| episode_pack 4テンプレ（実体） | △ 説明のみ | コピー | `template/overlay/unit-episode-pack/*.template.md` |
| domain_model 56語 / storage_trinity / pipeline | ✗ 欠落 | v4コピー | `current/docs/v4/02,03,04` |

---

## 2. 意図的に「変えた」もの（踏襲でなく上書き。理由付き）

| 元 | 新 | 理由 |
|---|---|---|
| state（character_states / foreshadowing / timeline template） | オントロジー版（entities/knowledge_state/…+ID+relation語彙） | オントロジー基盤化（01_見立て）。元の情報は包含しつつ ID/relation を追加 |
| agents/skills を .claude で運用 | TAKT facets/workflow へ写像（暫定） | ループ化。ただし元agents/skillsも `current/agents,skills` に温存（消していない） |
| 単一構造 | コア+オーバーレイ | fools/villainess の分岐統合（PROPOSAL 第2節） |
| DoRのみ | DoR + 3人間ゲート | 「人間は成果物だけ見る」運用 |

---

## 3. 残TODO（次セッションで詰める）

- **参照パスの張り替え**: コピーした元STEファイル内の相対リンク（`proposal/2026-04-30-zero-base-v4/...` 等）は STE 前提。新 current 内で解決するよう貼り直す。
- **重複の一本化**: `template/core/checklists/dor_dod.md`（私版）と `docs/dor_dod.md`（supersede stub→v4）と `docs/v4/06_bible_dor.md`（正本）が併存。正本を v4 に一本化し私版はstub化する。
- **kernel整合**: `template/core/kernel.template.yaml`（元の完全版に差替済）と私が書いた簡略 kernel の記述を全docで統一。
- **agents/skills と takt facets の対応表**: 18 agents・7 skills が takt の persona/workflow のどこに写るかを明示（現状 `INHERITANCE.md` に骨子）。
- **craft/lenses の中身**: 元 craft は README+lenses ディレクトリのみ。rubric 実体は evaluation-lab と接続して育てる。

---

## 4. 検証方法（再現可能）

```bash
# 元STE current と新 current のファイル系統を比較
ls StoryTemplateEvolutionのコピー/current
find workbench/current -type f | sort
```
本チェックは `review-prompt.md`（別セッション用）で第三者が再監査できる。

---

## 5. STE リポジトリ統合後の決定・追記（2026-07-06 統合作業）

workbench → StoryTemplateEvolutionLab 本体への統合（新 current = リポジトリ直下 `current/`、旧 current は `archive/2026-04-31-integreated/` に凍結）に伴う決定:

1. **§3「参照パスの張り替え」は統合で解消**。`proposal/2026-04-30-zero-base-v4/`（07/08/10 含む完全版）が同一リポジトリに実在するため、53 件の参照はそのまま解決する。張り替え不要。
2. **`current/docs/v4/` は削除**（proposal との完全重複だったため）。v4 ドキュメントの正本は `proposal/2026-04-30-zero-base-v4/` に一本化。`INHERITANCE.md`・`current/README.md` の参照を更新済み。
3. **status 語彙を 11→12 値に拡張**: `rejected` と `genre_not_applicable` を両立。正本は `current/docs/status_vocabulary.md`（decision tree / 権限表 / 遷移ルールも rejected 対応済み）。「11 値」表記は current 全体で 12 値に更新済み。v4 02_domain_model Section 12（基底 11 値）は履歴として不変。
4. **§4 の検証コマンドは旧パス**（workbench 前提）。統合後は `ls archive/2026-04-31-integreated` と `find current -type f | sort` で読み替える。`review-prompt.md` の対象パスも同様に読み替え（再監査時に更新）。

（同日追記）再監査で発見された workbench 圧縮時の劣化4ファイル（drafter-preflight / human_approval_policy / episode_acceptance / kakuyomu-policy）は archive 版から復元マージ（詳細: `current/learning/2026-07-06-workbench-integration.md`）。learning 二層構造を導入し `current/learning/` を復活。repo 直下 `inbox/` は `improvement_request_inbox/` に改名。
