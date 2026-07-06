# Human Approval Policy（汎用版）

> 何を AI / Adapter が自動反映してよく、何が人間判断必須かを 1 枚で固定する。
> 適用: update_proposal の処理、writing_pack 生成、draft 修正、各種反映。
> 改訂: pilot 運用で誤判定が出たら更新する。

---

## 0. 基本姿勢

- **デフォルトは「人間判断必要」**。auto_apply_allowed は例外として明示的に true
- **不可逆性のあるものは絶対に自動反映しない**（bible canon 確定 / 公開実施 / 没案削除）
- **status 不一致が出たら author に上げる**
- **AI 提案の根拠を必ず source 参照で示す**

---

## 1. 操作カテゴリと判定

### A. ファイル新規作成

| 操作 | auto OK | 理由 |
|---|---|---|
| inbox/planning_sessions/ への raw 保存 | ✅ AUTO | 受信ログ |
| synthesis/session_digests/ への digest 出力 | ✅ AUTO | 加工生成、bible 触らない |
| synthesis/update_proposals/ への proposal 出力 | ✅ AUTO | あくまで「案」 |
| bible/{anywhere}.md の新規作成 | ❌ HUMAN | canon 化、不可逆 |
| design/{anywhere}.md の新規作成 | ⚠️ AUTO with notice | 仮の置場 |
| state/{anywhere}.yaml の新規作成 | ⚠️ AUTO with notice | seed 投入時のみ |
| writing/episode_packs/{ep}/*.md の新規作成 | ✅ AUTO | bible/state 由来 pack |
| drafts/episodes/{ep}.md の新規作成 | ⚠️ AUTO（content は別判定） | ファイルのみ |

### B. 既存ファイルへの変更

| 操作 | auto OK |
|---|---|
| bible/ 本文書き換え | ❌ HUMAN |
| bible/ typo 修正のみ | ⚠️ AUTO with notice |
| design/open_design_questions.md への append | ✅ AUTO |
| design/author_decisions.md への append | ❌ HUMAN |
| design/project_principles.md の変更 | ❌ HUMAN |
| design/editorial_notes.md への append | ✅ AUTO |
| state/timeline.yaml への append（episode 公開時） | ⚠️ AUTO with notice |
| state/character_states.yaml の更新 | ⚠️ AUTO with notice |
| state/foreshadowing.yaml の status 更新 | ⚠️ AUTO with notice |
| state/rejected_ideas.md への append | ✅ AUTO |

### C. 削除・破棄

| 操作 | auto OK |
|---|---|
| 任意ファイルの削除 | ❌ HUMAN（厳格） |
| state/rejected_ideas.md からの除去 | ❌ HUMAN |
| draft の上書き保存 | ❌ HUMAN（前世代を superseded/ へ） |

### D. 公開系

| 操作 | auto OK |
|---|---|
| approved/ への移動 | ❌ HUMAN |
| カクヨム等への投稿実施 | ❌ HUMAN（必ず） |
| AI タグ設定 | ❌ HUMAN |

---

## 2. status 別判定

| status | bible | design | state |
|---|---|---|---|
| filled | ❌ HUMAN | ⚠️ AUTO with notice | ⚠️ AUTO with notice |
| tentative | ❌ HUMAN | ✅ AUTO | ✅ AUTO |
| candidate | ❌ HUMAN | ❌ HUMAN | ❌ HUMAN |
| open | ❌ HUMAN | ✅ AUTO | ✅ AUTO |
| contradiction | ❌ HUMAN（必ず） | ❌ HUMAN | ❌ HUMAN |
| needs_author_decision | ❌ HUMAN（必ず） | ❌ HUMAN | ❌ HUMAN |
| deferred | ⚠️ AUTO with notice | ✅ AUTO | ✅ AUTO |
| intentionally_hidden | ❌ HUMAN（漏洩リスク） | ⚠️ AUTO | ⚠️ AUTO |
| rejected | n/a | n/a | ⚠️ AUTO with notice |

---

## 3. 影響度別判定

### High Impact（1 つでも該当 → ❌ HUMAN）

- premise / reader_promise / theme / genre 変更
- 主要キャラの動機 / wound 変更
- POV 方針の変更
- 文体方針の変更
- arc の主反転変更
- promise の追加・削除
- intended_unknowns の追加・削除
- forbidden_words の追加・削除
- 章末資料の意味変更
- 作品固有装置（三層対応 等）の構造変更

### Medium Impact（⚠️ AUTO with notice + 24h 以内通知）

- 単一 episode の scene_card 微調整
- 端役 NPC の追加
- 場所詳細追加
- 章末資料テンプレ追加
- editorial_notes 追記
- state seed 値投入
- design への論点追加
- 没案保存

### Low Impact（✅ AUTO）

- inbox / synthesis への保存
- writing_pack 生成
- typo / 句読点修正
- ファイル参照リンク追加
- README 索引更新

---

## 4. 「迷ったら HUMAN」のシグナル

以下が出たら auto_apply_allowed: false:

- 入力にない情報を「自然な解釈」で補完したくなった
- 既存 bible / design / state と矛盾しているように見える
- 同じ事実が 2 つの異なる version で来ている
- intended_unknowns に該当する可能性
- project_principles と衝突するかも
- 端役と思った人物が実は重要キャラかも
- 章末資料の意味を変えるかも
- POV 例外を新設したくなった
- 作品固有装置（三層対応 等）に新規 ID 発番したい

---

## 5. Human が見るタイミング

| 頻度 | 内容 |
|---|---|
| Daily | 当日の session_digest と update_proposal を 1 度通読、AUTO with notice 確認、approve/revise |
| Weekly | bible/design/state 全体整合、衝突解消、design→bible 昇格判断 |
| Per Episode | writing_pack 確認、acceptance_checklist の human_required 現実性、公開前は本文 + checklist |
| Per Arc | bible/state/design 差分 review、promise 進捗、文体ドリフト |

---

## 6. 衝突発生時のエスカレーション

```
contradiction 発生
  ↓
Adapter が contradictions_for_author に積む
  ↓
proposed_resolution_options 2〜3 案（解消はしない）
  ↓
author が読む
  ↓
author が option 選択 or 新案
  ↓
author_decisions.md にログ
  ↓
判断に従って bible/design/state 更新
```

**Adapter は絶対に自動解消しない**。

---

## 7. 失敗パターンと再発防止

| パターン | 防止策 |
|---|---|
| Adapter が「自然な補完」で bible 拡張 | 全提案に source 必須化、source 無し提案は reject |
| AUTO 反映後に author 差し戻し | AUTO with notice カテゴリは review log を残す |
| intended_hidden 漏洩 | hidden_from / visible_to 必須タグ付け |
| design に積みっぱなし | weekly review で deadline 設定 |
| 没案が canon に逆流 | rejected ステータス維持 |
| writing_pack に古い state | pack 生成時に state バージョン記録 |

---

## 8. 適用順位（衝突したら）

1. project_principles（design/）— 作品固有方針
2. forbidden_words / sensitive_handling（bible/style_guide）
3. promise（bible/reader_promise）
4. premise / theme（bible）
5. character voice（bible/characters）
6. plot / episode_plan（bible/plot）
7. genre overlay（bible/genre）

上位ほど強い。下位は上位を覆さない。

---

## 9. このポリシーの変更

本ポリシー自体の変更も human approval を要する。提案は `design/approval_policy_changes.md` 経由。
