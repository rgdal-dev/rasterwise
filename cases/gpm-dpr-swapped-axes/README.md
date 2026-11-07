# GPM DPR 3A-DAY via OPeNDAP: (nlon, nlat) order gives GDAL a grid with latitude as x

A one-day GPM Dual-frequency Precipitation Radar grid (2018-09-15, V05B), subset through a Hyrax OPeNDAP server. Its data are dimensioned (AD, chn, nlon, nlat), so latitude varies fastest. GDAL builds a self-consistent geotransform in which x is latitude and y is longitude. The data must be transposed before they can be used in a lon/lat CRS. (The candidate name for this case said TRMM; the file is GPM.)

| canonical_path | sha256 | size |
|---|---|---|
| extdata/swapped/3A-DAY.nc | df20ee33704c | 12359852 |
| extdata/swapped/gdal-dev-readme.txt | e3fce81277e9 | 67 |

## What's wrong

- `precipRateNearSurfMean(AD, chn, nlon, nlat)` = (2, 2, 1440, 536). `nlon` is -179.875..179.875 and `nlat` is -66.875..66.875 (ascending), both 0.25 degree.
- GDAL 3.14.0dev classic view: 536 x 1440, origin (-67, 180), pixel (0.25, -0.25), meaning x = latitude and y = longitude. No CRS. 4 bands = AD x chn.
- `chn:comment` names four channels (Ku, Ka, KaHS, DPR), but `chn` has length 2.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```
gdalmdimtranslate 3A-DAY.nc gpm.tif \
  -array "name=precipRateNearSurfMean,transpose=[0,1,3,2],view=[0,0,::-1,:]"
gdal_translate -a_srs EPSG:4326 gpm.tif gpm_4326.tif
```

The output is 1440 x 536, origin (-180, 67), 0.25 degree, equal to the stored slice transposed with latitude reversed. The transpose is applied before the view. Change `0,0` to choose another AD/chn slice.

## History

- `3A-DAY.nc` first listed 2018-10-12, commit "gdal-dev swapped axes". `gdal-dev-readme.txt` first listed 2019-03-21.
- The file's history attribute records the OPeNDAP request on 2018-10-11.

## Links

- https://lists.osgeo.org/pipermail/gdal-dev/2018-October/049139.html
