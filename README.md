# The list

Everything people have built for Claude Code and published on GitHub, with what each thing does and where it lives. Plugins, skills, agents, commands, MCP servers and hooks. Skills and agents written for other coding agents in the same file formats are here too.

| | Entries | What it is |
|---|---:|---|
| [Plugins](plugins/) | 187,380 | entries of marketplace listings |
| [Skills](skills/) | 2,688,670 | `SKILL.md` files |
| [Agents](agents/) | 411,250 | subagent definitions, `agents/*.md` |
| [Commands](commands/) | 321,510 | slash commands, `commands/*.md` |
| [MCP servers](mcp-servers/) | 38,767 | servers named in `.mcp.json` files, plus a directory of server repos |
| [Hooks](hooks/) | 92,827 | hook setups in `hooks.json` and `settings.json` |
| [Repos](repos/) | 339,949 | every repo that holds any of the above |

Start with [TOP.md](TOP.md) for the most installed and most copied.

## How to use it

- **Read it:** each folder has alphabetical pages that GitHub can show, indexed in the folder's README.
- **Take it:** each folder has the same list as CSV. Big lists are split into numbered parts.
- **Point an agent at it:** the CSVs are plain files at stable URLs, `https://raw.githubusercontent.com/pauljump/the-list/main/<folder>/<file>.csv`.

## How it was made

1. **Find the repos** (2026-09-19 to 2026-11-24; most were found in September 2026). Anthropic's official, community and knowledge-work marketplaces; GitHub repo search on fifteen topics; GitHub code search for `marketplace.json`, `plugin.json`, `hooks.json` and hook settings; the claudemarketplaces.com sitemaps; ten awesome-lists; and every marketplace found inside any repo, followed in turn. 419,673 repos seen.
2. **List their files.** One file listing per repo, keeping the paths that are Claude Code components.
3. **Read the files** (2026-11-24). Each distinct file once, by its git hash, so the text matches the listing. Names and descriptions come from each file's own frontmatter.
4. **Fold the copies.** Most of GitHub's skills are copies of other skills. Identical entries are shown once, at the original, with a count of how many repos carry them.

No model wrote or judged anything here. Every description is the author's own, cut at 600 characters. Install counts are from skills.sh.

## What it is not

- Not reviewed. Nothing here was run or checked, and being listed is not a recommendation. Plugins and hooks run code on your machine; read them first.
- Not live. It is a snapshot, and some repos have since moved or gone.
- Not everything. Private repos, and public ones the searches missed, are not here. GitHub's search returns at most 1,000 results per query, so files in crowded sizes were not all reachable.
- Email addresses and anything that looked like a key were removed from descriptions.

## Numbers

- **Skills:** 7,342,607 files found, 3,350,657 distinct, 3,329,861 read, 2,688,670 entries after folding copies.
- **Agents:** 856,921 files found, 510,730 distinct, 504,629 read, 411,250 entries after folding copies.
- **Commands:** 644,497 files found, 366,564 distinct, 362,723 read, 321,510 entries after folding copies.
- **MCP servers:** 54,605 files found, 38,767 entries after folding copies.
- **Hooks:** 157,209 files found, 92,827 entries after folding copies.
- **Plugins:** 257,759 marketplace entries, 187,380 after folding copies, 174,700 with a description.
- **Repos:** 419,673 seen, 377,271 opened, 19,749 already gone, 5,021 found but not opened yet (the crawl is still running; about 4,000 of these are MCP server repos kept for their description only).

The scripts that read the files and build these pages are in `crawl/` and `build.py`. The crawl database itself is several gigabytes and is not in this repo.
