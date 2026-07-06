# Packet Freeze Review — packet-NNN-{slug}

> **対象**: `packets/scoped/packet-NNN-{slug}.yaml`
> **日付**: YYYY-MM-DD
> **起動 skill**: `/freeze-review`
> **関連 rule**: `.claude/rules/review-system.md`, `.claude/rules/drafter-preflight.md`

---

## 1. 必須セクション存在チェック

- [ ] purpose
- [ ] entry_state / exit_state
- [ ] stakes / pressure
- [ ] episode_roles（ep01..epNN 全話分）
- [ ] end_hooks
- [ ] disclose / withhold
- [ ] guardrails
- [ ] focus / dependencies
- [ ] episodes[] 各話（role / purpose / desire / obstacle / loss / gain / emotion_curve / reveal / hooks / cliffhanger / draft_file / scenes_merged）
- [ ] open_questions
- [ ] freeze_check

## 2. 依存解決

- [ ] `story/promises.md` 該当セクションと矛盾なし
- [ ] `bible/world.md` / `characters.md` / `rules.md` と矛盾なし
- [ ] `arcs/arc-NN.md` と矛盾なし
- [ ] 前 packet との bridge-review 実施済み（packet-001 は除く）
- [ ] 依存する seed / open-questions を review 済み
- [ ] 依存する canon-patch-proposals が承認済み or 保留扱いで安全

## 3. 作品固有チェック（該当作品のみ）

- [ ] 反復 motif の ep 割り当て密度マップが packet 内に存在する
- [ ] withhold 辞書（monitoring-dictionary）が現行 packet に追従している
- [ ] 前 packet からの carryover が各 ep で再起動計画されている

## 4. preflight 前準備

- [ ] 各 ep の `task-context.yaml` 雛形が生成可能な情報量が揃っている
- [ ] 各 ep の scene card（seed または slotted）が揃った、または同時着手の scope 宣言がある
- [ ] Gate 0（直前 ep 散文照合）で参照すべき前 ep 範囲が明確

## 5. 読者体験チェック（簡易 persona review）

- [ ] hook が各 ep に設計されているか（cliffhanger / reveal）
- [ ] disclose / withhold バランスが読者の推理可能範囲を保っているか
- [ ] climax 配置が ep 後半に偏りすぎていないか（canon-patch-017 起源）

## 6. 契約チェック（典型問題）

- [ ] packet 跨ぎ伏線の末尾 ep 保留 signal が存在（villainess-coc §2.6 由来）
- [ ] 連続無接続 ep が 3 本以上続いていない
- [ ] 接続ビート保有率が 50% 以上

## 7. freeze 判定

- 結果: `freeze / return-to-scoped`
- return 理由（あれば）:
- 次アクション:
- freeze 後の `drafts/packet-NNN/` 構造準備:
  - [ ] 各 ep の task-context.yaml 作成
  - [ ] 該当 scene card を slotted/ に移動
