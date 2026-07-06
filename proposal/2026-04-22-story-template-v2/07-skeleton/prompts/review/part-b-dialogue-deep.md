# PART B — 対話特化レビュー プロンプト

> **起源**: `know_how_explore/小説レビュープロンプト.md` PART B（TD1-TD4）
> **関連**: `craft/dialogue-craft.md`, `.claude/rules/review-system.md`

---

## 役割

対話を 4 項目で深く診断する。台詞が地の文と分離しているか、話者が識別できるか、情報と感情と関係を同時に運べているか。

## 入力

- draft 本文
- bible/characters.md（声・関係）
- bible/rules.md（文体・方言）

## 項目（4 件）

### TD1 話者識別精度
- 話者ラベルを外した状態で誰の発言か識別できるか
- 語尾・語彙・話題選択・関係態度で区別できているか

### TD2 情報密度
- 1 つの台詞が複数機能（情報提供＋感情表現＋関係温度＋次行動喚起）を持てているか
- 情報提供だけの平坦な台詞になっていないか

### TD3 方言・立場・関係の表現
- 社会階層・年齢・立場・親密度が台詞で読めるか
- bible で定義された声が実装されているか

### TD4 モノローグの抑制
- 地の文に埋め込まれた「独白」が過剰になっていないか
- 台詞で語るべきことを地の文で語っていないか / その逆

## 手順

1. 台詞のみ抽出して読む
2. 各項目を 0-4 で採点、該当行を引用
3. 改善案を 3 つ以上提示（書き換え案を含む）

## 出力

`reviews/typed-review-{target-slug}.md` PART D-2（対話）に反映、または単独 `reviews/part-b-dialogue-{target-slug}.md` として起こす。

---

## 関連

- `craft/dialogue-craft.md`
- `prompts/review/part-a-per-scene.md`
- `prompts/review/part-c-macro-structure.md`
