# Prompt: scenes batch for first episode

以下の素材から、`ep01` の scene 群を 2〜4 本作成してください。
各 scene は 1 ファイルずつ出力し、ファイル区切りを明示してください。

[EXISTING PACKET]
<<<PACKET_001_YAML>>>
ここに frozen packet を貼る
<<<END_PACKET_001_YAML>>>

[EXISTING WORLD]
<<<WORLD_MD>>>
ここに bible/world.md を貼る
<<<END_WORLD_MD>>>

[EXISTING CHARACTERS]
<<<CHARACTERS_MD>>>
ここに bible/characters.md を貼る
<<<END_CHARACTERS_MD>>>

[EXISTING RULES]
<<<RULES_MD>>>
ここに bible/rules.md を貼る
<<<END_RULES_MD>>>

ルール:
- 出力は scene ファイルだけ
- `ep01` の role / loss / gain / disclose / withhold / hook に必ず整合させる
- packet の withhold にある情報は開示しない
- prose draft ではなく、scene card として書く
- 不足情報は `未決定`
- scene 数は最小限でよい

出力形式:

```md
===FILE: scenes/drafted/scene-ep01-01-<slug>.md===
---
packet_id: packet-001-<slug>
episode_id: ep01
target_episode: ep01
related_arcs:
  - arc-01
title: シーン名
pov: 未決定
intent: このシーンで達成する機能
purpose: このシーンの役割
desire: この場で欲しいもの
obstacle: それを邪魔するもの
turn: 状況がどう反転するか
reveal: このシーンで出す情報
emotional_turn: 開始感情 -> 終了感情
canon_delta: 世界 / 関係 / 認識の何が正式に変わるか
scene_type: 導入 | 対立 | 反転 | 余韻
summary: 1行要約
created: YYYY-MM-DD
---

# [シーン名]

## 前提
- 直前の状況:
- 誰が何を欲しているか:
- このシーンで出す情報:
- このシーンで出さない情報:

## ビート
1. 
2. 
3. 

## 変化
- loss:
- gain:
- canon delta:

## 次への接続
- 次シーンに渡すフック:
```
