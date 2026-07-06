# 設計原則: 「必要なこと」をいつ・どう機能させるか

> 議論の出発点: 「それぞれを立ち上げる時に必要なことは?」という場面でテンプレがちゃんと機能してほしい。READMEだけでいけるのか?
> 結論: **READMEだけでは機能しない**。READMEは pull 型で、「読むべきだと思い出す」こと自体に失敗するため。

## 1. 信頼性の3層

情報を届ける仕組みには信頼性の階層がある。

| 層 | 型 | 実体 | 機能する条件 | 向くもの |
|---|---|---|---|---|
| ① ドキュメント | pull（読みに行く） | README / 56語Card / folder_structure / docs/ | 読者が読むと決めた時のみ | 背景・全体像・「理解したい人」向けの説明 |
| ② ハーネス注入 | push（勝手に入る） | CLAUDE.md・rules（常時）/ skill description（発話マッチで浮上）/ skill 本文（起動時） | ハーネスに正しく載っていること。**容量は有限** | その時点の作業に効くべき要点・想起 |
| ③ 実行可能チェック | enforce（読まなくても止まる） | ontology_check / skill 冒頭の前提検査 / status 集計 | スクリプトが走ること | 保証したい前提条件・ゲート |

### 割り当て原則

**「必要なこと」は一つずつ、①説明したいのか・②想起させたいのか・③保証したいのか、を割り当てる。**

- 保証したいものを README に置くのは設計ミス（読まれない）
- 背景説明を rules に置くのも設計ミス（常時読込のコンテキストを圧迫する）
- ②は小さく保つ。CLAUDE.md / rules に入れてよいのは「執筆中いつでも効くべき要点」だけ。詳細は①へリンク、保証は③へ委譲

## 2. 「何が足りないか」は文書でなく問い合わせで出す

本テンプレは既に「全 field に status 12値・空欄禁止」を敷いている。したがって
**立ち上げ（や各工程）に何が足りないかは、人が思い出すものではなく state から生成できる**:

- `missing` / `needs_author_decision` / `tentative` の集計 = DoR 充足度の計算
- これがオントロジーを敷いた最大の配当。「必要なことリスト」の正本はチェックリスト文書ではなく **status の集計結果**

実装: `tools/ontology_check.py` に **DoR-A モード**を追加（`--dor-a` 等）。機械判定可能な項目はスクリプト化し、チェックリスト文書に残すのは機械判定できない項目（作者の納得感・promise の魅力等）だけにする。

## 3. skill 冒頭の DoR 自己検査（preflight 規約）

**各 skill は冒頭で自分の前提（DoR）を検査し、満たさなければ作業せず「不足リスト」を返す。**
これで README を読んでいない人・AI にもテンプレが機能する。

| skill | 冒頭で検査する前提（例） |
|---|---|
| new-work | 置き場所・slug の重複、current のバージョン |
| pitch | kernel.yaml の存在（なければ kernel から） |
| draft | frozen packet / Writing Pack の存在、`missing` が閾値以下 |
| critic / continuity | 対象 draft の存在、state/ が読めること |
| review-meeting | review 対象と観点票フォーマットの存在 |
| release | 12項目のうち機械化できる分の自動検査 → 残りを人間へ提示 |
| retro-meeting | 対象 run ログ / learning 出力先の存在 |
| handoff | 直近 run・OPEN 項目の収集可能性 |

この規約は `01_design_harness.md` の SKILL.md 変換規則に **規則5** として追加する:
「本文の最初のセクションは `## Preflight`。前提が欠ける場合はそこで停止し、不足を status 集計付きで報告する」

## 4. 「次の一手」ポインタ

READMEの目次(全体地図)ではなく、**今いる場所からの一歩だけ**を各成果物の末尾に置く。

- kernel.yaml を埋め終えた → 「次: bible の Logline / Promise から。/pitch が使える」
- bible DoR-A 充足 → 「次: overlay の unit 準備。/draft の前提はこれ」
- draft 完了 → 「次: /critic → /review-meeting」

実装: 各テンプレファイル（kernel.template.yaml・facet テンプレ・checklists）の末尾に `next:` 行を1行追加する。CLAUDE.md 雛形の「作業の入口」節とループが閉じる。

## 5. 本原則の既存設計への反映

| 反映先 | 内容 |
|---|---|
| 01_design_harness.md | SKILL.md 変換規則に規則5（Preflight 必須）を追加 |
| 02_design_reference.md | harness_map §1 に「①②③どの層で機能するか」列を追加。README 追記は①の役割に限定 |
| 03_design_lifecycle.md | `/new-work` を対話プロトコルとして明記（質問→複製→チェック→不足リスト自動生成→G-Intake 停止）。人は事前に「何が必要か」を知らなくてよい |
| Phase 3（PROPOSAL §3） | ontology_check の DoR-A モード追加をスコープに含める。dor_dod 一本化（TODO #2）は「機械判定分をスクリプトへ、残りを文書へ」の分割として実施 |

## 6. 判定基準（この原則が機能しているか）

新しい「必要なこと」が生まれた時に、次の問いで置き場所が即決できること:

1. 読まれなくても困らない説明か → ①docs/README
2. 作業中に思い出させたいか → ②description / rules（小さく）
3. 破られたら困る前提か → ③preflight / ontology_check

迷ったら③に寄せる（保証が最も安い層に落ちるのを防ぐ）。
