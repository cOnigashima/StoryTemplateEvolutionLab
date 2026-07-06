# craft/ — Layer 3: 作品共通の Craft Library

> **役割**: 作品不問で参照される **創作原理の常設道具箱**。
> **位置付け**: Layer 3。各 work から `current/craft/` を参照する（copy せず）。
> **整備方針**: Q-B-003 採用、各 work の `.claude/rules/` から共通要素を吸い上げて初期 craft を作る（30 日以内）。

---

## 配下のディレクトリ / ファイル

| ファイル / ディレクトリ | 役割 | 状態 |
|---|---|---|
| `rubric.md` | Typed Review の評価軸（9 軸 / 25 項目） | TBD（Phase 1.9 で初期版） |
| `framework-index.md` | 既存創作 framework の索引（Save the Cat / Hero's Journey / Egri / 等） | TBD |
| `lenses/` | Framework Lens 適用記録 | TBD |
| `scene-sequel.md` | Scene-Sequel 構造論 | TBD |
| `pov-design.md` | 視点設計の嘘と省略 | TBD |
| `foreshadowing-craft.md` | 伏線の三段運用 | TBD |

---

## Craft / Framework / Framework Lens の境界

| 概念 | 役割 | 物理位置 |
|---|---|---|
| **Craft** | 作品不問の常設道具箱 | `current/craft/` 直下 |
| **Framework** | 既存創作理論への索引 | `current/craft/framework-index.md` |
| **Framework Lens** | Framework の一時適用視点 | `current/craft/lenses/{framework_name}-{date}.md` |

詳細は `docs/domain/02_domain_model.md` Section 11 (Craft) を参照。

---

## 整備計画

### Step 1: 既存資産の吸い上げ（採用後 30 日以内）

各 work の `.claude/rules/` から共通要素を抽出:

- `fools-with-cheating/.claude/rules/drafter-preflight.md` の Gate 0 / A / C → craft の `drafter-gate.md` に
- `ia_society/.claude/rules/drafter-preflight.md` の追加 Gate（D / E / F / G） → craft の `narrative-discipline.md` に
- `ore_tueee_school_hell/.claude/rules/craft-methodology.md` → craft の `methodology-overview.md` に

### Step 2: rubric の初期版（Phase 1.9）

9 軸 rubric:
- 完成度 / 読者体験 / 独創性 / 整合性 / 感情的インパクト / キャラ強度 / 世界観強度 / 文章技術 / 推敲耐性

各軸の score range / weight / 判定基準を定義。

### Step 3: framework-index の初期版

既存創作 framework の索引（lens として一時適用するための README）:
- Save the Cat (15 ビート)
- Hero's Journey (12 段階)
- Egri's Premise Theory
- 3 幕 8 シークエンス
- Story Genius (Lisa Cron)

### Step 4: lenses/ の運用開始

特定 episode / arc を Framework Lens で評価したログを `lenses/{framework}-{date}.md` に append。

---

## 不変条件

1. **作品固有の知見は craft に積まない** — 各 work の `.claude/rules/` に置く
2. **Framework は wholesale 採用しない** — 一時 lens として当てるのみ
3. **rubric の axis 変更は canon patch 相当** — 過去 review との比較を破壊する
4. **craft は各 work から copy せず参照する** — `current/craft/` を共有

---

## 関連参照

- 用語: `docs/domain/02_domain_model.md` Section 11
- フロー: `docs/domain/04_pipeline_overview.md`
- 各 work の `.claude/rules/`（吸い上げ元）
