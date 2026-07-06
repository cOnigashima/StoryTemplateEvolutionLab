# prompts/

> StoryTemplateEvolution の改善作業をゼロベースで継続するための入口 prompt 群。
> 新セッション（Codex / Claude / 任意の AI）が、過去のセッションコンテキストなしに作業に入るための prompt。

---

## 使い方

新セッション開始時、いずれかの prompt をエージェントに貼り付ける。

| 状況 | 使う prompt |
|---|---|
| とにかく Evolution の改善を続けたい | `00_session_start.md` |
| ある作品（fools-with-cheating 等）から学びを Evolution に持ち上げたい | `01_improve_from_new_work.md` |
| Evolution に何が足りないかを点検したい | `02_audit_gaps.md` |
| 作品から見つけたパターンを template に抽象化したい | `03_extract_pattern.md` |
| 新規作品で Evolution を初めて使いたい | `04_apply_to_new_work.md` |
| Evolution 内のドキュメント間整合を直したい | `05_consistency_check.md` |

---

## 設計原則

各 prompt は:

1. **自己完結**: そのセッションだけで理解できる
2. **読むべき順序が明示**: 何をどの順で読むべきか
3. **成果物が明示**: 何を作って終わるか
4. **失敗パターン回避**: やりがちな間違いを最初に列挙

---

## 既存の作業履歴（参照用、必要に応じて読む）

- `../learning/2026-04-29-renji-pilot-retro.md` — Evolution が生まれた経緯
- `../learning/2026-04-29-template-extraction-method.md` — 抽出方法論
- `../learning/2026-04-29-handoff-to-next-session.md` — 過去セッションからの引き継ぎ
- `../proposals/2026-04-29-pilot-driven-evolution/04_next_steps.md` — 次のステップ候補

---

## prompt 執筆規約

新しい prompt を本ディレクトリに追加するとき:

- 番号 prefix（00, 01, 02, ...）で読み順 / 重要度を示す
- 1 prompt = 1 タスク
- 入出力を明示
- 「これを読む前に何を読むべきか」を冒頭に
- 完了時の成果物を明示
- 失敗パターンを末尾に
