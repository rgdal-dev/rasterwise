# rasterwise

An archive of problem files and the lessons attached to them: gridded data
(mostly netCDF and HDF, some GeoTIFF) that broke readers or misled them, with
a written account of what is wrong and how to read each one correctly.

It began in 2018 as a bundle of awkward files used to test R packages
(stars, tidync, ncmeta, raster). Those "how do I map this file?" moments now
make a corpus of what data storage has done well and badly over the years.
This repo is the long-term home for that corpus. It stands alone, and other
projects read it (storecard, for example, builds metadata cards keyed to
this manifest). Nothing downstream writes to it.

## What is here

| path | what |
|---|---|
| `manifest.csv` | one row per file, keyed by sha256 (see below) |
| `missing.csv` | files known to have existed, with no intact bytes found yet |
| `sightings.csv` | every place each file has been seen: machine, volume, path, date (append-only) |
| `cases/<slug>/` | one lesson per case: `case.yaml` (structured) + `README.md` (prose) |
| `issues/` | this repo's GitHub issues, archived as markdown |
| `fingerprints/` | `ncdump -h` headers of 50 files, recovered from the old generated README; used to recognise lost files when they turn up |
| `ledger/` | the old file lists (`listed.csv`), confirmed aliases, and known working folders |
| `tools/` | harvest and curation scripts, Python standard library only |

There are no data files in git. The bytes live in content-addressed storage
(`files/<sha256[0:2]>/<sha256>`); `manifest.csv` says where to fetch each one.

## Identity

A file's identity is its sha256. A path is just a name, and one file can have
several (`aliases`). A case is identified by its slug. Slugs are permanent:
they are never renamed or reused, and a retired case is marked
`retired: true`, not deleted.

## manifest.csv

| column | |
|---|---|
| `sha256` | identity |
| `size` | bytes |
| `canonical_path` | the file's name, relative to a rasterwise working tree (e.g. `extdata/swapped/3A-DAY.nc`). Fixed once assigned. |
| `aliases` | other names it has been seen under, `;`-separated |
| `case` | slug(s) of the cases that use it, from `cases/*/case.yaml` |
| `format` | sniffed from the bytes: `netcdf3`, `netcdf4/hdf5`, `hdf4`, `geotiff`, `tiff`, `zip`, `grib`, `vrt`, `script`, `text`; empty if the bytes have not been sniffed |
| `status` | `ok`, `truncated` (shorter than its own header or archive entry says), or `unreadable` (no known format matches the bytes, e.g. text named `.nc`). A file in a known format under the wrong extension is `ok`: readers such as GDAL identify files by content, and `sightings.csv` records `extension-mismatch` in its `check` column. |
| `sources` | every place it was seen, `machine:volume:root:path (date)`, `;`-separated |
| `url` | where the bytes can be fetched now. Set only after a verified download (see below). |
| `redistributable` | `yes`, `no` or `unknown` |
| `note` | free text |

`canonical_path`, `url`, `redistributable` and `note` are curated: rebuilding
keeps them. Everything else is generated from `sightings.csv` and the cases.
storecard depends on `sha256`, `canonical_path`, `case`, `format` and `url`,
and on the case slugs. Keep those stable.

## Getting the files

The blob store is not published yet, so `url` is empty for now. Until it is:

* The intact release bundles v0.0.6, v0.0.8, v0.0.10 and v0.0.12 are on this
  repo's GitHub releases (`weird.tar.gz`). Their members are in the manifest.
* The v0.5.0 bundle is **truncated** (32.7 MB of about 3 GB). Only three files come out
  of it, one of them cut short. The files only it held are listed in `missing.csv`.
* The files that were once committed under `data-raw/` are in git history.

To build a local blob store from whatever this machine has sightings of:

```sh
python3 tools/curate.py stage /path/to/store     # writes store/files/<aa>/<sha256>, re-hashed
```

Publishing a file: upload the blob, then

```sh
python3 tools/curate.py set-url <sha256> <url>   # downloads it, re-hashes, sets url only on a match
```

A file marked `redistributable=no` keeps its manifest row but gets no public url.

## Adding files, or checking another machine

`tools/harvest.py` is one self-contained file. Copy it anywhere with Python 3.6+:

```sh
python3 harvest.py ~/Git/rasterwise \
    --manifest manifest.csv --missing missing.csv --sightings sightings.csv
# the three tables may also be URLs (e.g. raw file URLs of this repo)
```

It hashes every file, every member of tar/zip/gz archives (nested too), and
every blob in the full history of any git repo it finds. It checks completeness
where the standard library can: the netCDF3 header, the HDF5 superblock, TIFF
strip/tile offsets, the zip directory and archive member lengths. It records
machine, volume, path and mtime for each file, and writes a delta
(`delta-<host>-<date>.csv` plus a `.txt` report) that classifies every row
as `new`, `new-location`, `known` or `missing-match`. It never edits the tables.

Bring the delta here, review it, and merge:

```sh
python3 tools/curate.py merge delta-<host>-<date>.csv   # appends sightings, rebuilds manifest + missing
python3 tools/curate.py check
git diff                                                # review, commit
```

For a `missing-match` (a file named like a lost one), compare its header
against the fingerprint before believing it:

```sh
python3 tools/readme_headers.py compare FILE fingerprints/<path>.cdl
```

If it matches under another name, record it in `ledger/aliases.csv` with the
evidence, then `python3 tools/curate.py build`.

What goes into the manifest (rather than only into sightings) is set by
`tools/scope.txt`.

## Adding a case

Create `cases/<slug>/case.yaml` and `cases/<slug>/README.md`. `case.yaml` uses
a strict YAML subset so the standard library can read it:

```yaml
id: aviso-mercator-as-lonlat
title: "One-line title"
status: open                 # open | understood | fixed-upstream
summary: "One line."
files:
  - <sha256>  # canonical_path
whats_wrong: |
  Prose.
how_to_read: |
  Prose or code (a VRT, a GDAL call, R or Python).
links:
  - "issues/013.md"
  - "https://github.com/r-spatial/stars/issues/62"
findings:                    # optional codes, e.g. LAT_MERCATOR_SPACED
  - LAT_MERCATOR_SPACED
missing:                     # optional: lost files from missing.csv this case is about
  - "chunking/wrfout_hist_prcp_2002-09-01.nc4"
```

Quote any scalar that contains `: ` or `#`. Then run `python3 tools/curate.py build`
to fill the manifest's `case` column, and `check`.

## Conventions

* No data files in git (`check` enforces this).
* Files are ASCII.
* Public text names repos and issues, not people.
* Refer to this repo's own issues by archive path (`issues/004.md`), not by a
  hosted URL: the repo has moved before and may again.

## History

2018-2019: files collected under `extdata/` and pushed as release tarballs with
R's piggyback; the generated README carried a `ncdump -h` of each file.
2024-2025: a few files committed directly under `data-raw/`. 2026-11: every
known copy (the release assets, git history, and working copies on three
machines) harvested, deduplicated by sha256, and restructured into this layout.
The earlier layout is in git history before that commit.
