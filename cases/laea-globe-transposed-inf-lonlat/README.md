# Whole-globe Lambert azimuthal disk stored transposed, with Inf lon/lat off the disk

A 128 x 128 GEBCO elevation image of the whole Earth as a Lambert azimuthal
equal-area disk. The only georeferencing is a pair of 2D lon/lat arrays,
which are +Inf outside the disk, and the image is transposed (north is to
the left). GDAL's geolocation warp fails on the Inf values. The projection
can be recovered from the lon/lat arrays and assigned directly.

| canonical_path | sha256 | size |
|---|---|---|
| data-raw/spherical.nc | da47930e9aba | 338174 |

Also uploaded as `data-raw/spherical.nc1` and `data-raw/spherical.nc2`
(same bytes).

## What's wrong

- `gebco(y, x)` with `coordinates = "lon lat"`; `lon`, `lat` 2D, no units;
  `crs` is `latitude_longitude` (describes lon/lat, not the grid). No
  `_FillValue`.
- 3492 of 16384 cells have lon = lat = +Inf (the corners outside an
  inscribed disk); gebco is 0 there.
- Pixel radius matches sin(c/2) of angular distance from (0, 0): a whole
  sphere LAEA, radius 2R, ~199.3 km pixels. Checked against azimuthal
  equidistant and orthographic, which do not fit.
- Transposed: easting follows the row index, northing the column index.
  Data and lon/lat agree with each other (Tibet and the Mariana Trench
  land where they should).
- GDAL 3.14: `gdalwarp -geoloc` fails with "Int overflow : -nan x -nan";
  gebco rows come back reversed unless `GDAL_NETCDF_BOTTOMUP=NO`.

## How to read it

Mask, transpose, assign LAEA. Verified with GDAL 3.14.0dev on 2026-11-06:

```python
import numpy as np
from osgeo import gdal
gdal.UseExceptions()
gdal.SetConfigOption("GDAL_NETCDF_BOTTOMUP", "NO")
rd = lambda v: gdal.Open('NETCDF:"spherical.nc":%s' % v).ReadAsArray()
g, lon = rd("gebco"), rd("lon")
a = np.where(np.isfinite(lon), g, np.nan).T
ext = 2 * 6378137.0; res = 2 * ext / 128
d = gdal.GetDriverByName("GTiff").Create("spherical_laea.tif", 128, 128, 1, gdal.GDT_Float32)
d.SetGeoTransform([-ext, res, 0, ext, 0, -res])
d.SetProjection("+proj=laea +lat_0=0 +lon_0=0 +R=6378137 +units=m +no_defs")
b = d.GetRasterBand(1); b.SetNoDataValue(float("nan")); b.WriteArray(a)
d = None
```

Cell centres agree with the file's lon/lat to under a quarter pixel; the
producer's exact extent is unknown, so this is a best fit.

## History

- 2024-03-22, all via GitHub web upload: commit 96853fe "spherical.nc";
  27e1317 "Rename spherical.nc to spherical.nc1"; b1e3263 "Add files via
  upload"; 9124bf9 "Rename spherical.nc to spherical.nc2"; 39dda7b "Add
  files via upload". All three names hold the same bytes.
- 2026-11-06, commit fd09e23 removed data files from the tree.
- Not listed in weirdlist.txt; no issue mentions it. Who made it and why
  is not recorded.

## Links

None recorded.
