# Story Template Gap Analysis

- date: 2026-04-18
- scope:
  - `story-template/`
  - `works/villainess-coc-survival-with-cheating/`
  - `works/one-man-statefall/`
- purpose: `story-template` 改善の前段として、現状とあるべき姿を切り分ける

## 結論

`story-template` はすでに **Story OS の思想・最低限の運用ルール** は持っている。
ただし、執筆が進んだ作品から得られた知見のうち、現在 template に反映されているのは主に **docs / rule 層** までで、**review system / starter schema / runtime system** の反映は途中で止まっている。

要するに、現状は以下の状態。

1. **思想は先行している**
2. **実運用で効いた review 手法は local に残っている**
3. **automation / task / intake まわりは one-man-statefall に閉じている**
4. **starter の形が現場の実態に追いついていない**

したがって、template 改善は「全部を一気に取り込む」ではなく、次の 3 段に分けるのが妥当。

1. **core template の底上げ**
2. **review-learning module の昇格**
3. **automation-runtime module の分離導入**

## 現状

## 1. すでに template に入っているもの

以下はすでに `story-template` に昇格済み、または思想として吸収済み。

| 領域 | 現在の反映 | 根拠 |
|---|---|---|
| Story OS の骨格 | `promises -> arc -> packet -> scene -> draft -> review -> canon reverse flow` が README/CLAUDE に明記済み | `story-template/README.md`, `story-template/CLAUDE.md` |
| learning の基本思想 | `learning/` を単なる日報ではなく再利用ルール置き場として扱う思想は反映済み | `story-template/README.md`, `.claude/rules/learning-capture.md` |
| learning capture | 学びを即時ログ化し、昇格パスを持つルールは導入済み | `story-template/.claude/rules/learning-capture.md` |
| drafter preflight の核 | 因果一段落、知識状態台帳、合理化語彙 tell 検知は template 側に本籍がある | `story-template/.claude/rules/drafter-preflight.md` |
| file growth | `one-pager`, `foreshadowing-map`, `typed-review-template`, `reader-review-personas`, `automation-*` などの成長先は概念として記述済み | `story-template/.claude/rules/file-growth.md` |

この意味で、template は「ゼロから考えるための箱」ではなく、すでに **育った作品の痕跡を部分的に抽象化した箱** になっている。

## 2. villainess から見た不足

`works/villainess-coc-survival-with-cheating/` は、template を使って執筆しながら **review 方法論そのもの** を育てた作品になっている。
ここから見える不足は主に 4 つ。

### 2-1. review system が template に実装されていない

template 側は `reviews/README.md` でレビューの存在を説明しているが、実運用で効いた review pack はまだ本体にない。

不足しているもの:

- typed review テンプレート本体
- reader review personas
- 3-pass design review
- packet bridge check
- persona A/B/C の受領プロトコル
- 離脱型読者チェック

根拠:

- template 側は `story-template/reviews/README.md` のみ
- 実運用側には `reviews/typed-review-template-v4.md`, `reviews/packet-002-design-3pass-review.md`, `reviews/P9-post-02-packet-001-to-002-bridge-check.md`, `prompts/reader-review-personas.md` がある

診断:

- **README には review の思想がある**
- **だが review を再実行できる starter / template / prompt が本体にない**

### 2-2. drafter-preflight の本籍がまだ浅い

template 側の preflight は 3 項目に絞られているが、villainess 側ではそこからさらに一般化可能な Gate が増えている。

local に留まっているが、作品固有ではないもの:

- **Gate 0**: 直前 ep の散文照合
- **Gate A**: packet 要件マッピング
- **Gate C**: 前振りチェック
- **Multi-Pass Self-Review**
- **3話以上まとめ書き時の横断チェック**

根拠:

- template 本籍: `story-template/.claude/rules/drafter-preflight.md`
- local 拡張: `works/villainess-coc-survival-with-cheating/.claude/rules/drafter-preflight.md`
- 起源ログ: `works/villainess-coc-survival-with-cheating/learning/2026-04-15-multi-pass-draft-review-flow.md`

診断:

- template は **draft 着手前の最低安全装置** は持つ
- しかし **連続話運用で崩れるポイントを防ぐ運用 Gate** はまだ local

### 2-3. starter schema が実運用に対して薄い

template の `packet-template.yaml` と `scene-template.md` は最小構成としては有効だが、実作品の scene / packet が持っている実務項目を吸えていない。

差分の代表例:

| 領域 | template | 実運用 |
|---|---|---|
| frozen packet | `episodes: []` の空配列中心 | episode ごとの `purpose / desire / obstacle / loss / gain / reveal / hooks / cliffhanger / draft_file / scenes_merged` まで持つ |
| scene card | `purpose / desire / obstacle / turn / reveal` まで | `explorer_action`, 段階ログ, `cliffhanger`, `draft判断メモ` まで持つ |
| packet bridge | 明示項目なし | 上流 exit と下流 entry の接続監査を独立レビュー化 |

根拠:

- template: `story-template/packets/scoped/packet-template.yaml`, `story-template/packets/frozen/packet-template.yaml`, `story-template/scenes/seed/scene-template.md`
- villainess 実運用: `works/villainess-coc-survival-with-cheating/packets/frozen/packet-002-missing-classroom.md`, `works/villainess-coc-survival-with-cheating/scenes/slotted/packet-002-ep20-always-empty.md`
- one-man 改良版 template: `works/one-man-statefall/packets/templates/frozen-template.yaml`

診断:

- 現 template は **思考補助用の starter**
- 実運用で必要なのは **handoff 可能な starter**

### 2-4. review から canon への戻し方が template に型として無い

villainess では review 結果が `learning/`, `typed-review-template-v4`, `canon-patch`, `bible`, `scene` に系統的に戻っている。
しかし template 側は「必要なら戻す」と書いているだけで、戻し先の判断フレームが弱い。

実際に local で起きている昇格:

- Persona B 由来で `PART G / PART H` を typed review に追加
- Persona C 由来で bridge check / 離脱型チェック / scene freeze の離脱リスク欄の構想が出ている
- Axis / 正気耐性の統合で canon patch の交差チェックが必要になっている

根拠:

- `works/villainess-coc-survival-with-cheating/reviews/typed-review-template-v4.md`
- `works/villainess-coc-survival-with-cheating/learning/2026-04-18-persona-A-review-packet-002.md`
- `works/villainess-coc-survival-with-cheating/learning/2026-04-18-persona-B-review-packet-002.md`
- `works/villainess-coc-survival-with-cheating/learning/2026-04-18-persona-C-review-packet-002.md`

診断:

- template は reverse flow の方向だけ持つ
- **reverse flow の受け皿テンプレート** はまだ弱い

## 3. one-man-statefall から見た不足

`works/one-man-statefall/` は、template を執筆 repo として使うだけでなく、**automation-driven runtime** にまで拡張している。
ここから見える不足は主に 5 つ。

### 3-1. template artifact と live runtime artifact の境界が曖昧

もっとも重要な指摘はこれ。

現在の template は `packets/scoped/packet-template.yaml` や `packets/frozen/packet-template.yaml` を **runtime が読む live directory** に置いている。
one-man-statefall ではこれが init 時の事故要因として記録されている。

根拠:

- template 配置: `story-template/packets/scoped/packet-template.yaml`, `story-template/packets/frozen/packet-template.yaml`
- 問題ログ: `works/one-man-statefall/learning/storytemplate-init-intake-20260405.md`
- one-man 側の改善: `works/one-man-statefall/packets/templates/frozen-template.yaml`, `.../scoped-template.yaml`

診断:

- template は **runtime-safe init** をまだ持っていない

### 3-2. intake layer がない

one-man-statefall は、巨大入力をそのまま `story/seeds/` に入れるのではなく、`raw -> digest -> seed -> canon` の層を必要としている。
template 側にはこの入口がまだない。

根拠:

- 問題提起: `works/one-man-statefall/learning/storytemplate-init-intake-20260405.md`
- 実運用 layer: `works/one-man-statefall/story/intake/`

診断:

- template は **small-input manual design** には向く
- **大量インプット起点の作品立ち上げ** にはまだ弱い

### 3-3. machine-readable learning layer がない

template の `learning/` は narrative log 前提。
one-man-statefall ではさらに `daily-writing-retro` と `current-focus.yaml` を分け、翌 run が advisory input として読める形にしている。

根拠:

- 契約: `works/one-man-statefall/story/learning-loop.md`
- narrative retro: `works/one-man-statefall/learning/daily-writing-retro-20260417.md`
- machine-readable focus: `works/one-man-statefall/learning/current-focus.yaml`

診断:

- template は **人間の再読** には対応
- **次 run の機械的再利用** までは未対応

### 3-4. task / workflow / automation module がない

one-man-statefall は `tasks/`, `workflow/`, `logs/automation/`, `telemetry/story-runs/`, `story/progress.yaml`, `story/automation-control.yaml` を持ち、執筆を task queue として運用している。
この世界観は template 側に存在しない。

根拠:

- `works/one-man-statefall/workflow/packet-standard.yaml`
- `works/one-man-statefall/tasks/templates/task.yaml`
- `works/one-man-statefall/tasks/templates/task-context.yaml`
- `works/one-man-statefall/prompts/automation-hourly-queue-manager.md`

診断:

- これは core template へ直接入れると重すぎる
- ただし **optional module として切り出す価値は高い**

### 3-5. queue / frontier / progress の正本が template にない

template manifest は `queue/` を legacy projection と認識しているが、実際の automation 運用では `story/progress.yaml`, `automation-control.yaml`, `tasks/` が正本になっている。

根拠:

- `story-template/template.manifest.json`
- `works/one-man-statefall/story/progress.yaml`
- `works/one-man-statefall/story/automation-control.yaml`

診断:

- template は queue legacy を説明している
- しかし **next-generation runtime contract** はまだ定義していない

## 4. 現在の template の強み

批判だけではなく、強みも明確。

### 4-1. core が痩せていて移植しやすい

いまの template は、最初の 1 作品を立ち上げるには十分軽い。
`README`, `CLAUDE`, `promises`, `bible`, `arcs`, `packets`, `scenes`, `reviews`, `learning` が一式あるため、manual authoring には使いやすい。

### 4-2. 過剰に先回りしていない

`file-growth.md` があるため、「最初から全部揃える」より「必要になったら育てる」の思想が明確。
これは正しい。

### 4-3. core と optional の感覚はすでにある

`actions`, `community`, `campaigns`, `metrics`, `queue` を「運用オプション層」として分けているため、将来的に module 化しやすい。

## あるべき姿

## 1. core template は軽いまま、段階的に強くなるべき

あるべき姿は「全部入り template」ではない。
むしろ以下の 4 層に分けるべき。

### Layer A: Core Authoring

必須。

- `README.md`
- `CLAUDE.md`
- `story/promises.md`
- `bible/*`
- `arcs/*`
- `packets/*`
- `scenes/*`
- `drafts/`
- `reviews/`
- `learning/`
- `.claude/rules/learning-capture.md`
- `.claude/rules/drafter-preflight.md`

### Layer B: Review-Learning Module

強く推奨。

- `reviews/typed-review-template.md`
- `reviews/bridge-review-template.md`
- `prompts/reader-review-personas.md`
- `prompts/design-3pass-review.md`
- `learning/README.md` の強化
- persona review 受領プロトコル
- multi-pass draft review 運用

### Layer C: Intake Module

大量入力作品向けの optional。

- `story/intake/raw/`
- `story/intake/digests/`
- raw -> digest -> seed の provenance メモ

### Layer D: Automation-Runtime Module

自動執筆作品向けの optional。

- `workflow/`
- `tasks/`
- `logs/automation/`
- `telemetry/story-runs/`
- `story/progress.yaml`
- `story/automation-control.yaml`
- `story/learning-loop.md`
- `learning/current-focus.yaml`

## 2. core に入れるべきもの

次に template 本体へ入れるべきなのは、作品固有でないものに限る。

### 2-1. runtime-safe starter 配置

最優先。

- `packets/scoped/packet-template.yaml` と `packets/frozen/packet-template.yaml` を live dir から外す
- `packets/templates/` へ移す
- `template.manifest.json` で「template artifact」と「runtime artifact」を分離する

### 2-2. packet starter v2

`episodes: []` の空配列ではなく、最初から 3 話分の episode schema を持つ starter にする。

最低限ほしい項目:

- `id`
- `title`
- `status`
- `role`
- `purpose`
- `desire`
- `obstacle`
- `loss`
- `gain`
- `emotion_curve`
- `reveal.disclose`
- `reveal.withhold`
- `hooks`
- `cliffhanger`
- `draft_file`
- `scenes_merged`

### 2-3. scene starter v2

以下は generic なので template に昇格可能。

- `cliffhanger`
- `next scene handoff`
- `review memo`
- `bridge note`

以下は optional field として載せるのが妥当。

- `explorer_action`
- `motif note`
- `dropout risk`

### 2-4. typed review base template

template は `reviews/README.md` だけでなく、最低 1 本の typed review template を持つべき。

最低構成:

- Part A: micro/prose
- Part B: dialogue/scene
- Part C: macro structure
- Part D: score or verdict
- Part E: packet fulfillment audit

extension slots:

- Part F+: works-local extension

### 2-5. drafter-preflight base expansion

works 固有でない範囲で、以下は本籍昇格を検討してよい。

- 直前 prose 照合
- packet 要件マッピング
- multi-pass self-review
- batch draft 時の cross-episode audit
- climax 前振りチェック

## 3. optional module に切り出すべきもの

### 3-1. persona review pack

villainess の Persona A/B/C はそのままは作品依存がある。
ただし抽象化した pack としては切り出せる。

抽象化すべき軸:

- 没入型
- 構造型
- 離脱型

作品ごとに差し替えるもの:

- ジャンル期待
- 市場期待
- 固有モチーフ

### 3-2. bridge review pack

packet-001 終了 -> packet-002 開始のような橋渡し監査は、多くの作品で再利用できる。
これは core に入れてもよいが、まずは optional template として分離導入が安全。

### 3-3. automation-runtime pack

one-man-statefall の `tasks/` 運用は有効だが、全作品の default にすると重い。
optional starter として分離すべき。

### 3-4. machine-readable learning pack

`learning/current-focus.yaml` は automation 作品では非常に効く。
ただし manual 作品では過剰。
これも optional。

## 優先順位付きの反映候補

## P0

- `packets/templates/` を template 本体へ追加し、live dir の packet template を退避する
- `template.manifest.json` に template artifact / runtime artifact の境界を追加する
- `reviews/typed-review-template.md` を追加する
- `prompts/reader-review-personas.md` または review pack README を追加する

## P1

- `packet-template` を episode embedded 形式へ更新する
- `scene-template` に `cliffhanger` と handoff 系項目を追加する
- `.claude/rules/drafter-preflight.md` に generic Gate 追加を検討する
- `reviews/bridge-review-template.md` を新設する

## P2

- `story/intake/` module を optional で導入する
- `learning/current-focus.yaml` module を optional で導入する
- `workflow/` + `tasks/` automation module を optional で導入する

## 反映しないほうがよいもの

以下は template core には入れないほうがよい。

- ジャンル固有モチーフ管理
- 固有作品の口調段階表
- villainess の鐘 / 紅茶 / ですわぁの具体値
- one-man-statefall の queue policy の細部
- 作品別の運用ログ命名に依存する task 契約

template core に入れるべきなのは、あくまで **抽象化された失敗回避手順** と **再利用可能な器**。

## 最終診断

改善方針は明確。

`story-template` は今、

- **思想テンプレとしては強い**
- **review template と starter schema は弱い**
- **runtime system は未分離**

という状態にある。

次の一手として最も効果が高いのは、

1. **runtime-safe init**
2. **typed review / bridge review / persona review の template 化**
3. **packet / scene starter の v2 化**

の 3 点。

これをやるだけで、template は「考え方の箱」から「進んだ作品の知見を再現できる箱」へ一段上がる。
