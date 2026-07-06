# 既存 StoryTemplate について議論するためのアジェンダ

このファイルは、既存の StoryTemplate を別セッションでレビュー・統合するための議題集です。

---

# 0. 事前に用意したいもの

```text
既存StoryTemplate本体
過去に使った入力例
過去に出力された設計資料
そのテンプレートでうまくいった事例
そのテンプレートで詰まった事例
現在の作品の設計資料
```

---

# 1. StoryTemplate の役割確認

## 質問

```text
このStoryTemplateは、何のために作られたものか？
企画用か？
設計用か？
執筆前チェック用か？
レビュー用か？
ジャンル管理用か？
世界観管理用か？
キャラ管理用か？
AIへの入力用か？
```

## 判定

```text
thinking tool:
  考えるための道具

capture tool:
  チャット設計を回収する道具

workflow input:
  執筆AIへ渡す入力

review checklist:
  レビュー・judge用

state tracker:
  ledger的な状態管理

framework lens:
  必要時だけ使う視点
```

---

# 2. 項目棚卸し

各項目について以下を確認する。

```yaml
field_name: ""
description: ""
example: ""
is_required: true
current_usage: ""
layer: universal_kernel | genre_overlay | project_override | workflow_input | review_checklist | ledger_target | framework_lens | unclear
used_by: writer | reviewer | judge | adapter | human | ledger_keeper | none
risk_if_missing: ""
risk_if_forced: ""
notes: ""
```

---

# 3. 必須項目と任意項目

## 質問

```text
本当に毎回必須か？
ジャンルによって不要ではないか？
初期段階では未定でよいのではないか？
読者に未開示のため、埋まっていても出してはいけないのではないか？
作品固有方針で空白にするべきではないか？
```

## status 候補

```text
filled
missing
tentative
deferred
intentionally_blank
intentionally_hidden
not_applicable
genre_not_applicable
project_override
contradiction
needs_author_decision
```

---

# 4. StoryTemplate の思想確認

## 質問

```text
このテンプレートはプロット重視か？
キャラ重視か？
テーマ重視か？
ジャンル約束重視か？
読者体験重視か？
文体・声重視か？
因果重視か？
トップダウン設計向きか？
探索的執筆向きか？
```

## なぜ重要か

テンプレートは必ず何かを強調し、何かを見えにくくする。  
その思想を自覚しないと、すべての作品を同じ型に寄せてしまう。

---

# 5. Workflowとの接続

既存StoryTemplateの各項目が、どこで使われるか確認する。

```text
freeform chat
domain synthesis
scene card
acceptance contract
writer prompt
review prompt
judge contract
ledger update
retro
```

## 質問

```text
この項目は writer に渡すべきか？
reviewer に渡すべきか？
judge に渡すべきか？
ledger に入れるべきか？
人間だけが見るべきか？
hidden_from_reader 情報ではないか？
```

---

# 6. Adapterで吸収するべき揺れ

## 質問

```text
StoryTemplateの項目名とworkflowの項目名は一致させるべきか？
それともAdapterで変換するべきか？
既存項目を直接 scene_card に入れてよいか？
acceptance contract に落とすには不足がないか？
```

## 原則

```text
StoryTemplateの全項目をworkflowに直接渡さない
必要な情報だけAdapterで抽出する
```

---

# 7. 既存StoryTemplateの不足

## 見るべき不足

```text
intended_unknowns があるか
must_be_clear があるか
character knowledge があるか
reveal schedule があるか
reader promise があるか
auto_fix_allowed があるか
human_required_if があるか
rejected_ideas を扱えるか
retro に接続できるか
```

---

# 8. 既存StoryTemplateの過剰

## 見るべき過剰

```text
毎回不要な構造項目が必須化されていないか
ジャンル固有項目が汎用項目に混ざっていないか
テーマやメッセージが早期に固定されすぎないか
プロット構造が強制されすぎないか
キャラアークが一方向に固定されすぎないか
```

---

# 9. StoryTemplateとFramework Indexの分離

## 質問

```text
この項目は本当にStoryTemplateの常設項目か？
それとも特定フレームワークのlensか？
```

例。

```text
三幕構成のplot point:
  Framework Lens の可能性が高い

central dramatic question:
  kernel に入れてもよい可能性

red herring:
  mystery overlay

dark moment:
  romance overlay

value shift:
  Story Grid lens / scene diagnosis lens
```

---

# 10. 最初の統合方針を決める

議論の最後に決めること。

```text
既存StoryTemplateからkernelに残す項目
genre overlayへ分離する項目
project overrideとして扱う項目
framework lensへ移す項目
workflow inputへ変換する項目
review / judge に使う項目
ledgerに接続する項目
削除または保留する項目
```

---

# 出力すべき成果物

```text
existing_storytemplate_inventory.md
storytemplate_field_mapping.yaml
storytemplate_gap_report.md
storytemplate_adapter_mapping.yaml
storytemplate_revision_proposal.md
```

---

# 議論の終了条件

以下が揃えば、次へ進める。

```text
既存StoryTemplateの項目が分類済み
Adapterに渡す項目が決まっている
StoryTemplateからscene_cardを作れる
StoryTemplateからacceptance_contractを作れる
writer / judge に渡してよい情報が分かれている
不足・過剰・保留項目が明示されている
Pilot Episodeに使う最小項目が決まっている
```
