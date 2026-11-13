#!/usr/bin/env python3
"""Build the list from a Signal crawl database.

    python3 build.py /path/to/signal.db

Reads the crawl (read-only) and writes plugins/, skills/, agents/, commands/, mcp-servers/, hooks/,
repos.csv, TOP.md and README.md next to this file. No network, no model calls.
Run crawl/fetch_text.py first: skills, agents and commands take their descriptions from the file text.
"""
import csv
import json
import re
import shutil
import sqlite3
import sys
import zlib
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

OUT = Path(__file__).resolve().parent
MAX_DESC = 600
PAGE_BYTES = 380_000     # GitHub stops rendering Markdown a little past 500 KB
CSV_BYTES = 45_000_000   # GitHub warns above 50 MB a file
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SECRET = re.compile(r"(?<![A-Za-z0-9])(gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9_-]{24,}|AKIA[A-Z0-9]{16}"
                    r"|xox[abpr]-[0-9]{6,}-[A-Za-z0-9-]{10,}|AIza[A-Za-z0-9_-]{35}|eyJ[A-Za-z0-9_-]{20,}\.eyJ[A-Za-z0-9_-]{10,})")


def _redact(m):
    t = m.group(0)   # a real key mixes cases and digits; a hyphenated name like "sk-requirements-engineering" does not
    keyish = any(c.isdigit() for c in t) and any(c.isupper() for c in t) and any(c.islower() for c in t)
    return "[secret removed]" if keyish or t.startswith("AKIA") else t


def clean(s):
    s = re.sub(r"\s+", " ", s or "").strip()
    return SECRET.sub(_redact, EMAIL.sub("[email removed]", s))


def clip(s, n=MAX_DESC):
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def md(s):
    return s.replace("<", "&lt;").replace(">", "&gt;")


def num(n):
    n = int(n or 0)
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M".replace(".0M", "M")
    if n >= 10_000:
        return f"{n / 1000:.0f}k"
    if n >= 1000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return str(n)


def gh_url(repo, path="", tree=False):
    if not path:
        return f"https://github.com/{repo}"
    return f"https://github.com/{repo}/{'tree' if tree else 'blob'}/HEAD/{quote(path)}"


class Build:
    def __init__(self, db_path):
        self.con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        self.con.row_factory = sqlite3.Row
        self.repos = {}
        for r in self.con.execute("select full_name, description, stars, forks, is_fork, archived, license, pushed_at, "
                                  "created_at, topics, owner_type, homepage, status, n_components from repos"):
            self.repos[r["full_name"].lower()] = r
        self.stats = {}
        self.has_blobs = bool(self.con.execute("select 1 from sqlite_master where name='blobs'").fetchone())

    def meta(self, repo):
        r = self.repos.get((repo or "").lower())
        if not r:
            return {"stars": 0, "fork": False, "license": "", "pushed": "", "gone": False}
        return {"stars": r["stars"] or 0, "fork": bool(r["is_fork"]), "license": r["license"] or "",
                "pushed": (r["pushed_at"] or "")[:10], "gone": r["status"] == "gone"}

    # ---------- output ----------

    def write_kind(self, folder, title, blurb, entries, columns, row, line, notes):
        """entries sorted by name. Writes <folder>/<folder>[-N].csv, alphabetical pages and an index."""
        d = OUT / folder
        if d.exists():
            shutil.rmtree(d)
        d.mkdir()
        # CSV, split so no part is too big for GitHub
        parts, f, w, size = [], None, None, 0
        for e in entries:
            cells = row(e)
            n = sum(len(str(c).encode("utf-8")) + 3 for c in cells)
            if f is None or size + n > CSV_BYTES:
                if f:
                    f.close()
                parts.append(d / f"{folder}-{len(parts) + 1}.csv")
                f = open(parts[-1], "w", newline="", encoding="utf-8")
                w = csv.writer(f)
                w.writerow(columns)
                size = 0
            w.writerow(cells)
            size += n
        if f:
            f.close()
        if len(parts) == 1:
            parts[0] = parts[0].rename(d / f"{folder}.csv")
        # pages
        buckets = defaultdict(list)
        for e in entries:
            c = e["name"][0].lower()
            buckets[c if "a" <= c <= "z" else "0-9"].append(e)
        index = []
        for b in sorted(buckets):
            chunk, size, part = [], 0, 1

            def flush():
                nonlocal chunk, size, part
                if not chunk:
                    return
                fn = f"{b}-{part:03d}.md"
                first, last = chunk[0][0]["name"], chunk[-1][0]["name"]
                head = (f"# {title} · {b.upper()} · part {part}\n\n{len(chunk):,} entries, {md(clip(first, 60))} to "
                        f"{md(clip(last, 60))}. [Index](README.md) · [Everything](../README.md)\n\n")
                (d / fn).write_text(head + "".join(ln for _, ln in chunk), encoding="utf-8")
                index.append((fn, len(chunk), first, last))
                chunk, size, part = [], 0, part + 1

            for e in buckets[b]:
                ln = line(e)
                n = len(ln.encode("utf-8"))
                if size + n > PAGE_BYTES:
                    flush()
                chunk.append((e, ln))
                size += n
            flush()
        out = [f"# {title}\n\n", blurb + "\n\n", "## Get it\n\n"]
        for p in parts:
            out.append(f"- [`{p.name}`]({p.name}) ({p.stat().st_size / 1e6:.0f} MB)\n")
        out.append("\nColumns: " + ", ".join(f"`{c}`" for c in columns) + ".\n\n")
        if notes:
            out += ["## Notes\n\n"] + [f"- {n}\n" for n in notes] + ["\n"]
        out.append("## Browse\n\n")
        for fn, n, first, last in index:
            out.append(f"- [{fn[:-3]}]({fn}): {n:,} entries, {md(clip(first, 50))} to {md(clip(last, 50))}\n")
        (d / "README.md").write_text("".join(out), encoding="utf-8")
        self.stats[folder] = {"entries": len(entries), "pages": len(index), "csv": [p.name for p in parts]}

    # ---------- plugins ----------

    def plugins(self):
        con = self.con
        mk_name = {(r["repo"].lower(), r["path"]): clean(r["name"]) for r in con.execute("select repo, path, name from marketplaces")}
        # what sits inside each plugin: component paths per repo
        inside = defaultdict(list)
        for r in con.execute("select repo, kind, path from components where kind in ('skill','agent','command','hook','mcp')"):
            inside[r["repo"].lower()].append((r["path"], r["kind"]))
        plugin_json = {}
        if self.has_blobs:
            for r in con.execute("select c.repo, c.path, b.description from components c join blobs b on b.sha = c.sha "
                                 "where c.kind = 'plugin' and b.description is not null"):
                plugin_json[(r["repo"].lower(), r["path"])] = r["description"]

        by_home, n_rows = {}, 0
        for p in con.execute("select marketplace_repo, marketplace_path, name, description, version, category, keywords, "
                             "source_kind, source_repo, source_path, source_url from plugins"):
            n_rows += 1
            name = clean(p["name"])
            if not name:
                continue
            home = clean(p["source_repo"]) or (
                "" if p["source_kind"] in ("url", "npm", "git", "archive") and p["source_url"] else p["marketplace_repo"])
            desc = clean(p["description"])
            key = ((home or p["source_url"] or p["marketplace_repo"]).lower(), name.lower())
            own = bool(home) and home.lower() == p["marketplace_repo"].lower()
            official = p["marketplace_repo"].startswith("anthropics/")
            e = by_home.get(key)
            if e is None:
                e = by_home[key] = {"name": name, "home": home, "desc": "", "category": "", "version": "", "keywords": "",
                                    "rank": (False, False, -1), "markets": set(), "url": "", "prefix": None,
                                    "mk": None, "mk_rank": (-1, -1, -1)}
            e["markets"].add(p["marketplace_repo"].lower())
            e["category"] = e["category"] or clean(p["category"]).lower()
            e["version"] = e["version"] or clean(p["version"])
            if not e["keywords"] and p["keywords"]:
                try:
                    kw = json.loads(p["keywords"])
                    e["keywords"] = clean(", ".join(str(k) for k in kw)) if isinstance(kw, list) else clean(str(kw))
                except ValueError:
                    e["keywords"] = clean(p["keywords"])
            rank = (own, official, len(desc))
            if rank > e["rank"]:
                e["rank"], e["desc"] = rank, desc
                path = (p["source_path"] or "").strip()
                prefix = None
                if home:
                    if p["source_kind"] in ("relative", "git-subdir") and ".." not in path and not path.startswith(("/", "http")):
                        prefix = re.sub(r"^(\./)+", "", path).strip("/")
                        prefix = "" if prefix == "." else prefix
                    elif not path:
                        prefix = ""
                e["prefix"] = prefix
                e["url"] = (gh_url(home, prefix, tree=True) if prefix else gh_url(home)) if home else (p["source_url"] or "")
            mk_rank = (official, own, self.meta(p["marketplace_repo"])["stars"])
            if mk_rank > e["mk_rank"]:
                e["mk_rank"] = mk_rank
                e["mk"] = (p["marketplace_repo"], mk_name.get((p["marketplace_repo"].lower(), p["marketplace_path"]), ""))

        groups = defaultdict(list)
        for key, e in by_home.items():
            groups[(e["name"].lower(), e["desc"].lower()) if e["desc"] else key].append(e)
        entries = []
        for es in groups.values():
            for e in es:
                e["meta"] = self.meta(e["home"])
            best = max(es, key=lambda e: (not e["meta"]["gone"], not e["meta"]["fork"], e["meta"]["stars"], len(e["markets"])))
            best["markets"] = set().union(*(e["markets"] for e in es))
            best["copies"] = len(es)
            for k in ("category", "version", "keywords"):
                best[k] = best[k] or next((e[k] for e in es if e[k]), "")
            entries.append(best)
        n_filled = 0
        for e in entries:
            counts = defaultdict(int)
            if e["home"] and e["prefix"] is not None:
                pre = e["prefix"] + "/" if e["prefix"] else ""
                for path, kind in inside.get(e["home"].lower(), ()):
                    if path.startswith(pre):
                        counts[kind] += 1
                if not e["desc"]:
                    d = plugin_json.get((e["home"].lower(), pre + ".claude-plugin/plugin.json"))
                    if d:
                        e["desc"], n_filled = clean(d), n_filled + 1
            e["inside"] = counts
            if not e["desc"] and e["home"] and e["prefix"] == "":
                r = self.repos.get(e["home"].lower())
                if r and r["description"]:
                    e["desc"], n_filled = clean(r["description"]), n_filled + 1
        entries.sort(key=lambda e: (e["name"].lower(), -e["meta"]["stars"], e["home"].lower()))

        def inside_text(e):
            c = e["inside"]
            bits = [f"{c[k]} {label}{'s' if c[k] != 1 else ''}" for k, label in
                    (("skill", "skill"), ("command", "command"), ("agent", "agent"), ("hook", "hook file"), ("mcp", "MCP config")) if c[k]]
            return ", ".join(bits)

        def row(e):
            m, c, mk = e["meta"], e["inside"], e["mk"] or ("", "")
            return [e["name"], clip(e["desc"]), e["category"], e["keywords"][:200], e["version"][:30], e["home"], e["url"],
                    m["stars"], m["license"], m["pushed"], c["skill"], c["command"], c["agent"], c["hook"], c["mcp"],
                    mk[0], mk[1], len(e["markets"]), e["copies"], "yes" if m["gone"] else ""]

        def line(e):
            m = e["meta"]
            where = f"[{e['home'] or 'source'}]({e['url']})" if e["url"] else (e["home"] or "")
            tail = [where] if where else []
            if m["stars"]:
                tail.append(f"★{num(m['stars'])}")
            it = inside_text(e)
            if it:
                tail.append(it)
            d = md(clip(e["desc"]))
            return f"- **{md(e['name'])}**" + (f": {d}" if d else "") + (f" ({' · '.join(tail)})" if tail else "") + "\n"

        n_desc = sum(1 for e in entries if e["desc"])
        n_gone = sum(1 for e in entries if e["meta"]["gone"])
        self.write_kind(
            "plugins", "Plugins",
            f"{len(entries):,} Claude Code plugins: every entry of every `.claude-plugin/marketplace.json` the crawl found, "
            "with what it does, where it lives and what is inside it.",
            entries,
            ["name", "description", "category", "keywords", "version", "repo", "url", "stars", "license", "last_pushed",
             "skills", "commands", "agents", "hook_files", "mcp_configs", "marketplace_repo", "marketplace_name",
             "marketplaces", "copies", "repo_gone"],
            row, line,
            [f"Built from {n_rows:,} marketplace entries. A plugin listed in several marketplaces appears once; copies with "
             f"the same name and description under other repos (forks, mirrors) are folded into the original (`copies`).",
             f"{n_desc:,} have a description, in the author's words, cut at {MAX_DESC} characters. {n_filled:,} of those were "
             "blank in the marketplace and filled from the plugin's own `plugin.json` or its repo description.",
             "`skills`, `commands`, `agents`, `hook_files`, `mcp_configs` count the files found under the plugin's folder.",
             "To install one: `/plugin marketplace add <marketplace_repo>` then `/plugin install <name>@<marketplace_name>`.",
             f"{n_gone:,} point at a repo that was already deleted or renamed at crawl time (`repo_gone`).",
             "`stars`, `license` and `last_pushed` belong to the repo, not the plugin."])
        self.stats["plugins"].update(rows=n_rows, described=n_desc, gone=n_gone)
        return entries

    # ---------- skills, agents, commands ----------

    def components(self, kind, folder, title, blurb, extra_cols, extra, notes):
        con = self.con
        total_files = con.execute("select count(*) from components where kind=?", (kind,)).fetchone()[0]
        unique = con.execute("select count(distinct sha) from components where kind=?", (kind,)).fetchone()[0]
        installs = {}
        if kind == "skill":
            listed = {}
            for r in con.execute("select owner, repo, skill, installs, weekly, source_repo from skill_installs where installs is not null"):
                listed[((r["source_repo"] or f"{r['owner']}/{r['repo']}").lower(), r["skill"].lower())] = (r["installs"], r["weekly"])
            for r in con.execute("select repo, name, sha from components where kind = 'skill'"):
                hit = listed.get((r["repo"].lower(), (r["name"] or "").lower()))
                if hit and hit[0] > installs.get(r["sha"], (0,))[0]:
                    installs[r["sha"]] = hit
        groups = {}
        n_text = 0
        q = """select x.sha, x.repo, x.path, x.cname, x.n, b.name, b.description, b.lead, b.fm from (
                   select c.sha, c.repo, c.path, c.name cname, count(*) over (partition by c.sha) n,
                          row_number() over (partition by c.sha order by (coalesce(r.status,'')='gone'), coalesce(r.is_fork,0),
                                             coalesce(r.stars,0) desc, c.repo) rn
                   from components c left join repos r on r.full_name = c.repo where c.kind = ?
               ) x join blobs b on b.sha = x.sha where x.rn = 1 and b.status = 'ok'"""
        for r in con.execute(q, (kind,)):
            n_text += 1
            name = clean(r["name"]) or clean(r["cname"])
            if not name:
                continue
            desc = clean(r["description"]) or clean(r["lead"])
            m = self.meta(r["repo"])
            ins = installs.get(r["sha"])
            cand = {"name": name[:200], "desc": desc, "repo": r["repo"], "path": r["path"], "meta": m, "copies": r["n"],
                    "fm": r["fm"], "installs": ins[0] if ins else 0, "weekly": ins[1] if ins else None}
            key = (name.lower(), desc.lower()) if desc else (r["sha"],)
            g = groups.get(key)
            if g is None:
                groups[key] = cand
            else:
                copies, inst, wk = g["copies"] + cand["copies"], max(g["installs"], cand["installs"]), g["weekly"] or cand["weekly"]
                rank = lambda e: (not e["meta"]["gone"], not e["meta"]["fork"], e["meta"]["stars"], e["copies"])
                if rank(cand) > rank(g):
                    groups[key] = g = cand
                g["copies"], g["installs"], g["weekly"] = copies, inst, wk
        entries = list(groups.values())
        n_sh = 0
        if kind == "skill":   # skills.sh lists skills from repos the crawl never opened
            have = {(e["repo"].lower(), e["name"].lower()) for e in entries}
            for r in con.execute("select owner, repo, skill, installs, weekly, description, source_repo from skill_installs "
                                 "where description is not null and description != ''"):
                repo = r["source_repo"] or f"{r['owner']}/{r['repo']}"
                if (repo.lower(), r["skill"].lower()) in have:
                    continue
                have.add((repo.lower(), r["skill"].lower()))
                entries.append({"name": clean(r["skill"]), "desc": clean(r["description"]), "repo": repo, "path": "",
                                "meta": self.meta(repo), "copies": 1, "fm": None, "installs": r["installs"] or 0,
                                "weekly": r["weekly"]})
                n_sh += 1
        for e in entries:
            fm = {}
            if e["fm"]:
                try:
                    fm = json.loads(e["fm"])
                except ValueError:
                    fm = {}
            e["x"] = [clean(str(fm.get(k) or fm.get(k.replace("_", "-")) or ""))[:300] for k in extra]
            wk = None
            if e["weekly"]:
                try:
                    wk = json.loads(e["weekly"])[-1]
                except (ValueError, IndexError, TypeError):
                    wk = None
            e["wk"] = wk or 0
            if e["path"]:
                p = e["path"].rsplit("/", 1)[0] if kind == "skill" and "/" in e["path"] else e["path"]
                e["url"] = gh_url(e["repo"], p, tree=(kind == "skill" and p != e["path"]))
            else:
                e["url"] = gh_url(e["repo"])
        entries.sort(key=lambda e: (e["name"].lower(), -e["meta"]["stars"], e["repo"].lower()))

        def row(e):
            m = e["meta"]
            base = [e["name"], clip(e["desc"]), e["repo"], e["url"], m["stars"], m["license"], m["pushed"], e["copies"]]
            if kind == "skill":
                base += [e["installs"] or "", e["wk"] or ""]
            return base + e["x"]

        def line(e):
            m = e["meta"]
            tail = [f"[{e['repo']}]({e['url']})"]
            if m["stars"]:
                tail.append(f"★{num(m['stars'])}")
            if e["installs"]:
                tail.append(f"{num(e['installs'])} installs")
            if e["copies"] > 1:
                tail.append(f"{num(e['copies'])} copies")
            d = md(clip(e["desc"]))
            return f"- **{md(e['name'])}**" + (f": {d}" if d else "") + f" ({' · '.join(tail)})\n"

        cols = ["name", "description", "repo", "url", "stars", "license", "last_pushed", "copies"]
        if kind == "skill":
            cols += ["installs", "installs_last_week"]
        n_desc = sum(1 for e in entries if e["desc"])
        pending = unique - n_text
        notes = [f"The crawl found {total_files:,} of these files across all repos; {unique:,} are distinct. "
                 f"The text of {n_text:,} was read" + (f"; {pending:,} could not be (too large, binary, or gone from GitHub)." if pending else "."),
                 "Entries with the same name and description are one entry, shown at the most-starred repo that is not a fork. "
                 "`copies` is how many copies of the file the crawl found across GitHub.",
                 f"{n_desc:,} have a description: the file's own `description`, or its first paragraph when it has none. "
                 f"Cut at {MAX_DESC} characters.",
                 "`stars`, `license` and `last_pushed` belong to the repo."] + notes
        if n_sh:
            notes.append(f"{n_sh:,} entries come from skills.sh alone: listed there, in repos the crawl did not open.")
        self.write_kind(folder, title, blurb.format(n=len(entries)), entries, cols + extra_cols, row, line, notes)
        self.stats[folder].update(files=total_files, unique=unique, read=n_text, described=n_desc)
        return entries

    # ---------- MCP servers ----------

    PKG = re.compile(r"^@?[A-Za-z0-9][\w.-]*(/[\w.-]+)?(@[\w.^~-]+)?$")

    def mcp(self):
        groups = {}
        n_files = 0
        for r in self.con.execute("""select c.repo, c.path, t.z from components c join blobs b on b.sha = c.sha
                                     join blob_text t on t.sha = c.sha where c.kind = 'mcp' and b.status = 'ok'"""):
            n_files += 1
            try:
                d = json.loads(zlib.decompress(r["z"]).decode("utf-8", "replace"))
            except Exception:
                continue
            servers = d.get("mcpServers") if isinstance(d, dict) else None
            if not isinstance(servers, dict):
                servers = d if isinstance(d, dict) and all(isinstance(v, dict) for v in d.values()) else None
            if not servers:
                continue
            m = self.meta(r["repo"])
            for name, s in servers.items():
                if not isinstance(s, dict):
                    continue
                cmd = clean(str(s.get("command") or ""))[:60]
                cmd = "" if "/" in cmd and not cmd.startswith(("npx", "uvx")) else cmd   # local paths say nothing
                pkg = ""
                for a in s.get("args") or []:
                    if isinstance(a, str) and not a.startswith("-") and self.PKG.match(a) and not a.endswith((".js", ".py", ".ts", ".mjs")):
                        pkg = a
                        break
                host = ""
                url = s.get("url") or s.get("serverUrl")
                if isinstance(url, str):
                    mm = re.match(r"https?://([^/?#\s]+)", url)
                    host = mm.group(1) if mm and "@" not in mm.group(1) else ""
                kind = clean(str(s.get("type") or ("http" if host else "stdio")))[:20]
                key = (clean(str(name)).lower(), pkg.lower() or host.lower() or cmd.lower())
                cand = {"name": clean(str(name))[:120], "type": kind, "command": cmd, "package": pkg, "host": host,
                        "repo": r["repo"], "path": r["path"], "meta": m, "copies": 1}
                g = groups.get(key)
                if g is None:
                    groups[key] = cand
                else:
                    copies = g["copies"] + 1
                    if (not m["gone"], not m["fork"], m["stars"]) > (not g["meta"]["gone"], not g["meta"]["fork"], g["meta"]["stars"]):
                        groups[key] = g = cand
                    g["copies"] = copies
        entries = [e for e in groups.values() if e["name"]]
        for e in entries:
            e["desc"], e["source"] = "", "config"
        n_dir = 0
        # the directory of MCP servers on claudemarketplaces.com: one repo per server
        for r in self.con.execute("select full_name, description from repos where discovered_via like '%claudemarketplaces-mcp%' "
                                  "and status != 'gone' and description is not null and description != ''"):
            n_dir += 1
            entries.append({"name": r["full_name"].split("/")[-1], "type": "", "command": "", "package": "", "host": "",
                            "repo": r["full_name"], "path": "", "meta": self.meta(r["full_name"]), "copies": 0,
                            "desc": clean(r["description"]), "source": "directory"})
        entries.sort(key=lambda e: (e["name"].lower(), -e["copies"], e["repo"].lower()))

        def how(e):
            if e["host"]:
                return f"{e['type']} at {e['host']}"
            return " ".join(x for x in (e["command"], e["package"]) if x) or e["type"]

        def row(e):
            m = e["meta"]
            return [e["name"], clip(e["desc"]), e["source"], e["type"], e["command"], e["package"], e["host"], e["copies"] or "",
                    e["repo"], gh_url(e["repo"], e["path"]), m["stars"]]

        def line(e):
            tail = [f"[{e['repo']}]({gh_url(e['repo'], e['path'])})"]
            if e["source"] == "directory":
                if e["meta"]["stars"]:
                    tail.append(f"★{num(e['meta']['stars'])}")
                return f"- **{md(e['name'])}**: {md(clip(e['desc']))} ({' · '.join(tail)})\n"
            if e["copies"] > 1:
                tail.append(f"in {num(e['copies'])} configs")
            return f"- **{md(e['name'])}**: {md(how(e))} ({' · '.join(tail)})\n"

        self.write_kind(
            "mcp-servers", "MCP servers",
            f"{len(entries):,} MCP servers: {len(entries) - n_dir:,} that people wire into Claude Code, read from {n_files:,} "
            f"`.mcp.json` files, and {n_dir:,} server repos from the claudemarketplaces.com MCP directory.",
            entries, ["name", "description", "source", "type", "command", "package", "host", "copies", "repo", "url", "stars"],
            row, line,
            ["`source` is `config` for a server found in someone's `.mcp.json`, and `directory` for a server repo listed in "
             "the claudemarketplaces.com MCP directory.",
             "Config entries: one per server name and target (package or host). `copies` is how many configs use it, the "
             "closest thing here to a popularity count. Only the launcher, the package name and the host are kept; "
             "arguments, environment variables, headers and URL paths are dropped because configs often carry keys. "
             "Config files have no description field, so those entries have none.",
             "Directory entries: the description is the repo's own. The same server can appear under both sources."])
        self.stats["mcp-servers"].update(files=n_files, directory=n_dir)

    # ---------- hooks ----------

    def hooks(self):
        entries, n_files = [], 0
        for r in self.con.execute("""select c.repo, c.path, c.kind, t.z, b.description from components c join blobs b on b.sha = c.sha
                                     join blob_text t on t.sha = c.sha where c.kind in ('hook', 'settings') and b.status = 'ok'"""):
            n_files += 1
            try:
                d = json.loads(zlib.decompress(r["z"]).decode("utf-8", "replace"))
            except Exception:
                continue
            hooks = d.get("hooks") if isinstance(d, dict) else None
            if not isinstance(hooks, dict) or not hooks:
                continue
            events, matchers, n_cmd = [], set(), 0
            for ev, arr in hooks.items():
                if not isinstance(arr, list):
                    continue
                events.append(str(ev)[:40])
                for h in arr:
                    if isinstance(h, dict):
                        if isinstance(h.get("matcher"), str) and h["matcher"]:
                            matchers.add(clean(h["matcher"])[:60])
                        n_cmd += len(h.get("hooks") or []) if isinstance(h.get("hooks"), list) else 1
            if not events:
                continue
            parts = r["path"].split("/")
            name = parts[-3] if r["kind"] == "hook" and len(parts) >= 3 and parts[-2] == "hooks" else r["repo"].split("/")[-1]
            entries.append({"name": clean(name)[:120] or r["repo"], "desc": clean(r["description"]), "events": sorted(events),
                            "matchers": sorted(matchers)[:8], "n": n_cmd, "repo": r["repo"], "path": r["path"],
                            "meta": self.meta(r["repo"]), "where": "plugin hooks.json" if r["kind"] == "hook" else "settings.json"})
        seen, uniq = set(), []
        for e in sorted(entries, key=lambda e: (-e["meta"]["stars"], e["meta"]["fork"])):
            key = (e["name"].lower(), tuple(e["events"]), tuple(e["matchers"]), e["n"])
            if key in seen:
                continue
            seen.add(key)
            uniq.append(e)
        uniq.sort(key=lambda e: (e["name"].lower(), -e["meta"]["stars"], e["repo"].lower()))

        def row(e):
            m = e["meta"]
            return [e["name"], clip(e["desc"]), ", ".join(e["events"]), ", ".join(e["matchers"]), e["n"], e["where"],
                    e["repo"], gh_url(e["repo"], e["path"]), m["stars"], m["license"], m["pushed"]]

        def line(e):
            m = e["meta"]
            bits = ", ".join(e["events"]) + (f" on {', '.join(e['matchers'][:4])}" if e["matchers"] else "")
            tail = [f"[{e['repo']}]({gh_url(e['repo'], e['path'])})"] + ([f"★{num(m['stars'])}"] if m["stars"] else [])
            d = md(clip(e["desc"], 300))
            return f"- **{md(e['name'])}**: {md(bits)}" + (f". {d}" if d else "") + f" ({' · '.join(tail)})\n"

        self.write_kind(
            "hooks", "Hooks",
            f"{len(uniq):,} hook setups: which Claude Code events people hook and on which tools, read from {n_files:,} "
            "`hooks.json` and `.claude/settings.json` files.",
            uniq, ["name", "description", "events", "matchers", "handlers", "where", "repo", "url", "stars", "license", "last_pushed"],
            row, line,
            ["`name` is the plugin folder for a plugin's `hooks.json`, or the repo for a `settings.json`.",
             "`events` are the hook events used, `matchers` the tools they fire on, `handlers` how many commands run.",
             "The commands themselves are not copied here; follow the link to read them.",
             "Identical setups under the same name are listed once, at the most-starred repo."])
        self.stats["hooks"].update(files=n_files)

    # ---------- repos ----------

    def repos_csv(self):
        counts = defaultdict(lambda: defaultdict(int))
        for r in self.con.execute("select repo, kind, count(*) n from components group by 1, 2"):
            counts[r["repo"].lower()][r["kind"]] = r["n"]
        listed = defaultdict(int)
        for r in self.con.execute("select marketplace_repo, count(*) n from plugins group by 1"):
            listed[r["marketplace_repo"].lower()] = r["n"]
        holds = ("plugin", "marketplace", "skill", "command", "agent", "hook", "mcp")
        rows = [r for r in self.repos.values() if r["status"] in ("treed", "done")
                and any(counts[r["full_name"].lower()].get(k) for k in holds)]
        rows.sort(key=lambda r: (-(r["stars"] or 0), r["full_name"].lower()))
        with open(OUT / "repos.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["repo", "description", "stars", "forks", "license", "owner_type", "created", "last_pushed", "is_fork",
                        "archived", "topics", "homepage", "plugins_listed", "skills", "commands", "agents", "hook_files",
                        "mcp_configs", "has_marketplace", "has_claude_md"])
            for r in rows:
                c = counts[r["full_name"].lower()]
                try:
                    topics = ", ".join(json.loads(r["topics"] or "[]"))
                except ValueError:
                    topics = ""
                w.writerow([r["full_name"], clip(clean(r["description"]), 400), r["stars"] or 0, r["forks"] or 0, r["license"] or "",
                            r["owner_type"] or "", (r["created_at"] or "")[:10], (r["pushed_at"] or "")[:10],
                            "yes" if r["is_fork"] else "", "yes" if r["archived"] else "", topics, clean(r["homepage"])[:200],
                            listed.get(r["full_name"].lower(), 0), c["skill"], c["command"], c["agent"], c["hook"], c["mcp"],
                            "yes" if c["marketplace"] else "", "yes" if c["claude-md"] else ""])
        by_status = defaultdict(int)
        for r in self.repos.values():
            by_status[r["status"]] += 1
        self.stats["repos"] = {"entries": len(rows), "seen": len(self.repos), "by_status": dict(by_status)}

    # ---------- top + readme ----------

    def top(self, plugins, skills, agents, commands):
        out = ["# Top of the list\n\n", "The most used and most copied entries. [Back to the index](README.md)\n\n"]

        def section(title, note, items, fmt, n=100):
            out.append(f"## {title}\n\n{note}\n\n")
            for i, e in enumerate(items[:n], 1):
                out.append(f"{i}. {fmt(e)}\n")
            out.append("\n")

        def comp(e, extra):
            return f"**{md(e['name'])}** ({extra} · [{e['repo']}]({e['url']})): {md(clip(e['desc'], 200))}"

        section("Skills by installs", "Install counts come from skills.sh, the only public install counter. It counts skills only.",
                sorted([e for e in skills if e["installs"]], key=lambda e: -e["installs"]),
                lambda e: comp(e, f"{num(e['installs'])} installs" + (f", {num(e['wk'])} last week" if e["wk"] else "")))
        section("Skills by copies", "How many copies of the same skill file the crawl found across GitHub.",
                sorted(skills, key=lambda e: -e["copies"]), lambda e: comp(e, f"{num(e['copies'])} copies"))
        seen, tops = set(), []
        for e in sorted(plugins, key=lambda e: (-len(e["markets"]), -e["meta"]["stars"])):
            if e["name"].lower() not in seen:
                seen.add(e["name"].lower()); tops.append(e)
        section("Plugins by marketplaces", "How many marketplaces list the plugin.", tops,
                lambda e: f"**{md(e['name'])}** (in {len(e['markets']):,} marketplaces · [{e['home'] or 'source'}]({e['url']})): {md(clip(e['desc'], 200))}")
        section("Agents by copies", "How many copies of the same agent file the crawl found.",
                sorted(agents, key=lambda e: -e["copies"]), lambda e: comp(e, f"{num(e['copies'])} copies"), 50)
        section("Commands by copies", "How many copies of the same command file the crawl found.",
                sorted(commands, key=lambda e: -e["copies"]), lambda e: comp(e, f"{num(e['copies'])} copies"), 50)
        (OUT / "TOP.md").write_text("".join(out), encoding="utf-8")

    def readme(self):
        s = self.stats
        first, last = self.con.execute("select min(first_seen), max(tree_at) from repos").fetchone()
        crawl = f"{(first or '')[:10]} to {(last or '')[:10]}"
        read = (self.con.execute("select max(fetched_at) from blobs").fetchone()[0] or "")[:10] if self.has_blobs else ""
        queue = dict(self.con.execute("select coalesce(status,'pending'), count(*) from blob_queue group by 1").fetchall()) if self.has_blobs else {}
        rows = [("plugins", "Plugins", "entries of marketplace listings"), ("skills", "Skills", "`SKILL.md` files"),
                ("agents", "Agents", "subagent definitions, `agents/*.md`"), ("commands", "Commands", "slash commands, `commands/*.md`"),
                ("mcp-servers", "MCP servers", "servers named in `.mcp.json` files, plus a directory of server repos"), ("hooks", "Hooks", "hook setups in `hooks.json` and `settings.json`")]
        out = ["# The list\n\n",
               "Everything people have built for Claude Code and published on GitHub, with what each thing does and where it lives. "
               "Plugins, skills, agents, commands, MCP servers and hooks. Skills and agents written for other coding agents "
               "in the same file formats are here too.\n\n",
               "| | Entries | What it is |\n|---|---:|---|\n"]
        for key, title, what in rows:
            if key in s:
                out.append(f"| [{title}]({key}/) | {s[key]['entries']:,} | {what} |\n")
        out.append(f"| [Repos](repos.csv) | {s['repos']['entries']:,} | every repo that holds any of the above |\n\n")
        out += ["Start with [TOP.md](TOP.md) for the most installed and most copied.\n\n",
                "## How to use it\n\n",
                "- **Read it:** each folder has alphabetical pages that GitHub can show, indexed in the folder's README.\n",
                "- **Take it:** each folder has the same list as CSV. Big lists are split into numbered parts.\n",
                "- **Point an agent at it:** the CSVs are plain files at stable URLs, "
                "`https://raw.githubusercontent.com/pauljump/the-list/main/<folder>/<file>.csv`.\n\n",
                "## How it was made\n\n",
                f"1. **Find the repos** ({crawl}; most were found in September 2026). Anthropic's official, community and knowledge-work marketplaces; "
                "GitHub repo search on fifteen topics; GitHub code search for `marketplace.json`, `plugin.json`, `hooks.json` and "
                "hook settings; the claudemarketplaces.com sitemaps; ten awesome-lists; and every marketplace found inside "
                f"any repo, followed in turn. {s['repos']['seen']:,} repos seen.\n",
                "2. **List their files.** One file listing per repo, keeping the paths that are Claude Code components.\n",
                f"3. **Read the files** ({read}). Each distinct file once, by its git hash, so the text matches the listing. "
                "Names and descriptions come from each file's own frontmatter.\n",
                "4. **Fold the copies.** Most of GitHub's skills are copies of other skills. Identical entries are shown once, "
                "at the original, with a count of how many repos carry them.\n\n",
                "No model wrote or judged anything here. Every description is the author's own, cut at 600 characters. "
                "Install counts are from skills.sh.\n\n",
                "## What it is not\n\n",
                "- Not reviewed. Nothing here was run or checked, and being listed is not a recommendation. "
                "Plugins and hooks run code on your machine; read them first.\n",
                "- Not live. It is a snapshot, and some repos have since moved or gone.\n",
                "- Not everything. Private repos, and public ones the searches missed, are not here.\n",
                "- Email addresses and anything that looked like a key were removed from descriptions.\n\n",
                "## Numbers\n\n"]
        for key, title, _ in rows:
            if key in s and "files" in s[key]:
                st = s[key]
                bit = f"- **{title}:** {st['files']:,} files found"
                if "unique" in st:
                    bit += f", {st['unique']:,} distinct, {st['read']:,} read"
                out.append(bit + f", {st['entries']:,} entries after folding copies.\n")
        st = s["plugins"]
        out.append(f"- **Plugins:** {st['rows']:,} marketplace entries, {st['entries']:,} after folding copies, {st['described']:,} with a description.\n")
        bs = s["repos"]["by_status"]
        out.append(f"- **Repos:** {s['repos']['seen']:,} seen, {bs.get('treed', 0) + bs.get('done', 0):,} opened, "
                   f"{bs.get('gone', 0):,} already gone, {bs.get('resolved', 0) + bs.get('new', 0):,} MCP server repos "
                   "kept for their description only.\n")
        if queue.get("pending"):
            out.append(f"- **In progress:** {queue['pending']:,} files are still being read; this list will grow.\n")
        out.append("\nThe scripts that read the files and build these pages are in `crawl/` and `build.py`. "
                   "The crawl database itself is several gigabytes and is not in this repo.\n")
        (OUT / "README.md").write_text("".join(out), encoding="utf-8")
        (OUT / "stats.json").write_text(json.dumps({"crawl": crawl, "read": read, "queue": queue, **s}, indent=1), encoding="utf-8")


def main(db_path):
    b = Build(db_path)
    for old in ("the-list.csv", "the-list.md", "list"):   # the first layout
        p = OUT / old
        if p.is_dir():
            shutil.rmtree(p)
        elif p.exists():
            p.unlink()
    plugins = b.plugins()
    print("plugins", b.stats["plugins"]["entries"], flush=True)
    skills = b.components(
        "skill", "skills", "Skills", "{n:,} skills: every distinct `SKILL.md` the crawl could read, with what it does.",
        ["allowed_tools", "skill_license"], ["allowed_tools", "license"],
        ["`installs` and `installs_last_week` are from skills.sh, which counts installs made with `npx skills`. Blank means not listed there."])
    print("skills", b.stats["skills"]["entries"], flush=True)
    agents = b.components(
        "agent", "agents", "Agents", "{n:,} subagents: every distinct `agents/*.md` the crawl could read, with what it is for.",
        ["tools", "model"], ["tools", "model"],
        ["Any Markdown file in an `agents/` folder counts, so agents written for Copilot, Codex and others are included."])
    print("agents", b.stats["agents"]["entries"], flush=True)
    commands = b.components(
        "command", "commands", "Commands", "{n:,} slash commands: every distinct `commands/*.md` the crawl could read.",
        ["argument_hint", "allowed_tools", "model"], ["argument_hint", "allowed_tools", "model"],
        ["`name` is the file name, which is what you type after the slash."])
    print("commands", b.stats["commands"]["entries"], flush=True)
    b.mcp()
    b.hooks()
    b.repos_csv()
    b.top(plugins, skills, agents, commands)
    b.readme()
    print(json.dumps({k: v.get("entries") for k, v in b.stats.items()}))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
