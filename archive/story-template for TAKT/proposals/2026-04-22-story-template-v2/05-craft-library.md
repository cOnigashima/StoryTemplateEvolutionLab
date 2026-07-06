# Craft Library

本ファイルは **テーマ 3 後半「創作ノウハウ」** の設計。know_how_explore の craft / rubric / prompt 資産を `craft/` ディレクトリ下に再編し、template 正典として常駐させる。

---

## 1. Craft Library の位置づけ

- template の **Layer 3（知識基盤）**。作品に固有ではなく、**作品を書く drafter/critic/plotter が参照する一般知識**を置く
- `bible/` が「作品固有の約束」なら、`craft/` は「物語一般の原理」
- `.claude/rules/` は「守る規範」、`craft/` は「使う道具箱」
- agent や skill は必要に応じて `craft/*.md` を読み、該当原理を適用する

---

## 2. `craft/` ディレクトリ構成

```
craft/
├── README.md                  ← 道具箱の目次と使い方
├── principles.md              ← 面白い物語の 10 原則（抜粋）
├── scene-sequel.md            ← Goal-Conflict-Disaster / Reaction-Dilemma-Decision
├── want-need.md               ← 表層/深層動機、Want vs Need
├── scope-management.md        ← 登場人物数 / 視点数 / 時間軸 / ルール例外数
├── beat-sheets.md             ← Save the Cat / 三幕 / 起承転結 / Vonnegut 感情曲線
├── foreshadowing.md           ← 仕込み・回収・フェア開示・fair play
├── motif-operations.md        ← 反復モチーフの設計と grep 運用（generic）
├── rubric.md                  ← 25 項目評価基準（本パック §04 §7）
├── reader-personas.md         ← Persona A/B/C（本パック §04 §3）
├── cadence.md                 ← 緊張弛緩比率・章/話/ビート間のリズム
├── dialogue-craft.md          ← 対話の原理（情報密度・話者識別・方言・関係温度）
├── description-craft.md       ← 描写の原理（五感配分・物的触覚 5 行ルール）
├── pov-craft.md               ← POV / focal character / 知識状態単調性
├── reveal-plan.md             ← 開示計画の立て方（fabula vs syuzhet）
├── conflict-design.md         ← 対立の型（内的/対人/対社会/対運命）
├── character-design.md        ← Want/Need / 三軸 / 声
├── world-design.md            ← 世界の 3 条件（一貫・制約・驚き）
├── theme-design.md            ← テーマを物語で証明する方法
├── genre-patterns.md          ← ジャンル別の人気パターン
├── editing-craft.md           ← 推敲の手順（多層推敲）
├── sanderson-laws.md          ← 魔法・超常の 3 法則（superhero/villainess 系）
├── knox-rules.md              ← 本格ミステリ 10 則（謎解き系）
├── checklists/                ← 各フェーズのチェックリスト
│   ├── seed-check.md
│   ├── scoped-check.md
│   ├── frozen-check.md
│   ├── drafting-check.md
│   └── approval-check.md
└── worksheets/                ← ワークシート（記入用テンプレ）
    ├── want-need-sheet.md
    ├── beat-sheet-save-the-cat.md
    ├── scene-sequel-sheet.md
    ├── foreshadow-sheet.md
    └── cadence-sheet.md
```

---

## 3. 中核ドキュメントの一行要旨

| ファイル | 一行要旨 |
|---|---|
| `principles.md` | 物語は「約束→侵犯→回収」。約束は Promise、侵犯は Conflict、回収は Reveal |
| `scene-sequel.md` | Scene = Goal-Conflict-Disaster、Sequel = Reaction-Dilemma-Decision。交互配置が動と静のリズムを生む |
| `want-need.md` | Want は表層で欲しいもの（story engine）、Need は深層で満たすべきもの（character arc）。終盤で Want を失い Need を得る構造が定石 |
| `scope-management.md` | 作品破綻の 4 主因 = 登場人物数／視点数／時間軸／ルール例外数の爆発。各軸に bible 側で上限を宣言 |
| `beat-sheets.md` | 15 ビートの Save the Cat、三幕、起承転結、感情曲線。arc/packet 単位で選ぶ |
| `foreshadowing.md` | 仕込みは 3 度の原則（埋める・匂わす・強調）、回収はフェア。読者が手がかりだけで推理可能 = fair play |
| `motif-operations.md` | 反復は段階進行を持たせる（例: 3段 / 5段）。段階後退は因果説明必須、grep で単調性検証 |
| `rubric.md` | 25 項目 0-4 anchored、hard gate 3 項目。80+/60-79/≤59 |
| `reader-personas.md` | 没入型 / 構造型 / 離脱型の 3 persona で review する |
| `cadence.md` | 緊張 6 : 弛緩 4 を基準、作品毎に上書き。beat / scene / ep / packet でそれぞれ設定 |
| `dialogue-craft.md` | 台詞は「情報 + 感情 + 関係」を同時に運ぶ。話者識別は語尾・語彙・話題選択で |
| `description-craft.md` | 五感は 3 つ以上配分、物証は触覚時間 5 行以上（villainess-coc 由来） |
| `pov-craft.md` | focal character の知識状態は append-only。朧げな予感は「予感レイヤ」で別管理 |
| `reveal-plan.md` | fabula（時間順事実）と syuzhet（読者への提示順）を別管理、後者で読者体験を設計 |
| `conflict-design.md` | 4 型（内的・対人・対社会・対運命）を組み合わせる。単一 conflict は単調 |
| `character-design.md` | Want/Need/Sound（声）の 3 軸で定義、相互作用で人物が立ち上がる |
| `world-design.md` | 一貫（ルール）／制約（限界）／驚き（ジャンル外し）の 3 条件 |
| `theme-design.md` | テーマは「主張」ではなく「証明」。作中で証明される |
| `genre-patterns.md` | 悪役令嬢 / 異世界転生 / 学園 / ミステリ / ホラー等のジャンル別典型構造 |
| `editing-craft.md` | 多層推敲（構造→場面→段落→文→語）を順に回す |
| `sanderson-laws.md` | 1. 読者は理解した分だけ魔法を allow / 2. 制約が面白さ / 3. 拡張より深化 |
| `knox-rules.md` | 本格ミステリの fair play 10 則（探偵の隠しごと禁止、双子禁止、等） |

---

## 4. 各 craft ファイルのテンプレ構造

全 craft ドキュメントで以下の構造を取る:

```markdown
# {Topic}

## 1. 一行定義

## 2. なぜ大事か（物語への効能）

## 3. 原理（2〜5 個の原則）

## 4. 実装手順（書くときの具体手順）

## 5. 判定基準（review 時の観点）
- 何を見るか
- 何が不足のサインか
- 直すなら何を触るか

## 6. 失敗パターンと直し方

## 7. チェックリスト（scoped / frozen / drafting / review）

## 8. 参考ワークシート（あれば）

## 9. 出典
```

---

## 5. Motif Operations（generic 化）

本節は works/villainess-coc の `monitoring-dictionary.md` + `drafter-preflight.md` §canon motif から作品固有情報を取り除き、generic 化した手順書。

### 5.1 Motif の設計原理

- **反復 × 段階** の 2 軸を持たせる。ただの反復は退屈、ただの段階は記号化しない
- 段階は **3 段 / 5 段** が扱いやすい（人間の可読単位）
- 段階は **単調進行**（後退は因果説明必須）
- motif 毎に **開幕話での 1 段発生義務** を設けると序盤トーンが軽く保てる（villainess-coc v6 追加の一般化）

### 5.2 Motif Canon の記述項目

作品固有の `.claude/rules/monitoring-dictionary.md` に書くべき最低項目（generic 化したテンプレ）:

```markdown
## motif-{slug}

### 定義
（何の反復か、1〜2 文）

### 段階
| 段 | 意味 | 描写の焦点 | 身体所作／台詞の必要量 |
|---|---|---|---|
| 1 | ... | ... | ... |
| 2 | ... | ... | ... |
| ... | ... | ... | ... |

### 運用ルール
- 単調性: 後退（例: 3→1）は禁止ではないが因果一段落に理由明記
- 同一ビート内の同居: 2 段階以上を同居させない（OR 許容なら理由明記）
- 開幕話の 1 段発生: 必須 / 不要
- 卓/packet/arc 境界での扱い: 連続 / 再初期化

### grep キーワードセット
| 段 | 最低限の grep キーワード |
|---|---|
| 1 | ... |

### reviewer 側での検査
- typed review PART C-5（motif 単調性）で grep hit count と段階認定を記録
- packet freeze 時に「本 packet の motif 段階計画」を packet.yaml に記述
- 段階計画と draft grep 結果の乖離は差し戻し対象
```

### 5.3 Motif が果たし得る機能

同じ motif が複数機能を担うことがある。機能別に意識する:

- **主題のリフレイン** — 意味論の強化
- **伏線化** — 終盤に意味転化して回収
- **POV 単調性の傍証** — focal の内面変化を身体所作で可視化
- **境界接続** — packet 跨ぎの読者感覚の連続性
- **cadence marker** — 緊張弛緩のテンポ基準

### 5.4 Motif を作らない判断

- 作品の主題に結節しない motif は作らない
- 3 段以上の進行を維持できない motif は早期に削除
- 読者が「またこれか」で白けるラインは避ける（=過剰反復）

---

## 6. Scene/Sequel（中核の 1 枚）

### 6.1 定義

| 単位 | 構成 | 機能 |
|---|---|---|
| Scene | Goal → Conflict → Disaster | 動。主人公が何かを試みて、阻害され、さらなる窮地に落ちる |
| Sequel | Reaction → Dilemma → Decision | 静。主人公が反応し、選択肢を前に葛藤し、次の Goal を決める |

### 6.2 交互配置

Scene と Sequel は **原則交互**。連続 Scene は読者を疲弊させる、連続 Sequel は停滞する。

### 6.3 Disaster の 3 類型

- **No**: Goal 未達
- **Yes, but**: Goal 達成したが代償
- **No, and furthermore**: Goal 未達 + さらなる悪化

最も強いのは 3 番目。だが 3 番目ばかりだと息切れするので、1 / 2 を混ぜる。

### 6.4 review 観点

typed review PART C-1 で:
- Scene と Sequel が識別できるか
- 連続 Scene が 3 つ以上続いていないか
- Disaster の類型分布（No / Yes-but / No-and-furthermore の比率）

---

## 7. Want vs Need

### 7.1 定義

- **Want**: キャラクターが **意識的に欲しい** もの。story engine を駆動
- **Need**: キャラクターが **本当に必要** なもの（自覚無きことも多い）。character arc を作る

### 7.2 定石

- 終盤で Want を失うが Need を得る（または Want を見直して Need に再定義）
- Want と Need が一致している = フラットキャラ（動かない）
- Want と Need が遠すぎる = アーク追いづらい

### 7.3 review 観点

typed review PART C-2 で:
- 各主要キャラに Want / Need が設定されているか
- 現在の ep でどちらが駆動しているか
- Want と Need の距離感

---

## 8. Scope Management

### 8.1 4 軸と管理方法

| 軸 | 上限目安 | 管理先 | 爆発の兆候 |
|---|---|---|---|
| 登場人物数 | 主要 5-7 / 全体 30 | `bible/characters.md` | 名前を覚えきれない読者レビュー |
| 視点数 | 1-3 | `bible/rules.md` §POV | POV 変更で読者が混乱 |
| 時間軸 | 1-2（現在＋過去）| `arcs/series-overview.md` | 時系列が追えない |
| ルール例外数 | 3 以下 | `bible/world.md` §ルール | 「この時だけ違う」が増殖 |

### 8.2 review 観点

continuity review で 4 軸の現状をカウント。上限超過は design-debt 起票。

---

## 9. Beat Sheets（型）

### 9.1 主な型

- **Save the Cat 15 ビート**: Opening Image, Theme Stated, Set-Up, Catalyst, Debate, Break into Two, B Story, Fun and Games, Midpoint, Bad Guys Close In, All Is Lost, Dark Night of the Soul, Break into Three, Finale, Final Image
- **三幕**: Setup / Confrontation / Resolution、25-50-25 の比率
- **起承転結**: 序論 / 展開 / 転調 / 結末
- **Vonnegut 感情曲線**: 典型 6 曲線（Man in a Hole / Rags to Riches 等）

### 9.2 選択指針

- 作品全体: Save the Cat or 三幕
- Arc 内: 三幕 or 起承転結
- Packet 内: 起承転結 or Scene/Sequel 交互
- Episode 内: Scene/Sequel

### 9.3 use in review

typed review PART C-4（Cadence/Rhythm）で、採用したビートシートと実装状況を照合。

---

## 10. Foreshadowing

### 10.1 3 度の原則

- **1 度目**: 埋める（読者は気づかなくて良い）
- **2 度目**: 匂わす（違和感を残す）
- **3 度目**: 強調（読者が意識化）

回収は 3 度目以降で起きる。

### 10.2 Fair Play

読者が手がかりから **推理可能** な状態で伏線を置く。後出し設定は fair play 違反。Knox 10 則の精神を非ミステリにも適用。

### 10.3 Foreshadowing Map

`story/foreshadowing-map.md` を台帳化（villainess-coc 実装を参考）:

```markdown
| 伏線 id | 種別 | 1 度目 ep | 2 度目 ep | 3 度目 ep | 回収 ep | 状態 |
|---|---|---|---|---|---|---|
| PF-001 | 物証 | ep02 | ep07 | ep14 | ep20 | 回収済 |
| PF-002 | 言動 | ep05 | ep11 | - | - | 進行中 |
```

### 10.4 review 観点

- typed review PART C-4: 本 ep で仕込んだ伏線 / 回収した伏線を明記
- continuity review: 全 ep 横断で map と draft grep の整合検査

---

## 11. 人気作パターン（genre-patterns.md 抜粋）

### 11.1 悪役令嬢

- 逆転（破滅ルート知覚→回避）
- 元悪役の可愛さ露出
- 周囲の態度変化の段階描写
- 冤罪・誤解の解消
- 本当の敵の顕在化

### 11.2 異世界転生

- 前世記憶の活用（知識チート）
- 新ルール習得の驚き
- 故郷喪失の情緒
- 仲間形成の段階

### 11.3 学園

- 入学時の孤独→友人形成
- 学園祭・試験等のイベント駆動
- 先生・先輩・後輩の関係網
- 卒業の別れ

### 11.4 ミステリ

- fair play
- 読者が推理可能な状態を維持
- Knox / van Dine の 10 則
- 不可能状況→唯一解の快感

### 11.5 ホラー

- 不可視の脅威
- 正気崩壊の段階
- 超常ルールの不完全情報
- 生還か破滅かの不確定性

---

## 12. craft ライブラリの維持

### 12.1 新項目追加

- 作品 learning から複数作品で再利用できると判明したものを昇格
- 昇格は author 承認。昇格理由は元 learning に追記

### 12.2 既項目更新

- review での検出パターンが蓄積したら修正
- 作品固有化が進みすぎたら split し一部を作品側へ戻す

### 12.3 廃止

- 3 作品以上で「使っていない」が確認されたら `craft/archive/` へ移動（削除ではない）

---

## 13. 本ライブラリと既存ファイルの関係

- `bible/rules.md` は craft の **作品固有上書き**。「この作品では Scene/Sequel を採用する」「cadence は 7:3」等
- `.claude/rules/*` は **守る規範**。craft/ の原理から「違反したら ❌」レベルのものを抜粋した rule
- `prompts/` は **起動する prompt**。craft/ の原理を LLM に適用させる prompt 集
- `reviews/*-template.md` は **判定フォーマット**。craft の観点で採点・診断するテンプレ

---

## 14. 作品 init 時のデフォルト採用

新規作品は以下を **default 採用**:

- Scene/Sequel（基準骨格）
- Want/Need（主要キャラ全員）
- Scope Management（4 軸）
- 25 項目 rubric（標準重み）
- Persona A/B/C review
- Fair play foreshadowing

以下は作品側で **選択**:

- Save the Cat / 三幕 / 起承転結 のどれを arc 骨格に使うか
- 反復 motif を何本置くか（0 でも良い）
- ジャンル別パターン（genre-patterns の該当章を参照）

選択結果は `bible/rules.md` に宣言する。
