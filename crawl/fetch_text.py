#!/usr/bin/env python3
"""Download the text of every component file the crawl found, once per unique content.

    python3 crawl/fetch_text.py /path/to/signal.db prepare     # build the work queue (once)
    python3 crawl/fetch_text.py /path/to/signal.db enqueue     # add files found by a later tree pass
    python3 crawl/fetch_text.py /path/to/signal.db run [--max-seconds N] [--follow]
    python3 crawl/fetch_text.py /path/to/signal.db status

Read-only against GitHub: `gh api graphql` only, so the token stays inside gh. No model calls.
Resumable: every call commits, and `run` picks up where the last one stopped.

The crawl's `components` table has one row per file per repo. Most files are copies (forks, vendored
skill packs), so the work is done per git blob sha: each unique content is fetched once, from the
most-starred live repo that holds it. The parsed frontmatter (name, description) goes in `blobs`, the
text itself zlib-compressed in `blob_text`, kept apart so that reading the metadata stays fast.
"""
import calendar
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
import zlib
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

KINDS = ("skill", "agent", "command", "plugin", "marketplace", "hook", "settings", "mcp", "lsp", "readme",
         "claude-md", "package")
MAX_BLOB_BYTES = 200_000
MAX_ATTEMPTS = 3            # distinct repos tried for one sha before it is recorded as missing
CALL_BLOBS = 100            # blobs per GraphQL call, adapted down when GitHub cannot serve a call
CALL_BYTES = 1_500_000
CALL_REPOS = 30
MIN_GAP = 0.6               # seconds between calls


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


class Fetcher:
    def __init__(self, db_path):
        self.dir = Path(db_path).resolve().parent
        self.log_path = self.dir / "logs" / "fetch_text.log"
        self.log_path.parent.mkdir(exist_ok=True)
        self.con = sqlite3.connect(db_path, timeout=120)
        self.con.row_factory = sqlite3.Row
        self.con.execute("pragma busy_timeout=120000")
        self.con.execute("pragma synchronous=normal")
        self.call_blobs = CALL_BLOBS

    def log(self, msg):
        line = f"{now()} {msg}"
        print(line, flush=True)
        with open(self.log_path, "a") as f:
            f.write(line + "\n")

    # ---------- queue ----------

    def prepare(self):
        c = self.con
        c.executescript("""
            create table if not exists blobs(
                sha text primary key, kind text, size int, status text, truncated int,
                name text, description text, lead text, fm text, repo text, path text, fetched_at text);
            create table if not exists blob_text(sha text primary key, z blob);
            create index if not exists components_sha on components(sha);
        """)
        if c.execute("select 1 from sqlite_master where name='blob_queue'").fetchone():
            self.log("prepare: queue exists")
            return
        self.log("prepare: seeding from text already downloaded")
        for r in c.execute("select sha, kind, size, path, repo, text from components where text is not null and text!='' group by sha").fetchall():
            self.store(r["sha"], r["kind"], r["size"], r["repo"], r["path"], r["text"], False)
        c.commit()
        self.log("prepare: building queue (one source repo per unique sha)")
        marks = ",".join("?" * len(KINDS))
        c.execute(f"""
            create table blob_queue as
            select sha, repo, path, size, kind, stars, 0 as attempts, '' as tried, null as status from (
                select c.sha, c.repo, c.path, c.size, c.kind, coalesce(r.stars, 0) stars,
                       row_number() over (partition by c.sha order by (coalesce(r.status,'')='gone'),
                                          coalesce(r.is_fork, 0), coalesce(r.stars, 0) desc, c.repo) rn
                from components c left join repos r on r.full_name = c.repo
                where c.sha is not null and coalesce(c.size, 0) <= ? and c.kind in ({marks})
            ) where rn = 1 and sha not in (select sha from blobs)""", (MAX_BLOB_BYTES, *KINDS))
        c.execute("create unique index blob_queue_sha on blob_queue(sha)")
        c.execute("create index blob_queue_next on blob_queue(status, stars desc, repo)")
        c.commit()
        self.log(f"prepare: {c.execute('select count(*) from blob_queue').fetchone()[0]:,} blobs queued")

    def enqueue(self):
        """Queue the shas of components added since `prepare` (a later tree pass found more repos)."""
        c = self.con
        marks = ",".join("?" * len(KINDS))
        before = c.execute("select count(*) from blob_queue").fetchone()[0]
        c.execute(f"""
            insert or ignore into blob_queue(sha, repo, path, size, kind, stars, attempts, tried, status)
            select sha, repo, path, size, kind, stars, 0, '', null from (
                select c.sha, c.repo, c.path, c.size, c.kind, coalesce(r.stars, 0) stars,
                       row_number() over (partition by c.sha order by coalesce(r.is_fork, 0), coalesce(r.stars, 0) desc, c.repo) rn
                from components c left join repos r on r.full_name = c.repo
                where c.sha is not null and coalesce(c.size, 0) <= ? and c.kind in ({marks})
                  and c.sha not in (select sha from blob_queue) and c.sha not in (select sha from blobs)
            ) where rn = 1""", (MAX_BLOB_BYTES, *KINDS))
        c.commit()
        self.log(f"enqueue: {c.execute('select count(*) from blob_queue').fetchone()[0] - before:,} new blobs queued")

    # ---------- parsing ----------

    FM_RE = re.compile(r"\A﻿?\s*---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.S)

    @staticmethod
    def one_line(v, cap):
        if v is None:
            return None
        if isinstance(v, (list, tuple)):
            v = ", ".join(str(x) for x in v)
        elif isinstance(v, dict):
            v = json.dumps(v, ensure_ascii=False)
        v = re.sub(r"\s+", " ", str(v)).strip()
        return v[:cap] or None

    def parse(self, kind, path, text):
        """name, description, lead (first prose of the body), frontmatter as JSON. Deterministic."""
        name = desc = lead = fm_json = None
        if path.lower().endswith(".json"):
            try:
                d = json.loads(text)
            except ValueError:
                d = None
            if isinstance(d, dict):
                name, desc = self.one_line(d.get("name"), 200), self.one_line(d.get("description"), 2000)
            return name, desc, None, None
        body = text
        m = self.FM_RE.match(text)
        if m:
            body = text[m.end():]
            fm = None
            if yaml:
                try:
                    fm = yaml.safe_load(m.group(1))
                except Exception:
                    fm = None
            if not isinstance(fm, dict):   # loose fallback: top-level `key: value` lines
                fm = {}
                for ln in m.group(1).splitlines():
                    k = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", ln)
                    if k:
                        fm[k.group(1)] = k.group(2).strip().strip("\"'")
            name, desc = self.one_line(fm.get("name"), 200), self.one_line(fm.get("description"), 2000)
            try:
                fm_json = json.dumps({str(k): self.one_line(v, 600) for k, v in fm.items()}, ensure_ascii=False)[:6000]
            except Exception:
                fm_json = None
        for para in re.split(r"\n\s*\n", body[:6000]):
            p = para.strip()
            if not p or p.startswith(("#", "<", "!", "[!", "```", "---", "|", "=")):
                continue
            lead = self.one_line(p, 400)
            break
        return name, desc, lead, fm_json

    def store(self, sha, kind, size, repo, path, text, truncated):
        # GitHub's JSON can carry unpaired surrogates, which sqlite refuses; pair them or drop them
        text = text.encode("utf-16", "surrogatepass").decode("utf-16", "replace")
        name, desc, lead, fm = (v if v is None else v.encode("utf-8", "replace").decode("utf-8")
                                for v in self.parse(kind, path, text))   # YAML escapes can make surrogates too
        self.con.execute(
            "insert or replace into blobs(sha, kind, size, status, truncated, name, description, lead, fm, repo, path, fetched_at) "
            "values(?,?,?,?,?,?,?,?,?,?,?,?)",
            (sha, kind, size, "ok", int(bool(truncated)), name, desc, lead, fm, repo, path, now()))
        self.con.execute("insert or replace into blob_text(sha, z) values(?,?)",
                         (sha, zlib.compress(text.encode("utf-8", "replace"), 6)))

    # ---------- GitHub ----------

    def graphql(self, query):
        """One call. Returns (data, problem); problem is None, 'rate', 'heavy' or 'error'."""
        tmp = self.dir / f"_gql.{os.getpid()}.json"
        tmp.write_text(json.dumps({"query": query}))
        try:
            p = subprocess.run(["gh", "api", "graphql", "--input", str(tmp)], capture_output=True, text=True, timeout=150)
        except subprocess.TimeoutExpired:
            return None, "heavy"
        out = None
        if p.stdout.strip():
            try:
                out = json.loads(p.stdout)
            except ValueError:
                out = None
        if isinstance(out, dict) and out.get("data") is not None:   # partial data + errors (a missing repo) is normal
            return out["data"], None
        err = ((p.stderr or "") + (p.stdout or ""))[:600]
        low = err.lower()
        if "rate limit" in low or "abuse" in low or "http 403" in low or "http 429" in low:
            self.rate_msg = err.strip()[:160]
            return None, "rate"
        if "http 5" in low or "timeout" in low or "timed out" in low or "connection" in low or "eof" in low:
            return None, "heavy"
        self.log(f"graphql error: {err.strip()[:300]}")
        return None, "error"

    def alternate(self, row):
        """Another repo holding the same content, for a sha whose first source is gone."""
        tried = [t for t in (row["tried"] or "").split("\n") if t] + [row["repo"]]
        if row["attempts"] + 1 >= MAX_ATTEMPTS:
            return None, tried
        marks = ",".join("?" * len(tried))
        alt = self.con.execute(
            f"""select c.repo, c.path from components c left join repos r on r.full_name = c.repo
                where c.sha = ? and c.repo not in ({marks})
                order by (coalesce(r.status,'')='gone'), coalesce(r.stars, 0) desc limit 1""", (row["sha"], *tried)).fetchone()
        return alt, tried

    def run(self, max_seconds=None, follow=False):
        c = self.con
        start, last_call, n_ok, n_miss, calls, rate_waits, last_log = time.time(), 0.0, 0, 0, 0, 0, time.time()
        self.log(f"run: {c.execute('select count(*) from blob_queue where status is null').fetchone()[0]:,} pending")
        while True:
            if max_seconds and time.time() - start > max_seconds:
                self.log("run: time limit reached; stopping cleanly")
                break
            rows = c.execute("select * from blob_queue where status is null order by stars desc, repo limit 3000").fetchall()
            if not rows:
                if not follow:
                    self.log("run: queue empty")
                    break
                time.sleep(300)  # a tree pass is still opening repos: let files pile up, then take them
                self.enqueue()
                continue
            i = 0
            while i < len(rows):
                if max_seconds and time.time() - start > max_seconds:
                    break
                group, size, repos = [], 0, set()
                while i < len(rows) and len(group) < self.call_blobs:
                    r = rows[i]
                    if group and (size + (r["size"] or 0) > CALL_BYTES or (r["repo"] not in repos and len(repos) >= CALL_REPOS)):
                        break
                    group.append(r); size += r["size"] or 0; repos.add(r["repo"]); i += 1
                by_repo = {}
                for r in group:
                    by_repo.setdefault(r["repo"], []).append(r)
                parts = []
                for k, (repo, rs) in enumerate(by_repo.items()):
                    owner, _, name = repo.partition("/")
                    blobs = " ".join(f'b{r["sha"]}: object(oid: "{r["sha"]}") {{ ... on Blob {{ text isTruncated isBinary }} }}' for r in rs)
                    parts.append(f"r{k}: repository(owner: {json.dumps(owner)}, name: {json.dumps(name)}) {{ {blobs} }}")
                wait = MIN_GAP - (time.time() - last_call)
                if wait > 0:
                    time.sleep(wait)
                data, problem = self.graphql("query { rateLimit { remaining cost resetAt } " + " ".join(parts) + " }")
                last_call = time.time(); calls += 1
                if problem == "rate":
                    rate_waits += 1
                    pause = min(90 * rate_waits, 900)
                    self.log(f"rate limited ({self.rate_msg}); sleeping {pause}s")
                    time.sleep(pause)
                    i -= len(group)
                    continue
                if problem == "heavy":
                    if len(group) == 1:   # one blob GitHub cannot serve: set it aside
                        c.execute("update blob_queue set status='error' where sha=?", (group[0]["sha"],)); c.commit()
                        continue
                    self.call_blobs = max(5, self.call_blobs // 2)
                    self.log(f"call too heavy; blobs per call now {self.call_blobs}")
                    time.sleep(5)
                    i -= len(group)
                    continue
                if problem == "error":
                    for r in group:
                        c.execute("update blob_queue set status='error' where sha=?", (r["sha"],))
                    c.commit()
                    continue
                rate_waits = 0
                for k, (repo, rs) in enumerate(by_repo.items()):
                    rd = data.get(f"r{k}") or {}
                    for r in rs:
                        b = rd.get(f"b{r['sha']}")
                        if b and b.get("text") is not None:
                            try:
                                self.store(r["sha"], r["kind"], r["size"], repo, r["path"], b["text"], b.get("isTruncated"))
                            except Exception as ex:   # one unreadable file must not stop the run
                                self.log(f"store failed {r['sha']} {repo}/{r['path']}: {ex!r}"[:300])
                                c.execute("update blob_queue set status='error' where sha=?", (r["sha"],))
                                continue
                            c.execute("update blob_queue set status='ok' where sha=?", (r["sha"],))
                            n_ok += 1
                        elif b and b.get("isBinary"):
                            c.execute("update blob_queue set status='binary' where sha=?", (r["sha"],))
                        else:
                            alt, tried = self.alternate(r)
                            if alt:
                                c.execute("update blob_queue set repo=?, path=?, attempts=attempts+1, tried=? where sha=?",
                                          (alt["repo"], alt["path"], "\n".join(tried), r["sha"]))
                            else:
                                c.execute("update blob_queue set status='missing', attempts=attempts+1 where sha=?", (r["sha"],))
                                n_miss += 1
                c.commit()
                if self.call_blobs < CALL_BLOBS and calls % 50 == 0:
                    self.call_blobs = min(CALL_BLOBS, self.call_blobs + 10)
                rl = data.get("rateLimit") or {}
                if time.time() - last_log > 300:
                    last_log = time.time()
                    left = c.execute("select count(*) from blob_queue where status is null").fetchone()[0]
                    rate = n_ok / max(1, time.time() - start) * 3600
                    self.log(f"ok {n_ok:,} missing {n_miss:,} calls {calls:,} · {rate:,.0f}/h · pending {left:,} · "
                             f"graphql remaining {rl.get('remaining')} (cost {rl.get('cost')})")
                if (rl.get("remaining") or 999) < 60:
                    self.log(f"graphql budget nearly spent; sleeping until {rl.get('resetAt')}")
                    reset = calendar.timegm(time.strptime(rl["resetAt"], "%Y-%m-%dT%H:%M:%SZ"))
                    time.sleep(max(60, min(3700, reset - time.time() + 5)))
        self.log(f"run end: ok {n_ok:,} missing {n_miss:,} calls {calls:,} in {(time.time() - start) / 60:.0f} min")

    def status(self):
        c = self.con
        print("queue:", dict(c.execute("select coalesce(status,'pending'), count(*) from blob_queue group by 1").fetchall()))
        for r in c.execute("select kind, count(*) n, sum(description is not null) d from blobs group by 1 order by 2 desc"):
            print(f"  {r['kind']:<12} {r['n']:>9,} texts · {r['d'] or 0:>9,} with description")


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[2] not in ("prepare", "enqueue", "run", "status"):
        sys.exit(__doc__)
    f = Fetcher(sys.argv[1])
    if sys.argv[2] == "prepare":
        f.prepare()
    elif sys.argv[2] == "enqueue":
        f.enqueue()
    elif sys.argv[2] == "status":
        f.status()
    else:
        secs = int(sys.argv[sys.argv.index("--max-seconds") + 1]) if "--max-seconds" in sys.argv else None
        f.run(secs, follow="--follow" in sys.argv)
