# SSM/I sea ice on the NSIDC south polar grid with no coordinates; GDAL reads it upside down

A 12.5 km Antarctic sea-ice concentration grid that carries no coordinates
and no CRS: the only hint is `grid = "NSIDC"`, `pole = "south"` in global
attributes. With nothing to say which way is up, GDAL assumes bottom-up and
flips it, but the rows are stored top-down, so the default read is upside
down.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/19911203.nc | 549a1b01dda6 | 840508 |

## What's wrong

- `concentration(time, nj, ni)` and `quality_flag`, byte, 1 x 664 x 632,
  nodata -128. No lon/lat, x/y, grid_mapping or CRS.
- 632 x 664 at 12.5 km matches the NSIDC southern polar stereographic grid
  exactly (x -3950..3950 km, y -3950..4350 km).
- GDAL's netCDF driver flips rows when there are no coordinates (checked:
  default array == storage array reversed).
- Storage order is top-down. On the NSIDC grid, storage order puts land
  (quality_flag 1) on the Antarctic Peninsula and 87-100 percent ice in the
  Weddell Sea at 40 W 65 S, as expected for 3 December; the flipped order
  does not.
- Value 127 occurs in concentration (3127 cells) and quality_flag uses
  0-14, with no flag meanings in the file.
- It was first archived under a folder called `rectlinear`; it is a
  projected grid, not rectilinear lon/lat.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```
gdal_translate --config GDAL_NETCDF_BOTTOMUP NO -a_srs EPSG:3412 \
  -a_ullr -3950000 4350000 3950000 -3950000 \
  NETCDF:19911203.nc:concentration conc.tif
```

The config option only applies while reading, so a VRT built this way does
not keep it; write a GTiff, or flip the array yourself.

## History

- 2007-01-16: file created (its creation_time attribute).
- 2018-10-13: listed as `rectlinear/19911203.nc`, commit e013b91 "some
  rectlinear stuff" (release bundle v0.0.6 has it at that path).
- 2018-10-15: moved to the top of extdata, commit ac58085 "add fronts".

## Links

- fingerprints/19911203.nc.cdl (header fingerprint)
