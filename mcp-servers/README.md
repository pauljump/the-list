# MCP servers

31,791 MCP servers: 27,531 that people wire into Claude Code, read from 41,163 `.mcp.json` files, and 4,260 server repos from the claudemarketplaces.com MCP directory.

## Get it

- [`mcp-servers.csv`](mcp-servers.csv) (5 MB)

Columns: `name`, `description`, `source`, `type`, `command`, `package`, `host`, `copies`, `repo`, `url`, `stars`.

## Notes

- `source` is `config` for a server found in someone's `.mcp.json`, and `directory` for a server repo listed in the claudemarketplaces.com MCP directory.
- Config entries: one per server name and target (package or host). `copies` is how many configs use it, the closest thing here to a popularity count. Only the launcher, the package name and the host are kept; arguments, environment variables, headers and URL paths are dropped because configs often carry keys. Config files have no description field, so those entries have none.
- Directory entries: the description is the repo's own. The same server can appear under both sources.

## Browse

- [0-9-001](0-9-001.md): 124 entries, 0bull to 飞书
- [a-001](a-001.md): 2,442 entries, a to atopile
- [a-002](a-002.md): 482 entries, atp to azurewiki
- [b-001](b-001.md): 1,084 entries, b to bzzoiro-tennis
- [c-001](c-001.md): 2,454 entries, c to contractoracle
- [c-002](c-002.md): 593 entries, Contracts Analyzer to cyrus
- [d-001](d-001.md): 1,449 entries, d to dynatrace-mcp-server
- [e-001](e-001.md): 827 entries, e to e签宝
- [f-001](f-001.md): 1,472 entries, f1 to fyreflock
- [g-001](g-001.md): 1,564 entries, g to gyst
- [h-001](h-001.md): 818 entries, h1 to hzdb
- [i-001](i-001.md): 658 entries, i-ching to izTolkMcp
- [j-001](j-001.md): 473 entries, j-quants-doc-mcp to jxscout
- [k-001](k-001.md): 667 entries, k-deal-skill to kyvos-mcp
- [l-001](l-001.md): 1,097 entries, l0s to LystBot
- [m-001](m-001.md): 2,237 entries, m to modelica
- [m-002](m-002.md): 501 entries, Modellix Docs Search to mz-relay
- [n-001](n-001.md): 883 entries, N8N to nzc
- [o-001](o-001.md): 1,083 entries, o-sumo to ozpb
- [p-001](p-001.md): 2,111 entries, p0 to pyxel-mcp
- [q-001](q-001.md): 237 entries, q to qyrus
- [r-001](r-001.md): 1,396 entries, r-btw to ryzome
- [s-001](s-001.md): 2,461 entries, s to stdlib
- [s-002](s-002.md): 733 entries, steady to szell
- [t-001](t-001.md): 1,558 entries, t to Typst MCP Server
- [u-001](u-001.md): 407 entries, u-he-preset-randomizer to uxmachine
- [v-001](v-001.md): 622 entries, v-marketing-kit to vyre
- [w-001](w-001.md): 741 entries, w2l to wzrd
- [x-001](x-001.md): 167 entries, x to xydc-mcp
- [y-001](y-001.md): 188 entries, y to ywm
- [z-001](z-001.md): 262 entries, z-image-mcp to zz-plugin-eval
