# folder_structure — 作品フォルダの完全な構造

current/template/ をコピーして作った作品(work)が持つべきフォルダの正本定義。
（origin: STE-v4 の storage_trinity + fools/villainess の実走構造を統合。inbox/synthesis は 2026-07-06 に v4 から復活）

## 作品フォルダの全体像

```
works/{slug}/                      # ← 外部フォルダ（current の外）
├── work.manifest.json             # 構造宣言（overlay・逸脱・kakuyomu設定）
│
├── inbox/                         # ★raw 受付箱（加工せずそのまま置く。raw はここで止まる）
│   ├── planning_sessions/         #   企画チャットのログ・外部生成 bible パッケージ
│   └── fragments/                 #   断片メモ
│
├── synthesis/                     # ★Intake Adapter の中間生成物
│   ├── session_digests/           #   raw を整理したダイジェスト（読み物）
│   └── update_proposals/          #   bible への反映指示書（G-Intake の承認対象）
│
├── core/                          # 全作品共通（template/core のコピー）
│   ├── kernel.yaml                # 芯11項目（template を埋めたもの）
│   ├── bible/                     # frozen設計（facet実体）
│   ├── design/                    # 揺れる設計（open-questions / canon-patch-proposals / design-debt）
│   ├── state/                     # ★動的事実＝オントロジー
│   │   ├── entities.yaml          #   Character/Location/Item/Faction
│   │   ├── knowledge_state.yaml   #   誰がいつ何を知っているか（KNOWS辺）
│   │   ├── foreshadowing.yaml     #   伏線 setup→payoff
│   │   └── timeline.yaml          #   出来事・因果
│   ├── checklists/                # DoR/DoD・acceptance
│   ├── rules/                     # preflight・review-gate・kakuyomu-policy・reverse-flow
│   └── schema/                    # entity_schema・relations（validator が参照）
│
├── (overlay 展開)                 # manifest で選んだ overlay の構造
│   ├─ unit-episode-pack の場合:   writing/episode_packs/{ep}/（4ファイル）
│   └─ unit-packet-2stage の場合:  packets/{exploring..published}/ , scenes/{seed,slotted,drafted,merged}/
│
└── runtime/                       # ★作業ログ・成果物（作品側で生まれる）
    ├── drafts/                    #   本文候補
    ├── reviews/                   #   レビュー票（採否判定付き）
    ├── approved/                  #   承認済み
    ├── published/                 #   公開済み
    ├── reader-export/             #   公開用テキスト（製作メタ除去。iPad Viewer 用）
    └── logs/
        ├── runs/                  #   TAKT実行ログ
        ├── sessions/              #   セッション実行ログ（handoff 等。※intake の digest は synthesis/ へ）
        └── learning/              #   作品固有の retro 全記録。汎用に効く知見は抽出して STE の improvement_request_inbox/ へ投入（→ 検討 → current 反映 → STE 側 current/learning/ に決着記録）
```

## データの流れ（三本柱の入口から出口まで）

```
inbox/（raw）→ [intake_adapter] → synthesis/（digest + update_proposal）
  → [G-Intake 人間承認] → core/{bible,design,state} に反映
  → [writing_adapter が1話分に圧縮] → (overlay の writing 構造)
  → [draft ループ] → runtime/drafts → reviews → approved → published
```

## 原則

- **core は必須**。overlay は1つ以上宣言。inbox / synthesis / runtime は空で始まり実走で埋まる。
- **raw は inbox で止まる**。bible への反映は必ず synthesis/update_proposals + G-Intake 経由。
- 作品固有の装置（CoC卓ルール等）は `work-local/` を作ってそこに置く（core に混ぜない）。
- どこに何を書くか迷ったら `../../CLAUDE.md`（大原則）と `core/rules/reverse-flow.md`（遡上先）を見る。
