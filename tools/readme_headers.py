#!/usr/bin/env python3
"""
Extract the per-file `ncdump -h` / gdalinfo blocks that rasterwise's README.Rmd
rendered into README.md, across *every* README.md version in git history.

These are metadata fingerprints of extdata files -- including ones whose bytes
are now lost -- usable to (a) confirm a candidate found on another machine is
the same file, and (b) seed metadata-only store cards.

usage: readme_headers.py GITDIR fingerprints
writes OUTDIR/<extdata path>.cdl  (latest version seen) and OUTDIR/index.tsv
"""
import os
import re
import subprocess
import sys

RULE = re.compile(r"^#{20,}\s*$")


def git(repo, *a):
    return subprocess.run(["git", "-C", repo] + list(a), stdout=subprocess.PIPE,
                          check=True).stdout.decode("utf-8", "replace")


def blocks(text):
    lines = text.replace("\r", "").split("\n")
    i = 0
    while i < len(lines):
        if RULE.match(lines[i].strip()):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j >= len(lines):
                break
            path = lines[j].strip().strip("#").strip()
            k = j + 1
            while k < len(lines) and not RULE.match(lines[k].strip()) \
                    and not (lines[k] and not lines[k].startswith((" ", "\t"))):
                k += 1
            body = "\n".join(l.strip() for l in lines[j + 1:k] if l.strip())
            if path and " " not in path:
                yield path, body
            i = k
        else:
            i += 1


def main(repo, out):
    os.makedirs(out, exist_ok=True)
    commits = git(repo, "log", "--all", "--reverse", "--format=%H %ad", "--date=short",
                  "--", "README.md").split("\n")
    latest, first = {}, {}
    for c in filter(None, commits):
        sha, date = c.split()
        try:
            txt = git(repo, "show", sha + ":README.md")
        except subprocess.CalledProcessError:
            continue
        for path, body in blocks(txt):
            if len(body) < 20 or ("running command" in body and "ncdump -h" in body):
                continue  # scripts/readmes: ncdump failed, not a header
            latest[path] = (date, sha[:12], body)
            first.setdefault(path, date)
    with open(os.path.join(out, "index.tsv"), "w") as idx:
        idx.write("path\tfirst_seen\tlast_seen\tcommit\tlines\n")
        for path in sorted(latest, key=str.lower):
            date, sha, body = latest[path]
            dest = os.path.join(out, path + ".cdl")
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "w") as f:
                f.write(body + "\n")
            idx.write("%s\t%s\t%s\t%s\t%d\n" % (path, first[path], date, sha, body.count("\n") + 1))
    print("%d file headers recovered from %d README versions" % (len(latest), len(list(filter(None, commits)))))


if __name__ == "__main__":
    main(*sys.argv[1:3])
