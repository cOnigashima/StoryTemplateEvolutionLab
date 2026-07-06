# 新規作品で Evolution を初めて使う

> 新作品の bootstrap で Evolution の templates / adapter / docs を使うプロンプト。
> 同時に「実際に使ってみて Evolution の不足を発見する」検証セッションでもある。

---

## 前提

- `prompts/00_session_start.md` 読了
- `work_init/new-work-bootstrap.md` を読む（本 prompt の詳細手順）

---

## あなたへの指示

新規作品 directory を起こし、Evolution の templates から init して、ep001 の Writing Pack まで作ります。

---

## Step 1. 新作品の前提確認

author に確認:

- 作品 slug
- 配置先（推奨: `works/{slug}/`）
- 既存資料の有無（あれば inbox に raw として配置）
- 完全新規 or 既存資料あり
- 想定規模（短編 / 中編 / 長編）
- ジャンル

---

## Step 2. work_init を実行

`work_init/new-work-bootstrap.md` の Step 1〜14 に従う:

```
Step 1.  ディレクトリ作成
Step 2.  .claude/rules/ 継承
Step 3.  .adapter/ コピー
Step 4.  CLAUDE.md 作成
Step 5.  inbox/ に初期素材を配置
Step 6.  Intake Adapter 実行
Step 7.  Human Approval
Step 8.  bible/design/state 反映
Step 9.  story/kernel.yaml 作成
Step 10. DoR-A チェック
Step 11. arc-1 / packet-001 最小設計
Step 12. ep001 Writing Pack 生成
Step 13. DoR-B チェック
Step 14. （次セッション）執筆開始
```

各 Step は work_init の本ファイルに詳細あり。

---

## Step 3. Evolution の不足を記録

bootstrap 中に「あれ、これ Evolution の templates に無いな」と気づいた項目を都度メモ:

```markdown
## bootstrap 中に発見した Evolution の不足

- {新作品が必要としている template / docs / rule で Evolution に無いもの}
- なぜ必要か
- 暫定対処（作品内で個別作成 / 後で Evolution に追加）
```

---

## Step 4. 比較 audit

bootstrap 完了後、以下を比較:

| 項目 | 新作品で実装 | Evolution に template あり? | template が機能した? |
|---|---|---|---|
| premise | ○ | ○ | yes/no |
| reader_promise | ○ | ○ |  |
| theme | ○ | ○ |  |
| ... |  |  |  |

機能しなかった template があれば改善候補に。

---

## Step 5. learning に記録

`StoryTemplateEvolution/learning/{date}-applied-to-{work-slug}.md` に:

- 新作品 slug
- bootstrap の所要時間
- 各 Step で問題なく進めたか
- Evolution templates の機能度（well / OK / 不足あり）
- 発見した不足 / 改善候補
- 次セッションで Evolution に追加すべき項目

---

## Step 6. Evolution への即時反映（high priority のみ）

「次の作品も同じ問題に当たる」のような high priority な不足は本セッション中に Evolution に追加検討。

ただし「軽微」「特殊」なものは learning に書いて後回しでよい。

---

## bootstrap 中に注意すべきこと

### Adapter の使い方が分からないとき

- `adapter/intake_adapter.md` を読み直す
- `adapter/writing_adapter.md` を読み直す
- renji の `works/fools-with-cheating/.adapter/` を実例として参照

### template が空欄ばかりで何を書けばいいか分からないとき

- 各 template ファイルの `<!-- example -->` ヒント注釈を読む
- renji の対応ファイル（`works/fools-with-cheating/bible/{path}`）を実例として参照
- author に「ここはどう埋めるか」を聞く

### kernel 11 項目が多くて埋めきれないとき

- MUST と SHOULD を区別（`docs/kernel_spec.md`）
- SHOULD は status: deferred / tentative で OK
- MUST が埋まらないなら status: needs_author_decision で author 待ち

### 作品固有装置を作りたくなったとき

- まず「これは Evolution に汎用化できる装置か?」を判定
- 汎用なら新 template 候補
- 作品固有なら作品の bible/world/{name}.md として個別作成

---

## 失敗パターン

1. **Evolution の templates だけで埋めようとする** — 作品固有要素が必ずあるので、bible に作品固有 file を加える
2. **bootstrap を完璧に終わらせようとする** — pilot で OK、不足は次セッション
3. **kernel を全部 filled にしようとする** — needs_author_decision / tentative も valid
4. **新作品の bible を Evolution の templates と完全同期させる** — 作品固有 / 汎用の境界を維持
5. **発見した不足を即 Evolution に反映** — high priority のみ即時、他は learning に

---

## 成果物

- 新作品 directory `works/{slug}/`（bootstrap 完了状態）
- 新作品の ep001 Writing Pack
- learning ログ 1 件（applied to / 不足発見）
- Evolution への小改善（あれば数件）

---

## 期待される所要時間

- 既存資料あり（renji 級）: 2〜3 セッション
- 完全新規（kernel から）: 3〜5 セッション

1 セッション完結は無理。複数セッション前提で進める。
