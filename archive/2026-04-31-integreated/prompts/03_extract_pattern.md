# パターンを template に抽象化する

> 作品 / 作業で見つけた具体的なパターンを Evolution の template に汎用化するプロンプト。

---

## 前提

- `prompts/00_session_start.md` 読了
- `learning/2026-04-29-template-extraction-method.md` 読了
- 抽象化したい具体例が手元にある

---

## あなたへの指示

1 つの具体例（ある作品のあるファイル / ある手順 / ある書き方）から、他作品でも使える structure を抽出して template 化します。

---

## Step 1. 抽出対象の特定

author or 自分で:

- **対象は何?** — 具体的なファイル / 手順 / 書き方
- **どこから?** — works/{slug}/{path} or proposals/{...}
- **これは pattern か specific か?** — 他で使える構造か、その作品 / 場面に固有か

判定基準:

```
Q. このパターンは他作品で「同じ役割」を果たすか?
  Yes → template 化候補
  No  → 作品固有として残置

Q. 他作品で使うとき、構造の何割を流用できるか?
  80%+ → template 化に値する
  50-80% → 部分 template + 作品ごとカスタマイズ
  50% 未満 → 個別ケース、template 化しない
```

---

## Step 2. 抽出方針の決定

### 方針 A: 構造のみ抽出

具体例の構造（section / フィールド / 順序）を template に残し、中身は `<!-- example -->` ヒント注釈に。

**例**: renji の `bible/style_guide.md` から `templates/bible/style_guide.template.md` を抽出（POV 運用 / 文体 / 禁則 / センシティブ の section 構造のみ）

### 方針 B: パターン + 適用例

template + 別ファイルで「適用例」を残す。

**例**: `checklists/work_dramatic_principles.template.md` + 適用例として「renji の 7 ルール例」を末尾に注釈

### 方針 C: rule に昇格

繰り返し出てくる原則 / 禁則は `rules/` に昇格。`.claude/rules/` 追加候補。

**例**: 「raw を直接 bible に流さない」は `rules/intake-flow.md` に。

### 方針 D: docs に概念追加

新しい概念（例: 三層構造）が出たら `docs/` に項目追加。

ただし作品固有装置は docs 化しない。汎用概念のみ。

---

## Step 3. 抽出実行

選んだ方針に従って:

1. Evolution 内の該当ディレクトリにファイル新設 or 既存ファイル追記
2. 構造を抽象化（具体例から固有名詞 / 個別事実を除去）
3. ヒント注釈（`<!-- ... -->`）で「ここに何が入るか」を示す
4. 「{出典作品} で観察」を冒頭に明記
5. 関連 Evolution ファイルから参照リンク

---

## Step 4. 検証

抽出した template について:

- [ ] 別作品（架空でよい）で使うことを想像、unstuck か?
- [ ] 作品固有要素が混入していないか?
- [ ] section 構造が overgeneralized でないか?
- [ ] ヒント注釈が適切か（具体的すぎ / 抽象的すぎ）?
- [ ] 既存 template と重複していないか?

---

## Step 5. 出典作品への反映（任意）

抽出した template を出典作品でも使うなら:

- 出典作品の `CLAUDE.md` or `.adapter/` に「Evolution の {新ファイル} を参照」追記

---

## Step 6. learning に記録

`StoryTemplateEvolution/learning/{date}-extracted-{pattern-name}.md` に:

- 出典 / 観察対象
- 抽出したパターン（要約）
- 抽出方針（A/B/C/D）
- 抽出結果 / 配置先
- 検証結果
- 残置した要素（作品固有のもの）
- 次に観察すべきこと

---

## 失敗パターン

1. **作品固有装置を template 化** — renji の三層 / レンジ語 / 正当化圏 / 壁時計の一拍 等は禁止
2. **抽象化のために抽象化** — 「他作品で本当に使うか?」を毎回問う
3. **template に renji の固有名詞が残る** — 抽出の最後に必ず固有名詞 grep
4. **既存 template と重複作成** — 抽出前に必ず既存 template を確認
5. **ヒント注釈が短すぎる** — 「ここを埋める」だけでなく「何を / どう / 例」を書く
6. **出典明示を忘れる** — 出典なしの template は trace 不能

---

## 抽出例（参考）

### Good 例: renji の作劇ルール 7 項目 → `checklists/work_dramatic_principles.template.md`

- renji の「主人公を賢くしない」は固有
- しかし「作品ごとに 5〜10 件の作劇ルールを最高優先で置く」という構造は汎用
- 構造を抽出、個別ルールは作品ごとに

### Bad 例: renji の三層構造を `templates/bible/world/three_layer.template.md` として抽出

- 三層構造そのものが renji 固有
- 「N 層対応構造」と汎用化しても overgeneralized で誰も使わない
- 抽出しないのが正解。renji の固有装置として残置

---

## 成果物

- 抽出された template / rule / docs（数件）
- learning ログ 1 件
- 出典作品への参照追加（任意）
