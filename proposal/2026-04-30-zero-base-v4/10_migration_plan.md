# 10 Migration Plan — 採用後の移行手順 + 既存 work への適用順 + rollback

> **役割**: 本提案 v4 が author 承認された後の、StoryTemplate と既存 work の移行手順正本。
> **依存**: 01_supersession_map.md（取捨）+ 08_pilot_validation/（3 作品の walkthrough）+ 09_open_questions.md（未決）。
> **対象読者**: 採用承認後の移行作業者（author + LLM 協働）。

---

## 0. 移行スコープ

採用判断後の影響範囲:

```
┌──────────────────────────────────────────────┐
│  StoryTemplateEvolution/ （template 側）     │
│  - docs/ adapter/ templates/ prompts/ 更新   │
│  - archive/ 新設 + 旧資産退避                 │
└──────────────────────────────────────────────┘
                    │
                    ▼
┌──────────────────────────────────────────────┐
│  works/{各 work}/ （実作品側）                │
│  - ia_society / ore_tueee / fools-with-      │
│    cheating / renji（任意）                   │
└──────────────────────────────────────────────┘
```

両方を同時に動かす必要がある。template 先行 → works 段階追従が原則。

---

## 1. 採用判断 Gate

採用前に 09 の Q-A 4 件を必ず詰める:

```
□ Q-A-001 ディレクトリ命名 kebab-case で確定
□ Q-A-002 bible/plot.md デフォルト 1 ファイル
□ Q-A-003 二層ファイル separator: Markdown headers
□ Q-A-004 作品固有 facet は同階層配置 + README 識別
```

これらが author confirmed で「採用承認」状態。

---

## 2. Phase 1: StoryTemplate 側の移行（採用直後 1-3 日）

### Phase 1.1: Archive 作成

```bash
cd StoryTemplateEvolution/
mkdir -p archive/2026-04-30-pre-v4/{docs,adapter,templates,proposals}
```

### Phase 1.2: 旧 proposal の archive

```bash
# v2-fat と handoff を archive
mv proposals/2026-04-22-story-template-v2 archive/2026-04-30-pre-v4/proposals/
mv proposals/storytemplate_workflow_handoff_pack_takt archive/2026-04-30-pre-v4/proposals/

# v3-kernel と pilot-driven は keep（履歴として）
# proposals/2026-04-30-zero-base-v4 は本提案、最新として運用
```

### Phase 1.3: docs/ の supersede

```bash
# vocabulary を archive に退避、新は proposal を参照
cp docs/vocabulary.md archive/2026-04-30-pre-v4/docs/
# 新 vocabulary は proposal/.../02_domain_model.md を参照（docs/vocabulary.md は削除 or stub に）
echo "# Superseded — see proposal/2026-04-30-zero-base-v4/02_domain_model.md" > docs/vocabulary.md

# 同様に dor_dod
cp docs/dor_dod.md archive/2026-04-30-pre-v4/docs/
echo "# Superseded — see proposal/2026-04-30-zero-base-v4/06_bible_dor.md" > docs/dor_dod.md
```

### Phase 1.4: docs/ の refactor

`docs/kernel_spec.md` を v4 に更新:
- schema_version: "v4"
- `premise:` → `logline:` rename
- 11 項目の card 参照を新 02 へ向ける

`docs/layer_facet_map.md` を v4 に更新:
- 二軸モデル（案 Z）反映
- `bible/plot/` 廃止 → `bible/plot.md`
- adapter は dot なし

`docs/unit_taxonomy.md` を v4 に更新:
- Transformation Curve 追記
- Plot を Unit から外し Bible Facet に

`docs/status_vocabulary.md` keep（11 値継承）。

### Phase 1.5: adapter/ の refactor

`adapter/folder_structure.md` を archive に退避、新は 03 を参照:

```bash
cp adapter/folder_structure.md archive/2026-04-30-pre-v4/adapter/
echo "# Superseded — see proposal/2026-04-30-zero-base-v4/03_storage_trinity.md" > adapter/folder_structure.md
```

`adapter/intake_adapter_prompt.md` を v4 仕様に書き直し（Q-B-001）:
- 86 項目チェックリスト参照
- intake_coverage_report 出力
- version: v4 明示

`adapter/writing_adapter_prompt.md` を v4 体制に合わせて軽微修正。

`adapter/field_mapping_template.yaml` を更新:
- premise → logline
- 17 facet 体制への mapping 例

`adapter/update_proposal_format.yaml` を更新:
- 86 項目への trace 必須化
- status 11 値明示

### Phase 1.6: templates/ の refactor + 新規作成

```bash
cd StoryTemplateEvolution/current/templates/

# bible リネーム
mv bible/premise.template.md archive/2026-04-30-pre-v4/templates/
# 旧 premise.template.md は archive、新規 logline.template.md を作成
touch bible/logline.template.md
mv bible/reader_promise.template.md bible/promise.template.md
mv bible/genre.template.md bible/genre-overlay.template.md

# style_guide を分割
# bible/style_guide.template.md を読み、style-voice と rules に分割（手作業）

# 新規作成（13 ファイル）
touch bible/cadence-plan.template.md
touch bible/plot.template.md
touch bible/foreshadowing-map.template.md
touch bible/reveal-plan.template.md
touch bible/motif-ladder.template.md
touch bible/project-override.template.md
mkdir -p bible/system bible/timeline bible/samples bible/walkthroughs
touch bible/system/institutions.template.md
touch bible/timeline/history.template.md
touch bible/timeline/day-by-day.template.md
touch bible/samples/sample-scene.template.md
touch bible/walkthroughs/reading-order.template.md

# README templates
touch bible/README.template.md
touch design/README.template.md
touch state/README.template.md
touch arcs/README.template.md
touch packets/README.template.md
```

各 template の中身は logline / promise / theme / world / character / system 等の skeleton として埋める。`02_domain_model.md` の各 card を参照しつつ、各 facet の最小スケルトンを書く。

### Phase 1.7: prompts/ の refactor

`prompts/` 6 本のうち 4 本を v4 参照に更新:
- `00_session_start.md`: 4 論点と 56 語 card を踏まえた起動文
- `02_audit_gaps.md`: `07_review_prompts/design-audit-prompt.md` 連動
- `04_apply_to_new_work.md`: DoR-A v4 準拠
- `05_consistency_check.md`: `07_review_prompts/intake-coverage-review.md` 連動

### Phase 1.8: README.md 更新

トップレベルの README.md を v4 採用後の構成で書き直し。本提案 `proposal/2026-04-30-zero-base-v4/00_README.md` への導線を明示。

### Phase 1.9: craft/ 整備（Q-B-003）

`StoryTemplateEvolution/current/craft/` を新規作成:

```bash
mkdir -p craft/lenses
touch craft/README.md
touch craft/rubric.md
touch craft/framework-index.md
touch craft/scene-sequel.md
touch craft/pov-design.md
touch craft/foreshadowing-craft.md
```

各 work の `.claude/rules/` から共通の craft 知識を抽出して移植（30 日以内）。

### Phase 1.10: 検証

```bash
# 提案ファイルの内部リンクが切れていないか
# vocabulary / kernel_spec / dor_dod の supersede stub が機能しているか
```

---

## 3. Phase 2: 既存 work の移行（30 日以内）

### Phase 2.0: 移行優先順位

```
Priority 1: ia_society（最も状態が複雑、価値が高い）
Priority 2: ore_tueee_school_hell（中規模、移行が楽）
Priority 3: fools-with-cheating（充実 bible、リネーム中心）
Priority 4: renji（任意、archive も選択肢、Q-B-002）
```

### Phase 2.1: ia_society 移行（08-ia_society 参照）

`08_pilot_validation/ia_society_zero_state.md` の Step 1-10 を実行。

主要なステップ:
1. archive 取得
2. v4 ディレクトリ 11 個作成
3. actions/ → backlog/ rename
4. bible/ia_society_v2/ の 50 ファイルを Intake Adapter で再配置
5. kernel.yaml v4 作成
6. EPISODE_FULL_DRAFT 18 本を drafts/ に剥がす
7. log 系を State に移行
8. X-001 を Patch lifecycle で解決
9. DoR-A 検証

所要時間: 8-16 時間（人間 + LLM 協働）

### Phase 2.2: ore_tueee_school_hell 移行（08-ore_tueee 参照）

`08_pilot_validation/ore_tueee_school_hell_partial.md` の Step 1-11 を実行。

主要:
1. archive 取得
2. v4 ディレクトリ作成 + actions → backlog rename
3. story/promises → bible/promise 等の単純 move
4. bible v1 形式（series-bible-v1 等）を facet 別に分解
5. rules.md を style-voice + rules に分割
6. kernel.yaml v4 作成
7. handover_v2 を archive
8. DoR-A 検証

所要時間: 4-8 時間

### Phase 2.3: fools-with-cheating 移行（08-fools 参照）

`08_pilot_validation/fools_with_cheating_complete.md` の Step 1-11 を実行。

主要:
1. archive 取得
2. v4 ディレクトリ作成
3. `.adapter/` → `adapter/` rename
4. bible リネーム群（premise → logline 等）
5. bible/plot/ から arcs/ へ部分移動
6. style_guide.md を分割
7. 作品固有 facet を bible/three-layer/ bible/in-world-documents/ に独立配置
8. 不足 facet（foreshadowing-map / reveal-plan 等）構築
9. kernel.yaml v4 作成
10. DoR-A 検証

所要時間: 6-12 時間

### Phase 2.4: renji の扱い（Q-B-002）

採用判断時に決める:
- 移行する → 上記 3 作品と同様の手順
- archive する → `archive/2026-04-30-renji-pilot/` に退避、active 開発しない

---

## 4. Phase 3: 運用開始（30-90 日）

### Phase 3.1: Q-B / Q-C の解決（30-90 日）

`09_open_questions.md` の Q-B 4 件、Q-C 4 件を順次詰める。

### Phase 3.2: 運用観察と learning

各作品で本提案を運用しながら、`learning/` に retro を残す:
- ファイル成長の実態（300 行ルールが妥当か）
- card 書式の運用感（8 フィールド過不足ないか）
- DoR-A / DoR-B / DoR-C の通過頻度
- review prompt 7 本の使われ具合

### Phase 3.3: v5 への進化判断（90 日後）

90 日運用後、v5 を切るか判断:
- v4 で十分なら継続
- 大きな構造変更が必要なら v5 起票
- 小修正なら本提案の Patch として処理

---

## 5. Rollback 戦略

万一、v4 採用後に問題が発覚し、v3 に戻す必要が出た場合:

### Rollback Step 1: 作業停止

新規作業を停止し、archive から v3 状態を復元する判断を author 承認。

### Rollback Step 2: archive からの復元

```bash
# StoryTemplate 側
cd StoryTemplateEvolution/
cp -r archive/2026-04-30-pre-v4/docs/* docs/
cp -r archive/2026-04-30-pre-v4/adapter/folder_structure.md adapter/
cp -r archive/2026-04-30-pre-v4/templates/premise.template.md templates/bible/
mv proposals/2026-04-30-zero-base-v4 archive/2026-04-30-rolled-back-zero-base-v4
mv archive/2026-04-30-pre-v4/proposals/2026-04-22-story-template-v2 proposals/
mv archive/2026-04-30-pre-v4/proposals/storytemplate_workflow_handoff_pack_takt proposals/
```

### Rollback Step 3: 各 work の復元

```bash
cd works/ia_society/
# v3 状態を復元
mv ../../archive/2026-04-30-ia_society-pre-v4/* ./
# v4 化したファイルを退避（作業ログ）
# bible/logline.md → bible/premise.md にリネームバック等
```

各 work で同様の手順。

### Rollback Step 4: 移行ログ retro

`learning/{date}-rollback-v4.md` に rollback の経緯と learning を記録。

---

## 6. リスクとミティゲーション

| リスク | 影響 | ミティゲーション |
|---|---|---|
| **archive 漏れで v3 状態を失う** | rollback 不能 | Phase 1.1 / 各 Phase 2.X の最初で archive を必須化、checklist で確認 |
| **支援 LLM が intake adapter 実行で hallucination** | bible に偽情報混入 | `07_review_prompts/intake-digest-review.md` を必ず通す |
| **86 項目チェックリストが重すぎて使われない** | DoR-A 判定が曖昧化 | Q-C-002（自動化）を 90 日以内に進める |
| **作品固有 facet が template に流入** | template 汚染 | `01_supersession_map.md` の "作品固有 facet 不流入" を migration check で確認 |
| **kernel.yaml v3 → v4 migration script が破綻** | kernel データ欠損 | Q-C-001 で B + C（自動 + LLM 検証）の 2 段階 |
| **複数 work の並行移行で参照断** | grep で旧パスが残る | 各 Phase 2.X 完了時に grep 検証を必須化 |
| **EPISODE_FULL_DRAFT の meta 欄遡及不能** | DoR-B 通過不可 | 必要な ep のみ meta 欄を遡及記入、不要は backlog に |
| **二層ファイル運用が author に重い** | 運用放棄 | Q-A-003 で separator を確定、必要なら分離（option C）にロールバック |

---

## 7. 完了判定

本 migration plan の DoD:

```
□ Phase 1 完了: StoryTemplate 側の supersede / refactor / 新規作成すべて
□ Phase 2.1 完了: ia_society が DoR-A 通過
□ Phase 2.2 完了: ore_tueee_school_hell が DoR-A 通過
□ Phase 2.3 完了: fools-with-cheating が DoR-A 通過
□ Phase 2.4 判断完了: renji の扱い決定
□ Phase 3.1 完了: Q-B 4 件 + Q-C 4 件解決
□ archive/2026-04-30-pre-v4/ にすべての旧資産が退避済み
□ rollback 手順が動作確認済み（dry-run）
□ learning/{date}-v4-migration-retro.md 記録
```

---

## 8. 不変条件（移行作業中）

1. **archive を作らずに作業を始めない** — 復元手段の確保
2. **author 承認なしに kernel schema 変更しない**
3. **複数 work の同時移行を避ける** — 1 作品ずつ完了させる
4. **作業ログを `learning/` に残す**
5. **作品固有 facet を generic template に流入させない** — 各 phase で確認
6. **rollback 手順を最初に dry-run しておく** — 採用判断前に試行
7. **移行中の work は draft 着手禁止** — DoR-A 通過まで drafting を止める

---

## 9. 関連参照

- 取捨マップ: `01_supersession_map.md`
- 各 work の手順詳細: `08_pilot_validation/`
- 未決論点: `09_open_questions.md`
- Card 書式: `02_domain_model.md`
- 物理配置: `03_storage_trinity.md`
- 全体フロー: `04_pipeline_overview.md`
- DoR-A: `06_bible_dor.md`
- 検証 prompt: `07_review_prompts/`
