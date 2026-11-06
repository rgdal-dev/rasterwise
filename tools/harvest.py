#!/usr/bin/env python3
"""
harvest.py -- find rasterwise content in a directory or archive on any machine
and write a *delta*: what was seen, where, and how it relates to the manifest.

It never edits manifest.csv or sightings.csv. Merging a delta is a separate,
reviewable step:  python3 tools/curate.py merge <delta.csv>

Python standard library only (3.6+). Copy this one file to a bare VM.

  python3 harvest.py ROOT [ROOT ...] [-o delta.csv]
          [--manifest manifest.csv|URL] [--missing missing.csv|URL]
          [--as MACHINE:VOLUME:ROOT]   # record a downloaded copy as where it came from
          [--no-git] [--no-archives]

What is hashed: every regular file; every member of tar/tgz/zip/gz/bz2/xz
archives (recursively); every blob in the full history of any git repo found
(all refs + reflog). Each row records machine, volume (mount point), root,
relpath, archive member, mtime, size, sha256, sniffed format, and a status:

  ok          bytes look complete by the check named in `check`
  truncated   shorter than its own header/archive says it should be
  unreadable  format signature doesn't match the file (e.g. .nc that isn't netCDF/HDF)

The `delta` column classifies each row against the manifest (if given):
  new           sha256 not in the manifest
  new-location  known sha256, seen somewhere the manifest doesn't record
  known         nothing new
  missing-match file name/path matches an entry in missing.csv (check it!)
plus status truncated/unreadable rows are always reported.
A short human report goes to stderr (and to <delta>.txt).
"""
import argparse
import bz2
import csv
import datetime
import gzip
import hashlib
import io
import lzma
import os
import shutil
import socket
import struct
import subprocess
import sys
import tarfile
import tempfile
import zipfile

try:
    from urllib.request import urlopen
except ImportError:  # pragma: no cover
    urlopen = None

COLS = ["sha256", "size", "status", "check", "expected_size", "format", "kind",
        "machine", "volume", "root", "relpath", "member", "mtime", "seen", "delta"]
SKIP_DIRS = {".git", ".Rproj.user", "__pycache__", ".ipynb_checkpoints", "node_modules"}
SKIP_FILES = {".DS_Store", "Thumbs.db", "desktop.ini"}
SEP = "!"
CHUNK = 1 << 20
MAX_DEPTH = 4
HOME = os.path.expanduser("~")
TODAY = datetime.date.today().isoformat()

csv.field_size_limit(min(sys.maxsize, 2 ** 31 - 1))


def log(*a):
    print(*a, file=sys.stderr)


def tilde(p):
    """Record home-relative paths as ~ (public text names repos, not people)."""
    if p == HOME or p.startswith(HOME + os.sep):
        return "~" + p[len(HOME):]
    return p


def iso(t):
    try:
        return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    except Exception:
        return ""


def mount_point(path):
    path = os.path.realpath(path)
    try:
        dev = os.stat(path).st_dev
    except OSError:
        return ""
    while path != os.path.dirname(path):
        parent = os.path.dirname(path)
        try:
            if os.stat(parent).st_dev != dev:
                return path
        except OSError:
            return path
        path = parent
    return path


# ------------------------------------------------------------------ hashing

class Truncated(Exception):
    def __init__(self, digest, n, err):
        Exception.__init__(self, str(err))
        self.digest, self.n = digest, n


def sha256_stream(f, keep_head=0):
    """Return (hexdigest, nbytes, head_bytes)."""
    h = hashlib.sha256()
    n = 0
    head = b""
    while True:
        try:
            b = f.read(CHUNK)
        except (EOFError, OSError, tarfile.ReadError, zipfile.BadZipFile, lzma.LZMAError, zlib_error()) as e:
            raise Truncated(h.hexdigest(), n, e)
        if not b:
            break
        if len(head) < keep_head:
            head += b[: keep_head - len(head)]
        h.update(b)
        n += len(b)
    return h.hexdigest(), n, head


def zlib_error():
    import zlib
    return zlib.error


# ------------------------------------------------------------------ format sniffing

HDF5_SIG = b"\x89HDF\r\n\x1a\n"
SCRIPT_EXT = (".r", ".py", ".sh", ".rmd", ".qmd", ".ipynb", ".js", ".sql", ".bat", ".ps1")
DATA_EXT = (".nc", ".nc4", ".h5", ".hdf", ".hdf5", ".he5", ".tif", ".tiff", ".grb", ".grib",
            ".grb2", ".grib2", ".zip")


def sniff(head, name):
    n = name.lower()
    if head[:3] == b"CDF" and head[3:4] in (b"\x01", b"\x02", b"\x05"):
        return "netcdf3"
    if head[257:262] == b"ustar":
        return "tar"  # before HDF5: tar puts member data on 512-byte boundaries too
    if head[:8] == HDF5_SIG or any(head[o:o + 8] == HDF5_SIG for o in (512, 1024, 2048)):
        return "netcdf4/hdf5"
    if head[:4] == b"\x0e\x03\x13\x01":
        return "hdf4"
    if head[:4] in (b"II*\x00", b"MM\x00*", b"II+\x00", b"MM\x00+"):
        return "geotiff" if is_geotiff(head) else "tiff"
    if head[:4] == b"PK\x03\x04" or head[:4] == b"PK\x05\x06":
        return "zip"
    if head[:4] == b"GRIB":
        return "grib"
    if head[:2] == b"\x1f\x8b":
        return "gzip"
    if head[257:262] == b"ustar":
        return "tar"
    if head[:3] == b"BZh":
        return "bzip2"
    if head[:6] == b"\xfd7zXZ\x00":
        return "xz"
    if b"<VRTDataset" in head[:512]:
        return "vrt"
    if head and b"\x00" not in head[:8192]:
        try:
            head[:8192].decode("utf-8")
            return "script" if n.endswith(SCRIPT_EXT) or n.endswith(".rhistory") else "text"
        except UnicodeDecodeError:
            pass
    if not head:
        return "empty"
    return "binary"


def is_geotiff(head):
    """Look for GeoKeyDirectory (34735) / ModelTiepoint (33922) / ModelPixelScale (33550)
    in the first IFD, if it is inside the head we have."""
    try:
        bo = "<" if head[:2] == b"II" else ">"
        if head[2:4] in (b"*\x00", b"\x00*"):
            off = struct.unpack(bo + "I", head[4:8])[0]
            n = struct.unpack(bo + "H", head[off:off + 2])[0]
            tags = {struct.unpack(bo + "H", head[off + 2 + 12 * i: off + 4 + 12 * i])[0] for i in range(n)}
        else:
            off = struct.unpack(bo + "Q", head[8:16])[0]
            n = struct.unpack(bo + "Q", head[off:off + 8])[0]
            tags = {struct.unpack(bo + "H", head[off + 8 + 20 * i: off + 10 + 20 * i])[0] for i in range(n)}
        return bool(tags & {34735, 33922, 33550, 34264})
    except Exception:
        return False


# ------------------------------------------------------------------ completeness checks
# Each returns (check_name, expected_size or None). None = could not determine.

def expected_size(fmt, f):
    try:
        if fmt == "netcdf3":
            return "nc3-header", nc3_expected(f)
        if fmt == "netcdf4/hdf5":
            return "hdf5-eoa", hdf5_expected(f)
        if fmt in ("geotiff", "tiff"):
            return "tiff-blocks", tiff_expected(f)
    except Exception as e:
        return "%s-failed:%s" % (fmt, type(e).__name__), None
    return "none", None


def nc3_expected(f):
    f.seek(0)
    magic = f.read(4)
    v = magic[3]
    big = v == 5
    off_big = v in (2, 5)

    def r(fmt, n):
        b = f.read(n)
        if len(b) < n:
            raise EOFError
        return struct.unpack(">" + fmt, b)[0]

    def num():  # NON_NEG
        return r("Q", 8) if big else r("I", 4)

    def name():
        n = num()
        b = f.read(n)
        f.read((4 - n % 4) % 4)
        return b

    tsize = {1: 1, 2: 1, 3: 2, 4: 4, 5: 4, 6: 8, 7: 1, 8: 2, 9: 4, 10: 8, 11: 8}

    def atts():
        tag = r("I", 4)
        n = num()
        if tag == 0:
            return
        for _ in range(n):
            name()
            t = r("I", 4)
            ne = num()
            nb = ne * tsize[t]
            f.seek(nb + (4 - nb % 4) % 4, 1)

    numrecs = num()
    tag = r("I", 4)
    nd = num()
    dims = []
    for _ in range(nd if tag else 0):
        name()
        dims.append(num())
    atts()
    tag = r("I", 4)
    nv = num()
    end_fixed, rec_begin, recsize, nrecvars = 0, None, 0, 0
    for _ in range(nv if tag else 0):
        name()
        ndims = num()
        dimids = [num() for _ in range(ndims)]
        atts()
        r("I", 4)  # nc_type
        vsize = num()
        begin = r("Q", 8) if off_big else r("I", 4)
        is_rec = ndims > 0 and dims[dimids[0]] == 0
        if is_rec:
            nrecvars += 1
            recsize += vsize
            rec_begin = begin if rec_begin is None else min(rec_begin, begin)
        else:
            if vsize in (0xFFFFFFFF,):
                return None
            end_fixed = max(end_fixed, begin + vsize)
    if numrecs == (0xFFFFFFFFFFFFFFFF if big else 0xFFFFFFFF):
        return None  # streaming
    exp = end_fixed
    if rec_begin is not None and numrecs:
        exp = max(exp, rec_begin + numrecs * recsize)
    return exp


def hdf5_expected(f):
    for base in [0] + [512 * 2 ** i for i in range(16)]:
        f.seek(base)
        if f.read(8) != HDF5_SIG:
            continue
        ver = f.read(1)[0]
        if ver in (0, 1):
            hdr = f.read(15)
            so = hdr[4]
            rest = 4 if ver == 1 else 0
            f.read(rest)
            fmt = {4: "<I", 8: "<Q"}[so]
            vals = [struct.unpack(fmt, f.read(so))[0] for _ in range(3)]
            base_addr, eof = vals[0], vals[2]
        else:
            so = f.read(1)[0]
            f.read(2)
            fmt = {4: "<I", 8: "<Q"}[so]
            vals = [struct.unpack(fmt, f.read(so))[0] for _ in range(3)]
            base_addr, eof = vals[0], vals[2]
        return base_addr + eof
    return None


def tiff_expected(f):
    f.seek(0)
    h = f.read(16)
    bo = "<" if h[:2] == b"II" else ">"
    bigtiff = h[2:4] in (b"+\x00", b"\x00+")
    off = struct.unpack(bo + ("Q" if bigtiff else "I"), h[8:16] if bigtiff else h[4:8])[0]
    tsz = {1: 1, 2: 1, 3: 2, 4: 4, 5: 8, 6: 1, 7: 1, 8: 2, 9: 4, 10: 8, 11: 4, 12: 8, 16: 8, 17: 8, 18: 8}
    tcode = {1: "B", 3: "H", 4: "I", 16: "Q"}
    end = 0
    seen = 0
    while off and seen < 1000:
        seen += 1
        f.seek(off)
        if bigtiff:
            n = struct.unpack(bo + "Q", f.read(8))[0]
            esz = 20
        else:
            n = struct.unpack(bo + "H", f.read(2))[0]
            esz = 12
        raw = f.read(n * esz)
        nxt = f.read(8 if bigtiff else 4)
        tags = {}
        for i in range(n):
            e = raw[i * esz:(i + 1) * esz]
            tag, typ = struct.unpack(bo + "HH", e[:4])
            cnt = struct.unpack(bo + ("Q" if bigtiff else "I"), e[4:12] if bigtiff else e[4:8])[0]
            if tag not in (273, 279, 324, 325) or typ not in tcode:
                continue
            nb = cnt * tsz[typ]
            inline = e[12:20] if bigtiff else e[8:12]
            if nb <= len(inline):
                data = inline[:nb]
            else:
                p = struct.unpack(bo + ("Q" if bigtiff else "I"), inline)[0]
                here = f.tell()
                f.seek(p)
                data = f.read(nb)
                f.seek(here)
            tags[tag] = struct.unpack(bo + tcode[typ] * cnt, data)
        for o_tag, c_tag in ((273, 279), (324, 325)):
            if o_tag in tags and c_tag in tags:
                for o, c in zip(tags[o_tag], tags[c_tag]):
                    if c:
                        end = max(end, o + c)
        off = struct.unpack(bo + ("Q" if bigtiff else "I"), nxt)[0] if len(nxt) == (8 if bigtiff else 4) else 0
    return end or None


def assess(path_or_fobj, name, size):
    """-> (format, status, check, expected_size)"""
    own = isinstance(path_or_fobj, str)
    f = open(path_or_fobj, "rb") if own else path_or_fobj
    try:
        f.seek(0)
        head = f.read(65536)
        fmt = sniff(head, name)
        if fmt == "zip":
            try:
                f.seek(0)
                zipfile.ZipFile(f).namelist()
                return fmt, "ok", "zip-directory", ""
            except zipfile.BadZipFile:
                return fmt, "truncated", "zip-directory", ""
        check, exp = expected_size(fmt, f)
        status = "ok"
        if exp is not None and size < exp:
            status = "truncated"
        low = name.lower()
        if (low.endswith((".nc", ".nc4")) and fmt not in ("netcdf3", "netcdf4/hdf5")) or \
           (low.endswith((".h5", ".hdf5", ".he5")) and fmt != "netcdf4/hdf5") or \
           (low.endswith(".hdf") and fmt not in ("hdf4", "netcdf4/hdf5")) or \
           (low.endswith((".tif", ".tiff")) and fmt not in ("geotiff", "tiff")):
            status = "unreadable"
            check = "signature"
        return fmt, status, check, "" if exp is None else str(exp)
    finally:
        if own:
            f.close()


# ------------------------------------------------------------------ archives

def archive_kind(name):
    n = name.lower()
    if n.endswith((".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tbz2", ".tar.xz", ".txz")):
        return "tar"
    if n.endswith(".zip"):
        return "zip"
    if n.endswith(".gz"):
        return "gz"
    if n.endswith(".bz2"):
        return "bz2"
    if n.endswith(".xz"):
        return "xz"
    return None


def is_tar(fobj):
    try:
        pos = fobj.tell()
        try:
            with tarfile.open(fileobj=fobj, mode="r:*"):
                return True
        finally:
            fobj.seek(pos)
    except Exception:
        return False


def spool(f, spool_max=512 << 20):
    t = tempfile.SpooledTemporaryFile(max_size=spool_max)
    try:
        shutil.copyfileobj(f, t, CHUNK)
        complete = True
    except Exception:
        complete = False
    t.seek(0)
    return t, complete


def iter_archive(fobj, name, depth):
    """Yield dicts for every regular file inside, recursing into nested archives."""
    if depth > MAX_DEPTH:
        return
    kind = archive_kind(name)
    try:
        if kind == "tar" or (kind == "gz" and is_tar(fobj)):
            fobj.seek(0)
            with tarfile.open(fileobj=fobj, mode="r:*") as tf:
                for m in tf:
                    if not m.isfile():
                        continue
                    sp, complete = spool(tf.extractfile(m))
                    digest, n, _ = sha256_stream(sp)
                    if complete and n == m.size:
                        fmt, st, chk, exp = assess(sp, m.name, n)
                        if st == "ok":
                            chk = chk + "+archive" if chk != "none" else "archive"
                    else:
                        fmt, _, chk, _ = assess(sp, m.name, n)
                        st, chk, exp = "truncated", "archive-member", str(m.size)
                    yield dict(member=m.name, size=n, mtime=iso(m.mtime), sha256=digest,
                               status=st, check=chk, expected_size=exp, format=fmt)
                    if st == "truncated":
                        log("  [truncated] %s :: %s  %d of %d bytes" % (name, m.name, n, m.size))
                        return  # stream is broken past here
                    if archive_kind(m.name):
                        sp.seek(0)
                        for d in iter_archive(sp, m.name, depth + 1):
                            d["member"] = m.name + SEP + d["member"]
                            yield d
        elif kind == "zip":
            with zipfile.ZipFile(fobj) as zf:
                for zi in zf.infolist():
                    if zi.is_dir():
                        continue
                    t = "%04d-%02d-%02dT%02d:%02d:%02d" % zi.date_time
                    try:
                        with zf.open(zi) as ef:
                            sp, complete = spool(ef)
                        digest, n, _ = sha256_stream(sp)
                        fmt, st, chk, exp = assess(sp, zi.filename, n)
                        if not complete:
                            st, chk, exp = "truncated", "archive-member", str(zi.file_size)
                    except Exception:
                        digest, n, fmt, st, chk, exp = "", 0, "", "unreadable", "archive-member", str(zi.file_size)
                    yield dict(member=zi.filename, size=n, mtime=t, sha256=digest, status=st,
                               check=chk, expected_size=exp, format=fmt)
                    if st == "ok" and archive_kind(zi.filename):
                        sp.seek(0)
                        for d in iter_archive(sp, zi.filename, depth + 1):
                            d["member"] = zi.filename + SEP + d["member"]
                            yield d
        elif kind in ("gz", "bz2", "xz"):
            opener = {"gz": gzip.GzipFile, "bz2": bz2.BZ2File, "xz": lzma.LZMAFile}[kind]
            inner = os.path.basename(name)[: -(len(kind) + 1)] or "content"
            fobj.seek(0)
            sp, complete = spool(opener(fileobj=fobj))
            digest, n, _ = sha256_stream(sp)
            fmt, st, chk, exp = assess(sp, inner, n)
            if not complete:
                st, chk = "truncated", "compressed-stream"
            yield dict(member=inner, size=n, mtime="", sha256=digest, status=st, check=chk,
                       expected_size=exp, format=fmt)
    except Exception as e:
        log("  [warn] could not read archive %s: %s" % (name, e))


# ------------------------------------------------------------------ git

def is_git_repo(d):
    return os.path.exists(os.path.join(d, ".git")) or \
        all(os.path.exists(os.path.join(d, x)) for x in ("HEAD", "objects", "refs"))


def git(repo, *args, **kw):
    return subprocess.run(["git", "-C", repo] + list(args), stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, check=True, **kw).stdout


def iter_git_blobs(repo):
    try:
        out = git(repo, "rev-list", "--all", "--reflog", "--objects")
    except Exception as e:
        log("  [warn] git rev-list failed in %s: %s" % (repo, e))
        return
    paths = {}
    for line in out.decode("utf-8", "replace").splitlines():
        parts = line.split(" ", 1)
        if len(parts) == 2 and parts[1]:
            paths.setdefault(parts[0], set()).add(parts[1])
    try:
        raw = git(repo, "log", "--all", "--reflog", "--raw", "--no-abbrev", "--no-renames",
                  "--root", "-c", "--format=").decode("utf-8", "replace")
        for line in raw.splitlines():
            if line.startswith(":") and "\t" in line:
                meta, path = line.split("\t", 1)
                oid = meta.split()[-2]
                if oid in paths:
                    paths[oid].add(path.split("\t")[-1])
    except Exception:
        pass
    if not paths:
        return
    chk = git(repo, "cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)",
              input=("\n".join(paths) + "\n").encode()).decode().splitlines()
    blobs = [l.split()[0] for l in chk if l.split()[1:2] == ["blob"]]
    for oid in blobs:
        data = git(repo, "cat-file", "blob", oid)
        digest = hashlib.sha256(data).hexdigest()
        for path in sorted(paths[oid]):
            fmt, st, chk_, exp = assess(io.BytesIO(data), path, len(data))
            yield dict(path=path, oid=oid, size=len(data), sha256=digest, format=fmt,
                       status=st, check=chk_, expected_size=exp)


def git_describe(repo):
    info = {}
    for k, args in (("remote", ["config", "--get", "remote.origin.url"]),
                    ("commits", ["rev-list", "--all", "--count"])):
        try:
            info[k] = git(repo, *args).decode().strip()
        except Exception:
            info[k] = ""
    return info


# ------------------------------------------------------------------ scan

def scan(roots, machine, as_spec=None, no_git=False, no_archives=False, exclude=(), no_mtime=False):
    import fnmatch
    rows = []

    def add(**kw):
        kw.setdefault("seen", TODAY)
        if no_mtime:
            kw["mtime"] = ""
        kw.setdefault("machine", machine)
        rows.append(kw)

    for root in roots:
        aroot = os.path.abspath(root)
        base = os.path.dirname(aroot) if os.path.isfile(aroot) else aroot
        if as_spec:
            m, vol, rec_root = as_spec.split(":", 2)
            loc = dict(machine=m, volume=vol, root=rec_root)
        else:
            loc = dict(machine=machine, volume=tilde(mount_point(base)), root=tilde(base))
        log("harvest %s  (as %s:%s:%s)" % (aroot, loc["machine"], loc["volume"], loc["root"]))

        def do_file(full, rel):
            try:
                st = os.stat(full)
                with open(full, "rb") as f:
                    digest, n, _ = sha256_stream(f)
                fmt, status, chk, exp = assess(full, full, n)
            except Exception as e:
                log("  [warn] %s: %s" % (full, e))
                return
            add(sha256=digest, size=n, status=status, check=chk, expected_size=exp, format=fmt,
                kind="file", relpath=rel, member="", mtime=iso(st.st_mtime), **loc)
            if not no_archives and (archive_kind(full) or fmt in ("tar", "gzip", "zip", "bzip2", "xz")):
                name = full if archive_kind(full) else full + {"tar": ".tar", "gzip": ".gz", "zip": ".zip",
                                                             "bzip2": ".bz2", "xz": ".xz"}.get(fmt, "")
                with open(full, "rb") as f:
                    for d in iter_archive(f, name, 1):
                        add(kind="archive-member", relpath=rel, **dict(d, **loc))

        def do_git(repo, rel):
            info = git_describe(repo)
            log("  git %s  remote=%s commits=%s" % (rel or ".", info["remote"], info["commits"]))
            for d in iter_git_blobs(repo):
                add(sha256=d["sha256"], size=d["size"], status=d["status"], check=d["check"],
                    expected_size=d["expected_size"], format=d["format"], kind="git-blob",
                    relpath=rel, member=d["path"] + "@" + d["oid"][:12], mtime="", **loc)

        if os.path.isfile(aroot):
            do_file(aroot, os.path.basename(aroot))
            continue
        for dp, dns, fns in os.walk(aroot):
            rel_dp = os.path.relpath(dp, aroot)
            rel_dp = "" if rel_dp == "." else rel_dp
            bare = all(os.path.exists(os.path.join(dp, x)) for x in ("HEAD", "objects", "refs"))
            if is_git_repo(dp) and not no_git:
                do_git(dp, rel_dp)
            if bare:
                dns[:] = []
                continue
            dns[:] = sorted(d for d in dns if d not in SKIP_DIRS)
            dns[:] = [d for d in dns if not any(fnmatch.fnmatch(os.path.join(rel_dp, d) if rel_dp else d, x.rstrip("/*"))
                                                for x in exclude)]
            for fn in sorted(fns):
                full = os.path.join(dp, fn)
                rel = os.path.join(rel_dp, fn) if rel_dp else fn
                if fn in SKIP_FILES or os.path.islink(full) or any(fnmatch.fnmatch(rel, x) for x in exclude):
                    continue
                do_file(full, rel)
    return rows


# ------------------------------------------------------------------ classify vs manifest

def read_csv_any(src):
    if not src:
        return []
    if src.startswith(("http://", "https://")):
        data = urlopen(src).read().decode("utf-8")
        return list(csv.DictReader(io.StringIO(data)))
    if not os.path.exists(src):
        log("  (no %s; classifying everything as new)" % src)
        return []
    with open(src, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def loc_key(r):
    return (r.get("machine", ""), r.get("volume", ""), r.get("root", ""), r.get("relpath", ""), r.get("member", ""))


def classify(rows, manifest, missing, sightings):
    known = {m["sha256"] for m in manifest}
    seen_at = {loc_key(s) + (s["sha256"],) for s in sightings}
    miss_paths = [m["path"] for m in missing]
    for r in rows:
        full = r["relpath"] + ("/" + r["member"].split("@")[0].replace(SEP, "/") if r["member"] else "")
        full = full.replace("\\", "/")
        hit = [p for p in miss_paths if full == p or full.endswith("/" + p)]
        if not hit:
            base = os.path.basename(full)
            hit = [p for p in miss_paths if os.path.basename(p) == base and len(base) >= 12
                   and not base.lower().startswith("readme")]
        if r["sha256"] not in known:
            r["delta"] = "missing-match" if hit else "new"
        elif loc_key(r) + (r["sha256"],) not in seen_at:
            r["delta"] = "new-location"
        else:
            r["delta"] = "known"
    return rows


def report(rows, out):
    def p(*a):
        print(*a, file=out)
    by = {}
    for r in rows:
        by.setdefault(r["delta"], []).append(r)
    bad = [r for r in rows if r["status"] != "ok"]
    p("# harvest %s  %d rows, %d distinct contents" % (TODAY, len(rows), len({r["sha256"] for r in rows})))
    for k in ("missing-match", "new", "new-location", "known"):
        rs = by.get(k, [])
        p("%-14s %5d rows  %5d distinct" % (k, len(rs), len({r["sha256"] for r in rs})))
    p("not ok         %5d rows" % len(bad))
    for title, rs in (("MISSING-MATCH (check against fingerprints/)", by.get("missing-match", [])),
                      ("NEW content", by.get("new", [])), ("NOT OK", bad)):
        if not rs:
            continue
        p("\n## " + title)
        done = set()
        for r in sorted(rs, key=lambda r: (r["relpath"], r["member"])):
            if (r["sha256"], title) in done:
                continue
            done.add((r["sha256"], title))
            where = r["relpath"] + (" :: " + r["member"] if r["member"] else "")
            extra = "" if r["status"] == "ok" else "  [%s %s/%s]" % (r["status"], r["size"], r["expected_size"] or "?")
            p("  %s %12s %-13s %s%s" % (r["sha256"][:12], r["size"], r["format"], where, extra))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("roots", nargs="+")
    ap.add_argument("-o", "--out", default="delta-%s-%s.csv" % (socket.gethostname().split(".")[0], TODAY))
    ap.add_argument("--manifest", help="manifest.csv path or URL")
    ap.add_argument("--missing", help="missing.csv path or URL")
    ap.add_argument("--sightings", help="sightings.csv path or URL (to tell new-location from known)")
    ap.add_argument("--machine", default=socket.gethostname().split(".")[0])
    ap.add_argument("--as", dest="as_spec", help="record roots as MACHINE:VOLUME:ROOT (e.g. github:release/v0.0.10:weird.tar.gz)")
    ap.add_argument("--no-git", action="store_true")
    ap.add_argument("--no-archives", action="store_true")
    ap.add_argument("--exclude", action="append", default=[], help="relative path glob to skip (repeatable)")
    ap.add_argument("--no-mtime", action="store_true", help="don't record mtimes (e.g. for copies)")
    a = ap.parse_args(argv)
    rows = scan(a.roots, a.machine, a.as_spec, a.no_git, a.no_archives, a.exclude, a.no_mtime)
    rows = classify(rows, read_csv_any(a.manifest), read_csv_any(a.missing), read_csv_any(a.sightings))
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    with open(os.path.splitext(a.out)[0] + ".txt", "w", encoding="utf-8") as f:
        report(rows, f)
    report(rows, sys.stderr)
    log("\nwrote %s (+ .txt). Merge with: python3 tools/curate.py merge %s" % (a.out, a.out))


if __name__ == "__main__":
    main()
