# 単位階層

> Manuscript / Part / Arc / Packet / Episode / Scene / Beat の入れ子。
> 詳細は v3 `02_unit_taxonomy.md`。

---

## 入れ子（順序固定・スキップ可・順序入替不可）

```
Manuscript      作品全体
└── Part        第一部・第二部
    └── Arc     中規模（複数 Packet）
        └── Packet  章束（複数 Episode）
            └── Episode  1 話・公開単位
                └── Scene  Episode 内の局所衝突
                    └── Beat  最小 story moment
```

短編は Part / Scene / Beat を省略可。

---

## ID 命名

- Episode: `ep###` (ep001, ep072)
- Packet: `packet-###`
- Arc: `arc-#`
- Scene Card（既存マスター ID）: `C###`
- Character: `ch_{slug}`
- 三層対応: `##-##` (00-01, 01-13)

---

## 各単位の最小条件

### Manuscript
- premise / unit_tree / 完結予定

### Part
- 番号 / 主題 1 文 / 不可逆変化 / 次 Part への接続

### Arc
- 番号 / 中核問い 1 文 / 主反転 1 文 / 含む Packet 一覧

### Packet（DoR-C 関連）
- purpose / entry_state / exit_state / episode_roles / end_hooks / disclose / withhold / guardrails

### Episode（DoR-B 関連）
- focal character / 因果一段落 / 開始終了知識状態 / packet 要件マッピング

### Scene
- location / time / focal char goal / conflict / turn / end_state

### Beat
- 自由形式

---

## サイズ目安（推奨）

| 単位 | サイズ |
|---|---|
| Beat | 50〜300 字 |
| Scene | 500〜2000 字 |
| Episode | 1500〜5000 字（kakuyomu 1 話想定） |
| Packet | 5〜15 Episode |
| Arc | 2〜5 Packet |
| Part | 2〜5 Arc |

---

## Scene Card（混同警告）

`Scene Card` は story unit ではなく **設計成果物**。`Scene` という story unit とは別物。1 episode に対する設計カードを `scene_card` と呼ぶ。

---

## Acceptance Contract

`Scene Card` と対。drafter 用が scene_card、judge 用が acceptance_contract。Adapter が両方を同時生成。
