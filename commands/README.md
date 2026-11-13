# Commands

31,026 slash commands: every distinct `commands/*.md` the crawl could read.

## Get it

- [`commands.csv`](commands.csv) (9 MB)

Columns: `name`, `description`, `repo`, `url`, `stars`, `license`, `last_pushed`, `copies`, `argument_hint`, `allowed_tools`, `model`.

## Notes

- The crawl found 193,042 of these files across all repos; 136,636 are distinct. The text of 33,488 was read; 103,148 could not be (too large, binary, or gone from GitHub).
- Entries with the same name and description are one entry, shown at the most-starred repo that is not a fork. `copies` is how many copies of the file the crawl found across GitHub.
- 30,942 have a description: the file's own `description`, or its first paragraph when it has none. Cut at 600 characters.
- `stars`, `license` and `last_pushed` belong to the repo.
- `name` is the file name, which is what you type after the slash.

## Browse

- [0-9-001](0-9-001.md): 113 entries, .command-template to 生成 README
- [a-001](a-001.md): 1,406 entries, a to arch
- [a-002](a-002.md): 1,155 entries, arch to azure-tenant-setup
- [b-001](b-001.md): 1,002 entries, b to bzpopmin
- [c-001](c-001.md): 1,666 entries, c to CLAUDE
- [c-002](c-002.md): 1,477 entries, CLAUDE to coograph-review
- [c-003](c-003.md): 1,244 entries, coograph-search to cypher
- [d-001](d-001.md): 1,440 entries, d to do-teams
- [d-002](d-002.md): 453 entries, doc to dynatrace
- [e-001](e-001.md): 910 entries, e to extras
- [f-001](f-001.md): 1,109 entries, f5-agent to fuzz-fix
- [g-001](g-001.md): 1,042 entries, g to gyoshu-auto
- [h-001](h-001.md): 655 entries, ha-automation-lint to hypothesize
- [i-001](i-001.md): 1,115 entries, i18n-audit to itinerary
- [j-001](j-001.md): 213 entries, james to jwt-scan
- [k-001](k-001.md): 255 entries, k-teacher to kztek-brand-info
- [l-001](l-001.md): 801 entries, la-connector-config to lyra
- [m-001](m-001.md): 1,294 entries, m to mythril
- [n-001](n-001.md): 440 entries, n8n-builder to nz-business-english
- [o-001](o-001.md): 751 entries, oaa-adm-lite to ox-status
- [p-001](p-001.md): 1,463 entries, p to prepare-commit
- [p-002](p-002.md): 715 entries, prepare-mr to pytorch-lightning
- [q-001](q-001.md): 249 entries, q-analyze to qwik-expert
- [r-001](r-001.md): 1,454 entries, r-audit to resources
- [r-002](r-002.md): 1,212 entries, resources to rvf
- [s-001](s-001.md): 1,468 entries, saas to setup-github-actions
- [s-002](s-002.md): 1,432 entries, setup-global to status
- [s-003](s-003.md): 775 entries, status to szechuan-sauce
- [t-001](t-001.md): 1,445 entries, t_metaprompt_workflow to typeset
- [u-001](u-001.md): 705 entries, UA Analyze to ux_design
- [v-001](v-001.md): 617 entries, v to vvm-run-inspect
- [w-001](w-001.md): 812 entries, wa-pipeline to wts
- [x-001](x-001.md): 51 entries, x to xtrim
- [y-001](y-001.md): 38 entries, yara-authoring to ytt
- [z-001](z-001.md): 49 entries, zadd to zzzprobe
