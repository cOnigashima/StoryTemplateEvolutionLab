# Monitoring Dictionary — Generic Guide

作品固有の `monitoring-dictionary.md`（反復 motif / withhold / disclose の grep 用辞書）を立てる際の **generic テンプレート** と運用規則。

原型は `works/villainess-coc-survival-with-cheating/.claude/rules/monitoring-dictionary.md`。本ファイルは作品固有情報を抜き、骨組みのみを提示する。

---

## 1. 作品固有ファイルが必要になる条件

以下のいずれかが該当する作品:
- 反復 motif を 1 本以上 canon 化している（紅茶5段 / 鐘3回等）
- packet / arc 境界で withhold 対象となる固有名詞が卓/段階で切り替わる
- reviewer に grep 検証を課す（typed review PART B Gate B 起動）

該当しない作品（例: 短編、単 packet 作品）は本辞書を作らなくて良い。

---

## 2. 作品側ファイルの最低構成

`.claude/rules/monitoring-dictionary.md` を作品側に作り、以下 6 セクションを置く:

```markdown
# Monitoring Dictionary — {work-slug}

## 1. 監査キーワード辞書（境界別）
| 境界 | 主系列キーワード | 従属チェック |

## 2. motif キーワードセット（grep 用）
| motif | 最低限の grep キーワード |

## 3. canon motif 定義（段階・意味論）
### 3.1 motif-A（例: 紅茶5段）
### 3.2 motif-B（例: ですわぁ3段）
...

## 4. draft meta 欄への記録項目

## 5. 辞書更新手順

## 6. 関連
```

---

## 3. 境界（packet / arc / 卓）の概念

villainess-coc は「卓」という作品固有境界で段階切替する。generic には以下を「境界」と呼ぶ:

- packet 境界（最も一般的）
- arc 境界
- 作品固有の劇的段階（villainess-coc の「卓」、連作物の「巻」等）

境界毎に「主系列キーワード」と「従属チェック（前境界の語）」を持つ。

---

## 4. 主系列キーワードと従属チェック

- **主系列キーワード**: 現行境界で withhold すべき語セット
- **従属チェック**: 前境界の語。完全禁止ではなく「前境界接続ビートでの既知引用は許容」

grep は両方を走らせ、prose/meta を分けて記録する。

---

## 5. motif 段階の設計原則

（詳細は `craft/motif-operations.md`）

- 段数は 3〜5 が扱いやすい
- 単調進行。後退は因果説明必須
- 同一ビート内の段階同居を避ける
- 境界開幕話に 1 段目（余裕/基調）を置くと序盤トーン軽く保てる

---

## 6. 辞書と review の接続

- drafter: preflight Pass 2 で grep 実行 → 該当 hit を draft meta の canon motif 出現ログに記録
- reviewer: typed review PART B Gate B で同辞書を参照し再 grep → hit 差分を確認
- 差分があれば drafter 側の記録ミス、無ければ判定材料として使う

---

## 7. 辞書更新手順

新境界を freeze する時:
1. §1 に新境界行を追加（主系列 / 従属）
2. §2 に新 motif 行を追加（必要なら）
3. §3 に新 motif 定義節を追加
4. packet freeze 文書と相互参照リンクを張る
5. 更新理由を learning/ に残す

---

## 8. 関連

- `craft/motif-operations.md`（generic motif 運用原理）
- `.claude/rules/review-system.md`（grep 検証ルール）
- `.claude/rules/drafter-preflight.md`（drafter 側 grep 運用）
- `works/villainess-coc-survival-with-cheating/.claude/rules/monitoring-dictionary.md`（実装例）
