# 新規作品 Pilot Bootstrap 手順 v3

> **目的**: 新規 pilot 作品を起こすための最小手順を 1 本にまとめる。本 v3 全ての設計を実物に落とす最初の一手。
> **ガチガチ度**: 手順順序は推奨。スキップ条件は明示。
> **前提**: `00_README.md` 〜 `08_open_questions.md` を読了済。author の `08_open_questions §4 AD-01 〜 AD-08` 判断が済んでいる。

---

## 0. 前提決定事項

着手前に author 判断（AD-01 〜 AD-08）が確定していること:

| ID | 確定事項 | サンプル値 |
|---|---|---|
| AD-01 | 作品 genre | 例: ライトノベル系 / 文芸 / etc. |
| AD-02 | 作品 scale | 例: 短編 1〜3 episode |
| AD-03 | writer persona 数 | 例: 3（faithful / emotional / plot-drive） |
| AD-04 | ディレクトリ位置 | 例: `works/{slug}/` |
| AD-05 | executable depth | 例: DoD-E まで通すが公開はしない |
| AD-06 | fat-by-design 上限 | 例: 中庸（craft 5 本先行） |
| AD-07 | TAKT 採用可否 | 例: 採用 |
| AD-08 | 完全新規 vs 既存転用 | 例: 完全新規 |

**未決があれば本 bootstrap 手順を始めない**。author に判断を仰ぐ。

---

## 1. ディレクトリ作成

```bash
WORK_SLUG="..."   # 例: "ai-atelier"
WORK_PATH="story-template for TAKT/works/${WORK_SLUG}"

mkdir -p "${WORK_PATH}"/{story/{intake/{raw,digests},seeds,canon-patch-proposals},bible,arcs,packets/{exploring,scoped,frozen},scenes/{seed,slotted,superseded},drafts/candidates,reviews/contracts,craft,approved,published,learning,ledger/character-states}
mkdir -p "${WORK_PATH}/.claude/agents"
mkdir -p "${WORK_PATH}/.takt/"{workflows,facets/{personas,policies,knowledge,instructions},tasks,runs}
```

### チェック
```
□ 上記全ディレクトリが存在
□ 各ディレクトリは空（gitkeep でもよい）
```

---

## 2. .claude/rules/ 継承

Story Template 本体の `.claude/rules/` をコピー（または symlink）:

```bash
TEMPLATE_RULES="story-template for TAKT/.claude/rules"

cp "${TEMPLATE_RULES}/learning-capture.md" "${WORK_PATH}/.claude/rules/"
cp "${TEMPLATE_RULES}/drafter-preflight.md" "${WORK_PATH}/.claude/rules/"
cp "${TEMPLATE_RULES}/file-growth.md" "${WORK_PATH}/.claude/rules/"
cp "${TEMPLATE_RULES}/kakuyomu-policy.md" "${WORK_PATH}/.claude/rules/"
cp "${TEMPLATE_RULES}/story-os-boundaries.md" "${WORK_PATH}/.claude/rules/"
```

### チェック
```
□ 5 ルール継承済
□ 必要に応じて作品固有 rules（drafter-preflight 拡張等）を追加
```

---

## 3. CLAUDE.md 作成

`${WORK_PATH}/CLAUDE.md` を作成。Story Template の CLAUDE.md を母体に、作品固有情報を埋める:

```markdown
# {作品タイトル}

## 作品概要
- 一行要約: {1 文}
- genre: {genre}
- 現在のフォーカス Arc: arc-01
- 現在のフォーカス Packet: packet-001-{slug}

## 制作優先順位
1. story/promises.md の約束を壊さない
2. 巨大入力は story/intake/ を経由
3. 次の 1〜2 packet の因果に効くものだけ先に固める
4. 空欄は禁止。未確定は status で明示
5. Review は感想で終わらせず、必要なら上流へ戻す
6. Review では issue level / return target / recommended next job / expected delta を残す

## 文体指針
- POV: {pov}
- 時制: {tense}
- 文体: {register}
- 一文の長さ: {sentence_length_baseline}
- 地の文の温度: {narrative_temperature}

## 禁則
- 絶対 NG: {forbidden_words}
- 避ける: {soft_forbidden}

## 執筆開始ライン（DoR-A 準拠）
（DoR-A チェックリスト → 06_setup_dor.md §2）

## 参照ファイル
（Story Template と同じ参照集 + 本作品固有のもの）

## Story OS
（Story Template と同じ）

## Skills / Agents
- /pitch  - seed / packet 材料を作る
- /draft  - frozen packet と scene 群から本文を起こす
- /critic - typed review を作り、必要なら上流へ返す
- /continuity - 過去話との整合性チェック
- /release - 公開用に整形

agents:
- plotter
- drafter
- critic
- continuity-checker
- adapter（次セッション）
- judge（次セッション）
- ledger-keeper（次セッション）
```

### チェック
```
□ CLAUDE.md が存在
□ 作品固有情報が暫定でも埋まっている
□ 参照ファイル一覧が更新されている
```

---

## 4. story/kernel.yaml 作成

これが本 bootstrap の **核心**。`04_kernel_spec.md` §2 のスキーマで作成。

```bash
touch "${WORK_PATH}/story/kernel.yaml"
```

```yaml
# story/kernel.yaml の中身
# 04_kernel_spec.md §2 の全構造をコピーし、各 value を埋める
# 全 MUST 項目に必ず value or status を入れる
# 不明な項目は status: needs_author_decision にする
```

### 手順詳細

1. **premise を 1〜2 文で書く**（10 〜 30 分）
   - サンプル: 04_kernel_spec.md §3.1 参照
2. **promise を 3〜5 項目で書く**（30 分）
   - 各 item に evidence_target（暫定でよい）
3. **protagonist_vector の want / need を書く**（30 分）
   - want と need は **必ずぶつける**
   - wound は deferred 可
4. **conflict 3 軸**（20 分）
   - 最低 1 軸 filled、他は tentative
5. **stakes**（15 分）
6. **change_model**（15 分）
   - arc_shape のどれかを選ぶ
7. **causality**（10 分）
   - linear / strict が default 推奨
8. **information_design**（30 分）
   - must_be_clear と intended_unknowns を分けて書く
9. **emotional_arc**（15 分）
10. **style_voice**（30 分）
    - pov / tense は author 確定必須
    - forbidden_words は最低 3 件
11. **unit_tree**（10 分）
    - target_total_episodes は AD-02 の scale から逆算

合計 3〜4 時間程度。

### チェック
```
□ kernel.yaml の全 MUST 項目に value or 適切 status
□ kernel_complete.all_must_filled 検証
□ kernel_complete.internal_consistency_checked 検証
□ DoR-A §2.2 を満たす
```

---

## 5. story/promises.md 作成

kernel.promise の各 item を人間可読形式で記述:

```markdown
# {作品タイトル} の作品約束

## 約束 p1: {claim}
**evidence_target**: {packet-XXX or arc-XX}
**status**: filled

詳細...

## 約束 p2: ...
```

### チェック
```
□ kernel.promise の全 item が記述されている
□ DoR-A §2.3 を満たす
```

---

## 6. bible 最小化

### 6.1 bible/world.md

最低 3 行サマリ:

```markdown
# 世界設定

## 1 行サマリ
{時代・場所・特殊ルール の 1 文}

## 主要設定
- {設定 1}
- {設定 2}
- {設定 3}

（詳細は packet ごとに必要なときに追加）
```

### 6.2 bible/characters.md

最低 主人公 + 主要対立者:

```markdown
# キャラクター

## ch-protagonist: {主人公名}
- 役割: protagonist
- want: {kernel.protagonist_vector から}
- need: {kernel.protagonist_vector から}
- wound: {kernel.protagonist_vector から}
- 声: {語尾・口調・話し方}
- 関係: {主要関係 1〜2 件}

## ch-antagonist: {対立者名}
- 役割: antagonist / rival / obstacle
- 動機: {1 文}
- 主人公との関係: {1 文}
```

### 6.3 bible/rules.md

最低 文体方針 + 禁則 1 件:

```markdown
# 文体・禁則

## 文体方針
（kernel.style_voice の内容を反映）
- POV: {pov}
- 時制: {tense}
- 一文の長さ: {sentence_length_baseline}
- 地の文の温度: {narrative_temperature}

## 禁則
- 絶対 NG: {forbidden_words の list}
- 避ける: {soft_forbidden}

## 言葉遣い
（必要に応じて追加）
```

### 6.4 bible/genre-overlay.md（genre 適用時のみ）

AD-01 で確定した genre が overlay を必要とするなら作成:

```markdown
# Genre Overlay: {genre name}

## このジャンルの読者期待
- {期待 1}
- {期待 2}

## このジャンルの約束
- {約束 1}
- {約束 2}

## このジャンルの禁則
- {禁則 1}

## 採用する Framework Lens
- {lens 1}
- {lens 2}
```

### 6.5 bible/project-override.md（必要時のみ）

kernel default や genre overlay を上書きする作品固有方針があれば:

```markdown
# Project Override: {作品タイトル}

## 上書き項目
- {field}: {default} → {override 値}（理由: {reason}）
```

### チェック
```
□ bible/world.md
□ bible/characters.md
□ bible/rules.md
□ bible/genre-overlay.md（必要時）
□ bible/project-override.md（必要時）
□ DoR-A §2.4 を満たす
```

---

## 7. arcs 作成

### 7.1 arcs/series-overview.md

```markdown
# {作品タイトル} シリーズ俯瞰

## Manuscript 全体
- target_total_episodes: {kernel から}
- serial_or_complete: {kernel から}

## Part 構成（Part を持つ場合）
- part-01: {主題}
- part-02: {主題}

## Arc 構成
- arc-01: {中核問い} / {主反転}
- arc-02: ...

## 進行度
- 現在のフォーカス: arc-01
- 完了: なし
```

### 7.2 arcs/arc-01.md

```markdown
# Arc-01: {arc title}

## 中核問い
{1 文}

## 主反転
{1 文}

## 含む Packet
- packet-001-{slug}: {役割}

## 関係性変化
{Arc 中で変わる関係 1 件}

## 伏線（仕込予定）
- {伏線 1}（packet-001 で仕込）

## 伏線（回収予定）
- なし（次 Arc 持ち越し）

## このアーク終了時の不可逆変化
{1 文}
```

### チェック
```
□ arcs/series-overview.md
□ arcs/arc-01.md
□ DoR-A §2.5 を満たす
```

---

## 8. packets/ 最初の 1 本

### 8.1 packets/scoped/packet-001-{slug}.yaml

```yaml
packet:
  id: "packet-001"
  slug: "{slug}"
  arc_id: "arc-01"
  stage: scoped   # exploring → scoped → frozen
  
  purpose: "{1 文}"
  
  entry_state:
    protagonist_position: ""
    knowledge: []
    relationships: {}
  exit_state:
    protagonist_position: ""
    knowledge: []
    relationships: {}
  
  episode_count_target: 5   # 短編なら 1-3、中編なら 8-12
  
  episodes:
    - id: "ep01"
      role: "opening"
      purpose: ""
      loss: ""
      gain: ""
      reveal: ""
      hooks: []
      cliffhanger: ""
    - id: "ep02"
      role: "..."
      ...
  
  end_hooks: []
  
  disclose:
    - ""
  withhold:
    - ""
  guardrails:
    - ""
  
  promise_implementation:
    - promise_id: "p1"
      implementation_episodes: ["ep03", "ep05"]
      note: ""
```

### 8.2 frozen に進めるか?

DoR-C（`06_setup_dor.md` §4）を満たせば `packets/frozen/` に移動。
満たせない項目があれば `packets/scoped/` に留め、足りない部分を埋める。

**典型的な不足**:
- entry/exit_state の knowledge が空
- episode_roles が暫定すぎる
- guardrails が無い

→ author / plotter で詰める。

### チェック
```
□ packets/scoped/packet-001-{slug}.yaml が存在
□ DoR-A §2.6 を満たす（scoped 段階）
□ DoR-C を満たすなら packets/frozen/ に移動
```

---

## 9. story 補助ファイル

### 9.1 story/open-questions.md

```markdown
# Open Questions

## 現在の未解決論点
（執筆中に発見した論点をここに追記）

- なし（v3 bootstrap 時点）
```

### 9.2 story/design-debt.yaml

```yaml
design_debt:
  items: []
```

### チェック
```
□ story/open-questions.md
□ story/design-debt.yaml
□ DoR-A §2.7 §2.8 を満たす
```

---

## 10. ledger 初期化

```bash
touch "${WORK_PATH}/ledger/canon-facts.yaml"
touch "${WORK_PATH}/ledger/timeline.yaml"
touch "${WORK_PATH}/ledger/foreshadowing-status.yaml"
touch "${WORK_PATH}/ledger/open-questions.yaml"
touch "${WORK_PATH}/ledger/author-decisions.yaml"
touch "${WORK_PATH}/ledger/rejected-ideas.yaml"
```

各ファイルの初期内容（空）:

```yaml
# canon-facts.yaml
canon_facts: []
```

```yaml
# timeline.yaml
timeline: []
```

```yaml
# foreshadowing-status.yaml
foreshadowing: []
```

同様に他の 3 ファイルも空配列で初期化。

```markdown
# ledger/README.md（書く場合）
# Ledger 運用

このディレクトリは「制作中の真実台帳」。Bible が書く前の安定設定、Ledger は書きながら更新される実装状況。

## 更新タイミング
- canon-facts: Episode 公開時
- character-states: Episode soft_lock 時
- foreshadowing-status: Episode 仕込/回収時
- open-questions: 制作中の発見時
- author-decisions: author 判断時
- rejected-ideas: 没案発生時

## 更新者
- ledger-keeper persona（TAKT workflow 内）
- author（手動）

## 参照者
- adapter（次回 Episode の文脈作成時）
- judge（contract 充足判定時）
- continuity-checker
```

### チェック
```
□ ledger/ の 6 ファイル初期化
□ DoR-A §2.9 を満たす
```

---

## 11. craft/ 最小（fat-by-design 上限に従う）

AD-06 の判断に従う。中庸（5 本先行）の場合:

```bash
# Story Template の craft/ から最小 5 本をコピー
cp "story-template/craft/principles.md" "${WORK_PATH}/craft/"
cp "story-template/craft/scene-sequel.md" "${WORK_PATH}/craft/"
cp "story-template/craft/want-need.md" "${WORK_PATH}/craft/"
cp "story-template/craft/rubric.md" "${WORK_PATH}/craft/"
cp "story-template/craft/reader-personas.md" "${WORK_PATH}/craft/"
```

> **注**: 本 v3 時点では `story-template/craft/` の中身は README しか無い。Phase 2 で書く想定。Pilot 着手時点では空でもよい（craft 参照しない drafter で start し、必要になったら埋める）。

### チェック
```
□ AD-06 の方針に従って craft/ が用意されている
```

---

## 12. .takt/ 初期化（TAKT 採用時）

### 12.1 .takt/config.yaml

```yaml
takt:
  schema_version: "v1"
  default_provider: claude_code
  default_model: claude-opus-4-7
  language: ja
  workflows_dir: .takt/workflows
  facets_dir: .takt/facets
  tasks_dir: .takt/tasks
  runs_dir: .takt/runs
```

### 12.2 .takt/facets/policies/, knowledge/

参照のみ。例:

```markdown
# .takt/facets/policies/drafter-preflight.md
（参照）.claude/rules/drafter-preflight.md
```

### 12.3 .takt/workflows/, personas/

**本 v3 時点では空**。次セッションで設計・実装。

### チェック
```
□ AD-07 で TAKT 採用なら .takt/config.yaml が存在
□ TAKT 不採用なら本セクションスキップ
```

---

## 13. learning/ 初期化

```bash
mkdir -p "${WORK_PATH}/learning"
touch "${WORK_PATH}/learning/.gitkeep"
```

bootstrap 直後は空。pilot 中に学びが出たら `learning/{date}-{slug}.md` で追加。

---

## 14. DoR-A 全体検証

`06_setup_dor.md` §2 のチェックリストを最後に通す:

```
□ §2.1 ディレクトリ構造 全 ☑
□ §2.2 kernel.yaml MUST 全 ☑
□ §2.3 promises.md
□ §2.4 bible 最小
□ §2.5 arcs 最小
□ §2.6 packet 最小
□ §2.7 open_questions
□ §2.8 design_debt
□ §2.9 ledger 初期化
□ §2.10 サマリ判定
```

→ 全部 ☑ なら **DoR-A 満足**。Episode draft フェーズに入れる。

---

## 15. 最初の Episode draft（次セッション）

DoR-A 満足後、最初の Episode を draft する手順は **次セッション** で扱う。

ただし、必要なものは先取りして列挙:

```
□ scenes/slotted/packet-001-ep01-{slug}.md（scene_card）作成
□ Adapter で acceptance_contract 生成
□ DoR-B チェックリスト通過
□ TAKT episode-draft-tournament 起動 or 手動 draft
□ Multi-Pass Self-Review 4 パス
□ Judge 判定
□ Ledger 更新
□ Typed Review
□ Continuity Review
□ DoD-E チェック
□ author 承認
```

これらは次セッションで個別設計・実装する（→ `08_open_questions.md` §3 NSD-01 〜 NSD-05）。

---

## 16. bootstrap 完了の DoD

本 pilot bootstrap 自体が完了したと言える条件:

```
□ work ディレクトリが存在
□ DoR-A §2 全項目 ☑
□ Pilot 1 本目の Episode draft に入れる状態
□ author が「bootstrap 完了」を確認
```

→ 全部 ☑ なら次は最初の Episode の DoR-B → draft → DoD-E のサイクルへ進む。

---

## 17. bootstrap 中によくある引っかかり

| 引っかかり | 原因 | 対処 |
|---|---|---|
| kernel.premise が 5 行になる | 分解不足 | 「誰が・何を・どうする・なぜ」の 4 要素に絞る |
| promise の evidence_target が全て tentative | packet 未設計 | OK。pilot 進行で埋まる |
| protagonist の want と need が一致 | アーク不在 | want と need を **必ずぶつける** |
| genre_overlay を kernel に書きたくなる | kernel 拡張誘惑 | overlay は別ファイル。kernel は薄く |
| bible/world.md に raw 設定を全部入れたくなる | intake/raw を経由していない | story/intake/raw/ に置いてから digest → seed → bible |
| ledger/ に何を入れるか分からない | bootstrap 時は空でよい | Episode 公開時に初登録。空のままで DoR-A 満足 |
| .takt/workflows/ が空で不安 | 次セッション作成 | 本 bootstrap 時点では空で OK |

---

## 18. 完了後の進路

bootstrap 完了後の選択肢:

1. **次セッションへ**: NSD-01 〜 NSD-10 を順に詰めながら最初の Episode を draft
2. **手動で 1 Episode 試走**: TAKT 不在で人間 + Claude で 1 episode を書き、Retro で問題発見
3. **Adapter 設計に集中**: NSD-01 を最優先で詰めて Adapter 実装
4. **craft 拡充**: AD-06 の上限を上げて craft/* を増やす

author 判断で進路を決める。
