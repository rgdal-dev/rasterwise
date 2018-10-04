
<!-- README.md is generated from README.Rmd. Please edit that file -->

# weird.nc

The goal of weird.nc is to collect illustrative NetCDF files so our R
code works right.

Files are put into “extdata/”, and then a script is run to

  - archive all the files in extdata/ as a tarball
  - generate a record of the list of files
  - commit to the repo and tag the release
  - push the tarball artefact out into the Releases files (using R’s
    piggyback)

I put the stars issue number into the folder name
<https://github.com/r-spatial/stars/issues>

There are some weird and wonderful files in the extdata/ on their own,
from my personal collections.
