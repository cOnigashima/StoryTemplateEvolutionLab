# /retro-meeting

> **v4 注記 (2026-04-30)**: 本 skill 定義は v4 generic 雛形。
> 各 work で実行する際は work 固有の `bible/` `state/` を参照。
> v4 のフロー全体: `docs/domain/04_pipeline_overview.md`
> 旧 v3 の `scenes/drafted/` 等の dir 参照は v4 で更新あり（書き換え TODO、Q-B-001）。
> Drafter は `drafter-preflight.md` rule の適用必須。

---


Agent Team を起動して、packet / 週次の振り返りを行い、learning を次 sprint に返す。

## 概要

packet 完了時または週次に実行する振り返り会議。
3人のチームメイトが review, run, metrics を見て、再利用可能な learning と次 sprint の注意点を決める。

## チーム構成

| Teammate | 役割 |
|----------|------|
| analyst | review / run / metrics から傾向を出す |
| strategist | 次 sprint へ持ち越す方針を提案 |
| experimenter | 次に試す rewrite lever / experiment を1つ提案 |

## 実行手順

1. analyst が `reviews/`, `learning/`, 必要なら `metrics/`, `approved/`, `published/` を読み、今回の傾向を分析
2. strategist が分析結果を受けて、次 sprint の carryover rule と human gate 注意点を提案
3. experimenter が試してみるべき rewrite lever / experiment を1つ提案
4. 3人で議論し、`learning/` に残す要点と次 sprint への持ち越しを決定

## 出力

`learning/retro_YYYYMMDD.md` か `learning/packet-<id>-retro.md` に以下を保存:

```markdown
# Retro Meeting YYYY-MM-DD

## 今回の分析（by analyst）

[analyst の分析結果]

## 次 sprint の戦略（by strategist）

[strategist の提案]

## 次に試す実験（by experimenter）

[experimenter の提案]

## Reuse Rules

### 次 sprint で必ず守ること
1. ...
2. ...

### 再発防止
- 変更なし / [変更内容]

### 実験採用
- 実施する / 見送る
- [理由]

## Human Gate Notes
- 次 sprint で人が必ず見るべき点:

## Context Carryover
- draft 時に自動で持ち込みたい要点:

## 議論メモ

[議論の要点]
```

## 起動コマンド例

```
振り返りのため Agent Team を作って。
3人にして:
- analyst: reviews / runs / metrics を分析して傾向を出す
- strategist: 分析結果から次 sprint の方針を提案
- experimenter: 試してみるべき rewrite lever を1つ提案

議論して、最終方針を learning/retro_YYYYMMDD.md にまとめて。
```

## 補助ファイル

### publish_log.csv
```csv
date,episode_id,title,pv,follows,stars,comments,score
2024-01-01,ep001,第1話,1234,12,5,3,85
```

### experiment_log.csv
```csv
date,experiment_id,hypothesis,group,metric,value,conclusion
2024-01-01,exp001,冒頭を短くするとPVが上がる,A,pv,1000,
2024-01-01,exp001,冒頭を短くするとPVが上がる,B,pv,1200,成功
```
