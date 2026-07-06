# inbox/ — Raw 入力の受付

> **役割**: 企画 chat / 既存 bible package / 設計メモ / 断片メモを **原文ママで保存**する場所。
> **重要**: ここに置いた raw を直接 bible に流さない。Intake Adapter 経由で `synthesis/` に変換する。

---

## 何を入れる

- ChatGPT との企画 chat ログ
- 既存の bible package（外部 LLM で作った設計資料）
- 設計セッションの議事録
- 断片メモ（ふと思いついたアイデア）

---

## 配下構造

```
inbox/
├── README.md                              本ファイル
├── planning_sessions/                     大きな設計 chat
│   └── {YYYY-MM-DD}_{slug}.md
└── fragments/                             断片メモ
    └── {YYYY-MM-DD}_{slug}.md
```

---

## ファイル命名

- `{YYYY-MM-DD}_{slug}.md`（例: `2026-05-15_arc02-pitch-chat.md`）
- 拡張子は `.md` 推奨（チャットログでも markdown 化）
- 既存 bible package を取り込む場合: `{YYYY-MM-DD}_{source-name}-import.md`（複数ファイルなら 1 つに連結 or 索引付き）

---

## 入れた後の流れ

```
inbox/{date}_{slug}.md
        ↓
[Intake Adapter Prompt 実行]
（StoryTemplateEvolution/current/adapter/intake_adapter_prompt.md）
        ↓
synthesis/session_digests/{date}_{slug}.md     ← Digest 生成
synthesis/update_proposals/{date}_{target}_proposal.md  ← 反映指示書
        ↓
[Human Approval]
        ↓
bible/, design/, state/ に確定反映
```

詳細フローは:
- `../../StoryTemplateEvolution/current/WORKFLOW.md`
- `../../StoryTemplateEvolution/proposal/2026-04-30-zero-base-v4/04_pipeline_overview.md` Phase 1

---

## 不変条件

1. **raw を bible に直接書かない** — Intake Adapter 経由必須
2. **inbox に置いた raw を編集しない** — 原文を保持
3. **加工後は synthesis/ に分離** — inbox はそのまま
4. **大量入力を 1 ファイルに丸ごと保存しない** — batch ごとに分ける

---

## 関連参照

- 全体フロー: `../../StoryTemplateEvolution/current/WORKFLOW.md`
- Intake Adapter: `../../StoryTemplateEvolution/current/adapter/intake_adapter_prompt.md`
- intake-flow rule: `.claude/rules/intake-flow.md`（v4 注記済）
- 86 項目チェックリスト: `../../StoryTemplateEvolution/proposal/2026-04-30-zero-base-v4/05_intake_coverage_checklist.md`
