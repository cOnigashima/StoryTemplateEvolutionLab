# WORKFLOW — 新StoryTemplate 1枚ガイド

current/(正本) の全体像と、企画→公開の1周を1枚で掴む。詳細な運用契約は `CLAUDE.md`。

---

## current/ の中身

```
current/
├── README.md              # 正本一覧
├── WORKFLOW.md            # このファイル（1枚ガイド）
├── CLAUDE.md              # AI運用契約
├── work_init/
│   └── new-work-bootstrap.md   # 新作の作り方（current をコピー→別フォルダ）
├── template/              # ★新作がコピーする雛形
│   ├── work.manifest.template.json  # 作品が overlay/逸脱を宣言
│   ├── folder_structure.md          # 作品フォルダの完全な構造定義
│   ├── core/              #   全作品が従う背骨
│   │   ├── kernel.template.yaml     # 芯11項目
│   │   ├── bible/         #   frozen設計（facet）
│   │   ├── design/        #   揺れる設計
│   │   ├── state/         #   ★ontology対応: entities/knowledge/foreshadowing/timeline
│   │   ├── checklists/    #   DoR/DoD・episode acceptance
│   │   ├── rules/         #   preflight・review-gate・kakuyomu-policy・reverse-flow
│   │   └── schema/        #   ontology薄いスキーマ＋relation語彙
│   ├── overlay/           #   作品が選ぶ構造（episode-pack / packet-2stage）
│   └── runtime/           #   作品が持つ空フォルダ雛形（drafts/reviews/approved/published/reader-export/logs）
├── adapter/               # チャット→セッション引き渡し（intake/writing/handoff + review_prompts 7本）
├── agents/                # generic エージェント18本（STE踏襲・温存）
├── skills/                # generic スキル7本（STE踏襲・温存）
├── prompts/               # テンプレ進化メタ手順（00-05）
├── craft/                 # 創作原理の道具箱
├── docs/                  # 仕様正本（kernel_spec / status_vocabulary 12値 / unit_taxonomy / layer_facet_map）
├── INHERITANCE.md         # 元STEからの継承マップ
├── takt/                  # ループ実装（暫定・別セッション）
└── tools/                 # ontology_check.py
```

> 作業ログ・成果物は「作品側」に生まれる（`template/runtime/` が雛形）。ラボ(current)直下には置かない。

---

## 1周（ライフサイクル）

```
[チャットで発想]
    │  adapter/intake が構造化 → [G-Intake 人間承認]
    ▼
current/ をコピー → 別フォルダの works/{作品}/  （core必須＋overlay宣言＋runtime空フォルダ）
    │  bible/design/state が埋まる（checklists で DoR-A 判定）
    ▼
adapter/writing が「1話分」に圧縮（+ ontology k-hop 抽出）
    ▼
takt の workflow がループ： draft → ontology_check → multi-pass review → 修正（堂々巡りは loop_monitor が打切り）
    ▼
作品側 runtime に成果物  ←★ G-Deliverable で人間が確認
    ▼
approved → published、retro を logs/learning へ
    │
    └─ 効いた工夫は current/template に昇格（＝StoryTemplate の進化）
```

---

## 「今なにをしたい？」→ どこを見るか

| やりたいこと | 入口 |
|---|---|
| 運用ルールを知る | `CLAUDE.md` |
| 新作を立ち上げる | `work_init/new-work-bootstrap.md` |
| 作品フォルダの構造を知る | `template/folder_structure.md` |
| 企画を作品に流し込む | `adapter/intake_adapter.md` |
| 1話書く | `adapter/writing_adapter.md` → `takt/workflows/draft-episode.yaml` |
| レビューを回す | `takt/workflows/review-multipass.yaml` |
| 整合性を検査する | `tools/ontology_check.py` |
| TAKTを理解する | `takt/README.md`（暫定） |
| 置換の根拠を読む | `../proposal/2026-07-06-workbench-ontology-loop/PROPOSAL.md` |
