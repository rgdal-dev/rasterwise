#!/usr/bin/env python3
"""
Extract the per-file `ncdump -h` / gdalinfo blocks that rasterwise's README.Rmd
rendered into README.md, across *every* README.md version in git history.

These are metadata fingerprints of extdata files -- including ones whose bytes
are now lost -- usable to (a) confirm a candidate found on another machine is
the same file, and (b) seed metadata-only store cards.

usage: readme_headers.py GITDIR fingerprints
         writes fingerprints/<extdata path>.cdl (latest version seen) + index.tsv
       readme_headers.py compare FILE fingerprints/<path>.cdl
         runs `ncdump -h FILE` and reports whether it matches the fingerprint

Fingerprints are normalised so they compare reliably and stay ASCII: leading
whitespace stripped, blank lines and the `netcdf <name> {` line dropped, and
every non-ASCII character written as \\uXXXX (\\xNN for undecodable bytes).
"""
import os
import re
import subprocess
import sys

RULE = re.compile(r"^#{20,}\s*$")


def git(repo, *a):
    return subprocess.run(["git", "-C", repo] + list(a), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                          check=True).stdout.decode("utf-8", "backslashreplace")


def normalise(text):
    out = []
    for l in text.replace("\r", "").split("\n"):
        l = l.strip()
        if not l or l.startswith("netcdf "):
            continue
        out.append("".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in l))
    return "\n".join(out) + "\n"


def compare(path, fp):
    got = subprocess.run(["ncdump", "-h", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if got.returncode:
        print("ncdump failed on %s: %s" % (path, got.stderr.decode("utf-8", "replace").strip()))
        return 2
    a = normalise(got.stdout.decode("utf-8", "backslashreplace"))
    b = open(fp, encoding="ascii").read()
    if a == b:
        print("MATCH  %s == %s" % (path, fp))
        return 0
    import difflib
    print("DIFFER %s vs %s" % (path, fp))
    sys.stdout.writelines(list(difflib.unified_diff(b.splitlines(True), a.splitlines(True),
                                                    "fingerprint", "file", n=1))[:40])
    return 1


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
            body = normalise("\n".join(lines[j + 1:k])).rstrip("\n")
            if path and " " not in path:
                yield path, body
            i = k
        else:
            i += 1


def main(repo, out):
    if repo == "compare":
        sys.exit(compare(out, sys.argv[3]))
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
