#!/usr/bin/env python3
"""Reopen code-search ranges that are marked done without a whole result behind them.

    python3 crawl/reopen_gaps.py /path/to/signal.db [--dry-run]

A range counts as searched only if some search over it returned at least 90% of what GitHub could give (1,000 a search).
Ranges GitHub reported as empty have no search on record, so a few are re-counted each time; that costs one call each.
"""
import json
import re
import sqlite3
import sys

con = sqlite3.connect(sys.argv[1], timeout=600)
pat = re.compile(r"(.+) size:(\d+)\.\.(\d+)$")
whole = {}
for q, t, g in con.execute("select query, total, got from searches where engine='code' and ran_at >= '2026-11-19T04'"):
    m = pat.match(q)
    if m and g >= 0.9 * min(t or 0, 1000):
        whole.setdefault(m[1], set()).add((int(m[2]), int(m[3])))
for k, v in con.execute("select k, v from kv where k like 'slices:code:%'").fetchall():
    q = k[len("slices:code:"):].rsplit(":", 1)[0]
    keep, gaps = [], []
    for a, b in json.loads(v):
        pos = a
        for x, y in sorted(whole.get(q, ())):
            if y < pos or x > b:
                continue
            if x > pos:
                gaps.append((pos, x - 1))
            keep.append([max(x, pos), min(y, b)])
            pos = max(pos, y + 1)
        if pos <= b:
            gaps.append((pos, b))
    merged = []
    for a, b in sorted(keep):
        if merged and a <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])
    if gaps:
        print(q, "| reopened", gaps[:8])
        if "--dry-run" not in sys.argv:
            con.execute("update kv set v=? where k=?", (json.dumps(merged), k))
con.commit()
