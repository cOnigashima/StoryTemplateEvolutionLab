# レビュー体系

本ファイルは **テーマ 3 前半「レビュー体系」** の設計。works/villainess-coc の reviewer-gate-b / monitoring-dictionary / multi-pass self-review、know_how_explore の 25 項目 rubric / PART A-C プロンプト、既存 typed-review-template / bridge-review-template / seed-to-macro-template を、template 正典として再編する。

---

## 1. Review Matrix（5 種 × 目的 × タイミング × 入力 × 出力）

| Review 種別 | 目的 | タイミング | 主入力 | 主出力 | 本籍 template |
|---|---|---|---|---|---|
| **Typed Review** | 章/draft 単位の構造診断 | draft 完了→approval 前 | draft 本文 + packet + bible | typed-review-*.md（Part A/B/C + Issue Routing + Upstream Returns） | `reviews/typed-review-template.md` |
| **Bridge Review** | packet 切替時の入口/出口整合 | packet N → packet N+1 間 | packet N 最終 ep + packet N+1 先頭 ep | bridge-review-*.md | `reviews/bridge-review-template.md` |
| **Continuity Review** | 横断での連続性検査 | 定期 / packet 完了時 | 全 draft + foreshadowing-map + canon | continuity-review-*.md | `reviews/continuity-review-template.md`（新設） |
| **Persona Review** | 3 persona 視点での読者体験検査 | approval 前 | draft + meta | persona-review-{A,B,C}-*.md | `reviews/persona-review-template.md`（新設） |
| **Approval Review** | 公開可否判定 | 公開直前 | 上記 review 結果一式 + kakuyomu-policy | approval-*.md | `reviews/approval-template.md`（新設） |
| **Seed-to-Macro Review** | seed 昇格判定 | seed 起票後 | seed + macro 該当箇所 | seed-to-macro-*.md | `reviews/seed-to-macro-template.md`（既存） |
| **Packet Freeze Review** | packet を frozen に落とす前検査 | packets/scoped → frozen | packet yaml + 依存 bible/arcs | freeze-review-*.md | `reviews/packet-freeze-template.md`（新設） |

---

## 2. Typed Review（骨格）

既存 `reviews/typed-review-template.md` は良好だが、以下を拡張する:

### 2.1 セクション構成（v2）

```
PART A: Hard Gate
  - A-1: 因果・時間整合（hard gate、weight 7）
  - A-2: 話者識別（hard gate、weight 3）
  - A-3: 文法・自然さ（hard gate、weight 4）
  - A-4: 約束不侵犯（hard gate、weight 5）

PART B: Packet Fulfillment Audit（Gate B）
  - E-1: packet 要件の実装状況（✅/⚠️/❌）
  - E-2: withhold 検査（grep 必須ルール）
  - E-3: 差し戻し判定
  - E-4: 卓接続ビート分布検査（packet 横断、generic化: 「接続ビート」= 前 packet/arc との結節点）

PART C: Shared Craft Diagnosis（craft library 観点）
  - C-1: Scene/Sequel 判定（目的→対立→災→反応→ジレンマ→決定の骨格）
  - C-2: Want/Need 駆動（表層動機と深層動機の両立）
  - C-3: Cadence / Rhythm（緊張弛緩比率）
  - C-4: Foreshadow 仕込み・回収（foreshadowing-map との整合）
  - C-5: Motif 単調性（反復 motif の段階・回数・意味論）
  - C-6: POV / Focal character 規律（知識状態単調性）

PART D: Prose & Scene Diagnosis
  - D-1: 文体（文の長短・密度・語彙）
  - D-2: 対話（話者識別・方言・情報密度）
  - D-3: 描写（五感配分・物的証拠の触覚時間 5 行ルール）
  - D-4: 合理化語彙 tell 検知（「つまり」「なるほど」「思えば」）

PART E: Issue Routing
  - prose 問題 → scenes/ or drafts/
  - hook/pacing → packets/
  - 動機/関係性 → bible/characters.md
  - 開示順/反転 → arcs/
  - 約束ズレ → story/promises.md
  - 長生きする構造問題 → design-debt.yaml
  - 未確定設定 → canon-patch-proposals/

PART F: Upstream Returns
  - issue level / return target / recommended next job / expected delta

PART G: 25 項目 rubric 採点（know_how_explore 移植）
  - ハードゲート 3 項目 (weight 7/3/4)
  - 文体 6 項目 / 対話 4 項目 / 構成 6 項目 / 伏線 3 項目 / キャラ 2 項目 / 世界観 2 項目
  - 総合点 80+/60-79/≤59 で公開可否推奨
```

### 2.2 Gate B PART E の generic 化

works/villainess-coc の reviewer-gate-b.md は作品固有（卓・神格・motif）表現だが、以下を generic 化して template に移植する:

| villainess-coc 固有 | generic 名 |
|---|---|
| 卓 | packet / arc boundary |
| 神格 | antagonist mystery / central conceit |
| 主系列キーワード | withhold main keyword set |
| 従属チェック | carryover keyword set from previous boundary |
| 紅茶5段・嗜好ズレ・鐘3回・ですわぁ3段 | （作品固有 motif）template の generic motif operation manual に置き換え |
| 卓接続ビート分布検査 | boundary connection beat distribution audit（packet 横断） |
| 辞書漏れ防止プロトコル | monitoring dictionary sync protocol |

generic化したルールは `.claude/rules/review-system.md` + `craft/motif-operations.md` に入れる。

### 2.3 grep 必須ルール（template 正典化）

villainess-coc §8.1 を template 正典に昇格:

```
typed review で「該当なし」判定を書く場合、必ず draft 本文への grep 結果を併記する。
- 記憶ベースの判定禁止
- meta / scene card ベースの判定禁止
- grep キーワードは作品固有 monitoring-dictionary または craft/motif-operations.md から採用
- grep の hit count と対象行番号を review に記録
```

これを `.claude/rules/review-system.md` §grep-verification に入れる。

---

## 3. Persona Review（3 persona 設計）

### 3.1 3 persona の定義

| persona | 読み方 | 重視する観点 | 離脱トリガ |
|---|---|---|---|
| **Persona A — 没入型（immersive）** | 感情・体感優先で読む | 情緒のリアリティ、身体感、関係温度 | 感情が置いてけぼり、説明過多、主人公の動機不透明 |
| **Persona B — 構造型（structural）** | 伏線・整合・論理で読む | 因果整合、伏線回収、設定の一貫性、フェア開示 | 論理破綻、後出し設定、反則開示 |
| **Persona C — 離脱型（churn/dropout）** | 興味が続かなければ即離脱 | テンポ、掴み、次を読みたくなる hook | 冗長、無 hook、キャラが好きになれない |

### 3.2 各 persona の review prompt 骨格

新設 `prompts/review/persona-{A,B,C}.md`:

**Persona A prompt**:
```
あなたは没入型読者。本 draft を読み、以下を答える。
1. 感情が動いた箇所（該当 beat）
2. 感情が置いてけぼりだった箇所（該当 beat）
3. 身体感・五感・関係温度が効いている場所
4. ここで主人公が何を感じているか不明だった箇所
5. 続きを読みたいか（yes/no + 理由 1 行）
```

**Persona B prompt**:
```
あなたは構造型読者。本 draft を読み、以下を答える。
1. 伏線として拾ったもの（= 今後の回収を期待した箇所）
2. 既に回収されたと認識した箇所
3. 論理破綻・後出し設定の疑いがある箇所（証拠として該当行）
4. 既 canon（提示された bible/arcs）との整合性で引っかかった箇所
5. 開示のフェアさ（読者が手がかりから推理できる状態か）
```

**Persona C prompt**:
```
あなたは離脱型読者。本 draft を読み、以下を答える。
1. 読み始めて最初に離脱しかけた箇所（もしあれば）
2. 次を読みたくなる hook（cliffhanger / turn / reveal）
3. キャラクターに好意を持てたか
4. テンポが遅いと感じた箇所（冗長・説明過多）
5. 他の作品に切り替えたくなる瞬間
```

### 3.3 持ち込み・出力

- persona 3 名分の review を揃える（=`reviews/persona-review-{A,B,C}-*.md` × 3 本）
- 各 persona review の結論を typed review の **PART F Upstream Returns** に合流
- 起源: `works/villainess-coc-survival-with-cheating/learning/2026-04-18-persona-*-review-packet-002.md`

---

## 4. Continuity Review（新設）

### 4.1 目的

packet 内の drafter-preflight Gate 0（直前 ep 散文照合）や Multi-Pass Self-Review Pass 4（3 話以上横断）では拾えない、**長尺の連続性**を検査する。

典型的検出対象:
- 何 packet も前に設置した伏線が消えていないか
- キャラの声（口調・語尾）が長期で崩れていないか
- 物証・関係温度・名前 motif の経時変化の単調性
- 登場人物の知識状態の通時整合

### 4.2 入力

- 検査対象の全 draft（published + approved）
- `story/foreshadowing-map.md`
- `bible/characters.md`（声・関係）
- 作品固有 `.claude/rules/monitoring-dictionary.md`（motif 辞書）

### 4.3 出力フォーマット（`reviews/continuity-review-template.md`、新設）

```markdown
# Continuity Review — range: {ep-XX to ep-YY}

> 検査範囲: arc-01 packet-003 ep15 〜 packet-005 ep28
> 日付: YYYY-MM-DD
> reviewer: {agent / human}

## PART 1: 伏線経時台帳
| 伏線 id | 設置 ep | 期待回収 ep | 現在状態 | 備考 |

## PART 2: キャラ声経時台帳
| キャラ | 語尾/口調 motif | 初出 ep | 最近の ep | 単調性 | 備考 |

## PART 3: 物証経時台帳
| 物証 | 初出 ep | 直近参照 ep | 状態変化 | 備考 |

## PART 4: 知識状態通時台帳（focal 別）
（focal character 毎に、各 ep 終了時点の既知リスト）

## PART 5: motif 反復経時台帳
| motif | 段階進行 | 出現 ep | 単調性 | 備考 |

## PART 6: 検出された不整合
| # | 種別 | 該当 ep / beat | 内容 | 深刻度 | 差し戻し先 |

## PART 7: Upstream Returns
- issue level / return target / recommended next job / expected delta
```

---

## 5. Approval Review（新設）

### 5.1 目的

公開前の最終チェック。kakuyomu-policy 遵守含む。

### 5.2 チェック項目

```markdown
# Approval Review — ep-NN

## 1. 上流 review 結果
- [ ] Typed Review OK
- [ ] Persona Review (A/B/C) 全員合格
- [ ] Continuity Review 必要なら実施済み
- [ ] Bridge Review（packet 切替時のみ）実施済み

## 2. 25 項目 rubric
- [ ] 総合点 80+ / 60-79（条件付き公開）/ ≤59（公開不可）
- [ ] ハードゲート 3 項目全合格

## 3. kakuyomu-policy 遵守
- [ ] AI 利用タグ（AI本文利用）設定
- [ ] 投稿頻度（1 日 3 話 / 週 15 話 / 最小 4h 間隔）内
- [ ] 禁止コンテンツ該当なし（暴力・性的・著作権・差別）
- [ ] コンテスト条件適合（応募時のみ）

## 4. 最終散文チェック
- [ ] 誤字脱字スキャン済
- [ ] タイトル / あらすじ確定
- [ ] タグ設定確定

## 5. 差し戻し or 承認
- 判定: approve / hold / reject
- hold/reject 理由:
- 次アクション:
```

---

## 6. Packet Freeze Review（新設）

### 6.1 目的

packet を `scoped → frozen` に落とす前に、以下が揃っているかを検査する。既存 `prompts/packet-freeze-check.md` を review 化。

### 6.2 チェック項目

```markdown
# Packet Freeze Review — packet-NNN

## 1. 必須セクション存在
- [ ] purpose
- [ ] entry_state / exit_state
- [ ] stakes / pressure
- [ ] episode_roles（ep01..epNN 全話）
- [ ] end_hooks
- [ ] disclose / withhold
- [ ] guardrails
- [ ] focus / dependencies
- [ ] episodes[] 各話の role / purpose / desire / obstacle / loss / gain / emotion_curve / reveal / hooks / cliffhanger

## 2. 依存解決
- [ ] story/promises.md §該当項目と矛盾なし
- [ ] bible/world / characters / rules と矛盾なし
- [ ] arcs/arc-NN と矛盾なし
- [ ] 前 packet との bridge-review 実施済み（packet-001 は除く）

## 3. 作品固有チェック（該当作品のみ）
- [ ] 作品固有 motif の ep 割り当て密度マップ（villainess-coc §5 相当）が入っている
- [ ] withhold 辞書（monitoring-dictionary）が現行 packet に追従している

## 4. preflight 前準備
- [ ] 各 ep の task-context.yaml 雛形が生成可能な情報量
- [ ] 各 ep の scene card が slotted に揃った（or 同時着手の scope 宣言）

## 5. freeze 承認
- 判定: freeze / return-to-scoped
- 次アクション:
```

---

## 7. 25 項目 Rubric（know_how_explore 移植）

### 7.1 構成（重み付き・ハードゲート付き）

`craft/rubric.md`（新設）に、know_how_explore `AI小説評価基準設計.md` から 25 項目を移植する。

**項目と重み**:

| # | カテゴリ | 項目 | weight | 判定尺度 |
|---|---|---|---|---|
| G1 | Gate | 因果・時間整合 | 7 (hard) | 0 破綻 / 2 軽度 / 3 ほぼ OK / 4 完璧 |
| G2 | Gate | 話者識別 | 3 (hard) | 同上 |
| G3 | Gate | 文法・自然さ | 4 (hard) | 同上 |
| M1 | 文体 | 文の長短のリズム | 5 | 0-4 |
| M2 | 文体 | 語彙の適合 | 5 | 0-4 |
| M3 | 文体 | POV/Focal 規律 | 5 | 0-4 |
| M4 | 文体 | 描写密度（五感配分） | 5 | 0-4 |
| M5 | 文体 | 地の文の温度 | 5 | 0-4 |
| M6 | 文体 | 合理化語彙の抑制 | 4 | 0-4 |
| D1 | 対話 | 話者識別 (話題の別の側面) | 4 | 0-4 |
| D2 | 対話 | 情報密度 | 4 | 0-4 |
| D3 | 対話 | 方言・立場・関係の表現 | 4 | 0-4 |
| D4 | 対話 | モノローグの抑制 | 4 | 0-4 |
| S1 | 構成 | Scene/Sequel 骨格 | 6 | 0-4 |
| S2 | 構成 | Turn / Reveal の効果 | 6 | 0-4 |
| S3 | 構成 | Cliffhanger の引き | 5 | 0-4 |
| S4 | 構成 | Pacing / Cadence | 5 | 0-4 |
| S5 | 構成 | Promise 遵守 | 6 | 0-4 |
| S6 | 構成 | Packet 要件充足 | 6 | 0-4 |
| F1 | 伏線 | 仕込みの適切さ | 5 | 0-4 |
| F2 | 伏線 | 回収のフェアさ | 5 | 0-4 |
| F3 | 伏線 | Foreshadowing map 整合 | 4 | 0-4 |
| C1 | キャラ | Want/Need の駆動 | 5 | 0-4 |
| C2 | キャラ | 関係温度の変化 | 5 | 0-4 |
| W1 | 世界観 | ルール一貫性 | 5 | 0-4 |
| W2 | 世界観 | 固有名詞の品位 | 4 | 0-4 |

**合計**: 重み総和 = 一度計算して正規化。判定線: 80+ / 60-79 / ≤59。

**ハードゲート**: G1/G2/G3 のどれかで 0 または 1 が付いたら、他が満点でも **公開不可**。

### 7.2 rubric の運用

- typed review の PART G で採点
- approval review の判定基準として参照
- 作品ごとに重み調整可（`bible/rubric-override.md`）

---

## 8. レビュー用 PART A/B/C プロンプト（know_how_explore 移植）

`prompts/review/` に以下を移植:

### 8.1 `prompts/review/part-a-per-scene.md`（章・シーン徹底レビュー）

know_how_explore `小説レビュープロンプト.md` PART A を移植。30 項目チェック:
- GATE CHECK G1-G3（因果/話者/文法）
- 文体 M1-M6
- 対話 D1-D4
- 構成 S1-S6
- 伏線 F1-F3
- キャラ C1-C2
- 世界観 W1-W2

### 8.2 `prompts/review/part-b-dialogue-deep.md`（対話特化）

TD1-TD4 を移植:
- TD1: 話者識別精度
- TD2: 情報密度
- TD3: 関係温度の台詞表現
- TD4: モノローグ境界

### 8.3 `prompts/review/part-c-macro-structure.md`（マクロ構造）

ML1-ML5+ を移植:
- ML1: 作品約束との整合
- ML2: Arc 骨格
- ML3: 伏線グラフ
- ML4: Reveal Plan
- ML5: Cadence

---

## 9. Review Agents（既存 + 新設）

既存 agents を Review Matrix に対応させる:

| Review | 担当 agent | skill |
|---|---|---|
| Typed | critic | /critic |
| Bridge | critic + plotter | /critic-bridge（新設 skill） |
| Continuity | continuity-checker | /continuity |
| Persona A/B/C | audience-proxy | /audience-review（新設 skill） |
| Approval | editor + compliance-agent | /release |
| Seed-to-Macro | plotter + critic | /seed-to-macro（新設 skill） |
| Packet Freeze | plotter + critic | /freeze-review（新設 skill） |

---

## 10. Review Runtime（実行順序）

### 10.1 標準フロー（作品 1 ep 分）

```
1. drafter: Gate 0 / A / C + 因果一段落 + 知識状態台帳
2. drafter: draft 本文
3. drafter: Multi-Pass Self-Review (Pass 1-4)
4. critic: typed review (PART A-G)
5. critic: 必要なら bridge review / continuity review
6. audience-proxy: persona A/B/C review
7. editor + compliance: approval review (kakuyomu-policy 含む)
8. 公開 → published/ に移動 + provenance 更新
```

### 10.2 並列化可能箇所

- step 4 / step 6 は並列可
- step 5 は step 4 の結果次第（bridge の必要性は typed review で確定）

### 10.3 差し戻しフロー

- PART F Upstream Returns の `return target` に従って:
  - scenes/ or drafts/ 差し戻し → drafter 再実行
  - packets/ 差し戻し → plotter 再 freeze
  - bible/ 差し戻し → canon-patch-proposal 起票
  - promises/ 差し戻し → author 判断、上位改訂
  - design-debt.yaml → 負債台帳に積む（いずれ着手）

---

## 11. 新規 review template ファイル一覧

本提案で追加:

- `reviews/continuity-review-template.md`
- `reviews/persona-review-template.md`
- `reviews/approval-template.md`
- `reviews/packet-freeze-template.md`

更新:

- `reviews/typed-review-template.md` に PART B（Gate B）と PART G（25 項目 rubric）追加
- `reviews/bridge-review-template.md` に bridge 専用チェック項目を追加
- `reviews/README.md` に Review Matrix 表追加

新規 skill:

- `.claude/skills/critic-bridge.md`
- `.claude/skills/audience-review.md`
- `.claude/skills/freeze-review.md`
- `.claude/skills/seed-to-macro.md`

新規 rule:

- `.claude/rules/review-system.md`（本ファイル要約 + grep-verification + PART B generic 化ルール + vocabulary-lint）

---

## 12. 作品固有 vs template

作品固有で残すもの（template では generic のみ）:
- 作品固有の monitoring-dictionary（卓・神格・motif キーワード辞書）
- 作品固有の反復 motif 定義（紅茶5段 / ですわぁ3段 等）
- 作品固有の rubric 重み上書き

template 正典化するもの:
- grep 必須ルール（判定に grep を要求する構造）
- Gate B 4-block 出力（packet 要件 / withhold / 差し戻し / 境界接続分布）
- multi-pass self-review flow
- 25 項目 rubric（標準重み）
- Persona A/B/C 定義
- foreshadowing map 整合チェック
