# /draft

> **v4 注記 (2026-04-30)**: 本 skill 定義は v4 generic 雛形。
> 各 work で実行する際は work 固有の `bible/` `state/` を参照。
> v4 のフロー全体: `proposal/2026-04-30-zero-base-v4/04_pipeline_overview.md`
> 旧 v3 の `scenes/drafted/` 等の dir 参照は v4 で更新あり（書き換え TODO、Q-B-001）。
> Drafter は `drafter-preflight.md` rule の適用必須。

---


frozen packet と scene 群から draft を起こす。

## 入力

- `packets/frozen/*.yaml`
- `scenes/drafted/`, `scenes/slotted/`, `scenes/merged/`
- `learning/` の直近 packet retro / learning note
- 必要に応じて `story/promises.md`, `bible/`, `approved/`, `published/`

## 手順

1. 対象の frozen packet を読み、`purpose / episode_roles / disclose / withhold / guardrails` を確認する
2. 対象 episode の scene 群を読み、scene の loss / gain / emotional turn を把握する
3. `bible/rules.md`, 直近の `approved/`, `published/`, `learning/` を読み、文体・handoff・再発防止ルールを合わせる
4. `drafts/` に episode 単位の draft を書く
5. draft から packet / scene / carryover learning へのトレースが残るようにする

## 執筆ルール

- `bible/rules.md` の文体・禁則に従う
- `withhold` にある情報は前倒しで明かさない
- 冒頭は `hook_in` を受け、末尾は `cliffhanger` を返す
- scene 群の役割が消えないように、各 scene の turn を本文に反映する
- 直近の `learning/` に再発防止ルールがある場合は、汎用最適化より優先する

## 出力フォーマット

```markdown
# [タイトル]

[本文]

---

## メタ情報

- packet: packet-001-<slug>
- episode: ep01
- source scenes:
  - scenes/drafted/scene-ep01-01-<slug>.md
  - scenes/drafted/scene-ep01-02-<slug>.md
- carryover learning:
  - learning/packet-001-retro.md
- draft status: drafted
- unresolved notes:
  - 
```

## 保存先

`drafts/draft_epXX_YYYYMMDD_HHMMSS.md`
