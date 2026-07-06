# Late-day Reorg + Prompts 追加

> **種別**: 方法論 / インシデント
> **日付**: 2026-04-29（同日後半）
> **関連**: 前回 retro `2026-04-29-renji-pilot-retro.md`

---

## 何が変わったか

### 1. 作品の再配置

**Before**:
- `story-template for TAKT/works/renji/` （renji の bootstrap 物）
- `story-template for TAKT/renji_novel_bible/` （raw 35 files）
- `story-template for TAKT/.claude/rules/` （継承元 5 ルール）

**After**:
- `works/fools-with-cheating/` 配下に集約（自己完結）
  - `bible/`, `design/`, `state/`, `writing/`, `inbox/`, `synthesis/`, `learning/`, `drafts/`, `reviews/`, `.adapter/` （renji からコピー）
  - `.claude/rules/` 5 本（コピー）
  - `CLAUDE.md` （fools-with-cheating 固有版に書き直し）
  - `README.md` （新設、ナビゲーション）
  - `raw/` 36 files（旧 renji_novel_bible）

合計 104 ファイル / 自己完結状態。

### 2. パス参照の書き換え

- `renji_novel_bible/` → `raw/`
- `works/renji/` → `./`
- `story-template for TAKT/works/renji/` → `./`
- `story-template for TAKT/renji_novel_bible/` → `raw/`

29 ファイル更新（grep 確認、残置参照ゼロ）。

### 3. StoryTemplateEvolution に prompts/ 追加

`StoryTemplateEvolution/prompts/` 新設、6 ファイル:

- `README.md` — prompts の使い方
- `00_session_start.md` — 任意セッションの入口
- `01_improve_from_new_work.md` — 既存作品から学びを抽出
- `02_audit_gaps.md` — Evolution の不足点検
- `03_extract_pattern.md` — パターンを template に抽象化
- `04_apply_to_new_work.md` — 新規作品で Evolution を使う
- `05_consistency_check.md` — Evolution 内の整合チェック

これにより Evolution の改善作業が **任意セッション / 任意エージェント** で続けられる（ゼロベースで）。

---

## 残作業（cleanup 推奨）

`story-template for TAKT/` 配下の以下は **削除候補**（fools-with-cheating にコピー済 / 自己完結化済）:

- `story-template for TAKT/works/renji/` → 削除候補
- `story-template for TAKT/renji_novel_bible/` → 削除候補（raw として fools-with-cheating/raw/ にコピー済）

ただし `story-template for TAKT/proposals/` は履歴として温存推奨（v2-fat / handoff / v3-kernel 三提案の足跡）。

`story-template for TAKT/CLAUDE.md` と `story-template for TAKT/.claude/rules/` は v1 として温存（他作品の参照元になっている可能性）。

---

## 削除する場合のコマンド（author 確認後）

```bash
cd write_read_novel_manufacture
# 確認:
ls "story-template for TAKT/works/renji/"   # 中身確認
ls "story-template for TAKT/renji_novel_bible/"  # 中身確認

# fools-with-cheating で再現できているか確認:
ls "works/fools-with-cheating/bible/"
ls "works/fools-with-cheating/raw/"

# 問題なければ:
rm -rf "story-template for TAKT/works/renji"
rm -rf "story-template for TAKT/renji_novel_bible"
```

---

## なぜ再配置したか

ユーザー（author）の意図:

1. **renji を書くのに必要なものを 1 箇所に集約** — works/fools-with-cheating/ が「執筆プロジェクト」として完結
2. **StoryTemplateEvolution は独立して改善し続ける** — 作品の運用と template 改善を分離
3. **Codex / Claude が新セッションでもすぐ着手できる** — fools-with-cheating の README + CLAUDE.md で executable, Evolution の prompts/ で improvable

---

## 次セッションの開始方法

### 「ep001 を書きたい」セッション

入口: `works/fools-with-cheating/README.md` + `CLAUDE.md`

そのまま `writing/episode_packs/ep001/` を読んで draft 作業へ。Evolution は不要。

### 「Evolution を改善したい」セッション

入口: `StoryTemplateEvolution/prompts/00_session_start.md`

そこから A/B/C/D/E のオプションを選ぶ。

### 「両方触りたい」セッション

両方の入口を順に読む。fools-with-cheating での発見を Evolution に持ち上げる場合は `prompts/01_improve_from_new_work.md` を使う。

---

## 学び

### 1. 作品 directory は自己完結すべき

renji が `story-template for TAKT/works/renji/` にあったとき、参照が `renji_novel_bible/` `.claude/rules/`（template 配下）等に散乱していて、可搬性が低かった。

**works/{slug}/ は外部参照ゼロで動作可能** な状態に保つべき。raw 素材も内部に持つ（コピーで OK）。

### 2. template 改善と作品運用を分離する

Evolution の改善 vs 作品の執筆は、本来別の関心軸。同じ session で両方やると混乱する（午前の v3-kernel 議論で経験済）。

prompts/ の各 prompt が「これは template 改善 / これは作品運用」を明示することで、混在を防ぐ。

### 3. プロンプトを書くのは prompt engineering の典型

「作業の入口」を prompt として固定化することで、毎回「何から始めるか」を考える時間が消える。Codex に渡す前に prompt を整備する価値が高い。

---

## 横展開チェック

同じ「自己完結化」が必要な対象:

- `works/villainess-coc-survival-with-cheating/`、`one-man-statefall/`、`sample-story/` 等の既存作品も同様に整理すべきか? → 別セッションで author 判断
- `evaluate-lab-v0/`、`know_how_explore/`、`evaluation-revolution-lab/` 等の他リポジトリ → 同上
