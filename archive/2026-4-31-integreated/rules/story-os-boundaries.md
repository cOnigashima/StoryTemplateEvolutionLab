# Story OS Boundaries

Story OS に関わる作業では、次の境界を守る。

- 物語の入口は `story/seeds/`。`backlog/` は legacy 資産であり、正規 intake とはみなさない
- 正式語は `章束`。`packet` は実装語。`bundle` は使わない
- `micro` は `scenes + drafts + episodes` を指す。`reviews` は `meta` に置く
- `review` を単独で使わず、`typed review` と `approval review` を分ける
- `queue/` は projection であり、作品正本ではない
- `Story Board`、`Loop Canvas`、`Run Ledger` の数字は観測値であり、正本の代わりにしない
- 正本に迷ったら `story/promises.md`、`bible/*`、`arcs/`、`packets/`、`scenes/`、`drafts/`、`reviews/`、`learning/` を優先する


---

## v4 で追加された境界（2026-04-30）

- **作品固有 facet は generic 雛形に流入させない**: 三層対応 / 章末資料 / 批評性シート等は work bible に独立、`StoryTemplateEvolution/current/templates/` には積まない
- **Bible に Draft（本編 prose）を入れない**: drafts/ のみ。Sample Scene のみ `bible/samples/` に許容
- **adapter/ は leading dot なし**: `.adapter/` は v4 で禁止、`adapter/` を使う（人が編集する work-content 隣接の扱い）
- **proposals/ は単数形 `proposal/`**: 複数形は禁止
- **Premise (kernel #1) は deprecated**: `Logline` を使う
- **作品固有 facet の物理位置は同階層 + README で識別**: `bible/_custom/` のような prefix はつけない

詳細: `proposal/2026-04-30-zero-base-v4/02_domain_model.md` Section 14（Deprecated）
