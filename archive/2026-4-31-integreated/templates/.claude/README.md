# templates/.claude/ — 各 work の `.claude/` 雛形

> **役割**: 新規 work bootstrap 時、各 work の `.claude/` 配下に copy する元。
> **使い方**: `current/work_init/new-work-bootstrap.md` Step 1.5 から呼ばれる。

---

## 配下

```
templates/.claude/
├── README.md                    本ファイル
├── settings.template.json       Claude Code 設定テンプレ（project_name 等の placeholder）
├── rules/                       共通 rule 5 本（v4 化済）
│   ├── drafter-preflight.md
│   ├── file-growth.md
│   ├── kakuyomu-policy.md
│   ├── learning-capture.md
│   └── story-os-boundaries.md
├── agents/                      generic agent 18 本
│   ├── plotter.md / drafter.md / critic.md / continuity-checker.md   ← 主要 4 役
│   ├── editor.md / continuity-guard.md / audience-proxy.md / devils-advocate.md
│   ├── community-agent.md / compliance-agent.md / kakuyomu-launch-agent.md / sns-copy-agent.md
│   └── 他 6 本
└── skills/                      generic skill 7 本
    ├── pitch.md / draft.md / critic.md / continuity.md / release.md   ← 主要 5 種
    └── retro-meeting.md / review-meeting.md
```

---

## bootstrap での copy

```bash
cd works/{slug}/
mkdir -p .claude
cp -r ../../StoryTemplateEvolution/current/templates/.claude/rules    .claude/
cp -r ../../StoryTemplateEvolution/current/templates/.claude/agents   .claude/
cp -r ../../StoryTemplateEvolution/current/templates/.claude/skills   .claude/
cp ../../StoryTemplateEvolution/current/templates/.claude/settings.template.json .claude/settings.json
```

---

## 各 work での扱い

**copy 後はその作品固有に refactor して良い**。

- ia_society の `.claude/rules/drafter-preflight.md` は generic + 作品固有 Gate D/E/F/G を追加
- fools-with-cheating の `.claude/skills/draft.md` は三層対応の制約を追加
- 各 work で agents の役割を絞り込む / 廃止する

generic 雛形は **出発点**。作品の特性に合わせて成長させる。

---

## generic / 作品固有の境界

| 内容 | template に積む | 各 work で書き換える |
|---|---|---|
| Drafter Preflight の 3 項目 | ✓ | 作品固有 Gate を追加 |
| File Growth ルール | ✓ | 基本そのまま |
| Kakuyomu Policy | ✓ | platform を追加 |
| Learning Capture | ✓ | 基本そのまま |
| Story OS Boundaries | ✓ | 作品固有禁止語を追加 |
| Plotter / Drafter / Critic Agent | ✓ | 作品の Promise / Theme との整合を追加 |
| Skill 群 | ✓ | 作品固有の手順を追加 |
| 三層対応 / 章末資料 / 批評性 等の作品固有 facet | ✗ | 各 work が独自 rule で扱う |

---

## v4 整合性 (2026-04-30 時点)

- ✅ rules/ 5 本: v4 用語注記済み
- ⚠ agents/ 18 本: 冒頭に v4 注記あり、内部 dir 参照は一部 v3 残存（Q-B-001 で 90 日以内に書き換え）
- ⚠ skills/ 7 本: 同上
