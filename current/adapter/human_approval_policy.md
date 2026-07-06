# origin: STE-v4 / workbench（2026-07-06 復元マージ: 旧196行版の AUTO/HUMAN マトリクスを新構造・12値対応で復元）
# 人間承認ポリシー — 「人間は成果物だけ見る」を具体化

## 0. 基本姿勢

- **デフォルトは「人間判断必要」**。auto_apply_allowed は例外として明示的に true
- **不可逆性のあるものは絶対に自動反映しない**（bible canon 確定 / 公開実施 / 没案削除）
- **status 不一致が出たら author に上げる**
- **AI 提案の根拠を必ず source 参照で示す**

## 1. 止まる場所（人間ゲート）

| ゲート | 何を承認するか | 判断材料 |
|---|---|---|
| **G-Intake** | 企画をbibleに反映してよいか | update proposal + 矛盾チェック結果 |
| **G-Deliverable** | draft+レビュー1サイクルの結果 | 本文 + レビュー票 + validator結果 |
| **G-Publish** | 公開してよいか | approved本文 + 公開メタ + kakuyomu-policy適合 |

止まらない場所（AI自律）: Writing Pack圧縮 / draft生成 / ontology_check / self-review / レビュー票作成 / loop_monitor打切り / reader-export / logs記録。

## 2. 操作カテゴリ別 AUTO/HUMAN 判定（ゲート間で AI がどこまで動けるか）

### A. ファイル新規作成

| 操作 | auto OK | 理由 |
|---|---|---|
| raw 受付への保存（intake 入口） | ✅ AUTO | 受信ログ |
| session digest の出力（intake 中間生成物） | ✅ AUTO | 加工生成、bible 触らない |
| update proposal の出力 | ✅ AUTO | あくまで「案」（反映は G-Intake） |
| `bible/` 配下の新規作成 | ❌ HUMAN | canon 化、不可逆 |
| `design/` 配下の新規作成 | ⚠️ AUTO with notice | 仮の置場 |
| `state/` 配下 yaml の新規作成 | ⚠️ AUTO with notice | seed 投入時のみ |
| Writing Pack の生成 | ✅ AUTO | bible/state 由来の圧縮 |
| `runtime/drafts/` の新規ファイル | ⚠️ AUTO（content は別判定） | ファイルのみ |

### B. 既存ファイルへの変更

| 操作 | auto OK |
|---|---|
| `bible/` 本文書き換え | ❌ HUMAN |
| `bible/` typo 修正のみ | ⚠️ AUTO with notice |
| `design/open-questions.md` への append | ✅ AUTO |
| author 決定ログへの append | ❌ HUMAN |
| `design/project_principles.md` の変更 | ❌ HUMAN |
| `state/timeline.yaml` への append（episode 公開時） | ⚠️ AUTO with notice |
| `state/entities.yaml` / `knowledge_state.yaml` の更新 | ⚠️ AUTO with notice |
| `state/foreshadowing.yaml` の status 更新 | ⚠️ AUTO with notice |
| `state/rejected_ideas.md` への append | ✅ AUTO |

### C. 削除・破棄

| 操作 | auto OK |
|---|---|
| 任意ファイルの削除 | ❌ HUMAN（厳格） |
| `state/rejected_ideas.md` からの除去 | ❌ HUMAN |
| draft の上書き保存 | ❌ HUMAN（前世代を superseded として保全） |

### D. 公開系

| 操作 | auto OK |
|---|---|
| `runtime/approved/` への移動 | ❌ HUMAN（= G-Deliverable） |
| カクヨム等への投稿実施 | ❌ HUMAN（必ず。= G-Publish） |
| AI タグ設定 | ❌ HUMAN |

## 3. status 別判定（12値、正本: `docs/status_vocabulary.md`）

| status | bible | design | state |
|---|---|---|---|
| filled | ❌ HUMAN | ⚠️ AUTO with notice | ⚠️ AUTO with notice |
| tentative | ❌ HUMAN | ✅ AUTO | ✅ AUTO |
| deferred | ⚠️ AUTO with notice | ✅ AUTO | ✅ AUTO |
| intentionally_blank | ❌ HUMAN（状態変更は再承認） | ⚠️ AUTO | ⚠️ AUTO |
| intentionally_hidden | ❌ HUMAN（漏洩リスク） | ⚠️ AUTO | ⚠️ AUTO |
| not_applicable | ⚠️ AUTO with notice | ✅ AUTO | ✅ AUTO |
| genre_not_applicable | ⚠️ AUTO with notice | ✅ AUTO | ✅ AUTO |
| project_override | ❌ HUMAN（強拘束） | ❌ HUMAN | ❌ HUMAN |
| contradiction | ❌ HUMAN（必ず） | ❌ HUMAN | ❌ HUMAN |
| needs_author_decision | ❌ HUMAN（必ず） | ❌ HUMAN | ❌ HUMAN |
| missing | ❌ HUMAN（候補提案まで） | ✅ AUTO | ✅ AUTO |
| rejected | n/a | ⚠️ AUTO with notice | ⚠️ AUTO with notice |

## 4. 影響度別判定

**High Impact（1 つでも該当 → ❌ HUMAN）**: logline / promise / theme / genre 変更、主要キャラの動機・wound 変更、POV 方針変更、文体方針変更、arc の主反転変更、promise の追加・削除、intended_unknowns の追加・削除、forbidden_words の追加・削除、作品固有装置の構造変更。

**Medium Impact（⚠️ AUTO with notice + 24h 以内通知）**: 単一 episode の scene card 微調整、端役 NPC 追加、場所詳細追加、editorial notes 追記、state seed 値投入、design への論点追加、没案保存。

**Low Impact（✅ AUTO）**: raw / digest / proposal の保存、Writing Pack 生成、typo・句読点修正、参照リンク追加、README 索引更新。

## 5. 「迷ったら HUMAN」のシグナル

以下が出たら auto_apply_allowed: false —
入力にない情報を「自然な解釈」で補完したくなった / 既存 bible・design・state と矛盾して見える / 同じ事実が2つの異なる version で来ている / intended_unknowns に該当する可能性 / project_principles と衝突するかも / 端役と思った人物が実は重要キャラかも / POV 例外を新設したくなった / 作品固有装置に新規 ID を発番したい。

## 6. 不可逆判断の扱い

プロット根本変更・約束破棄・キャラの死などは自動確定せず、`design/canon-patch-proposals/` に proposal 化 → G-Deliverable で提示。
判断式: 「取り返しがつくか？」YES=自律 / NO=proposal化。

## 7. 衝突発生時のエスカレーション

```
contradiction 発生 → Adapter が contradictions_for_author に積む
→ proposed_resolution_options 2〜3 案（解消はしない）→ author が option 選択 or 新案
→ 決定をログ → 判断に従って bible/design/state 更新
```

**Adapter は絶対に自動解消しない**。

## 8. 失敗パターンと再発防止

| パターン | 防止策 |
|---|---|
| Adapter が「自然な補完」で bible 拡張 | 全提案に source 必須化、source 無し提案は reject |
| AUTO 反映後に author 差し戻し | AUTO with notice カテゴリは review log を残す |
| intentionally_hidden 漏洩 | hidden_from / visible_to 必須タグ付け |
| design に積みっぱなし | weekly review で deadline 設定 |
| 没案が canon に逆流 | rejected ステータス維持 |
| Writing Pack に古い state | pack 生成時に state バージョン記録 |

## 9. 適用順位（衝突したら上位が勝つ）

1. project_principles（design/）— 作品固有方針
2. forbidden_words / sensitive_handling（bible/style_voice）
3. promise（bible/promise）
4. logline / theme（bible）
5. character voice（bible/characters）
6. plot / episode plan（bible/plot）
7. genre overlay（bible/genre_overlay）

## 10. このポリシーの変更

本ポリシー自体の変更も human approval を要する（G-Intake 相当。`design/open-questions.md` 経由で提案）。
