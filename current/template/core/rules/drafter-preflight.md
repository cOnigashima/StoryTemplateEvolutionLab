# origin: STE-v4 / fools / villainess（2026-07-06 復元マージ: 旧216行版のディテールを新構造パスで復元）
# drafter-preflight — 執筆着手の前に必ず通すゲート（AIはこれをスキップできない）

> **起源**: villainess ep01 因果順矛盾インシデント（drafter が scene card のビート順を機械的に prose に写し、POV 人物の知識状態の単調性が壊れた）。この失敗型は作品固有ではなく drafter 一般の落とし穴。

## 適用範囲

- `/draft` skill、`drafter` agent、TAKT draft workflow、および drafter 役を担う AI セッション
- 対象: `runtime/drafts/` 配下に新規 prose を書き出す前段
- narration mode（三人称一元／三人称多元／一人称／書簡体 等）を問わず適用。mode ごとに異なるのは「focal character を誰と見るか」だけで、原則は共通

## 用語

- **focal character**: 当該 scene / beat で読者の知覚がくっついている人物。三人称一元なら POV 人物、一人称なら語り手、三人称多元なら当該ビートの focalizer、書簡体なら書き手
- **知識状態**: focal character が「正式に知っている」情報の集合。身体的予感・朧げな印象は別枠の**予感レイヤ**で扱う

## 基本3原則（meta 欄に書き下ろせないなら prose に入らない）

### 1. 因果一段落の事前圧縮（MUST）

- 開始時点で focal character が知っていること / 知らないこと
- この話で新しく「正式に」知る情報と、その伝達者・伝達方法
- focal character が取る行動の因果連鎖（Aを見たからBをした、BしたからCが起きた）
- 終了時点で知っていること / まだ知らないこと
- → 1段落に圧縮できなければ scene card に戻って上流と相談する。

### 2. 知識状態台帳の単調性チェック（MUST）

- `state/knowledge_state.yaml` を参照。既知は **append-only**。
- 既に台帳にある情報を「初めて知る」ように書かない。台帳に無い情報を「既に知っている」ように書かない。
- 新規に知る情報は at_episode と source（どの出来事で知ったか）を追記する。
- 身体的予感・直感・朧げな印象として前倒しで書く場合は、正式な既知と区別して**予感レイヤ**に明記する。
- focalizer が beat ごとに切り替わる mode では、**focal character ごとに独立した台帳**を持つ。

### 3. 合理化語彙の tell 検知（SHOULD）

以下が出たら因果順矛盾を文体で塗り潰している可能性を疑い、出現箇所ごとに因果が実際に通っているか再確認する:

- 「つまり」「要するに」「ということは」「〜ということになる」
- 「なるほど」「合点がいく」「腑に落ちる」
- 「思えば」「考えてみれば」「振り返ってみると」
- 知識状態の飛躍を滑らかに埋める接続詞・メタコメント全般

## draft 着手前の運用 Gate

### Gate 0: 直前散文照合（MUST）

series opener でない限り、**直前エピソードの散文そのもの**を読む（scene card や packet の要約で代替しない）。

1. 直前 ep の散文を開く
2. 開始時点で focal character が知っていることを**散文根拠付きで**短く書く
3. 持ち越す物・傷・関係温度・未解決の問いを列挙する
4. 今回の draft 冒頭で、その carryover をどこで再起動するかを決める

検査基準: 散文根拠が無い「既知」が1件でもあれば着手禁止。packet 切替直後の ep では前 packet からの carryover を最低1件は再起動する。

### Gate A: Packet / Writing Pack 要件マッピング（MUST）

対象 ep が packet（overlay: unit-packet-2stage）または Writing Pack の must_satisfy を持つ場合、着手前に要件を一覧化する。

優先して読む場所: purpose / entry_state・exit_state / episode_roles / end_hooks / disclose・withhold / guardrails / 依存する bible facet（promise / plot / arcs）

1. 今回の ep に関係する要件を抽出する
2. 各要件について「どの beat / scene で実装するか」を宣言する
3. 実装しない要件は「今回の担当外」と理由付きで明記する

検査基準: 実装 beat が空白の要件が1件でもあれば着手禁止。「全話通奏低音」型の要件を外す場合、どこで回収するかを明記する。

### Gate B について

Gate B は reviewer 側の工程。drafter は Gate A で宣言した実装計画を本文に落とし、review 側が typed review の Packet Fulfillment Audit で達成可否を判定する（`review-gate.md` 参照）。

### Gate C: 前振りチェック（MUST when needed）

クライマックス beat・大きな反転・正体判明・同調ピーク等の強い山がある場合:

1. クライマックス / 反転を1行で定義する
2. その **softer version の前振り**が前 ep または本 ep 前半のどこにあるか特定する
3. 無い場合: 前振りを追加する / クライマックスを後ろ倒す / 初見の衝撃を意図した例外と明記する、のいずれかを選ぶ

検査基準: 強い山があるのに Gate C 判定欄が空白なら着手禁止。「前振りを追加する」を選んだら本文に実装する。

## draft 完了後の Multi-Pass Self-Review

typed review / TAKT critic に渡す前に、最低3パスを自分で回す。

- **Pass 1: 因果・認知** — 知識状態台帳を末尾時点まで更新 / 因果一段落と散文実装の一致 / carryover の散文上の再起動 / クライマックスが後ろ1割に押し込まれすぎていないか
- **Pass 2: Packet / Canon 反映** — disclose・withhold・guardrails の遵守 / 物的証拠・重要物が一瞬で通過していないか / bible・design・packet 定義との衝突 / motif・thread・callback 等の作品固有別軸ルールの照合
- **Pass 3: 読者シミュレーション** — meta を見ず散文だけで理解できるか / 読者が追うべき問いが散文上に見えるか / 情報過少・過多の箇所に印
- **Pass 4: 横断チェック（3話以上まとめ書き時は必須）** — 全話横断の知識状態台帳を表で並べる / 物証・関係温度・motif・未解決の問いの連続性 / 1話目の前振りが後ろで消えていないか

## draft ファイルの meta 欄テンプレ

```markdown
## meta

### focal character
（複数いる場合は beat 単位で記載）

### 因果一段落
（1段落で因果と知識状態遷移を書く）

### 知識状態台帳
- 開始時点既知:
- beat 毎の追加: （追加情報 / 追加経路）
- 終了時点既知:
- 予感レイヤ（正式な既知ではない身体的予感・朧げな印象）:

### Gate 0: 直前散文照合
- 直前 ep: / 開始時点 carryover: / 散文根拠: / 今回どこで再起動するか:

### Gate A: 要件マッピング
| # | 要件 | source | 実装 beat / scene | note |
|---|---|---|---|---|

### Gate C: 前振りチェック
- クライマックス / 反転: / softer version の場所:
- 判定: `ok / add_foreshadow / delay_climax / intentional_first_shock`

### 合理化語彙 self-check
- 出現: （該当語と箇所 / なし） / 判定: （因果は通っている / 要修正）
```

## 禁止事項

- meta 3項目を書かずに prose に入ること
- 「因果一段落」に未決定や空欄を残したまま prose に入ること（未決定は scene card / packet に戻す）
- scene card のビート順を、因果整合の確認なしにそのまま prose に写すこと
- 予感レイヤを正式な既知として台帳に書くこと
- Gate 0 / A / C のどれかを「省略」とだけ書いて済ませること

## 作品固有の拡張

各作品は work.manifest の `work_local_extensions` で本ファイルへの参照と作品固有の補足のみを追加する。典型例: canon motif の monotonicity（反復・回数・段階制）の別軸管理 / 物的証拠・固有名詞の初出 ep 明記 / narration mode 固有の追加制約。
