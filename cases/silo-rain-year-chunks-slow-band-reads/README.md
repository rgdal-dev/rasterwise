# SILO daily rain: chunks span the whole year, so GDAL reads the full file once per band

A SILO annual daily rainfall file (Australia, 0.05 degree, 365 days) whose
netCDF-4 chunks are (365, 30, 50): each chunk holds the whole year for a
small tile. GDAL reads one day (band) at a time, and each band read pulls in
every chunk whole, so converting to GeoTIFF reads the 428 MB file 365
times. In 2019 that took about 40 minutes. The workaround tried then
(reordering dimensions) gives a file GDAL misreads.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/nc-to-cog/1889.daily_rain.nc | ba6453ee9460 | 428217080 |
| extdata/nc-to-cog/llt.nc | 030cf5d72045 | 428203293 |
| extdata/nc-to-cog/out.tif | 5049578e7197 | 48752606 |
| extdata/nc-to-cog/out.tif.aux.xml | 98ce7d30850e | 138234 |

Lost: `nc-to-cog/nc-to-cog-readme.R`.

## What's wrong

- `daily_rain(time=365, lat=681, lon=841)` int16, scale 0.1, lat ascending;
  `_ChunkSizes = 365, 30, 50`, uncompressed.
- Measured with GDAL 3.14 / netCDF 4.9.2 (2026-11-06): reading 10 bands
  read 4.28 GB, i.e. the whole variable per band. The chunk shape, not
  dimension order by itself, causes this.
- The issue's command now takes 26 s here, since the file is in the page
  cache. The 2019 figure fits 365 cold re-reads (inference).
- `llt.nc` (from `ncpdq -a lon,lat,time`) is `daily_rain(lon, lat, time)`;
  GDAL 3.14 reads it as 365 x 681 with 841 bands. Wrong axes.

**Evidence vs inference.** `1889.daily_rain.nc` matches the listed file by
header fingerprint. `llt.nc`'s history attribute records the issue's ncpdq
and ncks commands. `out.tif` (841 x 681 x 365, LZW, EPSG:4283) is
band-for-band identical to a fresh run of the issue's first command, so it
was made from `1889.daily_rain.nc`. That it is the output of the slow 2019
run is inferred from its mtime (50 minutes after `llt.nc`).

## How to read it

The plain command is correct (verified, GDAL 3.14.0dev, 2026-11-06):

```
gdal_translate 1889.daily_rain.nc out.tif -co TILED=YES -co COMPRESS=LZW \
  -co INTERLEAVE=BAND -unscale -ot Float32 -a_srs EPSG:4283
```

To read the file once, read `daily_rain` in one call with the
multidimensional API and write bands from memory (snippet in case.yaml;
verified: 437 MB read, 5.5 s, output identical to `out.tif`). Do not
reorder dimensions for GDAL. Rechunking should help too (untested).

## History

- 2019-05-15: issues/007.md "the slow nc to geotiff thing" opened; commit
  40d3bbe "more nc goodness" listed `nc-to-cog/1889.daily_rain.nc` and
  `nc-to-cog/nc-to-cog-readme.R`.
- Working-folder mtimes, 2019-05-15 UTC: 1889.daily_rain.nc 14:12, llt.nc
  14:22, out.tif 15:11.

## Links

- issues/007.md
- https://s3-ap-southeast-2.amazonaws.com/silo-open-data/annual/daily_rain/1889.daily_rain.nc
  (source URL from the issue; not re-fetched)
