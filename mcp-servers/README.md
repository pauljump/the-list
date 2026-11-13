# MCP servers

19,901 MCP servers: 15,603 that people wire into Claude Code, read from 21,405 `.mcp.json` files, and 4,298 server repos from the claudemarketplaces.com MCP directory.

## Get it

- [`mcp-servers.csv`](mcp-servers.csv) (3 MB)

Columns: `name`, `description`, `source`, `type`, `command`, `package`, `host`, `copies`, `repo`, `url`, `stars`.

## Notes

- `source` is `config` for a server found in someone's `.mcp.json`, and `directory` for a server repo listed in the claudemarketplaces.com MCP directory.
- Config entries: one per server name and target (package or host). `copies` is how many configs use it, the closest thing here to a popularity count. Only the launcher, the package name and the host are kept; arguments, environment variables, headers and URL paths are dropped because configs often carry keys. Config files have no description field, so those entries have none.
- Directory entries: the description is the repo's own. The same server can appear under both sources.

## Browse

- [0-9-001](0-9-001.md): 84 entries, 0x-mcp to 飞书
- [a-001](a-001.md): 1,826 entries, a to azuredevops
- [b-001](b-001.md): 667 entries, b to byterover-mcp
- [c-001](c-001.md): 1,989 entries, c to cyrus
- [d-001](d-001.md): 872 entries, d to dynatrace-mcp
- [e-001](e-001.md): 506 entries, e to e签宝
- [f-001](f-001.md): 713 entries, f1 to Fynd
- [g-001](g-001.md): 1,003 entries, g to gyst
- [h-001](h-001.md): 511 entries, h1 to hzdb
- [i-001](i-001.md): 382 entries, i-ching to izTolkMcp
- [j-001](j-001.md): 314 entries, j-quants-doc-mcp to jxscout
- [k-001](k-001.md): 378 entries, k12mcp to kyvos-mcp
- [l-001](l-001.md): 666 entries, l402-kit to LystBot
- [m-001](m-001.md): 1,998 entries, m to mywiki
- [n-001](n-001.md): 553 entries, n8n to nyra
- [o-001](o-001.md): 682 entries, o2 to ozon-perf
- [p-001](p-001.md): 1,321 entries, p21-connector to pyxel-mcp
- [q-001](q-001.md): 150 entries, q-ring to qyrus
- [r-001](r-001.md): 867 entries, r-btw to ryzome
- [s-001](s-001.md): 1,965 entries, s to szell
- [t-001](t-001.md): 956 entries, t to Typst MCP Server
- [u-001](u-001.md): 264 entries, u-he-preset-randomizer to uxai
- [v-001](v-001.md): 376 entries, v-marketing-kit to vynn
- [w-001](w-001.md): 463 entries, w8s-astro-mcp to Wyndham Hotels and Resorts
- [x-001](x-001.md): 114 entries, x to xtask
- [y-001](y-001.md): 124 entries, y0slack to yutu
- [z-001](z-001.md): 157 entries, z-image-mcp to zz-plugin-eval
