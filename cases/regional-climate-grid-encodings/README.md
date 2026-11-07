# Three regional climate files, three grid encodings: 2D lon/lat only, rotated pole without 2D lon/lat, projected LAEA

Three example files sent to stars issue 62, each encoding its grid differently. The first has only 2D lon/lat and no CRS. The second has a CF rotated pole but no 2D lon/lat. The third is a projected LAEA grid that also carries 2D lon/lat. Current GDAL georeferences the second and third. The first has to be read through its 2D lon/lat as geolocation arrays.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/bad_examples_62/example1.nc | 6fc294f03328 | 153852 |
| extdata/bad_examples_62/example2.nc | 46f5e1cadb06 | 65952 |
| extdata/bad_examples_62/example3.nc | a7ac72b0d8db | 464473 |
| extdata/bad_examples_62/bad_examples.R | 86530e5b3447 | 717 |

## What's wrong

- **example1.nc** (PROMES, MED-44, 97 x 65) has no grid_mapping and no 1D coordinates, only 2D `lon`/`lat`. It is not on the MED-44 rotated grid. A fit I ran matches a spherical Lambert conformal conic (parallels 20/60, about 50 km cells) to 0.3 m, but the producer's projection is not recorded and the fit may not be unique.
- **example2.nc** (CCLM, MED-44, 98 x 63) has `rlon`/`rlat` with a `rotated_pole` mapping but no 2D lon/lat, and `pr` has no `_FillValue`. GDAL reads it correctly.
- **example3.nc** (EURO4M-APGD, 243 x 138, 5 km LAEA) is read correctly by GDAL. Its 2D lon/lat match the CRS to 4e-6 degrees.
- The reporter said one file "relies only on lat-lon arrays" (example1) and one has a projection "not formatted according to common practice". Which file that second remark meant is not recorded.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```
gdalwarp -geoloc -t_srs EPSG:4326 -tr 0.1 0.1 -r near example1.nc ex1_ll.tif
```

All 6305 cells of example1 held their own value at their stored lon/lat. Open example2 and example3 directly (`NETCDF:"example2.nc":pr`).

## History

- All four files were first listed 2018-10-04, commit "bad examples #62". The script records the stars issue comment they came from.

## Links

- https://github.com/r-spatial/stars/issues/62
