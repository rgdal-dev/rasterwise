# MESAN precipitation over Italy: a rotated-pole grid flattened to 2-D lon/lat by cdo

A one-day precipitation field whose native rotated lat/lon grid was
converted by `cdo -setgridtype,curvilinear` into 2-D lon/lat arrays only.
It looks curvilinear, but the lon/lat fit an exactly regular 0.05 degree
grid in a rotated pole, so it can be given a plain geotransform.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/hmr_ita.nc | cc8761e5b094 | 2440116 |

## What's wrong

- `pr(time, height, y, x)`, 1 x 1 x 248 x 223, with `lon(y, x)`,
  `lat(y, x)` and 4-corner bounds. No 1-D axes, no grid_mapping, no CRS.
- The history attribute records the cause: the GRIB source was read with
  `cdo -f nc cat -setgridtype,curvilinear`, then cut with
  `sellonlatbox,6.5,19,36,48`.
- Fit (checked): grid north pole at lon -165, lat 29; rotated lon
  -7.55..3.55 and rotated lat -25.0..-12.65 (cell centres), step 0.05;
  residual 2e-6 degrees.
- Rows are stored south to north; GDAL's default flip gives north-up.
- `pr` has no units and no fill attribute; GDAL invents nodata 9.96921e+36
  (not present). Values 0 to 51.4, none missing.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```
gdal_translate \
  -a_srs "+proj=ob_tran +o_proj=longlat +o_lon_p=0 +o_lat_p=29 +lon_0=15 +datum=WGS84 +no_defs" \
  -a_ullr -7.575 -12.625 3.575 -25.025 \
  NETCDF:hmr_ita.nc:pr pr_rotated.tif
```

Then `gdalwarp -t_srs EPSG:4326` if lon/lat output is wanted.

## History

- 2016-06-10: GRIB to netCDF with cdo setgridtype,curvilinear (history).
- 2018-07-11 and 2018-09-18: cdo subsetting and seltimestep,100 (history).
- 2018-10-04: listed in the first weirdlist.txt (commit 65a62da,
  "EURO-CORDEX_81_DOMAIN000 example for stars"; that commit created the
  12-file list, so its message is not about this file). Why it was added is
  not recorded.

## Links

- fingerprints/hmr_ita.nc.cdl
