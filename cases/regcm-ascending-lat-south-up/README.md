# RegCM exceedance grid stored south-to-north (latitude ascending)

A regular lon/lat grid whose rows are stored with latitude ascending. The
coordinates are correct, but anything that treats array row 0 as the top of
an image draws it upside down. GDAL's netCDF driver corrects the order; the
HDF5 driver (which can claim this netCDF-4 file) does not.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/inverted_73/regcm-nn-2100_reg4_22.nc | 7ac6cca2ea00 | 2904294 |

## What's wrong

- Variable `POT(RP, lat, lon)`, 5 x 307 x 470, float, `_FillValue = -1`;
  `RP` is return period in years (2, 10, 20, 50, 100).
- `lat` runs 44.75 to 47.198 ascending, step 0.008; `lon` 10.2 to 13.952.
  So the first stored row is the southernmost (checked on the bytes).
- The folder name `inverted_73` refers to r-spatial/stars issue 73. That
  thread is not archived here, so the reported symptom is not recorded beyond
  the word "inverted".
- GDAL 3.14 netCDF driver: north-up geotransform, data flipped to match
  (verified: GDAL array == stored array reversed along lat).
- GDAL HDF5 driver: no georeferencing and rows in storage order. GDAL chose
  this driver for a copy of the file that had no `.nc` extension.
- No CRS is declared (no `grid_mapping`), so GDAL assigns none by default.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```
gdal_translate -oo ASSUME_LONGLAT=YES \
  NETCDF:regcm-nn-2100_reg4_22.nc:POT pot.tif
```

Result: 5 bands, origin (10.196, 47.202), pixel size 0.008, OGC:CRS84.
With a raw array reader, reverse the lat axis (or keep lat with the data)
before plotting.

## History

- 2018-11-10: file created (its history attribute: calc_POT_noraster.R).
- 2018-11-12: listed in weirdlist.txt by commit 629d870,
  "add https://github.com/r-spatial/stars/issues/73". Shipped in the
  weird.tar.gz release bundles v0.0.12 and v0.5.0.

## Links

- https://github.com/r-spatial/stars/issues/73
