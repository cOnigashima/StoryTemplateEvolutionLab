# folder_structure — 作品フォルダの完全な構造

current/template/ をコピーして作った作品(work)が持つべきフォルダの正本定義。
（origin: STE-v4 の storage_trinity + fools/villainess の実走構造を統合）

## 作品フォルダの全体像

```
works/{slug}/                      # ← 外部フォルダ（current の外）
├── work.manifest.json             # 構造宣言（overlay・逸脱・kakuyomu設定）
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
        ├── sessions/              #   セッションダイジェスト
        └── learning/             #   作品固有の retro 全記録。汎用に効く知見は抽出して STE の improvement_request_inbox/ へ投入（→ 検討 → current 反映 → STE 側 current/learning/ に決着記録）
```

## 原則
- **core は必須**。overlay は1つ以上宣言。runtime は空で始まり実走で埋まる。
- 作品固有の装置（CoC卓ルール等）は `work-local/` を作ってそこに置く（core に混ぜない）。
- どこに何を書くか迷ったら `../../CLAUDE.md`（大原則）と `core/rules/reverse-flow.md`（遡上先）を見る。
