# CORDEX EUR-44 rotated-pole grids, and a GeoTIFF that labels rotated coordinates as WGS84

Two CF-compliant rotated-pole regional climate files (EUR-44 tas), and `out.tif`, a GeoTIFF copy of the first with the same values and the same rotated-degree geotransform, tagged EPSG:4326. Current GDAL reads the netCDF files correctly. `out.tif` shows what happens when rotated coordinates are treated as longitude/latitude: Europe moves to the tropical Atlantic.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/ob_tran/example_ob_tran.nc | 9e5bac9b6135 | 520774 |
| extdata/ob_tran/example_ob_tran2.nc | 4e94d7b897c9 | 255551 |
| extdata/ob_tran/out.tif | e3f71e978fee | 49758 |
| extdata/ob_tran/readme.txt | 446b80ff3b41 | 69 |

## What's wrong

- Both netCDF files have 1D `rlon`/`rlat` (0.44 degree) and a `rotated_latitude_longitude` grid mapping (pole 39.25N, -162E), plus 2D `lon`/`lat`. GDAL 3.14.0dev turns the grid mapping into a rotated-pole CRS. The cell centres it implies match the stored 2D lon/lat to 8e-6 degrees, so the 2D arrays are derived.
- `out.tif`: values identical to `example_ob_tran.nc`, extent -28.43..18.21 x -23.43..21.89 (rotated degrees), CRS EPSG:4326. Read as is, the data sit at 28W-18E, 23S-22N. How it was made is not recorded.
- When GDAL 3.14.0dev writes a GeoTIFF from these files, the rotated-pole CRS goes only into a `.aux.xml` sidecar. The .tif alone has no CRS.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```
gdalwarp -t_srs EPSG:4326 -tr 0.25 0.25 -r near NETCDF:"example_ob_tran.nc":tas tas_ll.tif
```

All 2756 sampled cells held the matching value at their stored lon/lat. To repair `out.tif` (also run and checked; keep the sidecar it writes):

```
gdal_translate -a_srs "+proj=ob_tran +o_proj=longlat +o_lon_p=0 +o_lat_p=39.25 +lon_0=18 +datum=WGS84" out.tif fixed.tif
```

## History

- The two netCDF files were first listed 2018-10-15, commit "ob_tran from stars #52". The folder was also called `ob_trans/` in the v0.0.8 release.
- `out.tif` and `readme.txt` were first listed 2019-03-21. The readme holds only a link to a comment on stars issue 52; the content of that issue is not archived here.

## Links

- https://github.com/r-spatial/stars/issues/52
