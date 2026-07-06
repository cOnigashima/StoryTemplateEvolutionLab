# Seed-to-Macro Review Template

**日付**: YYYY-MM-DD
**レビュアー**: story-architect
**対象**: `story/seeds/seed-YYYYMMDD-HHMMSS.md`
**レビュー種別**: macro 昇格の反映先整理

## 判定

- overall: `promote / hold / partial / blocked`
- summary:
  - この seed の本丸はどの layer にあるか
  - いま direct edit すべきものと、まだ上げないもの

## 反映先の整理

### story

- `story/promises.md`: `direct_edit / patch / no_change / hold`
  - 理由:
- `story/open-questions.md`: `direct_edit / no_change`
  - 理由:
- `story/design-debt.yaml`: `direct_edit / no_change`
  - 理由:
- `story/canon-patch-proposals/`: `create / no_change`
  - 理由:

### world

- `bible/world.md`: `direct_edit / patch / no_change / hold`
  - 理由:

### characters

- `bible/characters.md`: `direct_edit / patch / no_change / hold`
  - 理由:

### rules

- `bible/rules.md`: `direct_edit / patch / no_change / hold`
  - 理由:

### arcs

- `arcs/series-overview.md`: `direct_edit / patch / no_change / hold`
  - 理由:
- `arcs/arc-01.md` または対象 arc: `direct_edit / patch / no_change / hold`
  - 理由:

### packet

- `packets/`: `create / update / no_change / too_early`
  - 理由:

## Reflection Ledger

| item | decision | target | note |
|---|---|---|---|
| seed core | promote | `story/promises.md` | |
| unresolved point | hold | `story/open-questions.md` | |
| canon delta | patch | `story/canon-patch-proposals/...` | |
| packet-ready detail | defer | `packets/` | |
| keep as source | keep | `story/seeds/...` | |

## 今回の論点

### 1. 直接 canon に上げるもの

- 

### 2. まだ上げないもの

- 

### 3. 差分 proposal や debt に送るもの

- 

## 今回の成果物

1. `reviews/seed-to-macro-YYYYMMDD-<slug>.md`
2. 必要なら更新した target file
3. 必要なら作成した canon patch proposal / design debt

## 次アクション

1. 次に編集する file:
2. 今回 edit しない file:
3. packet に落としてよい条件:

## 結論

- この seed の主反映先:
- まだ保留すべき論点:
- 次に進む最短手:
