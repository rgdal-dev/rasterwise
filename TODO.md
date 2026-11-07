# Parked work

## Survey the large managed data collection (bowerbird / blueant)

A many-year collection built with ropensci/bowerbird and
AustralianAntarcticDivision/blueant (legacy, not all of it managed) is mounted
on one of the harvested machines. It is likely to hold:

* copies or close relatives of the 39 files in `missing.csv`. Most are public
  products (MODIS HDF4, GOES-16 ABI, NSIDC SWE, E-OBS, CMIP5 mrso, UERRA,
  UKCP18), so the same files may be there under their original names;
* many more instances of the problem classes the cases describe, which would
  give a real measure of how common each is.

Approach, to keep it read-only and cheap at petabyte scale:

1. Name sweep first: match `missing.csv` names (and the product names they
   imply) against the collection's file listing, without reading data.
2. For candidates, compare headers against `fingerprints/` with
   `tools/readme_headers.py compare` before hashing anything.
3. Add a header-only mode to `tools/harvest.py` (sniff the format and record a
   header fingerprint, no full sha256) for sampling the collection by product,
   so problem-class counts can be made without reading the data.
4. Hash and harvest only what is to be adopted into the manifest.

## Other loose ends

* cliotop3: 14 working files (MYD09A1 HDF4, gauss/, jimshady/, CAMS, ffdi,
  righted.tif, out.vrt, ...) are in the manifest by hash only. Collect the
  bytes, sniff them, and decide whether each deserves a case.
* `data-raw/dt_global_allsat_phy_l4_19930101_20190101.nc` has no case. It was
  committed as "old MERCATOR AVISO", but it is the modern regular lon/lat
  product. It may belong in `aviso-mercator-as-lonlat` as the contrast.
* Findings vocabulary: the cases use about 15 codes beyond storecard's
  first-pass set. Write one `findings.md` (code, definition, cases using it)
  and align it with storecard, e.g. confirmed fits could use
  `GRID_CRYPTIC_CURVILINEAR` (with the fitted CRS) rather than the heuristic
  `GRID_2D_LONLAT_ONLY`.
* `acc-fronts-mercator`: GDAL 3.14.0dev's classic API returned 0 for cells
  stored as NaN, while the multidimensional API returned NaN. Not reproduced
  with a synthetic file. Possibly a GDAL bug; worth a minimal reproducer.
* Publish the blobs (`tools/curate.py stage`, upload, `set-url`) and set
  `redistributable` per file.
* `harvest.py --manifest URL` (reading the tables over HTTP) is written but
  has not been exercised against a real URL.
