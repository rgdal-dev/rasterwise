# R raster writeRaster output: generic z layer dimension and CRS only in a global attribute

A 14-layer, 0.25 degree lon/lat grid south and east of Tasmania, written
by the R raster package. Nothing in the record says why it was collected.
Checks found it reads correctly; the only awkward points are a layer
dimension `z` with units "unknown" and a CRS kept only as a PROJ.4 string in
a global attribute. Status: open.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/file.nc | aee348002973 | 244060 |

## What's wrong

Not determined. What was checked:

- `variable(z, latitude, longitude)`, 14 x 72 x 60, fill -3.4e+38, no units.
- lon 140.125..154.875, lat -38.125..-55.875 (descending), regular 0.25;
  GDAL's geotransform and orientation are correct; missing cells are land.
- `z` = 1..14, units "unknown"; GDAL warns it is not a time or vertical
  dimension.
- CRS only as global `crs` / `crs_format = "PROJ.4"`; GDAL assigns no CRS.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```
gdal_translate -oo ASSUME_LONGLAT=YES file.nc file.tif
```

## History

- 2018-08-30: file created (date attribute; created_by "R, packages ncdf4
  and raster (version 2.6-7)").
- 2018-10-04: listed in the first weirdlist.txt (commit 65a62da,
  "EURO-CORDEX_81_DOMAIN000 example for stars"; that commit created the
  12-file list, so its message is not about this file).

## Links

- fingerprints/file.nc.cdl
