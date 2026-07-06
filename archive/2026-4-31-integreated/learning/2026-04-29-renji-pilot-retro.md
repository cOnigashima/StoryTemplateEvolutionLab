# Renji Pilot Retro

> **種別**: 方法論 + author フィードバック
> **日付**: 2026-04-29
> **関連ファイル**: 本セッションで作成した 70+ ファイル全部
> **深刻度**: 中（手戻り発生しつつも収束）

---

## 何が起きたか

朝から夕方までの 1 日セッションで、StoryTemplate 改善 + 新規作品 (renji) ingest + 執筆環境整備を試みた。

時系列:

1. **朝**: 旧 story-template (v1 / 空骨) の改善案として v2-fat（重装備設計、Layer 0-4+R / Review Matrix 7 種 / 25 項目 rubric）を作成。9 docs + 28 skeleton。
2. **午前**: 別セッションで生成された storytemplate_workflow_handoff_pack（kernel 薄 / Adapter / Judge / Ledger 軸）を発見。13 docs。v2-fat と方向性が衝突。
3. **午前後半**: v3-kernel として両者を統合（語彙統一・kernel 11 項目・DoR/DoD）。10 docs。
4. **午後**: author から方向修正。「v3 はまだ抽象的、もっと fat でよい」「Adapter で受け入れる体制が先」「TAKT を調べて」「新規作品でやる」。
5. **午後**: renji_novel_bible（35 既存ファイル / 750KB / 完成度高い作品設計）が pilot 対象として登場。
6. **午後**: works/renji/.adapter/ 7 docs + ep001 Writing Pack 4 ファイル作成。
7. **夕方**: 「StoryTemplate 充実 → Adapter で受け入れ → TAKT で執筆」というユーザーのメンタルモデルとの逆走に気づく。
8. **夕方**: StoryTemplateEvolution として新ディレクトリで再構築。renji Phase A 実体化 + template skeleton 並行生成 + ep001 Writing Pack 更新。

---

## なぜ起きたか（根本原因）

### 1. 設計優先病

設計書を 3 つ作る間（v2-fat / v3-kernel + handoff の統合）に、**実物を 1 つも作っていなかった**。設計が膨らむほど、author からは「で、何が動くの?」と見えにくくなる。

設計と実物の比率が 100:0 になっていた。

### 2. ユーザーのメンタルモデルを後回しにした

ユーザーは最初から「Story Template 充実 → Adapter で受け入れ → 執筆」と言っていた。私は最初の「Story Template 充実」を **設計議論で済ませて** 実体化を後回しにした。

実は「Story Template 充実」は **実体ファイルが揃った状態** を指していた。

### 3. fat-by-design 指示を文字通り取りすぎた

「コンテキスト・ハーネスエンジニアリングっぽいこと」という指示を「設計書を厚く書く」と解釈した。実際は「実装を厚く揃える」が正しかった。

### 4. renji_novel_bible の存在を知らずに設計した

セッション後半まで renji_novel_bible（既に作品設計が完成しているもの）の存在を知らなかった。これがあれば最初から **実物 ingest 中心** に進められた。

---

## どうやるべきだったか（正しい手順）

### 最初の 30 分でやるべきだったこと

1. **既存資産の棚卸し** を最優先
   - story-template/ 本体の現状確認
   - works/ 配下の既存作品の確認
   - 既存設計資料（renji_novel_bible のような）の有無確認
2. **ユーザーのメンタルモデルを正確に握る**
   - 「Story Template 充実」が「設計書」なのか「実体ファイル」なのか確認
3. **設計と実物の比率を 30:70 に保つ**
   - 設計を書きながら、対応する実物も作る

### 設計を作る場面でも

1. **1 ファイルの設計書ごとに、対応する 1 件の実体ファイル** を作る規律
2. 「これは 30 分で実例を作れるか?」を毎回問う
3. 実例が作れない設計書は捨てる or 保留

---

## 実際にやった対処

### 軌道修正（午後）

1. v3-kernel を発見的に作って失敗を認識（「もっと fat でよい」）
2. renji_novel_bible を発見、pilot 対象として採用
3. works/renji/.adapter/ で実物 7 docs を作る（ようやく実装着手）
4. ep001 Writing Pack で具体的な執筆準備を作る

### StoryTemplateEvolution への再構築（夕方）

1. v1 / 提案 3 Pack はそのまま温存（足跡）
2. 新ディレクトリで v2 を **実物中心** に構築
3. renji bible 実体化と template skeleton 抽出を並行
4. ep001 Writing Pack を realized bible に更新

---

## 根本対応（再発防止策）

### Rule 化候補

`StoryTemplateEvolution/rules/` に追加候補:

- **「設計書 1 つに実例 1 つ」ルール**: 設計書を書くたびに、その設計を実装した実例を 1 つ作る
- **「30 分実例ルール」**: 30 分以内に実例が作れない設計は捨てる or 保留
- **「メンタルモデル確認ルール」**: セッション開始時にユーザーが想像する完成形を 3 行で書き起こさせる
- **「既存資産棚卸しルール」**: 設計を書く前に、関連する既存資産を必ず棚卸しする

### Workflow 改良

- 各セッション開始時の最初の 5 分: 既存資産棚卸し + ユーザーメンタルモデル確認
- 設計書作成時: 各セクションに「対応する実例ファイルパス」を必須化
- セッション中盤: 「設計と実物の比率」を確認

### 横展開

このパターンは **renji 以外の作品** でも、また **renji 以外のドメイン**（コード設計、企画書など）でも起きる。

「設計優先病」の汎用対策として:
- 抽象化は実走後にのみ可能（事前抽象化は仮説）
- 1 例は無 / 2 例で抽象化検討 / 3 例で抽象化決定
- 1 例で template 化したものは「仮 template」と明記

---

## 横展開チェック

似た構造の問題が起きうる場面:

- 別作品の bootstrap 時 → 本セッションの learning から「設計より実物」を継承する
- 別ドメインのドキュメント整備時 → 同上
- TAKT 採用判断時 → 「TAKT 仕様を網羅理解」してから着手するのではなく、「TAKT で 1 タスク回す」ところから着手する

既存の story-template / works / 提案フォルダで、同種の「設計過剰・実装不足」がないかチェック:

- ✗ story-template/ 本体（CLAUDE.md と .claude/rules/ のみ、bible/arcs/packets 等の実体なし）
- ✗ proposals/ 3 Pack（設計のみ、template 本体への統合なし）
- ✓ works/renji/（v8 として実物完成度高い、本セッションで Phase A bible 化）
- ✓ StoryTemplateEvolution/（本セッションで実物中心に構築）

---

## 学び: pilot-driven extraction

本セッションで発見した方法論。「設計を先に作って、後から実例で検証する」ではなく、「実例を作りながら、共通パターンを抽出して template にする」。

具体手順:
1. 1 つの作品（pilot）の bible / design / state を実体化する
2. 各実体ファイルを作りながら、「他作品でも使う構造」を別ファイルとして同時に書く
3. 1 度の作業で実物 + template 抽出 を両方産出
4. 作品固有のもの（renji の三層対応 等）は template 化しない、と明確に判断

これが本セッション後半の StoryTemplateEvolution 構築で機能した。

詳細: `StoryTemplateEvolution/learning/2026-04-29-template-extraction-method.md`
