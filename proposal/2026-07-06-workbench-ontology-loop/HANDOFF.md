# HANDOFF — セッション引き継ぎ（2026-07-06）

compact / セッション跨ぎ用。次のセッションはこれを最初に読む。

## いま何を作っているか
`workbench/` = 新しい StoryTemplate の作業場。成果は StoryTemplateEvolutionLab（別Git・後日）の `current/` を**置換**し、`proposal/` に1エントリ追加する形。
- `workbench/current/` … 新正本（旧STE current を置換）。ファイル数は `find workbench/current -type f | wc -l` で確認（数値のハードコードは腐るため書かない）。
- `workbench/proposal/2026-07-06-workbench-ontology-loop/` … 設計提案（PROPOSAL / COVERAGE / review-prompt / 00把握マップ / 01オントロジー見立て）。

## 決まっている方針
- **共通化**: コア+オーバーレイ。core=全作品必須、overlay=執筆単位（episode-pack / packet-2stage）、work-local=作品固有。逸脱は `work.manifest.json` に理由付きで明示。
- **人間確認**: 成果物だけ見る。ゲートは G-Intake / G-Deliverable / G-Publish の3つ。途中はループとvalidatorが自動。
- **オントロジー**: state をプロパティグラフ化（entities/knowledge_state/foreshadowing/timeline + schema）。`tools/ontology_check.py` で整合性検査（非gating warning）。
- **works は外部フォルダ**（current をコピーして作る）。runtime(drafts/reviews/approved/logs)は作品側に生まれる。`template/runtime/` が空雛形。
- **TAKT は暫定**（別セッションで詰める）。takt/README に PROVISIONAL バナー。

## 済んだこと
- 5プロジェクト解剖 → `00_現状把握マップ.md`
- オントロジー調査+設計 → `01_オントロジー適用の見立て.md`
- 新 current 構築 → current/proposal に再編
- 元STE current との突き合わせ → 取りこぼし多数発覚 → **元ファイルをコピーして踏襲**（docs/agents/skills/prompts/craft/adapter formats/review_prompts/rules/checklists、kernel完全版）。記録は `proposal/.../COVERAGE.md`、継承マップは `current/INHERITANCE.md`。

## 残TODO（COVERAGE.md 第3節）
1. コピーした旧ファイル内の相対リンク（`proposal/2026-04-30-zero-base-v4/...`）を新current内で解決するよう**張り替え**。
2. DoR/DoD の正本を**一本化**（`template/core/checklists/dor_dod.md` / `docs/dor_dod.md` / `docs/v4/06_bible_dor.md` が併存）。
3. agents 18 / skills 7 と TAKT facets の**対応表**を作る。
4. craft/rubric の実体化（evaluation-lab と接続）。

## 次の選択肢
- (A) `proposal/.../review-prompt.md` を別セッションで回して第三者監査を得る。
- (B) 残TODO 1〜2（参照張り替え・DoR一本化）をこのまま実施。
- (C) ダミー作品1本で bootstrap→ループを実走テスト。
- (D) TAKT を別セッションで確定。
