# Prompt: packets/scoped/packet-001-<slug>.yaml

以下の素材から `packets/scoped/packet-001-<slug>.yaml` を作成してください。

[EXISTING PROMISES]
<<<PROMISES_MD>>>
ここに story/promises.md を貼る
<<<END_PROMISES_MD>>>

[EXISTING WORLD]
<<<WORLD_MD>>>
ここに bible/world.md を貼る
<<<END_WORLD_MD>>>

[EXISTING CHARACTERS]
<<<CHARACTERS_MD>>>
ここに bible/characters.md を貼る
<<<END_CHARACTERS_MD>>>

[EXISTING ARC]
<<<ARC_01_MD>>>
ここに arcs/arc-01.md を貼る
<<<END_ARC_01_MD>>>

要件:
- 出力は YAML のみ
- `status` は `scoped`
- `primaryArcId`, `relatedArcIds`, `episode_roles`, `end_hooks`, `disclose`, `withhold`, `guardrails`, `focus`, `episodes`, `queue_bucket` は必須
- `reader_promise`, `entry_state`, `exit_state`, `stakes`, `pressure`, `dependencies`, `open_questions`, `freeze_check` を含める
- `primaryArcId` は `arc-01`
- `episodes[]` は packet_size に合わせて 3 話前後
- 各 episode には `id`, `title`, `status`, `role`, `purpose`, `desire`, `obstacle`, `loss`, `gain`, `emotion_curve`, `reveal`, `hooks`, `cliffhanger`, `draft_file`, `scenes_merged` を入れる
- disclose / withhold / guardrails は空配列にしない
- `open_questions.blocker` は blocker がなければ空配列でもよい
- `freeze_check` は未確定項目がある間は `false` を基本にする
- 不足情報は `未決定`
- YAML として妥当な形式にする

出力フォーマット例:

```yaml
id: packet-001-<slug>
title: タイトル
status: scoped
packet_size: "3"
primaryArcId: arc-01
relatedArcIds:
  - arc-01
goal: この束で達成したいこと
summary: この束の要約
purpose: この束で読者に何を感じさせるか
reader_promise:
  - この packet で継続的に渡す快楽
entry_state:
  protagonist: 未決定
  world: 未決定
  relationships: 未決定
exit_state:
  protagonist: 未決定
  world: 未決定
  relationships: 未決定
stakes:
  personal: 未決定
  relational: 未決定
  external: 未決定
pressure:
  antagonist_or_obstacle: 未決定
  time_or_structural_limit: 未決定
episode_roles:
  - "ep01: 導入"
end_hooks:
  - 次束へ渡すフック
disclose:
  - 今回明かすこと
withhold:
  - 今回まだ伏せること
guardrails:
  - 今回やりすぎないこと
focus:
  - 主人公の欲望
dependencies:
  world:
    - 未決定
  characters:
    - 未決定
  rules:
    - 未決定
episodes:
  - id: ep01
    title: 未決定
    status: planned
    role: 導入
    purpose: 未決定
    desire: 未決定
    obstacle: 未決定
    loss: 未決定
    gain: 未決定
    emotion_curve:
      start: 未決定
      peak: 未決定
      end: 未決定
    reveal:
      disclose:
        - 未決定
      withhold:
        - 未決定
    hooks:
      - 未決定
    cliffhanger: 未決定
    draft_file: drafts/draft_ep01_YYYYMMDD_HHMMSS.md
    scenes_merged: []
open_questions:
  blocker:
    - 未決定
  non_blocker:
    - 未決定
freeze_check:
  purpose_clear: false
  entry_exit_state_clear: false
  episode_roles_clear: false
  loss_gain_clear: false
  disclose_withhold_clear: false
  dependencies_resolved: false
  sceneable_without_strategy_questions: false
queue_bucket: ideas
```
