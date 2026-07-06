# template — 正本（育てる最終アウトプット）

ここは「新作の出発点」であり、同時に「実走から進化させていく再利用資産」。
`core/`（全作品が従う背骨）と `overlay/`（作品が選ぶ構造）に分かれる。

---

## 新作の bootstrap 手順（詳細は `../work_init/new-work-bootstrap.md`）

1. **外部フォルダ** `works/{slug}/` を作る（current の中には置かない）。
2. この `template/` を `works/{slug}/` にコピー（core＋選んだoverlay＋runtime＋manifest）。
3. `work.manifest.template.json` → `work.manifest.json` にして overlay/逸脱を宣言。
4. `adapter/intake_adapter.md` で企画を取り込み、`bible/design/state` を埋める。
5. `core/checklists/dor_dod.md` の **DoR-A** を満たしたら執筆へ。

## 3つの中身
- `core/` … 全作品が従う背骨（必須）
- `overlay/` … 作品が選ぶ執筆単位（episode-pack / packet-2stage）
- `runtime/` … 作品側で埋まる空フォルダ雛形（drafts/reviews/approved/published/reader-export/logs）
- `folder_structure.md` … 作品フォルダの完全な構造定義

---

## core と overlay の境界

| 種別 | 例 | 変更ポリシー |
|---|---|---|
| **core（共通・必須）** | kernel11 / bible-facet / state(ontology) / review pipeline / DoR-DoD / rules | 変更は「昇格」扱い。理由を learning に残す |
| **overlay（作品選択）** | 執筆単位の刻み（episode-pack / packet-2stage） | manifest で選ぶ。作品ごとに差し替え可 |
| **work-local（作品固有）** | CoCの卓ルール、三層記録 | core に積まない。works/{slug}/ に置く |

境界判断: 「別の作品でも使えるか？」YES→core/overlay候補、NO→work-local。

---

## origin タグ（統合のため）

core 配下の各ファイル冒頭に `origin:` を書く。
- `origin: STE-v4` … StoryTemplateEvolution v4 由来
- `origin: workbench` … workbench で新規に起こした
- `origin: fools` / `origin: villainess` … 実走作品から抽象化して吸収

後で StoryTemplateEvolution と統合する際、差分マージの手がかりになる。
