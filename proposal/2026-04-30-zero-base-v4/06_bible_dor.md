# 06 Bible DoR — Definition of Ready for Bible（受け入れ完了条件）

> **役割**: Bible が「受け入れ完了 / 下流フェーズに進めて良い」と判定するための機械的な完了条件。
> **依存**: 02_domain_model.md（用語） / 03_storage_trinity.md（物理配置） / 05_intake_coverage_checklist.md（網羅項目）。
> **対象読者**: Intake Adapter 実行後の reviewer / Episode draft 着手前の drafter / Packet を frozen にする plotter。
> **3 段階**: DoR-A（新規作品 bootstrap） → DoR-B（Episode draft 開始） → DoR-C（Packet frozen 化）。

---

## 0. 使い方

### 0.1 3 つの DoR の関係

```
[企画 / 既存資料]
        ↓
   Intake (Phase 1)
        ↓
   ┌─────────┐
   │  DoR-A  │  新規作品 bootstrap 完了
   └────┬────┘
        ↓ 通過 → Packet 設計可能
   ┌─────────┐
   │  DoR-C  │  Packet frozen 化（Packet ごと）
   └────┬────┘
        ↓ 通過 → Episode draft 可能
   ┌─────────┐
   │  DoR-B  │  Episode draft 開始（Episode ごと）
   └────┬────┘
        ↓ 通過 → drafter が prose を書き始めて良い
```

DoR-A は 1 作品 1 回。DoR-C は packet ごと、DoR-B は episode ごとに毎回判定する。

### 0.2 status との関係（再掲）

| status | DoR-A | DoR-B | DoR-C | DoD-E（参考） |
|---|---|---|---|---|
| `filled` | ✓ | ✓ | ✓ | ✓ |
| `tentative` | ✓ (low risk) | ✓ if 検証段階 | ✓ if not critical | △ |
| `deferred` | MUST=✗ / SHOULD=✓ | MUST=✗ | per case | ✗ |
| `intentionally_blank` | ✓ | ✓ | ✓ | ✓ |
| `intentionally_hidden` | ✓ | ✓ | ✓ | ✓ |
| `not_applicable` | ✓ | ✓ | ✓ | ✓ |
| `project_override` | ✓ | ✓ | ✓ | ✓ |
| `contradiction` | ✗ | ✗ | ✗ | ✗ |
| `needs_author_decision` | MUST=✗ / SHOULD=case | MUST=✗ | per case | ✗ |
| `missing` | MUST=✗ | MUST=✗ | per case | ✗ |
| `rejected` | -（採用前提なので適用外） | - | - | - |

✓ = 通過可、✗ = 通過不可、△ = 通過可だが要レビュー、- = 適用外。

### 0.3 機械的判定 vs author judgment

DoR は **機械的判定可能な条件**で構成する。author judgment 必要な箇所は `needs_author_decision` として明示し、DoR には含めない（含めると判定が止まる）。

---

## 1. DoR-A — 新規作品 Bootstrap 完了条件

### 1.1 ディレクトリ構造（35 項目）

```
□ {work}/CLAUDE.md                          # 制作 OS 契約（必須、分割禁止）
□ {work}/README.md                          # repo 入口（必須、分割禁止）

□ {work}/.claude/                           # Claude Code 設定
  □ {work}/.claude/rules/
    □ drafter-preflight.md                  # MUST 継承
    □ file-growth.md                        # MUST 継承
    □ learning-capture.md                   # MUST 継承
    □ kakuyomu-policy.md                    # MUST（公開作品のみ）
    □ story-os-boundaries.md                # MUST 継承
  □ {work}/.claude/agents/                  # （任意）
  □ {work}/.claude/skills/                  # （任意）

□ {work}/story/
  □ kernel.yaml                             # MUST、schema_version: v4

□ {work}/inbox/                             # raw 受付
□ {work}/adapter/                           # work 固有 override（dot なし）
□ {work}/synthesis/                         # Adapter 出力
□ {work}/bible/                             # frozen 設計
  □ bible/README.md                         # MUST
□ {work}/design/                            # 揺れる設計
  □ design/README.md                        # MUST
□ {work}/state/                             # 動的事実
  □ state/README.md                         # MUST
□ {work}/arcs/                              # Arc 単位設計
  □ arcs/README.md                          # MUST
□ {work}/packets/                           # Packet 単位設計
  □ packets/{exploring,scoped,frozen}/      # 3 ステージ
□ {work}/scenes/                            # Scene Card
□ {work}/drafts/                            # 本編 prose
□ {work}/reviews/                           # 全 review
□ {work}/approved/                          # 承認済 prose
□ {work}/published/                         # 公開済 prose
□ {work}/backlog/                           # 全 task（旧 actions/）
□ {work}/learning/                          # 制作 learning
```

### 1.2 Kernel 完全性（11 項目 → MUST 28 サブ項目）

`story/kernel.yaml` について:

```
□ schema_version: "v4"
□ work_id: 設定済み
□ last_updated: ISO 日付

□ kernel #1  Logline:           value 埋まり、status=filled or tentative
□ kernel #2  Promise:           items が 3 項目以上、各 status 適切
□ kernel #3  Protagonist Vector: want / need 必須、wound は SHOULD
□ kernel #4  Conflict:          external 必須、internal / relational は SHOULD
□ kernel #5  Stakes:            if_fails / why_reader_cares 必須
□ kernel #6  Change Model:      arc_shape / direction / end_state 必須
□ kernel #7  Causality:         time_order / monotonicity 必須
□ kernel #8  Information Design: must_be_clear 必須、intended_unknowns は SHOULD
□ kernel #9  Emotional Arc:     overall_curve / target_emotion 必須
□ kernel #10 Style Voice:       pov / tense 必須、register / temperature は SHOULD
□ kernel #11 Unit Tree:         has_part / target_total / serial_or_complete 必須

□ kernel 全体に missing なし（MUST のみ）
□ kernel 全体に contradiction なし
□ kernel 全体に needs_author_decision なし（または author 解決済み）
```

### 1.3 Bible Facet 完全性（17 facet）

#### MUST facet（必須、必ずファイル存在）

```
□ bible/logline.md                  # Term: Logline (kernel #1 同期)
□ bible/promise.md                  # Term: Promise (kernel #2 同期、3+ items)
□ bible/theme.md                    # Term: Theme
□ bible/rules.md                    # Term: Rules（POV / tense / 禁則 1 件以上）
□ bible/style-voice.md              # Term: Style Voice (kernel #10 同期)
□ bible/plot.md                     # Term: Plot（causal chain 3+ steps）
□ bible/world/                      # Term: World（最低 overview.md）
  □ bible/world/overview.md         # MUST
□ bible/characters/                 # Term: Character
  □ 主人公シート 1 つ以上
  □ 主要対立者 1 つ以上
```

#### SHOULD facet（推奨、不在なら not_applicable 明示）

```
□ bible/system/                     # Term: System（または not_applicable）
□ bible/timeline/                   # Term: Timeline（または not_applicable）
  □ bible/timeline/history.md       # macro
  □ bible/timeline/day-by-day.md    # micro（任意）
□ bible/cadence-plan.md             # Term: Cadence
□ bible/foreshadowing-map.md        # Term: Foreshadowing Map
□ bible/reveal-plan.md              # Term: Reveal Plan（または reveal-budget.md 二層）
□ bible/motif-ladder.md             # Term: Motif（または二層）
□ bible/samples/                    # Term: Sample Scene
  □ サンプル 1 つ以上
```

#### MAY facet（任意）

```
□ bible/genre-overlay.md            # Term: Genre Overlay（必要時）
□ bible/project-override.md         # Term: Project Override（必要時）
□ bible/walkthroughs/               # Term: Walkthrough（必要時）
```

### 1.4 Design 完全性

```
□ design/open-questions.md          # MUST（空でもファイル存在）
□ design/design-debt.yaml           # MUST（空でもファイル存在）
□ design/rejected-ideas.md          # MUST（空でもファイル存在）
□ design/canon-patch-proposals/     # MUST（ディレクトリ）
```

### 1.5 State 完全性

```
□ state/decision-log.yaml           # MUST（空でもファイル存在）
□ state/contradiction-log.yaml      # MUST（空でもファイル存在）
□ state/canon-patch-log.yaml        # MUST（空でもファイル存在）
□ state/timeline-state.yaml         # SHOULD（Timeline facet がある場合 MUST）
□ state/character-states.yaml       # SHOULD
□ state/foreshadowing-implementation.yaml  # SHOULD（Foreshadowing Map がある場合）
□ state/reveal-implementation.yaml         # SHOULD（Reveal Plan がある場合、二層なら不要）
□ state/motif-status.yaml                  # SHOULD（Motif がある場合、二層なら不要）
```

### 1.6 単位主軸の最小成立

```
□ arcs/series-overview.md           # MUST（Manuscript / Part 構造）
□ arcs/arc-01.md                    # MUST（最初の Arc が scoped）
□ arcs/manuscript-plan.md           # SHOULD（制作ロードマップ）
□ packets/scoped/packet-001-{slug}.yaml  # MUST（最初の Packet が scoped）
□ scenes/seed/scene-template.md     # MUST（テンプレート）
```

### 1.7 一貫性チェック

```
□ contradiction-log の severity=high がゼロ
□ open-questions に DoR-A blocker フラグがゼロ
□ Update Proposal 群が author confirmed
□ kernel と bible 同期項目が整合
   - kernel.logline.value == bible/logline.md
   - kernel.promise.items == bible/promise.md の項目
   - kernel.style_voice == bible/style-voice.md
□ Bible vs Genre Overlay の整合（または Project Override で明示）
□ Bible vs Promise の整合
```

### 1.8 DoR-A 通過判定

**MUST 全 ✓ + 一貫性チェック全 ✓ + ディレクトリ構造完全** で DoR-A 通過。

---

## 2. DoR-B — Episode Draft 開始条件

DoR-A を通過した上で、特定 Episode の draft を開始する直前に判定する。

### 2.1 前提

```
□ DoR-A 通過済み
□ 当該 Episode が属する Packet が frozen（DoR-C 通過済み）
```

### 2.2 Episode Pack 完全性（Writing Pack）

```
□ writing/episode_packs/{ep_id}/episode_brief.md
□ writing/episode_packs/{ep_id}/scene_card.md
□ writing/episode_packs/{ep_id}/context_pack.md
□ writing/episode_packs/{ep_id}/acceptance_checklist.md

□ scenes/slotted/{ep_id}-{slug}.md       # Scene Card 正本
□ reviews/contracts/{ep_id}.contract.yaml # Acceptance Contract 正本
```

### 2.3 Drafter Preflight 必須項目

draft ファイル冒頭の meta 欄に書かれていること:

```
□ focal character 宣言
□ 因果一段落（focal character の知識状態遷移を 1 段落に圧縮）
□ 知識状態台帳
   □ 開始時点既知
   □ ビート毎の追加（情報 / 経路）
   □ 終了時点既知
   □ 予感レイヤ（正式既知と区別）
□ Gate 0: 直前散文照合（series opener 以外 MUST）
□ Gate A: Writing Pack 要件マッピング
□ Gate C: 前振りチェック（クライマックス beat あるなら MUST）
□ 合理化語彙 self-check
```

### 2.4 State Snapshot

draft 着手時点の State 値が確認可能:

```
□ state/character-states.yaml の該当 character の現在値
□ state/timeline-state.yaml の直前 ep までの時刻
□ state/foreshadowing-implementation.yaml の planted / not yet harvested 一覧
□ state/reveal-implementation.yaml の disclose 済み / withhold 中一覧
```

### 2.5 DoR-B 通過判定

**Episode Pack 4 ファイル ✓ + Drafter Preflight 全項目 ✓ + State Snapshot 取得済み** で DoR-B 通過。

drafter は prose を書き始めて良い。

---

## 3. DoR-C — Packet Frozen 化条件

`packets/scoped/packet-{NNN}.yaml` を `packets/frozen/` に進める直前に判定する。

### 3.1 Packet YAML 完全性

```
□ packet.id
□ packet.purpose                      # この packet が物語に何をもたらすか
□ packet.entry_state                  # 開始状態
□ packet.exit_state                   # 終了状態
□ packet.episode_count                # 含む Episode 数
□ packet.episode_roles[]              # 各 Episode の役割
□ packet.end_hooks[]                  # Packet 終了の hook
□ packet.disclose[]                   # 本 packet で開示する情報
□ packet.withhold[]                   # 本 packet で隠す情報
□ packet.guardrails[]                 # 守るべき制約
```

### 3.2 各 Episode の最小成立

```
各 episode について:
□ episode.id
□ episode.role                        # この episode が packet 内で果たす役割
□ episode.loss                        # 失うもの
□ episode.gain                        # 得るもの
□ episode.reveal                      # 本 episode で reveal するもの
□ episode.hooks                       # 次への hook
□ episode.cliffhanger                 # 末尾の引き
```

### 3.3 整合性

```
□ entry_state が直前 packet の exit_state と整合
   （または「最初の packet」と明示）
□ 内 episode 間の知識状態遷移が単調
□ disclose / withhold が Reveal Plan と整合
□ guardrails が Promise / Project Override と整合
□ 本 packet で実装する promise.items が列挙されている
□ contradiction 残存ゼロ（severity 問わず）
```

### 3.4 依存先の status

```
依存する以下のすべてが filled / tentative（low risk） / project_override:
□ kernel
□ bible/promise.md
□ bible/theme.md
□ bible/rules.md
□ bible/style-voice.md
□ bible/world/ の関連箇所
□ bible/characters/ の関連箇所
□ bible/foreshadowing-map.md の本 packet 関連
□ bible/reveal-plan.md の本 packet 関連
□ arcs/arc-{N}.md の該当部分
```

### 3.5 Packet Freeze Review 通過

`reviews/packet-freeze-{packet_id}-{date}.md` で:

```
□ 全項目埋まりが reviewer により確認された
□ 直前 packet の exit_state と整合
□ Bridge Review が必要なら実施済み（直前 packet が frozen の場合）
□ 5 つ以下の minor concern（major concern なし）
□ author hard_lock
```

### 3.6 DoR-C 通過判定

**Packet YAML ✓ + 各 Episode ✓ + 整合性 ✓ + 依存先 status ✓ + Packet Freeze Review 通過** で DoR-C 通過。

`packets/scoped/` → `packets/frozen/` に移動可能。

---

## 4. 不満足時の戻し先（Reverse Flow）

各 DoR 不通過時のアクションを明示。

### 4.1 DoR-A 不通過

| 不通過の原因 | 戻し先 / アクション |
|---|---|
| ディレクトリ構造不足 | `work_init/new_work_bootstrap.md` の手順を再実行 |
| kernel item missing (MUST) | Intake Adapter 再実行 + Update Proposal 起票 |
| bible facet missing (MUST) | 該当 facet を埋める Pitch / Seed → Update Proposal |
| bible facet missing (SHOULD) | author に raise → not_applicable / deferred 判断 |
| contradiction high | `design/canon-patch-proposals/` に Patch 起票 → author Approval |
| needs_author_decision | `design/open-questions.md` で author に raise |
| 一貫性違反（kernel-bible 同期不全） | 該当ファイルの sync を Patch で修正 |

### 4.2 DoR-B 不通過

| 不通過の原因 | 戻し先 / アクション |
|---|---|
| Episode Pack 4 ファイル missing | Writing Adapter 再実行 |
| Scene Card missing | `scenes/slotted/` に Scene Card 生成（plotter or Writing Adapter） |
| Acceptance Contract missing | `reviews/contracts/` に Contract 生成（plotter or Writing Adapter） |
| 因果一段落が書けない | scene card に戻る、または packet に戻る（plot 不明確） |
| Gate 0 未実施 | 直前 ep の散文を読む |
| Gate A 不完全 | Writing Pack 要件を再マッピング |
| Gate C 不通過 | 前振りを追加 / クライマックスを後ろ倒し / 初見の衝撃を意図と明示 |
| 知識状態台帳が書けない | `state/character-states.yaml` 確認 → 不足あれば過去 ep を読み直す |
| 合理化語彙乱発 | scene card のビート順を見直す |

### 4.3 DoR-C 不通過

| 不通過の原因 | 戻し先 / アクション |
|---|---|
| Packet YAML 不足 | plotter で再設計 |
| Episode 役割未割り当て | plotter で各 ep の role / loss / gain を埋める |
| entry_state 不整合 | Bridge Review（前 packet と）を実施 |
| 知識状態遷移非単調 | packet 内 episode 順序見直し / scene card 修正 |
| contradiction 残存 | Patch lifecycle 起動 |
| 依存先 missing | bible / arcs に戻って先に埋める（DoR-A の再判定） |
| Packet Freeze Review 通過しない | reviewer 指摘に応じて再修正 → 再 review |

---

## 5. 空欄ポリシー

### 5.1 空欄の意味の使い分け

| 空欄の表現 | 意味 | DoR-A 通過 |
|---|---|---|
| `missing` | 単純に埋まっていない | MUST=✗、SHOULD=✗、MAY=✓ |
| `intentionally_blank` | 「意図的に空」だが該当ありの場合 | ✓ |
| `not_applicable` | 「当該作品に該当なし」 | ✓ |
| `deferred` | 「後で決める、現時点では不要」 | MUST=✗、SHOULD=✓ |
| `intentionally_hidden` | 「裏に値ありだが本文には書かない」 | ✓ |

### 5.2 missing → intentionally_blank の降格条件

`missing` を `intentionally_blank` に降格できるのは、次の条件すべて満たす時:

1. author が「この作品ではこの項目は不要」と明示した
2. 理由が書かれている（`reason: "短編なので Part 不要"` 等）
3. ジャンル特性 / 作品特性として該当しない

降格は **author confirm 必須**。Adapter / drafter 単独で降格しない。

### 5.3 missing → deferred の降格条件

`missing` を `deferred` に降格できるのは:

1. 「後で決める」が author 明示
2. 期限 or 期日 trigger が書かれている（`defer_until: arc-01 完了` 等）
3. defer 中は MUST 項目は DoR-A 通過不可、SHOULD 項目は通過可

期限到来時に再判定。`filled` / `tentative` / `not_applicable` のいずれかに昇格。

### 5.4 not_applicable の判定

| not_applicable が許容される項目 | 条件 |
|---|---|
| Part | 短編・中編 |
| System | 純粋日常系で能力 / 制度なし |
| Foreshadowing Map | 短編で伏線設計が不要 |
| Genre Overlay | ジャンル定義が曖昧な作品 |
| Project Override | ジャンル例外なしの作品 |
| Walkthrough | 単純な作品 |
| Sample Scene | 開始時点で見本不要（後で追加可） |

**Logline / Promise / Theme / Rules / Style Voice / World / Character / Plot は not_applicable を許さない**（必ず何かは存在する）。

---

## 6. 自己点検手順（Review Prompt との連動）

DoR 判定は人間が手で点検すると見落としが発生する。次の review prompt を併用する:

| DoR | 対応 review prompt |
|---|---|
| DoR-A | `07_review_prompts/bible-readiness-review.md` |
| DoR-A の Kernel 部分のみ | `07_review_prompts/kernel-fill-review.md` |
| DoR-A の Bible facet 網羅 | `07_review_prompts/intake-coverage-review.md` |
| DoR-A の Update Proposal 検証 | `07_review_prompts/update-proposal-review.md` |
| DoR-A の contradiction 整理 | `07_review_prompts/contradiction-triage.md` |
| DoR-A の Bible 設計監査 | `07_review_prompts/design-audit-prompt.md` |
| DoR-A の Digest 自己 review | `07_review_prompts/intake-digest-review.md` |
| DoR-B | drafter-preflight.md（既存 rule 継承） |
| DoR-C | Packet Freeze Review template |

---

## 7. 実行例

### 7.1 ia_society の DoR-A 判定

ia_society の現状（`bible/ia_story_bible_v2/` 50 ファイル + αの状態）を本書で点検:

```
□ ディレクトリ構造        △ inbox/ adapter/ synthesis/ 不在 → 要作成
□ kernel.yaml             ✗ 存在しない → 要作成（v3 から v4 へ）
□ bible/logline.md        △ 内容は 01_CORE_CANON.md にあり、要 logline.md として切り出し
□ bible/promise.md        △ 同上、明示的なファイル化が必要
□ bible/theme.md          △ 暗黙には存在、要明文化
□ bible/rules.md          ✓ 10_WRITING_GUIDE_AND_VOICE.md にあり
□ bible/style-voice.md    △ rules と統合中、要分離
□ bible/world/            △ 02_WORLD_SOCIAL_MODEL.md にあり、要再配置
□ bible/characters/       △ 05_CHARACTERS_MAIN_NOVEL.md 等を分割
□ bible/system/           △ 04_INSTITUTIONS_GLOSSARY.md → 移動
□ bible/timeline/         △ 03 + 15 → 移動
□ bible/samples/          △ 11_SAMPLE_SCENES.md → 移動
□ bible/plot.md           △ 08_PLOT_3ACT_AND_20EP.md → 一部 plot.md、一部 arcs/
□ bible/foreshadowing-map △ 07_TRUTH_AND_CLUE_MAP.md → 移動
□ bible/reveal-plan.md    △ 28_REVEAL_BUDGET_SHEET.md → 二層ファイルとして再配置
□ bible/motif-ladder.md   △ 29_OBJECT_MOTIF_LADDER.md → 二層ファイル
□ design/open-questions   △ 13 から分割
□ design/design-debt      △ 50 を移行
□ state/decision-log      △ 13 から分割
□ state/contradiction-log △ 27 を移行
□ state/canon-patch-log   △ 26 を移行

□ contradiction-log severity=high  ✗ X-001（湊の身長 170/175）残存 → Patch 起票要
□ Update Proposal 群     ✗ 未生成 → Intake Adapter 再実行要

DoR-A 通過: NO
Blockers:
  - 大規模な物理再配置必要（Intake Adapter で実施）
  - X-001 解決必要
  - kernel.yaml 作成必要
  - 22-49 EPISODE_FULL_DRAFT を bible から drafts/ に剥がす必要
```

→ **ia_society は v4 への移行プロジェクトを実施しないと DoR-A 通過しない**。詳細は `08_pilot_validation/ia_society_zero_state.md`（実は zero state ではなく partial migration state）と `10_migration_plan.md` で扱う。

### 7.2 ore_tueee_school_hell の DoR-A 判定

```
□ ディレクトリ構造        △ inbox/ adapter/ synthesis/ 不在
□ kernel.yaml             ✗ v3 形式 or 未作成 → 要 v4 化
□ bible/logline.md        ✗ 不在 → 企画書 v0.9.md から抽出
□ bible/promise.md        △ promises.md にあり、リネーム要
□ bible/theme.md          △ 企画書の核から抽出可
□ bible/rules.md          ✓ rules.md 既存
□ bible/style-voice.md    △ rules.md と分離要
□ bible/world/            ✓ world.md 既存（→ world/ に分割可）
□ bible/characters/       ✓ characters.md 既存（→ characters/ に分割可）
□ bible/system/           ✗ 未作成 or not_applicable 要明示
□ bible/timeline/         ✗ 未作成 or not_applicable 要明示
□ bible/samples/          ✗ 未作成 → SHOULD なので deferred 可
□ bible/plot.md           △ 100ep-chapter-list.md と series-bible-v1 から構成
□ design/open-questions   △ open-questions.md 既存
□ design/design-debt      △ design-debt.yaml 既存
□ design/rejected-ideas   △ 既存？要確認

□ contradiction-log severity=high   要確認

DoR-A 通過: NO
Blockers:
  - 物理ファイル名 v3 → v4 リネーム多数（premise → logline 等）
  - 主要 facet の物理分離必要
  - kernel.yaml v4 化必要
```

→ **中間状態の移行**。`08_pilot_validation/ore_tueee_school_hell_partial.md` で詳細。

### 7.3 fools-with-cheating の DoR-A 判定

```
□ ディレクトリ構造        △ adapter/ あり、inbox/ synthesis/ 一部
□ kernel.yaml             ✗ 未作成
□ bible/logline.md        △ premise.md → リネーム要
□ bible/promise.md        ✓ promise.md 既存
□ bible/theme.md          ✓ theme.md 既存
□ bible/rules.md          △ style_guide.md → リネーム要
□ bible/style-voice.md    △ style_guide.md と分離要
□ bible/world/            ✓ world/ 既存（充実）
□ bible/characters/       ✓ characters/ 既存（個別シート充実）
□ bible/system/           ✓ ability_seitouka_ken.md 等から構成可
□ bible/timeline/         △ raw/20_時系列_昇進年表 から構築要
□ bible/samples/          ✓ 26_本文文体サンプル集 を移行可
□ bible/plot/             ✓ plot/ 既存（arc_map 等）
□ bible/foreshadowing-map ✗ 未作成、raw から構築要
□ bible/reveal-plan.md    ✗ 未作成、要設計
□ bible/motif-ladder.md   △ 章末資料から構築可
□ design/open-questions   ✗ 未作成
□ state/                  △ state/ 7 ファイルあるが v4 形式に再配置要

□ Three-Layer 系（fools 固有 facet）  → 作品固有として bible/ 配下に追加
□ 三層対応表 → bible/three-layer/ または state/three-layer-status.yaml
□ 章末資料配置 → bible/in-world-documents/ + state/in-world-documents-placement.yaml
□ 批評性シート → bible/critical-intent.md（fools 固有）

DoR-A 通過: NO
Blockers:
  - ファイル名 v3 → v4 リネーム
  - 一部 facet 不在（foreshadowing-map / reveal-plan）
  - kernel.yaml 作成
```

→ **充実した bible だが v4 整合性なし**。`08_pilot_validation/fools_with_cheating_complete.md` で詳細。

---

## 8. 不変条件（まとめ）

1. **DoR-A 通過なしに DoR-B / DoR-C を判定しない**
2. **DoR-C 通過なしに該当 packet 内 episode の DoR-B を判定しない**
3. **MUST 項目を勝手に降格しない**（author confirm 必須）
4. **contradiction high を放置して DoR 通過させない**
5. **deferred の defer_until が来たら再判定必須**
6. **status は 11 値のいずれか、`-` や `?` で済まさない**
7. **DoR は機械的判定**。author judgment 必要なものは別記
8. **作品固有 facet は本書の MUST に含めない**（generic only）

---

## 9. 関連参照

- **網羅項目の詳細**: `05_intake_coverage_checklist.md`
- **物理配置**: `03_storage_trinity.md`
- **フロー上の位置**: `04_pipeline_overview.md` Phase 1 終了 → Phase 2 開始
- **判定 prompt 群**: `07_review_prompts/`
- **既存 work での通過判定**: `08_pilot_validation/`
- **採用後の移行手順**: `10_migration_plan.md`
