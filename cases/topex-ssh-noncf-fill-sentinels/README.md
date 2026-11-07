# TOPEX/POSEIDON sea level: land and no-data sentinels declared under non-CF attribute names

A 0.5 degree global ten-day sea level map from the WOCE CD-ROM. Land is
32766 and no data is 32767. The file declares them only through attributes
named `land_value` and `fill_value`, which CF tools ignore, so a careless
read reports 32 m sea level. `valid_min`/`valid_max` (-1500, 1500) is the
only standard hint, and GDAL uses it.

| canonical_path | sha256 | size |
|---|---|---|
| extdata/ssh05d19921006.nc | 0bc799977131 | 784264 |

## What's wrong

- `sea_level(latitude, longitude)` short, mm. 117250 cells hold 32767,
  88417 hold 32766, and 53533 hold real values, -815 to 925 (checked).
- No `_FillValue` or `missing_value`; `fill_value` and `land_value` are not
  CF attribute names.
- GDAL 3.14 honours valid_min/valid_max by default: both sentinels become
  nodata (reported as -32767, a value that never occurs), so land and gaps
  merge into one mask.
- latitude ascending (-89.75 first), longitude 0.25..359.75. GDAL flips
  the rows correctly; no CRS is declared.
- No time coordinate variable (woce_date = 19921006, julian_day_1990,
  depth(time) instead).
- The 89.75 N row is all land_value; 63 land cells have bin_count > 0.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```
gdal_translate -oo ASSUME_LONGLAT=YES NETCDF:ssh05d19921006.nc:sea_level sl.tif
gdalwarp -te -180 -90 180 90 -tr 0.5 0.5 sl.tif sl_180.tif
```

Mean 35.8 mm, 20.65 percent valid. To keep land distinct:

```
gdal_translate -oo HONOUR_VALID_RANGE=NO -oo ASSUME_LONGLAT=YES \
  -a_nodata 32767 NETCDF:ssh05d19921006.nc:sea_level sl_raw.tif
```

then treat 32766 as land.

## History

- 2000-07-05: file created (creation_date attribute).
- 2018-10-04: listed in the first weirdlist.txt (commit 65a62da,
  "EURO-CORDEX_81_DOMAIN000 example for stars"; that commit created the
  12-file list, so its message is not about this file). Why it was added is
  not recorded.

## Links

- fingerprints/ssh05d19921006.nc.cdl
