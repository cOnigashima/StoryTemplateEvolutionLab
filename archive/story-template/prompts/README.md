# Story Template Prompts

ChatGPT / Claude に貼るための prompt 集。
共通ルールはまず `common-preamble.md` を先頭に付け、そのあと目的別 prompt を使う。

使い分け:

- ChatGPT / Claude の Web UI:
  この `prompts/` をそのまま使う
- Codex / Claude Code:
  `README.md` と `CLAUDE.md` を運用ガイドにしつつ、必要に応じてこの `prompts/` を素材に流用する

## 推奨順序

1. `common-preamble.md`
2. `promises.md`
3. `world.md`
4. `characters.md`
5. `rules.md`
6. `series-overview.md`
7. `arc-01.md`
8. `packet-scoped.md`
9. `packet-freeze-check.md`
10. `scene-batch.md`

## 執筆開始ライン

- `story/promises.md` がある
- `bible/world.md`, `bible/characters.md`, `bible/rules.md` がある
- `arcs/arc-01.md` がある
- `packets/frozen/` に 1 本ある
- `scenes/` に first episode を書ける scene 群がある
- blocker な open question がない

## 完了ライン

- `drafts/` に対象 draft がある
- `reviews/` に typed review がある
- 必要な canon 修正が `bible/` に反映されている
- 未反映のものが `story/canon-patch-proposals/` にある
- 長生きする問題が `story/design-debt.yaml` にある
- `approved/` と `published/` に成果物がある

## 方針

- 会話ログから直で本文へ飛ばない
- `Promise -> Arc -> Packet -> Scene -> Draft` の順で下ろす
- 空欄は禁止。未確定は `未決定`
- `packets/scoped/` で作り、`packet-freeze-check.md` で `packets/frozen/` に上げる
