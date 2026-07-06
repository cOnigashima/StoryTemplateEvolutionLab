# adapter/ — Intake / Writing Adapter 設計（汎用版）

> renji pilot の `.adapter/` から汎用化したもの。新規作品で使うときはこのディレクトリを参照する。
> 作品固有の adapter 設定は各 work の `.adapter/` に置く（このディレクトリの中身を **コピー or 参照** して使う）。

---

## ファイル

| ファイル | 役割 |
|---|---|
| `folder_structure.md` | 作品ディレクトリの bible/design/state/writing 構造仕様 |
| `intake_adapter_prompt.md` | 自由 chat / raw → 更新案 prompt |
| `writing_adapter_prompt.md` | bible/state → Writing Pack 生成 prompt |
| `field_mapping_template.yaml` | 既存項目名 → 各層への mapping テンプレ |
| `update_proposal_format.yaml` | 反映前差分のフォーマット |
| `writing_pack_format.yaml` | 1 episode 用 pack の 4 ファイル仕様 |
| `human_approval_policy.md` | 自動・人間判断の境界 |

---

## 全体フロー

```
[企画チャット / 既存資料 / 大量入力]
        ↓
inbox/planning_sessions/  (raw 保存)
        ↓
[Intake Adapter Prompt]
        ↓
synthesis/session_digests/   (整理済 digest)
synthesis/update_proposals/  (反映案)
        ↓
[Human Approval]
        ↓
bible/, design/, state/  (確定反映)
        ↓
[Writing Adapter Prompt]
        ↓
writing/episode_packs/{ep}/  (執筆用 4 ファイル)
        ↓
[執筆]
        ↓
drafts/episodes/  (本文)
        ↓
[Review / Judge]
        ↓
ledger/ 更新 + approved/ → published/
```

---

## 設計原則

1. **raw を直接 bible に流さない**
2. **bible / design / state / writing を分離**
3. **bible 全体を writer に渡さない**（圧縮 pack のみ）
4. **status を必ず付ける**（11 値）
5. **更新は必ず human approval を経る**
6. **trace を残す**（source 参照を全提案に付与）
7. **作品固有装置は generic 化しない**（template に積まない）

---

## 使う場面

### 新規作品の最初

1. `../work_init/new_work_bootstrap.md` の手順で work directory を切る
2. 本ディレクトリの内容を作品の `.adapter/` にコピー
3. 作品固有のカスタマイズ（field_mapping の追加項目等）
4. inbox に企画チャットを入れる
5. `intake_adapter_prompt.md` を実行

### 既存資料を ingest

1. inbox/planning_sessions/ に資料一式を配置
2. `intake_adapter_prompt.md` を実行
3. session_digest と update_proposals が出力される
4. human approval を経て bible/design/state を反映

### 1 episode を書く前

1. bible/state が DoR-B を満たすか確認
2. `writing_adapter_prompt.md` を実行
3. writing/episode_packs/{ep}/ に 4 ファイル生成
4. drafter（人 or AI）に渡す

---

## renji pilot との差分

renji の `.adapter/` (`works/renji/.adapter/`) は本ディレクトリの **最初の利用例**。renji 固有の例（三層対応 / 正当化圏 等）が含まれていたが、本ディレクトリでは generic 化済み。
