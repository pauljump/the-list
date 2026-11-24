# MCP servers

38,767 MCP servers: 34,507 that people wire into Claude Code, read from 54,605 `.mcp.json` files, and 4,260 server repos from the claudemarketplaces.com MCP directory.

## Get it

- [`mcp-servers.csv`](mcp-servers.csv) (6 MB)

Columns: `name`, `description`, `source`, `type`, `command`, `package`, `host`, `copies`, `repo`, `url`, `stars`.

## Notes

- `source` is `config` for a server found in someone's `.mcp.json`, and `directory` for a server repo listed in the claudemarketplaces.com MCP directory.
- Config entries: one per server name and target (package or host). `copies` is how many configs use it, the closest thing here to a popularity count. Only the launcher, the package name and the host are kept; arguments, environment variables, headers and URL paths are dropped because configs often carry keys. Config files have no description field, so those entries have none.
- Directory entries: the description is the repo's own. The same server can appear under both sources.

## Browse

- [0-9-001](0-9-001.md): 149 entries, 0bull to 飞书
- [a-001](a-001.md): 2,454 entries, a to archplan
- [a-002](a-002.md): 1,096 entries, archrivet to azurewiki
- [b-001](b-001.md): 1,336 entries, b to bzzoiro-tennis
- [c-001](c-001.md): 2,491 entries, c to commerce_audit
- [c-002](c-002.md): 1,243 entries, commercengine-docs to cyrus
- [d-001](d-001.md): 1,792 entries, d to dynatrace-mcp-server
- [e-001](e-001.md): 1,008 entries, e to e签宝
- [f-001](f-001.md): 1,787 entries, f1 to fyreflock
- [g-001](g-001.md): 1,889 entries, g to gyst
- [h-001](h-001.md): 993 entries, h1 to hzdb
- [i-001](i-001.md): 830 entries, i-ching to izTolkMcp
- [j-001](j-001.md): 569 entries, j-quants-doc-mcp to jxscout
- [k-001](k-001.md): 806 entries, k-deal-skill to kyvos-mcp
- [l-001](l-001.md): 1,346 entries, l0s to LystBot
- [m-001](m-001.md): 2,258 entries, m to mind-palace
- [m-002](m-002.md): 918 entries, mind_your_tone to mz-relay
- [n-001](n-001.md): 1,040 entries, N8N to nzc
- [o-001](o-001.md): 1,338 entries, o-matic-elementor-connector to ozpb
- [p-001](p-001.md): 2,485 entries, p-note to pumperly-mcp
- [p-002](p-002.md): 155 entries, pumpfun to pyxel-mcp
- [q-001](q-001.md): 296 entries, q to qyrus
- [r-001](r-001.md): 1,687 entries, r-btw to ryzome
- [s-001](s-001.md): 2,485 entries, s to spanning
- [s-002](s-002.md): 1,444 entries, spanning to szell
- [t-001](t-001.md): 1,914 entries, t to tzar-bot
- [u-001](u-001.md): 510 entries, u-blox-docs to uxmachine
- [v-001](v-001.md): 776 entries, v-marketing-kit to vyre
- [w-001](w-001.md): 902 entries, w2l to wzrd
- [x-001](x-001.md): 210 entries, x to xyne-claw
- [y-001](y-001.md): 228 entries, y to yzel-wildberries
- [z-001](z-001.md): 332 entries, z-image-mcp to zz-plugin-eval
