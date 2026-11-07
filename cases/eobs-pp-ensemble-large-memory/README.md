# E-OBS v19.0e sea-level pressure ensemble mean: 25202 daily grids, too big to read whole

A large-memory example: the E-OBS 0.25 degree daily sea-level pressure
ensemble mean, 1950 onward. Only the download script survives. The data
file is lost, but its header fingerprint gives the shape: about 4.7 GB as
packed int16, 9.4 GB as float32. Nothing records what went wrong with it.

| canonical_path | sha256 | size |
|---|---|---|
| data-raw/large-mem.R | 61cf44d9e374 | 219 |

Lost: `large-mem/pp_ens_mean_0.25deg_reg_v19.0e.nc` (header in
`fingerprints/large-mem/`).

## What's wrong

- `pp(time=25202, latitude=201, longitude=464)` short, scale 0.1 hPa,
  `_FillValue -9999`; days since 1950-01-01 (to 2018-12-31 if daily and
  contiguous).
- 2.35e9 values: 4.70 GB int16, 9.40 GB float32, 18.8 GB as doubles.
- The memory lesson is inferred from the commit message and folder name.
  The symptom, software and chunk layout are not recorded.

## How to read it

Untested (no bytes). Read subsets: `gdal_translate -b 1 -unscale -ot
Float32 file.nc day1.tif` for one day, or a window via xarray / the GDAL
multidimensional API. Check `ncdump -hs` for chunks spanning many time
steps (see silo-rain-year-chunks-slow-band-reads).

## History

- 2019-04-19, commit 8fb16b4 "ensemble large file" added
  `data-raw/large-mem.R`; the data path `large-mem/pp_ens_mean_0.25deg_reg_v19.0e.nc`
  was listed in weirdlist.txt from that date to 2020-01-29.
- 2026-11-06, commit fd09e23 removed the script from the tree.

## Links

- https://www.ecad.eu/download/ensembles/data/Grid_0.25deg_reg_ensemble/pp_ens_mean_0.25deg_reg_v19.0e.nc
  (from the script; not re-fetched)
