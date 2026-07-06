# Domain ＆ Kernel v3 — ガチガチ設計パック

> **日付**: 2026-04-29
> **作成者**: Claude（本 Cowork セッション）
> **依拠する決定事項**:
> - 「Layer 1 kernel は薄く、Layer 2/3 は太く」で両立
> - Pilot は新規作品で実施
> - TAKT を workflow 実行基盤として採用（YAML + Faceted Prompting + Git-native）
> **session goal**: 語彙統一 ＋ kernel 仕様 ＋ 必須 setup ＋ DoR/DoD まで固める。Adapter 実装と TAKT workflow yaml は次セッション以降。

---

## このパックの位置付け

`story-template for TAKT/proposals/` には現在 3 つのパックがある:

```
proposals/
├── 2026-04-22-story-template-v2/        ← Pack A: Story Template の中身を fat 整理
├── storytemplate_workflow_handoff_pack/ ← Pack B: TAKT workflow の外側設計
└── 2026-04-29-domain-kernel-v3/         ← 本パック: A と B を語彙・kernel で接合
```

本パックは **Pack A と Pack B の語彙衝突を解消し、kernel に何が入るか / 何が入らないかを固定** することを目的とする。Pack A も Pack B も削除しない。共に参照資産として残す。

> Pack A と Pack B のどちらが「正」ではなく、本 v3 の語彙が「正」になる。両 pack の語彙ズレは本 v3 で吸収する。

---

## このパックの読み順

| # | ファイル | 一言で |
|---|---|---|
| 00 | `00_README.md` | 本ファイル。スコープと読み順 |
| 01 | `01_vocabulary.md` | 統一語彙表（1 概念 1 語、衝突解決） |
| 02 | `02_unit_taxonomy.md` | 単位階層（Manuscript / Part / Arc / Packet / Episode / Scene / Beat） |
| 03 | `03_layer_facet_map.md` | Layer 0-4+R × TAKT facet × ファイル位置 |
| 04 | `04_kernel_spec.md` | 薄い kernel 11 項目の field-by-field 仕様 |
| 05 | `05_status_vocabulary.md` | 状態語彙（11 status / Judge 4 値 / Lock 状態） |
| 06 | `06_setup_dor.md` | Definition of Ready（執筆を始める前の必要条件） |
| 07 | `07_publish_dod.md` | Definition of Done（公開前の必要条件） |
| 08 | `08_open_questions.md` | 本 v3 で意図的に決めなかった論点 |
| 09 | `09_pilot_setup.md` | 新規 pilot 作品を始めるための最小手順 |

依存関係:

- `02` → `01`（単位は語彙の subset）
- `03` → `01` `02`（layer/facet は語彙と単位の上に乗る）
- `04` → `01` `02` `03`（kernel は語彙・単位・layer を踏まえる）
- `05` → `01`（status は語彙の補助）
- `06` `07` → `04` `05`（DoR/DoD は kernel と status を使う）
- `08` → 全部（未決は決めたものとの差分）
- `09` → 全部（pilot は完成像を実装する）

---

## ガチガチに固める対象

本 v3 で固定する:

- **語彙**: 1 概念 = 1 正式語。同義語・別表記は禁止 or 別物として明示
- **単位階層**: Manuscript / Part / Arc / Packet / Episode / Scene / Beat の入れ子順序
- **Layer 帰属**: 各概念がどの Layer に属し、どの TAKT facet に流れるか
- **Kernel 必須項目**: 執筆開始の最低条件として絶対必要なフィールド
- **Status 語彙**: 未記入を区別する 11 状態
- **Judge 判定値**: PASS / FAIL_AUTO_FIX / NEEDS_HUMAN / REJECT_AND_REGENERATE
- **Lock 状態**: soft_lock / packet_soft_lock / hard_lock
- **DoR 3 段**: 作品 bootstrap 時 / Episode 執筆前 / Packet 凍結前
- **DoD 3 段**: Episode 公開 / Packet release / Arc/Part 大区分

本 v3 で固定しない:

- TAKT workflow yaml の内部構造（次セッション）
- Adapter の実装詳細 step-by-step（次セッション）
- 各 reviewer persona の prompt 本文（pilot 後）
- 個別 Genre Overlay の中身（pilot 作品 genre 確定後）
- Framework Lens カタログ（実適用案件が出てから）

---

## 決定の優先順位

衝突したらこの順で:

1. **本 v3 の固定語彙** — 全 pack の語彙より優先
2. **Pack A の 4+1 Layer 構造** — 全体配置の枠組み
3. **Pack B の役割分解（Kernel / Overlay / Override / Workflow Input / Review Checklist / Ledger Target / Framework Lens）** — kernel 設計の基準
4. **TAKT の facet 構造（persona / policy / knowledge / instruction）** — prompt 配置
5. **Pack A の `.claude/rules/` 5 本** — 既存運用ルール
6. **kakuyomu-policy** — 公開時の制約

---

## このパックを読み終えた後の状態

- 語彙の意味で議論が止まらなくなる
- 「kernel に入れる / 入れない」の判定が機械的にできる
- 新規作品を始めるとき、何を埋めれば執筆に入れるか即座に判定できる
- Episode 1 本を draft する前に何が揃っていればいいかが書ける
- 公開前に何を確認すれば事故らないかが書ける
- pilot で何が「足りない」と判明したらどこに足せばいいか分かる

---

## 承認プロセス

- **full-accept** → `09_pilot_setup.md` の手順で新規 pilot 作品を起こし、実走に入る
- **partial-accept** → 採否を per-file で指示。非採用部は `08_open_questions.md` に持ち上げる
- **revise** → コメントを反映して本 v3 を改訂（同じディレクトリ内で in-place 上書き、必要なら revision メモを併設）
- **reject** → 本パックを archive 化し、Pack A / Pack B どちらか単独で進める判断

---

## 既存資産との関係

- **Pack A の `02-domain-map.md`** — 本 v3 `01_vocabulary.md` の母体
- **Pack A の `01-design-overview.md` §2 Layer 構造** — 本 v3 `03_layer_facet_map.md` の母体
- **Pack B の `04_core_concepts.md`** — 本 v3 `01_vocabulary.md` のもう一方の母体
- **Pack B の `06_existing_storytemplate_review_agenda.md`** — 本 v3 `04_kernel_spec.md` の論点源
- **Pack B の `07_adapter_design.md`** — 本 v3 では参照のみ。Adapter 実装は次セッション
- **TAKT `docs/README.ja.md`** — 本 v3 `03_layer_facet_map.md` で facet 構造に反映
- **`.claude/rules/` 5 本** — 本 v3 で変更しない。境界追記は次セッション以降

---

## DoD（本 v3 の完了条件）

本パック自身が完了したと言える条件:

- 9 ファイルが揃っている
- `01_vocabulary.md` に Pack A / Pack B 双方で使われている全用語が登録済
- `04_kernel_spec.md` の 11 項目それぞれに必須度・記述形式・サンプルがある
- `06_setup_dor.md` ・ `07_publish_dod.md` がチェックリスト形式で書かれている
- `08_open_questions.md` に「本 v3 で意図的に決めなかったこと」が列挙されている
- `09_pilot_setup.md` の手順を読んだだけで新規作品を起こし始められる
