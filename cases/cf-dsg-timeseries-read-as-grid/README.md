# CF timeSeries station file that GDAL opens as a 20 x 10 raster

A small CF-1.7 discrete sampling geometry file: precipitation at 10 stations
over 20 days. It is a table of point time series, not a grid, but GDAL's
raster view shows it as a time-by-station image with no georeferencing, and
its vector view loses the stations.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/timeseries.nc | 33765f301d00 | 10854 |

## What's wrong

- `featureType = "timeSeries"`; `pr(station, time)` with `lat(station)`,
  `lon(station)`, `alt(station)` and `num(station)` (`cf_role =
  "timeseries_id"`). Valid CF.
- GDAL 3.14 (`gdalinfo`) opens it as a 20 x 10 raster, x = time,
  y = station, pixel coordinates only, with warnings that time and station
  are not X/Y dimensions. Station positions are dropped.
- `ogrinfo` gives a layer with 20 features, no geometry and only `time`.
- storecard's heuristic Y_ASCENDING on `lat` does not apply: lat is per
  station, not an axis.

## How to read it

As a table (verified with xarray on 2026-11-06):

```python
import xarray as xr
df = xr.open_dataset("timeseries.nc").to_dataframe().reset_index()
# 200 rows: station, time, pr, num, lat, lon, alt
```

## History

- File dated 2018-08-29 in the release tarball; origin not recorded. The
  regular station values (lat 40..49, lon 10..19) suggest a synthetic
  example (inference).
- First listed in weirdlist.txt by commit 65a62da (2018-10-04), whose message
  is about a different file ("EURO-CORDEX_81_DOMAIN000 example for stars").
- Shipped in weird.tar.gz in releases v0.0.6 to v0.0.12.

## Links

- CF conventions 1.7 (chapter 9, discrete sampling geometries):
  https://cfconventions.org/Data/cf-conventions/cf-conventions-1.7/cf-conventions.html
