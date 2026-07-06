# 08 Pilot Validation — 3 作品での試走結果

> **役割**: 本提案 v4 を 3 つの実在 work（ia_society / ore_tueee_school_hell / fools-with-cheating）に適用したときの walkthrough。
> **目的**: 05 / 06 / 07 が現実の作品に当てたときに機能するか、不足はどこかを検証。
> **依存**: 02-07 を前提とする。

---

## 3 作品の選定理由

| work | 状態 | 検証目的 |
|---|---|---|
| **ia_society** | bible/ia_story_bible_v2/ に 50 ファイル超の **完成形 bible package** + 18 EPISODE_FULL_DRAFT が同居 | **大量既存資料の再配置 + Bible→drafts 剥がし** の試走 |
| **ore_tueee_school_hell** | seed 8 ファイル + bible v1（4 ファイル）+ packets/000-003 frozen + handover_v2 構造 | **中間状態のマージ + v3→v4 リネーム** の試走 |
| **fools-with-cheating** | raw 35 ファイル + bible 充実 + .adapter/ 整備済 + 作品固有 facet（三層対応 / 章末資料 / 批評性） | **作品固有 facet の保持 + generic 雛形への流入抑止** の試走 |

3 作品で「ほぼゼロ」「中間」「ほぼ完成」の 3 段階の状態をカバーしている。

---

## 各ファイルの構造

各 walkthrough は次の 7 セクション構成:

1. **現状サマリ** — 何がある / 何がない
2. **DoR-A 判定**（06 を適用）
3. **Intake Coverage**（05 を適用、86 項目スコア）
4. **物理再配置マップ**（旧 → 新の対応表）
5. **作品固有 facet の扱い**（generic vs work-specific）
6. **migration step 順序**（具体的な手順）
7. **想定リスク**（移行中に何が崩れうるか）

---

## walkthrough ファイル

| ファイル | 対象 work |
|---|---|
| `ia_society_zero_state.md` | ia_society（**実は zero state ではなく partial migration state**、命名は便宜上） |
| `ore_tueee_school_hell_partial.md` | ore_tueee_school_hell |
| `fools_with_cheating_complete.md` | fools-with-cheating |

---

## 全体の learning（3 作品共通）

3 作品の walkthrough 後、共通して言える:

1. **kernel.yaml の v3 → v4 移行**は単純リネーム（`premise:` → `logline:`）で済む
2. **bible facet 物理再配置**は手作業 or Intake Adapter 一括が必要、後者推奨
3. **EPISODE_FULL_DRAFT を bible から drafts/ に剥がす**作業は ia_society のみ深刻
4. **作品固有 facet** は work の bible 配下に許容、template には積まない（fools の三層対応 / 章末資料配置）
5. **既存 contradiction-log / canon-patch-log は v4 でも 1:1 移行可能**

詳細は `09_open_questions.md` と `10_migration_plan.md` で扱う。
