# Definition of Ready (DoR) v3

> **目的**: 「執筆を始めてよい状態」を 3 段で固定する。① 新規作品 bootstrap 時 ② 各 Episode 執筆前 ③ 各 Packet 凍結前。
> **ガチガチ度**: 各段の MUST 項目は本 v3 で固定。SHOULD 項目は推奨。
> **使い方**: チェックリスト。全 MUST に ☑ が入るまで次工程に進めない。

---

## 1. 3 段構成の理由

| 段 | タイミング | 検証対象 |
|---|---|---|
| DoR-A | 新規作品起こし完了時 | kernel + 最低限 bible + 1 packet 設計 |
| DoR-B | Episode draft 開始前 | scene_card + acceptance_contract + 直前散文 |
| DoR-C | Packet を frozen に進める前 | packet 全 episode 設計済 + 依存解決 |

DoR-A は「作品が動かせる」状態、DoR-B は「1 話書ける」状態、DoR-C は「章束として draft フェーズに入れる」状態。

---

## 2. DoR-A: 新規作品 bootstrap 完了時

### 2.1 ディレクトリ構造

```
□ work-id ディレクトリが切られている
  例: works/{work-slug}/

□ Story Template の最小骨格が init されている
  □ CLAUDE.md
  □ .claude/rules/  （5 本+v3 で追加した分）
  □ story/
  □ bible/
  □ arcs/
  □ packets/
  □ scenes/
  □ drafts/
  □ reviews/
  □ craft/
  □ approved/
  □ published/
  □ learning/
  □ ledger/

□ .takt/ が初期化されている（TAKT 採用時のみ）
  □ .takt/config.yaml
  □ .takt/workflows/  （次セッションで埋める）
  □ .takt/facets/
  □ .takt/tasks/
  □ .takt/runs/
```

### 2.2 kernel.yaml

```
□ story/kernel.yaml が存在する

MUST 項目（全て埋まっているか、status が valid):
□ premise (filled)
□ promise (最低 3 項目, 各 status valid)
□ protagonist_vector.primary_protagonist.want (filled)
□ protagonist_vector.primary_protagonist.need (filled)
□ conflict (最低 1 軸 filled)
□ stakes.if_protagonist_fails (filled)
□ stakes.why_reader_cares (filled)
□ change_model.arc_shape (filled)
□ causality.time_order_policy (filled)
□ causality.knowledge_state_monotonicity (filled)
□ information_design.must_be_clear (最低 3 項目)
□ emotional_arc.overall_curve (filled or tentative)
□ style_voice.pov (filled)
□ style_voice.tense (filled)
□ unit_tree.target_total_episodes (filled or tentative)
□ unit_tree.serial_or_complete (filled)

SHOULD 項目:
□ protagonist_vector.primary_protagonist.wound_or_misbelief
□ conflict.internal
□ conflict.relational
□ change_model.direction_of_change
□ information_design.intended_unknowns
□ emotional_arc.target_reader_emotion_at_end
□ style_voice.register
□ style_voice.forbidden_words

NG 状態（1 つでもあったら DoR-A 不満足）:
✗ MUST のいずれかが missing
✗ MUST のいずれかが needs_author_decision
✗ MUST のいずれかが contradiction
```

### 2.3 promises.md

```
□ story/promises.md が存在する
□ kernel.promise の各 item が promises.md にも書かれている
  （二重管理ではなく、kernel.yaml は構造化、promises.md は人間可読の正典）
□ 各 promise に「いつ」「どこで」回収するかの暫定計画
```

### 2.4 bible 最小

```
□ bible/world.md（最低: 設定の 3 行サマリ）
□ bible/characters.md（最低: 主人公 + 主要対立者）
□ bible/rules.md（最低: 文体方針 + 禁則 1 件）

ジャンル overlay 採用時:
□ bible/genre-overlay.md
  例: mystery なら fair_play_constraints / clue_categories
       romance なら attraction_vector / dark_moment_position

project override がある時:
□ bible/project-override.md
```

### 2.5 arcs 最小

```
□ arcs/series-overview.md（Manuscript の俯瞰）
□ arcs/arc-01.md（最初の Arc）

最低限の内容:
□ Arc-01 の中核問い
□ Arc-01 の主反転
□ Arc-01 が含む packet 一覧（packet-001 のみで OK）
```

### 2.6 packet 最小

```
□ packets/scoped/packet-001-{slug}.yaml が存在
  または
□ packets/frozen/packet-001-{slug}.yaml が存在（DoR-C も満たすなら）

最低内容:
□ purpose
□ entry_state / exit_state
□ episode_roles（含む各 episode の役割）
□ end_hooks
□ disclose / withhold
□ guardrails
```

### 2.7 open_questions

```
□ story/open-questions.md が存在
□ 現時点の未解決論点が列挙されている（0 件でもファイルだけ存在させる）
```

### 2.8 design_debt

```
□ story/design-debt.yaml が存在
□ format に従った構造で 0 件 or 既知 debt が記載
```

### 2.9 ledger 初期化

```
□ ledger/ が空でも構わないが、初期構造が切られている
  □ ledger/canon-facts.yaml（初期は []）
  □ ledger/timeline.yaml（初期は []）
  □ ledger/character-states/  （ディレクトリ）
  □ ledger/foreshadowing-status.yaml
  □ ledger/open-questions.yaml
  □ ledger/author-decisions.yaml
  □ ledger/rejected-ideas.yaml
```

### 2.10 DoR-A サマリ判定

```
□ 上記 2.1〜2.9 の全 MUST が ☑
□ kernel.yaml の `kernel_complete.all_must_filled` が true
□ kernel.yaml の `kernel_complete.internal_consistency_checked` が true
```

→ 全部 ☑ なら DoR-A **満足**。Episode draft フェーズに入れる。

---

## 3. DoR-B: Episode draft 開始前

drafter（人間 or AI）が prose を書き始める **直前** に通すゲート。Pack A `drafter-preflight.md` を継承し、TAKT 文脈で再整理。

### 3.1 入力一式

```
□ scene_card が存在
  パス: scenes/slotted/packet-NNN-epMM-{slug}.md
  
□ scene_card の必須フィールドが埋まっている
  □ purpose
  □ entry_state / exit_state
  □ must_include
  □ must_not_include（空でもよいが、検討済として明示）
  □ intended_unknowns
  □ must_be_clear
  □ reader_target
  □ style_constraints（kernel.style_voice からの差分があれば明記）
  □ dependencies（依存 packet / bible / arc）

□ acceptance_contract が存在（Adapter 出力）
  パス: reviews/contracts/packet-NNN-epMM-{slug}.contract.yaml
  
□ acceptance_contract の必須フィールドが埋まっている
  □ must_satisfy
  □ must_not_violate
  □ intended_unknowns
  □ must_be_clear
  □ quality_bar
  □ auto_fix_allowed
  □ human_required_if
```

### 3.2 Gate 0: 直前散文照合

series opener 以外 MUST。

```
□ 直前 episode の散文を読んだ
□ 開始時点 carryover を散文根拠付きで列挙した
□ packet 切り替わり直後なら、前 packet からの carryover を最低 1 件再起動する計画がある
```

### 3.3 Gate A: Packet 要件マッピング

frozen packet 配下の episode は MUST。

```
□ 今回 episode が引き受ける packet 要件を抽出した
□ 各要件に「どのビート / シーンで実装するか」を宣言した
□ 「今回担当外」要件は理由付きで明示した
□ 実装ビートが空白の要件が 0 件
```

### 3.4 Gate C: 前振りチェック

クライマックス・大反転・正体判明・同調ピークがある draft は MUST。

```
□ 今回のクライマックス / 反転を 1 行で定義
□ softer version の前振りが特定済（前 ep または本 ep 前半）
□ 無い場合: add_foreshadow / delay_climax / intentional_first_shock のどれを採用するか宣言
```

### 3.5 因果一段落（基本 3 原則 1）

```
□ 因果一段落が draft meta 欄に書かれている
□ 1 段落に圧縮できている（できなければ scene card に戻る）
□ 開始時知識状態 / 終了時知識状態 が記述されている
```

### 3.6 知識状態台帳（基本 3 原則 2）

```
□ 開始時点既知が列挙されている
□ ビートごとの追加情報・追加経路が列挙されている
□ 終了時点既知が列挙されている
□ 予感レイヤが知識状態と分離されている
```

### 3.7 合理化語彙 self-check（基本 3 原則 3）

```
□ 「つまり」「要するに」「なるほど」等の出現予定 / 予防策がある
□ 出現する場合、因果が実際に通っているか確認の段取り
```

### 3.8 ledger snapshot 取得

```
□ ledger/ から本 episode に関連する状態を取得した
  □ canon-facts のうち関連項目
  □ 関連 character の character-state
  □ 関連 foreshadowing-status
  □ 関連 open-questions
  □ 直近の author-decisions
```

### 3.9 DoR-B サマリ判定

```
□ scene_card 必須項目 全 ☑
□ acceptance_contract 必須項目 全 ☑
□ Gate 0 / Gate A / Gate C 全 ☑（該当時）
□ 基本 3 原則 全 ☑
□ ledger snapshot 取得済
```

→ 全部 ☑ なら DoR-B **満足**。drafter は prose を書き始めてよい。

---

## 4. DoR-C: Packet を frozen に進める前

Packet が `scoped` から `frozen` に進む（drafter に渡せる）状態。

### 4.1 packet.yaml 完成度

```
□ purpose（1 文）
□ entry_state / exit_state
□ episode_roles（全 episode の役割）
□ end_hooks（次 packet への引き）
□ disclose / withhold
□ guardrails

□ episodes 配列の各要素が埋まっている
  □ role
  □ purpose
  □ loss / gain
  □ reveal
  □ hooks
  □ cliffhanger
```

### 4.2 依存解決

```
□ 依存する story/promises.md の項目を列挙
□ 依存する bible/* の章を列挙
□ 依存する arcs/* の項を列挙
□ 全依存先が現状 filled or tentative
□ contradiction 残存ゼロ
```

### 4.3 因果整合

```
□ entry_state が直前 packet の exit_state と整合
□ exit_state が次 packet の entry_state と整合（次 packet 未設計なら gap として記録）
□ packet 内の episode 間の知識状態遷移が単調
```

### 4.4 promise 紐付け

```
□ 本 packet で実装する promise.items を列挙
□ 各 promise の evidence_target が本 packet を指していれば、本 packet で実装される
□ 実装対象 promise が 0 件なら理由を記述
```

### 4.5 reader experience 検討

```
□ packet 開始時の読者期待
□ packet 中盤のフック
□ packet 終端の引き
□ 想定読者疲労（cadence の baseline と整合）
```

### 4.6 cadence 検討

```
□ tension/release ratio の予定
□ Scene/Sequel 構造の予定（Sequel beats の配置）
```

### 4.7 freeze review

```
□ Packet Freeze Review を回した
□ reviewer から「frozen 可」判定が出ている
```

### 4.8 DoR-C サマリ判定

```
□ packet.yaml 完成度 全 ☑
□ 依存解決 全 ☑
□ 因果整合 全 ☑
□ promise 紐付け ☑
□ reader experience 検討 ☑
□ cadence 検討 ☑
□ freeze review PASS
```

→ 全部 ☑ なら DoR-C **満足**。packet を `frozen/` に移動、drafter に渡す。

---

## 5. DoR の階層関係

```
DoR-A (作品 bootstrap)
  └── DoR-C (各 packet の frozen 化)
        └── DoR-B (各 episode の draft 開始)
              └── prose 開始
```

DoR-A 不満足のまま DoR-C / DoR-B に進むことは禁止。
DoR-C 不満足のまま DoR-B に進むことは禁止（exploring stage の packet で例外的試行は可、ただし frozen 扱いしない）。

---

## 6. DoR チェック自動化（次セッション）

将来的に TAKT step として実装する想定:

```yaml
# .takt/workflows/dor-check.yaml（次セッション設計）
name: dor-check
steps:
  - name: dor-a-check
    persona: dor-validator
    inputs:
      - story/kernel.yaml
      - bible/
      - arcs/series-overview.md
      - packets/
    rules:
      - condition: "All MUST satisfied"
        next: COMPLETE
      - condition: "MUST gap detected"
        next: report-and-stop
```

ただし、本 v3 では仕様の明文化のみで実装は次セッション。

---

## 7. DoR 不満足時の対応

DoR が満たされていないと判明した場合:

1. **DoR-A 不満足** → kernel / bible / arcs / packet-001 のどこが空か特定 → author に上げて埋める → 再 DoR-A
2. **DoR-B 不満足** → scene_card / contract / Gate のどこが空か特定 → plotter / Adapter に戻して埋める → 再 DoR-B
3. **DoR-C 不満足** → packet.yaml のどこが空か特定 → plotter に戻して埋める → 再 DoR-C

**勝手に埋めない**。空のまま進めない。author 承認を経て埋める。

---

## 8. DoR と status の関係

`05_status_vocabulary.md` §7.1 の通り、status によって DoR への影響が変わる:

- `filled` / `tentative` / `intentionally_blank` / `intentionally_hidden` / `not_applicable` / `genre_not_applicable` / `project_override` → DoR ✓
- `deferred` → MUST フィールドなら DoR ✗、SHOULD なら DoR ✓
- `missing` / `needs_author_decision` / `contradiction` → DoR ✗

DoR ✗ がある = 「埋めるか、status を変えるか、解消するか」の 3 択。**勝手に進めない**。
