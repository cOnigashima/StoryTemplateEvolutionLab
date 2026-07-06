# renji 固有として残置したもの

> 抽象化せず、renji 専用として `works/renji/` 内に残したもの。

---

## 1. 三層構造（真実 / レンジ認識 / 公的記録）

**renji 固有度**: 極めて高い

**残置場所**:
- `works/renji/bible/world/three_layer_principle.md`（原理）
- `works/renji/bible/plot/three_layer_table.md`（99 件マスター、未作成・renji_novel_bible/14 直参照）
- `works/renji/state/three_layer_status.yaml`（動的 status）

**なぜ template 化しないか**:
- 「真実 / 主人公認識 / 公的記録」の三層は renji の中核装置
- 他作品で同じ三層構造を採用する確率は低い
- 二層・四層・別軸の作品も多い（一人称信頼性・伏線層・etc.）
- 抽象化すると「N 層対応構造」となり generic すぎて実用性がない

**他作品での扱い方**: 採用したい作品が出たら、その作品の `bible/world/` に直接コピーして使う。template には積まない。

---

## 2. 正当化圏 / 認知整合 / 絶対時間（能力名）

**renji 固有度**: 完全に固有

**残置場所**: `works/renji/bible/world/ability_seitouka_ken.md`

**なぜ template 化しないか**:
- レンジ専用の能力概念
- 他作品の能力 / チート / 仕組みは別物
- 「主人公の自己正当化に世界が辻褄を合わせる」という具体的な仕組みは renji に固有

**他作品での扱い方**: どの作品も独自の世界ルール / 能力を持つ。bible/world/ に作品固有のファイルを作る。

---

## 3. レンジ語（口癖・自己正当化のパターン）

**renji 固有度**: 完全に固有

**残置場所**: `works/renji/bible/characters/protagonist_renji.md`（一部）

**なぜ template 化しないか**:
- 各作品の主人公の声は固有
- 「枝葉をつつくやつは本質が見えてない」のような口癖は他キャラには使えない

**他作品での扱い方**: protagonist.template.md の構造を使い、中身は各作品固有で埋める。

---

## 4. 章末公文書の type カタログ

**renji 固有度**: 中程度（半分は作品依存）

**部分的残置**:
- `works/renji/bible/in_world_documents/samples.md`（renji 固有のサンプル）
- `StoryTemplateEvolution/templates/bible/in_world_documents/samples.template.md`（構造のみ汎用化）

**なぜ部分残置か**:
- 章末資料を使う発想は他作品でも採用可（template 化）
- 個別 type（評価票 / 戦功審査議事録 等）は renji 固有

**他作品での扱い方**: template 構造を使い、type は作品ごとに定義。

---

## 5. 6 アーク構造（責任 → 言葉 → 関係 → 告発 → 死 → 歴史）

**renji 固有度**: 高い

**残置場所**: `works/renji/bible/plot/arc_map.md`

**なぜ template 化しないか**:
- アーク数（6）と「壊すもの」の連鎖は renji 固有のテーマ深化構造
- 他作品は別のアーク数 / 別のテーマ深化を持つ

**他作品での扱い方**: arc_map.template.md の構造（アーク表 / 階段 / 各アーク詳細）を使い、中身は作品固有。

---

## 6. 重要な作劇ルール 7 項目（renji 版）

**renji 固有度**: 中程度

**部分残置**:
- 個別 7 ルール（レンジを賢くしない 等）→ `works/renji/design/project_principles.md`
- 「作劇ルールという概念 + 形式」→ `StoryTemplateEvolution/checklists/work_dramatic_principles.template.md`

**なぜ部分残置か**:
- 「作品ごとに 5〜10 件の作劇ルールを置く」発想は汎用化できる（template 化）
- 個別ルールは renji 固有（他作品で同じ 7 ルールを採用するとは限らない）

**他作品での扱い方**: template 形式を使って、各作品で固有の作劇ルールを定義。

---

## 7. 「壁時計の一拍」モチーフ

**renji 固有度**: 完全に固有

**残置場所**: `works/renji/bible/style_guide.md` + `state/foreshadowing.yaml`

**なぜ template 化しないか**:
- 完全に renji 専用のモチーフ
- 「能力の兆候モチーフを 1 ep + 最終 ep で円環させる」という発想は generic 化可能だが、それは別の craft 原理として扱うべき（本セッションでは未着手）

---

## 8. 72 話 / 6 アーク / 12 話の数字

**renji 固有度**: 完全に固有

**残置場所**: `works/renji/bible/plot/arc_map.md`、`bible/plot/episode_plan.md`、`story/kernel.yaml.unit_tree`

**なぜ template 化しないか**:
- どの作品も独自のスケールを持つ
- kernel.unit_tree でスキーマだけ提供すれば、数字は作品ごとに

---

## 9. レクシア王国 / 魔王領 等の固有名詞

**renji 固有度**: 完全に固有

**残置場所**: `works/renji/bible/world/`

**なぜ template 化しないか**:
- 全部作品固有

---

## 10. 99 件三層対応表

**renji 固有度**: 完全に固有

**残置場所**: `works/renji/bible/plot/three_layer_table.md`（未作成、renji_novel_bible/14 直参照）

**なぜ template 化しないか**:
- 三層構造自体が renji 固有なので、その対応表も固有

---

## 整理: 抽象化 vs 残置の判断基準

| 項目 | 判断 |
|---|---|
| 構造（フィールド構成・section 構成） | **template 化** |
| 概念（kernel / status / DoR DoD 等） | **template 化** |
| 個別データ（renji の固有名詞・場所・キャラ） | **残置** |
| 装置（三層対応 / 能力名） | **残置**（作品固有装置） |
| 数値（72 話 / 6 アーク） | **残置** |
| 形式・運用（章末資料を置く・モチーフを使う） | **template 化** |
| 内容（章末資料の中身・モチーフの種類） | **残置** |

抽象化されたものと残置されたものの境界はおおよそ「**何が必要か**」と「**何を入れるか**」の違い。前者は template に、後者は実作品の bible に。
