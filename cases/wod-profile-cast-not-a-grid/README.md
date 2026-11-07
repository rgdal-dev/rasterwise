# World Ocean Database single-cast profile: 1D in depth, not a raster

One World Ocean Database cast (CF `featureType = "Profile"`): a single
position and time with 12 depth levels of temperature, salinity, oxygen and
phosphate. GDAL's raster open fails on the file, and opening a variable
directly gives a 12 x 1 strip with depth as x. Read it as a profile.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/1D/test.nc | 5e5e6e71163d | 10776 |
| data-raw/1D-readme | 754b2204cf37 | 105 |

## What's wrong

- `lat`, `lon`, `time` are 0-d scalars: lon 14.56667, lat -32.66667,
  1963-10-11 04:00 (time 70774.1667 days since 1770-01-01; agrees with
  `date = 19631011`, `GMT_time = 4`).
- Measurements are `Temperature(z)` etc., z = 0 to 989 m (12 levels).
- GDAL 3.14: `gdalinfo test.nc` reports "not recognized as being in a
  supported file format"; `ogrinfo` fails too.
  `gdalinfo NETCDF:"test.nc":Temperature` gives a 12 x 1 raster, no
  georeferencing.
- `z` says `standard_name = "altitude"` but `positive = "down"` and
  `long_name = "depth_below_sea_level"`; the values are depths.

## How to read it

Verified with the GDAL 3.14 Python multidimensional API, 2026-11-06:

```python
from osgeo import gdal
gdal.UseExceptions()
rg = gdal.OpenEx("test.nc", gdal.OF_MULTIDIM_RASTER).GetRootGroup()
get = lambda n: rg.OpenMDArray(n).ReadAsArray()
lon, lat, t = get("lon"), get("lat"), get("time")   # scalars
z = get("z")                                        # m, positive down
temp = get("Temperature")                           # 16.84 at 0 m ... 3.41 at 989 m
```

## History

- 2018-12-17, commit 6f0f436 "1D example from a user report" (message
  paraphrased): added `data-raw/1D-readme`, a one-line R
  `download.file()` of the cast from a user's GitHub release, saved as
  `test.nc`. The file's own `date_created` is 2018-11-06.
- Shipped in weird.tar.gz in release v0.0.12.

## Links

None recorded.
