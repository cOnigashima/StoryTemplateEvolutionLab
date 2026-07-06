# adapter — チャット→セッションの引き渡し口

物語を考えるのはチャット。そのチャットを構造化して作品に流し込み、次のセッションへ引き渡すのが adapter の役目。
「会話ログ ≠ 正本」を守るための関所。

## 2つのadapter
- **intake_adapter.md** — 企画チャット（raw） → 構造化した update proposal → 承認 → bible/design/state へ反映。**raw を直接 bible に入れない。**
- **writing_adapter.md** — 確定 bible/state → 「今書く1単位」に圧縮した Writing Pack。ここで ontology の k-hop 抽出を使い、必要な context だけ渡す。

## セッション間の引き渡し
- **session_handoff.template.md** — セッションを跨ぐとき「今どこ・次何・未決・懸念」を1枚で渡す（villainess の HUB.md 相当）。
- 大きな chat は `logs/sessions/` にダイジェスト化してから proposal へ。

## 人間の承認
- **human_approval_policy.md** — どのタイミングで人間が承認するか（G-Intake / G-Deliverable / G-Publish）。

## 流れ
```
チャット発想 → intake_adapter → (logs/sessions ダイジェスト) → update proposal
   → [G-Intake 人間承認] → bible/design/state 反映
   → writing_adapter → Writing Pack → takt の draft workflow へ
```
