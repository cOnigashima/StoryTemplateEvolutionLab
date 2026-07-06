# facets — プロンプト部品（Faceted Prompting）

一枚岩のプロンプトを関心事で分解し、各stepに必要な分だけ渡す。context肥大を防ぎ、再利用する。

- `personas/` … 誰として振る舞うか（drafter / critic / editor / reader_* / supervisor …）
- `policies/` … 何を守るか（style_voice / review_gate / drafter_preflight …）
- `instructions/` … そのstepの手順（多くは workflow 内に直書きでよい）
- `knowledge/` … 何を参照するか（writing_pack / ontology_slice / bible …）
- `output_contracts/` … どう出力するか（draft_format / review_ticket …）

workflow の step は `persona:` `policy:` `knowledge:` `output_contract:` でこれらを名前参照する。
各カテゴリに雛形を1つずつ置いた。作品固有の facet は works/{slug}/ 側に置いて上書きする。
