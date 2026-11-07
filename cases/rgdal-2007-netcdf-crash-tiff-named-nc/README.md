# 2007: rgdal crashed R on the first four problem files, and the workaround wrote TIFFs named .nc

This is where the archive starts. In May 2007, in R 2.5.0 on Windows with
rgdal 0.5-9 and GDAL 1.4.0 (FWTools 1.2.2), four ordinary oceanographic
netCDF files crashed R as soon as rgdal opened them. The working folder held
the four files, a script recording each attempt (`nctrouble.R`), `gdalinfo`
dumps of each file, a screenshot of the crash, and the converted outputs.
Ten years later the same four files went into the ranch repo's
`weird_nc.zip`, and from there into this archive. The problems first noted
here (lon-major storage, south-up rows) are the same ones the 2026 cases
describe in detail.

| file | what |
|---|---|
| `legacy/R/nc/nctrouble.R` | the attempts, with versions and results in comments |
| `legacy/R/nc/extract.R` | helpers that parse `gdalinfo` output for subdataset names |
| `legacy/R/nc/RCrash.png` | the "R for Windows GUI front-end has encountered a problem" dialog |
| `extdata/dt_ref_...20060315.nc`, `oscar_gdr_5d1993.nc`, `R13352.nc`, `ssh05d19921006.nc` | the four source files |
| `legacy/R/nc/*.txt` | `gdalinfo` from GDAL 1.4 for each source file |
| `legacy/R/nc/dt.nc`, `oscar.nc`, `R133.nc`, `ssh05.nc`, `p.nc`; `ranch/weird_nc/p_calibrate.nc` | GeoTIFFs named `.nc`, made by `gdal_translate` |
| `legacy/R/nc/dt.png`, `oscarU.png` | plots of the converted grids |

## What went wrong

1. **Opening crashed R.** `GDAL.open()` on each file, and on its subdatasets
   (`NETCDF:"file":var`), crashed R or failed.
2. **The workaround changed the format without saying so.** Each subdataset
   was converted with `gdal_translate NETCDF:"file":var out.nc`. The default
   output driver was GTiff, so the outputs are GeoTIFFs with a `.nc`
   extension. Readers that identify files by content (GDAL does) open them
   without complaint; anything that trusts the extension fails.
3. **The grids came out misoriented.** `dt.nc` is 915 x 1080, latitude along x
   ("aligned E-W up" in the script), because the AVISO file is stored lon-major.
   `ssh05.nc` is south-up ("aligned South-up"), because the latitude axis
   ascends.
4. **The geotransforms were off by a cell.** GDAL 1.4 put the origin at the
   first cell centre and divided the centre-to-centre span by the number of
   cells: `oscar.nc` has origin (120.5, 34.5) and pixels of 0.9941 x 0.9857
   degrees on a 1 degree grid, and `ssh05.nc` has 0.4993 x 0.4986 on a 0.5
   degree grid.

## How to read it now

Current GDAL opens all four source files, with correct geotransforms (verified
with GDAL 3.14.0dev on 2026-11-07: OSCAR origin (120, 35) with 1 degree
pixels; ssh05d origin (0, 90) with 0.5 degree pixels, north-up). What remains
awkward about each file is in its own case:
[aviso-mercator-as-lonlat](../aviso-mercator-as-lonlat/),
[oscar-pacific-0-360-dateline](../oscar-pacific-0-360-dateline/),
[argo-profiles-char-dim-dropped](../argo-profiles-char-dim-dropped/) and
[topex-ssh-noncf-fill-sentinels](../topex-ssh-noncf-fill-sentinels/).

The derived `.nc` TIFFs are kept as evidence of the 2007 behaviour, not as
references: their georeferencing carries the errors above.

## History

- 2000-07-31, 2006-03-21, 2006-08-30, 2006-10-07: source files dated (ssh05d, AVISO, OSCAR, R13352)
- 2007-05-01: the attempts, dumps and outputs
- 2018-09-12: four of the sources, plus `p_calibrate.nc`, committed to ranch in `weird_nc.zip`
- 2018-10: the same four are among the first files in rasterwise's `extdata/`
- 2026-11-07: found in a legacy web folder in the data collection and archived here

## Links

- [issues/004.md](../../issues/004.md) (R13352 in the rogue gallery)
- [issues/005.md](../../issues/005.md) (stars testing; R13352 the one failure)
