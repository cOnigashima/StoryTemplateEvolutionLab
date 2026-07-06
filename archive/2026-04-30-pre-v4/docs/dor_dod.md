# Definition of Ready / Definition of Done

> DoR = 作業を始めて良い状態 / DoD = 完了して次へ進めて良い状態
> 各 3 段。詳細は v3 `06_setup_dor.md` `07_publish_dod.md`。

---

# DoR — 作業開始前の必要条件

## DoR-A: 新規作品 bootstrap 完了時

```
□ ディレクトリ構造（bible/design/state/writing/inbox/synthesis）
□ CLAUDE.md
□ .claude/rules/ 5 本継承
□ story/kernel.yaml の MUST 11 項目すべて (filled or 適切 status)
□ kernel に missing / contradiction / needs_author_decision なし
□ story/promises.md（kernel.promise 由来）
□ bible/world.md（最低 3 行サマリ）
□ bible/characters.md（最低 主人公 + 主要対立者）
□ bible/rules.md（最低 文体方針 + 禁則 1 件）
□ bible/genre-overlay.md（必要時）
□ bible/project-override.md（必要時）
□ arcs/series-overview.md
□ arcs/arc-01.md
□ packets/scoped/packet-001-{slug}.yaml
□ story/open-questions.md（空でもファイルあり）
□ story/design-debt.yaml
□ ledger/ 6 ファイル初期化
```

→ 全 ✓ で Episode draft フェーズに入れる

## DoR-B: Episode draft 開始前

```
□ scenes/slotted/{ep}.md（scene_card 必須項目埋まり）
□ reviews/contracts/{ep}.contract.yaml（acceptance_contract 必須項目）
□ Gate 0: 直前散文照合（series opener 以外 MUST）
□ Gate A: packet 要件マッピング（frozen packet 配下なら MUST）
□ Gate C: 前振りチェック（クライマックスあるなら MUST）
□ 因果一段落
□ 知識状態台帳（開始 / ビート毎 / 終了 / 予感レイヤ）
□ 合理化語彙 self-check
□ ledger snapshot 取得
```

→ 全 ✓ で drafter は prose を書き始めて良い

## DoR-C: Packet を frozen に進める前

```
□ packet.yaml の必須項目すべて
□ 各 episode の役割・loss・gain・reveal・hooks・cliffhanger
□ 依存先（promise / bible / arcs）が filled or tentative
□ contradiction 残存ゼロ
□ entry_state が直前 packet の exit_state と整合
□ packet 内 episode 間の知識状態遷移が単調
□ 本 packet で実装する promise.items 列挙
□ reader experience / cadence の予定
□ Packet Freeze Review 通過
```

→ 全 ✓ で packets/frozen/ へ移動

---

# DoD — 完了して次に進める条件

## DoD-E: Episode 公開直前

```
□ Multi-Pass Self-Review 4 パス（drafter-preflight）
□ meta 欄完成
□ episode-judge PASS（or auto_fix → PASS）
□ Acceptance Contract の must_satisfy 全 ✓
□ must_not_violate ゼロ
□ intended_unknowns が prose で意図通り隠されている
□ must_be_clear が読者に伝わっている
□ quality_bar（rubric ≥60、hard gate ≥2）
□ Typed Review 実施
□ Continuity 確認
□ Ledger 更新提案
□ kakuyomu policy 適合（AI タグ / 頻度 / 禁止コンテンツ）
□ author 承認（hard_lock）
□ approved/ コピー
□ 公開実施 → published/ コピー
□ ledger に published 状態反映
```

## DoD-P: Packet release

```
□ 全 Episode が DoD-E 満足
□ packet-assembly-review PASS
□ packet 内接続・重複・テンポ・矛盾なし
□ promise 紐付け検証（本 packet で実装した promise が prose に存在）
□ Bridge Review（次 packet 設計済の場合）
□ packet 単位 Continuity 確認
□ ledger reconciliation
□ author 承認 → packet_soft_lock → hard_lock
```

## DoD-A: Arc / Part 完結

```
□ 全 Packet が DoD-P 満足
□ arc-through-review 実施
□ 中期問いの決着（or 持ち越し決定）
□ 主反転が prose で実装
□ 関係性変化が起きた
□ 中だるみなし
□ 伏線回収（本 Arc 範囲）
□ Part 進行度確認（Part 完結時のみ）
□ Reader Persona 検証（推奨）
□ author 承認
```

---

## status と DoR/DoD の関係

| status | DoR | DoD |
|---|---|---|
| filled | ✓ | ✓ |
| tentative | ✓ | ✓（low risk） |
| deferred | MUST=✗, SHOULD=✓ | per case |
| intentionally_blank | ✓ | ✓ |
| intentionally_hidden | ✓ | ✓ |
| not_applicable | ✓ | ✓ |
| project_override | ✓ | ✓ |
| contradiction | ✗ | ✗ |
| needs_author_decision | MUST=✗ | per case |
| missing | MUST=✗ | per case |

---

## 不満足時の対応

```
DoR-A 不満足 → kernel/bible/arcs/packet-001 のどこ空か特定 → author に上げる → 再 DoR-A
DoR-B 不満足 → scene_card / contract / Gate のどこ空か特定 → plotter / Adapter に戻す
DoR-C 不満足 → packet.yaml のどこ空か → plotter に戻す

DoD-E 不満足
  Judge FAIL_AUTO_FIX → auto_fix → 再 Judge
  Judge NEEDS_HUMAN → author 介入 → 修正 → 再 Judge
  Judge REJECT_AND_REGENERATE → tournament 再走

DoD-P / DoD-A 不満足 → 個別 episode の DoD-E に戻す or 構造変更
```

**勝手にスキップしない**。
