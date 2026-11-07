# Old AVISO geostrophic velocity grid: Mercator rows labelled as latitude, stored lon-major

A 2006 SSALTO/DUACS delayed-time geostrophic velocity file (U and V for 1992-10-14). Its latitude axis is regular in spherical Mercator y, not in latitude. The data are stored (lon, lat), and the only grid metadata (a "south/west corner" and a 1/3 degree "step") looks like a regular lon/lat grid. Build a regular latitude axis from the end points and rows land up to 19.5 degrees of latitude from where they belong.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/dt_ref_global_merged_madt_uv_19921014_19921014_20060315.nc | d7dcc72ce30b | 7923224 |
| extdata/rectlinear/readme_rectlinear.txt~febe778e | febe778e5550 | 135 |

## What's wrong

- `NbLatitudes` (915 values, -82.0 to 81.9746) has a step of 0.0465 degrees near the poles and 0.333 at the equator. In spherical Mercator y, `ln(tan(pi/4 + lat/2))`, the step is a constant 1/3 degree, the same as the longitude step. Global attribute `FileType = "GRID_DOTS_MERCATOR"` is the only hint.
- `LatLonMin = (-82, 0)` and `LatLonStep = (1/3, 1/3)` invite a regular lon/lat reading. If the rows are spread evenly between the end latitudes, the true 60.06 N row lands at 40.71 N. The worst error is 19.5 degrees, near 57 S.
- `Grid_0001(NbLongitudes, NbLatitudes)`: longitude is the slow dimension. GDAL's classic view is 915 x 1080 (latitude across), with no geotransform and no CRS.
- Latitude ascends; longitude runs 0 to 359.67.
- The grid is spherical Mercator. Ellipsoidal Mercator (EPSG:3395) gives a row spacing that varies by 0.7%. Still open: whether the coordinates are cell centres or edges. The recipe assumes centres.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```
gdalmdimtranslate dt_ref_global_merged_madt_uv_19921014_19921014_20060315.nc u.tif \
  -array "name=Grid_0001,transpose=[1,0],view=[::-1,:]"
gdal_translate u.tif u_merc.tif -a_srs "+proj=merc +R=6378137 +units=m +no_defs" \
  -a_ullr -18553.2485 16966094.5000 40056463.4371 -16986350.1920
gdalwarp -t_srs "+proj=longlat +R=6378137" -r near u_merc.tif u_ll.tif
```

The cell size is R * radians(1/3) = 37106.4969 m. The extent is half a cell beyond the outer coordinates: x for longitudes 0 and 359.667, Mercator y for latitudes -82 and 81.9746. 2000 random stored (lon, lat) pairs each fell in a u_merc.tif cell holding the matching value. Use `name=Grid_0002` for V.

## History

- The file was first listed 2018-10-04, in commit "EURO-CORDEX_81_DOMAIN000 example for stars", which added several files to the list at once.
- The bytes were committed to data-raw/ on 2024-05-13 as "the real actual file". That was 16 minutes after a commit titled "old MERCATOR AVISO", which actually added `dt_global_allsat_phy_l4_19930101_20190101.nc`. That file is the modern CMEMS product on a regular 0.25 degree lon/lat grid (checked), so it is not part of this case.
- The earliest readme in the rectlinear/ folder (in a v0.0.6 release tarball) lists this file under "rectlinear". Later versions add "Mercator grid from Aviso (deprecated by Copernicus now)".

## Links

- Same Mercator grid, Southern Ocean subset: `cases/acc-fronts-mercator`
