# RegCM domain file: proper LCC grid with two staggered 2D lon/lat sets (cross and dot points)

A RegCM 4.6.1 terrain/domain file for a 12 km EURO-CORDEX domain. It has a correct Lambert conformal conic grid (1D `jx`/`iy` plus a `crs` variable), which current GDAL georeferences. It also carries two sets of 2D lon/lat: "cross points" (cell centres) and "dot points" (corners, offset half a cell). If 2D coordinates are used at all, they must be the cross points.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/EURO-CORDEX_81_DOMAIN000_54/EURO-CORDEX_81_DOMAIN000.nc | 0ca0d4aa0124 | 44955316 |
| extdata/EURO-CORDEX_81_DOMAIN000_54/issue_54.R | 7f0316eeb1b1 | 522 |

## What's wrong

- Nothing is broken in the grid definition. LCC with parallels 30/65, origin 48N 9.75E, sphere R 6371229, false easting/northing -6000. `jx`/`iy` run -3174000..3174000 m at 12000 m.
- `xlon`/`xlat` project onto `jx`/`iy` to within 0.5 m. `dlon`/`dlat` project to `jx - 6000`, `iy - 6000` (south-west corners).
- `dlat` has `long_name` and `standard_name` swapped.
- The plain file opens in GDAL as subdatasets; choose a field such as `topo`.
- `issue_54.R` treats `topo` as curvilinear on `xlon`/`xlat`. That is correct, but it is not needed. What stars issue 54 reported is not archived here.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```
gdal_translate NETCDF:"EURO-CORDEX_81_DOMAIN000.nc":topo topo.tif
```

The result is an LCC GeoTIFF with origin (-3180000, 3180000) and 12000 m cells. GDAL's cell centres agree with `xlon`/`xlat` to float32 precision.

## History

- Both files first listed 2018-10-04, commit "EURO-CORDEX_81_DOMAIN000 example for stars". The folder suffix 54 is the stars issue number.

## Links

- https://github.com/r-spatial/stars/issues/54
