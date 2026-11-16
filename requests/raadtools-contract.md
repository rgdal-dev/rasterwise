# Request: the raadtools dataset contract

From: AustralianAntarcticDivision/raadtools (branch `read-to-grid`).
For: the harvest of assertions here, through storecard, into raad.virtualize
as a resource raadtools pulls from.

## What raadtools needs

raadtools reads a subset of the raad collection on /rdsi, which the
rasterwise scan already covers. It wants one contract row per dataset to
come out of this pipeline, rather than facts written by hand into each
reader:

| field | meaning |
|---|---|
| `dataset` | a stable id (the raad.virtualize store name, where there is one) |
| `crs` | the CRS of the grid, and how it is known: `declared` (the file says so) or `asserted` (an assertion supplies it) |
| `extent` | `c(xmin, xmax, ymin, ymax)`, cell edges, in `crs` |
| `dim` | `c(ncol, nrow)` |
| `source_finder` | how files are found (the raadfiles lister, or the path pattern) and the GDAL source name form, including the subdataset, e.g. `NETCDF:"<file>":sst` |
| `date_contract` | cadence, whether dates are unique and ordered, how a date maps to a file, or to a band within a file, and the matching tolerance raadtools uses |

Later, not needed to place data on a grid: values (CF packing, fill values,
valid range, flag codes). These are storecard's `values` section.

## How raadtools uses it

Every read is one GDAL classic-raster open of `dsn` and `band` (multidim is
not used: raadtools reads 2D grids with bands). With the contract's `crs`
and `extent` applied where the file lacks or misstates them, raadtools warps
the source directly onto any target grid (CRS, extent, dim), for example the
view of a slippy map. So the contract is exactly what a correct open needs,
and nothing about how raadtools presents the result.

Its consumer check is `tests/testthat/test-source-spec.R`: each reader's
result must give `dsn`, `band`, `crs`, `extent` and `dim`, and each `dsn`
must open in GDAL with that band.

## Facts found so far (2026-11-09, GDAL 3.14)

Candidates for assertions or findings. Each needs the file's sha256 and a
sighting before it becomes a case.

- OISST v2.1 daily (NCEI AVHRR netCDF): no `grid_mapping`; raadtools
  asserts EPSG:4326. Longitude 0-360 (extent 0, 360, -90, 90, 1440 x 720).
  Variables sst, anom, err, ice, one file per day.
- OISST monthly (PSL `sst.mon.mean.nc`): no CRS; one file, 542 time steps
  as bands, chunked one step per chunk (`1, 720, 1440`). Date to band is the
  month index from 1981-09.
- NSIDC sea ice concentration (CDR and older NSIDC-0051): raadtools sets the
  CRS explicitly (south EPSG:3976, north EPSG:3413) because older files lack
  it. It does so only when the file declares none, so for G02202 v6 the CRS
  may be `declared`. The rasterwise case nsidc-polar-grid-no-coords-flipped
  and storecard's f03d assertion use EPSG:3412 (Hughes 1980) for the same
  grid; the contract needs one answer per dataset, with evidence. Values above 1 are flag codes (land, coast, missing, pole hole); the
  valid range is [0, 1], and the mask must be applied before any
  interpolating resample.
- AVISO/CMEMS FSLE: the extent reads as -1.057e-09, 360 (floating point noise
  at the west edge).
- Mixed layer depth climatology: read from an `.Rdata` RasterBrick, so there
  is no file for GDAL to open. A candidate for converting once to a GeoTIFF.
- Fast ice: no file within 26 days of 2020-01-15 (a coverage gap, or the
  lister; not yet checked).

Not file problems, and not for rasterwise: raadtools readers that return
in-memory results by default (`rotate()` for 0-360 sources, `classify()` for
the ice flag mask), and a slow warp of one band of the 542-band monthly OISST
file (5.6 min against 70 ms) that came from handing the warper the whole
dataset; the file's chunking is fine.

## Datasets in scope

The raadtools front-door readers surveyed on 2026-11-09, by what their
default result reads:

| reader | source on /rdsi | crs | grid |
|---|---|---|---|
| readsst, read_oisst_daily | OISST v2.1 AVHRR daily netCDF, var sst | asserted EPSG:4326 | 1440 x 720, 0-360 |
| read_oisst_monthly | PSL OISST `sst.mon.mean.nc`, band per month | asserted EPSG:4326 | 1440 x 720, 0-360 |
| readice, read_nsidc_cdr_daily | NSIDC CDR daily, south | set: EPSG:3976 | 316 x 332 |
| readice(hemisphere = "north") | NSIDC CDR daily, north | set: EPSG:3413 | 304 x 448 |
| read_amsr2_ice | AMSR2 ASI 6.25 km (s6250 GeoTIFF), south | declared | 1264 x 1328 |
| read_amsr_ice_3k_daily | AMSR2 ASI 3.125 km, south | declared | 2528 x 2656 |
| readssh, read_adt_daily, readcurr | CMEMS SEALEVEL_GLO_PHY_L4 daily, vars adt, ugos, vgos | declared | 2880 x 1440, -180-180 |
| readwind | NCEP2 6-hourly u/v | declared | 192 x 94, 0-360 |
| read_ccmp | CCMP v3.1 daily, uwnd/vwnd | declared | 1440 x 720, 0-360 |
| readchla, read_oc_chl_daily | MODIS Aqua L3m daily CHL 4 km | declared | 8640 x 4320 |
| readghrsst | GHRSST MUR v2 | declared | 36000 x 17999 |
| readfsle | AVISO FSLE | declared | 9000 x 4500, 0-360 |
| readtopo | ETOPO2 (through a VRT) | declared | 10800 x 5400 |
| read_bathy | GEBCO 2023 COG | declared | 86400 x 43200 |
| readmld | MLD climatology (`.Rdata`) | n/a | 721 x 120, south of 30S |

"declared" means GDAL reports a CRS from the file, as raadtools reads it;
whether that CRS is right is for the harvest to confirm.

## Acceptance

For each dataset: sampled files across its date range open with
`source_finder`'s GDAL name and band, under the contract's crs where it is
asserted, and give the contract's crs, extent and dim; dates are ordered and
unique, and each date resolves to exactly one file and band. When raad.virtualize
publishes the table, raadtools reads its rows instead of its own constants.

## Ledger

`ledger/raadtools.csv` maps each raadtools reader (and the arguments that
select a source) to its raadfiles finder, listing-corpus source, dataset,
era and any rasterwise case. One contract row is one (dataset, era), keyed
by the raad.virtualize dataset id (decided 2026-11-09); readers and finders
join to it through the ledger and are never the key. `dataset_status` is
`built` where raad.virtualize publishes the dataset, `proposed` for an id not
built yet, `none` where no store is planned. `tier` is 1 (store exists), 2
(corpus listing, no store) or 3 (neither).
