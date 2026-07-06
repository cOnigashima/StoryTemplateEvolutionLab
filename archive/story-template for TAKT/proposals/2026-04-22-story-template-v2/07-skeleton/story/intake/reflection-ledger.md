# Reflection Ledger

本台帳は intake → canon までの反映状況を追う。`provenance.yaml` と併読する。

> **更新タイミング**: digest 完了時 / seed 起票時 / 反映完了時 / 却下時 / 週次棚卸し
>
> **関連**:
>   - `story/intake/raw-index.yaml`（raw 一覧）
>   - `story/intake/digest-index.yaml`（digest 一覧）
>   - `story/seeds/seed-index.yaml`（seed 一覧）
>   - `story/intake/provenance.yaml`（系譜）
>   - `.claude/rules/intake-flow.md`（運用規範）

---

## 未反映（pending）

| raw id | digest 済み | seed 化 | 未反映理由 | 次アクション | 期限 |
|---|---|---|---|---|---|
| （初期状態では空） |  |  |  |  |  |

---

## 却下（dropped）

| raw id / seed id | 却下理由 | 参照先 |
|---|---|---|
| （初期状態では空） |  |  |

---

## 反映完了（done）

直近 N 件のみ記録する。古いものは arc 完了時の consolidate で集約する。

| raw id / seed id | 反映先 | 反映日 | reviewer |
|---|---|---|---|
| （初期状態では空） |  |  |  |

---

## 棚卸し履歴

| 日付 | 棚卸し内容 | 移送先 |
|---|---|---|
| （初期状態では空） |  |  |
