# ファイル成長ルール

Story OS のファイルは **1ファイルで始めて、育ったら分割する**。
テンプレートが持つ初期ファイルは最小構成であり、上限ではない。

## 基本原則

- 1 ファイルが **300 行を超えた**、または **関心軸が 2 つ以上混在している** なら分割を検討する
- 分割しても、元ファイルは索引（目次＋参照リンク）として残す
- 新ファイルの命名は既存パターンに揃える（`.claude/rules/naming-conventions.md` があればそれに従う）
- 分割は author の承認を得てから行う。自己判断で分割しない
- **まだ書く必要のないファイルを先回りで作らない**。「次の 1〜2 packet の因果に効くか」が判断基準

## ディレクトリ別の成長パターン

### bible/

初期状態: `characters.md`, `world.md`, `rules.md` の 3 ファイル。

成長の兆候と分割パターン:

- キャラが 5 人を超え、1 人あたりの記述が長い
  → `character-sheets.md`（詳細シート）を分離。`characters.md` は索引にする
- 会話パターン・口調・禁則語が独立した管理対象になった
  → `dialogue-bible.md` を新設
- 世界のサブシステム（魔法体系、経済、政治）が複雑になった
  → `system-bible.md` や `world-{subsystem}.md` に分離
- 繰り返し登場する NPC が増えた
  → `world-regulars.md`（レギュラーNPC 一覧）を新設
- 関係性の変化が物語の駆動力になっている
  → `relationship-sheet.md` を新設
- テンプレートが欲しくなった
  → `bible/templates/` を作り、character-sheet / relationship-sheet / world-sheet のテンプレートを置く

`characters.md`, `world.md`, `rules.md` の 3 ファイル自体は常に存在させる。分割後も索引＋要約として機能させる。

### arcs/

初期状態: `series-overview.md`, `arc-01.md`。

成長の兆候と分割パターン:

- Arc が増えた → `arc-02.md`, `arc-03.md` を追加
- Arc 内のユニット（章・卓・パートなど）ごとに設計シートが必要になった
  → `design-sheet-{unit-slug}.md` を追加
- キャラの出現マップ、関係変化マップが欲しくなった
  → `character-appearance-map.md`, `relationship-changes.md` を追加
- 伏線の配置管理が必要になった
  → `foreshadowing-placement.md` を追加
- エピソード割り当ての構造表が欲しくなった
  → `episode-structure.md` を追加
- Arc の中間チェックポイントを記録したい
  → `arc-01-checkpoint-{slug}.md` を追加

`series-overview.md` は常にシリーズ全体の見取り図として維持する。

### packets/

初期状態: `exploring/`, `scoped/`, `frozen/` の 3 ステージ。

成長の兆候と分割パターン:

- frozen から draft に進んだが、draft 中に packet 自体を修正したくなった
  → `drafting/` ステージを追加（frozen のコピーを置いて作業する。frozen 側は凍結のまま残す）
- 古いバージョンの frozen packet を残したい
  → `packet-001-{slug}-v1-superseded.md` のように旧版をファイル名で区別する
- packet の凍結チェックや再凍結チェックのテンプレートが欲しい
  → `packets/templates/packet-frozen-checklist.md` を新設

### scenes/

初期状態: `seed/scene-template.md` のみ。

成長の兆候と分割パターン:

- scene card がエピソードに割り当てられた
  → `slotted/` に移動。命名: `packet-{NNN}-ep{NN}-{slug}.md`
- scene card が改訂された（古い版を残したい）
  → `superseded/` に旧版を移動
- 大規模な改稿で世代管理したい
  → `archive-v1/`, `archive-v2/` で世代ごとに保管

`seed/scene-template.md` は常にテンプレートとして残す。

### story/

初期状態: `promises.md`, `open-questions.md`, `design-debt.yaml`, `seeds/`, `canon-patch-proposals/`。

成長の兆候と分割パターン:

- 作品の全体像を1枚で見たい
  → `one-pager.md`（15 項目程度のワンページャー）を新設
- 伏線が複数軸あり、管理が必要になった
  → `foreshadowing-map.md` を新設
- テンプレート（伏線台帳、プロジェクトシートなど）が欲しい
  → `story/templates/` を新設

### reviews/

初期状態: `README.md` のみ。

成長の兆候と分割パターン:

- typed review を繰り返し書く
  → `typed-review-template.md` を作り、毎回のレビューはテンプレートに従って増やす
- 3パス設計レビュー、読者ペルソナレビューなど手法が増えた
  → 手法ごとにテンプレートファイルを追加
- レビューが溜まってきた
  → 命名で整理: `typed-review-{date}-{slug}.md`, `reader-review-{slug}.md` 等

### prompts/

初期状態: 11 ファイル（設計フェーズ用の prompt 群）。

成長の兆候と分割パターン:

- ドラフト後のレビュー用 prompt が生まれた
  → `scene-density-review.md`, `reader-review-personas.md` 等を追加
- 自動化ループ用の prompt が必要になった
  → `automation-{purpose}.md` を追加

### learning/

成長は learning-capture.md のルールに従う。日付＋slug で増やす。
繰り返し参照されるログは `.claude/rules/` や `bible/rules.md` に昇格させる。

## 分割してはいけないもの

- `CLAUDE.md` — 制作契約は1ファイルに集約する
- `story/promises.md` — 作品約束は1ファイルで一覧性を保つ
- `story/design-debt.yaml` — 負債台帳は1ファイルで管理する

これらが肥大した場合は、分割ではなく要約・圧縮で対応する。

## 分割時の手順

1. author に「このファイルを分割したい。理由は○○」と提案する
2. 承認を得たら、新ファイルを作成する
3. 元ファイルを索引化する（本体を消さない。参照リンクを張る）
4. `CLAUDE.md` の参照ファイルセクションに新ファイルを追加する
5. 分割の経緯を `learning/` に記録する
