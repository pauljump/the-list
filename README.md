# The list

Everything people have built for Claude Code and published on GitHub, with what each thing does and where it lives. Plugins, skills, agents, commands, MCP servers and hooks. Skills and agents written for other coding agents in the same file formats are here too.

| | Entries | What it is |
|---|---:|---|
| [Plugins](plugins/) | 113,195 | entries of marketplace listings |
| [Skills](skills/) | 938,965 | `SKILL.md` files |
| [Agents](agents/) | 173,382 | subagent definitions, `agents/*.md` |
| [Commands](commands/) | 166,738 | slash commands, `commands/*.md` |
| [MCP servers](mcp-servers/) | 19,901 | servers named in `.mcp.json` files, plus a directory of server repos |
| [Hooks](hooks/) | 51,124 | hook setups in `hooks.json` and `settings.json` |
| [Repos](repos.csv) | 100,432 | every repo that holds any of the above |

Start with [TOP.md](TOP.md) for the most installed and most copied.

## How to use it

- **Read it:** each folder has alphabetical pages that GitHub can show, indexed in the folder's README.
- **Take it:** each folder has the same list as CSV. Big lists are split into numbered parts.
- **Point an agent at it:** the CSVs are plain files at stable URLs, `https://raw.githubusercontent.com/pauljump/the-list/main/<folder>/<file>.csv`.

## How it was made

1. **Find the repos** (2026-09-19 to 2026-11-13; most were found in September 2026). Anthropic's official, community and knowledge-work marketplaces; GitHub repo search on fifteen topics; GitHub code search for `marketplace.json`, `plugin.json`, `hooks.json` and hook settings; the claudemarketplaces.com sitemaps; ten awesome-lists; and every marketplace found inside any repo, followed in turn. 130,072 repos seen.
2. **List their files.** One file listing per repo, keeping the paths that are Claude Code components.
3. **Read the files** (2026-11-13). Each distinct file once, by its git hash, so the text matches the listing. Names and descriptions come from each file's own frontmatter.
4. **Fold the copies.** Most of GitHub's skills are copies of other skills. Identical entries are shown once, at the original, with a count of how many repos carry them.

No model wrote or judged anything here. Every description is the author's own, cut at 600 characters. Install counts are from skills.sh.

## What it is not

- Not reviewed. Nothing here was run or checked, and being listed is not a recommendation. Plugins and hooks run code on your machine; read them first.
- Not live. It is a snapshot, and some repos have since moved or gone.
- Not everything. Private repos, and public ones the searches missed, are not here.
- Email addresses and anything that looked like a key were removed from descriptions.

## Numbers

- **Skills:** 1,681,040 files found, 1,110,772 distinct, 1,091,894 read, 938,965 entries after folding copies.
- **Agents:** 300,619 files found, 212,078 distinct, 206,286 read, 173,382 entries after folding copies.
- **Commands:** 271,362 files found, 185,850 distinct, 182,099 read, 166,738 entries after folding copies.
- **MCP servers:** 21,405 files found, 19,901 entries after folding copies.
- **Hooks:** 67,549 files found, 51,124 entries after folding copies.
- **Plugins:** 135,679 marketplace entries, 113,195 after folding copies, 101,356 with a description.
- **Repos:** 130,072 seen, 110,898 opened, 16,106 already gone, 3,023 MCP server repos kept for their description only.

The scripts that read the files and build these pages are in `crawl/` and `build.py`. The crawl database itself is several gigabytes and is not in this repo.
