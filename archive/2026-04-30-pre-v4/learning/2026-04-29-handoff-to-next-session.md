# 次セッションへの引き継ぎ

> **日付**: 2026-04-29
> **本セッション結果**: StoryTemplateEvolution / の初期構築完了。renji が ep001 を書ける状態。
> **次セッション**: 本ファイルから読み始めること。

---

## 本セッションの成果（全体像）

```
write_read_novel_manufacture/
├── story-template for TAKT/             (温存・参照)
│   ├── proposals/                       (v2-fat / handoff / v3-kernel 三提案)
│   ├── works/renji/
│   │   ├── .adapter/                    (Adapter 7 docs ★ 完成)
│   │   ├── bible/                       (Phase A 実体化 ★)
│   │   │   ├── premise / reader_promise / theme / genre / style_guide
│   │   │   ├── characters/ (protagonist + 編集者)
│   │   │   ├── world/ (three_layer / ability / locations)
│   │   │   ├── plot/ (arc_map / episode_plan / scene_cards) ※ ep001 中心
│   │   │   └── in_world_documents/samples ※ ep001 用 2 件
│   │   ├── design/                      (4 ファイル ★)
│   │   ├── state/                       (5 ファイル seed ★)
│   │   └── writing/episode_packs/ep001/ (4 ファイル ★ realized bible 参照に更新済)
│   └── renji_novel_bible/               (raw 35 files、温存)
│
└── StoryTemplateEvolution/              (★ 新設)
    ├── README.md
    ├── proposals/2026-04-29-pilot-driven-evolution/00_README.md
    ├── docs/                            (6 docs)
    ├── adapter/                         (8 docs 汎用版)
    ├── templates/                       (bible 12 + design 4 + state 4 + writing 4 = 24 templates)
    ├── checklists/                      (3 checklist templates)
    ├── rules/                           (1 intake-flow rule)
    ├── work_init/                       (2 docs: README + bootstrap 手順)
    └── learning/                        (本ファイル含む 3 docs)
```

総ファイル数: 約 70。

---

## 次セッションで Codex / Claude が「すぐ取り掛かる」べきこと

### Option A: ep001 本文を書く（最短ルート）

入力:
- `works/renji/writing/episode_packs/ep001/` の 4 ファイル
- `works/renji/bible/`, `design/`, `state/` の関連ファイル
- 必要なら raw として `renji_novel_bible/`

成果物:
- `works/renji/drafts/episodes/ep001-{slug}.md`

手順:
1. drafter-preflight（`.claude/rules/drafter-preflight.md`）の Gate 0/A/C と基本 3 原則を Writing Pack で埋める
2. 1500〜3000 字目安で prose を書く
3. Multi-Pass Self-Review 4 パスを通す
4. acceptance_checklist.md で must_satisfy / must_not_violate を確認
5. author レビューに渡す

注意事項:
- 老人レンジを賢く / 面白く描かない
- 編集者を未熟・小心者に描かない
- 壁時計の一拍は 1 文のみ、説明禁止
- メタ語（正当化圏 / 認知整合）を本文に出さない
- 異世界要素を ep001 に出さない
- 章末資料 2 件を末尾に置く

---

### Option B: renji bible を Phase B に進める

ep001 だけでなく ep002-012 までを書ける状態にする。

足すべきもの（renji_novel_bible/ から作業）:
- bible/characters/individual/{tomu, mira, saria, バルド, ハインリヒ, ガロス, レオン, アルマ}.md
- bible/world/locations.md（ギルド関連を充実）
- bible/world/lekushia_kingdom.md（renji_novel_bible/17 から）
- bible/plot/episode_plan.md（ep002-012 を詳細化）
- bible/plot/scene_cards.md（C002-C012 を詳細化）
- bible/in_world_documents/samples.md（arc-1 用全件）
- state/three_layer_status.yaml（01-01〜01-13 を seed 投入）
- state/character_states.yaml（若いレンジ・トマ等を初期化）

参照: `works/renji/.adapter/source_mapping.md` の Phase B 計画

---

### Option C: 別の新規作品を起こす（StoryTemplateEvolution の真の検証）

renji は既存資料が完成しすぎている。**別作品を空から起こす** ことで StoryTemplateEvolution の真の検証ができる。

手順: `StoryTemplateEvolution/work_init/new_work_bootstrap.md` を Step 1 から実行。

---

## 散らかっている部分・次セッションで整理すべき事項

### 1. 3 提案パック（v2-fat / handoff / v3-kernel）の扱い

現状: 3 つとも `story-template for TAKT/proposals/` に温存されている。本 v2 (StoryTemplateEvolution) との関係は:

- v3-kernel の docs（vocabulary / unit_taxonomy / kernel_spec / status_vocabulary / dor_dod / layer_facet_map）は **本セッションで本 v2 の docs/ に継承済**
- v2-fat / handoff の Adapter 思想は本 v2 の adapter/ に統合済
- 残った v2-fat / handoff / v3-kernel の Pack 自体は **歴史資産** として温存

次セッション action: 必要なら 3 Pack に `STATUS: archived` notice を付ける。本体は触らない。

### 2. CLAUDE.md / .claude/rules/ の旧版

`story-template for TAKT/CLAUDE.md` と `story-template for TAKT/.claude/rules/` 5 本は v1。本 v2 は本ファイルでも更新していない。

次セッション action: 旧 CLAUDE.md を本 v2 と整合させる or v1 として温存（works/renji/ は現状の v1 ルールで動作）。

### 3. TAKT の採用判断

本セッションでは TAKT に触れていない。Codex 利用中なら `.takt/` は不要。

次セッション action: TAKT 採用方針を確定。Codex で進めるなら .takt/ は作らない。

### 4. renji bible の Phase A 完了度

ep001 を書ける最低限は揃ったが、大きな未転写領域がある:

- bible/characters/individual/ — 編集者 1 名のみ。残り 14+ 名は Phase B
- bible/world/ — three_layer + ability(要約) + locations(arc-1 概略) のみ。lekushia_kingdom / maou_territory は未
- bible/plot/episode_plan.md — ep001 詳細のみ。残り ep002-072 は raw 直参照
- bible/plot/scene_cards.md — C001 のみ。残り C002-C100 は raw 直参照
- bible/plot/three_layer_table.md — **未作成**。renji_novel_bible/14 を直接参照
- bible/in_world_documents/samples.md — ep001 用 2 件のみ
- bible/in_world_documents/placement_table.md — **未作成**。renji_novel_bible/25 を直接参照

次セッション action: Phase B / C 計画に従って順次転写。

### 5. ep001 Writing Pack の整合更新

bible 実体化に合わせて ep001 Writing Pack の references を realized bible に更新済（本セッション末）。ただし scene_card.md / context_pack.md の **本文** は元の renji_novel_bible 参照ベースの内容のまま。整合性は保たれているが、**本文も Phase A bible 参照に書き直す** のが理想。

次セッション action: ep001 Writing Pack の本文を realized bible の引用ベースに refactor。

---

## 重要な決定事項（本セッションで author と合意）

1. **StoryTemplateEvolution として新ディレクトリで進める**（v1 とは物理的分離）
2. **proposals/ も本リポジトリ内に置く**（足跡として）
3. **renji は works/renji のまま**（後で Works/renji に移す前提）
4. **Layer 1 kernel は薄く、Layer 2/3 は太く**（kernel 11 項目を厳守）
5. **Pilot は新規作品で**（renji を pilot として実走）
6. **TAKT は調査のみ、Codex 利用中**
7. **bible 実体化を skip せず、ep001 周辺だけでも実体化**（Phase A）
8. **template skeleton も同時生成**（pilot-driven extraction）
9. **renji 固有装置は template 化しない**（三層対応 / 正当化圏 / レンジ語）

---

## 重要な参照先（次セッション開始時に必ず読むもの）

1. 本ファイル（handoff）
2. `StoryTemplateEvolution/README.md`
3. `StoryTemplateEvolution/learning/2026-04-29-renji-pilot-retro.md`（次セッション着手前）
4. `StoryTemplateEvolution/proposals/2026-04-29-pilot-driven-evolution/04_next_steps.md`
5. 必要なら `works/renji/.adapter/source_mapping.md`

---

## 質問・未決リスト（author に確認したい事項）

- AD-ep001-01〜05（ep001 の細部判断、`works/renji/writing/episode_packs/ep001/episode_brief.md` §human_decisions_needed）
- TAKT 採用 vs Codex 一本化
- 旧 CLAUDE.md / .claude/rules/ の本 v2 整合タイミング
- 3 提案パックの archived 化判断
- renji bible Phase B 着手タイミング
- ep001 本文を Claude が書くか / Codex が書くか / 人間が書くか

---

## 重要: このセッションで起きたこと

- 朝〜午前: 設計議論先行で散らかる（v2-fat / handoff / v3-kernel の三層）
- 午後: renji_novel_bible との出会い → 方針転換（pilot-driven）
- 夕方: StoryTemplateEvolution 構築 + renji Phase A 実体化 + ep001 Writing Pack 更新

学び: **設計優先より実走優先**。実走から template が育つ。
