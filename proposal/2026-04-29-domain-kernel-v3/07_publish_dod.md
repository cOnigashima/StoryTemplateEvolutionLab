# Definition of Done (DoD) v3

> **目的**: 「公開してよい状態」を 3 段で固定する。① Episode 公開 ② Packet release ③ Arc / Part 大区分。
> **ガチガチ度**: 各段の MUST 項目は本 v3 で固定。レビュー判定基準は recommend、kakuyomu policy は法的・規約的 MUST。
> **使い方**: チェックリスト。全 MUST に ☑ が入るまで `published/` に移さない。

---

## 1. 3 段構成の理由

| 段 | タイミング | 検証対象 |
|---|---|---|
| DoD-E | Episode 公開直前 | Episode 単体の品質・契約満足・規約適合 |
| DoD-P | Packet release | Packet 全 episode の整合・連続性・公開順 |
| DoD-A | Arc / Part 大区分 | 構造的な反転・伏線回収・読者体験 |

**段差の意味**: DoD-E は「1 話を出してよい」、DoD-P は「1 章を出し終えてよい」、DoD-A は「次の大区分に移ってよい」。

---

## 2. DoD-E: Episode 公開直前

### 2.1 本文成立

```
□ drafts/packet-NNN-epMM-{slug}.md が存在する
□ Multi-Pass Self-Review 全 4 パス済（drafter-preflight）
  □ Pass 1: 因果・認知チェック
  □ Pass 2: Packet / Canon 反映チェック
  □ Pass 3: 読者シミュレーション
  □ Pass 4: 横断チェック（3 話以上まとめ書き時のみ）
□ meta 欄が完成している（因果一段落 / 知識状態台帳 / Gate 0/A/C / 合理化語彙 self-check）
```

### 2.2 Judge 判定

```
□ episode-judge を回した
□ Judge 判定が PASS または FAIL_AUTO_FIX → auto_fix 経由 → 再 PASS
□ NEEDS_HUMAN が無い、または author 介入で解消済
□ REJECT_AND_REGENERATE が無い、または再生成後 PASS
```

### 2.3 Acceptance Contract 充足

```
□ acceptance_contract.must_satisfy の全項目が ☑
□ acceptance_contract.must_not_violate に違反なし
□ acceptance_contract.intended_unknowns が prose で意図通り隠されている
□ acceptance_contract.must_be_clear が prose で読者に伝わっている
□ acceptance_contract.quality_bar を満たしている
  □ rubric_minimum_total（既定 60）以上
  □ hard_gate_minimum（既定 G1/G2/G3 全て 2 以上）
```

### 2.4 typed_review

```
□ Typed Review が実施されている
□ rubric 25 項目のスコアが reviews/typed-review-{date}-{target}.md に記録されている
□ G1 (因果整合) ≥ 2
□ G2 (話者識別) ≥ 2
□ G3 (文法・自然さ) ≥ 2
□ 総合スコア（加重平均）≥ 60
□ 修正必須項目（0 / 1 のスコア）がゼロ、または対処済
```

### 2.5 Continuity 確認

```
□ Continuity Review を実施 or scope 内で確認
□ 直前 episode との時系列整合
□ 直前 episode との物的証拠連続性
□ 関連 character の知識状態が単調
□ 既出固有名詞・設定との衝突なし
□ Foreshadowing Map との整合（仕込/匂/強の進行が想定通り）
```

### 2.6 Ledger 更新

```
□ 本 episode 由来の canon_facts が ledger/canon-facts.yaml に登録
□ 関連 character の character-state が更新
□ 本 episode 内の reveal / 仕込 / 回収が ledger/foreshadowing-status.yaml に反映
□ 本 episode で発生した open-question が ledger/open-questions.yaml に登録
□ author-decisions があれば ledger/author-decisions.yaml に記録
□ 没案があれば ledger/rejected-ideas.yaml に保存
```

### 2.7 kakuyomu policy 適合（公開時 MUST）

```
□ AI 利用タグが正しく設定される予定
  □ AI 本文利用 / AI 本文一部利用 / AI 補助利用 のどれか確定
  □ 本 v3 工場の生成物は基本「AI 本文利用」
□ 投稿頻度が制限内（1 日 3 話 / 4h 間隔 / 週 15 話 以内）
□ 禁止コンテンツが含まれていない
  □ 過度な暴力描写
  □ 性的描写の規約違反
  □ 著作権侵害（引用範囲超え等）
  □ 第三者の権利侵害
  □ 差別的表現
□ コンテスト応募中なら、コンテスト要項に AI 利用の制約がないか確認済
```

### 2.8 author 承認

```
□ author が本 episode を読了
□ author が「公開可」と明示判定
□ hard_lock が付与された
□ approved/packet-NNN-epMM-{slug}.md にコピー
```

### 2.9 公開実施チェックリスト

```
□ 投稿先（カクヨム等）に貼り付け済
□ AI 利用タグ付与済
□ 投稿スケジュール設定 or 即時公開済
□ published/packet-NNN-epMM-{slug}.md にコピー
□ ledger に published 状態反映
```

### 2.10 DoD-E サマリ判定

```
□ 2.1〜2.9 の全 MUST が ☑
```

→ 全部 ☑ なら DoD-E **満足**。Episode を `published/` に移し、公開実施。

---

## 3. DoD-P: Packet release

Packet 内の全 Episode が DoD-E を満たした後の packet 全体の judgment。

### 3.1 全 Episode 公開済

```
□ packet 配下の全 Episode が DoD-E 満足
□ 全 Episode が published/ にある
□ 公開順序が unit_tree の予定と整合
```

### 3.2 packet-assembly-review

```
□ packet-assembly-review が実施済
□ packet 内の Episode 間接続に齟齬なし
□ 重複説明なし
□ テンポ（cadence）が baseline 比率内
□ 局所矛盾なし
□ 情報開示順が reveal_plan と整合
□ packet 末尾の引きが next packet の entry_state と整合
```

### 3.3 promise 紐付け検証

```
□ packet が引き受けた promise 項目が prose で実装されている
□ promise.evidence_target が本 packet を指していた項目について、本 packet で果たされた
  または、果たされなかった理由が ledger に記録
```

### 3.4 Bridge Review

```
□ 次 packet（次 packet が設計済の場合）への Bridge Review 実施
□ entry/exit の連続性確認
□ carryover 項目の確定
```

### 3.5 Packet 単位 Continuity

```
□ packet 全体での character 知識状態台帳が単調
□ packet 全体での foreshadow 進行が想定通り
□ packet 全体での timeline が連続
```

### 3.6 ledger reconciliation

```
□ packet 完了時点の ledger snapshot を取得
□ 想定との差分を確認
□ 設計時意図と実装結果のずれを open-questions に記録（あれば）
□ 続く packet への影響を design-debt に記録（あれば）
```

### 3.7 author 承認

```
□ author が packet 全体をレビュー
□ packet_soft_lock → hard_lock
```

### 3.8 DoD-P サマリ判定

```
□ 3.1〜3.7 の全 MUST が ☑
```

→ 全部 ☑ なら DoD-P **満足**。次 Packet の DoR-C 検討に入れる。

---

## 4. DoD-A: Arc / Part 大区分

Arc 完結 or Part 完結時の判定。

### 4.1 全 Packet 完了

```
□ Arc 配下の全 packet が DoD-P 満足
□ 全 packet が hard_lock
```

### 4.2 arc-through-review

```
□ arc-through-review 実施
□ 中期的な問いに答えが出ている（or 次 Arc に明示的に持ち越し）
□ 主反転が prose で実装され、読者に届いている
□ 関係性変化が起きている（kernel.protagonist_vector の need 方向に進行）
□ 中だるみがない
□ Part への貢献が明確
```

### 4.3 伏線回収度

```
□ 本 Arc 中に回収予定だった伏線が回収済
  またはずらして次 Arc 回収にする決定が ledger に記録
□ 新規仕込みの伏線が次 Arc に引き継ぎ可能な状態
□ Foreshadowing Map と現状が整合
```

### 4.4 Part 進行度（Part 完結時のみ）

```
□ Part 開始時 → 終了時の不可逆変化を確認
  □ 主人公の変化
  □ 世界の変化
  □ 読者理解の変化
□ 次 Part への接続が prose で示唆されている（or 完結なら満足感がある）
□ Part 末尾の引きと満足感が両立
```

### 4.5 Reader Persona 検証（推奨）

```
□ Persona A (没入読者) のレビュー実施 or simulate
□ Persona B (構造分析読者) のレビュー実施 or simulate
□ Persona C (離脱しやすい読者) のレビュー実施 or simulate
□ 3 persona 横断の合成サマリ作成
```

### 4.6 manuscript-final-review（Part 完結時のみ、optional）

```
□ Part 単独で見たとき、作品全体の中での意義が確認できる
□ 文体統一が崩れていない
□ Promise 全項目に対する進捗確認
```

### 4.7 author 承認

```
□ author が Arc / Part 全体をレビュー
□ 完了承認
```

### 4.8 DoD-A サマリ判定

```
□ 4.1〜4.7 の全 MUST が ☑
□ Part 完結なら 4.4 / 4.6 も ☑
```

→ 全部 ☑ なら DoD-A **満足**。次 Arc / Part の設計に入れる。

---

## 5. DoD の階層関係

```
DoD-A (Arc / Part 完結)
  └── DoD-P (各 Packet release)
        └── DoD-E (各 Episode 公開)
              └── 公開済
```

DoD-E 不満足のまま Episode を published/ に移すことは禁止。
DoD-P 不満足のまま Packet を完了扱いすることは禁止。
DoD-A 不満足のまま次 Arc / Part に進むことは推奨されない（連載中は飛ばす場合あり、debt として明示）。

---

## 6. DoD と kakuyomu policy の関係

`07_publish_dod.md` §2.7 で kakuyomu policy 適合を MUST にしている。理由:

- AI タグ未設定 → 規約違反
- 投稿頻度超過 → アカウント停止リスク
- 禁止コンテンツ → 削除・指導リスク

これらは **Layer 4 release の絶対条件**。kernel / craft レベルの問題ではないが、release を止める根拠になる。

---

## 7. DoD 判定の自動化（次セッション）

将来的に TAKT step として実装する想定:

```yaml
# .takt/workflows/dod-check-episode.yaml（次セッション設計）
name: dod-check-episode
steps:
  - name: contract-satisfaction-check
    persona: judge
    inputs:
      - drafts/packet-NNN-epMM-{slug}.md
      - reviews/contracts/packet-NNN-epMM-{slug}.contract.yaml
    rules:
      - condition: "All must_satisfy met"
        next: continuity-check
      - condition: "Violation detected"
        next: report-and-stop
  
  - name: continuity-check
    persona: continuity-checker
    rules:
      - condition: "PASS"
        next: kakuyomu-policy-check
      - condition: "Violation detected"
        next: report-and-stop
  
  - name: kakuyomu-policy-check
    persona: policy-validator
    rules:
      - condition: "Compliant"
        next: ledger-update-proposal
      - condition: "Non-compliant"
        next: report-and-stop
  
  - name: ledger-update-proposal
    persona: ledger-keeper
    rules:
      - next: human-approval-gate
  
  - name: human-approval-gate
    persona: author-notifier
    rules:
      - next: COMPLETE
```

ただし、本 v3 では仕様の明文化のみで実装は次セッション。

---

## 8. DoD 不満足時の対応

DoD が満たされていないと判明した場合:

### DoD-E 不満足

- Judge FAIL_AUTO_FIX → auto_fix_loop で修正 → 再 Judge
- Judge NEEDS_HUMAN → author 介入 → 修正 → 再 Judge
- Judge REJECT_AND_REGENERATE → 候補を捨てて episode-draft-tournament 再走
- Continuity Review fail → 該当 episode を unlocked に戻して修正

### DoD-P 不満足

- 個別 Episode の DoD-E 不満足が原因 → 該当 Episode の DoD-E に戻す
- packet-assembly-review fail → packet 内修正
- Bridge Review fail → 次 packet 設計に戻す

### DoD-A 不満足

- arc-through-review fail → packet レベルの修正 or arc 構造変更
- 反転が機能していない → arc-strategy-tournament で構造案再競争
- Reader Persona 検証 fail → 該当 persona のフィードバックに従って修正

**勝手にスキップしない**。DoD 不満足のまま公開しない。

---

## 9. DoD と Lock 状態の対応

| Lock 状態 | 対応 DoD | 公開可否 |
|---|---|---|
| unlocked | なし | 公開不可 |
| soft_lock | DoD-E の Judge PASS まで | 公開不可 |
| packet_soft_lock | DoD-P の packet-assembly-review PASS まで | 公開検討可 |
| hard_lock | DoD-E 全項目 + author 承認 | 公開可 |
| published | DoD-E + 公開実施 | 公開済 |

公開できるのは **hard_lock 以降**。
