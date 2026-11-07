# 5D netCDF test file: GDAL band metadata for more than one extra dimension

A synthetic 5D netCDF file made in 2009 to test a GDAL netCDF driver patch.
The array `a(c5, c4, c3, y, x)` has three non-spatial dimensions, so GDAL
exposes it as 12 bands, and each band must say which (c5, c4, c3) slice it
is. GDAL 1.7-era output got that wrong; GDAL 3.14 gets it right.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/high-dim/test-1.nc | fae2e2fc0b30 | 996 |
| data-raw/high-dim.R | 9c933b8fef75 | 8651 |

## What's wrong

Nothing in the file. The values are known by construction (m = 1:24; the
c5 slices are m, m + 0.1, m * 2). The script's 2009 comments show
unpatched GDAL (1.7.0dev, FWTools 2.4.3) giving `NETCDF_DIMENSION_c4=0` on
every band and a broken c3 sequence, and a patched build giving the right
sequence. The script cites GDAL trac tickets 2582 and 2583.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-06: `gdalinfo test-1.nc` gives 12
bands with `NETCDF_DIM_c5/c4/c3` stepping c3 fastest, then c4, then c5, and
band values that match the construction (band 1 = 1..6, band 12 = 38..48).

Differences from 2009: no geotransform now (x and y carry no attributes;
whether that is the reason was not checked), and rows come out in reverse
file order (GDAL's bottom-up default; `GDAL_NETCDF_BOTTOMUP=NO` gives file
order, checked: band 1 = 1..6 in file order).

Status is fixed-upstream on the strength of current behaviour; no fix commit
is archived here.

## History

- 2009-11-09: file and script written to test the GDAL ticket 2583 patch
  (per the script header).
- 2018-11-08, commit f16d369 "add old 5D faithful".
- Shipped in weird.tar.gz in release v0.0.12.

## Links

- https://trac.osgeo.org/gdal/ticket/2583
- https://trac.osgeo.org/gdal/ticket/2582
- https://www.unidata.ucar.edu/mailing_lists/archives/galeon/2005/msg00138.html
