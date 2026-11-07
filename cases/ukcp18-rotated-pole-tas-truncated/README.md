# UKCP18 12 km rotated-pole tas: full file lost, only 48 MiB truncated copies survive

A UKCP18 regional climate model monthly temperature file (12 km, RCP8.5,
1980-2080) on a rotated-pole grid, with a length-1 ensemble dimension in
front. It was listed with a note about its dimensions. The full 815 MB file
is gone: the v0.5.0 release tarball was cut off during upload, and every
surviving copy stops at about 50 MB. Its header survives as a fingerprint.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/ceda/ceda_dims.readme | 86d3b131192a | 47 |
| extdata/ceda/tas_rcp85_land-rcm_eur_12km_01_mon_198012-208011.nc | 4cea951df213 | 50887168 (truncated) |
| extdata/ceda/tas_rcp85_land-rcm_eur_12km_01_mon_198012-208011.nc~d0d99954 | d0d999549f6b | 50331648 (truncated) |

Lost: `ceda/tas_rcp85_land-rcm_eur_12km_01_mon_198012-208011.nc`
(814,764,140 bytes per the tar header).

## What's wrong

- **Truncation.** The tar member is exactly 48 MiB (v0.5.0 release and
  three local tarball copies). A loose partial copy in one working tree is
  50,887,168 bytes; it is larger than the tar member, and its origin is
  not known. storecard's first pass could not open it (HDF
  error). Not re-checked here; the bytes are on another machine.
- **Dimensions** (from
  `fingerprints/ceda/tas_rcp85_land-rcm_eur_12km_01_mon_198012-208011.nc.cdl`):
  `tas(ensemble_member=1, time=1200, grid_latitude=406, grid_longitude=418)`;
  `rotated_latitude_longitude` grid mapping (pole lat 39.25, lon 198,
  sphere 6371229 m); time in hours since 1970 with a `360_day` calendar;
  char auxiliary coordinates `ensemble_member_id`, `yyyymm`.
- The data size (1200 x 406 x 418 float32 = 814,598,400 bytes) is close to
  the file size, so it was stored uncompressed (inference).
- **Not determined:** what `ceda_dims.readme` said (text not available
  here), and so which of these features the case was about.

## How to read it

Untested; there are no complete bytes. For a fresh copy: expect 1200 bands
in GDAL, drop the length-1 member, decode time as 360_day, and check that
the rotated-pole CRS matches the parameters above.

## History

- 2019-05-03, commit f42768e "ceda": file and readme first listed.
- Release v0.5.0 weird.tar.gz carries the truncated 48 MiB member; the
  readme member is intact (47 bytes).
- Header fingerprint kept in `fingerprints/ceda/`.

## Links

- https://ukclimateprojections.metoffice.gov.uk (from the file's
  `references` attribute)
