# Open Questions v3

> **目的**: 本 v3 で意図的に決めなかった論点を一覧化する。pilot で discover する前提のもの・次セッションで詰めるもの・author 判断待ちを区別する。
> **ガチガチ度**: ガチガチに「決めない」と決める対象。判断を未来に押し出すための明示リスト。
> **昇格**: pilot で答えが出たら本 v3 の該当ファイルに反映する。

---

## 1. 区別軸

| 種別 | 意味 | 解決手段 |
|---|---|---|
| **Pilot Discover** | 新規作品 pilot を回せば自然に答えが見える | pilot 実走 → Retro |
| **Next Session Design** | 設計を続ければ答えが出る。次セッションで詰める | 次セッション内 design |
| **Author Decision** | author の好み・方針判断が必要 | author 判断待ち |
| **External Dependency** | 外部要因待ち（TAKT 仕様変更 / カクヨム規約変更 等） | 待つ |

---

## 2. Pilot Discover（Pilot で答えを取る）

### PD-01. kernel 11 項目で本当に十分か

**論点**: 薄い kernel として 11 項目を確定したが、新規作品 pilot で「これが kernel に無いと困る」項目が見つかるか。

**discover 方法**: 新規作品 bootstrap を回して、DoR-A を満たそうとする中で「kernel に無いが必要」項目を記録する。

**昇格先**: 答えが出たら `04_kernel_spec.md` の §2 を更新。

---

### PD-02. cadence 6:4 比率は genre 不問で機能するか

**論点**: kernel.emotional_arc.cadence_baseline.tension_to_release_ratio を `6:4` で baseline にしたが、これは Pack A で villainess-coc 由来の値。新規作品（別ジャンル）でも妥当か。

**discover 方法**: pilot 作品を 5 episode 程度書き、Persona Review C（離脱読者）に「テンポはどうか」を問う。

**昇格先**: ジャンル別 baseline が必要なら `craft/cadence.md` に派生表を作成。

---

### PD-03. Episode 1 本のサイズ目安 1500〜5000 字 は妥当か

**論点**: `02_unit_taxonomy.md` §2.5 の Episode サイズ目安は kakuyomu 想定。新規作品の文体・ジャンルで適正値が変わる可能性。

**discover 方法**: pilot Episode を実際に書いてみて、「1 話として読者に届く感」のサイズを測る。

**昇格先**: 作品ごとの style_voice / project_override に記録。template 側は維持。

---

### PD-04. 3 writer persona（faithful / emotional / plot-drive）で多様性が出るか

**論点**: Pack B P0-10 で初期は 3 writer persona と決めたが、3 案で実際に多様性が出るか pilot 実証が必要。

**discover 方法**: pilot Episode 1 本で 3 candidate を生成 → diversity を author が評価。

**昇格先**: 答えが No なら writer 増設 or persona 再設計。`prompts/personas/` を更新。

---

### PD-05. selection-synthesis の borrow ルール「最大 3 要素」は妥当か

**論点**: Pack B 11_risks_and_considerations.md で「borrow elements は最大 3」と決めたが、実走未検証。

**discover 方法**: pilot で synthesis を回して、3 個で足りるか / 多すぎないか確認。

**昇格先**: `prompts/selection-synthesis-prompt.md`（次セッション作成）に反映。

---

### PD-06. Judge auto_fix_allowed の境界

**論点**: 何までを auto_fix_allowed にし、何から NEEDS_HUMAN にするかの境界線。

**discover 方法**: pilot で Judge を回し、NEEDS_HUMAN が多すぎたり少なすぎたりしないかを観測。

**昇格先**: acceptance_contract のテンプレに反映。次セッションで Adapter 設計時に確定。

---

### PD-07. ledger 更新粒度

**論点**: ledger をどこまで詳細に更新するか。Pack B 11_risks の「ledger 肥大化」と「ledger 不足」のバランス。

**discover 方法**: pilot 5 episode で ledger を運用 → 「過剰 / 不足 / ちょうど良い」の感覚を author に問う。

**昇格先**: `ledger/README.md` に運用基準として明記。

---

### PD-08. Continuity Review の頻度

**論点**: Continuity Review を Episode ごと / Packet ごと / Arc ごと どの頻度で回すか。

**discover 方法**: pilot で各頻度を試す。Episode 単位だと過剰、Arc 単位だと遅すぎ、を経験で測る。

**昇格先**: `04-review-system.md`（Pack A）に作品別運用例として追記。

---

### PD-09. Pilot 作品の genre 影響

**論点**: 新規 pilot 作品の genre（romance / mystery / thriller / 文芸 / etc.）によって、必要な genre_overlay や framework_lens が変わる。

**discover 方法**: pilot 作品 genre 確定 → 必要な overlay / lens を選定 → 実走 → 過不足を測る。

**昇格先**: `craft/genre-overlays/` に第 1 例として保存。

---

### PD-10. Adapter の介在頻度

**論点**: Adapter は Episode ごとに毎回回すか、Packet 確定時に一括で回すか。

**discover 方法**: pilot で両方試す。

**昇格先**: 次セッションの Adapter 設計に反映。

---

## 3. Next Session Design（次セッションで詰める）

### NSD-01. Adapter の実装詳細

**論点**: `01_vocabulary.md` `03_layer_facet_map.md` で Adapter は Layer 1.5 に置くと決めたが、実装の step-by-step（入力受付 / status 判定 / lens 選択 / scene_card 生成 / contract 生成）は未確定。

**詰め方**: Pack B `07_adapter_design.md` を踏まえ、TAKT step として再設計。

**成果物予定**: `2026-XX-XX-adapter-design/` 配下に Adapter 仕様 + scene_card.schema.yaml + acceptance_contract.schema.yaml。

---

### NSD-02. TAKT workflow YAML の中身

**論点**: episode-draft-tournament.yaml / packet-assembly-review.yaml / arc-strategy-tournament.yaml 等を実装可能な YAML に落とす。

**詰め方**: TAKT `docs/README.ja.md` の構文で書き、parallel step / routing rule を活用。

**成果物予定**: `.takt/workflows/*.yaml` を新規作品 repo に配置。

---

### NSD-03. Persona Markdown の中身

**論点**: faithful_writer / emotional_writer / plot-drive_writer / dialogue_writer / risky_writer / reviser / judge / ledger-keeper / persona-A/B/C reviewer の各 markdown 本文。

**詰め方**: それぞれの役割 × 入出力 × 守るべき MUST / SHOULD を 1 ページに圧縮。

**成果物予定**: `.takt/facets/personas/*.md`。

---

### NSD-04. craft/ の個別ファイル本文

**論点**: Pack A v2 で目次（21 ファイル）は決めたが、個別 craft ファイルの本文は未着手。

**詰め方**: principles.md / scene-sequel.md / want-need.md / scope-management.md / cadence.md / beat-sheets.md / reveal-plan.md / foreshadowing.md / motif-operations.md / dialogue-craft.md / description-craft.md / pov-craft.md / conflict-design.md / world-design.md / theme-design.md / genre-patterns.md / editing-craft.md / sanderson-laws.md / knox-rules.md / rubric.md / reader-personas.md。

**成果物予定**: `craft/*.md` を順次。pilot で必要になったものから優先。

---

### NSD-05. .claude/rules/ への追加 3 本

**論点**: Pack A v2 で intake-flow.md / review-system.md / vocabulary-lint.md を追加すると決めた。本 v3 ではまだ template 本体に統合していない。

**詰め方**: 本 v3 と整合させてから template 本体に統合。

**成果物予定**: `story-template/.claude/rules/intake-flow.md` `review-system.md` `vocabulary-lint.md`。

---

### NSD-06. story-os-boundaries.md の更新

**論点**: 本 v3 で Layer 1.5 / Ledger / Adapter / Framework Index 等を新設したが、`.claude/rules/story-os-boundaries.md` には反映していない。

**詰め方**: boundary 追記。

**成果物予定**: `story-template/.claude/rules/story-os-boundaries.md` v2。

---

### NSD-07. CLAUDE.md の更新

**論点**: 本 v3 の語彙・kernel・layer に整合する CLAUDE.md。

**詰め方**: Pack A v2 と本 v3 を踏まえて template の CLAUDE.md を更新。

**成果物予定**: `story-template/CLAUDE.md` v2。

---

### NSD-08. Adapter input から output への変換ルール仕様

**論点**: domain_synthesis + storya_kernel + framework_lens_selection + project_design + ledger → scene_card + acceptance_contract への変換アルゴリズム。

**詰め方**: 入力フィールドごとに、どの出力フィールドにどう写像するかをマッピング表で固定。

**成果物予定**: `adapter_mapping_rules.yaml`。

---

### NSD-09. typed_review template v2 上書き本文

**論点**: Pack A v2 で typed-review-template の v2 化（PART A-G 全 7 セクション）を計画したが、本文は未生成。

**詰め方**: PART A〜G の各セクションテンプレを本文化。

**成果物予定**: `reviews/typed-review-template-v2.md`。

---

### NSD-10. Repertoire パッケージ化

**論点**: TAKT `repertoire add` で Story Template を配布パッケージにできる。これを実装するか。

**詰め方**: Story Template repo に repertoire manifest を追加。

**成果物予定**: `.takt/repertoire-manifest.yaml`。

---

## 4. Author Decision（author 判断待ち）

### AD-01. Pilot 作品の genre

**論点**: 新規 pilot 作品の genre をどれにするか。

**選択肢例**:
- ライトノベル（異世界転生 / 学園 / バトル / etc.）
- 文芸（純文学・現代文学）
- ミステリ（本格 / ハードボイルド / コージー）
- ホラー
- SF（ハード / スペオペ / サイバーパンク）
- ロマンス
- 短編複合（ジャンルレス）

**影響**: kernel の style_voice / genre_overlay / framework_lens の選択に直結。

---

### AD-02. Pilot 作品のスケール

**論点**: 短編 / 中編 / 長編 のどれを試すか。

**選択肢例**:
- 短編 1〜3 episode（end-to-end 検証だけ）
- 中編 1 packet（10 episode 前後、packet-assembly まで通す）
- 長編想定 1 arc（30 episode 前後、arc-through-review まで）

**影響**: bootstrap 時の unit_tree 設計、必要な workflow 数。

---

### AD-03. Pilot で writer persona を何種類にするか

**論点**: 3 / 4 / 5 のどれで始めるか。

**Pack B 推奨**: 3（faithful / emotional / plot-drive）。risky / dialogue は P1 で追加。

**author 確認事項**: pilot で 3 から始めて足りなければ追加、で OK か。

---

### AD-04. Pilot 作品のディレクトリ位置

**論点**: 新規作品をどこに置くか。

**選択肢例**:
- `works/pilot-001-{slug}/`（既存 works/ 配下）
- `works/{slug}/`（pilot ラベル無し、本気の新作品扱い）
- `pilot-works/{slug}/`（pilot 専用ディレクトリ新設）

**影響**: ディレクトリ命名規約。

---

### AD-05. Pilot 作品の executable depth

**論点**: pilot で「実際にカクヨム公開まで通す」か「DoD-E まで通すが公開しない」か。

**影響**: kakuyomu_policy MUST 項目を実走するかしないか。

---

### AD-06. fat-by-design の上限

**論点**: 「Layer 2/3 は太く」と決めたが、無限に太らせるわけではない。どこで止めるか。

**選択肢例**:
- pilot で必要になったものだけ追加（pilot-driven）
- next session で craft/* を 21 全部書く（comprehensive）
- 中庸（principles.md + scene-sequel.md + want-need.md + rubric.md + reader-personas.md の 5 本だけ先に書く）

**影響**: Phase 計画の容量。

---

### AD-07. .takt/ 採用するか / 別実装にするか

**論点**: TAKT を採用すると決めたが、TAKT の OAuth / API key / provider 制約が問題になる場合、別実装（Cowork session 内手動実行 / Python script 実装 等）も選択肢。

**author 確認事項**: TAKT を導入してよいか、それとも当面手動運用で進めるか。

---

### AD-08. 既存 works/ の作品を pilot に転用するか

**論点**: 「新規作品でやる」と決めたが、既存 works/ の sample-story を再起動する選択もあり得る。

**author 再確認**: 完全新規 vs sample-story 再起動 vs 既存 seed 復活 のどれか。

---

## 5. External Dependency（外部要因待ち）

### ED-01. TAKT のバージョン更新

**論点**: TAKT のバージョン更新で workflow yaml の構文が変わる可能性。

**対処**: 採用時点のバージョン pin。バージョン更新時は migration 計画。

---

### ED-02. カクヨムの AI タグ規約変更

**論点**: 2025/11 制定の AI タグ運用が変わる可能性。

**対処**: `.claude/rules/kakuyomu-policy.md` を定期確認。

---

### ED-03. Anthropic / OpenAI 等 provider のモデル更新

**論点**: model 更新で persona の挙動が変わる可能性。

**対処**: pilot Retro で provider/model 別の傾向を記録。

---

### ED-04. カクヨムコン等コンテストの AI 利用規約

**論点**: コンテスト応募時の AI 利用条件はコンテストごと。

**対処**: 応募予定があるたびに要項確認。

---

## 6. 本 v3 で意図的に決めなかった「やらないこと」

Pack B `12_not_now_list.md` を継承し、本 v3 でも「今やらない」リストを維持:

- 全創作理論の deep research
- 最強 Story Template 完全版
- 全ジャンル対応
- 全 workflow の TAKT 完全実装
- Arc / Part / Manuscript までの完全自動化
- 1000 タスクの完全整理
- 大量 reviewer の導入
- 精密スコアリング体系

これらは pilot 後 / works が増えた後 / template が安定した後 に再検討。

---

## 7. open_questions の運用

- 新しい論点が出たら即追記
- pilot で答えが出たら、本 v3 該当ファイルに反映 + 該当項目を「解決済」とマーク
- 次セッションで設計したら NSD を「解決済」に
- author 判断が出たら AD を「解決済」に
- 解決済項目は削除せず、`## 9. 解決済アーカイブ` に移動

---

## 8. v3 リリース時の open_questions snapshot

- Pilot Discover: 10 件（PD-01 〜 PD-10）
- Next Session Design: 10 件（NSD-01 〜 NSD-10）
- Author Decision: 8 件（AD-01 〜 AD-08）
- External Dependency: 4 件（ED-01 〜 ED-04）

合計 32 件。これが v3 リリース時の「未決」スナップショット。

---

## 9. 解決済アーカイブ

（pilot や次セッションで解決した項目をここに移動）

現時点: なし（v3 リリース直後）。
