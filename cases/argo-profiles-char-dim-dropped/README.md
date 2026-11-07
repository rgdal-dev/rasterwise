# Argo float profiles: not a grid, and char variables whose string dimension gets dropped

R13352.nc holds 54 profiles from a single Argo float (global title
"ARGO-CSIRO dataset"). It was swept up in a "read every .nc as a raster"
test and broke stars::read_ncdf: its char flag variables carry a length-1
string dimension that R's netCDF libraries drop, and in any case it is
profile data with one position per profile, not a grid.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/R13352.nc | 5d49cbcda738 | 165104 |

## What's wrong

- Dimensions: profile = 54, depth = 51, string_df = 72, string8 = 8,
  string1 = 1. Measurements p, t, s are (profile, depth); lon, lat and the
  time variables are (profile).
- lon is 0-360 (valid_range 0, 360) and the track crosses the prime
  meridian: 355.25 ... 359.9, then 0.38 ... 5.04 (checked with ncdump).
  lat 2.84 to 6.31.
- `*_qc` flags are `char(profile, depth, string1)`. Issue 4: read_ncdf
  failed because "the 1-dim first dimension" was dropped even with
  `collapse = FALSE`; the recorded answer is that ncdf4 and RNetCDF drop the
  NC_CHAR dimension and return a vector of strings, so the array shape no
  longer matches the header.
- GDAL 3.14 multidim API: `data_file` comes back as 54 strings (char dim
  dropped), `t_qc` as a 54 x 51 x 1 numeric array (char dim kept). The
  classic driver lists each 2-D variable as an ungeoreferenced subdataset.
- Times are encoded as `jday` ("days since -4712/1/1 12:00:0.0 (julian
  day)") and `decimal_time` ("years since 1-1-1"); the separate
  year/month/day/hour/minute/second variables are easier.
- `s` and all `*_calibrate` variables are all-missing (every value is
  99999; checked).

## How to read it

As a table of profiles. Verified with GDAL 3.14.0dev Python on 2026-11-07:

```python
from osgeo import gdal
gdal.UseExceptions()
rg = gdal.OpenEx("R13352.nc", gdal.OF_MULTIDIM_RASTER).GetRootGroup()
t   = rg.OpenMDArray("t").ReadAsArray()      # (54, 51); 99999 = missing
lon = rg.OpenMDArray("lon").ReadAsArray()    # (54,), 0-360
lat = rg.OpenMDArray("lat").ReadAsArray()
files = rg.OpenMDArray("data_file").Read()   # 54 strings
```

Use `(lon + 180) % 360 - 180` for a continuous track across 0 degrees.

## History

- 2018-10-04: listed in the first weirdlist.txt (commit 65a62da, "EURO-CORDEX_81_DOMAIN000
  example for stars"; that commit created the list of 12 files, so its
  message is not about this file).
- 2019-01-24: issue 4 "degen in R13352.nc (rogue gallery #1)" and issue 5
  "stars testing" opened, from a loop running read_ncdf over every file.
- 2019-05-15: issue 4 answered (ncdf4/RNetCDF drop the NC_CHAR dimension).

## Links

- issues/004.md
- issues/005.md
