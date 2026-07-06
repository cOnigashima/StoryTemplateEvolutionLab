# Craft Library

物語を書くときに参照する **一般原理** の道具箱。作品固有の約束は `bible/` に、守るべき規範は `.claude/rules/` に、**使う道具** は本ディレクトリに置く。

> **母体**: `know_how_explore/`（外部）から本 template 正典へ昇格させたもの
> **設計**: `proposals/2026-04-22-story-template-v2/05-craft-library.md`

## 構成

| カテゴリ | ファイル |
|---|---|
| 原理 | `principles.md` |
| Scene/Sequel | `scene-sequel.md` |
| キャラ動機 | `want-need.md` / `character-design.md` |
| 設計ガードレール | `scope-management.md` / `cadence.md` |
| 構造の型 | `beat-sheets.md` / `reveal-plan.md` |
| 伏線 | `foreshadowing.md` |
| モチーフ | `motif-operations.md` |
| 対話・描写・POV | `dialogue-craft.md` / `description-craft.md` / `pov-craft.md` |
| 対立・世界・テーマ | `conflict-design.md` / `world-design.md` / `theme-design.md` |
| ジャンル | `genre-patterns.md` |
| 推敲 | `editing-craft.md` |
| ジャンル特化則 | `sanderson-laws.md` / `knox-rules.md` |
| 評価基準 | `rubric.md` / `reader-personas.md` |
| チェックリスト | `checklists/*.md` |
| ワークシート | `worksheets/*.md` |

## 使い方

- drafter は draft 前に関連 craft を読む（Scene/Sequel, Want/Need, POV）
- critic は review 時に関連 craft を参照（rubric, reader-personas, foreshadowing, cadence）
- plotter は arc / packet 設計時に型を選ぶ（beat-sheets, reveal-plan, conflict-design）
- release は approval 時に最終 craft チェック（editing-craft）

## ファイル内テンプレ

各 craft ファイルは以下の節で書く:

1. 一行定義
2. なぜ大事か（物語への効能）
3. 原理
4. 実装手順
5. 判定基準（review 時の観点）
6. 失敗パターンと直し方
7. チェックリスト
8. 参考ワークシート（あれば）
9. 出典

## 維持

- 新項目追加は author 承認
- 廃止は `craft/archive/` に移動（削除しない）
- 作品固有化が進みすぎた項目は作品側に戻す
