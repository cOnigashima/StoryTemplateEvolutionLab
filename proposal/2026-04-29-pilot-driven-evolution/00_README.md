# 提案: Pilot-Driven Story Template Evolution

> **日付**: 2026-04-29
> **位置付け**: 旧 Story Template (v1) と提案 3 パック（v2-fat / handoff / v3-kernel）を踏まえ、renji 作品を pilot として実走しながら次世代 template を抽象化する方針。
> **承認**: 本提案は author (taiji) の合意済（本セッション内）。

---

## 本提案の起源

### 課題認識

- 旧 Story Template (v1) は CLAUDE.md と .claude/rules/ 5 本のみで、実体的な雛形が存在しなかった
- 提案 3 パックが残ったが、互いに方向性が異なり、本体に統合されなかった
  - v2-fat: 4+1 Layer + 25 項目 rubric + Craft Library （重装備）
  - handoff: 「最強テンプレ作るな」kernel 薄＋ Adapter / Judge / Ledger（軽装備）
  - v3-kernel: 上記を語彙統合し kernel 11 項目化（中庸）
- 結果として「網羅された Story Template」状態に到達しないまま、設計議論だけが膨らんだ

### 方針転換

設計優先 → 実走優先。renji 作品を pilot として:

1. renji の Bible (35 ファイル / 約 750KB) を Adapter で受け入れて bible/design/state に分割
2. 実体化と並行して、各 renji ファイルから template skeleton を抽出
3. 共通パターン（チェックリスト / ルール / 構造）を docs/ checklists/ rules/ に蒸留
4. 出力は renji の writable な bible + 次の作品で使える template skeleton 集

---

## 本提案の核

### 1. Pilot-driven Template Extraction

```
renji_novel_bible/35 files
        ↓ Adapter で処理
        ├── works/renji/bible|design|state/{file}     ← renji 固有の中身入り
        └── StoryTemplateEvolution/templates/{file}.template   ← 構造だけ汎用化
```

**1 ファイル作るごとに対応する template skeleton も同時生成**。renji を読みながら、共通構造を蒸留する。

### 2. 抽象化の境界

- ✅ 抽象化する: kernel 11 項目 / character sheet 構造 / scene card 構造 / acceptance checklist / DoR DoD / status 区別 / Adapter プロンプト / 作劇ルール template 形式
- ❌ 抽象化しない: 三層対応 / 正当化圏 / レンジ語 / renji 固有の世界設定 / 個別キャラ性格

「他作品で使えそうな構造」と「renji 専用装置」を最初から分離する。

### 3. Adapter を 2 つに分割

旧 v3 / handoff の Adapter を本提案で明確に 2 分:

- **Intake Adapter**: 自由 chat / 大量 raw → bible/design/state 更新案
- **Writing Adapter**: bible/design/state → 1 episode 用 Writing Pack

renji の `.adapter/` で得た知見をこの 2 分割に整合させて adapter/ に汎用化。

---

## 本提案で作るもの

### StoryTemplateEvolution/ 全体

| ディレクトリ | 内容 | 数 |
|---|---|---|
| README.md | 全体方針 | 1 |
| proposals/2026-04-29-pilot-driven-evolution/ | 本提案 + 知見記録 | 5 |
| templates/bible/ | bible 雛形 | 12 |
| templates/design/ | design 雛形 | 4 |
| templates/state/ | state 雛形 | 5 |
| templates/writing/episode_pack/ | writing pack 雛形 | 4 |
| adapter/ | Intake / Writing Adapter 汎用版 | 7 |
| checklists/ | チェックリスト集 | 5-8 |
| rules/ | .claude/rules/ への追加候補 | 2-3 |
| docs/ | 用語・単位・kernel・status・DoR DoD | 6 |
| work_init/ | 新規作品起こし手順 | 2 |
| learning/ | 本セッション retro + handoff | 3 |

### works/renji/ への並行産出

| 内容 | 数 |
|---|---|
| bible/ 実体 | 12 |
| design/ 実体 | 4 |
| state/ 実体 (seed) | 5 |
| writing/episode_packs/ep001/ 更新 | 4 (既存更新) |

---

## 本提案の Definition of Done

- [ ] StoryTemplateEvolution/ の全 directory に最低 1 ファイル
- [ ] templates/ から空 work をコピーすれば新作品を起こせる状態
- [ ] adapter/intake_adapter_prompt を別作品に適用可能な形（renji 固有要素なし）
- [ ] adapter/writing_adapter_prompt を別作品に適用可能な形
- [ ] works/renji/bible が realized され、ep001 Writing Pack が renji_novel_bible 直参照を脱した
- [ ] learning/ に retro と次セッションへの handoff 完備
- [ ] 本 README とこの 00_README が読了で全体把握できる

---

## このフォルダ内の他ファイル

- `01_extraction_method.md` — 「renji 実体 と template を並行生成する」方法論
- `02_what_was_extracted.md` — 抽象化されたもの一覧
- `03_what_stayed_renji_specific.md` — renji 固有として温存したもの一覧
- `04_next_steps.md` — 次セッション以降の進め方

---

## 関係先

- 旧 v1: `../../../story-template for TAKT/` (温存)
- 旧提案 v2-fat: `../../../story-template for TAKT/proposals/2026-04-22-story-template-v2/`
- 旧提案 handoff: `../../../story-template for TAKT/proposals/storytemplate_workflow_handoff_pack/`
- 旧提案 v3-kernel: `../../../story-template for TAKT/proposals/2026-04-29-domain-kernel-v3/`
- renji 実走場: `../../../story-template for TAKT/works/renji/`
- renji raw 元: `../../../story-template for TAKT/renji_novel_bible/`
