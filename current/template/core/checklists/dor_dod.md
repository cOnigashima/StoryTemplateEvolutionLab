# origin: STE-v4
# DoR / DoD ゲート — 各工程に進んでよいかの判定基準（中身入り）

## DoR-A（Bible完全性）— これを満たしたら執筆開始できる

- [ ] kernel 11項目が MUST 全て `filled`（未確定は status で明示、`missing` が無い）
- [ ] promise が3項目以上ある
- [ ] bible の各 facet（world / characters / rules / style-voice …）の最小項目が埋まっている
- [ ] state/entities.yaml に主要キャラの ID が振られている
- [ ] `contradiction` status がゼロ
- [ ] `tools/ontology_check.py` が参照整合性エラーを出さない

## DoR-B（Writing Pack整備）— 1話を draft してよい

- [ ] Writing Adapter の出力4点（episode_brief / scene_card / context_pack / acceptance_checklist）が揃う
- [ ] acceptance に must_satisfy（5〜10）と must_not_violate（禁則）が定義済み
- [ ] context_pack に「この話に必要な entity と、その時点の knowledge_state」が抽出済み

## DoR-C（Packet凍結）— overlay=packet-2stage の場合のみ

- [ ] packet の purpose / episode_roles / disclose / withhold / guardrails が埋まる
- [ ] entry_state / exit_state が直前 packet と整合
- [ ] episode の知識状態が単調（ontology_check の epistemic_monotonic が通る）

## DoD-E（承認）— 公開してよい（★人間ゲート G-Deliverable/G-Publish）

- [ ] acceptance_checklist の must_satisfy 全充足・must_not_violate 違反ゼロ
- [ ] multi-pass self-review 通過
- [ ] typed review + persona review の採否判定が出て、採用分が反映済み
- [ ] ontology_check が epistemic矛盾・未回収伏線（当該話で回収予定のもの）を出さない
- [ ] kakuyomu-policy（AI表記・投稿頻度）に適合
