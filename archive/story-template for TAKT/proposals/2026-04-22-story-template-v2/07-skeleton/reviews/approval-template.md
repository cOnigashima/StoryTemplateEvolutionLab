# Approval Review — ep-NN

> **対象**: packet-NNN epNN（または packet 単位）
> **日付**: YYYY-MM-DD
> **起動 skill**: `/release`
> **関連 rule**: `.claude/rules/kakuyomu-policy.md`, `.claude/rules/review-system.md`

---

## 1. 上流 review 結果

- [ ] Typed Review OK — `reviews/typed-review-packet-NNN-epNN.md`
- [ ] Persona Review A（没入）合格 — `reviews/persona-review-A-...md`
- [ ] Persona Review B（構造）合格 — `reviews/persona-review-B-...md`
- [ ] Persona Review C（離脱）合格 — `reviews/persona-review-C-...md`
- [ ] Continuity Review 実施済み（必要な場合） — `reviews/continuity-review-...md`
- [ ] Bridge Review 実施済み（packet 切替時） — `reviews/bridge-review-...md`

## 2. 25 項目 Rubric

- ハードゲート（G1 因果 / G2 話者 / G3 文法 / [G4 約束侵犯]）: 全合格必須
  - G1 因果: / 4
  - G2 話者: / 4
  - G3 文法: / 4
  - G4 約束: / 4
- 総合点: XX / 100
- 判定: 80+ 公開推奨 / 60-79 条件付き公開 / ≤59 公開不可

## 3. kakuyomu-policy 遵守

- [ ] AI 利用タグ: 「AI本文利用」に設定
- [ ] 投稿頻度: 直近 24h で 3 話以内 / 週 15 話以内 / 直近 ep から最小 4h 経過
- [ ] 禁止コンテンツ: 暴力 / 性的 / 著作権 / 差別表現が規約違反レベルでない
- [ ] コンテスト条件: 応募時に該当コンテストの AI 利用条件を確認済み

## 4. 最終散文チェック

- [ ] 誤字脱字スキャン済
- [ ] タイトル確定: `{title}`
- [ ] あらすじ確定（必要なら）
- [ ] タグ設定確定: [タグ一覧]

## 5. 公開後アクション

- [ ] published/ に移動
- [ ] provenance.yaml / reflection-ledger を done 更新
- [ ] learning/current-focus.yaml の `working_ep` を次へ

## 6. 判定

- 結果: `approve / hold / reject`
- hold/reject 理由:
- 次アクション:
