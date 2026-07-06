# origin: villainess
# overlay: unit-packet-2stage — packet を2段freezeで刻む（安定性重視・部分再構成に強い）

manifest で `"overlays": ["unit-packet-2stage"]` と宣言した作品が使う。

## 執筆単位
`Arc → Packet(1〜4話) → Episode → Scene → Draft`

## packet の状態遷移（8状態）
```
exploring → scoped → frozen(初回) → dry-run draft(冒頭1-2話)
  → frozen(再) → drafting(残り) → review → approved → published
```

## 2段freeze の意味
- **初回freeze**: purpose / episode_roles / disclose / withhold / guardrails を確定（DoR-C）。
- **dry-run draft**: 冒頭1〜2話を先に書き、persona A/B/C の1ラウンド目レビュー。
- **再freeze**: 密度マップ・motif配置・接続beat を確定。以降の変更は canon-patch protocol のみ。

## 付随フォルダ（works/{slug}/ に作られる）
`packets/{exploring,scoped,frozen,drafting,review,approved,published}/` と `scenes/{seed,slotted,drafted,merged}/`

## いつ選ぶか
複数 arc/packet が絡み合う・伏線が複雑・部分的に再構成する可能性がある作品。
