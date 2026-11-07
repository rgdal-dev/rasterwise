# NOAA snow cover CDR: a polar stereographic grid labelled latitude_longitude

The Northern Hemisphere snow cover extent CDR stores an 88 x 88 grid with
only 2-D latitude/longitude arrays, and its grid_mapping says
`latitude_longitude`. In fact it is an exact polar stereographic grid, and
the lon/lat arrays fit a simple geotransform to within rounding.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/nhsce_v01r01_19661004_20140203.nc | f43715f25daf | 19562536 |

## What's wrong

- `snow_cover_extent(time, rows, cols)`, 2470 weeks x 88 x 88, byte 0/1.
  No coordinate variables on rows/cols; `latitude(rows, cols)` and
  `longitude(rows, cols)` only.
- `coord_system:grid_mapping_name = "latitude_longitude"`, so GDAL reports
  WGS84 geographic with geolocation arrays and no geotransform.
- Fit (checked): polar stereographic north, lat_ts 60, lon_0 -80, WGS84
  ellipsoid. x and y are exactly affine in col and row: cell 190640.28 m,
  no rotation, max residual 12 m. A sphere leaves about 21 km of error.
  lat_ts cannot be fixed by the fit (it only rescales); 60 N is the usual
  value for this NMC-derived grid.
- Rows are stored top-down; GDAL assumes bottom-up and flips the data and
  the lon/lat arrays together.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07 (pixel centres reproduce the
file's lon/lat to 5e-5 degrees; Greenland is land, mid-Atlantic is water):

```
gdal_translate --config GDAL_NETCDF_BOTTOMUP NO \
  -a_srs "+proj=stere +lat_0=90 +lat_ts=60 +lon_0=-80 +ellps=WGS84 +units=m +no_defs" \
  -a_ullr -8388172.4 8388172.4 8388172.4 -8388172.4 \
  NETCDF:nhsce_v01r01_19661004_20140203.nc:snow_cover_extent sce.tif
```

## History

- 2014-02-05: file created (date_created attribute).
- 2018-10-04: listed in the first weirdlist.txt (commit 65a62da,
  "EURO-CORDEX_81_DOMAIN000 example for stars"; that commit created the
  12-file list, so its message is not about this file). Why it was added is
  not recorded.

## Links

- fingerprints/nhsce_v01r01_19661004_20140203.nc.cdl
