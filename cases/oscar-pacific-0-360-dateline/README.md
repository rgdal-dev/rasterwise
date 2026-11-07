# OSCAR tropical Pacific currents: a 0-360 grid that spans the antimeridian

A 1993 OSCAR surface current file (u, v and filtered uf, vf) on a 1 degree
tropical Pacific grid. Nothing in the record says why it was collected.
Checks found only mild awkwardness: longitudes 120.5 to 289.5 E that cross
the antimeridian, non-CF unit spellings, and no CRS. GDAL reads it
correctly. Status: open.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/oscar_gdr_5d1993.nc | 01bf16d9b390 | 13760564 |

## What's wrong

Not determined. What was checked:

- `u(time, depth, latitude, longitude)` is 72 x 1 x 70 x 170; missing is NaN.
- longitude 120.5..289.5 (0-360, crosses 180); latitude 34.5..-34.5
  (descending, north-up).
- Units "degree-N" / "degree-E". GDAL finds the geotransform anyway. It
  assigns no CRS, and a scratch copy with CF unit spellings got none either,
  so the units are not the reason.
- Time is not exactly regular: 67 steps of 5 days and 4 of 6 days.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```
gdal_translate -oo ASSUME_LONGLAT=YES NETCDF:oscar_gdr_5d1993.nc:u u.tif
gdalwarp -t_srs EPSG:4326 -te -180 -35 180 35 -tr 1 1 u.tif u_180.tif
```

Warp, don't relabel, if you need -180..180.

## History

- 2004-03-19: file date attribute.
- 2018-10-04: listed in the first weirdlist.txt (commit 65a62da,
  "EURO-CORDEX_81_DOMAIN000 example for stars"; that commit created the
  12-file list, so its message is not about this file).

## Links

- fingerprints/oscar_gdr_5d1993.nc.cdl
