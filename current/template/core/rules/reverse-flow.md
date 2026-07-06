# origin: villainess
# reverse-flow — 逆方向フロー。本文の問題は上流へ遡上させて直す（下で握りつぶさない）

レビューで出た問題は、症状の階層ではなく原因の階層で直す。

| 症状 | 遡上先（直す場所） |
|---|---|
| 文章・描写・台詞の質 | `drafts/` `scenes/` |
| フック不足・ペース | `overlay` の unit（packet/episode-pack） |
| 動機・関係の不整合 | `bible/characters` + `state/entities.yaml` |
| 開示順序・反転点 | `arcs/` |
| 約束との齟齬 | `kernel.promise` / `design/promises` |
| 構造的な負債（すぐ直せない） | `design/design-debt.yaml` に記録 |
| 未確定の設定変更 | `design/canon-patch-proposals/` に起票（承認後に bible へ） |

原則: **draft 内で完結する範囲だけ当該サイクルで直す。packet以上の遡上は learning + proposal に送る。**
