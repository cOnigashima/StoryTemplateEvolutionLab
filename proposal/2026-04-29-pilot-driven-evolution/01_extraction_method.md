# 抽象化方法論

> 詳細は `../../learning/2026-04-29-template-extraction-method.md` を参照。
> 本ファイルは proposals 内の索引版。

---

## 一言で

renji 実走から template を抽出する。設計室で先に作らず、**実走から蒸留する**。

## 流れ

```
作品 1 を ingest しながら、template を抽出する。
作品 2 を ingest するときに template を更新する。
作品 N で template が安定する。
```

## 詳細

`../../learning/2026-04-29-template-extraction-method.md` 参照。

## このセッションでの実例

- renji の 13 bible ファイル → 12 template 化、1 残置（three_layer_principle）
- renji の 4 design ファイル → 4 template 化
- renji の 5 state ファイル → 4 template 化、1 残置（three_layer_status）
- renji の 4 writing pack → 4 template 化
- 抽象化率: 約 80%
