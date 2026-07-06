# 次のステップ

> 本提案を踏まえて次セッション以降にやることの指針。
> 詳細な引き継ぎは `../../learning/2026-04-29-handoff-to-next-session.md`。

---

## 即着手候補

### A. ep001 本文を書く

**目的**: renji の最初の 1 話を完成させる。pilot の真の検証。

**入力**: works/renji/writing/episode_packs/ep001/ + works/renji/bible/ + works/renji/state/

**成果物**: works/renji/drafts/episodes/ep001-{slug}.md

**実行者**: Codex / Claude / 人間（author 選択）

**所要**: 1〜2 セッション

---

### B. renji bible Phase B に進める

**目的**: ep002-012（arc-1）が書ける状態にする。

**作業内容**: source_mapping.md の Phase B / C を実行。bible/characters/individual の追加、bible/plot の充実、state seed の拡張。

**実行者**: Codex（決定論的作業が多い）

**所要**: 1 セッション

---

### C. 別の新規作品を起こす

**目的**: StoryTemplateEvolution の真の汎用性検証。renji だけでは pilot として偏る可能性。

**作業内容**: work_init/new_work_bootstrap.md の手順で別作品を起こし、ep001 まで通す。

**実行者**: 人間 + Claude

**所要**: 2〜3 セッション

---

## 中期課題

### 1. 旧 v1 の整合 / archive 化

`story-template for TAKT/` 配下の v1 と提案 3 Pack をどう扱うか:

- **Option A**: そのまま温存（足跡として）
- **Option B**: archive ラベルを付けて「参照のみ」明示
- **Option C**: 削除（推奨しない、履歴として価値あり）

### 2. CLAUDE.md / .claude/rules/ の本 v2 整合

- 旧 CLAUDE.md を本 v2 と整合させる
- `intake-flow.md` 等の新ルールを `.claude/rules/` に追加

### 3. 3 提案パックからの追加抽出

本 v2 に未統合の項目があるかも:

- v2-fat の Review Matrix 7 種 → 本 v2 では未実装。次セッションで `checklists/review-matrix.template.md` 等を追加検討
- v2-fat の 25 項目 rubric → 本 v2 では未実装。次セッションで `checklists/rubric.template.md` 検討
- handoff の Framework Index → 本 v2 では未実装。実適用案件が出たら追加

### 4. Adapter の TAKT step 化

TAKT 採用が確定したら、Intake Adapter / Writing Adapter を `.takt/workflows/` の YAML として実装。

### 5. 複数 writer tournament（episode-draft-tournament）

現在は 1 writer 想定。複数 writer での tournament 方式は handoff Pack で議論された。次の課題。

---

## 長期課題

### 1. Story Template v3 への昇格

複数作品（renji + 他作品）を経て、本 v2 が安定したら:

- StoryTemplateEvolution を `story-template/` の正式版として昇格
- 旧 v1 を archive 化
- 別作品の bootstrap 時に本リポジトリを参照する

### 2. Review system の完成

- typed_review / bridge_review / continuity_review / persona_review / freeze_review / approval_review の各 prompt 整備
- review template 整備
- review skills の TAKT 化

### 3. ledger keeper persona の実装

- 各 ep 公開後、ledger を自動更新する persona の prompt
- TAKT step として実装

### 4. 公開フロー（Layer 4 Release）

- approved/ → published/ への自動化
- カクヨム投稿 API があれば活用（現状はない）
- AI タグ自動設定

### 5. Retro 自動化

- 各 arc 完結時の retro を半自動化
- learning/ への自動キャプチャ

---

## やらないこと（明示的）

renji_novel_bible/ 由来の議論で「今やらない」と決まったもの:

- 全創作理論の deep research
- 最強テンプレ完全版
- 全ジャンル overlay 作成
- Framework Index の網羅
- 1000 タスク完全整理
- 大量 reviewer 一気導入
- 精密スコアリング体系

これらは pilot が安定し、複数作品が走り、template が安定した後に再検討。

---

## 次セッション開始時の checklist

セッション開始時に必ず確認:

- [ ] 本ファイルを読了
- [ ] handoff-to-next-session.md を読了
- [ ] retro を読了
- [ ] author に「今日のゴール」を確認
- [ ] 既存資産の最新状態を確認（git log で本セッション以降の変更）
- [ ] AD-XX 系の判断待ち項目を author に確認

---

## 緊急時の rollback

万一、本 v2 への移行で問題が出た場合:

- works/renji/ は story-template for TAKT/ 配下のまま動作する
- StoryTemplateEvolution/ を一時的に無視して、旧 v1 + works/renji/.adapter/ で進める
- 後で再整理

---

## 結論

本セッションで:
- 設計議論の散らかり（v2-fat / handoff / v3-kernel）から脱出
- 実走（renji pilot）に集中
- StoryTemplateEvolution として実物中心の v2 を構築
- pilot-driven extraction 方法論を確立
- ep001 を書ける状態に到達

次は **書く**。設計はもう十分。
