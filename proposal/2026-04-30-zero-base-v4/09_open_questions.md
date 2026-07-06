# 09 Open Questions — 本提案で残された未決論点

> **役割**: 本提案 v4 を採用するうえで、現時点で author judgment が必要な未決論点を集約。
> **対象**: 採用判断の前に詰める論点 / 採用後 90 日以内に詰める論点 / 採用後随時詰める論点。

---

## 0. Open Question の分類

| 区分 | 意味 | 期限 |
|---|---|---|
| **Q-A** | 採用判断の前に詰めるべき | 採用前 |
| **Q-B** | 採用後 30 日以内に詰める | 30 日 |
| **Q-C** | 採用後 90 日以内に詰める | 90 日 |
| **Q-D** | 採用後、運用しながら随時詰める | 随時 |

---

## 1. 採用前に詰めるべき論点（Q-A）

> **✅ ALL RESOLVED (2026-04-30, v4 採用と同時に)**: Q-A 4 件すべて推し option A で確定。
> Q-A-001: kebab-case / Q-A-002: bible/plot.md デフォルト 1 ファイル / Q-A-003: Markdown headers / Q-A-004: 同階層配置 + README 識別

### Q-A-001: ディレクトリ命名の `kebab-case` vs `snake_case`

**論点**: v4 の generic 命名は kebab-case（`logline.md` `style-voice.md` `genre-overlay.md`）を採用したが、既存 work では `snake_case`（`renji_voice_catalog.md` `three_layer_principle.md`）が混在。
- **option A**: kebab-case で統一（v4 generic と整合、移行コスト発生）
- **option B**: 各 work に既存命名を許容（template は kebab、work は自由）
- **推し**: A（generic との整合性 + 探索性）
- **author 判断必要**

### Q-A-002: `bible/plot.md` 単一 vs `bible/plot/` ディレクトリのデフォルト

**論点**: 本提案では「デフォルト 1 ファイル、肥大時に分割」としたが、ia_society / fools-with-cheating の規模だと最初から分割したほうが運用が楽。
- **option A**: デフォルト 1 ファイル維持（小規模作品優先）
- **option B**: 規模 50 ep 以上は最初から `plot/` ディレクトリ
- **推し**: A（既存 file-growth.md ルール継承）
- **author 判断必要**

### Q-A-003: 二層ファイル形式の物理 separator

**論点**: Reveal Budget Sheet / Motif Ladder の二層ファイルで、Bible 部分と State 部分をどう物理的に区別するか。
- **option A**: `## === Section A: 設計意図（Bible 由来）===` と `## === Section B: 実装状況（State 由来）===` の Markdown headers
- **option B**: YAML front-matter で `bible_section:` `state_section:` を明示
- **option C**: 別ファイルにして、`reveal-budget.md` から両方を include
- **推し**: A（人間が読みやすい）
- **author 判断必要**

### Q-A-004: 作品固有 facet の物理配置パターン

**論点**: fools-with-cheating の三層対応 / 章末資料 / 批評性のような作品固有 facet は `bible/{custom-facet}/` に置くと決めたが、generic facet と同じ階層にあると見分けがつかない。
- **option A**: 同じ階層に置き、README で識別
- **option B**: `bible/_custom/` のような prefix で隔離
- **option C**: `bible/{work-slug}/` のような work-prefix
- **推し**: A（簡素、拡張容易）
- **author 判断必要**

---

## 2. 採用後 30 日以内に詰める論点（Q-B）

### Q-B-001: Intake Adapter prompt の v4 への書き直し範囲

**論点**: 既存 `adapter/intake_adapter_prompt.md` は v3 用に書かれているが、v4 では:
- 86 項目のチェックリストを参照する形にする
- output 形式に `intake_coverage_report` を含める
- `version: v4` を明示する

書き直しの範囲:
- **option A**: 既存 prompt の構造を維持し、参照と output だけ更新
- **option B**: 全面 rewrite して v4 仕様で書く
- **推し**: A（漸進的）
- 採用後の Patch lifecycle で実施

### Q-B-002: 旧 work（renji 等）の v4 移行優先度

> **✅ RESOLVED (2026-04-30)**: renji は archive 配下に物理ファイルが存在しないことが判明（`works/` ディレクトリは空）。実体は構想段階で存在しなかった。retrospective document `archive/2026-04-30-pre-v4/learning/2026-04-29-renji-pilot-retro.md` のみ残存。**追加作業不要**。option B（archive 維持、新作品から v4）相当で結着。

**論点**: renji（旧 pilot）も含めて 4 作品が v3 / v3-likes 状態。優先度は ia_society / ore_tueee / fools の 3 作品に置いたが、renji の扱いは:
- **option A**: renji も v4 に移行
- **option B**: renji は archive（旧 pilot として履歴に）、新作品から v4
- **option C**: renji は v3 のまま、移行は不要
- **結着**: archive にあり実体ファイルなしのため、何もしない

### Q-B-003: `craft/` の物理位置

**論点**: 03 で「`craft/` は StoryTemplate 共通、各 work には置かない」としたが、`StoryTemplateEvolution/current/craft/` は現状空に近い。整備計画:
- **option A**: 採用と同時に空のディレクトリ + README のみ作成
- **option B**: 各 work の `.claude/rules/` から共通要素を吸い上げて初期 craft/ を作る
- **option C**: 後追いで必要時に追加
- **推し**: B（既存資産活用）
- 30 日以内に作業

### Q-B-004: `adapter/` の generic と work-specific の sync

**論点**: 各 work の `adapter/` は generic を参照する形だが、generic 更新時の sync 機構が未定義。
- **option A**: work 側は git submodule で generic を参照
- **option B**: work 側は generic からの copy + override 差分のみ
- **option C**: work 側は何も置かず、必要時に StoryTemplate から手動 copy
- **推し**: B（運用上現実的、sync は自動化スクリプトで）
- 30 日以内に運用方針確定

---

## 3. 採用後 90 日以内に詰める論点（Q-C）

### Q-C-001: kernel.yaml の v3 → v4 自動 migration script

**論点**: kernel.yaml を v3 から v4 に変換する作業を:
- **option A**: 作品ごとに手動
- **option B**: yq + bash で自動 migration script 作成
- **option C**: LLM-driven migration prompt 作成
- **推し**: B + C（B で構造変換、C で値の妥当性チェック）
- 90 日以内

### Q-C-002: Intake Coverage の自動化レベル

**論点**: 86 項目チェックリストを毎回手動実行は重い。
- **option A**: `07_review_prompts/intake-coverage-review.md` を LLM に貼り付け実行（現状提案）
- **option B**: バッチスクリプトで bible 物理スキャン + LLM judge を自動化
- **option C**: 完全 CLI 化（`storytemplate audit --work=ia_society`）
- **推し**: A → B（段階的）
- 90 日以内に B 化を検討

### Q-C-003: 作品固有 facet を kernel.yaml で宣言する仕組み

**論点**: fools の三層対応のような作品固有 facet を kernel.yaml の `custom_facets:` で宣言すれば、Intake Coverage の対象に含められる。
- **option A**: kernel.yaml に `custom_facets: []` フィールドを追加
- **option B**: 別ファイル `bible/custom-facets.yaml` で宣言
- **option C**: 宣言不要、運用で識別
- **推し**: A（kernel との一体性）
- 90 日以内

### Q-C-004: Reverse Flow の機械化

**論点**: review で問題発見時、上流に戻す reverse flow は現状人間判断。
- **option A**: 各 review type の出力に `reverse_flow_target` フィールド必須化
- **option B**: review prompt 内で reverse flow 候補を必ず出力
- **option C**: 別 prompt（reverse-flow-router）を作る
- **推し**: A + B（軽量）
- 90 日以内

---

## 4. 随時詰める論点（Q-D）

### Q-D-001: status 11 値の運用妥当性

各 status 値が実運用で意味を持っているか、12 値以上が必要か、を 6 ヶ月運用後に評価。

### Q-D-002: card 書式の進化

8 フィールド書式が運用で過不足ないか。例えば「Status カラムを全 card に追加」「Severity フィールド追加」などの拡張要否を観察。

### Q-D-003: 17 facet の妥当性

17 facet が過不足ないか。ある facet が常に空、または別の facet が常に作品固有として独立している場合、generic 化を検討。

### Q-D-004: Backlog の構造

`backlog/{slug}.yaml` のフラット構造が運用で破綻しないか観察。
- 100 件超えたら何か仕組みが必要か
- channel フィールドで分類が必要か（`channel: writing | external | review`）

### Q-D-005: 二層ファイル運用の妥当性

Reveal Budget Sheet / Motif Ladder の二層ファイル運用が、書き手 / 読み手の両方で実用的か。**分離（Bible / State 別ファイル）に戻すべき場合もある**。

### Q-D-006: Walkthrough の活用度

`bible/walkthroughs/` が実際に使われるか。新セッション参加者が「README より walkthrough が役立った」場面が出るか観察。

### Q-D-007: 作品固有 facet のジャンル横断パターン

複数の異世界転生作品で「正当化圏」のような facet が再発見されたら、generic 化を検討。

---

## 5. 設計時に意図的に判断保留した論点

以下は議論したが「v4 では決めない」を選択した:

| 項目 | 保留理由 |
|---|---|
| **Layer R / TAKT 連携** | opt-in 方針、必要な作品で個別判断 |
| **多言語対応** | 日本語作品中心、英語化は需要発生時 |
| **Skill / Agent の統一仕様** | `.claude/agents/` `.claude/skills/` は work 自由、template 化は時期尚早 |
| **AI 生成本文の比率管理** | `kakuyomu-policy.md` の「AI 本文利用」タグ運用で当面 OK |
| **公開後の prose 改訂運用** | Patch lifecycle は bible 改訂用、prose 改訂は別運用（要設計） |
| **Series（複数 Manuscript）の管理** | 1 Manuscript = 1 work で当面 OK |
| **Spinoff / 外伝の扱い** | `design/spinoff-candidates.md` で当面 OK |

---

## 6. Open Question の昇格・解決

各 Open Question は次のライフサイクルを経る:

```
Q-X-XXX 起票
   ↓
[author 検討]
   ↓
- 解決 → Decision Log に append + 該当ファイル更新
- 採用見送り → Rejected Idea に append
- 引き続き保留 → 期限延長
- 大型化 → Canon Patch Proposal に昇格
```

本提案採用後、各 Q を `design/open-questions.md` に転記して継続管理。

---

## 7. 不変条件

1. **Q-A は採用判断の前に必ず author confirm**
2. **Q-B / Q-C / Q-D は採用と並行して詰める** — 採用ブロッカーにしない
3. **Open Question を勝手に解決しない** — Adapter / drafter が独断で決めない
4. **解決時は必ず Decision Log に記録** — 後から「なぜそう決めたか」を遡れるように
5. **保留しすぎない** — 90 日以内に Q-C は判断、それ以上は Q-D に降格
