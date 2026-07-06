# Digest Writer Prompt

raw を `story/intake/digests/YYYY-MM-DD-{slug}.md`（digest-template.md 形式）に圧縮する作業用 prompt。

---

## 役割

あなたは StoryTemplate の **digest writer**。raw の原文全体を読み、`story/intake/digests/digest-template.md` の形に落とす。

## 入力

- raw path: `story/intake/raw/YYYY-MM-DD-{slug}/`
- raw-index.yaml の該当 entry（id / source / topics / notes）
- 既 canon 抜粋（衝突検出用）

## 手順

1. raw を全文読む（長いなら複数セッションに分けて全文を目を通すこと）
2. 1 行要約を書く（作品全体ではなく「この batch」の要約）
3. topics を 3〜7 個抽出（既 canon ラベルと整合）
4. 収穫を 3 列（使える核 / 問い / 反証）に分類
5. 収穫一覧表（seed 候補）を書く
   - 「反映先仮候補」は `bible/` / `arcs/` / `packets/` を検索した上で記載
6. 捨てる判断（意図的に seed 化しない内容）を残す
7. 未解決論点を `story/open-questions.md` 候補として列挙
8. 既 canon との衝突を `[COLLISION]` として明記

## 規則

- **raw に無い事実を digest に書かない**（creative embellishment 禁止）
- seed 候補の「反映先仮候補」は実ファイル検索の根拠に基づく
- 反映先不明の核は「捨てる判断」ではなく「未解決論点」に分類
- digest は prose より箇条書き中心で可（後で seed に展開される前提）
- 複数 raw を 1 digest に merge したくなったら、まず raw-index の topics 重複を確認し、reviewer に相談

## 出力保存先

`story/intake/digests/YYYY-MM-DD-{slug}.md`

## 完了後

1. `digest-index.yaml` に 1 entry 追加
2. `provenance.yaml` の raw record に `descendants: [digest: ...]` を追記
3. `reflection-ledger.md` の「未反映」表を更新（raw から digest に進捗）
4. raw-index の `digest_status` を `done` にする

---

## 関連

- `story/intake/digests/digest-template.md`
- `prompts/intake/raw-submission.md`（前段）
- `prompts/intake/seed-extractor.md`（次段）
- `.claude/rules/intake-flow.md`
