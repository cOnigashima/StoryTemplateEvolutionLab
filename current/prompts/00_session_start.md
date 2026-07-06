# Session Start Prompt — StoryTemplateEvolution

> 新セッションで Evolution の改善を始めるときに、これをエージェントに貼り付ける。
> ゼロベース（過去セッション知識なし）でも作業に入れる。

---

## あなた（agent）への指示

あなたは小説制作のための **Story Template** を進化させる作業を担当します。

具体的には `write_read_novel_manufacture/StoryTemplateEvolution/` の中身を、実作品（`works/{slug}/`）の運用経験から学んで改善し続けます。

「最強テンプレートを設計室で作る」ではなく、「実作品から蒸留する」方針です。

---

## 最初に読むファイル（順序固定）

```
1. write_read_novel_manufacture/StoryTemplateEvolution/README.md
   → リポジトリ全体の方針

2. write_read_novel_manufacture/StoryTemplateEvolution/proposals/2026-04-29-pilot-driven-evolution/00_README.md
   → 起源・経緯

3. write_read_novel_manufacture/StoryTemplateEvolution/learning/2026-04-29-handoff-to-next-session.md
   → 過去セッションから引き継いだ状態

4. write_read_novel_manufacture/StoryTemplateEvolution/learning/2026-04-29-renji-pilot-retro.md
   → 何を学んだか

5. write_read_novel_manufacture/StoryTemplateEvolution/proposals/2026-04-29-pilot-driven-evolution/04_next_steps.md
   → 次のステップ候補

6. write_read_novel_manufacture/StoryTemplateEvolution/docs/README.md
   → docs ディレクトリの構成
```

これだけで Evolution の現状と方針が掴める。

---

## 現状の把握（quick reference）

**直近の pilot 作品**: `works/fools-with-cheating/`（佐山レンジ長編、ダークファンタジー異世界転生の脱構築）

**Evolution の構成**:
- `docs/` — 用語・kernel 仕様・status・DoR DoD・layer マップ
- `adapter/` — Intake / Writing Adapter 設計（汎用版）
- `templates/` — bible/design/state/writing の雛形
- `checklists/` — 作劇ルール / acceptance / packet freeze 等
- `rules/` — `.claude/rules/` 追加候補
- `work_init/` — 新規作品 bootstrap 手順
- `learning/` — retro と方法論
- `proposals/` — 提案・履歴
- `prompts/` — 本ディレクトリ

**設計原則（最重要）**:
1. Pilot-driven extraction — 設計室で先に作らない、実作から蒸留
2. kernel は薄く（11 項目固定）
3. 作品固有装置（renji の三層対応 等）は template 化しない
4. status を必ず付ける（12 値）
5. raw を直接 bible に流さない

詳細は各 docs を参照。

---

## あなたが選べる作業オプション

セッションのゴールに応じて、以下のいずれかを選ぶ:

### Option A: 既存作品（fools-with-cheating）から学びを抽出

`works/fools-with-cheating/` で発見されたパターン / 不足 / 改善点を Evolution に取り込む。

→ `prompts/01_improve_from_new_work.md` を読んで実行

### Option B: Evolution の不足を点検

何が template に足りないか、何が古くなったかを audit。

→ `prompts/02_audit_gaps.md` を読んで実行

### Option C: 特定パターンを template 化

ある作品 / ある作業で見つかった「これは他作品でも使える」パターンを template に追加。

→ `prompts/03_extract_pattern.md` を読んで実行

### Option D: 新規作品で Evolution を試す

新作品の bootstrap で work_init を使い、その経験から Evolution を改善。

→ `prompts/04_apply_to_new_work.md` を読んで実行

### Option E: ドキュメント整合チェック

Evolution 内のドキュメント間（docs / adapter / templates / checklists 等）の整合を直す。

→ `prompts/05_consistency_check.md` を読んで実行

---

## author に最初に確認すること

セッションを始める前に author に:

1. **今日のゴール** はどれか（A/B/C/D/E or その他）
2. **時間制約** はどのくらいか（1 セッション完結 / 複数セッション）
3. **触ってほしくないファイル** はあるか
4. **author の感覚** — Evolution の現状はどう感じているか（散らかってる / 不足 / 過剰 / 整合がおかしい等）

---

## 成果物として残すべきもの

セッション終了時に必ず:

1. **`learning/{date}-{slug}.md`** — 本セッションで何をしたか / 何を学んだか
2. **更新したファイルのリスト**（learning に含めても可）
3. **次セッションへの引き継ぎ事項**（learning に含めても可）

---

## 失敗パターン（やったら NG）

1. **設計議論に走る** — 「Evolution はこうあるべき」論を先に作らない。実作品の問題を起点に
2. **template を増やすために増やす** — 「他作品でも使うか?」を毎回問う
3. **renji 固有装置を template に持ち上げる** — 三層対応 / 正当化圏 / レンジ語 等は template 化禁止
4. **kernel に項目を増やす** — 11 項目固定。増やしたい場合は overlay / lens / bible に
5. **status 区別を省く** — filled / missing / tentative / 等の区別は必ず付ける
6. **過去セッションの提案 3 Pack を蒸し返す** — v2-fat / handoff / v3-kernel は Evolution に統合済 or archive 候補。再議論しない
7. **作品本文を勝手に変える** — works/ の本文 / bible / design / state は author 承認なしに触らない

---

## セッション中に詰まったら

- `learning/2026-04-29-renji-pilot-retro.md` を読み直す（過去の失敗から学ぶ）
- author に進路を確認する
- 「今やる必要があるか」を問う（やらない選択も常にある）

---

## 完了条件

セッションが「完了した」と言えるのは:

- 選んだ Option の成果物が揃った
- learning に記録した
- Evolution 内のドキュメント整合が崩れていない
- 次セッションが本ファイルから始められる状態
