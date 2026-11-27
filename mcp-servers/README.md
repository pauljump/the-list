# MCP servers

62,022 MCP servers: 57,762 that people wire into Claude Code, read from 99,095 `.mcp.json` files, and 4,260 server repos from the claudemarketplaces.com MCP directory.

## Get it

- [`mcp-servers.csv`](mcp-servers.csv) (9 MB)

Columns: `name`, `description`, `source`, `type`, `command`, `package`, `host`, `copies`, `repo`, `url`, `stars`.

## Notes

- `source` is `config` for a server found in someone's `.mcp.json`, and `directory` for a server repo listed in the claudemarketplaces.com MCP directory.
- Config entries: one per server name and target (package or host). `copies` is how many configs use it, the closest thing here to a popularity count. Only the launcher, the package name and the host are kept; arguments, environment variables, headers and URL paths are dropped because configs often carry keys. Config files have no description field, so those entries have none.
- Directory entries: the description is the repo's own. The same server can appear under both sources.

## Browse

- [0-9-001](0-9-001.md): 244 entries, $disabled_github to 나이스출결
- [a-001](a-001.md): 2,494 entries, a to alibabacloud-core
- [a-002](a-002.md): 2,569 entries, alibabacloud-devops-mcp-server to aws-docs
- [a-003](a-003.md): 427 entries, aws-docs to azurewiki
- [b-001](b-001.md): 2,229 entries, b to bzzoiro-tennis
- [c-001](c-001.md): 2,576 entries, c to close
- [c-002](c-002.md): 2,525 entries, close to countrix-docker
- [c-003](c-003.md): 790 entries, countrystats to Czy Na Czas
- [d-001](d-001.md): 2,518 entries, d to downdetector-mcp
- [d-002](d-002.md): 417 entries, downloaded-tool to dzienniczek
- [e-001](e-001.md): 1,701 entries, e to e签宝
- [f-001](f-001.md): 2,287 entries, F# to folio
- [f-002](f-002.md): 830 entries, folio to fzgx
- [g-001](g-001.md): 2,555 entries, g to grey
- [g-002](g-002.md): 363 entries, greybeard-memory to gyst
- [h-001](h-001.md): 1,587 entries, h1 to hzzs
- [i-001](i-001.md): 1,296 entries, i-ching to izzyblazor
- [j-001](j-001.md): 887 entries, j-quants-doc-mcp to jxscout
- [k-001](k-001.md): 1,218 entries, k-deal-skill to kyvos-mcp
- [l-001](l-001.md): 2,164 entries, l0s to lz-virtual-mail
- [m-001](m-001.md): 2,322 entries, m to melaya
- [m-002](m-002.md): 2,547 entries, melchizedek to mz800emu
- [n-001](n-001.md): 1,689 entries, n2adr to nzc
- [o-001](o-001.md): 2,061 entries, o-matic-elementor-connector to ozpb
- [p-001](p-001.md): 2,583 entries, p-note to portfolio
- [p-002](p-002.md): 1,675 entries, portfolio to pz
- [q-001](q-001.md): 470 entries, q to qyrus
- [r-001](r-001.md): 2,601 entries, r-btw to rungs
- [r-002](r-002.md): 156 entries, runheed to rzilla
- [s-001](s-001.md): 2,554 entries, s to siftree
- [s-002](s-002.md): 2,573 entries, sig-net to str
- [s-003](s-003.md): 1,232 entries, strada to szukaj
- [t-001](t-001.md): 2,611 entries, t to trent-eu
- [t-002](t-002.md): 499 entries, trent-us to tze-hud
- [u-001](u-001.md): 876 entries, u-blox-docs to uzura
- [v-001](v-001.md): 1,258 entries, v-marketing-kit to vzkn
- [w-001](w-001.md): 1,507 entries, w2l to wzrd
- [x-001](x-001.md): 319 entries, x to xyne-claw
- [y-001](y-001.md): 320 entries, y to yzel-wildberries
- [z-001](z-001.md): 492 entries, z-image-mcp to zzzmemo
