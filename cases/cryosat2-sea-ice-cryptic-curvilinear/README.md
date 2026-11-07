# CryoSat-2 Antarctic sea ice: the NSIDC 25 km polar stereographic grid stored as 2D lon/lat

A monthly CryoSat-2 sea ice file (CS2WFA algorithm, July 2010) that carries only
2D latitude and longitude arrays and no CRS. Those arrays are the NSIDC 25 km
south polar stereographic grid, exact to within 40 m, so the whole georeferencing
is an extent and EPSG:3412. This is the file regular-in-what opens with, and the
one gproj's detector is built on. It came to this archive as the attachment to
issue 20.

| canonical_path | sha256 | size |
|---|---|---|
| `issue-attachments/020/CS2WFA_25km_201007.nc` | `13cc4140fb59` | 2,152,693 |

## What's wrong

- **A regular grid in costume.** 332 x 316 cells, with `lat(y, x)` and `lon(y, x)`
  only. Projected into EPSG:3412, every cell centre is within about 40 m of an
  exact 25 km grid on NSIDC's south extent (x -3950000 to 3950000, y -3950000 to
  4350000).
- **The CRS that looks right isn't.** EPSG:3031, the usual Antarctic polar
  stereographic, has true scale at 71 S on WGS84; NSIDC's grid has true scale
  at 70 S on the Hughes 1980 ellipsoid. Against the file's own coordinates
  3031 is off by up to 13 km, about half a cell. EPSG:3976 (NSIDC's WGS84
  variant) is within 125 m. EPSG:3412 fits.
- **Upside down by default.** The rows are stored north first. With no 1D
  coordinates to say otherwise, GDAL's netCDF driver assumes bottom-up storage
  and flips them.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```sh
gdal_translate --config GDAL_NETCDF_BOTTOMUP NO \
  -a_srs EPSG:3412 -a_ullr -3950000 4350000 3950000 -3950000 \
  NETCDF:"CS2WFA_25km_201007.nc":sea_ice_concentration out.tif
```

The result reproduces the file's longitudes and latitudes to within 41 m. The
thickness variables are in a group:
`NETCDF:"CS2WFA_25km_201007.nc":/sea_ice_thickness/sea_ice_thickness`.

## History

- 2022-11-15: file created (its `history` attribute)
- 2024-02-01: attached to issue 20, with a fix using EPSG:3031
- 2026-11-07: archived here; the CRS settled as EPSG:3412 by fitting the
  file's own coordinates, agreeing with regular-in-what's worked case

## Links

- [issues/020.md](../../issues/020.md)
- regular-in-what: [the problem chapter](https://hypertidy.github.io/regular-in-what/01-problem.html)
  and [the CryoSat-2 worked case](https://hypertidy.github.io/regular-in-what/07-cases.html#sec-case-cryosat)
