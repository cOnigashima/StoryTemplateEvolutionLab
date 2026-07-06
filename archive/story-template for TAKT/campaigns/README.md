# campaigns/

Campaign Packet の生成先ディレクトリ。
テンプレートに空ディレクトリがあってもよいが、現行実装では生成時に遅延作成される。

構造:

  campaigns/{episodeId}/v{version}/
    title_variants.md
    catchcopy_variants.md
    intro_variants.md
    policy_check.json
    (Phase 2+: kakuyomu_note.md, x_launch_posts.md, ...)
