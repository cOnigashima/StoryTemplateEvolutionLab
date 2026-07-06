# 次セッション用プロンプト

以下を別セッションの冒頭に貼ると、議論を再開しやすい。

---

## 引き継ぎプロンプト

ここまで、AI支援の長編小説制作ワークフローについて議論してきました。  
最初は TAKT を使って小説ドラフト・レビュー・改稿を回す話でしたが、現在は以下のような全体構造に整理しています。

```text
Freeform Chat
  ↓
Domain Synthesis
  ↓
StoryTemplate / StoryaTemplate Kernel
  ↓
Framework Lens Selection
  ↓
Adapter
  ↓
scene_card / acceptance_contract / judge_contract / ledger targets
  ↓
episode-draft-tournament
  ↓
review / selection-synthesis / judge / ledger
  ↓
retro
```

重要な設計判断は以下です。

```text
Episode:
  1話単位。episode-draft-tournamentで複数writer候補を出す。

Packet:
  複数Episodeの章束。接続・テンポ・局所矛盾を見る。

Arc:
  Part内の中規模単位。構成戦略をレビュー・競わせる。

Part:
  第一部・第二部など。大局レビューを行う。

Draft:
  単位名ではなく状態名。

Chapter:
  内部制作単位としては使わない。
```

`episode-draft-tournament` は以下です。

```text
scene_card
  ↓
faithful writer
emotional writer
plot-drive writer
必要なら dialogue writer / risky writer
  ↓
selection-synthesis
  ↓
integrated episode reviser
  ↓
episode judge
  ↓
ledger keeper
```

重要ルール。

```text
base draft は1本だけ選ぶ
他案から借りる要素は最大数個
借りるのは基本的に文章片ではなく設計意図
judge は面白さの絶対判定ではなく acceptance contract の品質ゲート
ledger は制作中の真実台帳
```

現在の最大論点は、既存の StoryTemplate とこの workflow をどう統合するかです。

方針は以下です。

```text
既存StoryTemplateを捨てない
ただし巨大な最強テンプレートも作らない
既存項目を Universal Kernel / Genre Overlay / Project Override / Workflow Input / Review Checklist / Ledger Target / Framework Lens に分類する
Adapterで workflow input に変換する
```

最初に取り掛かるべきことは以下です。

```text
1. 既存StoryTemplateの棚卸し
2. StoryTemplate Kernel v0 の抽出
3. Domain Synthesis Prompt v0 の作成
4. Framework Index Card v0 の作成
5. Adapter v0 の作成
6. Scene Card / Acceptance Contract schema の作成
7. 1 Episode Pilot
8. Retro
```

今すぐやらなくていいこと。

```text
全創作理論のdeep research
最強StoryTemplate完全版
全ジャンル対応
全workflowのTAKT完全実装
Arc / Part / Manuscriptまでの完全自動化
1000タスクの完全整理
大量レビュアー導入
精密スコアリング体系
```

次にやりたいことは、既存StoryTemplateを見ながら、以下を議論することです。

```text
既存StoryTemplateの各項目はどの層に属するか
何をKernelに残すか
何をGenre Overlayへ分けるか
何をProject Overrideとして扱うか
何をFramework Lensへ移すか
何をscene_card / acceptance_contract / judge / ledger に接続するか
何が不足・重複・過剰・曖昧か
```

この前提で、既存StoryTemplateとの統合レビューから始めてください。
