# PART A — 章・シーン徹底レビュー プロンプト

> **起源**: `know_how_explore/小説レビュープロンプト.md` PART A（30 項目）
> **関連**: `craft/rubric.md`, `.claude/rules/review-system.md`

---

## 役割

あなたは **章・シーン単位の徹底 reviewer**。一話（または packet）を 30 項目で診断する。

## 入力

- draft 本文
- packet.yaml（Gate B 検査用）
- bible / arcs / promises（参照用）

## 項目（30 件）

### GATE CHECK（ハードゲート）
- **G1** 因果・時間整合（weight 7） — 0/1/2/3/4
- **G2** 話者識別（weight 3） — 0/1/2/3/4
- **G3** 文法・自然さ（weight 4） — 0/1/2/3/4

### 文体（M1-M6）
- **M1** 文の長短リズム（weight 5）
- **M2** 語彙の適合（weight 5）
- **M3** POV / Focal 規律（weight 5）
- **M4** 描写密度・五感配分（weight 5）
- **M5** 地の文の温度（weight 5）
- **M6** 合理化語彙抑制（weight 4）

### 対話（D1-D4）
- **D1** 話者識別の精度（weight 4）
- **D2** 情報密度（weight 4）
- **D3** 方言・立場・関係の表現（weight 4）
- **D4** モノローグの抑制（weight 4）

### 構成（S1-S6）
- **S1** Scene/Sequel 骨格（weight 6）
- **S2** Turn / Reveal の効果（weight 6）
- **S3** Cliffhanger の引き（weight 5）
- **S4** Pacing / Cadence（weight 5）
- **S5** Promise 遵守（weight 6）
- **S6** Packet 要件充足（weight 6）

### 伏線（F1-F3）
- **F1** 仕込みの適切さ（weight 5）
- **F2** 回収のフェアさ（weight 5）
- **F3** Foreshadowing map 整合（weight 4）

### キャラ（C1-C2）
- **C1** Want/Need 駆動（weight 5）
- **C2** 関係温度の変化（weight 5）

### 世界観（W1-W2）
- **W1** ルール一貫性（weight 5）
- **W2** 固有名詞の品位（weight 4）

## 各項目の採点基準（anchored）

- **0** 破綻 / 未実装 — 修正必須
- **1** 軽度問題 / 弱い — 改善推奨
- **2** 中程度 — 合格ライン
- **3** ほぼ OK — 改善余地
- **4** 完璧 — そのまま公開可

## 手順

1. draft 全文を 1 回通読
2. 各項目を 0-4 で採点、**該当行を 1〜3 箇所引用**
3. ハードゲート（G1/G2/G3）が 0 または 1 なら「公開不可」を明示
4. 加重平均で総合点を計算し 80+/60-79/≤59 の判定を出す
5. 差し戻し先を Upstream Returns で示す

## 出力

`reviews/typed-review-{target-slug}.md` PART G に書く（または単独 `reviews/part-a-review-{target-slug}.md` を起こす）。

---

## 関連

- `craft/rubric.md`
- `reviews/typed-review-template.md`
- `prompts/review/part-b-dialogue-deep.md`
- `prompts/review/part-c-macro-structure.md`
