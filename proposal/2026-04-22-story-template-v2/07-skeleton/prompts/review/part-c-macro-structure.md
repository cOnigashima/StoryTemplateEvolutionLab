# PART C — マクロ構造レビュー プロンプト

> **起源**: `know_how_explore/小説レビュープロンプト.md` PART C（ML1-ML5+）
> **関連**: `craft/beat-sheets.md`, `craft/reveal-plan.md`, `.claude/rules/review-system.md`

---

## 役割

作品全体 / arc / packet のマクロ構造を診断する。個別 ep の診断は PART A/B、本 PART はマクロ専用。

## 入力

- arcs / packets 群
- 既公開 draft 群
- story/promises.md
- story/foreshadowing-map.md

## 項目

### ML1 作品約束との整合
- story/promises.md の各項目が現在の実装で守られているか
- 守れなくなっているなら、promise 側を改訂すべきか、実装側を戻すべきか

### ML2 Arc 骨格
- 採用したビートシート（Save the Cat / 三幕 / 起承転結）の型に対して、現在の配置がどう整合するか
- ミッドポイント・オールイズロスト等の大きな節点に実装が存在するか

### ML3 伏線グラフ
- foreshadowing-map の全伏線を 3 度の原則（埋・匂・強）で配置できているか
- 回収期限を過ぎた伏線 / 回収されない伏線の数と理由

### ML4 Reveal Plan
- fabula（時間順の事実）と syuzhet（読者への提示順）が別管理できているか
- Reveal のフェア度（手がかりから推理可能か）

### ML5 Cadence / Rhythm
- packet 単位の緊張弛緩比率（基準 6:4）
- 長い弛緩 / 長い緊張が連続していないか
- Scene/Sequel の交互性

### ML6 Scope Management
- 登場人物数 / 視点数 / 時間軸 / ルール例外数が上限内か
- 爆発の兆候があれば design-debt 起票

### ML7 Theme Proving
- テーマが作中で「証明」されているか（主張だけで終わっていないか）

## 手順

1. 対象範囲（arc 全体 / packet 群）を決める
2. 各項目を 0-4 で採点
3. マクロ構造の変更を要する場合、差し戻し先を明示:
   - arcs/ 改訂
   - packets/ 再凍結
   - story/promises.md 改訂
   - canon-patch-proposals 起票

## 出力

`reviews/typed-review-{target-slug}.md` または `reviews/macro-review-{target-slug}.md`。

---

## 関連

- `craft/beat-sheets.md`
- `craft/reveal-plan.md`
- `craft/cadence.md`
- `prompts/review/part-a-per-scene.md`
- `prompts/review/part-b-dialogue-deep.md`
