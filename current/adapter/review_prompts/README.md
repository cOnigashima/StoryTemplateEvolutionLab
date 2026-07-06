# 07 Review Prompts — Intake-stage 用レビュープロンプト 7 本

> **役割**: Intake から DoR-A 通過までの各段階で、機械的に検証を回すための LLM 用プロンプト集。
> **依存**: 02_domain_model.md / 03_storage_trinity.md / 04_pipeline_overview.md / 05_intake_coverage_checklist.md / 06_bible_dor.md。
> **使い方**: 各 prompt は self-contained で、新セッションの LLM に貼り付けて実行可能。

---

## 7 本の prompt 一覧

| # | ファイル | 役割 | タイミング | 入力 | 出力 |
|---|---|---|---|---|---|
| 1 | `intake-digest-review.md` | Digest 出力の self-review | Intake Adapter 実行直後 | `synthesis/session_digests/{date}_{slug}.md` | review report（pass / fail） |
| 2 | `intake-coverage-review.md` | 05 の網羅チェックリストを機械的に回す | Intake Adapter 完了後 | bible/design/state + 05 | coverage report（86 項目スコア） |
| 3 | `bible-readiness-review.md` | DoR-A 通過判定 | Intake 完了後、Packet 設計前 | 全 work directory | DoR-A pass/fail report |
| 4 | `kernel-fill-review.md` | kernel 11 項目の status 整合性検査 | kernel.yaml 更新後 | `story/kernel.yaml` | kernel 検証 report |
| 5 | `update-proposal-review.md` | Update Proposal を bible に反映する前の最終 review | author Approval 直前 | `synthesis/update_proposals/*.md` | 反映可否判定 |
| 6 | `contradiction-triage.md` | 矛盾発見時の整理 | Continuity / Design Audit / drafter から矛盾報告時 | contradiction-log entry + 関連 ファイル | 解決方針（Patch / Open Question / 即修正） |
| 7 | `design-audit-prompt.md` | Bible 設計監査 | 定期 / Patch 後 / DoR-A 直前 | 全 bible/ + design/ + state/ | Design Audit report |

---

## prompt の標準フォーマット

各 prompt は次の 6 セクションを持つ:

1. **あなたの役割** — LLM の persona 設定
2. **前提読み込み** — 必ず先に読むファイル
3. **入力** — 検査対象の指定形式
4. **手順** — 順序固定のステップ
5. **出力フォーマット** — 構造化された report
6. **失敗パターン NG** — やりがちな間違い

prompt 内では proposal 全体の文書を参照する（`02_domain_model.md` 等）。LLM が proposal 配下を全部読めることが前提。

---

## 使用順（典型）

### Case A: 新規作品 bootstrap

```
Pitch / Seed → 企画 chat
        ↓
inbox/ に保存
        ↓
[Intake Adapter Prompt 実行]
        ↓
synthesis/ に Digest + Update Proposal
        ↓
[1. intake-digest-review.md]  → Digest 自己 review
        ↓
[2. intake-coverage-review.md]  → 86 項目網羅チェック
        ↓
[6. contradiction-triage.md]   ※矛盾発見時のみ
        ↓
[5. update-proposal-review.md]  → 反映前 review
        ↓
author Approval
        ↓
bible/design/state 反映
        ↓
[4. kernel-fill-review.md]    → kernel 整合性
        ↓
[3. bible-readiness-review.md] → DoR-A 判定
        ↓
[7. design-audit-prompt.md]   → Bible 全体監査
        ↓
DoR-A 通過 → 次 phase（Packet 設計）
```

### Case B: 既存 bible package の取り込み（ia_society 系）

```
既存 bible (50 ファイル) を inbox/ に配置
        ↓
[Intake Adapter Prompt 実行] (大規模 batch)
        ↓
[2. intake-coverage-review.md] → どの facet が埋まっているか確認
        ↓
[6. contradiction-triage.md]   → 大量の contradiction を整理
        ↓
[5. update-proposal-review.md] → facet ごとに分割 review
        ↓
段階的に bible 反映
        ↓
[7. design-audit-prompt.md]    → 全体整合性検査
        ↓
[3. bible-readiness-review.md] → DoR-A 判定
```

### Case C: 既存 work の bible audit

```
既存の bible / design / state（v3 等の旧構造）
        ↓
[7. design-audit-prompt.md]    → 何が v4 整合か確認
        ↓
[2. intake-coverage-review.md] → 86 項目の埋まり具合
        ↓
[3. bible-readiness-review.md] → DoR-A blocker 一覧
        ↓
リネーム / 分割 / 補完計画 → 10_migration_plan.md
```

---

## 参考: 既存の Intake Adapter Prompt との関係

`current/adapter/intake_adapter.md` は **生成 prompt**（raw → digest + update_proposal を作る）。本 7 本は **検証 prompt**（生成された artifact が正しいかチェックする）。両者は異なる役割で並走する。

---

## prompt 実行時の Anthropic 推奨

各 prompt はそれぞれ Claude / GPT 等に貼り付けて使う。実行時のチューニング指針:

- **temperature: 低**（決定論的な検証）
- **長文 context 必須**（02 / 05 / 06 を全部読み込ませる）
- **structured output**（YAML or JSON で受ける）
- **explicit refusal**（未確定や missing を勝手に埋めさせない）
