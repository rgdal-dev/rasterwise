#!/usr/bin/env python3
"""
curate.py -- maintain this repo's tables from harvest deltas. Standard library only.

  merge DELTA.csv ...    append a delta's sightings to sightings.csv, then build
  build                  regenerate manifest.csv and missing.csv from
                         sightings.csv + cases/*/case.yaml + ledger/ (+ the
                         curated columns already in manifest.csv)
  check                  validate tables, cases, ASCII, no data files in git
  issues JSONDIR         write issues/NNN.md from `gh issue view --json` dumps
  stage DEST             copy every manifest file this machine has a sighting of
                         into DEST/files/<aa>/<sha256>, re-hashing each
  pages                  write the generated site pages (cases/index.md,
                         files.md, missing.md) for the Quarto site
  set-url SHA URL        download URL, re-hash, and only if it matches set the
                         manifest url (rule: no url without a verified fetch)

Tables
  sightings.csv  one row per (content, place seen). Append-only; the truth.
  manifest.csv   one row per in-scope sha256. Generated columns: size, aliases,
                 case, format, status, sources. Curated columns, kept across
                 builds once set: canonical_path, url, redistributable, note.
  missing.csv    paths known from old file lists (ledger/listed.csv) with no
                 intact matching bytes yet. A path leaves when a hash turns up
                 at that path, or is confirmed in ledger/aliases.csv.
"""
import csv
import datetime
import fnmatch
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import harvest  # noqa: E402  (shared sniffing/ checks)

P = lambda *a: os.path.join(REPO, *a)  # noqa: E731
SIGHT_COLS = [c for c in harvest.COLS if c != "delta"]
MAN_COLS = ["sha256", "size", "canonical_path", "aliases", "case", "format", "status",
            "sources", "url", "redistributable", "note"]
CURATED = ("canonical_path", "url", "redistributable", "note")
MISS_COLS = ["path", "first_listed", "last_listed", "fingerprint", "best_partial", "note"]
CASE_REQUIRED = ["id", "title", "status", "summary", "files", "whats_wrong", "how_to_read", "links"]
# optional: findings (codes), missing (paths from ledger/listed.csv), retired (true/false),
# costume (list): the storage form(s) of the case's grid(s), as in the costumes table of
# regular-in-what (A-H, E2, E3), or "none" for data that is not a grid at all.
COSTUMES = {"A", "B", "C", "D", "E", "E2", "E3", "F", "G", "H", "none"}
COSTUME_TABLE = "https://hypertidy.github.io/regular-in-what/03-costumes.html#tbl-costumes"
# A case is never deleted or renamed; set retired: true instead.
CASE_STATUS = {"open", "understood", "fixed-upstream"}
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SHA = re.compile(r"^[0-9a-f]{64}$")
STATUS_RANK = {"ok": 0, "truncated": 1, "unreadable": 2}

csv.field_size_limit(min(sys.maxsize, 2 ** 31 - 1))


def log(*a):
    print(*a, file=sys.stderr)


def read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, cols, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)


# ------------------------------------------------------------------ case.yaml subset
# A strict YAML subset, so the standard library can read it and PyYAML agrees:
#   key: "quoted scalar" | plain-scalar-without-colon-space | true/false | []
#   key: |            block of lines indented by 2+ spaces
#   key:              followed by "  - item" lines (scalars; trailing "  # comment" ok)
# Comment lines start with "#".

def parse_case(text):
    out, key, mode, buf = {}, None, None, []
    lines = text.split("\n")

    def scalar(v):
        v = v.strip()
        if v.startswith('"'):
            if not v.endswith('"') or len(v) < 2:
                raise ValueError("unterminated quote: %s" % v)
            return v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
        if v in ("true", "false"):
            return v == "true"
        if v == "[]":
            return []
        if ": " in v or v.startswith(("{", "[", "&", "*", "!", "|", ">", "'", "@", "`")):
            raise ValueError("value must be quoted: %s" % v)
        return v

    def flush():
        nonlocal key, mode, buf
        if key is None:
            return
        if mode == "block":
            while buf and not buf[-1].strip():
                buf.pop()
            ind = min((len(l) - len(l.lstrip(" ")) for l in buf if l.strip()), default=0)
            out[key] = "\n".join(l[ind:] for l in buf) + "\n"
        elif mode == "list":
            out[key] = buf
        key, mode, buf = None, None, []

    for n, line in enumerate(lines, 1):
        if mode == "block":
            if line.startswith("  ") or not line.strip():
                buf.append(line)
                continue
            flush()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if mode == "list" and line.startswith("  - "):
            item = line[4:]
            item = re.sub(r"\s+#\s.*$", "", item) if not item.lstrip().startswith('"') else item
            buf.append(scalar(item))
            continue
        flush()
        m = re.match(r"^([a-z_]+):(.*)$", line)
        if not m:
            raise ValueError("line %d: expected 'key: value': %r" % (n, line))
        key, rest = m.group(1), m.group(2).strip()
        if key in out:
            raise ValueError("line %d: duplicate key %s" % (n, key))
        if rest == "|":
            mode, buf = "block", []
        elif rest == "":
            mode, buf = "list", []
        else:
            out[key] = scalar(rest)
            key = None
    flush()
    return out


def load_cases():
    cases = {}
    d = P("cases")
    if not os.path.isdir(d):
        return cases
    for slug in sorted(os.listdir(d)):
        y = os.path.join(d, slug, "case.yaml")
        if os.path.isfile(y):
            with open(y, encoding="utf-8") as f:
                cases[slug] = parse_case(f.read())
    return cases


# ------------------------------------------------------------------ scope + names

def load_scope():
    pats = []
    p = P("tools", "scope.txt")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.split("#", 1)[0].strip()
            if line:
                pats.append(line)
    return pats


def full_name(r):
    """Path of the content relative to the instance root it was seen in."""
    if r["kind"] == "git-blob":
        return r["member"].rsplit("@", 1)[0]
    if r["kind"] == "archive-member":
        return r["member"].replace(harvest.SEP, "/")
    return r["relpath"].replace("\\", "/")


def in_scope(r, pats):
    if r.get("_has_members"):
        return False  # an archive shell whose members are listed in their own right
    name = full_name(r)
    for p in pats:
        if p.startswith("sha256:"):
            if r["sha256"] == p[7:]:
                return False
            continue
        neg = p.startswith("!")
        pat = p[1:] if neg else p
        # match the content's own name, and for archive members also the archive's path
        if fnmatch.fnmatch(name, pat) or (r["kind"] == "archive-member" and fnmatch.fnmatch(r["relpath"], pat)):
            return neg  # "!pat" = force include; "pat" = exclude
    return True


def source_label(r):
    loc = r["machine"]
    if r["volume"]:
        loc += ":" + r["volume"]
    if r["root"]:
        loc += ":" + r["root"]
    where = full_name(r)
    if r["kind"] == "archive-member":
        where = r["relpath"] + "!" + r["member"]
    elif r["kind"] == "git-blob":
        where = r["member"]
    return "%s:%s (%s)" % (loc, where, r["seen"])


def load_places():
    """ledger/places.csv: machine,root,prefix,note -- names content found in a known
    working folder outside a rasterwise tree (e.g. ~/ncd -> extdata/nc-to-cog/)."""
    return {(r["machine"], r["root"]): r["prefix"] for r in read_csv(P("ledger", "places.csv"))}


PLACES = {}


def tree_name(r):
    return PLACES.get((r["machine"], r["root"]), "") + full_name(r)


def pick_canonical(rows):
    """Prefer the repo working-tree name: extdata/ then data-raw/ then shortest;
    among those, the earliest sighting by mtime."""
    listed = read_csv(P("ledger", "listed.csv"))
    latest = max((l["last_listed"] for l in listed), default="")
    current = {"extdata/" + l["path"] for l in listed if l["last_listed"] == latest}

    def key(r):
        n = tree_name(r)
        return (0 if n in current else 1,
                0 if n.startswith("extdata/") else 1 if n.startswith("data-raw/") else 2,
                0 if r["kind"] != "git-blob" else 1,
                "".join(chr(0x10FFFF - ord(c)) for c in (r["mtime"] or "")),  # newest first
                len(n), n)
    return tree_name(sorted(rows, key=key)[0])


# ------------------------------------------------------------------ build

def build():
    PLACES.clear()
    PLACES.update(load_places())
    sights = read_csv(P("sightings.csv"))
    pats = load_scope()
    shells = {(s["machine"], s["volume"], s["root"], s["relpath"]) for s in sights if s["kind"] == "archive-member"}
    for s in sights:
        s["_has_members"] = s["kind"] == "file" and (s["machine"], s["volume"], s["root"], s["relpath"]) in shells
    # an archive whose members were read anywhere is a shell everywhere (e.g. the same zip as a git blob)
    shell_shas = {s["sha256"] for s in sights if s["_has_members"]}
    for s in sights:
        if s["sha256"] in shell_shas:
            s["_has_members"] = True
    by_sha = {}
    for s in sights:
        if s["sha256"] and in_scope(s, pats):
            by_sha.setdefault(s["sha256"], []).append(s)

    cases = load_cases()
    case_of = {}
    for slug, c in cases.items():
        for h in c.get("files", []) or []:
            case_of.setdefault(h, []).append(slug)

    aliases = read_csv(P("ledger", "aliases.csv"))
    alias_of = {}
    for a in aliases:  # ledger paths are relative to extdata/
        alias_of.setdefault(a["sha256"], []).append("extdata/" + a["path"])

    old = {r["sha256"]: r for r in read_csv(P("manifest.csv"))}
    rows = []
    # canonical_path: never changed once set; unique. New content is named in order of
    # newest sighting first, so a name already in use by older bytes keeps going to... the
    # older bytes only if they were named first; otherwise older versions get "~<sha8>".
    taken = {old[h]["canonical_path"] for h in by_sha if old.get(h, {}).get("canonical_path")}
    newest = lambda h: max((s["mtime"] or "" for s in by_sha[h]), default="")  # noqa: E731
    canon_of = {}
    for h in sorted(by_sha, key=lambda h: (bool(old.get(h, {}).get("canonical_path")), newest(h)), reverse=True):
        prev = old.get(h, {})
        if prev.get("canonical_path"):
            canon_of[h] = prev["canonical_path"]
            continue
        ss = by_sha[h]
        named = [tree_name(s) for s in ss]
        if any(n.startswith("extdata/") for n in named) or h not in alias_of:
            c = pick_canonical(ss)
        else:
            c = alias_of[h][0]
        if c in taken:
            c = "%s~%s" % (c, h[:8])
        taken.add(c)
        canon_of[h] = c
    for h, ss in by_sha.items():
        prev = old.get(h, {})
        names = sorted({tree_name(s) for s in ss} | set(alias_of.get(h, [])))
        canon = canon_of[h]
        status = max((s["status"] for s in ss), key=lambda x: STATUS_RANK.get(x, 3))
        fmt = sorted({s["format"] for s in ss if s["format"]}) or [""]
        rows.append(dict(
            sha256=h, size=ss[0]["size"], canonical_path=canon,
            aliases=";".join(n for n in names if n != canon),
            case=";".join(sorted(case_of.get(h, []))),
            format=fmt[0], status=status,
            sources=";".join(sorted({source_label(s) for s in ss})),
            url=prev.get("url", ""), redistributable=prev.get("redistributable") or "unknown",
            note=prev.get("note", "")))
    rows.sort(key=lambda r: (r["canonical_path"].lower(), r["sha256"]))
    write_csv(P("manifest.csv"), MAN_COLS, rows)

    # missing list
    listed = read_csv(P("ledger", "listed.csv"))
    ok_names = {}
    partial = {}
    for h, ss in by_sha.items():
        for s in ss:
            n = full_name(s)
            (ok_names if s["status"] == "ok" and not short_of(s, sights) else partial).setdefault(n, set()).add(h)
    aliased = {a["path"] for a in aliases if a["sha256"] in by_sha}
    fps = set()
    if os.path.isdir(P("fingerprints")):
        for dp, _, fns in os.walk(P("fingerprints")):
            for fn in fns:
                if fn.endswith(".cdl"):
                    fps.add(os.path.relpath(os.path.join(dp, fn), P("fingerprints"))[:-4])
    miss = []
    for l in listed:
        p = l["path"]

        def match(d):
            return {h for n, hs in d.items() if n == p or n.endswith("/" + p) for h in hs}
        if match(ok_names) or p in aliased:
            continue
        part = match(partial)
        best = ""
        if part:
            best = max(part, key=lambda h: int(by_sha[h][0]["size"]))
        miss.append(dict(path=p, first_listed=l["first_listed"], last_listed=l["last_listed"],
                         fingerprint="yes" if p in fps else "no", best_partial=best,
                         note=l.get("note", "")))
    write_csv(P("missing.csv"), MISS_COLS, miss)
    log("manifest.csv: %d files (%d with a case);  missing.csv: %d paths" %
        (len(rows), sum(1 for r in rows if r["case"]), len(miss)))


def short_of(s, sights):
    """A plain file with the same name as an archive member that is known to be
    truncated at a larger expected size is itself short (e.g. an extracted stub)."""
    if s["kind"] != "file":
        return False
    n = full_name(s)
    for t in sights:
        if t["status"] == "truncated" and t["expected_size"] and full_name(t) == n:
            try:
                if int(s["size"]) < int(t["expected_size"]):
                    return True
            except ValueError:
                pass
    return False


# ------------------------------------------------------------------ merge

def merge(deltas):
    sights = read_csv(P("sightings.csv"))
    key = lambda r: tuple(r.get(c, "") for c in ("sha256", "kind", "machine", "volume", "root", "relpath", "member"))  # noqa
    have = {key(r) for r in sights}
    added = 0
    for d in deltas:
        for r in read_csv(d):
            if key(r) not in have:
                have.add(key(r))
                sights.append(r)
                added += 1
    sights.sort(key=lambda r: (r["machine"], r["volume"], r["root"], r["relpath"], r["member"]))
    write_csv(P("sightings.csv"), SIGHT_COLS, sights)
    log("sightings.csv: +%d rows (%d total)" % (added, len(sights)))
    build()


# ------------------------------------------------------------------ check

DATA_SNIFF = {"netcdf3", "netcdf4/hdf5", "hdf4", "geotiff", "tiff", "zip", "grib", "gzip", "tar",
              "bzip2", "xz", "binary"}


def check():
    errs, warns = [], []
    man = read_csv(P("manifest.csv"))
    if man and list(man[0].keys()) != MAN_COLS:
        errs.append("manifest.csv columns %s != %s" % (list(man[0].keys()), MAN_COLS))
    shas = {r["sha256"] for r in man}
    for r in man:
        if not SHA.match(r["sha256"]):
            errs.append("manifest: bad sha256 %r" % r["sha256"])
        if r["status"] not in STATUS_RANK:
            errs.append("manifest %s: status %r" % (r["sha256"][:12], r["status"]))
        if r["redistributable"] not in ("yes", "no", "unknown"):
            errs.append("manifest %s: redistributable %r" % (r["sha256"][:12], r["redistributable"]))
        if r["redistributable"] == "no" and r["url"]:
            errs.append("manifest %s: redistributable=no but has a public url" % r["sha256"][:12])
    try:
        import yaml  # optional cross-check only
    except ImportError:
        yaml = None
    seen_ids = set()
    for slug in sorted(os.listdir(P("cases"))) if os.path.isdir(P("cases")) else []:
        if not os.path.isdir(P("cases", slug)):
            continue  # e.g. the generated cases/index.md
        y = P("cases", slug, "case.yaml")
        if not os.path.isfile(y):
            errs.append("cases/%s: no case.yaml" % slug)
            continue
        text = open(y, encoding="utf-8").read()
        try:
            c = parse_case(text)
        except ValueError as e:
            errs.append("cases/%s/case.yaml: %s" % (slug, e))
            continue
        if yaml is not None:
            try:
                if yaml.safe_load(text) != c:
                    errs.append("cases/%s/case.yaml: PyYAML reads it differently" % slug)
            except Exception as e:
                errs.append("cases/%s/case.yaml: not valid YAML: %s" % (slug, e))
        for k in CASE_REQUIRED:
            if k not in c:
                errs.append("cases/%s: missing key %s" % (slug, k))
        if c.get("id") != slug:
            errs.append("cases/%s: id %r != directory name" % (slug, c.get("id")))
        if not SLUG.match(slug):
            errs.append("cases/%s: slug must be lowercase-hyphenated" % slug)
        if slug in seen_ids:
            errs.append("duplicate case id %s" % slug)
        seen_ids.add(slug)
        if c.get("status") not in CASE_STATUS:
            errs.append("cases/%s: status %r" % (slug, c.get("status")))
        for h in c.get("files", []) or []:
            if not SHA.match(str(h)):
                errs.append("cases/%s: files entry is not a sha256: %r" % (slug, h))
            elif h not in shas:
                errs.append("cases/%s: file %s not in manifest.csv" % (slug, h[:12]))
        listed_paths = {l["path"] for l in read_csv(P("ledger", "listed.csv"))}
        for mp in c.get("missing", []) or []:
            if mp not in listed_paths:
                errs.append("cases/%s: missing entry %r is not in ledger/listed.csv" % (slug, mp))
        for cc in c.get("costume", []) or []:
            if cc not in COSTUMES:
                errs.append("cases/%s: costume %r not one of %s" % (slug, cc, ", ".join(sorted(COSTUMES))))
        if "retired" in c and not isinstance(c["retired"], bool):
            errs.append("cases/%s: retired must be true or false" % slug)
        if not os.path.isfile(P("cases", slug, "README.md")):
            errs.append("cases/%s: no README.md" % slug)
    # ascii + no data in git
    try:
        tracked = subprocess.run(["git", "-C", REPO, "ls-files", "-z"], stdout=subprocess.PIPE,
                                 check=True).stdout.decode().split("\0")
    except Exception:
        tracked = []
        warns.append("not a git checkout: skipped tracked-file checks")
    for t in filter(None, tracked):
        p = P(t)
        if not os.path.isfile(p):
            continue
        with open(p, "rb") as f:
            head = f.read(65536)
        fmt = harvest.sniff(head, t)
        if fmt in DATA_SNIFF:
            errs.append("data file tracked in git: %s (%s)" % (t, fmt))
            continue
        data = open(p, "rb").read()
        try:
            data.decode("ascii")
        except UnicodeDecodeError as e:
            line = data[:e.start].count(b"\n") + 1
            errs.append("non-ASCII in %s line %d" % (t, line))
    for w in warns:
        log("warn: " + w)
    for e in errs:
        log("ERROR: " + e)
    log("check: %d errors, %d cases, %d manifest rows" % (len(errs), len(seen_ids), len(man)))
    return 1 if errs else 0


# ------------------------------------------------------------------ issues

ASCII_MAP = {"\u2014": "--", "\u2013": "-", "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
             "\u2026": "...", "\u00b5": "u", "\u00b1": "+/-", "\u03c3": "sigma", "\u00a0": " ",
             "\u00b0": " deg", "\u00d7": "x"}
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
REPLY_HDR = re.compile(r"^.*\bwrote:\s*$", re.M)


def to_ascii(s):
    s = "".join(ASCII_MAP.get(ch, ch) for ch in s)
    return s.encode("ascii", "backslashreplace").decode("ascii")


SIGN_OFF = re.compile(r"^\s*(cheers|regards|best|thanks|many thanks|kind regards|best wishes)\b.{0,25}$", re.I)
QUOTED_SIG = re.compile(r"^\s*(>\s*)+(--|##)\s*$")


def cut_signatures(s):
    out = []
    for line in s.split("\n"):
        if QUOTED_SIG.match(line):
            out.append("[quoted email footer and signature removed]")
            break
        if SIGN_OFF.match(line):
            out.append("[sign-off and signature removed]")
            break
        out.append(line)
    return "\n".join(out)


UNSUB = re.compile(r"\S*notifications/unsubscribe\S*")


def scrub(s):
    s = to_ascii(s.replace("\r\n", "\n"))
    s = cut_signatures(s)
    s = REPLY_HDR.sub("[quoted email reply header removed]", s)
    s = UNSUB.sub("[notification link removed]", s)
    return EMAIL.sub("[email]", s)


def repo_web_url():
    """This repo's web URL as git knows it now (never hard-coded: the repo may move)."""
    try:
        u = subprocess.run(["git", "-C", REPO, "remote", "get-url", "origin"], stdout=subprocess.PIPE,
                           check=True).stdout.decode().strip()
    except Exception:
        return ""
    if u.startswith("git@"):
        u = "https://" + u[4:].replace(":", "/", 1)
    return u[:-4] if u.endswith(".git") else u


def issue_url(n):
    base = repo_web_url()
    return "%s/issues/%d" % (base, n) if base else ""


CAPTURED = os.environ.get("RW_CAPTURED", "")


def issues(jsondir):
    import json
    os.makedirs(P("issues"), exist_ok=True)
    idx = []
    for fn in sorted(os.listdir(jsondir)):
        if not fn.endswith(".json"):
            continue
        d = json.load(open(os.path.join(jsondir, fn), encoding="utf-8"))
        n = d["number"]
        url = d.get("url") or issue_url(n)
        lines = ["# %d. %s" % (n, scrub(d["title"])), "",
                 "- number: %d" % n,
                 "- opened: %s" % d["createdAt"][:10],
                 "- state when archived: %s" % d["state"].lower(),
                 "- url when archived: %s" % url,
                 "- archived: %s (authors omitted; email addresses and reply headers redacted;"
                 " non-ASCII transliterated)" % d.get("_captured", CAPTURED or datetime.date.today().isoformat()),
                 "", "## Opening post", "", scrub(d["body"] or "(empty)").rstrip(), ""]
        for i, c in enumerate(d.get("comments", []), 1):
            lines += ["## Comment %d (%s)" % (i, c["createdAt"][:10]), "", scrub(c["body"]).rstrip(), ""]
        out = P("issues", "%03d.md" % n)
        with open(out, "w", encoding="ascii", newline="\n") as f:
            f.write("\n".join(lines))
        idx.append((n, scrub(d["title"]), d["createdAt"][:10], d["state"].lower()))
    with open(P("issues", "README.md"), "w", encoding="ascii", newline="\n") as f:
        f.write("# Issues archive\n\nThis repo's GitHub issues, archived as markdown so the lessons in them\n"
                "survive independently of the hosting. Identity is the issue number.\n\n"
                "| # | opened | state | title |\n|---|---|---|---|\n")
        for n, t, dt, st in sorted(idx):
            f.write("| [%d](%03d.md) | %s | %s | %s |\n" % (n, n, dt, st, t.replace("|", "/")))
    log("issues/: %d archived" % len(idx))


# ------------------------------------------------------------------ bytes

def local_sources(sha, sights, me):
    for s in sights:
        if s["sha256"] != sha or s["machine"] != me:
            continue
        root = os.path.expanduser(s["root"])
        yield s, root


def open_sighting(s, root):
    full = os.path.join(root, s["relpath"]) if s["relpath"] else root
    if s["kind"] == "file":
        return open(full, "rb")
    if s["kind"] == "git-blob":
        oid = s["member"].rsplit("@", 1)[1]
        repo = full
        data = subprocess.run(["git", "-C", repo, "cat-file", "blob",
                               subprocess.run(["git", "-C", repo, "rev-parse", oid], stdout=subprocess.PIPE,
                                              check=True).stdout.decode().strip()],
                              stdout=subprocess.PIPE, check=True).stdout
        return io.BytesIO(data)
    f = open(full, "rb")
    name = full
    for m in s["member"].split(harvest.SEP):
        k = harvest.archive_kind(name) or "tar"
        if k == "zip":
            import zipfile
            f, _ = harvest.spool(zipfile.ZipFile(f).open(m))
        elif k in ("tar",) or harvest.is_tar(f):
            import tarfile
            f.seek(0)
            f, _ = harvest.spool(tarfile.open(fileobj=f, mode="r:*").extractfile(m))
        else:
            import gzip, bz2, lzma  # noqa: E401
            op = {"gz": gzip.GzipFile, "bz2": bz2.BZ2File, "xz": lzma.LZMAFile}[k]
            f, _ = harvest.spool(op(fileobj=f))
        name = m
    return f


def stage(dest):
    import socket
    me = socket.gethostname().split(".")[0]
    sights = read_csv(P("sightings.csv"))
    man = read_csv(P("manifest.csv"))
    done = 0
    for r in man:
        h = r["sha256"]
        out = os.path.join(dest, "files", h[:2], h)
        if os.path.exists(out):
            done += 1
            continue
        for s, root in local_sources(h, sights, me):
            try:
                src = open_sighting(s, root)
                os.makedirs(os.path.dirname(out), exist_ok=True)
                hh = hashlib.sha256()
                with open(out + ".part", "wb") as o:
                    while True:
                        b = src.read(1 << 20)
                        if not b:
                            break
                        hh.update(b)
                        o.write(b)
                if hh.hexdigest() != h:
                    os.remove(out + ".part")
                    continue
                os.rename(out + ".part", out)
                done += 1
                break
            except Exception as e:
                log("  [warn] %s from %s: %s" % (h[:12], source_label(s), e))
    log("staged %d of %d manifest files under %s/files/" % (done, len(man), dest))


def set_url(sha, url):
    from urllib.request import urlopen
    h = hashlib.sha256()
    n = 0
    with urlopen(url) as resp:
        while True:
            b = resp.read(1 << 20)
            if not b:
                break
            h.update(b)
            n += len(b)
    if h.hexdigest() != sha:
        log("REFUSED: %s fetched %d bytes hashing to %s, not %s" % (url, n, h.hexdigest()[:12], sha[:12]))
        return 1
    man = read_csv(P("manifest.csv"))
    hit = [r for r in man if r["sha256"] == sha]
    if not hit:
        log("REFUSED: %s not in manifest.csv" % sha)
        return 1
    if hit[0]["redistributable"] == "no":
        log("REFUSED: %s is redistributable=no; keep it private" % sha[:12])
        return 1
    hit[0]["url"] = url
    write_csv(P("manifest.csv"), MAN_COLS, man)
    log("verified %d bytes; url set for %s" % (n, sha[:12]))
    return 0


# ------------------------------------------------------------------ site pages
# Generated markdown for the Quarto site (not committed; CI runs `pages` before
# `quarto render`). Everything here is derived from the tables and cases.

def md_cell(v):
    return str(v).replace("|", "/").replace("\n", " ")


def pages():
    cases = load_cases()
    man = read_csv(P("manifest.csv"))
    miss = read_csv(P("missing.csv"))
    by_sha = {r["sha256"]: r for r in man}
    order = {"open": 0, "understood": 1, "fixed-upstream": 2}
    out = ["---", 'title: "Cases"', "---", "",
           "Each case is one lesson: what is wrong with a file and how to read it correctly. "
           "`status` is `understood` when the case gives a working read, `open` when something "
           "is not yet determined, `fixed-upstream` when current software handles it.", "",
           "%d cases: %s." % (len(cases), ", ".join("%d %s" % (sum(1 for c in cases.values() if c.get("status") == st), st)
                                                     for st in ("understood", "open", "fixed-upstream"))), "",
           "Costume is the storage form of the grid, from the [costumes table](%s) in "
           "*regular-in-what*: what was stored versus what the grid really is. "
           "`none` means the data is not a grid." % COSTUME_TABLE, "",
           "Costumes: %s." % ", ".join("%s %d" % (k, v) for k, v in sorted(
               __import__("collections").Counter(x for c in cases.values() for x in (c.get("costume") or ["?"])).items())), "",
           "| case | costume | status | findings | summary |", "|---|---|---|---|---|"]
    for slug, c in sorted(cases.items(), key=lambda kv: (kv[1].get("title", "").lower())):
        if c.get("retired") is True:
            continue
        out.append("| [%s](%s/index.qmd) | %s | %s | %s | %s |" % (
            md_cell(c.get("title", slug)), slug, " ".join(c.get("costume") or []), c.get("status", ""),
            " ".join("`%s`" % f for f in (c.get("findings") or [])), md_cell(c.get("summary", ""))))
    with open(P("cases", "index.md"), "w", encoding="ascii", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    # Quarto never renders README.md files, so each one gets a wrapper page that includes it
    for d in [P("cases", slug) for slug in cases] + [P("issues")]:
        if os.path.isfile(os.path.join(d, "README.md")):
            t = cases.get(os.path.basename(d), {}).get("title", "Issues archive")
            with open(os.path.join(d, "index.qmd"), "w", encoding="ascii", newline="\n") as f:
                f.write('---\npagetitle: "%s"\n---\n\n{{< include README.md >}}\n' % t.replace('"', "'"))

    out = ["---", 'title: "Files"', "---", "",
           "Every file in the archive, keyed by sha256 (the full table is [manifest.csv](manifest.csv)). "
           "Download urls will appear once the content-addressed store is published.", "",
           "| name | format | status | size | sha256 | case |", "|---|---|---|---:|---|---|"]
    for r in man:
        cs = " ".join("[%s](cases/%s/index.qmd)" % (c, c) for c in r["case"].split(";") if c)
        out.append("| `%s` | %s | %s | %s | `%s` | %s |" % (
            md_cell(r["canonical_path"]), r["format"] or "?", r["status"], r["size"], r["sha256"][:12], cs))
    with open(P("files.md"), "w", encoding="ascii", newline="\n") as f:
        f.write("\n".join(out) + "\n")

    out = ["---", 'title: "Missing files"', "---", "",
           "Files listed in the old bundles (2018-2020) for which no intact bytes have been found on "
           "any machine searched. Most were only in the v0.5.0 release tarball, whose upload was cut "
           "off. Where the old README recorded an `ncdump -h`, a fingerprint survives and can confirm a "
           "copy if one turns up (`tools/readme_headers.py compare`). The table is [missing.csv](missing.csv).", "",
           "| path | listed | fingerprint | partial copy |", "|---|---|---|---|"]
    for m in miss:
        fp = "[yes](fingerprints/%s.cdl)" % m["path"] if m["fingerprint"] == "yes" else "no"
        part = ("`%s` (%s bytes)" % (m["best_partial"][:12], by_sha.get(m["best_partial"], {}).get("size", "?"))
                if m["best_partial"] else "")
        out.append("| `%s` | %s to %s | %s | %s |" % (md_cell(m["path"]), m["first_listed"], m["last_listed"], fp, part))
    with open(P("missing.md"), "w", encoding="ascii", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    log("pages: cases/index.md, files.md, missing.md, and an index.qmd beside each README.md")


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, args = argv[0], argv[1:]
    if cmd == "merge":
        merge(args)
    elif cmd == "build":
        build()
    elif cmd == "check":
        return check()
    elif cmd == "issues":
        issues(args[0])
    elif cmd == "pages":
        pages()
    elif cmd == "stage":
        stage(args[0])
    elif cmd == "set-url":
        return set_url(args[0], args[1])
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
