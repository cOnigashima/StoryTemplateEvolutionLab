# Packet Freeze Checklist Template

> Packet を `scoped/` から `frozen/` に進める前のチェックリスト。
> docs/dor_dod.md §DoR-C 準拠。

---

## 1. packet.yaml 完成度

- [ ] purpose（1 文）
- [ ] entry_state / exit_state
- [ ] episode_roles（全 episode の役割）
- [ ] end_hooks（次 packet への引き）
- [ ] disclose / withhold
- [ ] guardrails

各 episode について:
- [ ] role
- [ ] purpose
- [ ] loss / gain
- [ ] reveal
- [ ] hooks
- [ ] cliffhanger

## 2. 依存解決

- [ ] 依存する story/promises.md / bible/* / arcs/* を列挙
- [ ] 全依存先が filled or tentative
- [ ] contradiction 残存ゼロ

## 3. 因果整合

- [ ] entry_state が直前 packet の exit_state と整合
- [ ] exit_state が次 packet の entry_state と整合（次未設計なら gap として記録）
- [ ] packet 内の episode 間の知識状態遷移が単調

## 4. promise 紐付け

- [ ] 本 packet で実装する promise.items を列挙
- [ ] 各 promise.evidence_target が本 packet を指す項目について実装される
- [ ] 実装対象 promise が 0 件なら理由を記述

## 5. reader experience 検討

- [ ] packet 開始時の読者期待
- [ ] packet 中盤のフック
- [ ] packet 終端の引き
- [ ] 想定読者疲労（cadence の baseline と整合）

## 6. cadence 検討

- [ ] tension/release ratio の予定
- [ ] Scene/Sequel 構造の予定（Sequel beats 配置）

## 7. 作品固有チェック

- [ ] 作品固有装置（三層対応 等）の packet 整合
- [ ] 作品固有 motif の段階進行

## 8. freeze review

- [ ] Packet Freeze Review を実施
- [ ] reviewer から「frozen 可」判定が出ている

---

## 全 ✓ で packets/frozen/ へ移動。drafter に渡せる。
