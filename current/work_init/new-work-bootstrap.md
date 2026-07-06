# new-work-bootstrap — 新作の立ち上げ手順

作品は current/ をコピーした**外部フォルダ**として作る（current/ の中には置かない）。
完全な構造定義は `../template/folder_structure.md`、運用契約は `../CLAUDE.md`。

## 手順

1. 作品フォルダを別の場所に作る: `works/{slug}/`（このリポジトリの外、または専用リポジトリ）。slug は kebab-case。
2. `current/template/` を `works/{slug}/` にコピー:
   - `core/`（必須）
   - 使う `overlay/`（1つ以上）… 例 `unit-packet-2stage`
   - `inbox/`（raw 受付箱）と `synthesis/`（intake 中間生成物。G-Intake の承認対象が生まれる場所）
   - `runtime/`（空フォルダ雛形 drafts/reviews/approved/published/reader-export/logs）
   - `work.manifest.template.json` → **`work.manifest.json` にリネーム**
3. **`core/kernel.template.yaml` → `core/kernel.yaml` にリネーム**（folder_structure.md は `kernel.yaml` を要求。テンプレのまま残さない）。
4. 必要なら `current/adapter/` `current/takt/` `current/tools/` も作品側にコピー（自己完結させる場合）。または current/ を共有参照。
5. `work.manifest.json` を編集し、slug・uses_core_version・overlays・deviations_from_core（逸脱は理由必須）・kakuyomu 設定を宣言。
6. 企画チャットの raw を `inbox/planning_sessions/` に置き、`adapter/intake_adapter.md` で取り込む → `synthesis/` に digest + update_proposal が生成 → **G-Intake 承認** → `bible/design/state` に反映。
   - 全 field に status（12 値、`docs/status_vocabulary.md`）を付ける。空欄禁止。
7. オントロジー検査: `python3 tools/ontology_check.py works/{slug}/core`（**`core` まで指定**。作品フォルダ直下を指定すると state/ を見つけられない）。
8. `template/core/checklists/dor_dod.md` の **DoR-A** を満たしたら執筆開始（完全版 DoR は `docs/domain/06_bible_dor.md`。※新構造対応の一本化は TODO、迷ったら checklists 版に従う）。

## コピー例（コマンド）

```bash
SLUG=my-novel
mkdir -p works/$SLUG
cp -r current/template/core           works/$SLUG/core
cp -r current/template/inbox          works/$SLUG/inbox
cp -r current/template/synthesis      works/$SLUG/synthesis
cp -r current/template/overlay/unit-packet-2stage works/$SLUG/   # 使う overlay を選ぶ
cp -r current/template/runtime        works/$SLUG/runtime
cp current/template/work.manifest.template.json works/$SLUG/work.manifest.json
mv works/$SLUG/core/kernel.template.yaml works/$SLUG/core/kernel.yaml
python3 current/tools/ontology_check.py works/$SLUG/core   # 動作確認
```

## 出来上がりの形

```
works/my-novel/
├── work.manifest.json
├── inbox/           (planning_sessions/ fragments/ — raw 受付)
├── synthesis/       (session_digests/ update_proposals/ — G-Intake 承認対象)
├── core/            (kernel.yaml bible/ design/ state/ checklists/ rules/ schema/)
├── overlay:packet-2stage の中身   → packets/ scenes/ 等が展開
└── runtime/         (drafts/ reviews/ approved/ published/ reader-export/ logs/)
```

※ overlay の展開の詳細は各 overlay の README、完全構造は `../template/folder_structure.md` 参照。

## 進化への還元

実走で得た learning（runtime/logs/learning）で効いたものは、current/template に昇格させ、正本を更新する（Patch 経由、`proposal/README.md` のフロー参照）。
