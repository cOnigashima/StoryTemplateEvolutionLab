# 02 Domain Model — 56 語のユビキタス言語 Card 集

> **役割**: 本提案で参照されるすべての概念の正本。後続の文書 (03 / 04 / 05 / 06 / 07 / 08) はこの Card 集を参照する。
> **書式**: 英名 + Category + Definition + Role + Boundary + Examples + Lives in + Cousins の 8 フィールド。
> **読み順**: Section 1（メタ）→ Section 2（単位軸）→ Section 3（格納域）→ Section 4（Bible Facet）→ Section 5-12（その他）。

---

## 目次

- Section 1. メタ用語（Facet / Layer の軸自体）
- Section 2. 単位軸（Manuscript / Part / Arc / Packet / Episode / Scene / Beat / Transformation Curve）
- Section 3. 格納域（Bible / Canon / Design / State / Ledger / Patch / Continuity）
- Section 4. Bible Facet（Logline / Promise / Theme / Rules / Style Voice / Cadence / World / Character / System / Timeline / Sample Scene / Plot / Foreshadowing Map / Reveal Plan / Motif / Genre Overlay / Project Override）
- Section 5. Design Artifact（Open Question / Design Debt / Canon Patch Proposal / Rejected Idea）
- Section 6. State Artifact（Decision Log / Contradiction Log / Timeline State / Character State / Implementation Ledger / Backlog）
- Section 7. Intake Pipeline（Seed / Digest / Update Proposal / Intake Adapter）
- Section 8. Writing Pipeline（Writing Adapter / Writing Pack / Scene Card / Acceptance Contract）
- Section 9. Documentation（Walkthrough / README）
- Section 10. Review（Review / Typed / Bridge / Continuity / Persona / Packet Freeze / Approval / Design Audit + Rubric）
- Section 11. Craft（Craft / Framework / Framework Lens）
- Section 12. Status（Status meta + 11 値）
- Section 13. Process / Misc（Pitch / Beat Sheet / Prose）
- Section 14. Deprecated（Premise / Backlog 旧用法 / Bundle / Chapter 内部 / Review 単独）

---

## Section 1. メタ用語

### Term: Facet
| field | value |
|---|---|
| Japanese | 面 / 様相 |
| Category | **Meta-Category**（用語分類のメタ） |
| Definition | An aspect of the work that has its own internal logic, vocabulary, and stability — independent of the structural unit hierarchy. |
| Role | Bible / Design / State の中身を facet で分割する第 2 軸（Unit 軸とは独立）。 |
| Boundary | **Unit とは別軸**（Manuscript / Part / Arc / Packet / Episode / Scene / Beat）。Facet は「何について」、Unit は「どの範囲」。両者を交差した資料はあるが、軸自体は別物。判定ルール: 「その資料が消えたら、まず困るのは facet の理解か、unit の構造か」。 |
| Examples | World / Characters / Rules / System / Timeline / Plot / Samples / Cadence / Foreshadowing Map |
| Lives in | （概念のみ。各 Facet の物理位置は `bible/{facet_name}/`） |
| Cousins | Unit, Layer, Storage Layer |

### Term: Layer
| field | value |
|---|---|
| Japanese | レイヤー |
| Category | **Meta-Category**（リポジトリの階層） |
| Definition | One of seven canonical strata in the system: 0 Intake / 1 Core Authoring / 1.5 Adapter / 2 Review-Learning / 3 Craft / 4 Release / R Runtime. |
| Role | リポジトリ全体の責任分担を 7 階層に切る。各 Layer は他 Layer の責務を侵食しない。 |
| Boundary | **Facet とは別軸**: Layer は「いつ / どの段階で扱うか」、Facet は「何について扱うか」。**Layer R は opt-in**: TAKT / 自動化が無い構成では Layer 0-4 で完結する。 |
| Examples | "Bible は Layer 1"、"Intake Adapter は Layer 1.5"、"Typed Review は Layer 2" |
| Lives in | （概念のみ） |
| Cousins | Facet, Adapter, Storage Layer |

---

## Section 2. 単位軸（Unit）

### Term: Manuscript
| field | value |
|---|---|
| Japanese | 作品 / 本編 |
| Category | **Unit**（size class, top） |
| Definition | A complete work — the whole novel as a single bounded artifact. |
| Role | 作品全体の境界。Logline / Promise / unit_tree が記述する対象。 |
| Boundary | "Series" ではない（複数 Manuscript の集合がシリーズ）。"Volume / Book" でもない（Manuscript = 1 作品）。 |
| Examples | "アイエー社会"、"佐山レンジ長編" |
| Lives in | 1 work directory = 1 Manuscript。`story/kernel.yaml` に紐付く。 |
| Cousins | Part, Series（外部概念） |

### Term: Part
| field | value |
|---|---|
| Japanese | 第一部・第二部 |
| Category | **Unit**（size class, optional） |
| Definition | A top-level division of the Manuscript marking an irreversible thematic / temporal threshold. |
| Role | 大規模長編で、不可逆な変化の前後を分ける。短編・中編では省略可。 |
| Boundary | **Arc とは違う** — Part は**不可逆性**で切る、Arc は**問いの開始と決着**で切る。Part 境界 =「もう前には戻れない」。 |
| Examples | "第一部 矯正学園篇" / "第二部 解体篇" |
| Lives in | `arcs/series-overview.md` 内に Part ブロック、または `arcs/part-{n}.md` |
| Cousins | Manuscript, Arc |

### Term: Arc
| field | value |
|---|---|
| Japanese | アーク（単位） |
| Category | **Unit**（size class, mid） |
| Definition | A mid-scale narrative segment containing one central question opened and closed. |
| Role | 中核問いの提示 → 主反転 → 決着の一塊。複数 Packet を含む。 |
| Boundary | **"Character Arc" / "Change Arc" とは別物**。後者は "shape of transformation" であり Unit ではない。Unit としての Arc は容器、shape としての Arc は曲線。区別のため shape 側は **Transformation Curve** と呼ぶ。 |
| Examples | arc-01「最初の配属」、arc-02「責任の偽装」 |
| Lives in | `arcs/arc-{n}.md`（unit としての Arc） |
| Cousins | Part, Packet, **Transformation Curve**（同名衝突警告） |

### Term: Packet
| field | value |
|---|---|
| Japanese | 章束 |
| Category | **Unit**（size class, between Arc and Episode） |
| Definition | A frozen bundle of consecutive Episodes scoped together for design purposes. |
| Role | 1 つの設計責務（purpose / disclose / withhold / guardrails）の単位。frozen にしてから drafting 開始。 |
| Boundary | Arc より小さい / Episode より大きい。**"Bundle" 禁止語**（旧称）。**"Chapter"** は内部禁止（公開表示時のみ可）。 |
| Examples | packet-001-first-assignment（5 episodes） |
| Lives in | `packets/{exploring,scoped,frozen}/packet-{NNN}-{slug}.yaml` |
| Cousins | Arc（親）, Episode（子） |

### Term: Episode
| field | value |
|---|---|
| Japanese | エピソード / 話 |
| Category | **Unit**（size class, publishing-atomic） |
| Definition | The smallest publishable unit — one self-contained installment. |
| Role | カクヨムなどへの公開単位。1 話 = 1 Episode。 |
| Boundary | "Chapter" は内部禁止。Scene と違い、Episode は**公開境界**を持つ。1 Episode は複数 Scene を含む。 |
| Examples | ep001, ep072 |
| Lives in | `scenes/slotted/{ep_id}.md`（設計）, `drafts/episodes/{ep_id}-{slug}.md`（本文） |
| Cousins | Packet（親）, Scene（子） |

### Term: Scene
| field | value |
|---|---|
| Japanese | シーン |
| Category | **Unit**（size class, within-episode） |
| Definition | A localized dramatic confrontation with one focal goal, one obstacle, and one turn. |
| Role | Episode の中の 1 単位の衝突。場所・時間が固定された塊。 |
| Boundary | **"Scene Card" は別物**（Scene の設計成果物、Artifact カテゴリ）。"Sample Scene" も別物（bible/samples/ の文体見本）。 |
| Examples | "移送車内の押し問答"、"低速聴聞冒頭" |
| Lives in | drafts 内の prose の一部として実装。設計は Scene Card に分離。 |
| Cousins | Episode（親）, Beat（子）, **Scene Card**（同名警告）, **Sample Scene**（同名警告） |

### Term: Beat
| field | value |
|---|---|
| Japanese | ビート |
| Category | **Unit**（size class, smallest） |
| Definition | The smallest story moment — a single action, line, or shift that changes the situation. |
| Role | drafter が文章を組み立てる最小粒度。知識状態台帳の 1 行に対応する。 |
| Boundary | **"Beat Sheet" は別物**（craft 道具、Save the Cat 等で使う設計シート、Artifact）。 |
| Examples | "湊が黙って書類を伏せる"、"乃々の名前が口から漏れる" |
| Lives in | 通常はファイル化しない。drafter-preflight の知識状態台帳でビート単位列挙。 |
| Cousins | Scene（親）, **Beat Sheet**（同名警告） |

### Term: Transformation Curve
| field | value |
|---|---|
| Japanese | 変化形 |
| Category | **Facet attribute**（kernel #6 change_model に従属） |
| Definition | The qualitative shape of transformation a character or situation undergoes — growth, fall, flat, circular, mixed. |
| Role | 「キャラがどう変わるか」の曲線記述。kernel.change_model の値域。 |
| Boundary | Unit としての Arc とは独立。Transformation Curve は Episode 内でも観測できる。 |
| Examples | "growth"（成長）、"fall"（転落）、"circular"（円環） |
| Lives in | `story/kernel.yaml` の change_model、`bible/characters/{char}.md` 内 |
| Cousins | Arc（同名衝突）, Character Arc（= Transformation Curve の人物別実例） |

---

## Section 3. 格納域（Storage Layer）

### Term: Bible
| field | value |
|---|---|
| Japanese | バイブル / 公式設定 |
| Category | **Storage Layer**（安定設定の格納域） |
| Definition | The frozen, author-approved set of stable creative decisions that do not change without an explicit Patch. |
| Role | 設計者 / drafter / reviewer すべての参照正本。draft 中は read-only として扱う。 |
| Boundary | 揺れているもの（→ Design）、書きながら動くもの（→ State）、レビュー観点の概念（→ Continuity）は Bible に置かない。**"Canon" と概ね同義**だが、本書では場所を指す語として "Bible" を、性質を指す語として "Canon" を使う。**Draft（本編 prose）は Bible に置かない**（Sample Scene のみ例外）。 |
| Examples | `bible/world/`, `bible/characters/`, `bible/plot.md`, `bible/samples/` |
| Lives in | 各 work の `bible/` 配下 |
| Cousins | Canon, Design, State, Patch |

### Term: Canon
| field | value |
|---|---|
| Japanese | 正典 / 公式設定 |
| Category | **Property / Quality**（性質を表す形容） |
| Definition | The property of being officially established as part of the work's stable truth — applies to facts, decisions, or settings. |
| Role | 「これは canon である / canon になった / canon ではない」のように形容詞的に使う。 |
| Boundary | Bible（場所）と区別。Canon は性質、Bible はその性質を持つものの格納域。**"Canon" 単独でディレクトリ名にしない**。 |
| Examples | "湊が中間 ID を持つことは canon"、"白紙日制度は canon-anchored" |
| Lives in | （概念のみ） |
| Cousins | Bible, Patch（canon 化の手続き） |

### Term: Design
| field | value |
|---|---|
| Japanese | デザイン / 揺れる設計 |
| Category | **Storage Layer**（揺れる候補の格納域） |
| Definition | Tentative or shaky design decisions awaiting author judgment, kept distinct from Bible to avoid premature canonization. |
| Role | 提案・候補・author 判断待ちのものを保存。Bible 化は Patch を経る。 |
| Boundary | Bible は確定、Design は未確定。Design に書いたものを直接 draft で参照することは避ける（参照したら Bible 化候補が遅延している兆候）。 |
| Examples | `design/project_principles.md`, `design/open-questions.md`, `design/canon-patch-proposals/`, `design/rejected-ideas.md` |
| Lives in | 各 work の `design/` 配下 |
| Cousins | Bible, Patch, Open Question |

### Term: State
| field | value |
|---|---|
| Japanese | 状態 / 動的台帳 |
| Category | **Storage Layer**（制作中に動く事実の格納域） |
| Definition | The category of dynamic production data — anything that changes as the writing progresses, including timelines, character knowledge state, foreshadowing implementation, and decision logs. |
| Role | draft / review / Patch によって都度更新される。Bible（frozen）と区別される。 |
| Boundary | Bible（書く前に決まる）と区別。**書いた後にだけ書き換わる**ものは State。**実装履歴**を持つ State ファイルは Ledger 形式を取る。 |
| Examples | `state/timeline-state.yaml`, `state/character-states.yaml`, `state/foreshadowing-implementation.yaml` |
| Lives in | 各 work の `state/` 配下 |
| Cousins | Bible, Ledger（State の表現形式）, Continuity |

### Term: Ledger
| field | value |
|---|---|
| Japanese | 台帳 / ログ |
| Category | **File Format / Pattern**（State 配下のファイル形式） |
| Definition | An append-only journal file format — used for audit trails like canon patches, contradictions, reveal implementations, and motif progressions. |
| Role | 履歴を時系列で残し、後から「いつ何が起きたか」を巻き戻せるようにする。State 配下のファイルの 1 形式。 |
| Boundary | **Ledger は State の sibling ではなく、State の中の表現形式**。State には Ledger 形式と非 Ledger 形式（現在値スナップショット）の両方が存在する。**"Ledger" 単独でディレクトリ名にしない**。 |
| Examples | `state/canon-patch-log.yaml`, `state/contradiction-log.yaml`, `state/reveal-implementation-ledger.md` |
| Lives in | `state/` 配下のうち、append-only を選んだファイル |
| Cousins | State, Patch, Continuity |

### Term: Patch
| field | value |
|---|---|
| Japanese | パッチ / canon 改訂 |
| Category | **Process** + **Artifact** |
| Definition | A proposed amendment to Bible content, tracked through a proposal → approval → applied lifecycle and recorded in a Patch Ledger. |
| Role | Bible を直接書き換えず、Patch を経由する手続き。後から「何が canon になり、何が rejected されたか」を巻き戻せる。 |
| Boundary | Patch そのもの（提案）は **Design 配下**（`design/canon-patch-proposals/`）、適用履歴は **State 配下の Ledger**（`state/canon-patch-log.yaml`）。Bible 自体には Patch のメタ情報を書かない。 |
| Examples | "Patch #042: 真耕特区の所在を東北から東海に変更" |
| Lives in | 提案: `design/canon-patch-proposals/{patch_id}.md`、ログ: `state/canon-patch-log.yaml` |
| Cousins | Bible, Canon, Design, Ledger |

### Term: Continuity
| field | value |
|---|---|
| Japanese | 連続性 / 整合性 |
| Category | **Review Concern**（レビュー観点の概念） |
| Definition | The property that knowledge state, timeline, physical facts, and character behavior remain coherent across episodes and units. |
| Role | Continuity Review の対象軸。Bible と State の整合性、ならびに draft 間の一貫性を監視する。 |
| Boundary | **ファイル / ディレクトリ名にしない**。Continuity は性質。実装は State の各台帳と Bible の参照で担保される。違反が見つかったら Contradiction として State Ledger に記録する。 |
| Examples | "ep05 で湊が知っていた情報を ep08 で初めて知ったかのように書いた → continuity violation" |
| Lives in | （概念のみ。Continuity Review は `reviews/continuity-review-{ep}.md` に出る） |
| Cousins | Contradiction, State, Bible, Review |

---

## Section 4. Bible Facet（17）

### Term: Logline（旧 Premise を置き換え）
| field | value |
|---|---|
| Japanese | ログライン / 一行要約 |
| Category | **Kernel Item**（kernel #1） + **Bible Facet** |
| Definition | A 1-2 sentence summary capturing the work's central concept — protagonist + situation + dramatic tension — pitchable on its own. |
| Role | 作品を 1 文で同定する。pitch / 販売 / 検索の入口。 |
| Boundary | **Promise とは別**: Promise は読者向け契約（複数項目）、Logline は作品同定（1 文）。**Theme とは別**: Theme は問い、Logline は要約。**Egri-Premise（thematic argument）とは別**: 本書では Egri 流の "premise" は使わず、**Theme** に吸収する。 |
| Examples | "147 の記録官が、昇進のために完成させたい真実が、兄妹を国家へ売る文書だと知って、最後に書かない一行を選ぶ話" |
| Lives in | `bible/logline.md` |
| Cousins | Theme, Promise, Hook, Pitch |

### Term: Promise
| field | value |
|---|---|
| Japanese | 読者への約束 / 作品の核（外向き） |
| Category | **Kernel Item**（kernel #2） + **Bible Facet** |
| Definition | A short list of guarantees the work makes to the reader — what the work commits to deliver and not to break. |
| Role | drafter / reviewer の最上位制約。違反は最重度レビュー指摘。 |
| Boundary | **Logline とは別**: Logline は作品同定（IS）、Promise は読者契約（WILL BE）。**Theme とは別**: Theme は問い、Promise は約束（守る側）。**Project Override とは別**: Project Override は内向き例外、Promise は外向き契約。 |
| Examples | "和解で閉じない"、"主人公は反省しない"、"伏線は本文内で全回収"、"暴力グロテスクなし" |
| Lives in | `bible/promise.md` |
| Cousins | Logline, Theme, Premise（旧称、廃止）, Project Override |

### Term: Theme
| field | value |
|---|---|
| Japanese | 主題 / 問い |
| Category | **Bible Facet** |
| Definition | The central question or argument the work explores — the "what is this work asking?" that subordinates plot and character to a unifying inquiry. |
| Role | drafter / reviewer が「この場面はテーマに資するか」を判定する根拠。Promise / Logline と並ぶ最上位制約。 |
| Boundary | **Promise とは別**: Promise は読者契約、Theme は問い。**Logline とは別**: Logline は要約、Theme は核心問い。 |
| Examples | "責任は誰のものか？"、"自己正当化の暴力は処罰されるか？" |
| Lives in | `bible/theme.md` |
| Cousins | Promise, Logline, Critical Intent |

### Term: Rules
| field | value |
|---|---|
| Japanese | 文体・禁則 |
| Category | **Bible Facet** |
| Definition | The set of binding stylistic and content rules that all prose in the work must obey — POV, tense, register, forbidden vocabulary, dialogue conventions. |
| Role | drafter が prose を書くときの**破ってはいけない線**。違反は文体ドリフト / レビュー指摘の最重度。 |
| Boundary | **Style Voice とは別**: Style Voice は「目指す声」、Rules は「破ってはいけない線」（禁則）。**Project Override とは別**: Project Override は構造・展開レベルの例外、Rules は文体・禁則。**Genre Overlay とは別**: Genre Overlay はジャンルの一般制約、Rules は本作品の固有制約。 |
| Examples | "三人称一元・過去形固定"、"会話末『〜だわ』禁止"、"暴力描写は心理に置換" |
| Lives in | `bible/rules.md`（デフォルト 1 ファイル、肥大時 `bible/rules/{style.md, forbidden.md, dialogue.md}` に分割） |
| Cousins | Style Voice, Genre Overlay, Project Override |

### Term: Style Voice
| field | value |
|---|---|
| Japanese | 文体 / 声 |
| Category | **Kernel Item**（kernel #10） + **Bible Facet** |
| Definition | The narrative voice characteristics — POV, tense, register, sentence rhythm, narrative temperature, allowed and forbidden vocabularies. |
| Role | drafter が「目指す声」の正本。**Sample Scene が実装の見本帳、Rules が破ってはいけない線**。3 者一組で声を担保する。 |
| Boundary | **Rules とは別**: Rules は禁則（破るな）、Style Voice は目指す声（こうあれ）。**Sample Scene とは別**: Style Voice は宣言、Sample Scene は実装。 |
| Examples | "三人称一元 / 過去形 / 温度 cold / 短文ベース / ハイブロウ命題禁止" |
| Lives in | `bible/style-voice.md` |
| Cousins | Rules, Sample Scene, Voice Sample, Register |

### Term: Cadence
| field | value |
|---|---|
| Japanese | リズム / 緊張弛緩 |
| Category | **Bible Facet**（設計意図） + **Kernel Attribute**（kernel #9 emotional_arc） |
| Definition | The intended rhythm of tension and release across episodes — how often peaks fall, how long lulls last. |
| Role | reader の没入を持続させる時間設計。Reveal Plan / Emotional Arc とともに動く。 |
| Boundary | **"Rhythm" は別語として使わない**（本書では Cadence で統一）。**Reveal Plan とは別**: Cadence は緊張の波、Reveal Plan は情報の波。 |
| Examples | "tension:release = 6:4"、"3 話に 1 度大波"、"Arc 末尾は静か" |
| Lives in | `bible/cadence-plan.md` |
| Cousins | Emotional Arc, Reveal Plan, Tension Curve |

### Term: World
| field | value |
|---|---|
| Japanese | 世界観 / 舞台 |
| Category | **Bible Facet** |
| Definition | The fictional world's stable givens — geography, society, physics, economics, and locations that exist regardless of plot. |
| Role | Story が起こる前から存在する設定。drafter / reviewer が「世界の中で何ができて何ができないか」を判定する根拠。 |
| Boundary | **System とは別**: World は世界そのもの、System は世界の中の制度・能力体系。**Timeline とは別**: World は空間と性質、Timeline は時間軸。 |
| Examples | "アイエー社会の社会モデル"、"佐山レンジの 6 アーク世界" |
| Lives in | `bible/world/`（過大化したら locations / society / physics 等に分割） |
| Cousins | System, Timeline, Locations, Genre Overlay |

### Term: Character
| field | value |
|---|---|
| Japanese | キャラクター / 人物 |
| Category | **Bible Facet** |
| Definition | A named figure in the work with want, need, wound (or misbelief), voice, and trajectory. |
| Role | drafter が prose を書く根拠の中核。focal character を定める単位。 |
| Boundary | **Transformation Curve とは別**: Character は人、Transformation Curve はその人の変化形。**Relationship Arc とは別**: Relationship は人同士、Character は個。 |
| Examples | 主人公 / 対抗者 / 取り巻き / レギュラー NPC |
| Lives in | `bible/characters/`、個別シートは `bible/characters/{slug}.md` |
| Cousins | Transformation Curve, Relationship Arc, Voice Sample |

### Term: System ★ 新設 facet
| field | value |
|---|---|
| Japanese | 制度 / 能力体系 / 機構 |
| Category | **Bible Facet** |
| Definition | The internal mechanics of the world — institutions, glossary, abilities, economics, magic systems, technology — that govern what can happen and how. |
| Role | World が「世界そのもの」なら System は「世界の中の動作原理」。能力 / 制度 / 経済 / 魔法 / SF 技術が複雑な作品では分離が必須。 |
| Boundary | **World とは別**: World は地理・社会・物理の givens、System はそれらを動かす仕組み。**Rules とは別**: Rules は文体禁則、System は世界内ルール（in-world law）。 |
| Examples | "ia_society の institutions glossary（記録局 / 保全局 / 白紙日 / 真耕特区）"、"佐山レンジの正当化圏仕様"、"佐山レンジの章末資料制度" |
| Lives in | `bible/system/` |
| Cousins | World, Rules, Genre Overlay |

### Term: Timeline ★ 新設 facet（2 階層）
| field | value |
|---|---|
| Japanese | 時系列 / 年表 |
| Category | **Bible Facet** |
| Definition | The canonical temporal axis of the work — pre-history, institutional history, and day-by-day chronology of the manuscript period. |
| Role | 「いつ何が起きたか」の正本。**2 階層**を許容: (1) macro = 制度史 / 前史 / Manuscript 全期、(2) micro = 本編日次 / 時刻単位。 |
| Boundary | **State の timeline-progress とは別**: Bible.Timeline は**設計時に確定する歴史**、State 側は draft によって追加される実装履歴。**Plot とは別**: Plot は因果連鎖、Timeline は時刻軸。 |
| Examples | "ia_society 03_TIMELINE_AND_HISTORY（連結臨界 2045）+ 15_DAY_BY_DAY_CHRONOLOGY（白紙日逆算日次）" |
| Lives in | `bible/timeline/history.md`（macro）、`bible/timeline/day-by-day.md`（micro） |
| Cousins | Plot, World, History, Chronology |

### Term: Sample Scene ★ 新設 facet
| field | value |
|---|---|
| Japanese | 試し場面 / 文体見本 |
| Category | **Bible Facet** |
| Definition | A reference scene written at production-quality length and voice, used as the calibration target for all drafts — explicitly NOT a draft of the manuscript itself. |
| Role | drafter が「目指すべき品質と声の具体例」を持つ見本帳。reviewer が「文体ドリフトしていないか」を判定する根拠。 |
| Boundary | **Prose / Draft とは別**: Sample Scene は本編に載らない試し場面（or 本編の一部を見本として再掲）。**Style Voice とは別**: Style Voice は宣言、Sample Scene は実装例。**論点 2 で確定**: ドラフト本文は Bible に置かない、Sample Scene **だけ**は Bible に置く。 |
| Examples | "ia_society 11_SAMPLE_SCENES の 移送車 / 受け入れ検査 / 生身接触室前室 / 低速聴聞" |
| Lives in | `bible/samples/` |
| Cousins | Prose, Draft, Style Voice, Voice Sample |

### Term: Plot
| field | value |
|---|---|
| Japanese | プロット / 筋 |
| Category | **Bible Facet**（Unit ではない） |
| Definition | The causal chain of events — what happens, in causal order, abstracted from how it is written. |
| Role | 「誰が何をして、何が起きて、結果どうなる」の因果系列。文体・POV・順序操作を含まない、純粋な事象連鎖。 |
| Boundary | **Arc Map とは別**（Arc Map は単位の並べ方の図）。**Episode Plan とは別**（Episode Plan は公開単位の役割割り当て）。**Scene Card とは別**（Scene Card は局所設計）。**Foreshadowing Map とは別**（伏線設計図）。Plot は**事象の因果**だけ。 |
| Examples | "湊が薬を持ち込む → 検査で発覚 → 兄妹が離散 → 主人公が記録を書く側に立つ" |
| Lives in | `bible/plot.md`（デフォルト 1 ファイル、肥大時 `bible/plot/` ディレクトリに分割） |
| Cousins | Arc Map, Episode Plan, Foreshadowing Map, Reveal Plan |

### Term: Foreshadowing Map
| field | value |
|---|---|
| Japanese | 伏線配置図 / 伏線設計 |
| Category | **Bible Facet**（設計意図） |
| Definition | The author's design-time plan for clue placement — where each foreshadowing seed is sown, watered, and harvested across episodes. |
| Role | 伏線の置き場所と回収位置の正本。drafter は書くとき参照、reviewer は回収検証で参照。 |
| Boundary | **State.foreshadowing-implementation とは別**: Foreshadowing Map は**設計意図**（Bible）、State 側は**実装状況**。**Reveal Plan とは別**: Reveal Plan は読者への開示順、Foreshadowing Map は伏線の配置。 |
| Examples | "湊の中間 ID は ep02 で植え、ep08 で補強、ep18 で回収" |
| Lives in | `bible/foreshadowing-map.md` |
| Cousins | Reveal Plan, State.foreshadowing-implementation, Clue, Payoff |

### Term: Reveal Plan
| field | value |
|---|---|
| Japanese | 開示計画 |
| Category | **Bible Facet**（設計意図） |
| Definition | The author's design-time plan for what information is disclosed to the reader at which Episode / Packet / Arc. |
| Role | 「いつ何を読者に渡すか」の正本。Information Design.intended_unknowns の運用版。 |
| Boundary | **Foreshadowing Map とは別**: Foreshadowing Map は伏線の**置き場所**、Reveal Plan は読者への**開示順**。**Cadence とは別**: Cadence は緊張波、Reveal Plan は情報波。**State.reveal-implementation とは別**: 二層ファイル運用が Reveal Budget Sheet。 |
| Examples | "湊の中間 ID は ep08 で読者に開示"、"白紙日制度の真意は ep17 で開示" |
| Lives in | `bible/reveal-plan.md` または `bible/reveal-budget.md`（二層ファイル形式） |
| Cousins | Foreshadowing Map, Cadence, Information Design, Withhold Policy |

### Term: Motif
| field | value |
|---|---|
| Japanese | モチーフ / 反復像 |
| Category | **Bible Facet** |
| Definition | A recurring concrete image, object, gesture, or phrase that carries thematic weight and accumulates meaning through repetition and variation. |
| Role | テーマを抽象命題で説かず、具体物で読者に伝える装置。**初出 → 変奏 → 回収** の三段階運用（Motif Ladder）。 |
| Boundary | **Theme とは別**: Theme は問い、Motif は問いを運ぶ具体物。**Foreshadowing とは別**: Foreshadowing は情報の伏線、Motif は意味の反復。**Symbol とは別**: Symbol は固定意味、Motif は反復で変奏される。 |
| Examples | "ia_society の 土 / 種 / マッチ / 4-2 の空欄"、"佐山レンジの章末資料" |
| Lives in | `bible/motif-ladder.md`（設計）+ `state/motif-status.yaml`（実装履歴）／二層ファイルも可 |
| Cousins | Theme, Symbol, Foreshadowing Map, Object Ladder |

### Term: Genre Overlay
| field | value |
|---|---|
| Japanese | ジャンル制約 |
| Category | **Bible Facet**（外部由来の制約） |
| Definition | The set of conventions, tropes, and reader expectations imposed by the chosen genre — what the genre demands and forbids. |
| Role | ジャンル選択 = 読者期待 = 守るべき制約。違反すると読者が離脱する。 |
| Boundary | **Promise とは別**: Promise は本作品固有約束、Genre Overlay はジャンル一般約束。**Project Override とは別**: Project Override は genre を破る例外宣言。 |
| Examples | "異世界転生: チート要素 / 序盤転生必須"、"ダークファンタジー: 救いの欠如許容" |
| Lives in | `bible/genre-overlay.md`（必要時） |
| Cousins | Project Override, Promise, Reader Expectation |

### Term: Project Override
| field | value |
|---|---|
| Japanese | 作品例外 / 美学 |
| Category | **Bible Facet**（最強拘束） |
| Definition | A work-specific exception that overrides default conventions, including Genre Overlay or general craft rules — the author's binding aesthetic choice for this work. |
| Role | 「このジャンルでは普通だが、本作品では禁じる」「このジャンルでは禁じられているが、本作品では採用する」の宣言。**最強の拘束力**。 |
| Boundary | **Promise とは別**: Promise は読者向け約束（外向き）、Project Override は内部例外規定（内向き）。**Rules とは別**: Rules は文体禁則、Project Override は構造・テーマ・展開レベルの例外。 |
| Examples | "本作: 異世界転生だがチート無双禁止"、"本作: ダークファンタジーだが暴力グロテスク禁止"、"本作: 主人公を反省させない" |
| Lives in | `bible/project-override.md`（必要時） |
| Cousins | Genre Overlay, Promise, Rules, Theme |

---

## Section 5. Design Artifact

### Term: Open Question
| field | value |
|---|---|
| Japanese | 未決論点 |
| Category | **Design Artifact** |
| Definition | A design decision that author judgment has been deferred on, blocking forward progress until resolved. |
| Role | bible に流す前の「保留中」を可視化。同じ論点を何度も再発見しないための台帳。 |
| Boundary | **Design Debt とは別**: Open Question は答えで閉じる、Design Debt は構造的で答えだけでは閉じない。**Decision Log とは別**: Open Question は未決（Design）、Decision Log は確定済み履歴（State）。 |
| Examples | "白紙日制度は通年か月次か未決" |
| Lives in | `design/open-questions.md` |
| Cousins | Design Debt, Decision Log, Canon Patch Proposal |

### Term: Design Debt
| field | value |
|---|---|
| Japanese | 設計負債 |
| Category | **Design Artifact** |
| Definition | A long-lived structural concern that does not have a single resolution — the design itself has known weakness or fragility that must be tracked. |
| Role | 「未来の自分が忘れて踏み抜く」リスクを台帳化。書き進めるごとに参照される警告文。 |
| Boundary | **Open Question とは別**: Open Question は答えで閉じる、Design Debt は構造的。**Contradiction Log とは別**: Design Debt は事前警告（Design）、Contradiction Log は事後発見（State）。 |
| Examples | "三層対応は scene 単位で書く必要があるが現状 packet 単位でしか管理していない" |
| Lives in | `design/design-debt.yaml` |
| Cousins | Open Question, Contradiction Log, Patch |

### Term: Canon Patch Proposal
| field | value |
|---|---|
| Japanese | canon 改訂提案 |
| Category | **Design Artifact**（Patch lifecycle の第 1 段階） |
| Definition | A formal proposal to amend Bible content, describing the current canon state, the proposed change, justification, and impact — pending author approval. |
| Role | Bible を直接書き換えず Patch 経由で改訂する手続きの **proposal stage**。承認されると State の Canon Patch Log に entry が追加され、Bible が改訂される。 |
| Boundary | **Patch（プロセス全体）とは別**: Canon Patch Proposal はその第 1 段階のみ。**State.canon-patch-log とは別**: Proposal は未承認（Design）、Log は承認済み履歴（State）。 |
| Examples | "Patch #042 提案: 真耕特区の所在を東北から東海に変更" |
| Lives in | `design/canon-patch-proposals/{patch_id}.md` |
| Cousins | Patch, Canon, Bible, Decision Log |

### Term: Rejected Idea
| field | value |
|---|---|
| Japanese | 没案 |
| Category | **Design Artifact**（negative knowledge） |
| Definition | An idea, beat, character, or design choice that was considered and explicitly rejected, preserved with rationale to prevent rediscovery. |
| Role | 「同じアイデアを何度も提案して何度も却下する」を防ぐ。reject 理由とともに append。 |
| Boundary | **Open Question とは別**: Rejected Idea は閉じている、Open Question は未決。**Backlog とは別**: Backlog は採用候補の保留、Rejected Idea は不採用確定。**所属**: 採否判断は揺れる可能性があるので Design 側に置く（**論点 4 関連で確定**）。 |
| Examples | "ep05 で湊が反乱する展開は不採用（理由: Promise の '主人公は反省しない' と整合しない）" |
| Lives in | `design/rejected-ideas.md` |
| Cousins | Open Question, Backlog, Decision Log |

---

## Section 6. State Artifact

### Term: Decision Log
| field | value |
|---|---|
| Japanese | 判断履歴 / 決定ログ |
| Category | **State Artifact**（Ledger pattern） |
| Definition | An append-only journal of significant author decisions taken during production — what was decided, when, and why. |
| Role | 「いつ何を決めたか」を遡る正本。 |
| Boundary | **Open Question とは別**: Open Question は未決（Design）、Decision Log は確定履歴（State）。**Canon Patch Log とは別**: Canon Patch Log は Bible 改訂に限定、Decision Log は author 判断全般。 |
| Examples | "2026-04-30: ep05 ラストの時刻を 18:30 に確定" |
| Lives in | `state/decision-log.yaml` |
| Cousins | Open Question, Canon Patch Log, Patch |

### Term: Contradiction Log
| field | value |
|---|---|
| Japanese | 矛盾履歴 |
| Category | **State Artifact**（Ledger pattern） |
| Definition | An append-only journal of detected contradictions between Bible / State / drafts — what was found, when, severity, and resolution status. |
| Role | Continuity Review で発見した矛盾を起票・追跡する正本。解消済みも append で残す（削除しない）。 |
| Boundary | **Continuity（観点）とは別**: Continuity は性質、Contradiction Log は実装。**Design Debt とは別**: Design Debt は事前警告、Contradiction Log は事後発見。 |
| Examples | "X-001: ep03 で湊の身長 170cm、ep08 で 175cm（解消: 170cm に統一）" |
| Lives in | `state/contradiction-log.yaml` |
| Cousins | Continuity, Design Debt, Decision Log |

### Term: Timeline State
| field | value |
|---|---|
| Japanese | 時系列実装状況 |
| Category | **State Artifact** |
| Definition | Runtime tracking of which Bible.Timeline events have been written into prose, including per-episode date stamps and any drift from canonical timeline. |
| Role | Bible.Timeline（設計時の正史）に対して、prose で**いつ何が書かれたか**を記録する。 |
| Boundary | **Bible.Timeline とは別**: Bible 側は設計、State 側は実装履歴。 |
| Examples | "ep01 で言及された日付: 3/14"、"ep05 で実装された白紙日カウントダウン: T-71:42" |
| Lives in | `state/timeline-state.yaml` |
| Cousins | Bible.Timeline, Continuity, Decision Log |

### Term: Character State
| field | value |
|---|---|
| Japanese | キャラクター実装状況 |
| Category | **State Artifact** |
| Definition | Runtime snapshot of each character's known facts, relationships, knowledge state, and emotional temperature as implemented in prose. |
| Role | drafter が「現在このキャラは何を知っているか / どう感じているか」を確認する正本。Continuity Review の主要参照。drafter-preflight の知識状態台帳が直接参照する。 |
| Boundary | **Bible.Characters とは別**: Bible 側は設計（want/need/wound）、State 側は実装の現在値。 |
| Examples | "史弥（ep08 終了時）: 知っている = 湊の中間 ID / 知らない = 兄の死亡 / 関係温度 vs 乃々 = 警戒" |
| Lives in | `state/character-states.yaml` |
| Cousins | Bible.Characters, Relationship Arc, Continuity |

### Term: Implementation Ledger（パターン card）
| field | value |
|---|---|
| Japanese | 実装台帳 |
| Category | **State Artifact**（Ledger pattern, generic） |
| Definition | An append-only journal that pairs with a Bible Facet's design intent, recording what has actually been implemented in prose for that facet — applies to Foreshadowing, Reveal, Motif, and similar. |
| Role | 「設計したけど実装したか？」を機械的に検証する。Bible facet と State Implementation Ledger の **二層構造運用**の根本パターン。 |
| Boundary | **Bible.{facet}** が**設計意図**、**Implementation Ledger** が**実装状況**。両者をペアで参照する。**論点 3 で確定**: 二層ファイル形式は論理的にこの 2 つを物理的に同居させたもの。 |
| Examples | "FS-007 湊の中間 ID: 植 ep02 ✓ / 補強 ep08 ✓ / 回収 ep18 未"、"RV-003 白紙日真意: 予定 ep17 / 実装 ep17 ✓"、"MT-土と種: 起点 ep01 ✓ / 変奏 1 ep05 ✓ / 回収 ep20 未" |
| Lives in | `state/foreshadowing-implementation.yaml`、`state/reveal-implementation.yaml`、`state/motif-status.yaml` |
| Cousins | Foreshadowing Map, Reveal Plan, Motif, Bible Facet |

### Term: Backlog
| field | value |
|---|---|
| Japanese | バックログ |
| Category | **Process Artifact**（制作過程のタスクキュー） |
| Definition | A flat queue of pending production tasks — including writing, design, review, release tasks, and external actions on platforms or community — without lifecycle subfolders or packet hierarchy. |
| Role | 「やるべきだが今やっていない」を一元管理。task の種別・優先度・状態を持つが、過剰な lifecycle / packet 化はしない。フラット構造を維持。 |
| Boundary | **旧用法 NG**: 旧 v1 / v2 系で `backlog/` を**物語の入口**（idea inbox）として使っていた経緯あり、本書ではそれを禁止し、物語入口は `story/seeds/` に統一済み。Backlog は**作業台帳としてのみ**使う。**Pitch とは別**: Pitch は採用前提案、Backlog は採用後の積み残し。**Open Question とは別**: Open Question は判断が必要、Backlog は実行が必要。 |
| Examples | "ep10 の draft を書く" / "foreshadowing-map を ep05 まで更新" / "kakuyomu like 実行" / "reader-personas review 実施" |
| Lives in | `backlog/`（フラット）。各 task は `backlog/{slug}.md` または `.yaml`。既存 `actions/` は `backlog/` にリネーム |
| Cousins | Pitch, Open Question, Episode Status, Release |

---

## Section 7. Intake Pipeline

### Term: Seed
| field | value |
|---|---|
| Japanese | 種 / シード |
| Category | **Process Artifact**（intake-stage） |
| Definition | A reusable creative kernel extracted from raw planning input or approved pitches — a self-contained idea ready to be promoted into Bible / Design content. |
| Role | raw → digest を経て切り出された **再利用可能な核**。Pitch が承認されると Seed として保存。 |
| Boundary | **Pitch とは別**: Pitch は人へのプレゼン、Seed は再利用可能な核。**Raw とは別**: Raw は原文ママ、Seed は抽出された圧縮形。 |
| Examples | "種: 主人公が 147 という数字に身体的反応を示す癖（再利用可能な motif 候補）" |
| Lives in | `story/seeds/{date}_{slug}.md` |
| Cousins | Pitch, Raw, Digest, Idea |

### Term: Digest
| field | value |
|---|---|
| Japanese | ダイジェスト / 圧縮要約 |
| Category | **Process Artifact**（intake-stage） |
| Definition | A structured summary of one batch of raw planning input — chat logs, design documents, fragmentary notes — distilled into categorized items (confirmed / tentative / open / contradiction / needs_author_decision / deferred / hidden / rejected). |
| Role | Intake Adapter の出力 #1。raw を直接 bible に流さないための**中間層**。 |
| Boundary | **Raw とは別**: Raw は原文、Digest は構造化要約。**Update Proposal とは別**: Digest は読み物、Update Proposal は反映指示書。 |
| Examples | "Digest 2026-04-30: ChatGPT との企画 chat 50 件を C-XXX / T-XXX / Q-XXX / X-XXX で項目化" |
| Lives in | `synthesis/session_digests/{date}_{slug}.md` |
| Cousins | Raw, Update Proposal, Seed, Intake Adapter |

### Term: Update Proposal
| field | value |
|---|---|
| Japanese | 更新提案 |
| Category | **Process Artifact**（intake-stage、bible 反映直前） |
| Definition | A formal change proposal targeting specific Bible / Design / State files, including the diff content, source trace, status assignment, and contradiction flags — pending human approval before being applied. |
| Role | Intake Adapter の出力 #2。author / reviewer が「これを反映するか」を判断する**意思決定 packet**。 |
| Boundary | **Digest とは別**: Digest は読み物、Update Proposal は反映指示書。**Canon Patch Proposal とは別**: Canon Patch Proposal は **既存 Bible の改訂**に限定、Update Proposal は **新規追加 + 既存改訂を含む全 intake 反映**を扱う上位概念。 |
| Examples | "Update Proposal 2026-04-30: bible/world/locations.md に '真耕特区' 追加（出典: digest 2026-04-30 #C-007）" |
| Lives in | `synthesis/update_proposals/{date}_{target}_proposal.md` |
| Cousins | Digest, Canon Patch Proposal, Patch, Approval |

### Term: Intake Adapter
| field | value |
|---|---|
| Japanese | インテイク Adapter |
| Category | **Adapter**（Layer 1.5、変換層） |
| Definition | A prompt-driven processor that consumes raw planning input (chat / fragment / external bible package) and produces a Digest plus one or more Update Proposals — without writing directly to Bible / Design / State. |
| Role | raw → bible/design/state の **安全な搬送装置**。raw を直接 bible に流さないことを保証する gatekeeper。**human approval 必須**。 |
| Boundary | **Writing Adapter とは別**: Intake Adapter は**書く前の取り込み**、Writing Adapter は**書く前の圧縮**。 |
| Examples | "ia_society の bible/ia_story_bible_v2/ 50 ファイルを Intake Adapter にかけて bible/design/state に分割" |
| Lives in | prompt の正本: `StoryTemplateEvolution/current/adapter/intake_adapter_prompt.md`、各 work の利用設定: `<work>/adapter/`（leading dot なし） |
| Cousins | Writing Adapter, Digest, Update Proposal, Layer 1.5 |

---

## Section 8. Writing Pipeline

### Term: Writing Adapter
| field | value |
|---|---|
| Japanese | ライティング Adapter |
| Category | **Adapter**（Layer 1.5） |
| Definition | A prompt-driven processor that consumes Bible / Design / State and produces a Writing Pack tailored for one Episode — compressing only the parts the drafter needs for that unit. |
| Role | **bible 全体を drafter に渡さない**ための圧縮器。1 episode 単位で Writing Pack を生成する。 |
| Boundary | **Intake Adapter とは別**: Intake は搬送、Writing は圧縮。 |
| Examples | "ep08 の Writing Adapter 実行 → episode_brief / scene_card / context_pack / acceptance_checklist 生成" |
| Lives in | prompt の正本: `adapter/writing_adapter_prompt.md` |
| Cousins | Intake Adapter, Writing Pack, Drafter, Layer 1.5 |

### Term: Writing Pack
| field | value |
|---|---|
| Japanese | ライティング Pack |
| Category | **Adapter Output**（drafter input） |
| Definition | A compressed, episode-scoped bundle of drafter inputs — typically four files: episode_brief, scene_card, context_pack, acceptance_checklist. |
| Role | drafter が prose を書くための **入力一式**。 |
| Boundary | **Bible とは別**: Bible は正本、Writing Pack は episode 単位の抜粋。 |
| Examples | "writing/episode_packs/ep001/ 配下: episode_brief.md / scene_card.md / context_pack.md / acceptance_checklist.md" |
| Lives in | `writing/episode_packs/{ep_id}/` |
| Cousins | Writing Adapter, Scene Card, Acceptance Contract, Drafter |

### Term: Scene Card
| field | value |
|---|---|
| Japanese | シーンカード |
| Category | **Adapter Output / Design Artifact** |
| Definition | A design document for one Episode's prose — declaring focal character, scene goal, conflict, turn, reveal, end state, and beat sequence — used as the drafter's primary blueprint. |
| Role | Writing Pack の中核。drafter が beat 順に prose を組み立てる根拠。 |
| Boundary | **Scene（story unit）とは別**: Scene は story unit、Scene Card は episode-scope の設計成果物。**Acceptance Contract とは別**: Scene Card は drafter 用、Acceptance Contract は judge 用。両者は**ペアで生成**される。 |
| Examples | "scene-ep08-receipt-room.md: focal=史弥 / goal=書類受領 / conflict=湊との沈黙 / turn=湊が筆を止める / end_state=史弥が左手を確認" |
| Lives in | `scenes/slotted/{ep_id}-{slug}.md` |
| Cousins | Scene（unit、同名警告）, Acceptance Contract, Writing Pack, Beat |

### Term: Acceptance Contract
| field | value |
|---|---|
| Japanese | 受け入れ契約 |
| Category | **Adapter Output / Review Artifact** |
| Definition | A judge-side companion to Scene Card — the formal acceptance criteria for one Episode's draft, including must_satisfy, must_not_violate, and quality_bar. |
| Role | Scene Card と**ペアで生成**され、draft 完成時に judge / reviewer が機械的に「合格 / 修正 / 再生成」を判定する根拠。 |
| Boundary | **Scene Card とは別**: Scene Card は drafter 用、Acceptance Contract は judge 用。**Rubric とは別**: Rubric は全話共通評価軸、Acceptance Contract はこの ep 固有の合格基準。 |
| Examples | "ep08 acceptance: must_satisfy=[湊が筆を止める描写, 左手の癖再現] / must_not_violate=[Promise#3 の伏線抜け] / quality_bar=rubric≥60" |
| Lives in | `reviews/contracts/{ep_id}.contract.yaml` |
| Cousins | Scene Card, Rubric, Judge, Writing Pack |

---

## Section 9. Documentation

### Term: Walkthrough
| field | value |
|---|---|
| Japanese | ウォークスルー / 案内 |
| Category | **Documentation Artifact** |
| Definition | A step-by-step explanatory document that guides readers through a complex artifact — a reading order, a character introduction tour, a world overview tour — to lower onboarding cost. |
| Role | Bible / 設計資料の入口。新規セッション・新規コラボレーターが迷わずに作品の骨格を把握できるようにする。 |
| Boundary | **README とは別**: README は索引、Walkthrough は順序付きの読み方。**Sample Scene とは別**: Sample Scene は文体見本、Walkthrough は理解の手引き。 |
| Examples | "ia_society の `bible/ia_story_bible_v2/00_README.md` の 25 段階読み順は事実上の Walkthrough" |
| Lives in | `bible/walkthroughs/`（必要時） |
| Cousins | README, Sample Scene, Onboarding Guide |

### Term: README
| field | value |
|---|---|
| Japanese | リードミー / 索引 |
| Category | **Documentation Artifact** |
| Definition | A directory's index file — naming what's inside, what depends on what, and what to read first. Not ordered as a tour; ordered as a lookup. |
| Role | ディレクトリの入口。配下のファイル一覧 + 1 行説明 + 関連リンク。 |
| Boundary | **Walkthrough とは別**: Walkthrough は順序付き案内、README は索引。 |
| Examples | "bible/README.md（facet 索引・分割ルール・読み順導線）"、"design/README.md"、"state/README.md" |
| Lives in | 各ディレクトリのトップ |
| Cousins | Walkthrough, Index |

---

## Section 10. Review

### Term: Review（メタ・単独使用禁止）
| field | value |
|---|---|
| Japanese | レビュー |
| Category | **Meta-Process** |
| Definition | A formal evaluation pass against an artifact — always classified by review type. |
| Role | 品質ゲート全般を指す上位概念。 |
| Boundary | **"Review" 単独でファイル名・ディレクトリ名・タスクラベルにしない**。必ず種別を付ける。 |
| Examples | "ep08 review" は曖昧 → "ep08 typed review" "ep08 continuity review" に種別付与 |
| Lives in | （概念のみ） |
| Cousins | Typed / Bridge / Continuity / Persona / Approval / Packet Freeze / Design Audit Review |

### Term: Typed Review
| field | value |
|---|---|
| Japanese | タイプドレビュー / 総合レビュー |
| Category | **Review**（full coverage） |
| Definition | A comprehensive review against the work's full Rubric (9 to 25 axes) — applied at episode or packet scope. |
| Role | 「全体的にどうか」を網羅的に判定。最下位スコアを特定し reverse flow 先を必ず明示する。 |
| Boundary | **Bridge Review とは別**: Typed は単一 unit、Bridge は unit 間。 |
| Examples | "ep08 typed review: 9 軸スコア + 最下位 = '感情的インパクト' / reverse flow → packets/" |
| Lives in | `reviews/typed-review-{date}-{ep_id}.md` |
| Cousins | Rubric, Bridge Review, Continuity Review |

### Term: Bridge Review
| field | value |
|---|---|
| Japanese | ブリッジレビュー / 継ぎ目レビュー |
| Category | **Review**（transition focus） |
| Definition | A review specifically for the transition between two adjacent units (Packet→Packet, Arc→Arc) — verifying entry/exit state alignment, knowledge state monotonicity, and tonal continuity. |
| Role | unit 切り替えで読者が脱落する箇所を防ぐ。**packet/arc 切り替え時 MUST**。 |
| Boundary | **Continuity Review とは別**: Continuity は全話横断、Bridge は隣接 2 unit 限定。 |
| Examples | "packet-002 → packet-003 bridge: ep10 終了時の知識状態 vs ep11 開始時の単調性" |
| Lives in | `reviews/bridge-review-{packet_a}-{packet_b}-{date}.md` |
| Cousins | Typed Review, Continuity Review, Packet Freeze Review |

### Term: Continuity Review
| field | value |
|---|---|
| Japanese | 連続性レビュー |
| Category | **Review**（continuity focus） |
| Definition | A review focused on knowledge-state monotonicity, timeline coherence, physical fact stability, and character behavior consistency across episodes within scope. |
| Role | Continuity（性質）の実装検査。発見した矛盾は Contradiction Log に起票。 |
| Boundary | **Continuity（観点）とは別**: Continuity は性質、Continuity Review は実装。 |
| Examples | "continuity review ep01-ep08: 史弥の知識状態台帳が単調か、湊の身体描写が一貫しているか" |
| Lives in | `reviews/continuity-review-{scope}-{date}.md` |
| Cousins | Continuity, Contradiction Log, Bridge Review |

### Term: Persona Review
| field | value |
|---|---|
| Japanese | ペルソナレビュー / 読者視点レビュー |
| Category | **Review**（reader-perspective focus） |
| Definition | A review applying multiple distinct reader personas to one draft — typically immersive reader (A) / structural reader (B) / disengaged reader (C) — to detect failure modes invisible to a single perspective. |
| Role | 単一 reviewer 視点では見えない「ある層には刺さるが別の層には刺さらない」をあぶり出す。 |
| Boundary | **Reader Persona（kernel 由来）とは別**: 後者は target reader 像、Persona Review は評価のための仮想 reader 群。 |
| Examples | "ep08 persona review: A 没入 / B 構造 / C 離脱 の 3 視点で同一 draft を評価" |
| Lives in | `reviews/persona-review-{ep_id}-{date}.md` |
| Cousins | Reader Persona, Typed Review, Approval Review |

### Term: Packet Freeze Review
| field | value |
|---|---|
| Japanese | パケット凍結レビュー |
| Category | **Review**（gate at packet freeze） |
| Definition | A review applied when promoting a Packet from `scoped/` to `frozen/` — verifying purpose, episode_roles, end_hooks, disclose, withhold, guardrails, and entry/exit state are all filled and coherent. |
| Role | Packet を frozen にする前の最後の gate。drafter に渡せる状態かの DoR-C 検査。 |
| Boundary | **Typed Review とは別**: Packet Freeze は packet 凍結 gate、Typed は draft 評価。 |
| Examples | "packet-001-first-assignment freeze: 全 episode role 割り当て / disclose-withhold 整合 / guardrails 完全" |
| Lives in | `reviews/packet-freeze-{packet_id}-{date}.md` |
| Cousins | Packet, DoR-C, Typed Review |

### Term: Approval Review
| field | value |
|---|---|
| Japanese | 承認レビュー / 公開前レビュー |
| Category | **Review**（final gate before publish） |
| Definition | A final pre-publication gate review — verifying acceptance contract satisfied, must_not_violate clear, kakuyomu policy compliance (AI tag / posting frequency / forbidden content), and author hard_lock. |
| Role | Episode を `published/` に移す前の最後の gate。DoD-E 検査。 |
| Boundary | **Typed Review とは別**: Approval は公開可否判定、Typed は品質評価。 |
| Examples | "ep08 approval: acceptance ✓ / kakuyomu AI tag ✓ / 投稿頻度 ✓ / hard_lock ✓ → published/" |
| Lives in | `reviews/approval-{ep_id}-{date}.md` |
| Cousins | Acceptance Contract, DoD-E, Kakuyomu Policy |

### Term: Design Audit
| field | value |
|---|---|
| Japanese | 設計監査 |
| Category | **Review**（design integrity focus） |
| Definition | A review applied to Bible / Design artifacts (not drafts) — verifying completeness, internal consistency, and alignment with kernel and promise. |
| Role | 「設計が空疎ではないか」「promise と矛盾していないか」「intentionally_hidden の管理が破綻していないか」を点検。 |
| Boundary | **Typed Review とは別**: Typed は draft 対象、Design Audit は設計対象。 |
| Examples | "ia_society の bible/ia_story_bible_v2/ 50 ファイルを Design Audit にかけて promise との整合確認" |
| Lives in | `reviews/audits/{date}-{scope}-design-audit.md` |
| Cousins | Typed Review, Continuity Review, Bible, Promise |

### Term: Rubric
| field | value |
|---|---|
| Japanese | ルーブリック / 評価軸 |
| Category | **Review Tool** |
| Definition | The canonical set of evaluation dimensions used by Typed Review — typically 9 to 25 named axes with score ranges and weights. |
| Role | Typed Review の根拠。axis 変更は過去 review との比較を壊すので canon patch 相当の手続きを要する。 |
| Boundary | **Acceptance Contract とは別**: Rubric は全話共通、Acceptance Contract は ep 固有。 |
| Examples | "9 軸 rubric: 完成度 / 読者体験 / 独創性 / 整合性 / 感情的インパクト / キャラ強度 / 世界観強度 / 文章技術 / 推敲耐性" |
| Lives in | `craft/rubric.md` |
| Cousins | Typed Review, Acceptance Contract |

---

## Section 11. Craft

### Term: Craft
| field | value |
|---|---|
| Japanese | クラフト / 創作原理 |
| Category | **Knowledge Layer**（Layer 3、作品不問の常設道具箱） |
| Definition | A canonical library of work-agnostic creative principles — POV theory, dialogue craft, scene-sequel structure, foreshadowing technique, voice register theory — assembled from established craft sources. |
| Role | 作品の枠を超えて常に参照される道具箱。新作品でも copy せずリンク参照する。 |
| Boundary | **Bible とは別**: Bible は作品固有、Craft は作品不問。**Framework とは別**: Craft は常設、Framework は一時 lens。 |
| Examples | "Scene-Sequel 構造論"、"視点設計の嘘と省略"、"伏線の三段運用" |
| Lives in | `craft/`（StoryTemplate 共通） |
| Cousins | Framework, Framework Lens, Rubric, Bible |

### Term: Framework
| field | value |
|---|---|
| Japanese | フレームワーク |
| Category | **Knowledge Reference**（外部創作理論） |
| Definition | An established creative framework — Save the Cat, Hero's Journey, Three-Act Structure, Story Genius, etc. — referenced as a citation but not adopted wholesale. |
| Role | 既存理論への索引。「これを全部採用する」ではなく「必要なときに lens として一時的に当てる」。 |
| Boundary | **Craft とは別**: Craft は本書の正本道具箱、Framework は外部参照。**Framework Lens とは別**: Framework は理論、Lens は適用。 |
| Examples | "Save the Cat 15 ビート"、"Hero's Journey 12 段階"、"Egri's Premise Theory" |
| Lives in | `craft/framework-index.md`（索引のみ） |
| Cousins | Framework Lens, Craft, Beat Sheet |

### Term: Framework Lens
| field | value |
|---|---|
| Japanese | フレームワーク・レンズ |
| Category | **Knowledge Application**（一時適用視点） |
| Definition | A temporary application of a Framework as a review or design lens — picking up the framework, looking through it once, and putting it down without integrating it into Bible or Craft. |
| Role | 「Save the Cat lens で見ると ep15 が Midpoint に達していない」のように、必要なときだけ適用。**Bible には積まない**。**最強テンプレ作るな**原則の実装。 |
| Boundary | **Framework とは別**: Framework は索引、Lens は適用。 |
| Examples | "ep15 を Save the Cat の Midpoint lens で評価" |
| Lives in | `craft/lenses/{framework_name}-{date}.md` |
| Cousins | Framework, Craft, Typed Review |

---

## Section 12. Status

### Term: Status
| field | value |
|---|---|
| Japanese | ステータス |
| Category | **Meta-Field** |
| Definition | The classification of how a kernel item, bible facet, design proposal, or state record is currently filled — using one of 11 canonical values that capture both presence and intent. |
| Role | 「埋まっていない」を 1 種類に丸めない。**missing と intentionally_blank と not_applicable** は意味が違うので別管理。 |
| Boundary | **filled だけが OK ではない**。各 status は DoR / DoD 通過可否の判定根拠を持つ。 |
| Examples | （以下の 11 値を参照） |
| Lives in | （概念のみ。各項目の status フィールドに格納） |
| Cousins | DoR, DoD |

### Status の 11 値
| 値 | 意味 | DoR-A 通過 | 例 |
|---|---|---|---|
| `filled` | 確定済み | ✓ | promise.items 全部埋まり |
| `tentative` | 仮置き、要検証 | ✓ (low risk) | "stakes は仮で書いた、ep05 で確認" |
| `deferred` | 後で決める（意図的） | MUST=✗ / SHOULD=✓ | "Part 構造は Arc 完了後に決定" |
| `intentionally_blank` | 意図的に空欄（理由あり） | ✓ | "Genre Overlay 不適用作品なので空" |
| `intentionally_hidden` | 意図的に非開示（裏に値あり） | ✓ | "湊の正体は ep18 で開示、bible 本文に書かない" |
| `not_applicable` | 当該作品に該当なし | ✓ | "短編なので Part 不要" |
| `project_override` | 作品例外として個別判定 | ✓ | "本作はチート無双禁止 = override" |
| `contradiction` | 矛盾あり、要解消 | ✗ | "X-001 として Contradiction Log に起票済" |
| `needs_author_decision` | author 判断必須 | MUST=✗ | "AD-005 として Open Question に起票済" |
| `missing` | 単純欠落 | MUST=✗ | "logline.value が空" |
| `rejected` | 不採用確定 | -（適用外） | "R-007: 主人公反乱 case → reject" |

---

## Section 13. Process / Misc

### Term: Pitch
| field | value |
|---|---|
| Japanese | ピッチ / 提案 |
| Category | **Process** + **Artifact** |
| Definition | A short proposal for what to write next — a seed for an Episode, Packet, or Arc, before formal design begins. |
| Role | Seed を作る入口。`/pitch` skill の出力形式。 |
| Boundary | **Seed とは別**: Pitch は人へのプレゼン、Seed は再利用可能な核。 |
| Examples | "ep10 のピッチ: 主人公が初めて自分の票を投じる場面" |
| Lives in | 承認後は `story/seeds/` |
| Cousins | Seed, Outline, Idea |

### Term: Beat Sheet
| field | value |
|---|---|
| Japanese | ビートシート |
| Category | **Craft Artifact** + **Framework Lens** |
| Definition | A craft-imported structural template that lists expected story moments at fixed positions — typically Save the Cat's 15 beats or similar. |
| Role | story 構造を借りて点検する道具。 |
| Boundary | **Beat（単位）とは別**: Beat Sheet は craft 道具、Beat は最小 story unit。 |
| Examples | "Save the Cat 15 ビート" |
| Lives in | `craft/lenses/{framework_name}.md` |
| Cousins | Beat（単位、同名警告）, Framework, Outline |

### Term: Prose
| field | value |
|---|---|
| Japanese | 散文 / 本文 |
| Category | **Artifact**（最終成果物） |
| Definition | The actual narrative text — sentences, paragraphs, dialogue — as written. |
| Role | drafter の出力。reviewer の評価対象。 |
| Boundary | **Draft（状態名）とは別**: Prose は物、Draft は状態。**Sample Scene とは別**: Sample Scene は文体見本、Prose は本編原稿。 |
| Examples | "ep01 の冒頭 5 段落" |
| Lives in | `drafts/episodes/`、承認後 `approved/`、公開後 `published/` |
| Cousins | Draft（状態）, Sample Scene, Manuscript |

---

## Section 14. Deprecated（廃止語・禁止語）

| 廃止語 / 禁止語 | 理由 | 移行先 |
|---|---|---|
| **Premise**（kernel #1 として） | overloaded（Egri 用法と loose-logline 用法の衝突） | **Logline** にリネーム |
| **Bundle** | 旧 v1 で Packet を指していたが衝突発生 | **Packet** に統一 |
| **Chapter**（内部ファイル名として） | 公開表示の "章" との衝突 | 内部禁止、**Packet / Episode** で記述 |
| **Review**（単独で） | 種別が不明だと運用破綻 | **Typed / Bridge / Continuity / Persona / Approval / Packet Freeze / Design Audit Review** のいずれか必須 |
| **Backlog**（旧 v1 用法 = 物語の入口） | seeds/inbox との衝突 | **本書 Backlog は作業台帳のみ**、物語入口は `story/seeds/` |
| **Action Packet**（独立概念として） | 過剰設計 | **Backlog** に統合（フラット） |
| **「最強テンプレ」を目指す** | 新作品で必ず破綻 | **Pull 型 / Retro 駆動** |
| **作品固有 facet を generic 雛形に積む** | 別作品で不要負債になる | **各 work の bible に追加自由、template には積まない** |

---

## まとめ

本書 v4 は **56 語の Card** で StoryTemplate のドメインを zero-base に再定義した。

- 単位軸 8 語 + メタ 2 語
- 格納域 4 語 + 形式 1 語 + プロセス 2 語
- Bible Facet 17 語（うち 3 語が新設: System / Timeline / Sample Scene）
- Design Artifact 4 語
- State Artifact 6 語（うち Backlog は再定義）
- Intake Pipeline 4 語
- Writing Pipeline 4 語
- Documentation 2 語
- Review 8 語 + Rubric 1 語
- Craft 3 語
- Status 1 語 + 11 値
- Process / Misc 3 語
- Deprecated 8 件

これら 56 語は、後続文書（03 / 04 / 05 / 06 / 07 / 08）の参照元となる。
