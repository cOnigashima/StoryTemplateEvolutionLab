# Drafter Preflight

drafter が draft（prose 本文）を書く前に必ず通す preflight 手順。本 rule は StoryTemplate から切り出される全ての作品 repo に継承される。

> **起源**: `villainess-coc-survival-with-cheating/learning/2026-04-08-causal-order-preflight.md`（ep01 因果順矛盾インシデント）。drafter が scene card のビート順を機械的に prose に写したことで、POV 人物の知識状態の単調性が壊れた。この失敗型は作品固有ではなく、小説 drafter 一般に遭遇しうる落とし穴として StoryTemplate に本籍を置く。
>
> **方法論**: `factory-platform/docs/story-os-drafter-contract.md`（本ファイルは運用手順、向こうは方法論の解説）。

## 適用範囲

- `/draft` skill、`drafter` agent、および Cowork セッションで drafter 役を担う Claude
- 対象: `drafts/` 配下に新規 prose を書き出す前段
- narration mode（三人称一元／三人称多元／一人称／書簡体 等）を問わず適用する。mode ごとに異なるのは「focal character を誰と見るか」だけで、原則は共通

## 用語

- **focal character**: 当該 scene / beat で読者の知覚がくっついている人物。三人称一元なら POV 人物、一人称なら語り手、三人称多元なら当該ビートの focalizer、書簡体なら書き手
- **知識状態**: focal character が「正式に知っている」情報の集合。身体的予感・朧げな印象は別枠で扱う（後述）

## 基本3原則

drafter は prose を1文でも書き始める前に、以下3項目を **draft ファイルの meta 欄** に書き下ろさなければならない。書き下ろせない状態で prose に入ることを禁じる。

### 1. 因果一段落の事前圧縮（MUST）

このエピソードの時系列と因果を、focal character の知識状態の遷移を含めて1段落に圧縮して書く。

- 開始時点で focal character が知っていること／知らないこと
- このエピソード中に新しく「正式に」知ることになる情報と、その伝達者・伝達方法
- このエピソード中に focal character が取る行動の因果連鎖（Aを見たからBをした、BしたからCが起きた）
- 終了時点で focal character が知っていること／まだ知らないこと

1段落に圧縮できない（＝自分の中で因果が整理されていない）場合、scene card に戻って上流と相談する。

### 2. 知識状態台帳の単調性チェック（MUST）

draft 内で focal character が「知る」情報は append-only でなければならない。

- エピソード開始時点の既知リストを列挙
- ビートごとに追加される既知情報と、その追加経路（誰から・何によって・どのビートで）を列挙
- 「すでに台帳に載っている情報を、focal character が初めて知るかのように書く」ことを禁止
- 「台帳に載っていない情報を、focal character がすでに知っているかのように書く」ことも禁止
- 身体的予感・直感・朧げな印象として前倒しで書く場合は、**知識状態とは別の「予感レイヤ」** として明記する（正式な既知とは区別する）
- narration mode が三人称多元など、focalizer が beat ごとに切り替わる場合、各 focal character ごとに独立した台帳を持つ

### 3. 合理化語彙の tell 検知（SHOULD）

以下の語彙が draft に出たら、因果順矛盾を文体で塗り潰している可能性を疑う。出現箇所それぞれについて、因果が実際に通っているかを確認する。

- 「つまり」「要するに」「ということは」「〜ということになる」
- 「なるほど」「合点がいく」「腑に落ちる」
- 「思えば」「考えてみれば」「振り返ってみると」
- 知識状態の飛躍を滑らかに埋める接続詞・メタコメント全般

これらを全面禁止はしないが、出現するたびに「ここは因果順が正しいか」を再確認する。

## draft 着手前の運用 Gate

基本3原則だけでは、連続話運用や packet-first 運用で起きる崩れを防ぎ切れない。StoryTemplate では以下を generic gate として追加する。

### Gate 0: 直前散文照合（MUST）

series opener ではない限り、draft 着手前に **直前エピソードの散文そのもの** を読む。scene card や packet の要約では代替しない。

手順:

1. 直前 ep の散文を開く
2. 開始時点で focal character が知っていることを、**散文根拠付きで** 短く書く
3. 直前 ep から持ち越す物・傷・関係温度・未解決の問いを列挙する
4. 今回の draft 冒頭で、その carryover をどこで再起動するかを決める

検査基準:

- `知っていること` に散文根拠が無い項目がある場合、draft 着手を禁止する
- 直前 ep を読まずに prose に入ることを禁止する
- packet 切り替わり直後の ep では、前 packet からの carryover を最低1件は再起動する

### Gate A: Packet 要件マッピング（MUST）

対象 ep が `packets/frozen/` 配下の packet に属する場合、draft 着手前にその ep が引き受ける packet 要件を一覧化する。

優先して読む場所:

- `purpose`
- `entry_state / exit_state`
- `episode_roles`
- `end_hooks`
- `disclose / withhold`
- `guardrails`
- 依存する `story/promises.md`, `bible/*`, `arcs/*`

手順:

1. 今回の ep に関係する packet 要件を抽出する
2. 各要件について「どのビート / シーンで実装するか」を宣言する
3. 実装しない要件がある場合は `今回の担当外` と明記し、理由を書く

検査基準:

- `実装ビート` が空白の要件が1件でもあれば、draft 着手を禁止する
- `全話通奏低音` 型の要件を外す場合、どこで回収するかを明記する

### Gate C: 前振りチェック（MUST when needed）

この draft にクライマックス beat、大きな反転、正体判明、同調ピークなどの強い山がある場合、その前に **softer version の前振り** が存在するかを確認する。

手順:

1. この draft のクライマックス / 反転を1行で定義する
2. その形の softer version が、前 ep または本 ep 前半のどこにあるかを特定する
3. 無い場合は次のいずれかを選ぶ
   - 前振りを追加する
   - クライマックスを後ろ倒しする
   - 初見の衝撃を意図した例外と明記する

検査基準:

- 強い山があるのに Gate C 判定欄が空白なら、draft 着手を禁止する
- `前振りを追加する` を選んだ場合、本文にその前振りを実装する

### Gate B について

Gate B は reviewer 側の工程。drafter は Gate A で宣言した実装計画を本文に落とし、review 側は `reviews/typed-review-template.md` の `Packet Fulfillment Audit` で達成可否を判定する。

## draft 完了後の Multi-Pass Self-Review

draft を書き終えたら、typed review に渡す前に少なくとも 3 パスを自分で回す。

### Pass 1: 因果・認知チェック

- 知識状態台帳を末尾時点まで更新する
- 因果一段落が散文実装と一致しているか確認する
- 直前 ep からの carryover が散文で再起動しているか確認する
- クライマックスが後ろ1割に押し込まれすぎていないか確認する

### Pass 2: Packet / Canon 反映チェック

- `disclose / withhold / guardrails` が守られているか確認する
- 物的証拠や重要物が本文内で一瞬で通過していないか確認する
- `story/promises.md`, `bible/*`, `arcs/*` と衝突していないか確認する
- motif, thread, callback など作品固有の別軸ルールがある場合はここで照合する

### Pass 3: 読者シミュレーション

- meta を見ず、散文だけで読んで理解できるか確認する
- 読者がこの時点で追うべき問いが散文上に見えるか確認する
- 情報が足りなすぎる / 多すぎる箇所を印で残す

### Pass 4: 横断チェック（3話以上まとめ書き時）

3話以上まとめて書いた場合は必須。

- 全話横断の知識状態台帳を表で並べる
- 物証、関係温度、motif、未解決の問いの連続性を確認する
- 1話目で置いた前振りが後ろで消えていないか確認する

## draft ファイルの meta 欄テンプレ

draft ファイル冒頭に以下のセクションを常設する。

```markdown
## meta

### focal character
（このエピソードで焦点が乗る人物。複数いる場合はビート単位で記載）

### 因果一段落
（ここに1段落で因果と知識状態遷移を書く）

### 知識状態台帳
- 開始時点既知:
  - …
- ビート毎の追加:
  - ビート1: （追加情報 / 追加経路）
  - ビート2: （追加情報 / 追加経路）
- 終了時点既知:
  - …
- 予感レイヤ（正式な既知ではない身体的予感・朧げな印象）:
  - …

### Gate 0: 直前散文照合
- 直前 ep:
- 開始時点 carryover:
- 散文根拠:
- 今回どこで再起動するか:

### Gate A: packet 要件マッピング
| # | packet 要件 | source | 実装ビート / scene | note |
|---|---|---|---|---|
| 1 |  |  |  |  |

### Gate C: 前振りチェック
- 今回のクライマックス / 反転:
- softer version がある場所:
- 判定: `ok / add_foreshadow / delay_climax / intentional_first_shock`

### 合理化語彙 self-check
- 出現: （該当語と箇所 / なし）
- 判定: （因果は通っている / 要修正）
```

## 禁止事項

- meta 3項目を書かずに prose に入ること
- 「因果一段落」に `未決定` や空欄を残したまま prose に入ること（未決定がある場合は scene card / packet に戻る）
- scene card のビート順を、因果整合の確認なしにそのまま prose に写すこと
- 知識状態台帳と予感レイヤを区別せず、朧げな予感を正式な既知として台帳に書くこと
- Gate 0 / Gate A / Gate C のどれかを `省略` とだけ書いて済ませること

## 作品固有の拡張

各作品 repo は `.claude/rules/drafter-preflight.md` を持ち、本ファイルへの参照と作品固有の補足のみを記述する。典型的な拡張項目:

- canon motif の monotonicity（反復構造、回数カウント、段階制）の別軸管理
- 物的証拠・固有名詞の初出エピソードの明記
- 当該作品の narration mode 固有の追加制約
