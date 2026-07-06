# Raw Submission Prompt

ChatGPT Pro 等の外部環境で生成した大量素材を、raw に投入する前のプリセット。

---

## 役割

あなたは author（または author の代行者）。raw 投入前に **文脈情報を揃え** てから `story/intake/raw/` に入れる。

## 手順

raw に入れる前に以下 8 項目を揃える:

1. **source**: どの AI / モデル / 人間ミーティングか
2. **date**: 実施日
3. **duration**: 所要時間
4. **scope**: どの arc / packet / 領域（world / character / plot / motif）が主題か
5. **inputs**: 投げた prompt ファイルへのリンク（prompts/intake/pro-research-brief.md 等）
6. **outputs**: 得た生成結果（**そのまま全文保存、要約しない**）
7. **known_collisions**: 既 canon と衝突しそうな点（気づいた範囲で）
8. **一次印象**: 使えそうな核 / 捨てたい部分

## 保存先

`story/intake/raw/YYYY-MM-DD-{source}-{slug}/` ディレクトリを切り、以下を置く:

- `raw.md` または `raw.txt` — 出力全文
- `brief.md` — 本プロンプトの 8 項目記入済みファイル
- `attachments/` — 画像・pdf 等があれば
- `context.md` — 投入時の会話文脈、スクリーンショット等（あれば）

## 登録

保存後:

1. `story/intake/raw-index.yaml` に 1 entry 追加（8 項目を yaml に）
2. `story/intake/provenance.yaml` に 1 record 追加（origin_type: raw）
3. `story/intake/reflection-ledger.md` の「未反映（pending）」に行を加える（`digest 済み: ❌ / seed 化: ❌` で起票）

## 規則

- **全文保存**。後でからは raw 補完できない
- 8 項目をスキップしない。不明なら `unknown` と明記
- 一次印象は 2〜5 行。判断の縛りにするためではなく、後の digest 作業の助走

## 次段

数時間以内に `prompts/intake/digest-writer.md` を起動して digest 化する。

---

## 関連

- `prompts/intake/pro-research-brief.md`（Pro 投入時の指示書）
- `prompts/intake/digest-writer.md`（次段）
- `.claude/rules/intake-flow.md`
