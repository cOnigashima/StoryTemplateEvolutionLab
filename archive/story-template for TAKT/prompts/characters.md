# Prompt: bible/characters.md

以下の素材から `bible/characters.md` を作成してください。

[RAW NOTES]
<<<RAW_NOTES>>>
ここにキャラ案・会話メモ・関係メモを貼る
<<<END_RAW_NOTES>>>

[EXISTING PROMISES]
<<<PROMISES_MD>>>
ここに story/promises.md を貼る
<<<END_PROMISES_MD>>>

[EXISTING WORLD]
<<<WORLD_MD>>>
ここに bible/world.md を貼る
<<<END_WORLD_MD>>>

要件:
- 出力は Markdown のみ
- 主人公と主要キャラ 2〜4 人を優先して具体化する
- 各キャラは、欲望・恐れ・衝突が見えるようにする
- 主人公との関係が動力になるように書く
- 口調は 1〜2 行で差が出る程度に書く
- 断定できないものは「未決定」

出力フォーマット:

```md
# キャラクター

## キャスト一覧
| id | name | role | narrative_function | status |
|---|---|---|---|---|
| char-001 | 未決定 | protagonist | 物語の中心 | fixed |

## char-001 [主人公名]
- role: protagonist
- story_function: 未決定
- public_face: 未決定
- private_truth: 未決定
- external_goal: 未決定
- internal_lack: 未決定
- false_belief: 未決定
- fear: 未決定
- desire: 未決定
- need: 未決定
- contradiction: 未決定
- secret: 未決定
- pressure_response: 未決定
- moral_line: 未決定
- relationship_axes:
  - with: char-002
    dynamic: 未決定
- speech_signature:
  - 未決定
- change_vector:
  - start: 未決定
  - end: 未決定
- canon_status: fixed

## char-002 [対立者 / フォイル名]
- role: antagonist_or_foil
- story_function: 未決定
- what_they_want: 未決定
- why_they_are_right: 未決定
- pressure_method: 未決定
- fear: 未決定
- contradiction: 未決定
- secret: 未決定
- relationship_to_protagonist: 未決定
- speech_signature:
  - 未決定
- change_vector:
  - start: 未決定
  - end: 未決定
- canon_status: fixed

## char-003 [主要支援 / 攪乱キャラ名]
- role: ally | destabilizer | witness
- story_function: 未決定
- what_they_want_from_protagonist: 未決定
- pressure_added: 未決定
- secret: 未決定
- relationship_to_protagonist: 未決定
- speech_signature:
  - 未決定
- canon_status: provisional

## 脇役テンプレ
### [脇役名]
- role: 未決定
- story_function: 未決定
- relationship_to_protagonist: 未決定
- pressure_added: 未決定
- voice_note: 未決定
- canon_status: provisional

## 関係の火種
- 未決定
- 未決定

## 未決定
- 未決定
```
