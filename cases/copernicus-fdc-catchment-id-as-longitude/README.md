# C3S flow-duration indicators per catchment: SUBID codes labelled as longitude

Two Copernicus (C3S_441_Lot1_SMHI) river-flow indicator files on "remap215",
which is not a grid but a list of 35408 E-HYPE catchments (median 215 km2).
The catchment id coordinate is declared as longitude in degrees on the X
axis, so CF-trusting readers see a 1D "longitude" line with values in the
millions. Read it as a table keyed by catchment id.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/copernicus/cout-perc1_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap215.nc | 077840ba933a | 857364 |
| extdata/copernicus/cout-perc5_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap215.nc | d491c7b26d01 | 857364 |

## What's wrong

- `id(id)`, 35408 values: `standard_name = "longitude"`, `units =
  "degrees"`, `axis = "X"`, `long_name = "SUBID"`. Values are unique
  integers 8000001..9791075, unsorted. Both files carry the same ids.
- `spatial_resolution = "Irregular catchment polygons, median
  catchmentsize 215 km2."` The polygons are not in the file.
- `variable1..variable4(time, id)`, one per ensemble member; the member
  order is only in the global attribute `invar_hm_realization_id`.
- GDAL 3.14: default open lists subdatasets; a variable opens as a
  35408 x 1 raster in pixel coordinates.
- storecard's first-pass LON_0_360 on `id` is an artefact of the mislabel.
  COORD_NONMONOTONIC is literally true but only because ids are not sorted.
- Not determined: why units are "%" when the header says reference-period
  values are absolute; where the matching polygons are (the files cite
  DOI 10.5281/zenodo.581451, not checked).

## How to read it

Verified with the GDAL 3.14 Python multidimensional API, 2026-11-06:

```python
import numpy as np
from osgeo import gdal
gdal.UseExceptions()
rg = gdal.OpenEx("cout-perc1_..._remap215.nc", gdal.OF_MULTIDIM_RASTER).GetRootGroup()
subid = rg.OpenMDArray("id").ReadAsArray().astype("int64")
cols = {"subid": subid}
for k in range(1, 5):
    v = rg.OpenMDArray("variable%d" % k).ReadAsArray()[0]   # drop time
    cols["variable%d" % k] = np.where(v == -9999, np.nan, v)
```

Join to E-HYPE catchment polygons by SUBID to map it.

## History

- 2018-11-12, commit 629d870 "add https://github.com/r-spatial/stars/issues/73"
  first listed these files together with the gridded remap0.5 companions
  (see case copernicus-fdc-ensemble-as-variables). What that stars issue
  reports is not archived here.
- Shipped in weird.tar.gz in release v0.0.12.
- issues/013.md matches the folder name "copernicus" but is about a
  different Copernicus Marine product; it does not concern these files.

## Links

- https://github.com/r-spatial/stars/issues/73
- https://doi.org/10.5281/zenodo.581451
