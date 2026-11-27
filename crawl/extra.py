#!/usr/bin/env python3
"""Second-pass helpers for the crawl (November 2026).

    python3 crawl/extra.py <data dir> add-skillssh   # repos named on skills.sh that the crawl never saw
    python3 crawl/extra.py <data dir> mark-pushed    # known repos pushed since their last listing go back in the queue
    python3 crawl/extra.py <data dir> probe          # repos found only by tag search: skip those with no Claude Code files near the top
    python3 crawl/extra.py <data dir> unskip         # a skipped repo that a file search later found goes back in the queue
    python3 crawl/extra.py <data dir> untruncate     # re-list repos whose file listing GitHub cut short

`<data dir>` holds signal.db and signal/ingest.py. Read-only against GitHub; no model calls.
"""
import importlib.util
import json
import sys
import time
from pathlib import Path

# Paths whose presence at the root of a repo means it may hold plugins, skills, agents, commands, hooks or MCP config.
PROBE_PATHS = [".claude-plugin", ".claude", "skills", "plugins", "agents", "commands", "hooks", ".mcp.json", "SKILL.md",
               ".agents", ".github/agents", ".github/skills"]
REST_RESERVE = 1200   # REST calls per hour left for everything else on the account
MAX_CALLS_PER_REPO = 400


def load(data_dir):
    spec = importlib.util.spec_from_file_location("ingest", Path(data_dir) / "signal" / "ingest.py")
    ing = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ing)
    return ing, ing.db()


def add_skillssh(ing, con):
    n = 0
    for r in con.execute("select distinct coalesce(nullif(source_repo,''), owner||'/'||repo) fn from skill_installs").fetchall():
        if ing.add_repo(con, r["fn"], "dir:skills.sh"):
            n += 1
    con.commit()
    ing.log(f"add-skillssh: {n} new repos")


def mark_pushed(ing, con):
    cur = con.execute("update repos set status='resolved' where status in ('treed','done','empty') and pushed_at > tree_at")
    con.commit()
    ing.log(f"mark-pushed: {cur.rowcount} repos pushed since their last listing go back in the queue")


def search_only(via):
    """Found only by a topic or broad search: a tag says nothing about what the repo holds."""
    vias = json.loads(via or "[]")
    return bool(vias) and all(v.startswith(("broad:", "search:")) for v in vias)


ROOT_NAMES = {p for p in PROBE_PATHS if "/" not in p} | {"CLAUDE.md"}
CHILD_NAMES = {"SKILL.md", ".claude-plugin", "agents", "commands", "skills", "hooks", ".mcp.json"}
TREE2 = "object(expression: \"HEAD:\") { ... on Tree { entries { name type object { ... on Tree { entries { name } } } } } }"


def looks_like_claude(entries):
    """Root and one level down: a Claude Code folder or file anywhere there means the repo gets a full listing."""
    for e in entries or []:
        if e["name"] in ROOT_NAMES:
            return True
        if e["type"] == "tree":
            kids = ((e.get("object") or {}).get("entries")) or []
            if any(k["name"] in CHILD_NAMES for k in kids):
                return True
    paths = {"/".join(p.split("/")[:2]) for p in PROBE_PATHS if "/" in p}
    for e in entries or []:
        for k in ((e.get("object") or {}).get("entries")) or []:
            if f"{e['name']}/{k['name']}" in paths:
                return True
    return False


def probe(ing, con, batch=10):
    """Repos found only by topic or broad search get a cheap two-level look before a full listing."""
    # topic-tag finds hold Claude Code files ~97% of the time (sampled 2026-11-19), so only the broad tier is probed
    con.execute("create table if not exists probe_kept(full_name text primary key)")   # resolve clears repos.error
    rows = [r["full_name"] for r in con.execute("select full_name, discovered_via from repos where status in ('new','resolved') "
                                                "and full_name not in (select full_name from probe_kept)")
            if search_only(r["discovered_via"]) and all(v.startswith("broad:") for v in json.loads(r["discovered_via"]))]
    ing.log(f"probe: {len(rows)} broad-tier repos")
    kept = skipped = 0
    for i in range(0, len(rows), batch):
        chunk = rows[i:i + batch]
        parts = []
        for fn in chunk:
            o, n = fn.split("/", 1)
            parts.append(f"{ing.repo_alias(fn)}: repository(owner: {json.dumps(o)}, name: {json.dumps(n)}) {{ {TREE2} }}")
        data = ing.graphql("query { rateLimit { remaining } " + " ".join(parts) + " }")
        if data is None:
            if batch > 1:   # one heavy or broken repo: try this chunk one by one
                for fn in chunk:
                    o, n = fn.split("/", 1)
                    d1 = ing.graphql(f"query {{ {ing.repo_alias(fn)}: repository(owner: {json.dumps(o)}, name: {json.dumps(n)}) {{ {TREE2} }} }}")
                    if d1 is None:
                        continue
                    data = data or {}
                    data[ing.repo_alias(fn)] = d1.get(ing.repo_alias(fn))
            if data is None:
                continue
        for fn in chunk:
            d = data.get(ing.repo_alias(fn))
            if d is None:   # gone, or the org refuses the token: leave it to resolve
                continue
            obj = d.get("object")
            if obj is None:   # empty repo
                con.execute("update repos set status='skipped', error='probe: empty repo' where full_name=?", (fn,))
                skipped += 1
            elif looks_like_claude(obj.get("entries")):
                con.execute("insert or ignore into probe_kept values(?)", (fn,))
                kept += 1
            else:
                con.execute("update repos set status='skipped', error='probe: no Claude Code files in the top two levels' "
                            "where full_name=?", (fn,))
                skipped += 1
        con.commit()
        if (i // batch) % 100 == 0:
            ing.log(f"probe {i + len(chunk)}/{len(rows)} kept {kept} skipped {skipped} "
                    f"(graphql remaining {(data.get('rateLimit') or {}).get('remaining')})")
        if ((data.get("rateLimit") or {}).get("remaining") or 999) < 300:
            ing.log("probe: graphql budget low; sleeping 10 min")
            time.sleep(600)
    ing.log(f"probe end: kept {kept}, skipped {skipped}")


def unskip(ing, con):
    rows = [r["full_name"] for r in con.execute("select full_name, discovered_via from repos where status='skipped'")
            if not search_only(r["discovered_via"])]
    for fn in rows:
        con.execute("update repos set status='resolved', error=null where full_name=?", (fn,))
    con.commit()
    ing.log(f"unskip: {len(rows)} skipped repos were found another way and go back in the queue")


def rest_budget(ing):
    rl = ing.gh(["rate_limit"]) or {}
    core = (rl.get("resources") or {}).get("core") or {}
    if (core.get("remaining") or 9999) < REST_RESERVE:
        wait = max(30, int(core.get("reset", 0)) - int(time.time()) + 5)
        ing.log(f"untruncate: REST budget at reserve; sleeping {wait}s")
        time.sleep(wait)


def untruncate(ing, con):
    """GitHub cuts a recursive listing at 100,000 entries or 7 MB. Walk the tree a level at a time instead."""
    con.execute("create table if not exists untruncate_gave_up(full_name text primary key)")
    rows = con.execute("select full_name, default_branch from repos where tree_truncated=1 and status in ('treed','done') "
                       "and full_name not in (select full_name from untruncate_gave_up) order by coalesce(disk_kb, 0)").fetchall()
    ing.log(f"untruncate: {len(rows)} repos")
    for k, r in enumerate(rows):
        fn, branch = r["full_name"], r["default_branch"] or "HEAD"
        if k % 20 == 0:
            rest_budget(ing)
        # most were cut by the depth-limited GraphQL listing, not by GitHub: one full listing settles those
        whole = ing.gh(["-X", "GET", f"repos/{fn}/git/trees/{branch}", "-F", "recursive=1"], ok404=True)
        if whole and "tree" in whole and not whole.get("truncated"):
            ing.record_tree(con, fn, branch, [(e["path"], e["type"], e.get("sha"), e.get("size")) for e in whole["tree"]],
                            whole.get("sha"), False)
            if k % 100 == 0:
                ing.log(f"untruncate {k + 1}/{len(rows)} {fn}: one listing was enough")
            time.sleep(0.5)
            continue
        rest_budget(ing)
        root = ing.gh(["-X", "GET", f"repos/{fn}/git/trees/{branch}"], ok404=True)
        if not root or "tree" not in root:
            continue
        entries, calls, complete = [], 1, True
        todo = [("", e) for e in root["tree"]]
        while todo:
            prefix, e = todo.pop()
            path = prefix + e["path"]
            if e["type"] != "tree":
                entries.append((path, e["type"], e.get("sha"), e.get("size")))
                continue
            entries.append((path, "tree", e.get("sha"), None))
            if calls >= MAX_CALLS_PER_REPO:
                complete = False
                break
            sub = ing.gh(["-X", "GET", f"repos/{fn}/git/trees/{e['sha']}", "-F", "recursive=1"], ok404=True)
            calls += 1
            if not sub or "tree" not in sub:
                complete = False
                continue
            if sub.get("truncated"):   # still too big: list this level only and walk its subtrees
                lvl = ing.gh(["-X", "GET", f"repos/{fn}/git/trees/{e['sha']}"], ok404=True)
                calls += 1
                if not lvl or "tree" not in lvl:
                    complete = False
                    continue
                todo += [(path + "/", x) for x in lvl["tree"]]
            else:
                entries += [(path + "/" + x["path"], x["type"], x.get("sha"), x.get("size")) for x in sub["tree"]]
            if calls % 100 == 0:
                rest_budget(ing)
        if complete:
            n_entries, n_comps = ing.record_tree(con, fn, branch, entries, root.get("sha"), False)
            ing.log(f"untruncate {k + 1}/{len(rows)} {fn}: {n_entries} entries, {n_comps} components, {calls} calls")
        else:
            con.execute("insert or ignore into untruncate_gave_up values(?)", (fn,))
            con.commit()
            ing.log(f"untruncate {k + 1}/{len(rows)} {fn}: gave up after {calls} calls; kept the cut listing")


if __name__ == "__main__":
    cmds = {"add-skillssh": add_skillssh, "mark-pushed": mark_pushed, "probe": probe, "unskip": unskip, "untruncate": untruncate}
    if len(sys.argv) != 3 or sys.argv[2] not in cmds:
        sys.exit(__doc__)
    ing, con = load(sys.argv[1])
    cmds[sys.argv[2]](ing, con)
