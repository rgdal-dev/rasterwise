
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

## The list

    #> bad_examples_62/example1.nc
    #> bad_examples_62/example2.nc
    #> bad_examples_62/example3.nc
    #> dt_ref_global_merged_madt_uv_19921014_19921014_20060315.nc
    #> EURO-CORDEX_81_DOMAIN000_54/EURO-CORDEX_81_DOMAIN000.nc
    #> file.nc
    #> hmr_ita.nc
    #> nhsce_v01r01_19661004_20140203.nc
    #> oscar_gdr_5d1993.nc
    #> R13352.nc
    #> ssh05d19921006.nc
    #> test.nc_60/test.nc
    #> timeseries.nc
