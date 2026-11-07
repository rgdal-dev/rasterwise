# ACC frontal indices on the AVISO Mercator grid, with a duplicated seam and no time coordinate

Weekly Antarctic Circumpolar Current front classes (0..12) from CSIRO, 1992-10-14 to 2009-02-18, on the Southern Ocean rows of the old AVISO Mercator grid (see `cases/aviso-mercator-as-lonlat`). It shares that file's Mercator-spaced latitude. It also repeats the 0/360 seam column and has no time coordinate. And in the current GDAL classic raster API, its NaN cells read as 0, which is also a valid class.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/rectilinear/ACCfronts_nc4.nc | bec3c3cf8baa | 20408989 |
| extdata/rectilinear/readme_rectlinear.txt | 611d8dce5af2 | 719 |
| extdata/rectlinear/readme_rectlinear.txt | 230514509f27 | 324 |

## What's wrong

- `lat` (363 values, -82 to -30.25) is regular in spherical Mercator y at 1/3 degree. It matches the first 363 AVISO latitudes to 4e-6 degrees. Latitude ascends.
- `lon` is 0..360 inclusive (1081 values). The first and last columns are the same meridian and hold identical data.
- There is no `time` variable, only float `year`, `month` and `day` (7-day steps). GDAL warns "Several 1D variables are indexed by dimension time".
- `front:units = "valid range from 0 to 12"`. There is no `_FillValue`, and cells without a class are stored as NaN.
- GDAL 3.14.0dev classic API (`gdal.Open`, `gdal_translate`, `gdallocationinfo`) returns **0** at the stored-NaN cells and reports no nodata, so 238070 empty cells merge with class 0 (549 real cells at time 1). The multidimensional API, ncks and h5dump give NaN. Why this happens is not yet known.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07, on the first three weeks:

```
gdalmdimtranslate ACCfronts_nc4.nc fronts.tif -array "name=front,view=[:,::-1,0:1080]"
gdal_translate fronts.tif fronts_merc.tif -a_nodata nan \
  -a_srs "+proj=merc +R=6378137 +units=m +no_defs" \
  -a_ullr -18553.2485 -3516691.8060 40056463.4371 -16986350.1920
```

This keeps the NaN, drops the repeated 360 column and flips to north-up. 3000 random stored (lon, lat) pairs each fell in a cell with the matching value. Band k is week k; build dates from `year`/`month`/`day`. Reading is slow: deflate level 9, with chunks spanning 122 time steps.

## History

- Listed as `rectlinear/ACCfronts_nc4.nc` (misspelt folder) from 2018-10-15, and as `rectilinear/ACCfronts_nc4.nc` from 2018-10-19 (commit "data to match the mask").
- The readme (first listed 2019-03-21, commit "mrso and GPP examples") records how the file was made: `nccopy -d 9 -k nc7` from a 1 GB original, "also a Mercator grid".

## Links

- `cases/aviso-mercator-as-lonlat`
