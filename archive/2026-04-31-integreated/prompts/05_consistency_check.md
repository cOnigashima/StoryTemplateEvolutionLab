# Evolution 内の整合チェック

> ドキュメント間（docs / adapter / templates / checklists / rules / 等）の整合を点検し直すプロンプト。

---

## 前提

- `prompts/00_session_start.md` 読了
- Evolution 全体の構成把握済

---

## あなたへの指示

Evolution 内のファイル群が互いに矛盾していないか、参照リンクが有効か、用語が統一されているか等を点検し、必要に応じて修正します。

---

## Step 1. 用語整合チェック

`docs/vocabulary.md` を真として、各ファイルが従っているか:

- 禁止語が使われていないか（bundle / chapter 内部用 / backlog / 等）
- 同義語が混入していないか
- Scene と Scene Card の混同
- Review 単独使用（種別なし）
- 注意語の文脈不明使用

`grep` で機械的に検出可能:

```bash
cd write_read_novel_manufacture/StoryTemplateEvolution

# 禁止語検査
grep -rn "bundle" .
grep -rn "backlog" .
# 等
```

---

## Step 2. 単位階層整合チェック

`docs/unit_taxonomy.md` を真として:

- Manuscript / Part / Arc / Packet / Episode / Scene / Beat の使い方が正しいか
- Episode / Scene の混同なし
- Chapter が内部単位として使われていないか

---

## Step 3. kernel 整合チェック

`docs/kernel_spec.md` を真として:

- 11 項目のフィールド名が他ドキュメントで揺れていないか
- MUST / SHOULD 区別が一貫しているか
- 11 項目以上に増えていないか

---

## Step 4. status 整合チェック

`docs/status_vocabulary.md` を真として:

- 11 status 値の表記揺れなし
- Judge 4 値の表記揺れなし
- Lock 5 状態の表記揺れなし
- 各 template / checklist / proposal で正しい status 候補が使われているか

---

## Step 5. DoR/DoD 整合チェック

`docs/dor_dod.md` を真として:

- 各 checklist が DoR-A/B/C 区別を踏襲しているか
- DoD-E/P/A 区別を踏襲しているか
- writing_pack の acceptance_checklist が DoD-E と整合しているか

---

## Step 6. 参照リンク整合チェック

各ファイルから参照しているパス（`../../...`, `learning/...`, etc.）が:

- 実在するか
- typo がないか
- 正しい場所を指しているか

```bash
# Evolution 内の md ファイルから参照されているパスを抽出
grep -rh "\.\./" write_read_novel_manufacture/StoryTemplateEvolution/ | grep -oE "\`[^\`]+\`" | sort | uniq
```

---

## Step 7. adapter / templates 整合チェック

- `adapter/folder_structure.md` の構造と `templates/` 配下のファイル構造が整合しているか
- `adapter/field_mapping_template.yaml` の各フィールドが templates 内で扱われているか
- `adapter/writing_pack_format.yaml` の 4 ファイル仕様と `templates/writing/episode_pack/` の各 template が整合しているか

---

## Step 8. 提案 Pack との整合（任意）

`../story-template for TAKT/proposals/` の 3 Pack を Evolution に未統合の項目があるか軽くチェック:

- v3-kernel の 9 docs 全部 → Evolution の docs/ に転写済?
- handoff Pack の Adapter 概念 → Evolution の adapter/ に統合済?
- v2-fat の Review Matrix → Evolution の checklists/ に統合済?

---

## Step 9. 修正実行

発見した整合違反を修正:

- 用語修正（`docs/vocabulary.md` 準拠に置換）
- 参照リンク修正
- status 値の表記統一
- 構造の整合

ただし:

- **大規模な構造変更は author 承認必須**
- 軽微な typo / 用語 / リンクは即修正可
- 構造的な矛盾を発見したら author に上げる（解消案は提示）

---

## Step 10. learning に記録

`StoryTemplateEvolution/learning/{date}-consistency-check.md` に:

- audit 対象（Step 1〜8 のどれを実施したか）
- 発見した整合違反（種別 + 件数）
- 修正した件 / 修正できなかった件（author 上げ）
- 全体所感
- 次回 audit ポイント

---

## 失敗パターン

1. **用語を勝手に変える** — vocabulary.md と異なる用語が出た場合、本当に間違いか? 新概念か? を author に確認
2. **参照リンクを勝手に削除** — リンク先が無くても、後で作る予定かもしれない。author 確認
3. **構造を統一しすぎる** — 多少の差異は意図的な場合あり
4. **proposal Pack を再統合** — 本セッションで作業範囲外。learning に「未統合あり」と記録するだけ
5. **fix の grep / sed で全置換** — 文脈無視で置換すると意味が変わる。手動チェック必須

---

## 成果物

- 整合 audit report 1 件（learning に）
- 軽微修正のコミット（数件〜10 件）
- 大規模整合違反の author 上申（あれば）
