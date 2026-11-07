# GFDL CM2.1 ocean: 1D lon/lat axes are nominal; true positions are 2D (tripolar north of 65N)

A CM2.1 ocean region-mask file gives both nominal 1D axes and the true 2D cell positions. A CM2.1 SST file on the same grid carries 1D `xt`/`yt` that match neither. The 1D axes are right south of 65N and wrong in the tripolar Arctic, by up to 24 degrees of latitude. GDAL's default read of the SST uses its 1D axes. To place the SST correctly, use the mask file's `geolon_t`/`geolat_t` as geolocation arrays.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/rectilinear/CM2.1_regionmask.nc | 10b6eb4ff393 | 1733764 |
| extdata/rectilinear/readme_CM2.1regionmask.txt | 6110fe067b57 | 459 |
| extdata/rectilinear/test_3_.nc | 83f2a77cc9f3 | 583584 |

## What's wrong

- `CM2.1_regionmask.nc` has T and C grids (C offset +0.5 degree in lon and lat), each 360 x 200. `gridlon_t` is -279.5..79.5 (below -180). `gridlat_t` is irregular: 1 degree near the poles, 1/3 degree near the equator.
- `geolon_t`/`geolat_t` equal the 1D axes up to row 174. From `gridlat_t` = 65.5N northward they differ by up to 24.3 degrees in lat and 67.6 in lon, which fits a tripolar Arctic.
- `tmask`/`umask` hold region codes 0..10.
- In `test_3_.nc` (SST, 2 time steps), `xt` steps vary from 0.96 to 1.59 degrees. `yt` flattens north of 65N and stops at 78.78N, while the true grid reaches 89.49N. Both are close to row/column means of the 2D positions; how they were made is not recorded. The SST land mask matches `tmask == 0` in 99.95% of cells.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```
gdal_translate -of VRT NETCDF:test_3_.nc:SST sst.vrt
# edit the GEOLOCATION metadata in sst.vrt:
#   X_DATASET -> NETCDF:"CM2.1_regionmask.nc":geolon_t
#   Y_DATASET -> NETCDF:"CM2.1_regionmask.nc":geolat_t
gdalwarp -geoloc -t_srs EPSG:4326 -te -280 -90 80 90 -tr 0.25 0.25 -r near sst.vrt sst_ll.tif
```

Each SST cell's value was looked up at its true position in the output. All 14574 sampled ocean cells south of 65N matched. In the tripolar region 94% matched; the rest were overwritten by neighbours at 0.25 degrees. Output longitudes follow `geolon_t`; shift by 360 if needed.

## History

- `CM2.1_regionmask.nc` was first listed 2018-10-19, under `rectlinear/` and `rectilinear/`. `test_3_.nc` was first listed the same day. Both came in commit "data to match the mask".
- The readme (first listed 2019-03-21) points to a comment on stars issue 65. It describes the mask as "regular in longitude but non regular in latitude", with an Arakawa staggered grid. It calls `test_3_.nc` "ostensibly related".

## Links

- https://github.com/r-spatial/stars/issues/65
