# Template Extraction Method（pilot-driven）

> **種別**: 方法論
> **日付**: 2026-04-29
> **起源**: renji pilot 実走中の試行錯誤

---

## 方法の本旨

「設計室で先に作る最強テンプレート」ではなく、「実走から蒸留される template」を作る。

```
作品 1 を ingest しながら、template を抽出する。
作品 2 を ingest するときに template を更新する。
作品 N で template が安定する。
```

## なぜ pilot-driven か

### 設計室で先に作る場合の問題

- 抽象化が思弁的になり、実際の作品で必要なものが揃わない
- 抽象化が overgeneralized になり、どの作品でも完璧に使えない（汎用的だが、どこにも fit しない）
- 「最強テンプレ」を目指して肥大化する
- author が「で、どれ使えばいい?」と迷う

### pilot-driven の場合の利点

- **実例から抽出するので、抽象化が realistic**
- **作品固有 / 汎用の境界が明示的**（pilot で実走中に「これは renji 専用、これは他にも使える」と判断できる）
- **template skeleton が「埋めるべき項目」を realistic に持つ**
- author が **renji の実例を見ながら template を理解できる**（参照例があると認知負荷が低い）

---

## 具体手順（renji 実例）

### Step 1. 作品の既存資料を ingest 対象として配置

```
renji_novel_bible/
├── 35 既存ファイル
└── README.md
```

これを `inbox/` 相当として扱う。

### Step 2. 作品 directory を作る

```
works/renji/
├── .adapter/
├── inbox/, synthesis/
├── bible/, design/, state/
├── writing/, drafts/
└── ...
```

### Step 3. Adapter docs を作る（renji local）

renji 専用の Adapter 設定を `works/renji/.adapter/` に作る:
- folder_structure
- intake_adapter_prompt
- writing_adapter_prompt（後発、本セッションでは pack format で代用）
- field_mapping
- update_proposal_format
- writing_pack_format
- human_approval_policy
- source_mapping（35 既存ファイルの振り分け表）

この時点では **template 化はしない**。renji 局所で動かす。

### Step 4. ep001 Writing Pack を作る

実走の最終目標として ep001 が書ける状態を作る。これが「Adapter が機能する」具体的な証拠。

### Step 5. **転換点**: ここで template 化を始める

Step 1〜4 までで「renji が動く」状態になった。この時点で:
- 何が renji 固有だったか
- 何が他作品でも使えるか
が見えるようになる。

### Step 6. 並行生成

`works/renji/bible/{file}.md` を作るたびに、対応する `StoryTemplateEvolution/templates/bible/{file}.template.md` も同時に作る。

renji 中身入り版 ←→ 構造のみ template 版

### Step 7. 共通パターンを抽出

複数の bible ファイルで繰り返し出てくる構造（チェックリスト・ルール・状態 enum など）は別ファイルとして抽出:
- `StoryTemplateEvolution/checklists/`
- `StoryTemplateEvolution/rules/`
- `StoryTemplateEvolution/docs/`

### Step 8. 作品固有装置は明示的に隔離

renji の三層対応 / 正当化圏 / レンジ語は作品固有。template には積まない。**「renji 固有として残置」と明記**。

### Step 9. 次作品に持ち越し可能な状態にする

`StoryTemplateEvolution/work_init/new_work_bootstrap.md` で次作品を起こす手順を書く。templates/ から copy して埋める形を確立。

---

## 抽象化の判断基準

各実体ファイルを作るときに以下を問う:

```
Q1. このファイルの構造は他作品でも使えるか?
  Yes → template 化する
  No  → 作品固有として残置（template 化しない）

Q2. この構造のうち、何が作品依存で、何が汎用か?
  汎用部分のみを template に
  作品依存部分は example として注釈に

Q3. このファイルが他作品で同じ役割を果たすか?
  Yes → template 化
  No  → 作品固有
```

renji の実例:

| ファイル | template 化? | 理由 |
|---|---|---|
| premise.md | ✓ | どの作品でも 1 文要約は必要 |
| reader_promise.md | ✓ | どの作品でも読者約束は必要 |
| theme.md | ✓ | どの作品でも主題語は必要 |
| genre.md | ✓ | どの作品でもジャンル指定は必要 |
| style_guide.md | ✓ | どの作品でも文体方針は必要 |
| characters/protagonist.md | ✓ | どの作品でも主人公定義は必要 |
| characters/individual.md | ✓ | 個別キャラ template 化可 |
| world/three_layer_principle.md | ✗ | renji 固有装置 |
| world/ability_seitouka_ken.md | ✗ | renji 固有能力 |
| world/locations.md | ✓ | どの作品でも場所は必要 |
| plot/arc_map.md | ✓ | どの作品でも arc 構造は必要 |
| plot/episode_plan.md | ✓ | 同上 |
| plot/scene_cards.md | ✓ | 同上 |
| in_world_documents/samples.md | ✓ | 章末資料運用は他作品でも採用可 |
| design/project_principles.md | ✓ | 作劇ルール template 化可 |
| design/critical_intent.md | ✓ | 批評性概念は他作品でも採用可（採用しない作品もある） |
| design/editorial_notes.md | ✓ | レビュー観点 template 化可 |
| design/checklists.md | ✓ | チェックリスト template 化可 |
| state/timeline.yaml | ✓ | どの作品でも時系列管理は必要 |
| state/character_states.yaml | ✓ | 同上 |
| state/foreshadowing.yaml | ✓ | 同上 |
| state/three_layer_status.yaml | ✗ | renji 固有装置 |
| state/rejected_ideas.md | ✓ | どの作品でも没案保存は必要 |

template 化率: 約 80%。20% は renji 固有として残置。

---

## 失敗パターン

### Pattern 1: template を先に作る

→ 抽象化が思弁的になる。やめる。

### Pattern 2: 作品固有装置を template 化する

→ template が renji 専用になる。例: 三層対応を template 化すると、他作品が困惑する。

→ **作品固有は template 化しない、と明確に判断**。

### Pattern 3: 1 作品 1 ファイルで完璧 template を作ろうとする

→ 1 作品では汎用化できないことが多い。

→ **複数作品（pilot 1 作品 + 後発作品）で安定化させる**。renji だけで「完成」と思わない。

### Pattern 4: 抽象化のために renji の中身を template にコピー

→ renji 専用情報が template に流入する。

→ **template には構造のみ、中身はヒントとして `<!-- example -->` 注釈**。

### Pattern 5: 「全部 template 化したい」誘惑

→ template が肥大化する。

→ **「他作品で本当に使うか」を毎ファイル問う**。

---

## このメソッドの限界

- 1 作品（pilot）だけでは抽象化が偏る可能性。次作品で template を更新する想定で運用する
- 作品固有 / 汎用の境界判断は author 判断。AI 判断だけで決めない
- pilot 作品が極端な作品の場合（renji のように既存ジャンルの裏返し）、template が偏る可能性。一般作品も検証対象にする

---

## このメソッドを次作品で使うとき

1. 本ファイルを読み直す
2. 新作品の Adapter / Writing Pack を作る間、以下を意識:
   - 各実体ファイルで「これは template にあるか?」を確認
   - 既存 template に無い構造が必要なら、template に追記
   - renji 専用と思っていた装置が、実は別作品にも使えるなら template に持ち上げ
3. 作品 2 つ目のセッション末に、template の差分を retro

複数作品を経て、template が安定する。1 作品で完成形を求めない。
