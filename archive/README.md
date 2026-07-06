# archive/ — 凍結された旧資産

> **役割**: 歴史的経緯として保存された旧資産の格納域。
> **編集禁止**: ここに置いたファイルは原則編集しない（履歴として永続保存）。
> **削除禁止**: rollback 時の復元手段として保持。

---

## 配下のディレクトリ

| ディレクトリ | 由来 | アクセス頻度 |
|---|---|---|
| **`2026-04-30-pre-v4/`** | v4 採用直前のスナップショット（v3 状態の docs / adapter / templates / prompts / etc） | 中（rollback 時 / 履歴参照） |
| **`2026-04-31-integreated/`** | 2026-07-06 workbench 統合直前の旧 current 全体（v4 採用済み状態） | 中（rollback 時 / 継承検証） |
| **`proposal/`** | rejected / archived された提案の置き場（現在は空。handoff-pack-takt は `../proposal/2026-04-31-storytemplate_workflow_handoff_pack_takt/` に復帰） | 低（履歴のみ） |
| **`story-template/`** | v1 オリジナル skeleton（マニュアル移動 2026-04-30） | 低（履歴のみ） |
| **`story-template for TAKT/`** | v1 + proposals 拡張版（マニュアル移動 2026-04-30） | 低（履歴のみ） |

---

## 各 archive の経緯

### `2026-04-30-pre-v4/`

**作成日**: 2026-04-30
**経緯**: v4 採用に伴い、StoryTemplate トップレベルの v3 状態を退避。

**含まれるもの**:
- `docs/` — v3 の vocabulary / kernel_spec / dor_dod / layer_facet_map / unit_taxonomy / status_vocabulary
- `adapter/` — v3 の intake_adapter_prompt 等
- `templates/` — v3 の bible / design / state / writing 雛形
- `prompts/` — v3 の session prompt 群
- `checklists/` `rules/` `learning/` `work_init/`
- `README.md.snapshot` — v3 当時のトップ README

**v4 との対応**:
- `docs/vocabulary.md` ↔ `proposal/2026-04-30-zero-base-v4/02_domain_model.md`
- `docs/dor_dod.md` ↔ `proposal/2026-04-30-zero-base-v4/06_bible_dor.md`
- `adapter/folder_structure.md` ↔ `proposal/2026-04-30-zero-base-v4/03_storage_trinity.md`
- 他は current/ 配下で在籍中（refactor のみ、archive にも snapshot あり）

**アクセス用途**:
- v4 で問題発覚時の rollback ソース
- 「v3 ではどうだったか」の履歴参照
- **編集禁止**

---

### `2026-04-31-integreated/`

**作成日**: 2026-07-06
**経緯**: `proposal/2026-07-06-workbench-ontology-loop/` の採用（workbench 統合）に伴い、v4 採用済み状態の旧 current 全体を退避。新 current が置換。

**含まれるもの**:
- 旧 `current/` 一式 — docs（supersede stub 含む）/ adapter / agents 18 / skills 7 / rules / checklists / prompts 7 / craft / templates / learning / work_init / README / WORKFLOW

**新 current との対応**: `current/INHERITANCE.md` と `proposal/2026-07-06-workbench-ontology-loop/COVERAGE.md` に継承マップあり。

**アクセス用途**:
- workbench 統合で問題発覚時の rollback ソース
- 継承の完全性検証（COVERAGE との突合）
- **編集禁止**

※ フォルダ名の 4/31 は実在しない日付（v4 と統合の間を示す論理日付として user が命名維持を判断）。integrated のスペルは integreated のまま維持。

---

### `proposal/`

**経緯**: rejected または archived された提案を格納。**現在は空**。

- `storytemplate_workflow_handoff_pack_takt/` は 2026-07-06 の TAKT 暫定採用に伴い、日付 prefix 付きで `../proposal/2026-04-31-storytemplate_workflow_handoff_pack_takt/`（status: historic）に復帰。

---

### `story-template/` および `story-template for TAKT/`（マニュアル移動完了 2026-04-30）

**経緯**: v4 採用に伴い、旧 `../../story-template/` と `../../story-template for TAKT/` の 2 ディレクトリを user が物理移動した。

| ディレクトリ | サイズ | ファイル数 | 内容 |
|---|---|---|---|
| `story-template/` | 864KB | 201 | v1 オリジナル skeleton（proposals/ なし） |
| `story-template for TAKT/` | 1.4MB | 272 | v1 + proposals/ 拡張版（旧 v2-fat / v3-kernel / handoff の素材保管庫） |

両者は v1 時代の同系統だが、`for TAKT` は `proposals/` 配下に旧提案 3 件を抱えていた状態で凍結された。**現在 `proposal/2026-04-30-zero-base-v4/` 直下にある提案群と内容重複**しているが、**履歴として両方残す**（重複ストレージは許容）。

**renji の所在**: 当初想定された `works/renji/` は両ディレクトリの `works/` 配下に **物理ファイルとして存在しない**（works/ は空 dir）。renji は構想段階で実体化していなかった。retrospective document `archive/2026-04-30-pre-v4/learning/2026-04-29-renji-pilot-retro.md` に概念のみ残存。

**Q-B-002 の決着**: renji は実体ファイルを持たないため、移行作業は不要。「archive にある」だけで完結。

**命名はリネームせず維持**: user 判断で「そのまま archive にあるならそのままで良い」。`story-template-v1/` への rename は行わない。

---

## archive の不変条件

1. **編集禁止** — 一度 archive に入れたファイルは編集しない
2. **削除禁止** — rollback 用に保持
3. **新規 archive は理由付きで** — 「なぜここに来たか」を README に記録
4. **採用候補は archive ではなく proposal に** — archive は採用見送り済みのみ
5. **work の archive は work 内で完結** — 各 work の `archive/{date}-{slug}/` は別管理（StoryTemplate の archive とは別）

---

## rollback 手順（参考）

万一 v4 採用後に問題発覚し、v3 に戻す必要が出た場合:

```bash
cd StoryTemplateEvolution/

# 1. archive から v3 状態を復元
cp -r archive/2026-04-30-pre-v4/docs current/
cp -r archive/2026-04-30-pre-v4/adapter current/
cp -r archive/2026-04-30-pre-v4/templates current/
# ... 他

# 2. v4 提案を archive 化
mv proposal/2026-04-30-zero-base-v4 archive/2026-04-30-rolled-back-v4

# 3. handoff-pack を proposal/ に戻す（任意）
mv archive/proposal/storytemplate_workflow_handoff_pack_takt proposal/

# 4. README を v3 用に戻す
cp archive/2026-04-30-pre-v4/README.md.snapshot README.md
```

詳細は `proposal/2026-04-30-zero-base-v4/10_migration_plan.md` Section 5。

---

## 関連参照

- `../README.md` — リポジトリ全体
- `../current/README.md` — 現在の正本
- `../proposal/README.md` — 提案 status 表
