# 単位階層 v3

> **目的**: Manuscript / Part / Arc / Packet / Episode / Scene / Beat の入れ子関係と、それぞれが何を含み何を含まないかを固定する。Pack A と Pack B で揺れていた単位を 1 階層に統一する。
> **ガチガチ度**: 入れ子順序・命名・最小条件は本 v3 で固定。サイズ目安は推奨値（作品ごとに調整可）。

---

## 1. 入れ子の確定

```
Manuscript （作品全体）
└── Part      （第一部・第二部 等の大区分）
    └── Arc      （Part 内の中規模まとまり）
        └── Packet   （章束・制作レビュー単位）
            └── Episode  （1 話・公開単位）
                └── Scene    （Episode 内の局所衝突）
                    └── Beat     （最小の story moment）
```

**順序固定**: この入れ子は変えない。スキップは認めるが順序入れ替えは禁止。

**スキップ可**: 短編作品は `Manuscript → Part → Arc → Packet → Episode` で Scene/Beat を省略してよい。中編は `Part → Arc` を 1 対 1 にしてよい。長編・連載は全段使う前提。

**Chapter は内部単位として禁止**（→ `01_vocabulary.md` §11）。公開時の表示語としては `Episode` を `第 NN 話` と表示する、`Packet` を `第 N 章` と表示する、等の運用は可。

---

## 2. 各単位の定義

### 2.1 Manuscript（作品全体）

**含むもの**: 作品の全 Part / 全 Arc / 全 Packet / 全 Episode / 全本文

**最小条件**:
- 作品 slug（英数のディレクトリ名）
- premise（1 文）
- 完結予定の有無

**1 manuscript = 1 work = 1 ディレクトリ**。Story Template から init して作る。

**サイズ目安**: 短編 1 万字 〜 長編 100 万字超。本 v3 では字数で縛らない。

---

### 2.2 Part（大区分）

**含むもの**: 1 つ以上の Arc

**役割**: Manuscript を読者の体験単位で大きく区切る。「第一部完」「第二部開幕」のような転換点を持つ。

**最小条件**:
- Part 番号（part-01, part-02, ...）
- Part の主題（1 文）
- Part 開始時と終了時の不可逆変化（主人公／世界／読者理解）
- 次 Part への接続点（or 完結）

**サイズ目安**: 短編は Part を持たない。中編は 1 Part。長編は 2〜5 Part 程度。

**ファイル**: `arcs/series-overview.md` の中に Part 区切りを記述。Part が 3 以上になったら `arcs/parts/part-NN.md` に分割。

---

### 2.3 Arc（中規模まとまり）

**含むもの**: 1 つ以上の Packet

**役割**: Part 内の中期的な問い・反転・関係変化を担う。「主人公が新たな敵を知る Arc」「協力者を得る Arc」等。

**最小条件**:
- Arc 番号（arc-01, arc-02, ...）
- 中核問い（1 文）
- 主反転（1 文）
- 含む Packet 一覧

**サイズ目安**: 1 Arc = 2〜5 Packet 程度。

**ファイル**: `arcs/arc-NN.md`。1 Arc 1 ファイル。シリーズ俯瞰は `arcs/series-overview.md`。

---

### 2.4 Packet（章束）

**含むもの**: 1 つ以上の Episode

**役割**: 制作レビュー単位。複数 Episode の接続・テンポ・局所矛盾・情報開示順を一度に見る。Packet 単位で frozen → drafted → reviewed → released と進む。

**最小条件**（→ Pack A の packet 凍結基準を継承）:
- packet 番号（packet-001, packet-002, ...）
- purpose（1 文）
- entry_state / exit_state
- episode_roles（含む各 episode の役割）
- end_hooks（次 packet への引き）
- disclose / withhold（情報開示制御）
- guardrails（書きすぎ防止）
- 含む各 episode の `role / purpose / loss / gain / reveal / hooks / cliffhanger`

**サイズ目安**: 1 Packet = 5〜15 Episode 程度。

**ファイル**: `packets/exploring/`, `packets/scoped/`, `packets/frozen/` の 3 ステージ。`packet-NNN-{slug}.yaml`。

**ステージ**:
- `exploring`: 構想中。仕様未確定
- `scoped`: 範囲確定。Episode 役割割当中
- `frozen`: Episode 設計凍結。drafter に渡せる

---

### 2.5 Episode（1 話・公開単位）

**含むもの**: 1 つ以上の Scene（短い Episode は Scene を持たず直接 Beat を並べてよい）

**役割**: 公開単位。1 話として読者に届く分量。本文候補を競わせる単位（episode-draft-tournament の対象）。

**最小条件**:
- Episode 番号（packet-NNN-ep-MM）
- focal character（焦点人物）
- 因果一段落（preflight 必須項目）
- 開始時知識状態 / 終了時知識状態
- 関連する packet 要件（Gate A）
- 直前 episode からの carryover（Gate 0）

**サイズ目安**: 1 Episode = 1500〜5000 字程度。kakuyomu 1 話想定。

**ファイル**:
- 設計: `scenes/slotted/packet-NNN-epMM-{slug}.md`（scene_card 形式）
- 本文: `drafts/packet-NNN-epMM-{slug}.md`
- 候補: `drafts/candidates/packet-NNN-epMM/{persona}.md`
- 公開済: `published/packet-NNN-epMM-{slug}.md`

---

### 2.6 Scene（局所衝突単位）

**含むもの**: 1 つ以上の Beat

**役割**: Episode 内の小さな単位。1 つの場面・1 つの局所目的・1 つの転換を持つ。Swain の Scene/Sequel 構造（goal / conflict / disaster）に対応。

**最小条件**:
- 場所・時間
- focal character のローカル目標（goal / desire）
- 障害（obstacle）
- 転換（turn）
- 終了状態

**サイズ目安**: 1 Scene = 500〜2000 字。1 Episode 内に 1〜4 Scene 程度。

**ファイル**: 通常は scene_card に内包される。Episode より下の単位を独立ファイル化する必要は薄い。**例外**: 凝った構成の Episode で Scene 単位を別管理したい場合のみ独立ファイル化。

---

### 2.7 Beat（最小単位）

**含むもの**: なし（最小単位）

**役割**: 1 つの story moment。1 つの動き、1 つのリアクション、1 つの台詞群、1 つの reveal、1 つの内省、等。

**最小条件**: なし（自由形式）

**サイズ目安**: 50〜300 字程度。

**ファイル**: scene_card 内のビート列として記述。独立ファイル化は不要。

---

## 3. Scene Card（設計成果物）

> **混同警告**: `Scene Card` は story unit ではなく **設計成果物** の名前。`Scene` という story unit とは別物。

### 3.1 役割

1 Episode を書くための設計カード。Adapter の主出力。drafter に渡す。

### 3.2 含むフィールド

```yaml
scene_card:
  id: "packet-NNN-epMM-{slug}"
  target_unit: episode
  packet_id: "packet-NNN"
  episode_number: MM
  focal_character: ""
  
  # 1 行の物語的役割
  purpose: ""
  
  # 開始 / 終了の世界状態（外部）
  entry_state: {}
  exit_state: {}
  
  # 内容制約
  must_include:
    - ""
  must_not_include:
    - ""
  
  # 情報設計
  intended_unknowns:
    - ""
  must_be_clear:
    - ""
  
  # 読者への効果
  reader_target:
    - ""
  
  # 文体・声
  style_constraints:
    pov: ""
    tense: ""
    register: ""
  
  # 依存
  dependencies:
    - prior_episode: ""
    - packet_requirement: ""
    - bible_reference: ""
  
  # ビート列（任意。Scene/Beat レベルで詰めたい場合のみ）
  beats:
    - id: ""
      goal: ""
      conflict: ""
      turn: ""
```

### 3.3 ファイル

`scenes/slotted/packet-NNN-epMM-{slug}.md`（YAML フロントマター + 散文メモ）

---

## 4. Acceptance Contract（設計成果物）

> **対**: scene_card は drafter 用、acceptance_contract は judge 用。**Adapter が両方を同時に発行する**。

### 4.1 役割

judge がこの Episode を PASS / FAIL 判定するための合格基準。

### 4.2 含むフィールド

```yaml
acceptance_contract:
  id: "packet-NNN-epMM-{slug}"
  target_unit: episode
  
  # 必達
  must_satisfy:
    - id: ""
      claim: ""
      verifiable_by: prose | meta | reviewer | reader_simulation
  
  # 違反禁止
  must_not_violate:
    - id: ""
      claim: ""
      severity: low | medium | high | critical
  
  # 意図的曖昧
  intended_unknowns:
    - ""
  acceptable_ambiguity:
    - ""
  must_be_clear:
    - ""
  
  # 品質ライン
  quality_bar:
    rubric_minimum_total: 60
    hard_gate_minimum: 2  # G1/G2/G3 が全て 2 以上
  
  # 自動修正・人間判断の境界
  auto_fix_allowed:
    - ""
  human_required_if:
    - ""
  ignore_or_defer:
    - ""
```

### 4.3 ファイル

`reviews/contracts/packet-NNN-epMM-{slug}.contract.yaml`

---

## 5. 単位ごとの作業マッピング

| 単位 | 主たる作業 | 主たる workflow | 主たる reviewer |
|---|---|---|---|
| Manuscript | 全体構想 | manuscript-final-review | author + critic 全種 |
| Part | 大区分設計 | part-through-review | author + critic |
| Arc | 中規模設計 | arc-through-review / arc-strategy-tournament | plotter + critic |
| Packet | 章束設計 + freeze | packet-assembly-review / packet-freeze-review | plotter + critic |
| Episode | 本文 draft | episode-draft-tournament | drafter + judge + typed_review reviewer |
| Scene | 場面設計 | （Episode 内に内包） | drafter |
| Beat | 局所運用 | （Scene 内に内包） | drafter |

---

## 6. 公開表示との対応

> **再掲**: `Chapter` は内部単位として禁止だが、公開表示に使うのは自由。

| 内部単位 | カクヨム公開時の表示例 |
|---|---|
| Episode | 「第 N 話 〇〇」 |
| Packet | 「第 N 章」「Part N」（章束を読者に見せる場合） |
| Arc | 章タイトル群でグルーピング表示（読者には Arc という語は見せない） |
| Part | 「第一部」「第二部」 |

公開表示の語は kakuyomu 上の自由。**内部議論では本 v3 の正式語を使う**。

---

## 7. ID 命名規約

```
packet ID:    packet-NNN
              例: packet-001, packet-042

episode ID:   packet-NNN-epMM
              例: packet-001-ep01, packet-001-ep05

scene ID:     packet-NNN-epMM-scXX
              例: packet-001-ep01-sc02

beat ID:      packet-NNN-epMM-scXX-btYY
              例: packet-001-ep01-sc02-bt03

arc ID:       arc-NN
              例: arc-01, arc-05

part ID:      part-NN
              例: part-01, part-02
```

スラグは省略可だが、ファイル名には付ける（`packet-001-ep01-{kanji-or-romaji}.md`）。

---

## 8. 単位を増やす条件

サイズ目安を超えたとき、機械的に分割するのではなく以下を確認:

- **Episode が長すぎる（5000 字超）** → Episode 分割か、Scene 単位の独立ファイル化
- **Packet の Episode 数が 15 を超える** → Packet 分割または Arc 切り直し
- **Arc の Packet 数が 5 を超える** → Arc 分割または Part 切り直し
- **Part の Arc 数が 5 を超える** → Part 分割

ただし：

- 因果連続性で割れない場合は、サイズ目安を超えても許容する（Pack A `file-growth.md` 原則）
- 分割後も元単位は索引として残す

---

## 9. Pack A / Pack B からの整合差分

### Pack A からの変更

- `Scene` を Episode より下の story unit として明示（Pack A では `Scene` が文脈で曖昧だった）
- `Episode` を story unit として正式採用（Pack A では `episode` を非公式に使っていた）
- `Part` を新設（Pack A は不在）
- `Manuscript` を新設（Pack A は不在）

### Pack B からの変更

- `Scene Card` を story unit と区別して **設計成果物** に限定（Pack B は両方の意味で使われがち）
- `Beat` を最小単位として明示（Pack B は不明示）

### 共通の維持

- `Packet = 章束`（Pack A / Pack B 共通）
- `Episode = 1 話`（Pack B 由来）
- `Arc`（両者共通）
- `Chapter` 内部禁止（Pack B 由来）
