# The list

Everything people have built for Claude Code and published on GitHub, with what each thing does and where it lives. Plugins, skills, agents, commands, MCP servers and hooks. Skills and agents written for other coding agents in the same file formats are here too.

| | Entries | What it is |
|---|---:|---|
| [Plugins](plugins/) | 170,385 | entries of marketplace listings |
| [Skills](skills/) | 1,927,044 | `SKILL.md` files |
| [Agents](agents/) | 297,057 | subagent definitions, `agents/*.md` |
| [Commands](commands/) | 238,286 | slash commands, `commands/*.md` |
| [MCP servers](mcp-servers/) | 31,791 | servers named in `.mcp.json` files, plus a directory of server repos |
| [Hooks](hooks/) | 81,160 | hook setups in `hooks.json` and `settings.json` |
| [Repos](repos.csv) | 189,756 | every repo that holds any of the above |

Start with [TOP.md](TOP.md) for the most installed and most copied.

## How to use it

- **Read it:** each folder has alphabetical pages that GitHub can show, indexed in the folder's README.
- **Take it:** each folder has the same list as CSV. Big lists are split into numbered parts.
- **Point an agent at it:** the CSVs are plain files at stable URLs, `https://raw.githubusercontent.com/pauljump/the-list/main/<folder>/<file>.csv`.

## How it was made

1. **Find the repos** (2026-09-19 to 2026-11-20; most were found in September 2026). Anthropic's official, community and knowledge-work marketplaces; GitHub repo search on fifteen topics; GitHub code search for `marketplace.json`, `plugin.json`, `hooks.json` and hook settings; the claudemarketplaces.com sitemaps; ten awesome-lists; and every marketplace found inside any repo, followed in turn. 322,396 repos seen.
2. **List their files.** One file listing per repo, keeping the paths that are Claude Code components.
3. **Read the files** (2026-11-20). Each distinct file once, by its git hash, so the text matches the listing. Names and descriptions come from each file's own frontmatter.
4. **Fold the copies.** Most of GitHub's skills are copies of other skills. Identical entries are shown once, at the original, with a count of how many repos carry them.

No model wrote or judged anything here. Every description is the author's own, cut at 600 characters. Install counts are from skills.sh.

## What it is not

- Not reviewed. Nothing here was run or checked, and being listed is not a recommendation. Plugins and hooks run code on your machine; read them first.
- Not live. It is a snapshot, and some repos have since moved or gone.
- Not everything. Private repos, and public ones the searches missed, are not here.
- Email addresses and anything that looked like a key were removed from descriptions.

## Numbers

- **Skills:** 5,240,073 files found, 2,451,085 distinct, 2,417,818 read, 1,927,044 entries after folding copies.
- **Agents:** 615,961 files found, 373,352 distinct, 365,439 read, 297,057 entries after folding copies.
- **Commands:** 458,028 files found, 273,119 distinct, 268,753 read, 238,286 entries after folding copies.
- **MCP servers:** 41,163 files found, 31,791 entries after folding copies.
- **Hooks:** 124,268 files found, 81,160 entries after folding copies.
- **Plugins:** 228,220 marketplace entries, 170,385 after folding copies, 157,891 with a description.
- **Repos:** 322,396 seen, 208,640 opened, 19,337 already gone, 77,002 found but not opened yet (the crawl is still running; about 4,000 of these are MCP server repos kept for their description only).
- **In progress:** 1,582 files are still being read; this list will grow.

The scripts that read the files and build these pages are in `crawl/` and `build.py`. The crawl database itself is several gigabytes and is not in this repo.
