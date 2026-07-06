# 作品ディレクトリ構造（汎用）

> 1 作品 = 1 ディレクトリ。本ファイルは新規作品起こし時の標準構造。

---

## ディレクトリ

```
{work-slug}/
├── README.md
├── CLAUDE.md
├── .claude/rules/
│   ├── learning-capture.md
│   ├── drafter-preflight.md
│   ├── file-growth.md
│   ├── kakuyomu-policy.md
│   └── story-os-boundaries.md
│
├── .adapter/                        Adapter 設定（StoryTemplateEvolution/adapter からコピー or 参照）
│
├── inbox/
│   └── planning_sessions/           企画チャット / 大量 raw
│
├── synthesis/
│   ├── session_digests/             Intake Adapter 出力（整理済）
│   └── update_proposals/            反映案
│
├── story/
│   ├── kernel.yaml                  薄い 11 項目
│   ├── promises.md                  作品約束
│   ├── open-questions.md
│   ├── design-debt.yaml
│   ├── seeds/
│   └── canon-patch-proposals/
│
├── bible/                           作品の原典・安定設定
│   ├── premise.md
│   ├── reader_promise.md
│   ├── theme.md
│   ├── genre.md
│   ├── style_guide.md
│   ├── characters/
│   │   ├── README.md
│   │   ├── {protagonist_slug}.md
│   │   └── individual/{ch_slug}.md
│   ├── world/
│   │   ├── README.md
│   │   ├── locations.md
│   │   ├── rules.md
│   │   └── {作品固有}.md
│   ├── plot/
│   │   ├── README.md
│   │   ├── arc_map.md
│   │   ├── episode_plan.md
│   │   └── scene_cards.md
│   └── in_world_documents/
│       ├── samples.md
│       └── placement_table.md
│
├── design/                          まだ揺れる設計・author 判断
│   ├── editorial_notes.md
│   ├── checklists.md
│   ├── project_principles.md
│   ├── critical_intent.md
│   ├── open_design_questions.md
│   ├── author_decisions.md
│   └── idea_provenance.md
│
├── state/                           執筆中に動く状態（= ledger）
│   ├── timeline.yaml
│   ├── character_states.yaml
│   ├── foreshadowing.yaml
│   ├── three_layer_status.yaml      作品固有の場合あり
│   ├── open_questions.yaml
│   ├── continuity_notes.md
│   └── rejected_ideas.md
│
├── arcs/
│   ├── series-overview.md
│   └── arc-NN.md
│
├── packets/
│   ├── exploring/
│   ├── scoped/
│   └── frozen/
│
├── scenes/
│   ├── seed/scene-template.md
│   └── slotted/{packet-NNN-epMM}-{slug}.md
│
├── writing/                         Writing Adapter 出力
│   └── episode_packs/{ep}/
│       ├── episode_brief.md
│       ├── scene_card.md
│       ├── context_pack.md
│       └── acceptance_checklist.md
│
├── drafts/
│   └── episodes/{ep}-{slug}.md
│
├── reviews/
│   ├── contracts/{ep}.contract.yaml
│   └── typed-review-{date}-{target}.md
│
├── approved/
├── published/
├── learning/
└── .takt/                           TAKT 採用時のみ
    ├── config.yaml
    ├── workflows/
    ├── facets/
    ├── tasks/
    └── runs/
```

---

## 三層分離の原則

| 層 | 性質 | 配置 |
|---|---|---|
| **bible/** | 書く前に決まる、変更には canon patch | 安定 |
| **design/** | まだ揺れる、author 判断待ち | 揺れる |
| **state/** | 書きながら更新される | 動的 |
| **writing/** | 1 単位を書くために必要な情報だけを圧縮 | 派生 |

**鉄則**: bible に没案 / 仮設を入れない。state に永続設定を入れない。design を bible に昇格させる前に必ず human approval。

---

## 「どこに行くか」判定

| 情報の性質 | 行先 |
|---|---|
| 確定設定（変えない） | bible/ |
| 仮設・候補・未決 | design/ |
| 制作中の動的事実 | state/ |
| 没案 | state/rejected_ideas.md |
| 1 話分の執筆指示 | writing/episode_packs/{ep}/ |
| 完成本文 | drafts/ |
| 大量 raw | inbox/ |
| 構造化 digest と反映案 | synthesis/ |

---

## 重複排除

- 同じ事実は **1 ヶ所のみ正本**。他は索引で参照
- bible と state に同じ情報を書かない（補完関係）
- design で confirmed になったら bible に移動。design からは消す（git で履歴残る）
- state を bible 由来情報で初期化することはあり得る（seed）

---

## 何を作らないか（v0 段階）

- `seeds/`、`canon-patch-proposals/` は実際に必要が出るまで空でよい
- `.takt/` は TAKT 採用時のみ
- `learning/` は学びが出てから
- `craft/` は本リポジトリの `templates/bible/` に頼る（作品固有 craft が必要になったら作る）

---

## 作品固有の追加（renji 例）

renji は固有装置として以下を追加していた:

- `bible/world/three_layer_principle.md`（renji の三層対応原理）
- `bible/world/ability_seitouka_ken.md`（renji の能力仕様書）
- `state/three_layer_status.yaml`（renji 三層の動的 status）

これらは作品固有なので template には積まない。利用者が「うちも欲しい」と判断したらコピー。
