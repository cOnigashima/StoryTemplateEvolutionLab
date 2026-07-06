# Proposal: 2026-07-06 workbench — オントロジー基盤 × ループ × コア/オーバーレイ

status: **proposed（current 置換の提案）**
狙い: StoryTemplateEvolution の `current/` を、この提案の内容で**置き換える**。

同梱資料:
- `00_現状把握マップ.md` … 5プロジェクトの解剖（背景）
- `01_オントロジー適用の見立て.md` … オントロジー適用の調査＋設計

---

## 0. 一行

fools（TAKT自動化）と villainess（Cowork人間判断）に分岐していた正本を、**コア＋オーバーレイ**で一本化し、**オントロジー対応の state** を共通データ基盤に据え、**人間は成果物だけ見る**ループ運用へ寄せた新 current。

---

## 1. なぜ置き換えるのか（現行 current の課題）

現状把握（00）で見えたギャップ:

1. **正本が2系統に分岐** — fools=episode_pack、villainess=packet2段freeze。構造が違い、片方に寄せると片方の良さを失う。
2. **評価基準が未接続** — know_how の25項目ルーブリックや evaluation-lab の候補が、実レビュー工程に自動で刺さっていない。
3. **進化ループが手動** — 「実走→抽象化→昇格」が人手待ちで回っていない。
4. **作業場所・ルールが分散** — どこで書き、何を正本とするかが5プロジェクトに散っている。

---

## 2. 提案の要点（4つ）

### (1) コア＋オーバーレイで一本化
- **core**（全作品必須）: kernel11 / bible・design・state / レビューパイプライン / DoR-DoD / rules / 逆方向フロー。
- **overlay**（作品選択）: `unit-episode-pack`（fools流）/ `unit-packet-2stage`（villainess流）。
- 各作品は `work.manifest.json` で overlay と **core からの逸脱（理由付き）** を宣言。暗黙の逸脱を禁止。
- → 「共通の恩恵」と「作品ごとの自由」を両立し、分岐を解消。

### (2) オントロジーを共通データ基盤に
- `state/` をプロパティグラフ化（entities / knowledge_state / foreshadowing / timeline）。既存の character_states.yaml 等を formalize しただけで重い標準(OWL/RDF)は入れない。
- `tools/ontology_check.py` で参照整合性・epistemic矛盾・未回収伏線・タイムライン循環を検出（非gating warning）。
- → 「世界設定の構造化 / 整合性の自動チェック / AIへの文脈供給(k-hop)」を1基盤で提供。詳細は 01。

### (3) 評価基準の実装接続
- `rules/review-gate.md` に 25項目ルーブリック＋破綻ゲート＋evaluation-lab候補（shadow）を集約し、レビュー工程が必ず参照する。

### (4) 人間は成果物だけ見る（ループ運用）
- 人間ゲートは G-Intake / G-Deliverable / G-Publish の3つだけ。途中は自動（validator＋レビュー＋loop_monitor）。
- ループ実装は TAKT を想定するが **暫定**（別セッションで確定）。

---

## 3. 置換の対応（旧 current → 新 current）

| 旧 StoryTemplateEvolution/current | 新 current | 備考 |
|---|---|---|
| templates/ docs/ adapter/ | template/（core+overlay+runtime）, adapter/ | 再編・中身入り |
| agents/ skills/ | takt/facets/personas/ ＋ workflow | TAKTベースへ（暫定） |
| rules/ checklists/ | template/core/rules, template/core/checklists | 再整備 |
| （なし） | template/core/schema, template/core/state, tools/ontology_check.py | 新規（オントロジー） |
| WORKFLOW.md | WORKFLOW.md | 更新 |

---

## 4. 未確定・次アクション

- **TAKT**: workflow/facet は叩き台。別セッションで確定。確定まで参考実装。
- **実証**: ダミー作品1本か、既存 villainess/fools を1本この構造へ移行してループを実走。
- **StoryTemplateEvolutionLab へ**: 本 current をラボの current に据え、本 proposal を proposal 履歴に1エントリとして追加。
- **evaluation-lab との配線**: 追加criterion を shadow から本採用へ昇格する条件を詰める。

---

## 5. 設計原則の継承（STE v4 から）
kernelは薄く / bible・design・state 分離 / raw直投入禁止 / Writing Adapterで1単位圧縮 / status明示 / templateは実走から生む / 作品固有はgeneric化しない。本提案もこれらを維持する。
