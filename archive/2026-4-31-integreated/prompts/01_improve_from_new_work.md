# 既存作品から学びを抽出する

> 既存作品（fools-with-cheating 等）の運用経験を Evolution に持ち上げるためのプロンプト。

---

## 前提として読むべきもの

1. `prompts/00_session_start.md` — セッション全体方針
2. `learning/2026-04-29-template-extraction-method.md` — 抽出方法論

---

## あなたへの指示

ある作品（以下「対象作品」）を観察し、その作品で発見されたパターン / 問題 / 改善点を Evolution に取り込みます。

---

## Step 1. 対象作品の特定

author に確認:

- 対象作品は? （例: works/fools-with-cheating/）
- 観察対象期間は? （特定の arc / packet / ep / セッション）
- 何を見てほしいか? （bible / design / state / writing / draft / review）

決まったら、対象作品の `CLAUDE.md` と `README.md` を読む。

---

## Step 2. 観察対象の探索

対象作品の以下を読む（必要範囲のみ）:

```
- {対象作品}/CLAUDE.md
- {対象作品}/bible/  → 構造の特徴
- {対象作品}/design/project_principles.md  → 作品固有作劇ルール
- {対象作品}/design/critical_intent.md  → 批評性
- {対象作品}/state/  → 動的状態の使い方
- {対象作品}/writing/episode_packs/  → Writing Pack の使い方
- {対象作品}/learning/  → 失敗・学びの蓄積
- {対象作品}/.adapter/  → 作品固有の Adapter カスタマイズ
```

---

## Step 3. 抽出候補の判定

各観察項目について以下を問う:

```
Q1. このパターンは他作品でも使えるか?
  Yes → Q2 へ
  No  → 作品固有として残置（template 化しない）

Q2. このパターンは Evolution の既存ファイルでカバー済か?
  Yes → 既存ファイルを更新 or 検証で済ます
  No  → 新規追加候補

Q3. 新規追加するなら、どの場所に?
  - docs/        → 概念・仕様
  - adapter/     → Adapter 設計
  - templates/   → 雛形
  - checklists/  → チェックリスト
  - rules/       → .claude/rules/ 追加候補
  - work_init/   → 新規作品手順
```

---

## Step 4. 抽出実行

新規追加候補ごとに:

1. Evolution 内の既存ファイルとの衝突確認
2. 該当ディレクトリにファイル新設 or 既存ファイルに追記
3. 作品固有要素を取り除き、構造のみを汎用化
4. 「{対象作品} で確認」のような出典明記
5. 関連する Evolution の他ファイルから参照リンクを張る

---

## Step 5. 作品 → Evolution の逆フロー

抽出した結果を、対象作品の側にも反映:

- 対象作品の `CLAUDE.md` に「Evolution の {新ファイル} を参照」を追記
- 対象作品の `.adapter/` に新ルール / template を反映（必要なら）

---

## Step 6. learning に記録

`StoryTemplateEvolution/learning/{date}-improvement-from-{work-slug}.md` に:

- 対象作品 / 観察期間
- 抽出した項目（リスト + Evolution 内追加先）
- 残置した項目（list + 残置理由 = 「作品固有のため」）
- 次回観察時のポイント

---

## 失敗パターン

1. **作品固有要素を template に流す** — renji の三層対応のような装置は template 禁止
2. **抽出のために抽出する** — 「他作品で本当に使うか?」を毎回問う
3. **既存 Evolution ファイルを大改造** — 追記 / 新設で済ませる（破壊的変更は author 承認）
4. **対象作品を勝手に変える** — 作品の bible / design は触らない（参照リンク追加程度のみ）
5. **「最強テンプレ」化** — 各 Evolution ファイルが薄く保たれているか確認

---

## 成果物

- Evolution 内の更新 / 新設ファイル（数件〜10 件程度）
- learning ログ 1 件
- 対象作品の CLAUDE.md or .adapter への参照追加（任意）

---

## 注意

- 対象作品の本文（drafts/）を読む必要はない（時間がかかる）
- 設計層（bible / design / .adapter）の構造を見るのが主
- 1 セッションで全部抽出しようとしない（数項目で十分）
