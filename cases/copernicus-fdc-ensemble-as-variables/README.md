# C3S flow-duration indicators on a 0.5 degree grid: ensemble members as value1..value12

The gridded companions of the catchment files in
copernicus-fdc-catchment-id-as-longitude. The 0.5 degree lon/lat grid is
regular with ascending latitude, and GDAL places it correctly. The trouble
is bookkeeping: 12 ensemble members are 12 separate variables whose
identities are only in global-attribute strings, and four of them carry a
units typo.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/copernicus/cout-perc1_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap0.5.nc | 8ad498d23324 | 497572 |
| extdata/copernicus/cout-perc5_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap0.5.nc | 4cb5979532ce | 497572 |

## What's wrong

- Grid: lat 78 (33.25..71.75, ascending), lon 130 (-24.75..39.75), time 1.
- `value1..value12(time, lat, lon)` are ensemble members (E-HYPE21, VIC421,
  Lisflood, four each), named only in `invar_hm_realization_id`,
  `invar_gcm_id`, `invar_rcm_id` "in the order of the variables". The file
  stores them as value1, value10, value11, value12, value2, ...; the
  numeric suffix is the order to use (inference).
- `units = "m-3 s-1"` on value1..4, `"m3 s-1"` on value5..12; magnitudes
  are comparable, so the first is a typo (inference).
- `geospatial_lat_*` say "degrees_east", `geospatial_lon_*` say
  "degrees_west"; numbers are right, unit words wrong.
- Valid (land) mask differs by model: 4323 / 4618 / 3933 cells (perc1).

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-06:

```
gdalinfo NETCDF:"cout-perc1_..._remap0.5.nc":value1
# 130 x 78, origin (-25, 72), pixel (0.5, -0.5), NoData -1e20
```

Read value1..value12 in numeric order, label each from
`invar_hm_realization_id`, and treat all as m3 s-1.

## History

- 2018-11-12, commit 629d870 "add https://github.com/r-spatial/stars/issues/73".
  What that stars issue reports is not archived here.
- Shipped in weird.tar.gz in release v0.0.12.
- issues/013.md matches the folder name "copernicus" only; it is about a
  Copernicus Marine Arctic product, not these files.

## Links

- https://github.com/r-spatial/stars/issues/73
