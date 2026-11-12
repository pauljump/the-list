#!/usr/bin/env python3
"""Build the list from a Signal crawl database.

    python3 build.py /path/to/signal.db

Reads the `plugins` and `repos` tables (read-only) and writes the-list.csv, the-list.md,
list/*.md and README.md next to this file. No network, no model calls.
"""
import csv
import re
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

OUT = Path(__file__).resolve().parent
MAX_DESC = 600
PAGE_BYTES = 380_000  # GitHub stops rendering Markdown a little past 500 KB


EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def clean(s):
    return EMAIL.sub("[email removed]", re.sub(r"\s+", " ", s or "").strip())


def clip(s):
    return s if len(s) <= MAX_DESC else s[: MAX_DESC - 1].rstrip() + "…"


def link_for(home, kind, path, url):
    if not home:
        return url or ""
    base = f"https://github.com/{home}"
    p = (path or "").strip()
    if kind in ("relative", "git-subdir") and p and ".." not in p and not p.startswith(("/", "http")):
        p = re.sub(r"^(\./)+", "", p).strip("/")
        if p and p != ".":
            return f"{base}/tree/HEAD/{p}"
    return base


def md_text(s):
    return s.replace("<", "&lt;").replace(">", "&gt;")


def main(db_path):
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    snapshot = con.execute("select max(last_seen) from plugins").fetchone()[0] or ""
    repos = {
        r["full_name"].lower(): r
        for r in con.execute("select full_name, stars, is_fork, license, pushed_at, status from repos")
    }

    def meta(home):
        r = repos.get((home or "").lower())
        return {
            "stars": (r["stars"] or 0) if r else 0,
            "fork": bool(r["is_fork"]) if r else False,
            "license": (r["license"] or "") if r else "",
            "pushed": (r["pushed_at"] or "")[:10] if r else "",
            "gone": bool(r and r["status"] == "gone"),
        }

    # Stage 1: one entry per (home repo, name); a plugin listed in many marketplaces is one plugin.
    by_home = {}
    n_rows = 0
    for p in con.execute(
        "select marketplace_repo, name, description, category, source_kind, source_repo, source_path, source_url from plugins"
    ):
        n_rows += 1
        name = clean(p["name"])
        if not name:
            continue
        home = clean(p["source_repo"]) or (
            "" if p["source_kind"] in ("url", "npm", "git", "archive") and p["source_url"] else p["marketplace_repo"]
        )
        desc = clean(p["description"])
        key = ((home or p["source_url"] or p["marketplace_repo"]).lower(), name.lower())
        own = bool(home) and home.lower() == p["marketplace_repo"].lower()
        rank = (own, p["marketplace_repo"].startswith("anthropics/"), len(desc))
        e = by_home.get(key)
        if e is None:
            e = by_home[key] = {"name": name, "home": home, "desc": "", "category": "", "rank": (False, False, -1),
                                "markets": set(), "url": ""}
        e["markets"].add(p["marketplace_repo"].lower())
        e["category"] = e["category"] or clean(p["category"]).lower()
        if rank > e["rank"]:
            e["rank"], e["desc"] = rank, desc
            e["url"] = link_for(home, p["source_kind"], p["source_path"], p["source_url"])

    # Stage 2: identical name + description under different repos are forks and mirrors; keep the original.
    groups = defaultdict(list)
    for key, e in by_home.items():
        groups[(e["name"].lower(), e["desc"].lower()) if e["desc"] else key].append(e)
    entries = []
    for es in groups.values():
        for e in es:
            e["meta"] = meta(e["home"])
        best = max(es, key=lambda e: (not e["meta"]["gone"], not e["meta"]["fork"], e["meta"]["stars"], len(e["markets"])))
        best["markets"] = set().union(*(e["markets"] for e in es))
        best["copies"] = len(es)
        best["category"] = best["category"] or next((e["category"] for e in es if e["category"]), "")
        entries.append(best)
    entries.sort(key=lambda e: (e["name"].lower(), -e["meta"]["stars"], e["home"].lower()))

    with open(OUT / "the-list.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["name", "description", "category", "repo", "url", "stars", "license", "last_pushed",
                    "marketplaces", "copies", "repo_gone"])
        for e in entries:
            m = e["meta"]
            w.writerow([e["name"], clip(e["desc"]), e["category"], e["home"], e["url"], m["stars"], m["license"],
                        m["pushed"], len(e["markets"]), e["copies"], "yes" if m["gone"] else ""])

    def line(e):
        d = md_text(clip(e["desc"]))
        where = f"[{e['home'] or 'source'}]({e['url']})" if e["url"] else (e["home"] or "")
        return f"- **{md_text(e['name'])}**" + (f": {d}" if d else "") + (f" ({where})" if where else "") + "\n"

    lines = [line(e) for e in entries]
    title = "# The list\n\n"
    blurb = (f"{len(entries):,} Claude Code plugins, alphabetical, with what each one does and where it lives. "
             f"Snapshot of {snapshot[:10]}.\n\n")
    (OUT / "the-list.md").write_text(title + blurb + "".join(lines), encoding="utf-8")

    # Browsable pages: alphabetical, each small enough for GitHub to render.
    pages_dir = OUT / "list"
    pages_dir.mkdir(exist_ok=True)
    for old in pages_dir.glob("*.md"):
        old.unlink()
    buckets = defaultdict(list)
    for e, ln in zip(entries, lines):
        c = e["name"][0].lower()
        buckets[c if "a" <= c <= "z" else "0-9"].append((e, ln))
    index = []
    for b in sorted(buckets):
        chunk, size, part = [], 0, 1

        def flush():
            nonlocal chunk, size, part
            if not chunk:
                return
            fn = f"{b}-{part:02d}.md"
            first, last = chunk[0][0]["name"], chunk[-1][0]["name"]
            head = f"# {b.upper()} · part {part}\n\n{len(chunk):,} plugins, {md_text(first)} to {md_text(last)}. [Back to the index](../README.md)\n\n"
            (pages_dir / fn).write_text(head + "".join(ln for _, ln in chunk), encoding="utf-8")
            index.append((fn, b.upper(), len(chunk), first, last))
            chunk, size, part = [], 0, part + 1

        for e, ln in buckets[b]:
            n = len(ln.encode("utf-8"))
            if size + n > PAGE_BYTES:
                flush()
            chunk.append((e, ln))
            size += n
        flush()

    n_desc = sum(1 for e in entries if e["desc"])
    n_gone = sum(1 for e in entries if e["meta"]["gone"])
    readme = [
        "# The list\n\n",
        f"Every Claude Code plugin found in a public marketplace listing on GitHub, with what it does. "
        f"{len(entries):,} plugins, snapshot of {snapshot[:10]}.\n\n",
        "## Get it\n\n",
        "- [`the-list.csv`](the-list.csv): everything in one file, for a spreadsheet or a script.\n",
        "- [`the-list.md`](the-list.md): the same list as one document. Too big for GitHub to show; download it.\n",
        "- [`list/`](list/): the same list in alphabetical pages that GitHub can show (index below).\n\n",
        "## What is in it\n\n",
        f"- Source: {n_rows:,} entries read from every `.claude-plugin/marketplace.json` the crawl found, "
        "including Anthropic's official, community and knowledge-work marketplaces.\n",
        f"- A plugin listed in several marketplaces appears once. Copies with the same name and description "
        f"under other repos (forks, mirrors) are folded into the original, leaving {len(entries):,}.\n",
        f"- {n_desc:,} have a description, in the author's own words, cut at {MAX_DESC} characters.\n",
        f"- {n_gone:,} point at a repo that was already deleted or renamed at crawl time (`repo_gone` in the CSV).\n",
        "- Plugins only. Standalone skills, hooks and commands that no marketplace lists are not here.\n",
        "- Nothing here was reviewed or tested. Being listed is not a recommendation.\n\n",
        "CSV columns: `name`, `description`, `category` (as the marketplace gave it, often blank), `repo`, `url`, "
        "`stars` and `license` and `last_pushed` (of the repo, not the plugin), `marketplaces` (how many list it), "
        "`copies` (how many identical entries were folded in), `repo_gone`.\n\n",
        "Rebuild: `python3 build.py /path/to/signal.db`.\n\n",
        "## Index\n\n",
    ]
    for fn, b, n, first, last in index:
        readme.append(f"- [{fn[:-3]}](list/{fn}): {n:,} plugins, {md_text(first)} to {md_text(last)}\n")
    (OUT / "README.md").write_text("".join(readme), encoding="utf-8")

    print(f"rows {n_rows:,} -> per repo+name {len(by_home):,} -> list {len(entries):,}")
    print(f"with description {n_desc:,} · repo gone {n_gone:,} · pages {len(index)} · snapshot {snapshot}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
