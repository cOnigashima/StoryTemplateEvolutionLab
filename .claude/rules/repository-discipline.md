# Repository Discipline

> StoryTemplateEvolution リポジトリ自身の編集規律。

## MUST

1. **archive/ を編集しない**
2. **三本柱（current / proposal / archive）の境界を維持する**
3. **採用済み proposal（2026-04-30-zero-base-v4 / 2026-07-06-workbench-ontology-loop）を archive に下ろす前に必ず author 確認**
4. **supersede stub を直接書き換えない**（proposal 側で議論して、ここに反映）
5. **新規提案は `proposal/{YYYY-MM-DD}-{slug}/` の形式で**
6. **作品固有 facet を generic templates に流入させない**

## SHOULD

7. 重要な変更は `learning/{date}-{slug}.md` に retro 記録
8. v4 後追い TODO（Q-B-001 等）に着手する場合は 09_open_questions.md を先に確認
9. 既存 work（ia_society / fools-with-cheating 等）への影響は migration_plan.md を参照

## NG

- v3 の `bible/plot/` ディレクトリパターンを v4 で復活させる
- `bundle` `chapter (内部)` `Review (単独)` の使用
- `.adapter/` (dot あり) の使用
- `Premise` (kernel #1 として) の使用 — `Logline` を使う
