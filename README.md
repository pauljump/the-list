# The list

Everything people have built for Claude Code and published on GitHub, with what each thing does and where it lives. Plugins, skills, agents, commands, MCP servers and hooks. Skills and agents written for other coding agents in the same file formats are here too.

| | Entries | What it is |
|---|---:|---|
| [Plugins](plugins/) | 193,501 | entries of marketplace listings |
| [Skills](skills/) | 3,110,388 | `SKILL.md` files |
| [Agents](agents/) | 492,068 | subagent definitions, `agents/*.md` |
| [Commands](commands/) | 371,162 | slash commands, `commands/*.md` |
| [MCP servers](mcp-servers/) | 62,022 | servers named in `.mcp.json` files, plus a directory of server repos |
| [Hooks](hooks/) | 102,967 | hook setups in `hooks.json` and `settings.json` |
| [Repos](repos/) | 490,888 | every repo that holds any of the above |

Start with [TOP.md](TOP.md) for the most installed and most copied.

## How to use it

- **Read it:** each folder has alphabetical pages that GitHub can show, indexed in the folder's README.
- **Take it:** each folder has the same list as CSV. Big lists are split into numbered parts.
- **Point an agent at it:** the CSVs are plain files at stable URLs, `https://raw.githubusercontent.com/pauljump/the-list/main/<folder>/<file>.csv`.

## How it was made

1. **Find the repos** (2026-09-19 to 2026-11-27; most were found in September 2026). Anthropic's official, community and knowledge-work marketplaces; GitHub repo search on fifteen topics; GitHub code search for `marketplace.json`, `plugin.json`, `hooks.json` and hook settings; the claudemarketplaces.com sitemaps; ten awesome-lists; and every marketplace found inside any repo, followed in turn. 580,188 repos seen.
2. **List their files.** One file listing per repo, keeping the paths that are Claude Code components.
3. **Read the files** (2026-11-27). Each distinct file once, by its git hash, so the text matches the listing. Names and descriptions come from each file's own frontmatter.
4. **Fold the copies.** Most of GitHub's skills are copies of other skills. Identical entries are shown once, at the original, with a count of how many repos carry them.

No model wrote or judged anything here. Every description is the author's own, cut at 600 characters. Install counts are from skills.sh.

## What it is not

- Not reviewed. Nothing here was run or checked, and being listed is not a recommendation. Plugins and hooks run code on your machine; read them first.
- Not live. It is a snapshot, and some repos have since moved or gone.
- Not everything. Private repos, and public ones the searches missed, are not here. GitHub's search returns at most 1,000 results per query, so files in crowded sizes were not all reachable. The crawl stopped on 2026-11-27 with the code search for small `SKILL.md` files unfinished and the searches for agent, command and `.claude/skills` files not run, so repos only those searches would have found are missing.
- Email addresses and anything that looked like a key were removed from descriptions.

## Numbers

- **Skills:** 8,462,611 files found, 3,834,198 distinct, 3,812,707 read, 3,110,388 entries after folding copies.
- **Agents:** 1,016,602 files found, 606,559 distinct, 600,341 read, 492,068 entries after folding copies.
- **Commands:** 756,099 files found, 421,776 distinct, 417,974 read, 371,162 entries after folding copies.
- **MCP servers:** 99,095 files found, 62,022 entries after folding copies.
- **Hooks:** 188,144 files found, 102,967 entries after folding copies.
- **Plugins:** 268,663 marketplace entries, 193,501 after folding copies, 180,686 with a description.
- **Repos:** 580,188 seen, 539,663 opened, 19,746 already gone, 2,880 found but not opened yet (the crawl is still running; about 4,000 of these are MCP server repos kept for their description only).

The scripts that read the files and build these pages are in `crawl/` and `build.py`. The crawl database itself is several gigabytes and is not in this repo.
