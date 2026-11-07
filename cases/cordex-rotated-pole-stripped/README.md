# CORDEX EUR-11 file with the rotated-pole CRS and rlon/rlat stripped, leaving only 2D lon/lat

A DMI-HIRHAM5 EUR-11 precipitation field that has been through ncrcat and several cdo steps. It has lost its `rlon`/`rlat` axes and `rotated_pole` grid mapping, so only 2D `lon`/`lat` remain and readers see it as curvilinear. Its lon/lat are exactly the standard EUR-11 rotated grid, so the regular grid and CRS can be restored.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/get1index_64/test.nc | cfe075db7f20 | 3527924 |
| extdata/test.nc_60/num60.R | b9d6e8d15d5d | 61 |

## What's wrong

- Dims `x`/`y` (424 x 412) have no coordinate variables and there is no grid_mapping. GDAL 3.14.0dev gives no geotransform or CRS, only geolocation arrays.
- In the rotated system (pole 39.25N, -162E), `lon`/`lat` form the regular grid rlon = -28.375 + 0.11 i, rlat = -23.375 + 0.11 j, to 5e-6 degrees.
- `pr:units` still says kg m-2 s-1 after `cdo mulc,86400` in the history. The values (mean 2.84, max 92.6) look like mm/day.
- The history doesn't show which step dropped the CRS.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```
gdal_translate -a_srs "+proj=ob_tran +o_proj=longlat +o_lon_p=0 +o_lat_p=39.25 +lon_0=18 +datum=WGS84 +no_defs" \
  -a_ullr -28.43 21.89 18.21 -23.43 test.nc pr_rot.tif
```

Every cell centre matches the stored lon/lat to 6e-6 degrees, and the values equal the stored `pr`. The CRS is written to `pr_rot.tif.aux.xml`; keep it.

## History

- The same bytes were first listed 2018-10-04 as `test.nc_60/test.nc` (with `num60.R`, commit "EURO-CORDEX_81_DOMAIN000 example for stars"). They were listed again 2018-10-10 as `get1index_64/test.nc` (commit "stars #64").
- `num60.R` holds only `read_ncdf(.x)` and a link to stars issue 60. What issues 60 and 64 reported is not archived here.

## Links

- https://github.com/r-spatial/stars/issues/60
- https://github.com/r-spatial/stars/issues/64
- `cases/rotated-pole-as-lonlat`
