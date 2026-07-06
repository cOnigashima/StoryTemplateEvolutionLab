# Status 語彙

> field の「空に見える状態」を 12 値で区別する。
> Judge 4 値 / Lock 5 状態も同じ語彙系統。
> 基底 11 値の詳細は `v4/02_domain_model.md` Section 12。
> 2026-07-06 の workbench 統合で `rejected` を加え **12 値に拡張**（本ファイルが 12 値の正本）。

---

## Field Status 12 値

| 値 | 意味 | DoR への影響 |
|---|---|---|
| **filled** | 値あり、確定 | ✓ |
| **missing** | 空、本来埋まるべき | MUST フィールドなら ✗ |
| **tentative** | 値あり、暫定 | ✓ |
| **deferred** | 後で埋める | MUST なら ✗ / SHOULD なら ✓ |
| **intentionally_blank** | 意図的に空 | ✓ |
| **intentionally_hidden** | 値あり、読者非開示 | ✓（裏台帳で持つ） |
| **not_applicable** | 該当しない | ✓ |
| **genre_not_applicable** | このジャンルに不要 | ✓ |
| **rejected** | 提案されたが author が却下 | ✓（不採用が確定） |
| **project_override** | 作品固有方針で上書き | ✓（強拘束） |
| **contradiction** | 別フィールドと矛盾 | ✗（解消必須） |
| **needs_author_decision** | author 判断要 | MUST なら ✗ |

---

## Judge 4 値

| 値 | 意味 | 次の動き |
|---|---|---|
| **PASS** | 合格 | soft_lock → 次 step |
| **FAIL_AUTO_FIX** | auto_fix_allowed の範囲 | auto_fix_loop → 再 judge |
| **NEEDS_HUMAN** | author 判断必須 | 停止・通知 |
| **REJECT_AND_REGENERATE** | 候補棄却 | tournament 次 round |

---

## Lock 5 状態

| 状態 | 公開可否 | 変更 |
|---|---|---|
| **unlocked** | 不可 | 自由 |
| **soft_lock** | 不可 | 小修正可 |
| **packet_soft_lock** | 検討可 | arc 調整で可 |
| **hard_lock** | 可 | canon patch のみ |
| **published** | 公開済 | 周知必須 |

---

## 状態判定 Decision Tree

```
Q1. 値が入っているか?
  Yes → Q2
  No  → Q3

Q2. 確定?
  Yes → filled
  No  → tentative

Q3. 本来埋まるべき?
  Yes → Q4
  No  → Q5

Q4. 後で埋める?
  Yes → deferred
  No  → Q6

Q5. なぜ空?
  ジャンル不要 → not_applicable / genre_not_applicable
  提案を却下した → rejected
  意図的に空 → intentionally_blank
  読者非開示（裏に値あり） → intentionally_hidden
  作品固有方針 → project_override

Q6. 矛盾あり?
  Yes → contradiction
  No  → Q7

Q7. author 判断要?
  Yes → needs_author_decision
  No  → missing
```

---

## AI / 人間の権限境界

| status | AI | 人間 |
|---|---|---|
| filled | 参照のみ | 変更可（canon patch 経由） |
| missing | 候補提案 | 確定 |
| tentative | 提案・更新 | 確定昇格 |
| deferred | 触らない | deferred_until 変更可 |
| intentionally_blank | 触らない | 状態変更可 |
| intentionally_hidden | 参照可（visible_to のみ） | 開示判断 |
| project_override | 触らない | 変更可 |
| contradiction | 解消案提案 | 解消決定 |
| needs_author_decision | option 提案 | 確定 |
| rejected | 触らない（再提案は candidate として） | 却下決定・復活判断 |

**AI は status を勝手に上げ下げしない**。candidate 提案で止める。確定は author。

---

## 遷移ルール

```
許可:
  missing → tentative → filled
  tentative → contradiction
  filled → contradiction
  any → needs_author_decision
  needs_author_decision → filled / tentative
  contradiction → filled / tentative
  tentative / needs_author_decision → rejected（author 却下）
  rejected → tentative（author が再検討を認めた場合のみ）

禁止:
  filled → missing（埋まったものを「無かった」にしない）
  intentionally_blank → filled（再 author 承認必須）
  intentionally_hidden → filled（reveal_plan 経由）
```
