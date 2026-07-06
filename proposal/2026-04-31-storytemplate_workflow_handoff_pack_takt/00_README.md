# StoryTemplate × TAKT × AI小説制作ワークフロー 引き継ぎパック

このパックは、ここまでの議論を別セッションへ引き継ぐための俯瞰資料です。

目的は以下です。

1. ここまでの議論の流れを整理する
2. 主要論点・未決論点・優先タスクを明確にする
3. 既存の StoryTemplate と統合するための議論材料を用意する
4. TAKT / episode-draft-tournament / judge / ledger / adapter / framework index の関係を整理する
5. 次セッションでそのまま使えるプロンプトと議題を用意する

## 推奨読書順

1. `01_handoff_summary.md`
2. `02_discussion_timeline.md`
3. `03_system_architecture.md`
4. `04_core_concepts.md`
5. `05_storytemplate_integration_guide.md`
6. `06_existing_storytemplate_review_agenda.md`
7. `07_adapter_design.md`
8. `08_framework_index_strategy.md`
9. `09_workflow_design.md`
10. `10_prioritized_task_backlog.md`
11. `11_risks_and_considerations.md`
12. `12_not_now_list.md`
13. `13_next_session_prompt.md`

## 重要な前提

既存の StoryTemplate の実物は、この時点では未共有です。  
そのため、このパックでは「既存StoryTemplateをどうレビューし、どう統合するか」に重点を置いています。

やるべきことは、既存StoryTemplateを捨てて新しい最強テンプレートを作ることではありません。  
既存StoryTemplateを尊重しつつ、以下の役割に分解して再接続することです。

```text
StoryTemplate:
  物語設計の箱・観点・チェックリスト

Adapter:
  StoryTemplate / 自由チャット / Framework Lens を制作入力へ変換する層

Workflow:
  episode-draft-tournament など実際に書くための制作ライン

Judge:
  合意済み基準に照らして通すか止める品質ゲート

Ledger:
  執筆が進む中で確定した状態を管理する台帳

Retro:
  何が効いたかを振り返り、テンプレ・プロンプト・フローを更新する仕組み
```

## このパックの結論

最初から巨大な StoryTemplate や完全自動化ワークフローを作らない。  
まずは以下を作り、1 Episode で実験する。

```text
StoryTemplate Integration Review
  ↓
StoryaTemplate Kernel v0
  ↓
Domain Synthesis Prompt v0
  ↓
Framework Index Card v0
  ↓
Adapter v0
  ↓
Pilot Episode
  ↓
Retro
```
