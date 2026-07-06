# Evolution の不足を点検する

> Evolution 内に「あるべきだが無い」項目を発見するプロンプト。

---

## 前提

- `prompts/00_session_start.md` を読了
- Evolution 全体構成を把握済

---

## あなたへの指示

Evolution の現状を audit し、不足 / 過剰 / 古い項目をリストアップします。

---

## Step 1. audit 対象の選定

author に確認、または自動で:

### 軸 A: ディレクトリ別 audit

- `docs/` の不足項目は?（例: motif_operations.md が無い、cadence.md が無い 等）
- `adapter/` の不足は?（例: review_adapter_prompt.md が無い 等）
- `templates/` の不足は?（例: bible/world/rules.template.md が無い 等）
- `checklists/` の不足は?
- `rules/` の不足は?

### 軸 B: 既存実作品との突き合わせ

- works/{slug}/ にあって、Evolution に対応 template が無い構造は?
- works/{slug}/.adapter/ で作品固有 customize されている部分で、Evolution に汎用版が無いものは?

### 軸 C: 過去提案との突き合わせ

`../../archive/story-template for TAKT/proposals/` の 3 Pack（v2-fat / handoff / v3-kernel）で:
- 言及されているが Evolution に未統合の項目は?

例:
- v2-fat の Review Matrix 7 種 → Evolution の checklists に対応? typed/bridge/continuity/persona/freeze/approval の各 checklist
- v2-fat の 25 項目 rubric → Evolution の checklists/rubric.template.md
- handoff の Framework Index → Evolution の templates/craft/framework_index.template.md

---

## Step 2. audit checklist

以下の表を埋める:

```markdown
| ID | 不足カテゴリ | 場所 | 必要性 | 優先度 |
|---|---|---|---|---|
| GAP-01 | docs / adapter / templates / checklists / rules / work_init | 想定パス | 何が無い | high / medium / low |
```

各 GAP に以下を付ける:

- **必要性** — なぜ必要か（実作品で発生 / 想定される / 提案 Pack 由来）
- **優先度** — 次の作業で必要 / arc 完結時に必要 / 後回しでよい
- **作成提案** — 作るならどう作るか（数行）
- **作成しない場合の代替** — 作らない場合の workaround

---

## Step 3. audit report 作成

`StoryTemplateEvolution/learning/{date}-evolution-audit.md` に:

- audit 範囲（軸 A/B/C のどれをやったか）
- 発見した GAP リスト（テーブル）
- 重複 / 過剰の発見（あれば）
- 古い項目（メンテ不足 / 作品実態と乖離）
- 全体所感（Evolution は健全 / 改善必要 / 大改造必要）
- 推奨アクション（次セッションでやるべきこと）

---

## Step 4. high priority GAP の即時対応

優先度 high で 1〜2 セッション以内に必要なものは、本セッションで作成検討:

- 作成可能なら作る
- 作成に時間かかるなら、作成計画だけ立てて後回し

---

## audit でよく見落とすカテゴリ

注意して点検すべき:

1. **review 系** — typed_review_template の本文 / persona review の本文 / continuity review の本文
2. **rubric** — 25 項目 rubric テンプレ
3. **scene/sequel craft** — 創作原理 docs
4. **want/need craft** — 同上
5. **beat sheets** — Save the Cat / 三幕構成 / Hero's Journey 等の framework lens
6. **TAKT integration** — `.takt/` の workflow yaml サンプル
7. **persona prompts** — faithful_writer / emotional_writer 等の prompt 本文
8. **judge prompt** — 自動判定 prompt
9. **ledger keeper prompt** — state 更新 persona

これらは Evolution に **未着手** の可能性が高い。

---

## 失敗パターン

1. **「全部足りない」と判定する** — 完成形を求めない。pilot-driven なので段階的でよい
2. **GAP 優先度を全部 high にする** — 本当に次セッションで必要なものだけ high
3. **過剰判定 → 削除** を急ぐ — 削除は author 承認必須。過剰でも残置の判断あり
4. **作りながら audit** — audit は「リストアップ」まで。作るのは別セッション or Step 4 のみ

---

## 成果物

- audit report 1 件（learning に）
- 必要なら GAP fix の数件（high priority のみ）
