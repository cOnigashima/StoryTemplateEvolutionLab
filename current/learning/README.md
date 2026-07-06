# learning/ — StoryTemplate 進化の決着記録

> **役割**: template への変更（昇格・棄却・方法論）の「なぜそうしたか」を記録する台帳。
> template が変わっても記録は消さない — **変更の根拠として永続**する。

## 二層構造（作品 learning との関係）

| 層 | 場所 | 中身 |
|---|---|---|
| 作品 | `works/{slug}/runtime/logs/learning/` | 作品固有の retro 全記録。作品の資産としてそのまま残る |
| STE | `current/learning/`（ここ） | 汎用に効くと判断され current に反映された（or 棄却された）知見の決着記録 |

## フィードバックフロー

```
作品 retro（runtime/logs/learning/）
  → 汎用に効く知見を抽出し、STE の improvement_request_inbox/ に raw 投入
  → 検討（proposal/ 化 or 軽微なら直接 Patch）
  → current に反映
  → 決着を learning/{date}-{slug}.md に記録（採用理由・棄却理由・影響範囲）
```

`.claude/rules/repository-discipline.md` SHOULD #7 の書き先はここ。

## 既存記録

- `2026-04-29-renji-pilot-retro.md` — Evolution が生まれた経緯（renji pilot）
- `2026-04-29-template-extraction-method.md` — 抽出方法論
- `2026-04-29-reorg-and-prompts.md` — v3 期の再編記録
- `2026-04-29-handoff-to-next-session.md` — セッション引き継ぎの原型
- `2026-07-06-workbench-integration.md` — workbench 統合の決着記録

（04-29 の4本は origin: STE-v4。`archive/2026-04-31-integreated/learning/` からのコピー復元）
