
<!-- README.md is generated from README.Rmd. Please edit that file -->

# rasterwise

The goal of rasterwise is to collate hard-won knowledge of what’s wrong
and what’s right about various data sets.

It began as a collection of iillustrative NetCDF files, used for testing
so our R code works right.

## raadtools - a code collection of raster wise-dom

TBD

A classic example is old ocean surface data (Aviso) that was in a
regular Mercator grid, but published with rectlinear lon-lat
arrays

<https://github.com/AustralianAntarcticDivision/raadtools/blob/master/R/fronts.R#L129-L142>

There are many others
<https://twitter.com/mdsumner/status/1057504207043997697>

## Contributing

Raise issues, send PRs, tell us your war stories\!

## Rogue NetCDF files

Files are put into “extdata/”, and then a script is run to

  - archive all the files in extdata/ as a tarball
  - generate a record of the list of files
  - commit to the repo and tag the release
  - push the tarball artefact out into the Releases files (using R’s
    piggyback)

## Get the files

To download the entire file bundle run this code:

``` r
library(piggyback)
pb_download("weird.tar.gz", dest = ".", repo = "mdsumner/rasterwise", tag = "v0.5.0")
```

I often put the stars issue number into the folder name
<https://github.com/r-spatial/stars/issues>

There are some weird and wonderful files in the extdata/ on their own,
from my personal collections.

## The list

    19911203.nc
    1D/test.nc
    bad_examples_62/bad_examples.R
    bad_examples_62/example1.nc
    bad_examples_62/example2.nc
    bad_examples_62/example3.nc
    copernicus/cout-perc1_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap0.5.nc
    copernicus/cout-perc1_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap215.nc
    copernicus/cout-perc5_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap0.5.nc
    copernicus/cout-perc5_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap215.nc
    dt_ref_global_merged_madt_uv_19921014_19921014_20060315.nc
    EOBS/EOBS_2001-2016.nc
    EOBS/readme
    EURO-CORDEX_81_DOMAIN000_54/EURO-CORDEX_81_DOMAIN000.nc
    EURO-CORDEX_81_DOMAIN000_54/issue_54.R
    file.nc
    get1index_64/test.nc
    GPP/gpp_Lmon_EnsembleGPP_observations_198201-201112.nc
    GPP/readme
    HDF4/ladsweb/MOD021KM.A2015091.0010.006.2015091134552.hdf
    high-dim/test-1.nc
    historical/historical.nc
    historical/readme-historical.nc.md
    hmr_ita.nc
    inverted_73/regcm-nn-2100_reg4_22.nc
    large-mem/pp_ens_mean_0.25deg_reg_v19.0e.nc
    mrso/mrso_Lmon_CMCC-CESM_rcp85_r1i1p1_200001-200412.nc
    mrso/readme
    nhsce_v01r01_19661004_20140203.nc
    NSIDC/alaska_2007_2008_swe_v01.nc
    NSIDC/readme
    NSIDC/sierra_2008_2009_swe_v01.nc
    ob_tran/example_ob_tran.nc
    ob_tran/example_ob_tran2.nc
    ob_tran/out.tif
    ob_tran/readme.txt
    oscar_gdr_5d1993.nc
    R13352.nc
    rectilinear/ACCfronts_nc4.nc
    rectilinear/CM2.1_regionmask.nc
    rectilinear/readme_CM2.1regionmask.txt
    rectilinear/readme_rectlinear.txt
    rectilinear/test_3_.nc
    SO-reproj/OR_ABI-L1b-RadC-M3C01_G16_s20190621802131_e20190621804504_c20190621804546.nc
    SO-reproj/SO-reproj.R
    ssh05d19921006.nc
    swapped/3A-DAY.nc
    swapped/gdal-dev-readme.txt
    test.nc_60/num60.R
    test.nc_60/test.nc
    timeseries.nc
    tricky_grids/OR_ABI-L1b-RadC-M3C01_G16_s20190621802131_e20190621804504_c20190621804546.nc

## The ncdumps -h

    ###############################################################################
    19911203.nc
    
    
    
    netcdf \19911203 {
    dimensions:
        ni = 632 ;
        nj = 664 ;
        time = 1 ;
    variables:
        int time(time) ;
            time:long_name = "time" ;
            time:units = "hours since 1900-1-1 0:0:0" ;
        byte concentration(time, nj, ni) ;
            concentration:long_name = "sea-ice concentration" ;
            concentration:units = "percent" ;
            concentration:scale_factor = 1. ;
            concentration:add_offset = 0. ;
            concentration:missing_value = -128b ;
            concentration:_FillValue = -128b ;
        byte quality_flag(time, nj, ni) ;
            quality_flag:long_name = "quality_flag" ;
            quality_flag:units = "n/a" ;
            quality_flag:scale_factor = 1. ;
            quality_flag:add_offset = 0. ;
            quality_flag:missing_value = -128b ;
            quality_flag:_FillValue = -128b ;
    
    // global attributes:
            :CONVENTIONS = "COARDS" ;
            :long_name = "Sea-ice concentration as observed by SSM/I" ;
            :short_name = "PSI-F13-Concentration" ;
            :producer_agency = "IFREMER" ;
            :producer_institution = "CERSAT" ;
            :netcdf_version_id = "3.4" ;
            :product_version = "2.0" ;
            :creation_time = "2007-016T10:51:07.000" ;
            :time_resolution = "daily" ;
            :grid = "NSIDC" ;
            :pole = "south" ;
            :spatial_resolution = "12.5 km" ;
            :platform_id = "F13" ;
            :instrument = "SSM/I" ;
    }
    
    
    
    
    ###############################################################################
    1D/test.nc
    
    
    
    netcdf test {
    dimensions:
        z = 12 ;
        strnlen = 200 ;
    variables:
        char country(strnlen) ;
        char WOD_cruise_identifier(strnlen) ;
            WOD_cruise_identifier:comment = "two byte country code + WOD cruise number (unique to country code)" ;
            WOD_cruise_identifier:long_name = "WOD_cruise_identifier" ;
        char originators_cruise_identifier(strnlen) ;
        int wod_unique_cast ;
            wod_unique_cast:cf_role = "profile_id" ;
        float lat ;
            lat:standard_name = "latitude" ;
            lat:long_name = "latitude" ;
            lat:units = "degrees_north" ;
            lat:axis = "Y" ;
        float lon ;
            lon:standard_name = "longitude" ;
            lon:long_name = "longitude" ;
            lon:units = "degrees_east" ;
            lon:axis = "X" ;
        double time ;
            time:standard_name = "time" ;
            time:long_name = "time" ;
            time:units = "days since 1770-01-01 00:00:00" ;
            time:axis = "T" ;
        int date ;
            date:long_name = "date" ;
            date:comment = "YYYYMMDD" ;
        float GMT_time ;
            GMT_time:long_name = "GMT_time" ;
        int Access_no ;
            Access_no:long_name = "NODC_accession_number" ;
            Access_no:units = "NODC_code" ;
            Access_no:comment = "used to find original data at NODC" ;
        char Platform(strnlen) ;
            Platform:long_name = "Platform_name" ;
            Platform:comment = "name of platform from which measurements were taken" ;
        char Institute(strnlen) ;
            Institute:long_name = "Responsible_institute" ;
            Institute:comment = "name of institute which collected data" ;
        int Orig_Stat_Num ;
            Orig_Stat_Num:long_name = "Originators_Station_Number" ;
            Orig_Stat_Num:comment = "number assigned to a given station by data originator" ;
        float Bottom_Depth ;
            Bottom_Depth:long_name = "sea_floor_depth_below_sea_surface" ;
            Bottom_Depth:units = "meters" ;
        char Wave_Direction(strnlen) ;
            Wave_Direction:long_name = "Wave_Direction" ;
            Wave_Direction:units = "WMO 0877 or NODC 0110" ;
        char Wind_Direction(strnlen) ;
            Wind_Direction:long_name = "Wind_Direction" ;
            Wind_Direction:units = "WMO 0877 or NODC 0110" ;
        float Wind_Speed ;
            Wind_Speed:long_name = "wind_speed" ;
            Wind_Speed:units = "knots" ;
        float Barometric_Pres ;
            Barometric_Pres:long_name = "Barometric_Pressure" ;
            Barometric_Pres:units = "millibars" ;
        float Dry_Bulb_Temp ;
            Dry_Bulb_Temp:long_name = "Dry_Bulb_Air_Temperature" ;
            Dry_Bulb_Temp:units = "degree_C" ;
        float Wet_Bulb_Temp ;
            Wet_Bulb_Temp:long_name = "Wet_Bulb_Air_Temperature" ;
            Wet_Bulb_Temp:units = "degree_C" ;
        char Weather_Condition(strnlen) ;
            Weather_Condition:long_name = "Weather_Condition" ;
            Weather_Condition:comment = "Weather conditions at time of measurements" ;
        char dataset(strnlen) ;
            dataset:long_name = "WOD_dataset" ;
        char dbase_orig(strnlen) ;
            dbase_orig:long_name = "database_origin" ;
            dbase_orig:comment = "Database from which data were extracted" ;
        float z(z) ;
            z:standard_name = "altitude" ;
            z:long_name = "depth_below_sea_level" ;
            z:units = "m" ;
            z:positive = "down" ;
        short z_WODflag(z) ;
        short z_sigfig(z) ;
        float Temperature(z) ;
            Temperature:long_name = "Temperature" ;
            Temperature:standard_name = "sea_water_temperature" ;
            Temperature:units = "degree_C" ;
            Temperature:coordinates = "time lat lon z" ;
            Temperature:grid_mapping = "crs" ;
        short Temperature_sigfigs(z) ;
        short Temperature_WODflag(z) ;
            Temperature_WODflag:flag_definitions = "WODf" ;
        short Temperature_WODprofileflag ;
            Temperature_WODprofileflag:flag_definitions = "WODfp" ;
        float Salinity(z) ;
            Salinity:long_name = "Salinity" ;
            Salinity:standard_name = "sea_water_salinity" ;
        short Salinity_sigfigs(z) ;
        short Salinity_WODflag(z) ;
            Salinity_WODflag:flag_definitions = "WODf" ;
        short Salinity_WODprofileflag ;
            Salinity_WODprofileflag:flag_definitions = "WODfp" ;
        float Oxygen(z) ;
            Oxygen:long_name = "Oxygen" ;
            Oxygen:standard_name = "volume_fraction_of_oxygen_in_sea_water" ;
            Oxygen:units = "umol/kg" ;
            Oxygen:coordinates = "time lat lon z" ;
            Oxygen:grid_mapping = "crs" ;
        short Oxygen_sigfigs(z) ;
        short Oxygen_WODflag(z) ;
            Oxygen_WODflag:flag_definitions = "WODf" ;
        short Oxygen_WODprofileflag ;
            Oxygen_WODprofileflag:flag_definitions = "WODfp" ;
        char Oxygen_Original_units(strnlen) ;
            Oxygen_Original_units:comment = "Units originally used: coverted to standard units" ;
        float Phosphate(z) ;
            Phosphate:long_name = "Phosphate" ;
            Phosphate:standard_name = "mole_concentration_of_phosphate_in_sea_water" ;
            Phosphate:units = "umol/kg" ;
            Phosphate:coordinates = "time lat lon z" ;
            Phosphate:grid_mapping = "crs" ;
        short Phosphate_sigfigs(z) ;
        short Phosphate_WODflag(z) ;
            Phosphate_WODflag:flag_definitions = "WODf" ;
        short Phosphate_WODprofileflag ;
            Phosphate_WODprofileflag:flag_definitions = "WODfp" ;
        char Phosphate_Original_units(strnlen) ;
            Phosphate_Original_units:comment = "Units originally used: coverted to standard units" ;
        int crs ;
            crs:grid_mapping_name = "latitude_longitude" ;
            crs:epsg_code = "EPSG:4326" ;
            crs:longitude_of_prime_meridian = 0.f ;
            crs:semi_major_axis = 6378137.f ;
            crs:inverse_flattening = 298.2572f ;
        short WODf ;
            WODf:long_name = "WOD_observation_flag" ;
            WODf:flag_values = 0s, 1s, 2s, 3s, 4s, 5s, 6s, 7s, 8s, 9s ;
            WODf:flag_meanings = "accepted range_out inversion gradient anomaly gradient+inversion range+inversion range+gradient range+anomaly range+inversion+gradient" ;
        short WODfp ;
            WODfp:long_name = "WOD_profile_flag" ;
            WODfp:flag_values = 0s, 1s, 2s, 3s, 4s, 5s, 6s, 7s, 8s, 9s ;
            WODfp:flag_meanings = "accepted annual_sd_out density_inversion cruise seasonal_sd_out monthly_sd_out annual+seasonal_sd_out anomaly_or_annual+monthly_sd_out seasonal+monthly_sd_out annual+seasonal+monthly_sd_out" ;
        short WODfd ;
            WODfd:long_name = "WOD_depth_level_" ;
            WODfd:flag_values = 0s, 1s, 2s ;
            WODfd:flag_meanings = "accepted duplicate_or_inversion density_inversion" ;
    
    // global attributes:
            :institution = "National Oceanographic Data Center(NODC), NOAA" ;
            :source = "World Ocean Database" ;
            :references = "World Ocean Database 2013. URL:http://data.nodc.noaa.gov/woa/WOD/DOC/wod_intro.pdf" ;
            :title = "World Ocean Database - Unique Cast 000410903" ;
            :summary = "Data for single cast from the World Ocean Database" ;
            :id = "wod_000410903" ;
            :naming\ authority = "gov.noaa.nodc" ;
            :geospatial_lat_min = -32.66667f ;
            :geospatial_lat_max = -32.66667f ;
            :geospatial_lat_resolution = "point" ;
            :geospatial_lon_min = 14.56667f ;
            :geospatial_lon_max = 14.56667f ;
            :geospatial_lon_resolution = "point" ;
            :geospatial_vertical_min = 0.f ;
            :geospatial_vertical_max = 989.f ;
            :geospatial_vertical_positive = "down" ;
            :geospatial_vertical_units = "meters" ;
            :creator_name = "Ocean Climate Lab/NODC" ;
            :creator_email = "OCLhelp@noaa.gov" ;
            :creator_url = "http://www.nodc.noaa.gov" ;
            :project = "World Ocean Database" ;
            :acknowledgements = "" ;
            :processing_level = "" ;
            :keywords = "" ;
            :keywords_vocabulary = "" ;
            :date_created = "2018-11-06" ;
            :date_modified = "2018-11-06" ;
            :publisher_name = "US DOC; NESDIS; NATIONAL OCEANOGRAPHIC DATA CENTER - IN295" ;
            :publisher_url = "http://www.nodc.noaa.gov" ;
            :publisher_email = "NODC.Services@noaa.gov" ;
            :history = "" ;
            :license = "" ;
            :standard_name_vocabulary = "CF-1.6" ;
            :featureType = "Profile" ;
            :cdm_data_type = "Profile" ;
            :Conventions = "CF-1.6" ;
    }
    
    
    
    
    ###############################################################################
    bad_examples_62/bad_examples.R
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/bad_examples_62/
    bad_examples.R' had status 1
    
    
    
    
    ###############################################################################
    bad_examples_62/example1.nc
    
    
    
    netcdf example1 {
    dimensions:
        time = UNLIMITED ; // (1 currently)
        x = 97 ;
        y = 65 ;
    variables:
        double time(time) ;
            time:standard_name = "time" ;
            time:units = "days since 1949-12-01 00:00:00" ;
            time:calendar = "standard" ;
            time:axis = "T" ;
        double lon(y, x) ;
            lon:standard_name = "longitude" ;
            lon:long_name = "Longitude" ;
            lon:units = "degrees_east" ;
            lon:_CoordinateAxisType = "Lon" ;
        double lat(y, x) ;
            lat:standard_name = "latitude" ;
            lat:long_name = "Latitude" ;
            lat:units = "degrees_north" ;
            lat:_CoordinateAxisType = "Lat" ;
        double pr(time, y, x) ;
            pr:standard_name = "precipitation_flux" ;
            pr:long_name = "Precipitation" ;
            pr:units = "kg m-2 s-1" ;
            pr:coordinates = "lat lon" ;
            pr:_FillValue = 1.00000002004088e+20 ;
            pr:missing_value = 1.00000002004088e+20 ;
            pr:short_name = "pr" ;
    
    // global attributes:
            :CDI = "Climate Data Interface version 1.9.1 (http://mpimet.mpg.de/cdi)" ;
            :Conventions = "CF-1.4" ;
            :history = "Thu Oct 04 14:31:10 2018: cdo -C seltimestep,1 pr_PROMES_044_1989-2008.nc /dev/shm/example1.nc\n",
                "Fri Apr 10 15:12:41 2015: cdo selyear,1989/2008 pr_PROMES_044_1989-2009_gridOK.nc pr_PROMES_044_1989-2008.nc\n",
                "Fri Apr 10 15:05:19 2015: cdo setgrid,/home/clima-archive2/ctorma/MED-44/UCLM-PROMES/DD//pr_MED-44_ECMWF-ERAINT_evaluation_r1i1p1_UCLM-PROMES_v1_day_1994010100-1999010100.nc pr_PROMES_044_1989-2009.nc pr_PROMES_044_1989-2009_gridOK.nc\n",
                "Fri Apr 10 15:02:20 2015: cdo cat PROMES1_pr.nc PROMES2_pr.nc PROMES3_pr.nc PROMES4_pr.nc pr_PROMES_044_1989-2009.nc\n",
                "Fri Apr 10 15:02:09 2015: cdo selvar,pr /home/clima-archive2/ctorma/MED-44/UCLM-PROMES/DD//pr_MED-44_ECMWF-ERAINT_evaluation_r1i1p1_UCLM-PROMES_v1_day_1989010100-1994010100.nc PROMES1_pr.nc" ;
            :source = "PROMES model 2011" ;
            :institution = "University of Castilla-La Mancha, Toledo, España" ;
            :production = "Produced by PROMES 2009" ;
            :NCO = "20111211" ;
            :institute_id = "UCLM" ;
            :model_id = "PROMES" ;
            :project_id = "CORDEX" ;
            :driving_experiment = "ERA-INTERIM,evalutaion,r1i1p1" ;
            :driving_model_id = "ERAINT" ;
            :driving_model_ensemble_member = "r1i1p1" ;
            :driving_experiment_name = "evaluation" ;
            :experiment_id = "evaluation" ;
            :CORDEX_domain = "MED-44" ;
            :creation_date = "2011-09-15-T05:56:23Z" ;
            :nco_openmp_thread_number = 1 ;
            :frequency = "day" ;
            :CDO = "Climate Data Operators version 1.9.1 (http://mpimet.mpg.de/cdo)" ;
    }
    
    
    
    
    ###############################################################################
    bad_examples_62/example2.nc
    
    
    
    netcdf example2 {
    dimensions:
        time = UNLIMITED ; // (1 currently)
        bnds = 2 ;
        rlon = 98 ;
        rlat = 63 ;
    variables:
        double time(time) ;
            time:standard_name = "time" ;
            time:long_name = "time" ;
            time:bounds = "time_bnds" ;
            time:units = "days since 1949-12-01 00:00:00" ;
            time:calendar = "proleptic_gregorian" ;
            time:axis = "T" ;
        double time_bnds(time, bnds) ;
        float rlon(rlon) ;
            rlon:standard_name = "grid_longitude" ;
            rlon:long_name = "rotated longitude" ;
            rlon:units = "degrees" ;
            rlon:axis = "X" ;
        float rlat(rlat) ;
            rlat:standard_name = "grid_latitude" ;
            rlat:long_name = "rotated latitude" ;
            rlat:units = "degrees" ;
            rlat:axis = "Y" ;
        int rotated_pole ;
            rotated_pole:grid_mapping_name = "rotated_latitude_longitude" ;
            rotated_pole:grid_north_pole_latitude = 39.25 ;
            rotated_pole:grid_north_pole_longitude = -162. ;
        float pr(time, rlat, rlon) ;
            pr:standard_name = "precipitation_flux" ;
            pr:long_name = "Precipitation" ;
            pr:units = "kg m-2 s-1" ;
            pr:grid_mapping = "rotated_pole" ;
            pr:cell_methods = "time: mean" ;
            pr:original_name = "TOT_PREC" ;
    
    // global attributes:
            :CDI = "Climate Data Interface version 1.9.1 (http://mpimet.mpg.de/cdi)" ;
            :history = "Thu Oct 04 14:31:20 2018: cdo -C seltimestep,1 pr_GUF-CCLM_044_1989-2008.nc /dev/shm/example2.nc\n",
                "Fri Apr 10 10:50:33 2015: cdo selyear,1989/2008 pr_GUF-CCLM_044_allyears.nc pr_GUF-CCLM_044_1989-2008.nc\n",
                "Fri Apr 10 10:31:07 2015: cdo cat /home/clima-archive2/ctorma/MED-44/GUF-CCLM4-8-18/DD/pr_MED-44_ECMWF-ERAINT_evaluation_r1i1p1_GUF-CCLM4-8-18_v1_day_1979010100-1979020100.nc /home/clima-archive2/ctorma/MED-44/GUF-CCLM4-8-18/DD/pr_MED-44_ECMWF-ERAINT_evaluation_r1i1p1_GUF-CCLM4-8-18_v1_day_1979020100-1979030100.nc /home/clima-archive2/ctorma/MED-44/GUF-CCLM4-8-18/DD/pr_MED-44_ECMWF-ERAINT_evaluation_r1i1p1_GUF-CCLM4-8-18_v1_day_1979030100-1979040100.nc /home/clima-archive2/ctorma/MED-44/GUF-CCLM4-8-18/DD/pr_MED-44_ECMWF-ERAINT_evaluation_r1i1p1_GUF-CCLM4-8-18_v1_day_1979040100-1979050100.nc /home/clima-archive2/ctorma/MED-44/GUF-CCLM4-8-18/DD/pr_MED-44_ECMWF-ERAINT_evaluation_r1i1p1_GUF-CCLM4-8-18_v1_day_1979050100-1979060100.nc /home/clima-archive2/ctorma/MED-44/GUF-CCLM4-8-18/DD/pr_MED-44_ECMWF-ERAINT_evaluation_r1i1p1_GUF-CCLM4-8-18_v1_day_1979060100-1979070100.nc /home/clima-archive2/ctorma/MED-44/GUF-CCLM4-8-18/DD/pr_MED-44_ECMWF-ERAINT_evaluation_r1i1p1_GUF-CCLM4-8-18_v1_day_1979070100-1979080100.nc\n",
                "Fri Sep 06 09:52:34 2013: cdo -s -r setreftime,1949-12-01,00:00 -settaxis,1979-01-01,12:00,1day pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc.tmp1 pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncks -F -O -a -x -v time_bnds pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc.tmp1\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a calendar,time_bnds,d,, pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a long_name,time_bnds,c,c,time bounds pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a long_name,time,c,c,time -a standard_name,time,c,c,time pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a source,global,o,c,cosmo_090213_4.8_clm18 pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a product,global,o,c,output pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a CORDEX_domain,global,c,c,MED-44 pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a project_id,global,o,c,CORDEX pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a rcm_version_id,global,c,c,v1 pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a model_id,global,c,c,CCLM4-8-18 pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a institute_id,global,c,c,GUF pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a institution,global,o,c,Climate Limited-area Modelling Community (CLM-Community) pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a frequency,global,c,c,day pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a driving_experiment_name,global,c,c,evaluation pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a driving_model_ensemble_member,global,c,c,r1i1p1 pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a driving_model_id,global,c,c,ECMWF-ERAINT pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a driving_experiment,global,c,c,ECMWF-ERAINT, evaluation, r1i1p1 pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a experiment_id,global,o,c,r1i1p1 pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a experiment,global,c,c,Evaluation run with reanalysis forcing pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a contact,global,o,c,kothe@iau.uni-frankfurt.de pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:52:34 2013: ncatted -O -a Conventions,global,o,c,CF-1.4 pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:51:12 2013: ncatted -O -a cell_methods,pr,o,c,time: mean pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep 06 09:51:12 2013: cdo -s shifttime,1min -daymean -shifttime,-1min /gpfs/ahrenshsmfs/archive/skothe/COSMO_4_8_18_MED_CORDEX_ERAINT_044_extended/CMOR/OUT/T2/pr_CCLM4-8-18_MED-44_1hr_1979010100_1979020100.nc pr_CCLM4-8-18_MED-44_day_1979010100_1979020100.nc\n",
                "Fri Sep  6 09:51:11 2013: ncatted -O -a cell_methods,pr,o,c,time: mean pr_CCLM4-8-18_MED-44_1hr_1979010100_1979020100.nc\n",
                "Fri Sep 06 09:51:11 2013: cdo -s divc,3600 lffd197901_T2_1hr_TOT_PREC.nc pr_CCLM4-8-18_MED-44_1hr_1979010100_1979020100.nc\n",
                "Fri Sep 06 09:51:10 2013: cdo -s seltimestep,2/745 lffd197901_T2_1hr_TOT_PREC.nc lffd197901_T2_1hr_TOT_PREC.tmp.nc\n",
                "Fri Sep  6 09:51:10 2013: ncatted -O -a units,pr,o,c,kg m-2 s-1 lffd197901_T2_1hr_TOT_PREC.nc\n",
                "Fri Sep  6 09:51:09 2013: ncatted -O -a standard_name,pr,o,c,precipitation_flux lffd197901_T2_1hr_TOT_PREC.nc\n",
                "Fri Sep  6 09:51:09 2013: ncatted -O -a original_name,pr,c,c,TOT_PREC lffd197901_T2_1hr_TOT_PREC.nc\n",
                "Fri Sep  6 09:51:09 2013: ncatted -O -a long_name,pr,o,c,Precipitation lffd197901_T2_1hr_TOT_PREC.nc\n",
                "Fri Sep  6 09:51:09 2013: ncrename -v TOT_PREC,pr lffd197901_T2_1hr_TOT_PREC.nc\n",
                "Fri Sep 06 09:51:09 2013: cdo -s selname,TOT_PREC lffd197901.nc lffd197901_T2_1hr_TOT_PREC.nc\n",
                "Fri Sep  6 09:51:05 2013: ncks -O -F -d rlon,9,106 -d rlat,9,71 /gpfs/ahrenshsmfs/archive/skothe/COSMO_4_8_18_MED_CORDEX_ERAINT_044_extended/out03/lffd1979010100.nc lffd1979010100.nc\n",
                "2013-09-06 09:52 : add_bounds: time bounds added" ;
            :institution = "Climate Limited-area Modelling Community (CLM-Community)" ;
            :Conventions = "CF-1.4" ;
            :title = "COSMO_CLM_4.8 simulation (0.44 Deg) with ERAInt present day forcing" ;
            :project_id = "CORDEX" ;
            :experiment_id = "r1i1p1" ;
            :realization = 1 ;
            :conventionsURL = "http://www.unidata.ucar.edu/packages/netcdf/conventions.html" ;
            :contact = "kothe@iau.uni-frankfurt.de" ;
            :references = "http//www.clm-community.eu, http://www.geo.uni-frankfurt.de/iau/meso/" ;
            :creation_date = "2013-03-31 19:25:58" ;
            :experiment = "Evaluation run with reanalysis forcing" ;
            :driving_experiment = "ECMWF-ERAINT, evaluation, r1i1p1" ;
            :driving_model_id = "ECMWF-ERAINT" ;
            :driving_model_ensemble_member = "r1i1p1" ;
            :driving_experiment_name = "evaluation" ;
            :frequency = "day" ;
            :institute_id = "GUF" ;
            :model_id = "CCLM4-8-18" ;
            :rcm_version_id = "v1" ;
            :CORDEX_domain = "MED-44" ;
            :product = "output" ;
            :CDO = "Climate Data Operators version 1.9.1 (http://mpimet.mpg.de/cdo)" ;
    }
    
    
    
    
    ###############################################################################
    bad_examples_62/example3.nc
    
    
    
    netcdf example3 {
    dimensions:
        time = UNLIMITED ; // (1 currently)
        X = 243 ;
        Y = 138 ;
    variables:
        double time(time) ;
            time:standard_name = "time" ;
            time:long_name = "time" ;
            time:units = "days since 1900-01-01 00:00:00" ;
            time:calendar = "standard" ;
            time:axis = "T" ;
        float lon(Y, X) ;
            lon:standard_name = "longitude" ;
            lon:long_name = "longitude coordinate" ;
            lon:units = "degrees_east" ;
            lon:_CoordinateAxisType = "Lon" ;
        float lat(Y, X) ;
            lat:standard_name = "latitude" ;
            lat:long_name = "latitude coordinate" ;
            lat:units = "degrees_north" ;
            lat:_CoordinateAxisType = "Lat" ;
        double X(X) ;
            X:standard_name = "projection_x_coordinate" ;
            X:long_name = "x coordinate of projection" ;
            X:units = "meters" ;
            X:axis = "X" ;
        double Y(Y) ;
            Y:standard_name = "projection_y_coordinate" ;
            Y:long_name = "y coordinate of projection" ;
            Y:units = "meters" ;
            Y:axis = "Y" ;
        int ETRS89-LAEA ;
            ETRS89-LAEA:missing_value = -1. ;
            ETRS89-LAEA:grid_mapping_name = "lambert_azimuthal_equal_area" ;
            ETRS89-LAEA:longitude_of_projection_origin = 10. ;
            ETRS89-LAEA:latitude_of_projection_origin = 52. ;
            ETRS89-LAEA:false_easting = 4321000. ;
            ETRS89-LAEA:false_northing = 3210000. ;
            ETRS89-LAEA:inverse_flattening = 298.257222101 ;
            ETRS89-LAEA:semi_major_axis = 6378137. ;
        float pr(time, Y, X) ;
            pr:long_name = "PRECIPITATION" ;
            pr:units = "mm.d-1" ;
            pr:grid_mapping = "ETRS89-LAEA" ;
            pr:coordinates = "lat lon" ;
            pr:_FillValue = -999.99f ;
            pr:missing_value = -999.99f ;
            pr:grid_name = "al05.etrs.laea" ;
            pr:version = "v1.2" ;
            pr:prod_date = "2013-07-15" ;
    
    // global attributes:
            :CDI = "Climate Data Interface version 1.9.1 (http://mpimet.mpg.de/cdi)" ;
            :history = "Thu Oct 04 14:37:21 2018: cdo -C seltimestep,1 /home/esp-shared-a/Observations/EURO4M-APGD/EURO4M-APGD-1971-2008.nc example3.nc\n",
                "Fri Nov  1 13:32:07 2013: ncrename -v PRECIPITATION,pr EURO4M-APGD-1971-2008.nc\n",
                "Fri Nov  1 13:29:54 2013: ncrcat RapdD_al05.etrs.laea_19710100.nc RapdD_al05.etrs.laea_19710200.nc RapdD_al05.etrs.laea_19710300.nc RapdD_al05.etrs.laea_19710400.nc RapdD_al05.etrs.laea_19710500.nc RapdD_al05.etrs.laea_19710600.nc RapdD_al05.etrs.laea_19710700.nc RapdD_al05.etrs.laea_19710800.nc RapdD_al05.etrs.laea_19710900.nc RapdD_al05.etrs.laea_19711000.nc RapdD_al05.etrs.laea_19711100.nc RapdD_al05.etrs.laea_19711200.nc RapdD_al05.etrs.laea_19720100.nc RapdD_al05.etrs.laea_19720200.nc RapdD_al05.etrs.laea_19720300.nc RapdD_al05.etrs.laea_19720400.nc RapdD_al05.etrs.laea_19720500.nc RapdD_al05.etrs.laea_19720600.nc RapdD_al05.etrs.laea_19720700.nc RapdD_al05.etrs.laea_19720800.nc RapdD_al05.etrs.laea_19720900.nc RapdD_al05.etrs.laea_19721000.nc RapdD_al05.etrs.laea_19721100.nc RapdD_al05.etrs.laea_19721200.nc RapdD_al05.etrs.laea_19730100.nc RapdD_al05.etrs.laea_19730200.nc RapdD_al05.etrs.laea_19730300.nc RapdD_al05.etrs.laea_19730400.nc RapdD_al05.etrs.laea_19730500.nc RapdD_al05.etrs.laea_19730600.nc RapdD_al05.etrs.laea_19730700.nc RapdD_al05.etrs.laea_19730800.nc RapdD_al05.etrs.laea_19730900.nc RapdD_al05.etrs.laea_19731000.nc RapdD_al05.etrs.laea_19731100.nc RapdD_al05.etrs.laea_19731200.nc RapdD_al05.etrs.laea_19740100.nc RapdD_al05.etrs.laea_19740200.nc RapdD_al05.etrs.laea_19740300.nc RapdD_al05.etrs.laea_19740400.nc RapdD_al05.etrs.laea_19740500.nc RapdD_al05.etrs.laea_19740600.nc RapdD_al05.etrs.laea_19740700.nc RapdD_al05.etrs.laea_19740800.nc RapdD_al05.etrs.laea_19740900.nc RapdD_al05.etrs.laea_19741000.nc RapdD_al05.etrs.laea_19741100.nc RapdD_al05.etrs.laea_19741200.nc RapdD_al05.etrs.laea_19750100.nc RapdD_al05.etrs.laea_19750200.nc RapdD_al05.etrs.laea_19750300.nc RapdD_al05.etrs.laea_19750400.nc RapdD_al05.etrs.laea_19750500.nc RapdD_al05.etrs.laea_19750600.nc RapdD_al05.etrs.laea_19750700.nc RapdD_al05.etrs.laea_19750800.nc RapdD_al05.etrs.laea_19750900.nc RapdD_al05.etrs.laea_19751000.nc RapdD_al05.etrs.laea_19751100.nc RapdD_al05.etrs.laea_19751200.nc RapdD_al05.etrs.laea_19760100.nc RapdD_al05.etrs.laea_19760200.nc RapdD_al05.etrs.laea_19760300.nc RapdD_al05.etrs.laea_19760400.nc RapdD_al05.etrs.laea_19760500.nc RapdD_al05.etrs.laea_19760600.nc RapdD_al05.etrs.laea_19760700.nc RapdD_al05.etrs.laea_19760800.nc RapdD_al05.etrs.laea_19760900.nc RapdD_al05.etrs.laea_19761000.nc RapdD_al05.etrs.laea_19761100.nc RapdD_al05.etrs.laea_19761200.nc RapdD_al05.etrs.laea_19770100.nc RapdD_al05.etrs.laea_19770200.nc RapdD_al05.etrs.laea_19770300.nc RapdD_al05.etrs.laea_19770400.nc RapdD_al05.etrs.laea_19770500.nc RapdD_al05.etrs.laea_19770600.nc RapdD_al05.etrs.laea_19770700.nc RapdD_al05.etrs.laea_19770800.nc RapdD_al05.etrs.laea_19770900.nc RapdD_al05.etrs.laea_19771000.nc RapdD_al05.etrs.laea_19771100.nc RapdD_al05.etrs.laea_19771200.nc RapdD_al05.etrs.laea_19780100.nc RapdD_al05.etrs.laea_19780200.nc RapdD_al05.etrs.laea_19780300.nc RapdD_al05.etrs.laea_19780400.nc RapdD_al05.etrs.laea_19780500.nc RapdD_al05.etrs.laea_19780600.nc RapdD_al05.etrs.laea_19780700.nc RapdD_al05.etrs.laea_19780800.nc RapdD_al05.etrs.laea_19780900.nc RapdD_al05.etrs.laea_19781000.nc RapdD_al05.etrs.laea_19781100.nc RapdD_al05.etrs.laea_19781200.nc RapdD_al05.etrs.laea_19790100.nc RapdD_al05.etrs.laea_19790200.nc RapdD_al05.etrs.laea_19790300.nc RapdD_al05.etrs.laea_19790400.nc RapdD_al05.etrs.laea_19790500.nc RapdD_al05.etrs.laea_19790600.nc RapdD_al05.etrs.laea_19790700.nc RapdD_al05.etrs.laea_19790800.nc RapdD_al05.etrs.laea_19790900.nc RapdD_al05.etrs.laea_19791000.nc RapdD_al05.etrs.laea_19791100.nc RapdD_al05.etrs.laea_19791200.nc RapdD_al05.etrs.laea_19800100.nc RapdD_al05.etrs.laea_19800200.nc RapdD_al05.etrs.laea_19800300.nc RapdD_al05.etrs.laea_19800400.nc RapdD_al05.etrs.laea_19800500.nc RapdD_al05.etrs.laea_19800600.nc RapdD_al05.etrs.laea_19800700.nc RapdD_al05.etrs.laea_19800800.nc RapdD_al05.etrs.laea_19800900.nc RapdD_al05.etrs.laea_19801000.nc RapdD_al05.etrs.laea_19801100.nc RapdD_al05.etrs.laea_19801200.nc RapdD_al05.etrs.laea_19810100.nc RapdD_al05.etrs.laea_19810200.nc RapdD_al05.etrs.laea_19810300.nc RapdD_al05.etrs.laea_19810400.nc RapdD_al05.etrs.laea_19810500.nc RapdD_al05.etrs.laea_19810600.nc RapdD_al05.etrs.laea_19810700.nc RapdD_al05.etrs.laea_19810800.nc RapdD_al05.etrs.laea_19810900.nc RapdD_al05.etrs.laea_19811000.nc RapdD_al05.etrs.laea_19811100.nc RapdD_al05.etrs.laea_19811200.nc RapdD_al05.etrs.laea_19820100.nc RapdD_al05.etrs.laea_19820200.nc RapdD_al05.etrs.laea_19820300.nc RapdD_al05.etrs.laea_19820400.nc RapdD_al05.etrs.laea_19820500.nc RapdD_al05.etrs.laea_19820600.nc RapdD_al05.etrs.laea_19820700.nc RapdD_al05.etrs.laea_19820800.nc RapdD_al05.etrs.laea_19820900.nc RapdD_al05.etrs.laea_19821000.nc RapdD_al05.etrs.laea_19821100.nc RapdD_al05.etrs.laea_19821200.nc RapdD_al05.etrs.laea_19830100.nc RapdD_al05.etrs.laea_19830200.nc RapdD_al05.etrs.laea_19830300.nc RapdD_al05.etrs.laea_19830400.nc RapdD_al05.etrs.laea_19830500.nc RapdD_al05.etrs.laea_19830600.nc RapdD_al05.etrs.laea_19830700.nc RapdD_al05.etrs.laea_19830800.nc RapdD_al05.etrs.laea_19830900.nc RapdD_al05.etrs.laea_19831000.nc RapdD_al05.etrs.laea_19831100.nc RapdD_al05.etrs.laea_19831200.nc RapdD_al05.etrs.laea_19840100.nc RapdD_al05.etrs.laea_19840200.nc RapdD_al05.etrs.laea_19840300.nc RapdD_al05.etrs.laea_19840400.nc RapdD_al05.etrs.laea_19840500.nc RapdD_al05.etrs.laea_19840600.nc RapdD_al05.etrs.laea_19840700.nc RapdD_al05.etrs.laea_19840800.nc RapdD_al05.etrs.laea_19840900.nc RapdD_al05.etrs.laea_19841000.nc RapdD_al05.etrs.laea_19841100.nc RapdD_al05.etrs.laea_19841200.nc RapdD_al05.etrs.laea_19850100.nc RapdD_al05.etrs.laea_19850200.nc RapdD_al05.etrs.laea_19850300.nc RapdD_al05.etrs.laea_19850400.nc RapdD_al05.etrs.laea_19850500.nc RapdD_al05.etrs.laea_19850600.nc RapdD_al05.etrs.laea_19850700.nc RapdD_al05.etrs.laea_19850800.nc RapdD_al05.etrs.laea_19850900.nc RapdD_al05.etrs.laea_19851000.nc RapdD_al05.etrs.laea_19851100.nc RapdD_al05.etrs.laea_19851200.nc RapdD_al05.etrs.laea_19860100.nc RapdD_al05.etrs.laea_19860200.nc RapdD_al05.etrs.laea_19860300.nc RapdD_al05.etrs.laea_19860400.nc RapdD_al05.etrs.laea_19860500.nc RapdD_al05.etrs.laea_19860600.nc RapdD_al05.etrs.laea_19860700.nc RapdD_al05.etrs.laea_19860800.nc RapdD_al05.etrs.laea_19860900.nc RapdD_al05.etrs.laea_19861000.nc RapdD_al05.etrs.laea_19861100.nc RapdD_al05.etrs.laea_19861200.nc RapdD_al05.etrs.laea_19870100.nc RapdD_al05.etrs.laea_19870200.nc RapdD_al05.etrs.laea_19870300.nc RapdD_al05.etrs.laea_19870400.nc RapdD_al05.etrs.laea_19870500.nc RapdD_al05.etrs.laea_19870600.nc RapdD_al05.etrs.laea_19870700.nc RapdD_al05.etrs.laea_19870800.nc RapdD_al05.etrs.laea_19870900.nc RapdD_al05.etrs.laea_19871000.nc RapdD_al05.etrs.laea_19871100.nc RapdD_al05.etrs.laea_19871200.nc RapdD_al05.etrs.laea_19880100.nc RapdD_al05.etrs.laea_19880200.nc RapdD_al05.etrs.laea_19880300.nc RapdD_al05.etrs.laea_19880400.nc RapdD_al05.etrs.laea_19880500.nc RapdD_al05.etrs.laea_19880600.nc RapdD_al05.etrs.laea_19880700.nc RapdD_al05.etrs.laea_19880800.nc RapdD_al05.etrs.laea_19880900.nc RapdD_al05.etrs.laea_19881000.nc RapdD_al05.etrs.laea_19881100.nc RapdD_al05.etrs.laea_19881200.nc RapdD_al05.etrs.laea_19890100.nc RapdD_al05.etrs.laea_19890200.nc RapdD_al05.etrs.laea_19890300.nc RapdD_al05.etrs.laea_19890400.nc RapdD_al05.etrs.laea_19890500.nc RapdD_al05.etrs.laea_19890600.nc RapdD_al05.etrs.laea_19890700.nc RapdD_al05.etrs.laea_19890800.nc RapdD_al05.etrs.laea_19890900.nc RapdD_al05.etrs.laea_19891000.nc RapdD_al05.etrs.laea_19891100.nc RapdD_al05.etrs.laea_19891200.nc RapdD_al05.etrs.laea_19900100.nc RapdD_al05.etrs.laea_19900200.nc RapdD_al05.etrs.laea_19900300.nc RapdD_al05.etrs.laea_19900400.nc RapdD_al05.etrs.laea_19900500.nc RapdD_al05.etrs.laea_19900600.nc RapdD_al05.etrs.laea_19900700.nc RapdD_al05.etrs.laea_19900800.nc RapdD_al05.etrs.laea_19900900.nc RapdD_al05.etrs.laea_19901000.nc RapdD_al05.etrs.laea_19901100.nc RapdD_al05.etrs.laea_19901200.nc RapdD_al05.etrs.laea_19910100.nc RapdD_al05.etrs.laea_19910200.nc RapdD_al05.etrs.laea_19910300.nc RapdD_al05.etrs.laea_19910400.nc RapdD_al05.etrs.laea_19910500.nc RapdD_al05.etrs.laea_19910600.nc RapdD_al05.etrs.laea_19910700.nc RapdD_al05.etrs.laea_19910800.nc RapdD_al05.etrs.laea_19910900.nc RapdD_al05.etrs.laea_19911000.nc RapdD_al05.etrs.laea_19911100.nc RapdD_al05.etrs.laea_19911200.nc RapdD_al05.etrs.laea_19920100.nc RapdD_al05.etrs.laea_19920200.nc RapdD_al05.etrs.laea_19920300.nc RapdD_al05.etrs.laea_19920400.nc RapdD_al05.etrs.laea_19920500.nc RapdD_al05.etrs.laea_19920600.nc RapdD_al05.etrs.laea_19920700.nc RapdD_al05.etrs.laea_19920800.nc RapdD_al05.etrs.laea_19920900.nc RapdD_al05.etrs.laea_19921000.nc RapdD_al05.etrs.laea_19921100.nc RapdD_al05.etrs.laea_19921200.nc RapdD_al05.etrs.laea_19930100.nc RapdD_al05.etrs.laea_19930200.nc RapdD_al05.etrs.laea_19930300.nc RapdD_al05.etrs.laea_19930400.nc RapdD_al05.etrs.laea_19930500.nc RapdD_al05.etrs.laea_19930600.nc RapdD_al05.etrs.laea_19930700.nc RapdD_al05.etrs.laea_19930800.nc RapdD_al05.etrs.laea_19930900.nc RapdD_al05.etrs.laea_19931000.nc RapdD_al05.etrs.laea_19931100.nc RapdD_al05.etrs.laea_19931200.nc RapdD_al05.etrs.laea_19940100.nc RapdD_al05.etrs.laea_19940200.nc RapdD_al05.etrs.laea_19940300.nc RapdD_al05.etrs.laea_19940400.nc RapdD_al05.etrs.laea_19940500.nc RapdD_al05.etrs.laea_19940600.nc RapdD_al05.etrs.laea_19940700.nc RapdD_al05.etrs.laea_19940800.nc RapdD_al05.etrs.laea_19940900.nc RapdD_al05.etrs.laea_19941000.nc RapdD_al05.etrs.laea_19941100.nc RapdD_al05.etrs.laea_19941200.nc RapdD_al05.etrs.laea_19950100.nc RapdD_al05.etrs.laea_19950200.nc RapdD_al05.etrs.laea_19950300.nc RapdD_al05.etrs.laea_19950400.nc RapdD_al05.etrs.laea_19950500.nc RapdD_al05.etrs.laea_19950600.nc RapdD_al05.etrs.laea_19950700.nc RapdD_al05.etrs.laea_19950800.nc RapdD_al05.etrs.laea_19950900.nc RapdD_al05.etrs.laea_19951000.nc RapdD_al05.etrs.laea_19951100.nc RapdD_al05.etrs.laea_19951200.nc RapdD_al05.etrs.laea_19960100.nc RapdD_al05.etrs.laea_19960200.nc RapdD_al05.etrs.laea_19960300.nc RapdD_al05.etrs.laea_19960400.nc RapdD_al05.etrs.laea_19960500.nc RapdD_al05.etrs.laea_19960600.nc RapdD_al05.etrs.laea_19960700.nc RapdD_al05.etrs.laea_19960800.nc RapdD_al05.etrs.laea_19960900.nc RapdD_al05.etrs.laea_19961000.nc RapdD_al05.etrs.laea_19961100.nc RapdD_al05.etrs.laea_19961200.nc RapdD_al05.etrs.laea_19970100.nc RapdD_al05.etrs.laea_19970200.nc RapdD_al05.etrs.laea_19970300.nc RapdD_al05.etrs.laea_19970400.nc RapdD_al05.etrs.laea_19970500.nc RapdD_al05.etrs.laea_19970600.nc RapdD_al05.etrs.laea_19970700.nc RapdD_al05.etrs.laea_19970800.nc RapdD_al05.etrs.laea_19970900.nc RapdD_al05.etrs.laea_19971000.nc RapdD_al05.etrs.laea_19971100.nc RapdD_al05.etrs.laea_19971200.nc RapdD_al05.etrs.laea_19980100.nc RapdD_al05.etrs.laea_19980200.nc RapdD_al05.etrs.laea_19980300.nc RapdD_al05.etrs.laea_19980400.nc RapdD_al05.etrs.laea_19980500.nc RapdD_al05.etrs.laea_19980600.nc RapdD_al05.etrs.laea_19980700.nc RapdD_al05.etrs.laea_19980800.nc RapdD_al05.etrs.laea_19980900.nc RapdD_al05.etrs.laea_19981000.nc RapdD_al05.etrs.laea_19981100.nc RapdD_al05.etrs.laea_19981200.nc RapdD_al05.etrs.laea_19990100.nc RapdD_al05.etrs.laea_19990200.nc RapdD_al05.etrs.laea_19990300.nc RapdD_al05.etrs.laea_19990400.nc RapdD_al05.etrs.laea_19990500.nc RapdD_al05.etrs.laea_19990600.nc RapdD_al05.etrs.laea_19990700.nc RapdD_al05.etrs.laea_19990800.nc RapdD_al05.etrs.laea_19990900.nc RapdD_al05.etrs.laea_19991000.nc RapdD_al05.etrs.laea_19991100.nc RapdD_al05.etrs.laea_19991200.nc RapdD_al05.etrs.laea_20000100.nc RapdD_al05.etrs.laea_20000200.nc RapdD_al05.etrs.laea_20000300.nc RapdD_al05.etrs.laea_20000400.nc RapdD_al05.etrs.laea_20000500.nc RapdD_al05.etrs.laea_20000600.nc RapdD_al05.etrs.laea_20000700.nc RapdD_al05.etrs.laea_20000800.nc RapdD_al05.etrs.laea_20000900.nc RapdD_al05.etrs.laea_20001000.nc RapdD_al05.etrs.laea_20001100.nc RapdD_al05.etrs.laea_20001200.nc RapdD_al05.etrs.laea_20010100.nc RapdD_al05.etrs.laea_20010200.nc RapdD_al05.etrs.laea_20010300.nc RapdD_al05.etrs.laea_20010400.nc RapdD_al05.etrs.laea_20010500.nc RapdD_al05.etrs.laea_20010600.nc RapdD_al05.etrs.laea_20010700.nc RapdD_al05.etrs.laea_20010800.nc RapdD_al05.etrs.laea_20010900.nc RapdD_al05.etrs.laea_20011000.nc RapdD_al05.etrs.laea_20011100.nc RapdD_al05.etrs.laea_20011200.nc RapdD_al05.etrs.laea_20020100.nc RapdD_al05.etrs.laea_20020200.nc RapdD_al05.etrs.laea_20020300.nc RapdD_al05.etrs.laea_20020400.nc RapdD_al05.etrs.laea_20020500.nc RapdD_al05.etrs.laea_20020600.nc RapdD_al05.etrs.laea_20020700.nc RapdD_al05.etrs.laea_20020800.nc RapdD_al05.etrs.laea_20020900.nc RapdD_al05.etrs.laea_20021000.nc RapdD_al05.etrs.laea_20021100.nc RapdD_al05.etrs.laea_20021200.nc RapdD_al05.etrs.laea_20030100.nc RapdD_al05.etrs.laea_20030200.nc RapdD_al05.etrs.laea_20030300.nc RapdD_al05.etrs.laea_20030400.nc RapdD_al05.etrs.laea_20030500.nc RapdD_al05.etrs.laea_20030600.nc RapdD_al05.etrs.laea_20030700.nc RapdD_al05.etrs.laea_20030800.nc RapdD_al05.etrs.laea_20030900.nc RapdD_al05.etrs.laea_20031000.nc RapdD_al05.etrs.laea_20031100.nc RapdD_al05.etrs.laea_20031200.nc RapdD_al05.etrs.laea_20040100.nc RapdD_al05.etrs.laea_20040200.nc RapdD_al05.etrs.laea_20040300.nc RapdD_al05.etrs.laea_20040400.nc RapdD_al05.etrs.laea_20040500.nc RapdD_al05.etrs.laea_20040600.nc RapdD_al05.etrs.laea_20040700.nc RapdD_al05.etrs.laea_20040800.nc RapdD_al05.etrs.laea_20040900.nc RapdD_al05.etrs.laea_20041000.nc RapdD_al05.etrs.laea_20041100.nc RapdD_al05.etrs.laea_20041200.nc RapdD_al05.etrs.laea_20050100.nc RapdD_al05.etrs.laea_20050200.nc RapdD_al05.etrs.laea_20050300.nc RapdD_al05.etrs.laea_20050400.nc RapdD_al05.etrs.laea_20050500.nc RapdD_al05.etrs.laea_20050600.nc RapdD_al05.etrs.laea_20050700.nc RapdD_al05.etrs.laea_20050800.nc RapdD_al05.etrs.laea_20050900.nc RapdD_al05.etrs.laea_20051000.nc RapdD_al05.etrs.laea_20051100.nc RapdD_al05.etrs.laea_20051200.nc RapdD_al05.etrs.laea_20060100.nc RapdD_al05.etrs.laea_20060200.nc RapdD_al05.etrs.laea_20060300.nc RapdD_al05.etrs.laea_20060400.nc RapdD_al05.etrs.laea_20060500.nc RapdD_al05.etrs.laea_20060600.nc RapdD_al05.etrs.laea_20060700.nc RapdD_al05.etrs.laea_20060800.nc RapdD_al05.etrs.laea_20060900.nc RapdD_al05.etrs.laea_20061000.nc RapdD_al05.etrs.laea_20061100.nc RapdD_al05.etrs.laea_20061200.nc RapdD_al05.etrs.laea_20070100.nc RapdD_al05.etrs.laea_20070200.nc RapdD_al05.etrs.laea_20070300.nc RapdD_al05.etrs.laea_20070400.nc RapdD_al05.etrs.laea_20070500.nc RapdD_al05.etrs.laea_20070600.nc RapdD_al05.etrs.laea_20070700.nc RapdD_al05.etrs.laea_20070800.nc RapdD_al05.etrs.laea_20070900.nc RapdD_al05.etrs.laea_20071000.nc RapdD_al05.etrs.laea_20071100.nc RapdD_al05.etrs.laea_20071200.nc RapdD_al05.etrs.laea_20080100.nc RapdD_al05.etrs.laea_20080200.nc RapdD_al05.etrs.laea_20080300.nc RapdD_al05.etrs.laea_20080400.nc RapdD_al05.etrs.laea_20080500.nc RapdD_al05.etrs.laea_20080600.nc RapdD_al05.etrs.laea_20080700.nc RapdD_al05.etrs.laea_20080800.nc RapdD_al05.etrs.laea_20080900.nc RapdD_al05.etrs.laea_20081000.nc RapdD_al05.etrs.laea_20081100.nc RapdD_al05.etrs.laea_20081200.nc EURO4M-APGD-1971-2008.nc" ;
            :institution = "Federal Office of Meteorology and Climatology MeteoSwiss" ;
            :Conventions = "CF-1.4" ;
            :References = "Isotta, F.A. et al. 2013: The climate of daily precipitation in the Alps: development and analysis of a high-resolution grid dataset from pan-Alpine rain-gauge data. Int. J. Climatol., accepted. Please check for updates on the publication status!" ;
            :nco_openmp_thread_number = 1 ;
            :CDO = "Climate Data Operators version 1.9.1 (http://mpimet.mpg.de/cdo)" ;
    }
    
    
    
    
    ###############################################################################
    copernicus/cout-perc1_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap0.5.nc
    
    
    
    netcdf cout-perc1_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap0.5 {
    dimensions:
        lat = 78 ;
        lon = 130 ;
        time = UNLIMITED ; // (1 currently)
    variables:
        float lat(lat) ;
            lat:standard_name = "latitude" ;
            lat:long_name = "Latitude" ;
            lat:units = "degrees_north" ;
            lat:axis = "Y" ;
        float lon(lon) ;
            lon:standard_name = "longitude" ;
            lon:long_name = "Longitude" ;
            lon:units = "degrees_east" ;
            lon:axis = "X" ;
        double time(time) ;
            time:standard_name = "time" ;
            time:units = "days since 1951-01-01 00:00:00" ;
            time:calendar = "proleptic_gregorian" ;
        float value1(time, lat, lon) ;
            value1:units = "m-3 s-1" ;
            value1:_FillValue = -1.e+20f ;
            value1:original_name = "dis" ;
        float value10(time, lat, lon) ;
            value10:units = "m3 s-1" ;
            value10:_FillValue = -1.e+20f ;
            value10:original_name = "dis" ;
        float value11(time, lat, lon) ;
            value11:units = "m3 s-1" ;
            value11:_FillValue = -1.e+20f ;
            value11:original_name = "dis" ;
        float value12(time, lat, lon) ;
            value12:units = "m3 s-1" ;
            value12:_FillValue = -1.e+20f ;
            value12:original_name = "dis" ;
        float value2(time, lat, lon) ;
            value2:units = "m-3 s-1" ;
            value2:_FillValue = -1.e+20f ;
            value2:original_name = "dis" ;
        float value3(time, lat, lon) ;
            value3:units = "m-3 s-1" ;
            value3:_FillValue = -1.e+20f ;
            value3:original_name = "dis" ;
        float value4(time, lat, lon) ;
            value4:units = "m-3 s-1" ;
            value4:_FillValue = -1.e+20f ;
            value4:original_name = "dis" ;
        float value5(time, lat, lon) ;
            value5:units = "m3 s-1" ;
            value5:_FillValue = -1.e+20f ;
            value5:original_name = "dis" ;
        float value6(time, lat, lon) ;
            value6:units = "m3 s-1" ;
            value6:_FillValue = -1.e+20f ;
            value6:original_name = "dis" ;
        float value7(time, lat, lon) ;
            value7:units = "m3 s-1" ;
            value7:_FillValue = -1.e+20f ;
            value7:original_name = "dis" ;
        float value8(time, lat, lon) ;
            value8:units = "m3 s-1" ;
            value8:_FillValue = -1.e+20f ;
            value8:original_name = "dis" ;
        float value9(time, lat, lon) ;
            value9:units = "m3 s-1" ;
            value9:_FillValue = -1.e+20f ;
            value9:original_name = "dis" ;
    
    // global attributes:
            :Conventions = "CF-1.4" ;
            :title = "Flow duration curve (1th percentile)" ;
            :description = "The flow duration curve (FDC) gives information about how frequently certain river flow rates occur.\n",
                "Here, the FDC is described through 13 percentiles of the distribution of daily river flows during a 30-\n",
                "year period:\n",
                "• 1 %\n",
                "• 5 %\n",
                "• 10 % to 90 % in steps of 10 %\n",
                "• 95 %\n",
                "• 99 %\n",
                "In case of the FDC for the full period, it is based on all daily data for a 30-year period. In the case of\n",
                "FDC’s seasonality, it is based on all daily data for a 30-year period that belong to the same month,\n",
                "evaluated for all 12 months of a year (i.e. all Januaries, all Februaries etc.)\n",
                "For the reference period (1971-2000) the absolute values are given, while for the future periods the\n",
                "relative changes are provided.\n",
                "The indicators described above are delivered in a large number of NetCDF-files. This file is a part of the delivery." ;
            :variable_name = "dis-perc1" ;
            :comment = "The climate impact indicators are based on hydrological impact modelling performed within the EU\n",
                "FP7 project IMPACT2C (grant agreement 282746). The full ensemble of time series from the model\n",
                "runs within the IMPACT2C archive is available in NetCDF format\n",
                "from http://ensemblesrt3.dmi.dk/data/impact2c-archive/MODELS/HYDROLOGY/.\n",
                "More information on the climate-model ensemble used (for instance model selection procedures,\n",
                "uncertainties, adjustments) can be found\n",
                "here: http://impact2c.hzg.de/imperia/md/content/csc/projekte/impact2c_d5.1_fin.pdf\n",
                "The hydrological models were driven by regional climate model (RCM) data. Within the EU FP7\n",
                "project IMPACT2C, the original RCM output data has been spatially interpolated, adjusted to the\n",
                "standard Gregorian calendar and has partly been bias-corrected. More details can be found here:\n",
                "http://impact2c.hzg.de/imperia/md/content/csc/projekte/impact2c_d4.1.pdf\n",
                "The dataset covers the ensemble members given in Table 1. Statistics are computed for different time\n",
                "periods (see section 2.3) using this entire ensemble. " ;
            :references = "W. Greuell et al. 2015. Evaluation of five hydrological models across Europe. HESSD 12, 10289–10330\n",
                "P. Roudier et al. 2016. Projections of future floods and hydrological droughts in Europe under a +2°C\n",
                "global warming. Climatic Change, 135: 341, doi:10.1007/s10584-015-1570-4 " ;
            :contact = "hydro.fou@smhi.se" ;
            :date_created = "Wed Feb 17 17:07:55 2016" ;
            :invar_platform_id = "C3S_441_Lot1_SMHI contract" ;
            :invar_rcm_model_realization_id = "IMPACT2C" ;
            :invar_hm_model_id = "Hydrological models in the order of the variables are: E-HYPE21 E-HYPE21 E-HYPE21 E-HYPE21 VIC421 VIC421 VIC421 VIC421 Lisflood Lisflood Lisflood Lisflood " ;
            :invar_hm_realization_id = "Hydrological models in the order of the variables are: KNMI-E-HYPE21 SMHI-E-HYPE21 SMHI-E-HYPE21 CSC-E-HYPE21 KNMI-VIC421 CSC-VIC421 SMHI-VIC421 SMHI-VIC421 KNMI-Lisflood CSC-Lisflood SMHI-Lisflood SMHI-Lisflood" ;
            :invar_experiment_name = "rcp85" ;
            :invar_bc_method_id = "QM-EOBS" ;
            :invar_bc_observation_id = "QM-EOBS" ;
            :invar_bc_period = "1971-2000" ;
            :reference_period = "1971-2000" ;
            :output_frequency = "day" ;
            :time_coverage_start = "19710101" ;
            :time_coverage_end = "20001231" ;
            :time_coverage_comment = "If a projection did not cover the full period 2071-2100, the indicators were calculated based on the remaining years in the period." ;
            :domain = "EUR-44" ;
            :keywords = "Flux, river flow, flow duration curve" ;
            :data_quality = "The database used was produced within the research project IMPACT2C (www.impact2c.eu) funded\n",
                "by the European Union Seventh Framework Programme (FP7/2007- 2013) under the grant agreement 4282746. \n",
                "The hydrological models were evaluated by the scientific partners participating in the\n",
                "IMPACT2C project and results can be found in Greuell et al. (2015).\n",
                "DISCLAIMER: C3S_441_Lot1_SMHI uses state of the art, quality controlled data to produce this indicator, but the\n",
                "user should note that model performance can vary substantially by location and indicator and not all\n",
                "indicators can be evaluated at a pan-European scale. Also, in IMPACT2C, hydrological model\n",
                "variables were provided on a common 0.5 degree grid which is the native grid of VIC, while Lisflood\n",
                "and E-HYPE results were up-scaled to this resolution. This may reduce the quality of the indicators vs\n",
                "original hydrological model results." ;
            :license = "Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0), https://creativecommons.org/licenses/by-sa/4.0/legalcode" ;
            :geographic_area = "The model spans a pan-European domain. The grid points over the sea are masked and only land points are retained." ;
            :spatial_resolution = "Gridded at 0.5 x 0.5 degrees.\n",
                "The grid size is 130 x 78 grid points in longitudinal and latitudinal direction, respectively.\n",
                "Note that the grid is the native one of VIC, while Lisflood and E-HYPE results were up-scaled to this\n",
                "resolution." ;
            :package_name = "Indices have been computed using CDO (https://code.zmaw.de/projects/cdo)" ;
            :date_issued = "Wed Feb 17 17:07:55 2016" ;
            :date_modified = "Wed Feb 17 17:07:55 2016" ;
            :activity = "C3S_441_Lot1_SMHI contract" ;
            :geospatial_lat_min = "33.25 degrees_east" ;
            :geospatial_lat_max = "71.75 degrees_east" ;
            :geospatial_lat_resolution = "0.5 degree" ;
            :geospatial_lon_min = "-24.75 degrees_west" ;
            :geospatial_lon_max = "39.75 degrees_west" ;
            :geospatial_lon_resolution = "0.5 degree" ;
            :invar_gcm_id = "GCMs in the order of the variables are: KNMI-EC-EARTH SMHI-EC-EARTH SMHI-HadGEM2-ES CSC-MPI-ESM-LR KNMI-EC-EARTH CSC-MPI-ESM-LR SMHI-HadGEM2-ES SMHI-EC-EARTH KNMI-EC-EARTH CSC-MPI-ESM-LR SMHI-HadGEM2-ES SMHI-EC-EARTH" ;
            :invar_rcm_id = "RCMs in the order of the variables are: KNMI-RACMO22E SMHI-RCA4 SMHI-RCA4 CSC-REMO2009 KNMI-RACMO22E CSC-REMO2009 SMHI-RCA4 SMHI-RCA4 KNMI-RACMO22E CSC-REMO2009 SMHI-RCA4 SMHI-RCA4" ;
    }
    
    
    
    
    ###############################################################################
    copernicus/cout-perc1_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap215.nc
    
    
    
    netcdf cout-perc1_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap215 {
    dimensions:
        id = 35408 ;
        time = UNLIMITED ; // (1 currently)
    variables:
        double id(id) ;
            id:standard_name = "longitude" ;
            id:long_name = "SUBID" ;
            id:units = "degrees" ;
            id:axis = "X" ;
        double time(time) ;
            time:standard_name = "time" ;
            time:units = "days since 1971-01-01 00:00:00" ;
            time:calendar = "proleptic_gregorian" ;
        float variable1(time, id) ;
            variable1:units = "%" ;
            variable1:_FillValue = -9999.f ;
        float variable2(time, id) ;
            variable2:units = "%" ;
            variable2:_FillValue = -9999.f ;
        float variable3(time, id) ;
            variable3:units = "%" ;
            variable3:_FillValue = -9999.f ;
        float variable4(time, id) ;
            variable4:units = "%" ;
            variable4:_FillValue = -9999.f ;
    
    // global attributes:
            :Conventions = "CF-1.4" ;
            :title = "Flow duration curve (1th percentile)" ;
            :description = "The flow duration curve (FDC) gives information about how frequently certain river flow rates occur.\n",
                "Here, the FDC is described through 13 percentiles of the distribution of daily river flows during a 30-\n",
                "year period:\n",
                "• 1 %\n",
                "• 5 %\n",
                "• 10 % to 90 % in steps of 10 %\n",
                "• 95 %\n",
                "• 99 %\n",
                "In case of the FDC for the full period, it is based on all daily data for a 30-year period. In the case of\n",
                "FDC’s seasonality, it is based on all daily data for a 30-year period that belong to the same month,\n",
                "evaluated for all 12 months of a year (i.e. all Januaries, all Februaries etc.)\n",
                "For the reference period (1971-2000) the absolute values are given, while for the future periods the\n",
                "relative changes are provided.\n",
                "The indicators described above are delivered in a large number of NetCDF-files. This file is a part of the delivery." ;
            :variable_name = "cout-perc1" ;
            :comment = "The climate impact indicators are based on hydrological impact modelling using the hydrological\n",
                "model E-HYPEv3.1.2. The hydrological modelling was done for C3S_441_Lot1_SMHI with an ensemble of biascorrected\n",
                "climate model data provided by the EU FP7 project IMPACT2C (grant agreement 282746).\n",
                "More information on the climate-model ensemble used (for instance model selection procedures,\n",
                "uncertainties, adjustments) can be found\n",
                "here: http://impact2c.hzg.de/imperia/md/content/csc/projekte/impact2c_d5.1_fin.pdf\n",
                "Within the project IMPACT2C, the original RCM output data has been spatially interpolated, adjusted\n",
                "to the standard Gregorian calendar and has partly been bias-corrected. More details can be found here:\n",
                "http://impact2c.hzg.de/imperia/md/content/csc/projekte/impact2c_d4.1.pdf\n",
                "The dataset covers the ensemble members given in Table 1. The ensemble comprises three\n",
                "Representative Concentration Pathways (RCP) to cover a range of policy scenarios: a mitigation\n",
                "scenario (RCP2.6), a stabilization scenario (RCP4.5) and a high greenhouse gas scenario (RCP8.5).\n",
                "The C3S_441_Lot1_SMHI indicators on catchment resolution are provided for an ensemble using one hydrological\n",
                "model (E-HYPEv3.1.2).\n",
                "Further, note that the indicators for “Precipitation” are meant to show the data including the influence\n",
                "of E-HYPE’s pre-processing of precipitation (for e.g. height correction or spatial interpolation).\n",
                "The full ensemble of time series from the model runs is stored at SMHI and the original daily timeseries\n",
                "of some essential climate variables can be downloaded from the C3S_441_Lot1_SMHI interface." ;
            :references = "Y. Hundecha et al. 2016. A regional parameter estimation scheme for a pan-European multi-basin\n",
                "model. Journal of Hydrology: Regional Studies, 6(2016), 90-111., doi:10.1016/j.ejrh.2016.04.002" ;
            :contact = "hydro.fou@smhi.se" ;
            :date_created = "Wed Feb 17 17:07:55 2016" ;
            :invar_platform_id = "C3S_441_Lot1_SMHI contract" ;
            :invar_rcm_model_realization_id = "IMPACT2C" ;
            :invar_hm_model_id = "Hydrological models in the order of the variables are: E-HYPEv3.1.2 E-HYPEv3.1.2 E-HYPEv3.1.2 E-HYPEv3.1.2 " ;
            :invar_hm_realization_id = "Hydrological models in the order of the variables are: CSC-E-HYPEv3.1.2 KNMI-E-HYPEv3.1.2 SMHI-E-HYPEv3.1.2 SMHI-E-HYPEv3.1.2" ;
            :invar_experiment_name = "rcp85" ;
            :invar_bc_method_id = "QM-EOBS" ;
            :invar_bc_observation_id = "QM-EOBS" ;
            :invar_bc_period = "1971-2000" ;
            :reference_period = "1971-2000" ;
            :output_frequency = "day" ;
            :time_coverage_start = "19710101" ;
            :time_coverage_end = "20001231" ;
            :time_coverage_comment = "If a projection did not cover the full period 2071-2100, the indicators were calculated based on the remaining years in the period." ;
            :domain = "EUR-44" ;
            :keywords = "Flux, river flow, flow duration curve" ;
            :data_quality = "C3S_441_Lot1_SMHI uses state-of-the-art, quality controlled data to produce this indicator, but the user should\n",
                "note that underlying model performance can vary substantially by location and indicator and not all\n",
                "indicators can be evaluated at a pan-European scale. Note, that unregulated flows are not calibrated on\n",
                "observed data, hence they represent model assumptions on unregulated flow behavior. The quality of\n",
                "the E-HYPE pan-European hydrological model (incl. regulations) can be perused here:\n",
                "http://hypeweb.smhi.se/europehype/model-performance/ and is summarized in Hundecha et al. (2016)." ;
            :license = "Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0), https://creativecommons.org/licenses/by-sa/4.0/legalcode" ;
            :geographic_area = "The model spans a pan-European domain. The grid points over the sea are masked and only land points are retained." ;
            :spatial_resolution = "Irregular catchment polygons, median catchmentsize 215 km2." ;
            :package_name = "Indices have been computed using CDO (https://code.zmaw.de/projects/cdo)" ;
            :date_issued = "Wed Feb 17 17:07:55 2016" ;
            :date_modified = "Wed Feb 17 17:07:55 2016" ;
            :activity = "C3S_441_Lot1_SMHI contract" ;
            :DOI_link = "https://doi.org/10.5281/zenodo.581451" ;
            :invar_gcm_id = "GCMs in the order of the variables are: CSC-MPI-ESM-LR KNMI-EC-EARTH SMHI-EC-EARTH SMHI-HadGEM2-ES" ;
            :invar_rcm_id = "RCMs in the order of the variables are: CSC-REMO2009 KNMI-RACMO22E SMHI-RCA4 SMHI-RCA4" ;
    }
    
    
    
    
    ###############################################################################
    copernicus/cout-perc5_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap0.5.nc
    
    
    
    netcdf cout-perc5_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap0.5 {
    dimensions:
        lat = 78 ;
        lon = 130 ;
        time = UNLIMITED ; // (1 currently)
    variables:
        float lat(lat) ;
            lat:standard_name = "latitude" ;
            lat:long_name = "Latitude" ;
            lat:units = "degrees_north" ;
            lat:axis = "Y" ;
        float lon(lon) ;
            lon:standard_name = "longitude" ;
            lon:long_name = "Longitude" ;
            lon:units = "degrees_east" ;
            lon:axis = "X" ;
        double time(time) ;
            time:standard_name = "time" ;
            time:units = "days since 1951-01-01 00:00:00" ;
            time:calendar = "proleptic_gregorian" ;
        float value1(time, lat, lon) ;
            value1:units = "m-3 s-1" ;
            value1:_FillValue = -1.e+20f ;
            value1:original_name = "dis" ;
        float value10(time, lat, lon) ;
            value10:units = "m3 s-1" ;
            value10:_FillValue = -1.e+20f ;
            value10:original_name = "dis" ;
        float value11(time, lat, lon) ;
            value11:units = "m3 s-1" ;
            value11:_FillValue = -1.e+20f ;
            value11:original_name = "dis" ;
        float value12(time, lat, lon) ;
            value12:units = "m3 s-1" ;
            value12:_FillValue = -1.e+20f ;
            value12:original_name = "dis" ;
        float value2(time, lat, lon) ;
            value2:units = "m-3 s-1" ;
            value2:_FillValue = -1.e+20f ;
            value2:original_name = "dis" ;
        float value3(time, lat, lon) ;
            value3:units = "m-3 s-1" ;
            value3:_FillValue = -1.e+20f ;
            value3:original_name = "dis" ;
        float value4(time, lat, lon) ;
            value4:units = "m-3 s-1" ;
            value4:_FillValue = -1.e+20f ;
            value4:original_name = "dis" ;
        float value5(time, lat, lon) ;
            value5:units = "m3 s-1" ;
            value5:_FillValue = -1.e+20f ;
            value5:original_name = "dis" ;
        float value6(time, lat, lon) ;
            value6:units = "m3 s-1" ;
            value6:_FillValue = -1.e+20f ;
            value6:original_name = "dis" ;
        float value7(time, lat, lon) ;
            value7:units = "m3 s-1" ;
            value7:_FillValue = -1.e+20f ;
            value7:original_name = "dis" ;
        float value8(time, lat, lon) ;
            value8:units = "m3 s-1" ;
            value8:_FillValue = -1.e+20f ;
            value8:original_name = "dis" ;
        float value9(time, lat, lon) ;
            value9:units = "m3 s-1" ;
            value9:_FillValue = -1.e+20f ;
            value9:original_name = "dis" ;
    
    // global attributes:
            :Conventions = "CF-1.4" ;
            :title = "Flow duration curve (5th percentile)" ;
            :description = "The flow duration curve (FDC) gives information about how frequently certain river flow rates occur.\n",
                "Here, the FDC is described through 13 percentiles of the distribution of daily river flows during a 30-\n",
                "year period:\n",
                "• 1 %\n",
                "• 5 %\n",
                "• 10 % to 90 % in steps of 10 %\n",
                "• 95 %\n",
                "• 99 %\n",
                "In case of the FDC for the full period, it is based on all daily data for a 30-year period. In the case of\n",
                "FDC’s seasonality, it is based on all daily data for a 30-year period that belong to the same month,\n",
                "evaluated for all 12 months of a year (i.e. all Januaries, all Februaries etc.)\n",
                "For the reference period (1971-2000) the absolute values are given, while for the future periods the\n",
                "relative changes are provided.\n",
                "The indicators described above are delivered in a large number of NetCDF-files. This file is a part of the delivery." ;
            :variable_name = "dis-perc5" ;
            :comment = "The climate impact indicators are based on hydrological impact modelling performed within the EU\n",
                "FP7 project IMPACT2C (grant agreement 282746). The full ensemble of time series from the model\n",
                "runs within the IMPACT2C archive is available in NetCDF format\n",
                "from http://ensemblesrt3.dmi.dk/data/impact2c-archive/MODELS/HYDROLOGY/.\n",
                "More information on the climate-model ensemble used (for instance model selection procedures,\n",
                "uncertainties, adjustments) can be found\n",
                "here: http://impact2c.hzg.de/imperia/md/content/csc/projekte/impact2c_d5.1_fin.pdf\n",
                "The hydrological models were driven by regional climate model (RCM) data. Within the EU FP7\n",
                "project IMPACT2C, the original RCM output data has been spatially interpolated, adjusted to the\n",
                "standard Gregorian calendar and has partly been bias-corrected. More details can be found here:\n",
                "http://impact2c.hzg.de/imperia/md/content/csc/projekte/impact2c_d4.1.pdf\n",
                "The dataset covers the ensemble members given in Table 1. Statistics are computed for different time\n",
                "periods (see section 2.3) using this entire ensemble. " ;
            :references = "W. Greuell et al. 2015. Evaluation of five hydrological models across Europe. HESSD 12, 10289–10330\n",
                "P. Roudier et al. 2016. Projections of future floods and hydrological droughts in Europe under a +2°C\n",
                "global warming. Climatic Change, 135: 341, doi:10.1007/s10584-015-1570-4 " ;
            :contact = "hydro.fou@smhi.se" ;
            :date_created = "Wed Feb 17 17:07:55 2016" ;
            :invar_platform_id = "C3S_441_Lot1_SMHI contract" ;
            :invar_rcm_model_realization_id = "IMPACT2C" ;
            :invar_hm_model_id = "Hydrological models in the order of the variables are: E-HYPE21 E-HYPE21 E-HYPE21 E-HYPE21 VIC421 VIC421 VIC421 VIC421 Lisflood Lisflood Lisflood Lisflood " ;
            :invar_hm_realization_id = "Hydrological models in the order of the variables are: KNMI-E-HYPE21 SMHI-E-HYPE21 SMHI-E-HYPE21 CSC-E-HYPE21 KNMI-VIC421 CSC-VIC421 SMHI-VIC421 SMHI-VIC421 KNMI-Lisflood CSC-Lisflood SMHI-Lisflood SMHI-Lisflood" ;
            :invar_experiment_name = "rcp85" ;
            :invar_bc_method_id = "QM-EOBS" ;
            :invar_bc_observation_id = "QM-EOBS" ;
            :invar_bc_period = "1971-2000" ;
            :reference_period = "1971-2000" ;
            :output_frequency = "day" ;
            :time_coverage_start = "19710101" ;
            :time_coverage_end = "20001231" ;
            :time_coverage_comment = "If a projection did not cover the full period 2071-2100, the indicators were calculated based on the remaining years in the period." ;
            :domain = "EUR-44" ;
            :keywords = "Flux, river flow, flow duration curve" ;
            :data_quality = "The database used was produced within the research project IMPACT2C (www.impact2c.eu) funded\n",
                "by the European Union Seventh Framework Programme (FP7/2007- 2013) under the grant agreement 4282746. \n",
                "The hydrological models were evaluated by the scientific partners participating in the\n",
                "IMPACT2C project and results can be found in Greuell et al. (2015).\n",
                "DISCLAIMER: C3S_441_Lot1_SMHI uses state of the art, quality controlled data to produce this indicator, but the\n",
                "user should note that model performance can vary substantially by location and indicator and not all\n",
                "indicators can be evaluated at a pan-European scale. Also, in IMPACT2C, hydrological model\n",
                "variables were provided on a common 0.5 degree grid which is the native grid of VIC, while Lisflood\n",
                "and E-HYPE results were up-scaled to this resolution. This may reduce the quality of the indicators vs\n",
                "original hydrological model results." ;
            :license = "Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0), https://creativecommons.org/licenses/by-sa/4.0/legalcode" ;
            :geographic_area = "The model spans a pan-European domain. The grid points over the sea are masked and only land points are retained." ;
            :spatial_resolution = "Gridded at 0.5 x 0.5 degrees.\n",
                "The grid size is 130 x 78 grid points in longitudinal and latitudinal direction, respectively.\n",
                "Note that the grid is the native one of VIC, while Lisflood and E-HYPE results were up-scaled to this\n",
                "resolution." ;
            :package_name = "Indices have been computed using CDO (https://code.zmaw.de/projects/cdo)" ;
            :date_issued = "Wed Feb 17 17:07:55 2016" ;
            :date_modified = "Wed Feb 17 17:07:55 2016" ;
            :activity = "C3S_441_Lot1_SMHI contract" ;
            :geospatial_lat_min = "33.25 degrees_east" ;
            :geospatial_lat_max = "71.75 degrees_east" ;
            :geospatial_lat_resolution = "0.5 degree" ;
            :geospatial_lon_min = "-24.75 degrees_west" ;
            :geospatial_lon_max = "39.75 degrees_west" ;
            :geospatial_lon_resolution = "0.5 degree" ;
            :invar_gcm_id = "GCMs in the order of the variables are: KNMI-EC-EARTH SMHI-EC-EARTH SMHI-HadGEM2-ES CSC-MPI-ESM-LR KNMI-EC-EARTH CSC-MPI-ESM-LR SMHI-HadGEM2-ES SMHI-EC-EARTH KNMI-EC-EARTH CSC-MPI-ESM-LR SMHI-HadGEM2-ES SMHI-EC-EARTH" ;
            :invar_rcm_id = "RCMs in the order of the variables are: KNMI-RACMO22E SMHI-RCA4 SMHI-RCA4 CSC-REMO2009 KNMI-RACMO22E CSC-REMO2009 SMHI-RCA4 SMHI-RCA4 KNMI-RACMO22E CSC-REMO2009 SMHI-RCA4 SMHI-RCA4" ;
    }
    
    
    
    
    ###############################################################################
    copernicus/cout-perc5_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap215.nc
    
    
    
    netcdf cout-perc5_ref_EUR-44_rcp85_IMPACT2C_QM-EOBS_1971-2000_remap215 {
    dimensions:
        id = 35408 ;
        time = UNLIMITED ; // (1 currently)
    variables:
        double id(id) ;
            id:standard_name = "longitude" ;
            id:long_name = "SUBID" ;
            id:units = "degrees" ;
            id:axis = "X" ;
        double time(time) ;
            time:standard_name = "time" ;
            time:units = "days since 1971-01-01 00:00:00" ;
            time:calendar = "proleptic_gregorian" ;
        float variable1(time, id) ;
            variable1:units = "%" ;
            variable1:_FillValue = -9999.f ;
        float variable2(time, id) ;
            variable2:units = "%" ;
            variable2:_FillValue = -9999.f ;
        float variable3(time, id) ;
            variable3:units = "%" ;
            variable3:_FillValue = -9999.f ;
        float variable4(time, id) ;
            variable4:units = "%" ;
            variable4:_FillValue = -9999.f ;
    
    // global attributes:
            :Conventions = "CF-1.4" ;
            :title = "Flow duration curve (5th percentile)" ;
            :description = "The flow duration curve (FDC) gives information about how frequently certain river flow rates occur.\n",
                "Here, the FDC is described through 13 percentiles of the distribution of daily river flows during a 30-\n",
                "year period:\n",
                "• 1 %\n",
                "• 5 %\n",
                "• 10 % to 90 % in steps of 10 %\n",
                "• 95 %\n",
                "• 99 %\n",
                "In case of the FDC for the full period, it is based on all daily data for a 30-year period. In the case of\n",
                "FDC’s seasonality, it is based on all daily data for a 30-year period that belong to the same month,\n",
                "evaluated for all 12 months of a year (i.e. all Januaries, all Februaries etc.)\n",
                "For the reference period (1971-2000) the absolute values are given, while for the future periods the\n",
                "relative changes are provided.\n",
                "The indicators described above are delivered in a large number of NetCDF-files. This file is a part of the delivery." ;
            :variable_name = "cout-perc5" ;
            :comment = "The climate impact indicators are based on hydrological impact modelling using the hydrological\n",
                "model E-HYPEv3.1.2. The hydrological modelling was done for C3S_441_Lot1_SMHI with an ensemble of biascorrected\n",
                "climate model data provided by the EU FP7 project IMPACT2C (grant agreement 282746).\n",
                "More information on the climate-model ensemble used (for instance model selection procedures,\n",
                "uncertainties, adjustments) can be found\n",
                "here: http://impact2c.hzg.de/imperia/md/content/csc/projekte/impact2c_d5.1_fin.pdf\n",
                "Within the project IMPACT2C, the original RCM output data has been spatially interpolated, adjusted\n",
                "to the standard Gregorian calendar and has partly been bias-corrected. More details can be found here:\n",
                "http://impact2c.hzg.de/imperia/md/content/csc/projekte/impact2c_d4.1.pdf\n",
                "The dataset covers the ensemble members given in Table 1. The ensemble comprises three\n",
                "Representative Concentration Pathways (RCP) to cover a range of policy scenarios: a mitigation\n",
                "scenario (RCP2.6), a stabilization scenario (RCP4.5) and a high greenhouse gas scenario (RCP8.5).\n",
                "The C3S_441_Lot1_SMHI indicators on catchment resolution are provided for an ensemble using one hydrological\n",
                "model (E-HYPEv3.1.2).\n",
                "Further, note that the indicators for “Precipitation” are meant to show the data including the influence\n",
                "of E-HYPE’s pre-processing of precipitation (for e.g. height correction or spatial interpolation).\n",
                "The full ensemble of time series from the model runs is stored at SMHI and the original daily timeseries\n",
                "of some essential climate variables can be downloaded from the C3S_441_Lot1_SMHI interface." ;
            :references = "Y. Hundecha et al. 2016. A regional parameter estimation scheme for a pan-European multi-basin\n",
                "model. Journal of Hydrology: Regional Studies, 6(2016), 90-111., doi:10.1016/j.ejrh.2016.04.002" ;
            :contact = "hydro.fou@smhi.se" ;
            :date_created = "Wed Feb 17 17:07:55 2016" ;
            :invar_platform_id = "C3S_441_Lot1_SMHI contract" ;
            :invar_rcm_model_realization_id = "IMPACT2C" ;
            :invar_hm_model_id = "Hydrological models in the order of the variables are: E-HYPEv3.1.2 E-HYPEv3.1.2 E-HYPEv3.1.2 E-HYPEv3.1.2 " ;
            :invar_hm_realization_id = "Hydrological models in the order of the variables are: CSC-E-HYPEv3.1.2 KNMI-E-HYPEv3.1.2 SMHI-E-HYPEv3.1.2 SMHI-E-HYPEv3.1.2" ;
            :invar_experiment_name = "rcp85" ;
            :invar_bc_method_id = "QM-EOBS" ;
            :invar_bc_observation_id = "QM-EOBS" ;
            :invar_bc_period = "1971-2000" ;
            :reference_period = "1971-2000" ;
            :output_frequency = "day" ;
            :time_coverage_start = "19710101" ;
            :time_coverage_end = "20001231" ;
            :time_coverage_comment = "If a projection did not cover the full period 2071-2100, the indicators were calculated based on the remaining years in the period." ;
            :domain = "EUR-44" ;
            :keywords = "Flux, river flow, flow duration curve" ;
            :data_quality = "C3S_441_Lot1_SMHI uses state-of-the-art, quality controlled data to produce this indicator, but the user should\n",
                "note that underlying model performance can vary substantially by location and indicator and not all\n",
                "indicators can be evaluated at a pan-European scale. Note, that unregulated flows are not calibrated on\n",
                "observed data, hence they represent model assumptions on unregulated flow behavior. The quality of\n",
                "the E-HYPE pan-European hydrological model (incl. regulations) can be perused here:\n",
                "http://hypeweb.smhi.se/europehype/model-performance/ and is summarized in Hundecha et al. (2016)." ;
            :license = "Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0), https://creativecommons.org/licenses/by-sa/4.0/legalcode" ;
            :geographic_area = "The model spans a pan-European domain. The grid points over the sea are masked and only land points are retained." ;
            :spatial_resolution = "Irregular catchment polygons, median catchmentsize 215 km2." ;
            :package_name = "Indices have been computed using CDO (https://code.zmaw.de/projects/cdo)" ;
            :date_issued = "Wed Feb 17 17:07:55 2016" ;
            :date_modified = "Wed Feb 17 17:07:55 2016" ;
            :activity = "C3S_441_Lot1_SMHI contract" ;
            :DOI_link = "https://doi.org/10.5281/zenodo.581451" ;
            :invar_gcm_id = "GCMs in the order of the variables are: CSC-MPI-ESM-LR KNMI-EC-EARTH SMHI-EC-EARTH SMHI-HadGEM2-ES" ;
            :invar_rcm_id = "RCMs in the order of the variables are: CSC-REMO2009 KNMI-RACMO22E SMHI-RCA4 SMHI-RCA4" ;
    }
    
    
    
    
    ###############################################################################
    dt_ref_global_merged_madt_uv_19921014_19921014_20060315.nc
    
    
    
    netcdf dt_ref_global_merged_madt_uv_19921014_19921014_20060315 {
    dimensions:
        NbLatitudes = 915 ;
        NbLongitudes = 1080 ;
        GridDepth = 1 ;
        LatLon = 2 ;
    variables:
        int LatLon(LatLon) ;
            LatLon:_FillValue = 2147483647 ;
            LatLon:long_name = "No sense but necessary for some automatic tools" ;
            LatLon:units = "count" ;
        double NbLatitudes(NbLatitudes) ;
            NbLatitudes:_FillValue = 1.84467440737096e+19 ;
            NbLatitudes:long_name = "Latitudes" ;
            NbLatitudes:units = "degrees_north" ;
        double NbLongitudes(NbLongitudes) ;
            NbLongitudes:_FillValue = 1.84467440737096e+19 ;
            NbLongitudes:long_name = "Longitudes" ;
            NbLongitudes:units = "degrees_east" ;
        double LatLonMin(LatLon) ;
            LatLonMin:_FillValue = 1.84467440737096e+19 ;
            LatLonMin:long_name = "Latitude/Longitude of south/ouest corner" ;
            LatLonMin:units = "degree" ;
        double LatLonStep(LatLon) ;
            LatLonStep:_FillValue = 1.84467440737096e+19 ;
            LatLonStep:long_name = "latitude/longitude steps" ;
            LatLonStep:units = "degree" ;
        float Grid_0001(NbLongitudes, NbLatitudes) ;
            Grid_0001:_FillValue = 1.844674e+19f ;
            Grid_0001:long_name = "U" ;
            Grid_0001:units = "cm/s" ;
            Grid_0001:Date_CNES_JD = 15627. ;
            Grid_0001:date = "1992-10-14 00:00:00.000000 UTC" ;
        float Grid_0002(NbLongitudes, NbLatitudes) ;
            Grid_0002:_FillValue = 1.844674e+19f ;
            Grid_0002:long_name = "V" ;
            Grid_0002:units = "cm/s" ;
            Grid_0002:Date_CNES_JD = 15627. ;
            Grid_0002:date = "1992-10-14 00:00:00.000000 UTC" ;
    
    // global attributes:
            :FileType = "GRID_DOTS_MERCATOR" ;
            :OriginalName = "dt_ref_global_merged_madt_uv_19921014_19921014_20060315.nc" ;
            :CreatedBy = "SSALTO/DUACS" ;
            :CreatedOn = "18-MAR-2006 20:07:49:000000" ;
            :title = "SSALTO/DUACS - DT Geostrophic Velocities Anomaly - Homogeneous Global Processing" ;
    }
    
    
    
    
    ###############################################################################
    EOBS/EOBS_2001-2016.nc
    
    
    
    netcdf EOBS_2001-2016 {
    dimensions:
        time = UNLIMITED ; // (1 currently)
        jx = 95 ;
        iy = 110 ;
        bin = 1001 ;
        bnds = 2 ;
    variables:
        double time(time) ;
            time:standard_name = "time" ;
            time:long_name = "Time in days" ;
            time:units = "days since 1950-01-01 00:00" ;
            time:calendar = "standard" ;
            time:axis = "T" ;
        float xlon(iy, jx) ;
            xlon:standard_name = "longitude" ;
            xlon:long_name = "longitude" ;
            xlon:units = "degrees_east" ;
            xlon:_CoordinateAxisType = "Lon" ;
        float xlat(iy, jx) ;
            xlat:standard_name = "latitude" ;
            xlat:long_name = "latitude" ;
            xlat:units = "degrees_north" ;
            xlat:_CoordinateAxisType = "Lat" ;
        float jx(jx) ;
            jx:standard_name = "projection_x_coordinate" ;
            jx:long_name = "x-coordinate in Cartesian system" ;
            jx:units = "m" ;
            jx:axis = "X" ;
        float iy(iy) ;
            iy:standard_name = "projection_y_coordinate" ;
            iy:long_name = "y-coordinate in Cartesian system" ;
            iy:units = "m" ;
            iy:axis = "Y" ;
        int crs ;
            crs:grid_mapping_name = "lambert_conformal_conic" ;
            crs:proj4_params = "+proj=lcc +lat_1=30.00 +lat_2=65.00 +lat_0=48.00 +lon_0=9.75 +x_0=-6000. +y_0=-6000. +ellps=sphere +a=6371229. +b=6371229. +units=m +no_defs" ;
            crs:standard_parallel = 30., 65. ;
            crs:longitude_of_central_meridian = 9.75 ;
            crs:latitude_of_projection_origin = 48. ;
            crs:semi_major_axis = 6371229. ;
            crs:inverse_flattening = 0. ;
            crs:false_easting = -6000. ;
            crs:false_northing = -6000. ;
            crs:_CoordinateTransformType = "Projection" ;
            crs:_CoordinateAxisTypes = "GeoX GeoY" ;
        double bin(bin) ;
            bin:long_name = "histogram bins" ;
            bin:units = "level" ;
            bin:axis = "Z" ;
            bin:bounds = "bin_bnds" ;
        double bin_bnds(bin, bnds) ;
        float rr(time, bin, iy, jx) ;
            rr:standard_name = "thickness_of_rainfall_amount" ;
            rr:long_name = "rainfall" ;
            rr:units = "mm/day" ;
            rr:grid_mapping = "crs" ;
            rr:coordinates = "xlat xlon" ;
            rr:_FillValue = -9999.f ;
            rr:missing_value = -9999.f ;
    
    // global attributes:
            :CDI = "Climate Data Interface version 1.9.1 (http://mpimet.mpg.de/cdi)" ;
            :history = "Thu Apr 19 14:11:33 2018: cdo -s -C -O -b 32 histcount,-inf,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931,932,933,934,935,936,937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999,1000,inf EOBS_2001-2016.nc histograms/EOBS_2001-2016.nc\n",
                "Thu Apr 19 14:05:54 2018: cdo -s -C -O ifthen -seltimestep,1/5844 /home/netapp-clima-users1/afantini/EURO-CORDEX/validation/spatialData/mask_1dlcc_dewrain-fil_2001-2016.nc EOBS_2001-2016.nc masked/EOBS_2001-2016.nc\n",
                "Thu Apr 19 12:20:06 2018: cdo remap,../spatialData/grid_regcm.txt,../spatialData/nnweights_eobs_regcm.nc EOBS_2001-2016.nc remapped/EOBS_2001-2016.nc\n",
                "Wed Apr 04 15:26:04 2018: cdo -L -setunit,mm/day -sellonlatbox,6,19,36,48 EOBS_2001-2016.nc EOBS_2001-2016_small.nc\n",
                "Sat Mar 31 18:36:53 2018: cdo selyear,2001/2016 /home/esp-shared-a/Observations/E_OBS/v16/025/rr_0.25deg_reg_v16.0.nc EOBS/EOBS_2001-2016.nc\n",
                "Thu Sep 28 12:36:45 2017: ncks -a --fix_rec_dmn time tempfile.nc rr_0.25deg_reg_v16.0.nc\n",
                "Thu Sep 28 12:36:15 2017: ncrcat rr_0.25deg_reg_1950-1964_v16.0.nc rr_0.25deg_reg_1965-1979_v16.0.nc rr_0.25deg_reg_1980-1994_v16.0.nc rr_0.25deg_reg_1995-2010_v16.0.nc rr_0.25deg_reg_2011-2017_v16.0.nc tempfile.nc\n",
                "Thu Sep 28 12:35:50 2017: ncks -a -d time,0,5478 rr_0.25deg_regular_1.nc rr_0.25deg_reg_1950-1964_v16.0.nc\n",
                "Thu Sep 28 12:34:04 2017: ncks -a --mk_rec_dmn time rr_0.25deg_regular.nc rr_0.25deg_regular_1.nc" ;
            :Conventions = "CF-1.4" ;
            :Ensembles_ECAD = "16.0" ;
            :References = "http://www.ecad.eu\\nhttp://www.ecad.eu/download/ensembles/ensembles.php\\nhttp://www.ecad.eu/download/ensembles/Haylock_et_al_2008.pdf" ;
            :NCO = "\"4.6.2\"" ;
            :nco_openmp_thread_number = 1 ;
            :CDO = "Climate Data Operators version 1.9.1 (http://mpimet.mpg.de/cdo)" ;
    }
    
    
    
    
    ###############################################################################
    EOBS/readme
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/EOBS/readme' had status 1
    
    
    
    
    ###############################################################################
    EURO-CORDEX_81_DOMAIN000_54/EURO-CORDEX_81_DOMAIN000.nc
    
    
    
    netcdf EURO-CORDEX_81_DOMAIN000 {
    dimensions:
        jx = 530 ;
        iy = 530 ;
        kz = 24 ;
        soil_layer = 10 ;
        ntex = 17 ;
    variables:
        float jx(jx) ;
            jx:long_name = "x-coordinate in Cartesian system" ;
            jx:standard_name = "projection_x_coordinate" ;
            jx:units = "m" ;
            jx:axis = "X" ;
            jx:_CoordinateAxisType = "GeoX" ;
        float iy(iy) ;
            iy:long_name = "y-coordinate in Cartesian system" ;
            iy:standard_name = "projection_y_coordinate" ;
            iy:units = "m" ;
            iy:axis = "Y" ;
            iy:_CoordinateAxisType = "GeoY" ;
        float sigma(kz) ;
            sigma:long_name = "Sigma at full model layers" ;
            sigma:standard_name = "atmosphere_sigma_coordinate" ;
            sigma:units = "1" ;
            sigma:axis = "Z" ;
            sigma:positive = "down" ;
            sigma:formula_terms = "sigma: sigma ps: ps ptop: ptop" ;
            sigma:_CoordinateAxisType = "GeoZ" ;
        float ptop ;
            ptop:long_name = "Pressure at model top" ;
            ptop:standard_name = "air_pressure" ;
            ptop:units = "hPa" ;
        float xlon(iy, jx) ;
            xlon:long_name = "Longitude on Cross Points" ;
            xlon:standard_name = "longitude" ;
            xlon:units = "degrees_east" ;
            xlon:grid_mapping = "crs" ;
        float xlat(iy, jx) ;
            xlat:long_name = "Latitude on Cross Points" ;
            xlat:standard_name = "latitude" ;
            xlat:units = "degrees_north" ;
            xlat:grid_mapping = "crs" ;
        float dlon(iy, jx) ;
            dlon:long_name = "Longitude on Dot Points" ;
            dlon:standard_name = "longitude" ;
            dlon:units = "degrees_east" ;
            dlon:grid_mapping = "crs" ;
        float dlat(iy, jx) ;
            dlat:long_name = "latitude" ;
            dlat:standard_name = "Latitude on Dot Points" ;
            dlat:units = "degrees_north" ;
            dlat:grid_mapping = "crs" ;
        float xmap(iy, jx) ;
            xmap:long_name = "Map Factor on Cross Points" ;
            xmap:standard_name = "map_factor" ;
            xmap:units = "1" ;
            xmap:coordinates = "xlat xlon" ;
            xmap:grid_mapping = "crs" ;
        float dmap(iy, jx) ;
            dmap:long_name = "Map Factor on Dot Points" ;
            dmap:standard_name = "map_factor" ;
            dmap:units = "1" ;
            dmap:coordinates = "xlat xlon" ;
            dmap:grid_mapping = "crs" ;
        float coriol(iy, jx) ;
            coriol:long_name = "Coriolis Parameter" ;
            coriol:standard_name = "coriolis_parameter" ;
            coriol:units = "s-1" ;
            coriol:coordinates = "xlat xlon" ;
            coriol:grid_mapping = "crs" ;
        float mask(iy, jx) ;
            mask:long_name = "Land Mask" ;
            mask:standard_name = "land_binary_mask" ;
            mask:units = "1" ;
            mask:coordinates = "xlat xlon" ;
            mask:grid_mapping = "crs" ;
        float topo(iy, jx) ;
            topo:long_name = "Surface Model Elevation" ;
            topo:standard_name = "surface_altitude" ;
            topo:units = "m" ;
            topo:coordinates = "xlat xlon" ;
            topo:grid_mapping = "crs" ;
        float landuse(iy, jx) ;
            landuse:long_name = "Landuse category as defined in BATS1E" ;
            landuse:standard_name = "land_type" ;
            landuse:units = "1" ;
            landuse:coordinates = "xlat xlon" ;
            landuse:grid_mapping = "crs" ;
            landuse:legend = "1  => Crop/mixed farming\n",
                "2  => Short grass\n",
                "3  => Evergreen needleleaf tree\n",
                "4  => Deciduous needleleaf tree\n",
                "5  => Deciduous broadleaf tree\n",
                "6  => Evergreen broadleaf tree\n",
                "7  => Tall grass\n",
                "8  => Desert\n",
                "9  => Tundra\n",
                "10 => Irrigated Crop\n",
                "11 => Semi-desert\n",
                "12 => Ice cap/glacier\n",
                "13 => Bog or marsh\n",
                "14 => Inland water\n",
                "15 => Ocean\n",
                "16 => Evergreen shrub\n",
                "17 => Deciduous shrub\n",
                "18 => Mixed Woodland\n",
                "19 => Forest/Field mosaic\n",
                "20 => Water and Land mixture\n",
                "21 => Urban\n",
                "22 => Sub-Urban" ;
        float snowam(iy, jx) ;
            snowam:long_name = "Snow initial LWE in mm" ;
            snowam:standard_name = "snowfall_amount" ;
            snowam:units = "mm" ;
            snowam:coordinates = "xlat xlon" ;
            snowam:grid_mapping = "crs" ;
            snowam:_FillValue = 1.e+20f ;
        float smoist(iy, jx) ;
            smoist:long_name = "Soil Moisture" ;
            smoist:standard_name = "volume_fraction_of_water_in_soil" ;
            smoist:units = "1" ;
            smoist:coordinates = "xlat xlon" ;
            smoist:grid_mapping = "crs" ;
            smoist:_FillValue = 1.e+20f ;
        float texture(iy, jx) ;
            texture:long_name = "Texture dominant category" ;
            texture:standard_name = "soil_type" ;
            texture:units = "1" ;
            texture:coordinates = "xlat xlon" ;
            texture:grid_mapping = "crs" ;
            texture:legend = "1  => Sand\n",
                "2  => Loamy Sand\n",
                "3  => Sandy Loam\n",
                "4  => Silt Loam\n",
                "5  => Silt\n",
                "6  => Loam\n",
                "7  => Sandy Clay Loam\n",
                "8  => Silty Clay Loam\n",
                "9  => Clay Loam\n",
                "10 => Sandy Clay\n",
                "11 => Silty Clay\n",
                "12 => Clay\n",
                "13 => OM\n",
                "14 => Water\n",
                "15 => Bedrock\n",
                "16 => Other\n",
                "17 => No data" ;
        float rmoist(soil_layer, iy, jx) ;
            rmoist:long_name = "Soil Moisture" ;
            rmoist:standard_name = "volume_fraction_of_water_in_soil" ;
            rmoist:units = "kg m-2" ;
            rmoist:coordinates = "xlat xlon" ;
            rmoist:grid_mapping = "crs" ;
            rmoist:_FillValue = 1.e+20f ;
        float texture_fraction(ntex, iy, jx) ;
            texture_fraction:long_name = "Texture category fraction" ;
            texture_fraction:standard_name = "soil_type_fraction" ;
            texture_fraction:units = "1" ;
            texture_fraction:coordinates = "xlat xlon" ;
            texture_fraction:grid_mapping = "crs" ;
            texture_fraction:_FillValue = 1.e+20f ;
        char crs ;
            crs:proj4_params = "+proj=lcc +lat_1=30.00 +lat_2=65.00 +lat_0=48.00 +lon_0=9.75 +x_0=-6000. +y_0=-6000. +ellps=sphere +a=6371229. +b=6371229. +units=m +no_defs" ;
            crs:grid_mapping_name = "lambert_conformal_conic" ;
            crs:standard_parallel = 30., 65. ;
            crs:longitude_of_central_meridian = 9.75 ;
            crs:latitude_of_projection_origin = 48. ;
            crs:semi_major_axis = 6371229. ;
            crs:inverse_flattening = 0. ;
            crs:false_easting = -6000. ;
            crs:false_northing = -6000. ;
            crs:_CoordinateTransformType = "Projection" ;
            crs:_CoordinateAxisTypes = "GeoX GeoY" ;
        float soil_layer(soil_layer) ;
            soil_layer:long_name = "Soil layer levels" ;
            soil_layer:standard_name = "root_depth" ;
            soil_layer:units = "m" ;
    
    // global attributes:
            :title = "ICTP Regional Climatic model V4" ;
            :institution = "ICTP" ;
            :source = "RegCM Model output file" ;
            :Conventions = "CF-1.4" ;
            :references = "http://gforge.ictp.it/gf/project/regcm" ;
            :model_revision = "tag-4.6.1" ;
            :history = "2018-02-06 17:52:32 : Created by RegCM terrain program" ;
            :experiment = "EURO-CORDEX_81" ;
            :projection = "LAMCON" ;
            :grid_size_in_meters = 12000. ;
            :latitude_of_projection_origin = 48. ;
            :longitude_of_projection_origin = 9.75 ;
            :standard_parallel = 30., 65. ;
            :grid_factor = 0.749565224994391 ;
            :boundary_smoothing = "No" ;
            :minimum_h2o_pct_for_water = 50. ;
            :smoothing_level = 1 ;
            :h2o_hgt_over_water = "Yes" ;
            :intermediate_resolution = 3 ;
            :landuse_fudging = "No" ;
            :texture_fudging = "No" ;
            :initialized_soil_moisture = "No" ;
    }
    
    
    
    
    ###############################################################################
    EURO-CORDEX_81_DOMAIN000_54/issue_54.R
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/EURO-
    CORDEX_81_DOMAIN000_54/issue_54.R' had status 1
    
    
    
    
    ###############################################################################
    file.nc
    
    
    
    netcdf file {
    dimensions:
        longitude = 60 ;
        latitude = 72 ;
        z = UNLIMITED ; // (14 currently)
    variables:
        double longitude(longitude) ;
            longitude:units = "degrees_east" ;
            longitude:long_name = "longitude" ;
        double latitude(latitude) ;
            latitude:units = "degrees_north" ;
            latitude:long_name = "latitude" ;
        int z(z) ;
            z:units = "unknown" ;
            z:long_name = "z" ;
        float variable(z, latitude, longitude) ;
            variable :_FillValue = -3.4e+38f ;
            variable :missing_value = -3.4e+38f ;
            variable :long_name = "variable" ;
            variable :min = -1.26999997161329, -0.839999981224537, -1.02999997697771, -0.979999978095293, -1.18999997340143, -0.709999984130263, -0.679999984800816, -0.589999986812472, -0.559999987483025, -0.509999988600612, -0.819999981671572, -0.949999978765845, -0.859999980777502, -0.779999982565641 ;
            variable :max = 16.1699996385723, 16.6899996269494, 16.8699996229261, 16.7099996265024, 16.4999996311963, 16.4099996332079, 16.929999621585, 16.8099996242672, 16.1599996387959, 15.9599996432662, 16.3299996349961, 16.349999634549, 16.3599996343255, 15.9399996437132 ;
    
    // global attributes:
            :crs = "+proj=longlat +datum=WGS84 +ellps=WGS84 +towgs84=0,0,0" ;
            :crs_format = "PROJ.4" ;
            :Conventions = "CF-1.4" ;
            :created_by = "R, packages ncdf4 and raster (version 2.6-7)" ;
            :date = "2018-08-30 08:30:13" ;
    }
    
    
    
    
    ###############################################################################
    get1index_64/test.nc
    
    
    
    netcdf test {
    dimensions:
        time = UNLIMITED ; // (1 currently)
        bnds = 2 ;
        x = 424 ;
        y = 412 ;
    variables:
        double time(time) ;
            time:standard_name = "time" ;
            time:bounds = "time_bnds" ;
            time:units = "days since 1949-12-01 00:00:00" ;
            time:calendar = "proleptic_gregorian" ;
            time:axis = "T" ;
        double time_bnds(time, bnds) ;
        double lon(y, x) ;
            lon:standard_name = "longitude" ;
            lon:long_name = "longitude" ;
            lon:units = "degrees_east" ;
            lon:_CoordinateAxisType = "Lon" ;
        double lat(y, x) ;
            lat:standard_name = "latitude" ;
            lat:long_name = "latitude" ;
            lat:units = "degrees_north" ;
            lat:_CoordinateAxisType = "Lat" ;
        float pr(time, y, x) ;
            pr:standard_name = "precipitation_flux" ;
            pr:long_name = "Precipitation" ;
            pr:units = "kg m-2 s-1" ;
            pr:coordinates = "lat lon" ;
            pr:_FillValue = 1.e+20f ;
            pr:missing_value = 1.e+20f ;
            pr:cell_methods = "time: mean" ;
    
    // global attributes:
            :CDI = "Climate Data Interface version 1.9.1 (http://mpimet.mpg.de/cdi)" ;
            :history = "Wed Oct 03 11:53:06 2018: cdo -C seltimestep,1 /home/netapp-clima-scratch/fraffael/SPI/EC-EARTH_HIRHAM5/prOK_mon_2071-2098.nc /dev/shm/test.nc\n",
                "Mon Oct 01 18:02:40 2018: cdo mulc,86400 pr_mon_2071-2098.nc prOK_mon_2071-2098.nc\n",
                "Mon Oct 01 12:24:12 2018: cdo selyear,2071/2098 pr_mon_2071-2100.nc pr_mon_2071-2098.nc\n",
                "Mon Oct  1 12:23:45 2018: ncrcat /home/esp-shared-a/RegionalModels/CORDEX/EUR-11/rcp85/MM/EC-EARTH_HIRHAM5/pr_EUR-11_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_207101-208012.nc /home/esp-shared-a/RegionalModels/CORDEX/EUR-11/rcp85/MM/EC-EARTH_HIRHAM5/pr_EUR-11_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_208101-209012.nc /home/esp-shared-a/RegionalModels/CORDEX/EUR-11/rcp85/MM/EC-EARTH_HIRHAM5/pr_EUR-11_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_209101-210012.nc pr_mon_2071-2100.nc\n",
                "Mon Nov 18 04:53:38 2013: /usr/local/bin/ncks --mk_rec_dmn time pr_EUR-11_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_207101-208012.nc out1.nc\n",
                "Fri Dec 07 08:23:08 2012: cdo setday,16 NAM-44/DMI/DMI-ECEARTH/rcp85/r3i1p1/DMI-HIRHAM5/v1/mon/tas/tas_NAM-44_DMI-ECEARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_207101-208012.nc NAM-44/DMI/DMI-ECEARTH/rcp85/r3i1p1/DMI-HIRHAM5/v1/mon/tas/tas_NAM-44_DMI-ECEARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_207101-208012_sub.nc\n",
                "Fri Dec 07 08:23:07 2012: cdo monmean NAM-44/DMI/DMI-ECEARTH/rcp85/r3i1p1/DMI-HIRHAM5/v1/mon/tas/tas_NAM-44_DMI-ECEARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_20710101-20801231.nc NAM-44/DMI/DMI-ECEARTH/rcp85/r3i1p1/DMI-HIRHAM5/v1/mon/tas/tas_NAM-44_DMI-ECEARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_207101-208012.nc\n",
                "Fri Dec 07 08:22:56 2012: cdo mergetime NAM-44/DMI/DMI-ECEARTH/rcp85/r3i1p1/DMI-HIRHAM5/v1/day/tas/tas_NAM-44_DMI-ECEARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_day_20710101-20751231.nc NAM-44/DMI/DMI-ECEARTH/rcp85/r3i1p1/DMI-HIRHAM5/v1/day/tas/tas_NAM-44_DMI-ECEARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_day_20760101-20801231.nc NAM-44/DMI/DMI-ECEARTH/rcp85/r3i1p1/DMI-HIRHAM5/v1/mon/tas/tas_NAM-44_DMI-ECEARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_20710101-20801231.nc" ;
            :institution = "Danish Meteorological Institute" ;
            :Conventions = "CF-1.6" ;
            :tracking_id = "e9cc9b3b-9755-400b-b101-49c24b811781" ;
            :contact = "obc@dmi.dk" ;
            :creation_date = "2012-12-03 03:14:15" ;
            :driving_model_ensemble_member = "r3i1p1" ;
            :institute_id = "DMI" ;
            :model_id = "DMI-HIRHAM5" ;
            :rcm_version_id = "v1" ;
            :project_id = "CORDEX" ;
            :product = "output" ;
            :frequency = "mon" ;
            :NCO = "\"4.6.4\"" ;
            :experiment = "Scenario run using ECEARTH as driving model" ;
            :experiment_id = "rcp85" ;
            :driving_experiment_name = "rcp85" ;
            :CORDEX_domain = "EUR-11" ;
            :driving_experiment = "ICHEC-EC-EARTH,rcp85,r3i1p1" ;
            :driving_model_id = "ICHEC-EC-EARTH" ;
            :nco_openmp_thread_number = 1 ;
            :CDO = "Climate Data Operators version 1.9.1 (http://mpimet.mpg.de/cdo)" ;
    }
    
    
    
    
    ###############################################################################
    GPP/gpp_Lmon_EnsembleGPP_observations_198201-201112.nc
    
    
    
    netcdf gpp_Lmon_EnsembleGPP_observations_198201-201112 {
    dimensions:
        lon = 720 ;
        nb2 = 2 ;
        lat = 360 ;
        time = UNLIMITED ; // (360 currently)
    variables:
        double lon(lon) ;
            lon:standard_name = "longitude" ;
            lon:long_name = "longitude" ;
            lon:units = "degrees_east" ;
            lon:axis = "X" ;
            lon:bounds = "lon_bnds" ;
        double lon_bnds(lon, nb2) ;
            lon_bnds:long_name = "lon_bnds" ;
            lon_bnds:units = "1" ;
        double lat(lat) ;
            lat:standard_name = "latitude" ;
            lat:long_name = "latitude" ;
            lat:units = "degrees_north" ;
            lat:axis = "Y" ;
            lat:bounds = "lat_bnds" ;
        double lat_bnds(lat, nb2) ;
            lat_bnds:long_name = "lat_bnds" ;
            lat_bnds:units = "1" ;
        double time(time) ;
            time:standard_name = "time" ;
            time:bounds = "time_bnds" ;
            time:units = "days since 1582-10-14 00:00:00" ;
            time:calendar = "standard" ;
            time:long_name = "time" ;
        double time_bnds(time, nb2) ;
            time_bnds:units = "days since 1582-10-14 00:00:00" ;
            time_bnds:calendar = "standard" ;
            time_bnds:long_name = "time_bnds" ;
        float gpp(time, lat, lon) ;
            gpp:standard_name = "gross_primary_productivity_of_carbon" ;
            gpp:long_name = "Carbon Mass Flux out of Atmosphere due to Gross Primary Production on Land" ;
            gpp:units = "kg m-2 s-1" ;
            gpp:_FillValue = -9999.f ;
            gpp:original_name = "EnsembleGPP_GL_May12" ;
            gpp:cell_methods = "time: mean area: mean where land" ;
            gpp:history = "generated 05/2012" ;
            gpp:associated_files = "none" ;
        float std(time, lat, lon) ;
            std:standard_name = "uncertainty based on spread of ensemble" ;
            std:long_name = "standard deviation calculated based on median absolute deviation" ;
            std:units = "kg m-2 s-1" ;
            std:_FillValue = -9999.f ;
            std:original_name = "std" ;
            std:cell_methods = "time: mean area: mean where land" ;
            std:history = "generated 05/2012" ;
            std:associated_files = "none" ;
    
    // global attributes:
            :history = "Mon Feb 11 10:26:28 2013: cdo copy EnsembleGPP_GL_May12.1982.nc EnsembleGPP_GL_May12.1983.nc EnsembleGPP_GL_May12.1984.nc EnsembleGPP_GL_May12.1985.nc EnsembleGPP_GL_May12.1986.nc EnsembleGPP_GL_May12.1987.nc EnsembleGPP_GL_May12.1988.nc EnsembleGPP_GL_May12.1989.nc EnsembleGPP_GL_May12.1990.nc EnsembleGPP_GL_May12.1991.nc EnsembleGPP_GL_May12.1992.nc EnsembleGPP_GL_May12.1993.nc EnsembleGPP_GL_May12.1994.nc EnsembleGPP_GL_May12.1995.nc EnsembleGPP_GL_May12.1996.nc EnsembleGPP_GL_May12.1997.nc EnsembleGPP_GL_May12.1998.nc EnsembleGPP_GL_May12.1999.nc EnsembleGPP_GL_May12.2000.nc EnsembleGPP_GL_May12.2001.nc EnsembleGPP_GL_May12.2002.nc EnsembleGPP_GL_May12.2003.nc EnsembleGPP_GL_May12.2004.nc EnsembleGPP_GL_May12.2005.nc EnsembleGPP_GL_May12.2006.nc EnsembleGPP_GL_May12.2007.nc EnsembleGPP_GL_May12.2008.nc EnsembleGPP_GL_May12.2009.nc EnsembleGPP_GL_May12.2010.nc EnsembleGPP_GL_May12.2011.nc EnsembleGPP_GL.nc\n",
                "generated 05/2012" ;
            :institution = "Max Planck Institude for BioGeoChemistry Jena, Germany" ;
            :institute_id = "MPI-BGC" ;
            :experiment_id = "may12" ;
            :model_id = "may12" ;
            :forcing = "1982-1997 GIMMS 1998-2005 SeaWIFS 2006-2011 MERIS, ERAinterim meteo input" ;
            :contact = "mjung@bgc-jena.mpg.de" ;
            :references = "Jung, M., Reichstein, M., Bondeau, A. 2009 Biogeosciences, 6;    LASSLOP, G. et al. (2010),  Global Change Biology, 16: 187–208." ;
            :CDO = "Climate Data Operators version 1.5.5 (http://code.zmaw.de/projects/cdo)" ;
            :title = "Gross Primary Production on Land" ;
            :description = "GPP derived by upscaling observations from the current global network of eddy-covariance towers (FLUXNET, Jung et al 2011 Journal of Geophysical Research, 116 G00J07). For the upscaling a model tree ensemble approach was used as described in (Jung, M., Reichstein, M., Bondeau, A. 2009 Biogeosciences, 6). For this dataset the flux partitioning was based on LASSLOP, G. et al. (2010), Global Change Biology, 16: 187–208" ;
    }
    
    
    
    
    ###############################################################################
    GPP/readme
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/GPP/readme' had status 1
    
    
    
    
    ###############################################################################
    HDF4/ladsweb/MOD021KM.A2015091.0010.006.2015091134552.hdf
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/HDF4/ladsweb/
    MOD021KM.A2015091.0010.006.2015091134552.hdf' had status 1
    
    
    
    
    ###############################################################################
    high-dim/test-1.nc
    
    
    
    netcdf test-1 {
    dimensions:
        x = 2 ;
        y = 3 ;
        c3 = 2 ;
        c4 = 2 ;
        c5 = 3 ;
    variables:
        double a(c5, c4, c3, y, x) ;
        double x(x) ;
        double y(y) ;
        double c3(c3) ;
        double c4(c4) ;
        double c5(c5) ;
    }
    
    
    
    
    ###############################################################################
    historical/historical.nc
    
    
    
    netcdf historical {
    dimensions:
        time = UNLIMITED ; // (30 currently)
        bnds = 2 ;
        rlon = 94 ;
        rlat = 114 ;
    variables:
        double time(time) ;
            time:standard_name = "time" ;
            time:long_name = "time" ;
            time:bounds = "time_bnds" ;
            time:units = "days since 1949-12-01 00:00:00" ;
            time:calendar = "360_day" ;
            time:axis = "T" ;
        double time_bnds(time, bnds) ;
        double lon(rlat, rlon) ;
            lon:standard_name = "longitude" ;
            lon:long_name = "longitude" ;
            lon:units = "degrees_east" ;
            lon:_CoordinateAxisType = "Lon" ;
        double lat(rlat, rlon) ;
            lat:standard_name = "latitude" ;
            lat:long_name = "latitude" ;
            lat:units = "degrees_north" ;
            lat:_CoordinateAxisType = "Lat" ;
        double rlon(rlon) ;
            rlon:standard_name = "projection_x_coordinate" ;
            rlon:long_name = "longitude in rotated-pole grid" ;
            rlon:units = "degrees" ;
            rlon:axis = "X" ;
        double rlat(rlat) ;
            rlat:standard_name = "projection_y_coordinate" ;
            rlat:long_name = "latitude in rotated-pole grid" ;
            rlat:units = "degrees" ;
            rlat:axis = "Y" ;
        float mrro(time, rlat, rlon) ;
            mrro:standard_name = "runoff_flux" ;
            mrro:long_name = "Total Runoff" ;
            mrro:units = "kg m-2 s-1" ;
            mrro:coordinates = "lat lon" ;
            mrro:_FillValue = 1.e+20f ;
            mrro:missing_value = 1.e+20f ;
            mrro:cell_methods = "time: mean" ;
        float Q100(rlat, rlon) ;
            Q100:units = "m3 s-1" ;
            Q100:_FillValue = 1.e+20f ;
            Q100:long_name = "Peak discharge" ;
            Q100:coordinates = "lat lon" ;
            Q100:grid_mapping = 0. ;
    
    // global attributes:
            :CDI = "Climate Data Interface version 1.9.5 (http://mpimet.mpg.de/cdi)" ;
            :source = "RegCM Model output file" ;
            :institution = "International Centre for Theoretical Physics" ;
            :Conventions = "CF-1.4" ;
            :project_id = "CORDEX" ;
            :ipcc_scenario_code = "HISTORICAL" ;
            :institute_id = "ICTP" ;
            :comment = "RegCM CORDEX EURO-CORDEX_30 run" ;
            :experiment_id = "historical" ;
            :driving_model_ensemble_member = "r1i1p1" ;
            :driving_experiment_name = "historical" ;
            :creation_date = "2018-08-10T12:05:06Z" ;
            :rcm_version_id = "v1" ;
            :ICTP_version_note = "Archived on model native grid" ;
            :contact = "esp@ictp.it" ;
            :product = "output" ;
            :tracking_id = "db7822a6-9c84-11e8-b848-0894ef50a14e" ;
            :title = "ICTP Regional Climatic model V4" ;
            :references = "http://gforge.ictp.it/gf/project/regcm" ;
            :model_revision = "tag-4.6.1" ;
            :projection = "LAMCON" ;
            :grid_size_in_meters = 12000. ;
            :latitude_of_projection_origin = 48. ;
            :longitude_of_projection_origin = 9.75 ;
            :standard_parallel = 30., 65. ;
            :grid_factor = 0.749565224994391 ;
            :landsurface_model = "clm4.5" ;
            :model_icbc_data_source = "HA_85" ;
            :model_sst_data_source = "HA_85" ;
            :boundary_nspgx = 40 ;
            :boundary_nspgd = 40 ;
            :boundary_high_nudge = 12. ;
            :boundary_medium_nudge = 8. ;
            :boundary_low_nudge = 4. ;
            :model_is_restarted = "No" ;
            :model_simulation_initial_start = "1970-06-01 00:00:00 UTC" ;
            :model_simulation_start = "1970-06-01 00:00:00 UTC" ;
            :model_simulation_end = "1970-09-01 00:00:00 UTC" ;
            :atmosphere_time_step_in_seconds = 24. ;
            :surface_interaction_time_step_in_seconds = 600. ;
            :convection_time_step_in_seconds = 240. ;
            :radiation_scheme_time_step_in_minuts = 30. ;
            :absorption_emission_time_step_in_hours = 18. ;
            :dynamical_core = 1 ;
            :asselin_filter_nu = 0.0625 ;
            :diffusion_hgt_factor = 1 ;
            :lateral_boundary_condition_scheme = 5 ;
            :semi_lagrangian_advection_scheme = 0 ;
            :boundary_layer_scheme = 2 ;
            :cumulus_convection_scheme_lnd = 5 ;
            :cumulus_convection_scheme_ocn = 5 ;
            :moisture_scheme = 1 ;
            :ocean_flux_scheme = 2 ;
            :zeng_ocean_roughness_formula = 1 ;
            :zeng_ocean_roughness_method = 1 ;
            :pressure_gradient_scheme = 0 ;
            :surface_emissivity_factor_computed = 0 ;
            :lake_model_activated = 0 ;
            :chemical_aerosol_scheme_activated = 0 ;
            :diurnal_cycle_sst_scheme = 0 ;
            :simple_sea_ice_scheme = 0 ;
            :seasonal_desert_albedo = 0 ;
            :convective_lwp_as_large_scale = 1 ;
            :large_scale_cloud_fraction_scheme = 0 ;
            :rrtm_radiation_scheme_activated = 0 ;
            :climatic_ozone_input_dataset = 0 ;
            :static_solar_constant_used = 0 ;
            :cumulus_cloud_model = 1 ;
            :subex_bottom_level_with_no_clouds = 1 ;
            :subex_auto_conversion_rate_for_land = 5.e-05 ;
            :subex_auto_conversion_rate_for_ocean = 0.00025 ;
            :subex_gultepe_factor_when_rain_for_land = 0.4 ;
            :subex_gultepe_factor_when_rain_for_ocean = 0.4 ;
            :subex_rh_with_fcc_one = 1.01 ;
            :subex_rh_threshold_for_land = 0.9 ;
            :subex_rh_threshold_for_ocean = 0.9 ;
            :subex_limit_temperature = 238. ;
            :subex_land_raindrop_evaporation_rate = 0.01 ;
            :subex_ocean_raindrop_evaporation_rate = 0.001 ;
            :subex_land_raindrop_accretion_rate = 3. ;
            :subex_ocean_raindrop_accretion_rate = 3. ;
            :subex_cloud_fraction_maximum = 0.75 ;
            :subex_condensation_threshold = 1. ;
            :subex_cloud_fraction_max_for_convection = 1. ;
            :subex_cloud_liqwat_max_for_convection = 0.0003 ;
            :tiedtke_actual_scheme = 4 ;
            :tiedtke_entrainment_rate_downdraft = 0.0003 ;
            :tiedtke_entrainment_rate_deep = 0.00175 ;
            :tiedtke_penetrative = "Yes" ;
            :tiedtke_midlevel = "Yes" ;
            :tiedtke_shallow = "Yes" ;
            :tiedtke_cumulus_downdraft = "Yes" ;
            :tiedtke_prognostic_cloud = "Yes" ;
            :tiedtke_cumulus_friction = "Yes" ;
            :tiedtke_ke_dissipation = "Yes" ;
            :tiedtke_tracer_transport = "Yes" ;
            :tiedtke_tracer_smooth_massflux = "No" ;
            :tiedtke_shallow_wstar_closure = "No" ;
            :tiedtke_detrainment_rate_deep = 7.5e-05 ;
            :tiedtke_shallow_entrainment = 2. ;
            :tiedtke_cloud_cover_evap_over_land = 0.05 ;
            :tiedtke_cloud_cover_evap_over_ocean = 0.05 ;
            :tiedtke_coeff_evap_over_land = 5.55e-05 ;
            :tiedtke_coeff_evap_over_ocean = 5.55e-05 ;
            :tiedtke_critical_rh_over_land = 0.5 ;
            :tiedtke_critical_rh_over_ocean = 0.6 ;
            :tiedtke_cloud_water_conv_over_land = 0.009 ;
            :tiedtke_cloud_water_conv_over_ocean = 0.003 ;
            :tiedtke_cape_adjustment_timescale = 10800. ;
            :uwpbl_advection_scheme = 0 ;
            :uwpbl_cloud_evap_entr_incr_efficiency = 15. ;
            :uwpbl_eddy_LS_stable_PBL_scaling = 1.5 ;
            :uwpbl_czero = 5.869 ;
            :uwpbl_nuk = 5. ;
            :frequency = "year" ;
            :c3s_disclaimer = "This data has been produced in the context of the\n",
                " C3S_34b_Lot1 and Lot 2 projects (PRINCIPLES/CORDEX4CDS) as a data\n",
                " provider for the Climate Data Store within the Copernicus Climate Change\n",
                " Service (C3S - https://climate.copernicus.eu/). While abiding by the\n",
                " highest scientific and technical standards, ECMWF cannot warrant that\n",
                " any information provided by the C3S will be entirely free from errors or\n",
                " omissions or that such errors or omissions can or will be rectified\n",
                " entirely. This applies to data from projects that continue to be\n",
                " developed, but are made publicly available for the purpose of feedback\n",
                " and testing. Some data or metadata may have been created or structured\n",
                " in files or formats that are not error-free. ECMWF accepts no\n",
                " responsibility with regard to such problems incurred as a result of\n",
                " using this data (see http://climate.copernicus.eu/disclaimer-privacy for\n",
                " the full disclaimer)" ;
            :experiment = "EUR-11" ;
            :CORDEX_domain = "EUR-11" ;
            :note = "The domain is larger than EUR-11" ;
            :driving_model_id = "MOHC-HadGEM2-ES" ;
            :driving_experiment = "MOHC-HadGEM2-ES, historical, r1i1p1" ;
            :model_id = "ICTP-RegCM4-6" ;
            :CDO = "Climate Data Operators version 1.9.5 (http://mpimet.mpg.de/cdo)" ;
            :history = "2019-01-21 15:54:12 CET : created by create_Qx_regcm.R ; Mon Jan 21 15:19:58 2019: cdo yearmax data_hadgem/historical.nc data_hadgem/yearmax/historical.nc\n",
                "Mon Jan 21 15:17:30 2019: cdo -L sellonlatbox,6.5,19,36,48 -selyear,1976/2005 /home/clima-archive4/CORDEX2/EUR-11/ICTP-RegCM4-6/MOHC-HadGEM2-ES/historical//mrro_EUR-11_MOHC-HadGEM2-ES_historical_r1i1p1_ICTP-RegCM4-6_v1_day_1970060112-2006010112.nc data_hadgem/historical.nc\n",
                "Thu Jan 10 10:18:03 2019: cdo -O -z zip remap,/home/netapp-clima/users/jciarlo/scripts/postproc_cordex/sftlf_EUR-11_ICHEC-EC-EARTH_rcp45_r3i1p1_DMI-HIRHAM5_v1_fx.nc,../../../011grid_CORDEX_weights.nc mrro_EUR-11_MOHC-HadGEM2-ES_historical_r1i1p1_ICTP-RegCM4-6_v1_day_1970060112-1980010112.nc mrro_EUR-11_MOHC-HadGEM2-ES_historical_r1i1p1_ICTP-RegCM4-6_v1_day_1970060112-1980010112.nc_remap.nc\n",
                "2017-10-31 16:25:30 : Created by RegCM RegCM Model program" ;
            :R_version = "R version 3.4.4 (2018-03-15)" ;
            :ncdf4_version = "1.16" ;
    }
    
    
    
    
    ###############################################################################
    historical/readme-historical.nc.md
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/historical/readme-
    historical.nc.md' had status 1
    
    
    
    
    ###############################################################################
    hmr_ita.nc
    
    
    
    netcdf hmr_ita {
    dimensions:
        time = UNLIMITED ; // (1 currently)
        x = 223 ;
        y = 248 ;
        nv4 = 4 ;
        height = 1 ;
    variables:
        double time(time) ;
            time:standard_name = "time" ;
            time:units = "hours since 2000-1-1 00:00:00" ;
            time:calendar = "proleptic_gregorian" ;
            time:axis = "T" ;
        float lon(y, x) ;
            lon:standard_name = "longitude" ;
            lon:long_name = "longitude" ;
            lon:units = "degrees_east" ;
            lon:_CoordinateAxisType = "Lon" ;
            lon:bounds = "lon_bnds" ;
        float lon_bnds(y, x, nv4) ;
        float lat(y, x) ;
            lat:standard_name = "latitude" ;
            lat:long_name = "latitude" ;
            lat:units = "degrees_north" ;
            lat:_CoordinateAxisType = "Lat" ;
            lat:bounds = "lat_bnds" ;
        float lat_bnds(y, x, nv4) ;
        double height(height) ;
            height:standard_name = "height" ;
            height:long_name = "height" ;
            height:units = "m" ;
            height:positive = "up" ;
            height:axis = "Z" ;
        float pr(time, height, y, x) ;
            pr:code = 164 ;
            pr:table = 129 ;
            pr:coordinates = "lat lon" ;
    
    // global attributes:
            :CDI = "Climate Data Interface version 1.9.1 (http://mpimet.mpg.de/cdi)" ;
            :Conventions = "CF-1.4" ;
            :history = "Tue Sep 18 11:04:05 2018: cdo -C seltimestep,100 /home/clima-archive4-b/afantini/chym_simulations/analysis/rain/hmr/hmr.nc /dev/shm/hmr.nc\n",
                "Wed Jul 11 15:25:58 2018: cdo -s -C -O mergetime hmr/months/hmr200001.nc hmr/months/hmr200002.nc hmr/months/hmr200003.nc hmr/months/hmr200004.nc hmr/months/hmr200005.nc hmr/months/hmr200006.nc hmr/months/hmr200007.nc hmr/months/hmr200008.nc hmr/months/hmr200009.nc hmr/months/hmr200010.nc hmr/months/hmr200011.nc hmr/months/hmr200012.nc hmr/months/hmr200101.nc hmr/months/hmr200102.nc hmr/months/hmr200103.nc hmr/months/hmr200104.nc hmr/months/hmr200105.nc hmr/months/hmr200106.nc hmr/months/hmr200107.nc hmr/months/hmr200108.nc hmr/months/hmr200109.nc hmr/months/hmr200110.nc hmr/months/hmr200111.nc hmr/months/hmr200112.nc hmr/months/hmr200201.nc hmr/months/hmr200202.nc hmr/months/hmr200203.nc hmr/months/hmr200204.nc hmr/months/hmr200205.nc hmr/months/hmr200206.nc hmr/months/hmr200207.nc hmr/months/hmr200208.nc hmr/months/hmr200209.nc hmr/months/hmr200210.nc hmr/months/hmr200211.nc hmr/months/hmr200212.nc hmr/months/hmr200301.nc hmr/months/hmr200302.nc hmr/months/hmr200303.nc hmr/months/hmr200304.nc hmr/months/hmr200305.nc hmr/months/hmr200306.nc hmr/months/hmr200307.nc hmr/months/hmr200308.nc hmr/months/hmr200309.nc hmr/months/hmr200310.nc hmr/months/hmr200311.nc hmr/months/hmr200312.nc hmr/months/hmr200401.nc hmr/months/hmr200402.nc hmr/months/hmr200403.nc hmr/months/hmr200404.nc hmr/months/hmr200405.nc hmr/months/hmr200406.nc hmr/months/hmr200407.nc hmr/months/hmr200408.nc hmr/months/hmr200409.nc hmr/months/hmr200410.nc hmr/months/hmr200411.nc hmr/months/hmr200412.nc hmr/months/hmr200501.nc hmr/months/hmr200502.nc hmr/months/hmr200503.nc hmr/months/hmr200504.nc hmr/months/hmr200505.nc hmr/months/hmr200506.nc hmr/months/hmr200507.nc hmr/months/hmr200508.nc hmr/months/hmr200509.nc hmr/months/hmr200510.nc hmr/months/hmr200511.nc hmr/months/hmr200512.nc hmr/months/hmr200601.nc hmr/months/hmr200602.nc hmr/months/hmr200603.nc hmr/months/hmr200604.nc hmr/months/hmr200605.nc hmr/months/hmr200606.nc hmr/months/hmr200607.nc hmr/months/hmr200608.nc hmr/months/hmr200609.nc hmr/months/hmr200610.nc hmr/months/hmr200611.nc hmr/months/hmr200612.nc hmr/months/hmr200701.nc hmr/months/hmr200702.nc hmr/months/hmr200703.nc hmr/months/hmr200704.nc hmr/months/hmr200705.nc hmr/months/hmr200706.nc hmr/months/hmr200707.nc hmr/months/hmr200708.nc hmr/months/hmr200709.nc hmr/months/hmr200710.nc hmr/months/hmr200711.nc hmr/months/hmr200712.nc hmr/months/hmr200801.nc hmr/months/hmr200802.nc hmr/months/hmr200803.nc hmr/months/hmr200804.nc hmr/months/hmr200805.nc hmr/months/hmr200806.nc hmr/months/hmr200807.nc hmr/months/hmr200808.nc hmr/months/hmr200809.nc hmr/months/hmr200810.nc hmr/months/hmr200811.nc hmr/months/hmr200812.nc hmr/months/hmr200901.nc hmr/months/hmr200902.nc hmr/months/hmr200903.nc hmr/months/hmr200904.nc hmr/months/hmr200905.nc hmr/months/hmr200906.nc hmr/months/hmr200907.nc hmr/months/hmr200908.nc hmr/months/hmr200909.nc hmr/months/hmr200910.nc hmr/months/hmr200911.nc hmr/months/hmr200912.nc hmr/months/hmr201001.nc hmr/months/hmr201002.nc hmr/months/hmr201003.nc hmr/months/hmr201004.nc hmr/months/hmr201005.nc hmr/months/hmr201006.nc hmr/months/hmr201007.nc hmr/months/hmr201008.nc hmr/months/hmr201009.nc hmr/months/hmr201010.nc hmr/months/hmr201011.nc hmr/months/hmr201012.nc hmr/months/hmr201101.nc hmr/months/hmr201102.nc hmr/months/hmr201103.nc hmr/months/hmr201104.nc hmr/months/hmr201105.nc hmr/months/hmr201106.nc hmr/months/hmr201107.nc hmr/months/hmr201108.nc hmr/months/hmr201109.nc hmr/months/hmr201110.nc hmr/months/hmr201111.nc hmr/months/hmr201112.nc hmr/months/hmr201201.nc hmr/months/hmr201202.nc hmr/months/hmr201203.nc hmr/months/hmr201204.nc hmr/months/hmr201205.nc hmr/months/hmr201206.nc hmr/months/hmr201207.nc hmr/months/hmr201208.nc hmr/months/hmr201209.nc hmr/months/hmr201210.nc hmr/months/hmr201211.nc hmr/months/hmr201212.nc hmr/months/hmr201301.nc hmr/months/hmr201302.nc hmr/months/hmr201303.nc hmr/months/hmr201304.nc hmr/months/hmr201305.nc hmr/months/hmr201306.nc hmr/months/hmr201307.nc hmr/months/hmr201308.nc hmr/months/hmr201309.nc hmr/months/hmr201310.nc hmr/months/hmr201311.nc hmr/months/hmr201312.nc hmr/hmr.nc\n",
                "Wed Jul 11 15:18:09 2018: cdo -s -O -C -L splityearmon -setname,pr -sellonlatbox,6.5,19,36,48 /home/esp-shared-a/Observations/HMR//mesan_rr24_2000.nc hmr/months/hmr\n",
                "Fri Jun 10 17:06:12 2016: cdo -f nc cat -setgridtype,curvilinear /nobackup/smhid9/sm_tland/euro4m/mesan_e4m/rr24nQC/2000/rr24_MESAN_20000101.grb /nobackup/smhid9/sm_tland/euro4m/mesan_e4m/rr24nQC/2000/rr24_MESAN_20000102.grb /nobackup/smhid9/sm_tland/euro4m/mesan_e4m/rr24nQC/2000/rr24_MESAN_20000103.grb /nobackup/smhid9/sm_tland/euro4m/mesan_e4m/rr24nQC/2000/rr24_MESAN_20000104.grb /nobackup/smhid9/sm_tland/euro4m/mesan_e4m/rr24nQC/2000/rr24_MESAN_20000105.grb /nobackup/smhid9/sm_tland/euro4m/mesan_e4m/rr24nQC/2000/rr24_MESAN_20000106.grb /nobackup/smhid9/sm_tland/euro4m/mesan_e4m/rr24nQC/2000/rr24_MESAN_20000107.grb /nobackup/smhid9/sm_tland/euro4m/mesan_e4m/rr24nQC/2000/rr24_MESAN_20000108.grb /nobackup/smhid9/sm_tland/euro4m/mesan_e4m/rr24nQC/2000/rr24_MESAN_20000109.grb /nobackup/smhid9/sm_tland/euro4m/mesan_e4m/rr24nQC/2000/rr24_MESAN_20000110.grb /nobackup/smhid9/sm_tland/euro4m/mesan_e4m/rr24nQC/2000/rr24_MESAN_20000111.grb /nobackup/smhid9/sm_tland/euro4m/mesan_e4m/rr24nQC/2000/rr24_MESAN_20000112.grb" ;
            :CDO = "Climate Data Operators version 1.9.1 (http://mpimet.mpg.de/cdo)" ;
    }
    
    
    
    
    ###############################################################################
    inverted_73/regcm-nn-2100_reg4_22.nc
    
    
    
    netcdf regcm-nn-2100_reg4_22 {
    dimensions:
        lon = 470 ;
        lat = 307 ;
        RP = 5 ;
    variables:
        double lon(lon) ;
            lon:units = "degrees_east" ;
            lon:standard_name = "longitude" ;
            lon:long_name = "Longitude" ;
        double lat(lat) ;
            lat:units = "degrees_north" ;
            lat:standard_name = "latitude" ;
            lat:long_name = "Latitude" ;
        double RP(RP) ;
            RP:units = "years" ;
            RP:long_name = "RP" ;
        float POT(RP, lat, lon) ;
            POT:units = "percent" ;
            POT:_FillValue = -1.f ;
            POT:long_name = "Exceedance frequency" ;
            POT:coordinates = "lon lat" ;
            POT:valid_timesteps = 258480 ;
            POT:region = 4 ;
            POT:simulation = 22 ;
            POT:mask_value = 5 ;
            POT:period_name = 2100 ;
            POT:ref_period_name = 2005. ;
    
    // global attributes:
            :history = "2018-11-10 23:37:10 CET : created by calc_POT_noraster.R" ;
            :R_version = "R version 3.5.1 (2018-07-02)" ;
            :ncdf4_version = "1.16" ;
            :Conventions = "CF-1.7" ;
            :Creation_date = "2018-11-10 23:37:10 CET" ;
            :Return_period = 2., 10., 20., 50., 100. ;
    }
    
    
    
    
    ###############################################################################
    large-mem/pp_ens_mean_0.25deg_reg_v19.0e.nc
    
    
    
    netcdf pp_ens_mean_0.25deg_reg_v19.0e {
    dimensions:
        latitude = 201 ;
        longitude = 464 ;
        time = UNLIMITED ; // (25202 currently)
    variables:
        double latitude(latitude) ;
            latitude:units = "degrees_north" ;
            latitude:long_name = "Latitude values" ;
            latitude:axis = "Y" ;
            latitude:standard_name = "latitude" ;
        double longitude(longitude) ;
            longitude:units = "degrees_east" ;
            longitude:long_name = "Longitude values" ;
            longitude:axis = "X" ;
            longitude:standard_name = "longitude" ;
        short pp(time, latitude, longitude) ;
            pp:units = "hPa" ;
            pp:_FillValue = -9999s ;
            pp:long_name = "sea level pressure" ;
            pp:scale_factor = 0.1f ;
            pp:add_offset = 0.f ;
            pp:standard_name = "air_pressure_at_sea_level" ;
        int time(time) ;
            time:units = "days since 1950-01-01 00:00" ;
            time:long_name = "Time in days" ;
            time:calendar = "standard" ;
            time:standard_name = "time" ;
    
    // global attributes:
            :E-OBS_version = "19.0e" ;
            :Conventions = "CF-1.4" ;
            :References = "http://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php" ;
            :history = "Mon Feb 18 12:49:39 2019: ncks -O -d time,0,25201 /data4/Else/EOBSv19.0e/Grid_0.25deg/pp/pp_ensmean_master_untilJan2019.nc /data4/Else/EOBSv19.0e/Grid_0.25deg/pp/pp_ensmean_master.nc" ;
            :NCO = "netCDF Operators version 4.7.5 (Homepage = http://nco.sf.net, Code = http://github.com/nco/nco)" ;
    }
    
    
    
    
    ###############################################################################
    mrso/mrso_Lmon_CMCC-CESM_rcp85_r1i1p1_200001-200412.nc
    
    
    
    netcdf mrso_Lmon_CMCC-CESM_rcp85_r1i1p1_200001-200412 {
    dimensions:
        time = UNLIMITED ; // (60 currently)
        lat = 48 ;
        lon = 96 ;
        bnds = 2 ;
    variables:
        double time(time) ;
            time:bounds = "time_bnds" ;
            time:units = "days since 2000-1-1" ;
            time:calendar = "standard" ;
            time:axis = "T" ;
            time:long_name = "time" ;
            time:standard_name = "time" ;
        double time_bnds(time, bnds) ;
        double lat(lat) ;
            lat:bounds = "lat_bnds" ;
            lat:units = "degrees_north" ;
            lat:axis = "Y" ;
            lat:long_name = "latitude" ;
            lat:standard_name = "latitude" ;
        double lat_bnds(lat, bnds) ;
        double lon(lon) ;
            lon:bounds = "lon_bnds" ;
            lon:units = "degrees_east" ;
            lon:axis = "X" ;
            lon:long_name = "longitude" ;
            lon:standard_name = "longitude" ;
        double lon_bnds(lon, bnds) ;
        float mrso(time, lat, lon) ;
            mrso:standard_name = "soil_moisture_content" ;
            mrso:long_name = "Total Soil Moisture Content" ;
            mrso:comment = "the mass per unit area  (summed over all soil layers) of water in all phases." ;
            mrso:units = "kg m-2" ;
            mrso:original_name = "ws" ;
            mrso:cell_methods = "time: mean (interval: 1 month) area: mean where land" ;
            mrso:cell_measures = "area: areacella" ;
            mrso:missing_value = 1.e+20f ;
            mrso:_FillValue = 1.e+20f ;
            mrso:associated_files = "baseURL: http://cmip-pcmdi.llnl.gov/CMIP5/dataLocation gridspecFile: gridspec_land_fx_CMCC-CESM_rcp85_r0i0p0.nc areacella: areacella_fx_CMCC-CESM_rcp85_r0i0p0.nc" ;
            mrso:history = "2012-07-26T14:52:07Z altered by CMOR: Inverted axis: lat." ;
    
    // global attributes:
            :institution = "CMCC - Centro Euro-Mediterraneo per i Cambiamenti Climatici, Bologna, Italy" ;
            :institute_id = "CMCC" ;
            :experiment_id = "rcp85" ;
            :source = "CMCC-CESM" ;
            :model_id = "CMCC-CESM" ;
            :forcing = "Nat,Ant,GHG,SA,Oz,Sl" ;
            :parent_experiment_id = "historical" ;
            :parent_experiment_rip = "r1i1p1" ;
            :branch_time = 56978. ;
            :contact = "Marcello Vichi (marcello.vichi@cmcc.it)" ;
            :history = "Model output postprocessed with Afterburner and CDO (https://code.zmaw.de/projects) 2012-07-26T14:52:07Z CMOR rewrote data to comply with CF standards and CMIP5 requirements." ;
            :comment = "Equilibrium reached after more than 1500-year spin-up of the physics, 200-year spin-up of carbon content and 276 year at pre-industrial GHG concentrations after which data were output with nominal date of January 1850." ;
            :references = "model described in the documentation at http://www.cmcc.it/data-models/models" ;
            :initialization_method = 1 ;
            :physics_version = 1 ;
            :tracking_id = "bf042e49-b815-4ea8-bc2c-e0824db2cc14" ;
            :product = "output" ;
            :experiment = "RCP8.5" ;
            :frequency = "mon" ;
            :creation_date = "2012-07-26T14:52:07Z" ;
            :Conventions = "CF-1.4" ;
            :project_id = "CMIP5" ;
            :table_id = "Table Lmon (27 April 2011) c4244dce0826a43bb0b259f293e2f742" ;
            :title = "CMCC-CESM model output prepared for CMIP5 RCP8.5" ;
            :parent_experiment = "historical" ;
            :modeling_realm = "land" ;
            :realization = 1 ;
            :cmor_version = "2.7.1" ;
    }
    
    
    
    
    ###############################################################################
    mrso/readme
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/mrso/readme' had status 1
    
    
    
    
    ###############################################################################
    nhsce_v01r01_19661004_20140203.nc
    
    
    
    netcdf nhsce_v01r01_19661004_20140203 {
    dimensions:
        cols = 88 ;
        rows = 88 ;
        time = UNLIMITED ; // (2470 currently)
    variables:
        char coord_system ;
            coord_system:grid_mapping_name = "latitude_longitude" ;
            coord_system:longitude_of_central_meridian = 0. ;
            coord_system:semimajor_axis = 6378137 ;
            coord_system:semiminor_axis = 6356752.3 ;
        int time(time) ;
            time:standard_name = "time" ;
            time:long_name = "time" ;
            time:units = "days since 1966-10-03" ;
            time:axis = "T" ;
            time:valid_range = 7, 17290 ;
            time:calendar = "gregorian" ;
        float snow_cover_threshold ;
            snow_cover_threshold:standard_name = "surface_snow_area_fraction" ;
            snow_cover_threshold:long_name = "threshold for the snow_cover_extent measurement" ;
            snow_cover_threshold:units = "1" ;
        double latitude(rows, cols) ;
            latitude:standard_name = "latitude" ;
            latitude:long_name = "latitude of cell center in half mesh grid, based on NOAA NMC Limited Area Fine Mesh Grid" ;
            latitude:units = "degrees_north" ;
            latitude:valid_range = 0., 90. ;
            latitude:_FillValue = -999. ;
        double longitude(rows, cols) ;
            longitude:standard_name = "longitude" ;
            longitude:long_name = "longitude of cell center in half mesh grid, based on NOAA NMC Limited Area Fine Mesh Grid" ;
            longitude:units = "degrees_east" ;
            longitude:valid_range = -180., 180. ;
            longitude:_FillValue = -999. ;
        byte land(rows, cols) ;
            land:long_name = "land water mask" ;
            land:standard_name = "land_binary_mask" ;
            land:grid_mapping = "coord_system" ;
            land:coordinates = "longitude latitude" ;
            land:valid_range = 0b, 1b ;
            land:flag_values = 0b, 1b ;
            land:flag_meanings = "water land" ;
            land:_FillValue = -9b ;
        float area(rows, cols) ;
            area:long_name = "cell area in km^2" ;
            area:standard_name = "cell_area" ;
            area:grid_mapping = "coord_system" ;
            area:coordinates = "longitude latitude" ;
            area:units = "km^2" ;
            area:valid_range = 10676.8f, 41804.6f ;
            area:_FillValue = -999.9f ;
        byte snow_cover_extent(time, rows, cols) ;
            snow_cover_extent:long_name = "NOAA/NCDC Climate Data Record of snow cover extent" ;
            snow_cover_extent:standard_name = "surface_snow_binary_mask" ;
            snow_cover_extent:grid_mapping = "coord_system" ;
            snow_cover_extent:coordinates = "longitude latitude time snow_cover_threshold" ;
            snow_cover_extent:valid_range = 0b, 1b ;
            snow_cover_extent:flag_values = 0b, 1b ;
            snow_cover_extent:flag_meanings = "no_snow snow_covered" ;
            snow_cover_extent:_FillValue = -9b ;
    
    // global attributes:
            :Conventions = "CF-1.6" ;
            :Metadata_Conventions = "CF-1.6, Unidata Dataset Discovery v1.0, NOAA CDR v1.0, GDS v2.0" ;
            :standard_name_vocabulary = "CF Standard Name Table (v22, 12 February 2013)" ;
            :id = "nhsce_v01r01_19661004_20140203.nc" ;
            :naming_authority = "gov.noaa.ncdc" ;
            :metadata_link = "http://www1.ncdc.noaa.gov/pub/data/metadata/published/catalog/fgdc/xml/C00756.xml" ;
            :title = "Climate Data Record (CDR) of Northern Hemisphere (NH) Snow Cover Extent (SCE) (CDR Name: Snow_Cover_Extent_NH_IMS_Robinson)" ;
            :product_version = "v01r01" ;
            :summary = "The data record for the NH SCE CDR spans from October 4, 1966 to present. Prior to June 1999 the NH SCE CDR is based on satellite-derived maps of NH SCE produced weekly by trained NOAA meteorologists. Early NH SCE maps were based on a visual interpretation of photographic copies of shortwave imagery. Analysts incorporated various sources of imagery into the SCE mapping process as they became available (e.g. AVHRR, VAS). In June 1999 NOAA NH SCE maps were replaced by SCE output from the Interactive Multisensor Snow and Ice Mapping System (IMS) at the National Ice Center (NIC). SCE output from the NIC IMS is processed at Rutgers University and appended to the NH SCE CDR to form a cohesive, long-term climate record of SCE. " ;
            :keywords = "EARTH SCIENCE > CRYOSPHERE > SNOW/ICE > SNOW COVER, EARTH SCIENCE > TERRESTRIAL HYDROSPHERE > SNOW/ICE > SNOW COVER, EARTH SCIENCE > CLIMATE INDICATORS > CRYOSPHERIC INDICATORS > SNOW COVER" ;
            :keywords_vocabulary = "NASA Global Change Master Directory (GCMD) Earth Science Keywords, Version 8.0" ;
            :platform = "ESSA, NOAA POES, SMS, DMSP, GOES, TIROS, METEOSAT, GMS, TERRA, AQUA, METOP" ;
            :sensor = "VIDEO CAMERA, VISSR, VAS, VHRR, AVHRR, VISSR-GMS, VISSR-METEOSAT, SEVIRI, MODIS, AMSU-B, AMSR-E, SSMIS, VIIRS" ;
            :cdm_data_type = "Grid" ;
            :cdr_program = "NOAA Climate Data Record Program for satellites" ;
            :cdr_variable = "snow_cover_extent" ;
            :source = "NOAA NH Weekly SCE, NIC NH IMS SCE" ;
            :date_created = "2014-02-05T01:56:32Z" ;
            :institution = "Global Snow Lab, Center for Environmental Prediction, Rutgers University" ;
            :geospatial_lat_units = "degrees_north" ;
            :geospatial_lon_units = "degrees_east" ;
            :geospatial_lat_min = 0. ;
            :geospatial_lat_max = 90. ;
            :geospatial_lon_min = -180. ;
            :geospatial_lon_max = 180. ;
            :spatial_resolution = "Minimum cell area 10676.8 km^2, maximum cell area 41804.6 km^2" ;
            :time_coverage_start = "1966-10-04" ;
            :time_coverage_end = "2014-02-03" ;
            :license = "No restrictions on access or use" ;
    }
    
    
    
    
    ###############################################################################
    NSIDC/alaska_2007_2008_swe_v01.nc
    
    
    
    netcdf alaska_2007_2008_swe_v01 {
    dimensions:
        west_east = 327 ;
        south_north = 237 ;
        days = 274 ;
        charlength = 10 ;
    variables:
        double lat(south_north, west_east) ;
            lat:coordinates = "XLONG XLAT" ;
            lat:units = "degrees_north" ;
        double lon(south_north, west_east) ;
            lon:coordinates = "XLONG XLAT" ;
            lon:units = "degrees_east" ;
        double elevation(south_north, west_east) ;
            elevation:coordinates = "XLONG XLAT" ;
            elevation:units = "meters" ;
        double swe(days, south_north, west_east) ;
            swe:coordinates = "XLONG XLAT" ;
            swe:units = "mm" ;
        double mask(south_north, west_east) ;
            mask:coordinates = "XLONG XLAT" ;
            mask:units = "[]" ;
        char time(charlength, days) ;
            time:units = "[]" ;
    
    // global attributes:
            :title = "OUTPUT FROM WRF V3.6.1 MODEL" ;
            :creation_date = "22-May-2017 16:16:33" ;
            :wateryear = "2008" ;
            :dx = 9000.f ;
            :dy = 9000.f ;
            :map_projection = "Lambert Conformal" ;
    }
    
    
    
    
    ###############################################################################
    NSIDC/readme
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/NSIDC/readme' had status 1
    
    
    
    
    ###############################################################################
    NSIDC/sierra_2008_2009_swe_v01.nc
    
    
    
    netcdf sierra_2008_2009_swe_v01 {
    dimensions:
        west_east = 90 ;
        south_north = 162 ;
        days = 274 ;
        charlength = 10 ;
    variables:
        double lat(south_north, west_east) ;
            lat:coordinates = "XLONG XLAT" ;
            lat:units = "degrees_north" ;
        double lon(south_north, west_east) ;
            lon:coordinates = "XLONG XLAT" ;
            lon:units = "degrees_east" ;
        double elevation(south_north, west_east) ;
            elevation:coordinates = "XLONG XLAT" ;
            elevation:units = "meters" ;
        double swe(days, south_north, west_east) ;
            swe:coordinates = "XLONG XLAT" ;
            swe:units = "mm" ;
        double mask(south_north, west_east) ;
            mask:coordinates = "XLONG XLAT" ;
            mask:units = "[]" ;
        char time(charlength, days) ;
            time:units = "[]" ;
    
    // global attributes:
            :title = "OUTPUT FROM WRF V3.6.1 MODEL" ;
            :creation_date = "22-May-2017 16:26:16" ;
            :wateryear = "2009" ;
            :dx = 9000.f ;
            :dy = 9000.f ;
            :map_projection = "Lambert Conformal" ;
    }
    
    
    
    
    ###############################################################################
    ob_tran/example_ob_tran.nc
    
    
    
    netcdf example_ob_tran {
    dimensions:
        time = UNLIMITED ; // (1 currently)
        bnds = 2 ;
        rlon = 106 ;
        rlat = 103 ;
        vertices = 4 ;
    variables:
        double time(time) ;
            time:standard_name = "time" ;
            time:long_name = "time" ;
            time:bounds = "time_bnds" ;
            time:units = "days since 1949-12-01T00:00:00Z" ;
            time:calendar = "proleptic_gregorian" ;
            time:axis = "T" ;
        double time_bnds(time, bnds) ;
        float lon(rlat, rlon) ;
            lon:standard_name = "longitude" ;
            lon:long_name = "longitude coordinate" ;
            lon:units = "degrees_east" ;
            lon:_CoordinateAxisType = "Lon" ;
            lon:bounds = "lon_bnds" ;
        float lon_bnds(rlat, rlon, vertices) ;
        float lat(rlat, rlon) ;
            lat:standard_name = "latitude" ;
            lat:long_name = "latitude coordinate" ;
            lat:units = "degrees_north" ;
            lat:_CoordinateAxisType = "Lat" ;
            lat:bounds = "lat_bnds" ;
        float lat_bnds(rlat, rlon, vertices) ;
        double rlon(rlon) ;
            rlon:standard_name = "grid_longitude" ;
            rlon:long_name = "longitude in rotated pole grid" ;
            rlon:units = "degrees" ;
            rlon:axis = "X" ;
        double rlat(rlat) ;
            rlat:standard_name = "grid_latitude" ;
            rlat:long_name = "latitude in rotated pole grid" ;
            rlat:units = "degrees" ;
            rlat:axis = "Y" ;
        int rotated_latitude_longitude ;
            rotated_latitude_longitude:grid_mapping_name = "rotated_latitude_longitude" ;
            rotated_latitude_longitude:grid_north_pole_latitude = 39.25 ;
            rotated_latitude_longitude:grid_north_pole_longitude = -162. ;
            rotated_latitude_longitude:north_pole_grid_longitude = 0. ;
        double height ;
            height:standard_name = "height" ;
            height:long_name = "height" ;
            height:units = "m" ;
            height:positive = "up" ;
            height:axis = "Z" ;
        float tas(time, rlat, rlon) ;
            tas:standard_name = "air_temperature" ;
            tas:long_name = "Near-Surface Air Temperature" ;
            tas:units = "K" ;
            tas:grid_mapping = "rotated_latitude_longitude" ;
            tas:coordinates = "height lat lon" ;
            tas:_FillValue = 1.e+20f ;
            tas:missing_value = 1.e+20f ;
            tas:comment = "daily-mean near-surface (usually, 2 meter) air temperature." ;
            tas:cell_methods = "time: mean" ;
            tas:history = "2014-03-17T13:06:43Z altered by CMOR: Treated scalar dimension: \'height\'. 2014-03-17T13:06:43Z altered by CMOR: replaced missing value flag (-1e+20) with standard missing value (1e+20)." ;
            tas:associated_files = "gridspecFile: gridspec_atmos_fx_CLMcom-CCLM4-8-17_evaluation_r0i0p0.nc" ;
    
    // global attributes:
            :CDI = "Climate Data Interface version 1.9.1 (http://mpimet.mpg.de/cdi)" ;
            :history = "Wed Oct 17 10:54:49 2018: cdo -C seltimestep,1 evaluation/MM/CLMcom-CCLM4-8-17/tas_EUR-44_ECMWF-ERAINT_evaluation_r1i1p1_CLMcom-CCLM4-8-17_v1_mon_197901-198012.nc /dev/shm/example_ob_tran.nc\n",
                "Processing for CORDEX archive at DKRZ (SVN revision 4244 http://svn-mad.zmaw.de/svn/mad/Model/IMDI/tags/cclm/cosmo_090213_4.8_clm17_cordex/util/running) 2014-03-17T13:06:43Z CMOR rewrote data to comply with CF standards and CORDEX requirements." ;
            :source = "CLMcom-CCLM4-8-17" ;
            :institution = "Climate Limited-area Modelling Community (CLM-Community)" ;
            :Conventions = "CF-1.4" ;
            :institute_id = "CLMcom" ;
            :experiment_id = "evaluation" ;
            :model_id = "CLMcom-CCLM4-8-17" ;
            :contact = "cordex-cclm@dkrz.de" ;
            :comment = "CORDEX Europe RCM CCLM 0.44 deg EUR-44" ;
            :references = "http://www.clm-community.eu/" ;
            :initialization_method = 1 ;
            :physics_version = 1 ;
            :tracking_id = "63986e70-d227-4b5c-a4c1-2af6224616a3" ;
            :title = "CLMcom-CCLM4-8-17 model output prepared for CORDEX Evaluation run with reanalysis forcing" ;
            :CORDEX_domain = "EUR-44" ;
            :driving_experiment = "ECMWF-ERAINT, evaluation, r1i1p1" ;
            :driving_model_id = "ECMWF-ERAINT" ;
            :driving_model_ensemble_member = "r1i1p1" ;
            :driving_experiment_name = "evaluation" ;
            :rcm_version_id = "v1" ;
            :product = "output" ;
            :experiment = "Evaluation run with reanalysis forcing" ;
            :frequency = "mon" ;
            :creation_date = "2014-03-17T13:06:43Z" ;
            :project_id = "CORDEX" ;
            :table_id = "Table mon (Sept 2013) 1a8d24384e63c141a57dbedfd6710546" ;
            :modeling_realm = "atmos" ;
            :realization = 1 ;
            :cmor_version = "2.9.1" ;
            :CDO = "Climate Data Operators version 1.9.1 (http://mpimet.mpg.de/cdo)" ;
    }
    
    
    
    
    ###############################################################################
    ob_tran/example_ob_tran2.nc
    
    
    
    netcdf example_ob_tran2 {
    dimensions:
        time = UNLIMITED ; // (1 currently)
        bnds = 2 ;
        rlon = 106 ;
        rlat = 103 ;
    variables:
        double time(time) ;
            time:standard_name = "time" ;
            time:long_name = "time" ;
            time:bounds = "time_bnds" ;
            time:units = "days since 1949-12-01 00:00:00" ;
            time:calendar = "standard" ;
            time:axis = "T" ;
        double time_bnds(time, bnds) ;
        double lon(rlat, rlon) ;
            lon:standard_name = "longitude" ;
            lon:long_name = "longitude" ;
            lon:units = "degrees_east" ;
            lon:_CoordinateAxisType = "Lon" ;
        double lat(rlat, rlon) ;
            lat:standard_name = "latitude" ;
            lat:long_name = "latitude" ;
            lat:units = "degrees_north" ;
            lat:_CoordinateAxisType = "Lat" ;
        double rlon(rlon) ;
            rlon:standard_name = "grid_longitude" ;
            rlon:long_name = "longitude in rotated pole grid" ;
            rlon:units = "degrees" ;
            rlon:axis = "X" ;
        double rlat(rlat) ;
            rlat:standard_name = "grid_latitude" ;
            rlat:long_name = "latitude in rotated pole grid" ;
            rlat:units = "degrees" ;
            rlat:axis = "Y" ;
        int rotated_pole ;
            rotated_pole:grid_mapping_name = "rotated_latitude_longitude" ;
            rotated_pole:grid_north_pole_latitude = 39.25f ;
            rotated_pole:grid_north_pole_longitude = -162.f ;
        double height ;
            height:standard_name = "height" ;
            height:long_name = "height" ;
            height:units = "m" ;
            height:positive = "up" ;
            height:axis = "Z" ;
        float tas(time, rlat, rlon) ;
            tas:standard_name = "air_temperature" ;
            tas:long_name = "Near-Surface Air Temperature" ;
            tas:units = "K" ;
            tas:grid_mapping = "rotated_pole" ;
            tas:coordinates = "height lat lon" ;
            tas:_FillValue = 1.e+20f ;
            tas:missing_value = 1.e+20f ;
            tas:cell_methods = "time: mean" ;
    
    // global attributes:
            :CDI = "Climate Data Interface version 1.9.1 (http://mpimet.mpg.de/cdi)" ;
            :history = "Wed Oct 17 11:05:07 2018: cdo -C seltimestep,1 /home/esp-shared-a/RegionalModels/CORDEX/EUR-44/evaluation/MM/KNMI-RACMO22E/tas_EUR-44_ECMWF-ERAINT_evaluation_r1i1p1_KNMI-RACMO22E_v1_mon_197901-198012.nc example_ob_tran2.nc" ;
            :institution = "Royal Netherlands Meteorological Institute" ;
            :Conventions = "CF-1.4" ;
            :contact = "Erik van Meijgaard, KNMI, Regional Climate division (vanmeijg@knmi.nl)" ;
            :experiment = "Evaluation run with reanalysis forcing" ;
            :experiment_id = "evaluation" ;
            :realization = "1" ;
            :driving_experiment = "ECMWF-ERAINT,evaluation,r1i1p1" ;
            :driving_model_id = "ECMWF-ERAINT" ;
            :driving_model_ensemble_member = "r1i1p1" ;
            :driving_experiment_name = "evaluation" ;
            :institute_id = "KNMI" ;
            :model_id = "KNMI-RACMO22E" ;
            :rcm_version_id = "v1" ;
            :references = "http://www.knmi.nl/research/regional_climate" ;
            :project_id = "CORDEX" ;
            :CORDEX_domain = "EUR-44" ;
            :product = "output" ;
            :frequency = "mon" ;
            :knmi_model_comment = "RACMO22E: baseline physics from ECMWF CY31r1; modifications include HTESSEL CY33r1, patch K-diffusion CY32r3, moist Turbulent Kinetic Energy, satellite inferred Leaf Area Index" ;
            :knmi_version_comment = "v1: reference version for Europe and other midlatitude regions" ;
            :knmi_grib_path = "mos.knmi.nl:/climreg/CXEUR50/eCS6-v420-fERAIN/GRIB_data" ;
            :creation_date = "2014-01-09T21:35:03Z" ;
            :tracking_id = "60ab205f-db71-421e-a257-fd0843ca77a8" ;
            :CDO = "Climate Data Operators version 1.9.1 (http://mpimet.mpg.de/cdo)" ;
    }
    
    
    
    
    ###############################################################################
    ob_tran/out.tif
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/ob_tran/out.tif' had
    status 1
    
    
    
    
    ###############################################################################
    ob_tran/readme.txt
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/ob_tran/readme.txt' had
    status 1
    
    
    
    
    ###############################################################################
    oscar_gdr_5d1993.nc
    
    
    
    netcdf oscar_gdr_5d1993 {
    dimensions:
        latitude = 70 ;
        longitude = 170 ;
        time = 72 ;
        depth = 1 ;
        strlen = 11 ;
    variables:
        float latitude(latitude) ;
            latitude:units = "degree-N" ;
            latitude:long_name = "Latitude" ;
        float longitude(longitude) ;
            longitude:units = "degree-E" ;
            longitude:long_name = "Longitude" ;
        int time(time) ;
            time:units = "days since 1992-10-05 00:00:00" ;
            time:long_name = "Time" ;
        char date(time, strlen) ;
            date:long_name = "Date in character string" ;
        float depth(depth) ;
            depth:units = "meter" ;
            depth:long_name = "Depth" ;
        int mask(latitude, longitude) ;
            mask:long_name = "Mask" ;
        float u(time, depth, latitude, longitude) ;
            u:units = "meter/sec" ;
            u:long_name = "Zonal Velocity" ;
            u:missing_value = NaN ;
        float v(time, depth, latitude, longitude) ;
            v:units = "meter/sec" ;
            v:long_name = "Meridional Velocity" ;
            v:missing_value = NaN ;
        float uf(time, depth, latitude, longitude) ;
            uf:units = "meter/sec" ;
            uf:long_name = "Filtered Zonal Velocity" ;
            uf:missing_value = NaN ;
        float vf(time, depth, latitude, longitude) ;
            vf:units = "meter/sec" ;
            vf:long_name = "Filtered Meridional Velocity" ;
            vf:missing_value = NaN ;
    
    // global attributes:
            :year = "1993" ;
            :description = "Tropical Pacific Sea Surface Velocity" ;
            :version = 2002.f ;
            :source = "Gary Lagerloef, ESR (lager@esr.org) and Fabrice Bonjean (bonjean@esr.org)" ;
            :contact = "Fabrice Bonjean (bonjean@esr.org) or John T. Gunn (gunn@esr.org)" ;
            :company = "Earth & Space Researh, Seattle, WA" ;
            :reference1 = "Bonjean F. and G.S.E. Lagerloef, 2002 ,\"Diagnostic model and analysis of the surface currents in the tropical Pacific ocean\", J. Phys. Oceanogr., 32, 2,938-2,954" ;
            :reference2 = "Lagerloef, G. S. E., G. T. Mitchum, R. B. Lukas and P.P. Niiler, 1999, Tropical Pacific near-surface currents estimated from altimeter, wind and drifter data, J. Geophys. Res., 104, 23,313-23,326" ;
            :date = "19-Mar-2004" ;
    }
    
    
    
    
    ###############################################################################
    R13352.nc
    
    
    
    netcdf R13352 {
    dimensions:
        depth = 51 ;
        profile = 54 ;
        string_df = 72 ;
        string8 = 8 ;
        string1 = 1 ;
    variables:
        int profile_number(profile) ;
            profile_number:long_name = "Profile Number" ;
            profile_number:units = "scalar" ;
            profile_number:data_min = 1 ;
            profile_number:data_max = 12 ;
            profile_number:var_desc = "Profile number" ;
        char data_file(profile, string_df) ;
            data_file:long_name = "Data File" ;
            data_file:var_desc = "Original netcdf data file x each profile" ;
        char float_id(profile, string8) ;
            float_id:long_name = "Float Identifier" ;
            float_id:var_desc = "Float identifier number" ;
        double jday(profile) ;
            jday:long_name = "Julian Day" ;
            jday:units = "days since -4712/1/1 12:00:0.0 (julian day)" ;
            jday:data_min = 2451221.60347222 ;
            jday:data_max = 2452078.60694444 ;
            jday:var_desc = "Time in julian days" ;
        int year(profile) ;
            year:long_name = "Year" ;
            year:units = "year" ;
            year:data_min = 1999 ;
            year:data_max = 2001 ;
            year:var_desc = "Year of observation" ;
        int month(profile) ;
            month:long_name = "Month" ;
            month:units = "month" ;
            month:data_min = 1 ;
            month:data_max = 12 ;
            month:var_desc = "Month of observation" ;
        int day(profile) ;
            day:long_name = "Day" ;
            day:units = "day" ;
            day:data_min = 1 ;
            day:data_max = 31 ;
            day:var_desc = "Day of observation" ;
        int hour(profile) ;
            hour:long_name = "Hour" ;
            hour:units = "hour" ;
            hour:var_desc = "Hour of observation" ;
        int minute(profile) ;
            minute:long_name = "Minute" ;
            minute:units = "minute" ;
            minute:var_desc = "Minute of observation" ;
        int second(profile) ;
            second:long_name = "Second" ;
            second:units = "second" ;
            second:var_desc = "Second of observation" ;
        double decimal_time(profile) ;
            decimal_time:long_name = "Decimal Time" ;
            decimal_time:units = "years since 1-1-1 00:00.00" ;
            decimal_time:data_min = 1999.11458856187 ;
            decimal_time:data_max = 2001.46093619287 ;
            decimal_time:var_desc = "Time since 1-1-1 00:00.00 in years" ;
        double lon(profile) ;
            lon:long_name = "Longitude" ;
            lon:units = "degrees_east" ;
            lon:valid_range = 0., 360. ;
            lon:data_min = 0.379999999999995 ;
            lon:data_max = 359.9 ;
            lon:var_desc = "Longitude" ;
        double lat(profile) ;
            lat:long_name = "Latitude" ;
            lat:units = "degrees_north" ;
            lat:valid_range = -90., 90. ;
            lat:data_min = 2.84 ;
            lat:data_max = 6.31 ;
            lat:var_desc = "Latitude" ;
        int npoints(profile) ;
            npoints:long_name = "Observations number" ;
            npoints:units = "scalar" ;
            npoints:valid_range = 0, 300 ;
            npoints:data_min = 3 ;
            npoints:data_max = 51 ;
            npoints:var_desc = "Number of observations x profile" ;
        double p(profile, depth) ;
            p:long_name = "Sea Pressure" ;
            p:units = "decibar" ;
            p:valid_range = 0., 12000. ;
            p:data_min = 2. ;
            p:data_max = 961. ;
            p:missing_value = 99999. ;
            p:_FillValue = 99999. ;
            p:resolution = 0.1 ;
            p:var_desc = "In situ pressure measurement, sea surface = 0" ;
        double t(profile, depth) ;
            t:long_name = "Sea Temperature ITS-90 scale" ;
            t:units = "degC" ;
            t:valid_range = -2., 40. ;
            t:data_min = 4.6100001335144 ;
            t:data_max = 29.7999992370605 ;
            t:missing_value = 99999. ;
            t:_FillValue = 99999. ;
            t:resolution = 0.001 ;
            t:var_desc = "In situ temperature measurement" ;
        double s(profile, depth) ;
            s:long_name = "Pratical Salinity" ;
            s:units = "psu" ;
            s:valid_range = 0., 42. ;
            s:data_min = 99999. ;
            s:data_max = 99999. ;
            s:missing_value = 99999. ;
            s:_FillValue = 99999. ;
            s:resolution = 0.001 ;
            s:var_desc = "In situ salinity measurement" ;
        char p_qc(profile, depth, string1) ;
            p_qc:long_name = "Pressure Quality Flag" ;
            p_qc:missing_value = "9" ;
            p_qc:_FillValue = " " ;
            p_qc:var_desc = "Sea pressure quality flag, Argo reference table 2" ;
            p_qc:leg_1 = "0  No QC performed" ;
            p_qc:leg_2 = "1  Good data" ;
            p_qc:leg_3 = "2  Probably good data" ;
            p_qc:leg_4 = "3  Bad data which is potentially recoverable" ;
            p_qc:leg_5 = "4  Bad data" ;
            p_qc:leg_6 = "5  Value changed" ;
            p_qc:leg_7 = "8  Interpolated data" ;
            p_qc:leg_8 = "9  Missing data" ;
        char t_qc(profile, depth, string1) ;
            t_qc:long_name = "Temperature Quality Flag" ;
            t_qc:missing_value = "9" ;
            t_qc:_FillValue = " " ;
            t_qc:var_desc = "Sea temperature quality flag, Argo reference table 2" ;
            t_qc:leg_1 = "0  No QC performed" ;
            t_qc:leg_2 = "1  Good data" ;
            t_qc:leg_3 = "2  Probably good data" ;
            t_qc:leg_4 = "3  Bad data which is potentially recoverable" ;
            t_qc:leg_5 = "4  Bad data" ;
            t_qc:leg_6 = "5  Value changed" ;
            t_qc:leg_7 = "8  Interpolated data" ;
            t_qc:leg_8 = "9  Missing data" ;
        char s_qc(profile, depth, string1) ;
            s_qc:long_name = "Salinity Quality Flag" ;
            s_qc:missing_value = "9" ;
            s_qc:_FillValue = " " ;
            s_qc:var_desc = "Sea salinity quality flag, Argo reference table 2" ;
            s_qc:leg_1 = "0  No QC performed" ;
            s_qc:leg_2 = "1  Good data" ;
            s_qc:leg_3 = "2  Probably good data" ;
            s_qc:leg_4 = "3  Bad data which is potentially recoverable" ;
            s_qc:leg_5 = "4  Bad data" ;
            s_qc:leg_6 = "5  Value changed" ;
            s_qc:leg_7 = "8  Interpolated data" ;
            s_qc:leg_8 = "9  Missing data" ;
        double p_calibrate(profile, depth) ;
            p_calibrate:long_name = "Calibrated Sea Pressure" ;
            p_calibrate:units = "decibar" ;
            p_calibrate:valid_range = 0., 12000. ;
            p_calibrate:data_min = 99999. ;
            p_calibrate:data_max = 99999. ;
            p_calibrate:missing_value = 99999. ;
            p_calibrate:_FillValue = 99999. ;
            p_calibrate:precision = 0.1 ;
            p_calibrate:var_desc = "Calibrated sea pressure" ;
        double t_calibrate(profile, depth) ;
            t_calibrate:long_name = "Calibrated Temperature" ;
            t_calibrate:units = "degree_Celsius" ;
            t_calibrate:valid_range = -2., 40. ;
            t_calibrate:data_min = 99999. ;
            t_calibrate:data_max = 99999. ;
            t_calibrate:missing_value = 99999. ;
            t_calibrate:_FillValue = 99999. ;
            t_calibrate:resolution = 0.001 ;
            t_calibrate:var_desc = "Calibrated temperature" ;
        double s_calibrate(profile, depth) ;
            s_calibrate:long_name = "Calibrated Salinity" ;
            s_calibrate:units = "psu" ;
            s_calibrate:valid_range = 0., 42. ;
            s_calibrate:data_min = 99999. ;
            s_calibrate:data_max = 99999. ;
            s_calibrate:missing_value = 99999. ;
            s_calibrate:_FillValue = 99999. ;
            s_calibrate:resolution = 0.001 ;
            s_calibrate:var_desc = "Calibrated salinity" ;
        char p_calibrate_qc(profile, depth, string1) ;
            p_calibrate_qc:long_name = "Calibrated Pressure Quality Flag" ;
            p_calibrate_qc:missing_value = "9" ;
            p_calibrate_qc:_FillValue = " " ;
            p_calibrate_qc:var_desc = "Calibrated pressure quality flag" ;
            p_calibrate_qc:leg_1 = "0  No QC performed" ;
            p_calibrate_qc:leg_2 = "1  Good data" ;
            p_calibrate_qc:leg_3 = "2  Probably good data" ;
            p_calibrate_qc:leg_4 = "3  Bad data which is potentially recoverable" ;
            p_calibrate_qc:leg_5 = "4  Bad data" ;
            p_calibrate_qc:leg_6 = "5  Value changed" ;
            p_calibrate_qc:leg_7 = "8  Interpolated data" ;
            p_calibrate_qc:leg_8 = "9  Missing data" ;
        char t_calibrate_qc(profile, depth, string1) ;
            t_calibrate_qc:long_name = "Calibrated Temperature Quality Flag" ;
            t_calibrate_qc:missing_value = "9" ;
            t_calibrate_qc:_FillValue = " " ;
            t_calibrate_qc:var_desc = "Calibrated temperature quality flag" ;
            t_calibrate_qc:leg_1 = "0  No QC performed" ;
            t_calibrate_qc:leg_2 = "1  Good data" ;
            t_calibrate_qc:leg_3 = "2  Probably good data" ;
            t_calibrate_qc:leg_4 = "3  Bad data which is potentially recoverable" ;
            t_calibrate_qc:leg_5 = "4  Bad data" ;
            t_calibrate_qc:leg_6 = "5  Value changed" ;
            t_calibrate_qc:leg_7 = "8  Interpolated data" ;
            t_calibrate_qc:leg_8 = "9  Missing data" ;
        char s_calibrate_qc(profile, depth, string1) ;
            s_calibrate_qc:long_name = "Calibrated Salinity Quality Flag" ;
            s_calibrate_qc:missing_value = "9" ;
            s_calibrate_qc:_FillValue = " " ;
            s_calibrate_qc:var_desc = "Calibrated salinity quality flag" ;
            s_calibrate_qc:leg_1 = "0  No QC performed" ;
            s_calibrate_qc:leg_2 = "1  Good data" ;
            s_calibrate_qc:leg_3 = "2  Probably good data" ;
            s_calibrate_qc:leg_4 = "3  Bad data which is potentially recoverable" ;
            s_calibrate_qc:leg_5 = "4  Bad data" ;
            s_calibrate_qc:leg_6 = "5  Value changed" ;
            s_calibrate_qc:leg_7 = "8  Interpolated data" ;
            s_calibrate_qc:leg_8 = "9  Missing data" ;
    
    // global attributes:
            :title = "ARGO-CSIRO dataset" ;
            :date_start = "12-Feb-1999" ;
            :date_end = "18-Jun-2001" ;
            :description = "Data is translated from csiromat ARGO  ftp: ftp.marine.csiro.au/pub/argo/csiromat/" ;
            :original_file = "R13352.mat" ;
            :date_creation = "11-May-2006" ;
            :author = "Paola Petrelli" ;
            :institution = "TPAC - University of Tasmania" ;
            :history = "" ;
    }
    
    
    
    
    ###############################################################################
    rectilinear/ACCfronts_nc4.nc
    
    
    
    netcdf ACCfronts_nc4 {
    dimensions:
        lon = 1081 ;
        lat = 363 ;
        time = 854 ;
    variables:
        float lon(lon) ;
            lon:units = "degrees_east" ;
            lon:long_name = "longitude" ;
        float lat(lat) ;
            lat:units = "degrees_north" ;
            lat:long_name = "latitude" ;
        float month(time) ;
            month:long_name = "month" ;
        float year(time) ;
            year:long_name = "year" ;
        float day(time) ;
            day:long_name = "day" ;
            day:units = "central time of +/- 10-15 day window" ;
        float front(time, lat, lon) ;
            front:units = "valid range from 0 to 12" ;
            front:long_name = "frontal indices" ;
            front:description = "Indices:   0 - south of sBdy;  1 - between SACCF-S & sBdy;  2 - SACCF-N & SACCF-S;  3 - PF-S & SACCF-N;  4 - PF-M & PF-S;  5 - PF-N & PF-M;  6 - SAF-S & PF-N;  7 - SAF-M & SAF-S;  8 - SAF-N & SAF-M;  9 - SAZ-S & SAF-N; 10 - SAZ-M & SAZ-S; 11 - SAZ-N & SAZ-M; 12 - north of SAZ-N. " ;
    
    // global attributes:
            :Conventions = "none" ;
            :institution = "CSIRO Marine and Atmospheric Research" ;
            :title = "ACC frontal indices: ACC fronts are mapped using combined MSLA data; Sokolov & Rintoul, JGR, 2009.  " ;
            :description = "ACC fronts are mapped using local (estimated in  30-deg sectors) frontal labels. Navigation of the ACC jets around shallow bottom topography is also taken into account. For further details see Sokolov & Rintoul, JGR, 2009a,b.            " ;
            :history = "Generated on Tue Nov  3 10:49:18 EST 2009." ;
    }
    
    
    
    
    ###############################################################################
    rectilinear/CM2.1_regionmask.nc
    
    
    
    netcdf CM2.1_regionmask {
    dimensions:
        gridlon_t = 360 ;
        gridlat_t = 200 ;
        gridlon_c = 360 ;
        gridlat_c = 200 ;
    variables:
        float gridlon_t(gridlon_t) ;
            gridlon_t:long_name = "zonal" ;
            gridlon_t:units = "degree" ;
        float gridlat_t(gridlat_t) ;
            gridlat_t:long_name = "meridional" ;
            gridlat_t:units = "degree" ;
        float gridlon_c(gridlon_c) ;
            gridlon_c:long_name = "zonal" ;
            gridlon_c:units = "degree" ;
        float gridlat_c(gridlat_c) ;
            gridlat_c:long_name = "meridional" ;
            gridlat_c:units = "degree" ;
        float tmask(gridlat_t, gridlon_t) ;
            tmask:long_name = "tmask" ;
            tmask:units = "none" ;
        float umask(gridlat_c, gridlon_c) ;
            umask:long_name = "umask" ;
            umask:units = "none" ;
        float geolon_t(gridlat_t, gridlon_t) ;
            geolon_t:long_name = "geolon_t" ;
            geolon_t:units = "degree" ;
        float geolon_c(gridlat_c, gridlon_c) ;
            geolon_c:long_name = "geolon_c" ;
            geolon_c:units = "degree" ;
        float geolat_t(gridlat_t, gridlon_t) ;
            geolat_t:long_name = "geolat_t" ;
            geolat_t:units = "degree" ;
        float geolat_c(gridlat_c, gridlon_c) ;
            geolat_c:long_name = "geolat_c" ;
            geolat_c:units = "degree" ;
    
    // global attributes:
            :filename = "regionmask.nc" ;
            :MPP_IO_VERSION = "$Id: mpp_io.F90,v 6.5.6.1.2.1.2.1.2.1 2003/02/19 15:47:51 fms Exp $" ;
    }
    
    
    
    
    ###############################################################################
    rectilinear/readme_CM2.1regionmask.txt
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/rectilinear/
    readme_CM2.1regionmask.txt' had status 1
    
    
    
    
    ###############################################################################
    rectilinear/readme_rectlinear.txt
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/rectilinear/
    readme_rectlinear.txt' had status 1
    
    
    
    
    ###############################################################################
    rectilinear/test_3_.nc
    
    
    
    netcdf test_3_ {
    dimensions:
        time = UNLIMITED ; // (2 currently)
        bnds = 2 ;
        xt = 360 ;
        yt = 200 ;
    variables:
        double time(time) ;
            time:standard_name = "time" ;
            time:long_name = "time" ;
            time:bounds = "time_bnds" ;
            time:units = "days since 0001-01-01 00:00:00" ;
            time:calendar = "365_day" ;
            time:axis = "T" ;
        double time_bnds(time, bnds) ;
        float xt(xt) ;
            xt:standard_name = "longitude" ;
            xt:long_name = "longitude" ;
            xt:units = "degrees_E" ;
            xt:axis = "X" ;
        float yt(yt) ;
            yt:standard_name = "latitude" ;
            yt:long_name = "latitude" ;
            yt:units = "degrees_N" ;
            yt:axis = "Y" ;
        float SST(time, yt, xt) ;
            SST:long_name = "sea surface temperature" ;
            SST:units = "deg-C" ;
            SST:_FillValue = -1.e+34f ;
            SST:missing_value = -1.e+34f ;
            SST:cell_methods = "time: mean" ;
            SST:time_avg_info = "average_T1,average_T2,average_DT" ;
        double average_DT(time) ;
            average_DT:long_name = "Length of average period" ;
            average_DT:units = "days" ;
    
    // global attributes:
            :CDI = "Climate Data Interface version 1.9.1 (http://mpimet.mpg.de/cdi)" ;
            :Conventions = "CF-1.6" ;
            :history = "Fri Oct 19 13:55:32 2018: cdo -C seltimestep,1,2 /home/esp-shared-a/GlobalModels/CMIP5/OCEAN/Control/CM2.1/control-1860_CM2.1.sst.nc /dev/shm/test.nc\n",
                "Thu Jul 13 07:02:40 2017: ncrcat /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.0001-0100.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.0101-0200.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.0201-0300.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.0301-0400.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.0401-0500.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.0501-0600.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.0601-0700.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.0701-0800.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.0801-0900.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.0901-1000.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.1001-1100.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.1101-1200.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.1201-1300.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.1301-1400.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.1401-1500.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.1501-1600.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.1601-1700.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.1701-1800.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.1801-1900.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.1901-2000.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.2001-2100.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.2101-2200.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.2201-2300.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.2301-2400.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.2401-2500.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.2501-2600.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.2601-2700.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.2701-2800.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.2801-2900.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.2901-3000.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.3001-3100.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.3101-3200.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.3201-3300.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.3301-3400.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.3401-3500.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.3501-3600.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.3601-3700.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.3701-3800.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.3801-3900.SST.nc /archive/ccsp/ipcc_ar4/CM2.1U_Control-1860_D4/pp/ice/ts/annual/100yr/ice.3901-4000.SST.nc CM21_Control-1860_sst.nc" ;
            :filename = "ice.0001-0100.SST.nc" ;
            :title = "CM2.1U_Control-1860_D4" ;
            :comment = "FMS time averaging, version 3.0, precision=float" ;
            :nco_openmp_thread_number = 1 ;
            :CDO = "Climate Data Operators version 1.9.1 (http://mpimet.mpg.de/cdo)" ;
    }
    
    
    
    
    ###############################################################################
    SO-reproj/OR_ABI-L1b-RadC-M3C01_G16_s20190621802131_e20190621804504_c20190621804546.nc
    
    
    
    netcdf OR_ABI-L1b-RadC-M3C01_G16_s20190621802131_e20190621804504_c20190621804546 {
    dimensions:
        y = 3000 ;
        x = 5000 ;
        number_of_time_bounds = 2 ;
        band = 1 ;
        number_of_image_bounds = 2 ;
        num_star_looks = 24 ;
    variables:
        short Rad(y, x) ;
            Rad:_FillValue = 1023s ;
            Rad:long_name = "ABI L1b Radiances" ;
            Rad:standard_name = "toa_outgoing_radiance_per_unit_wavelength" ;
            Rad:_Unsigned = "true" ;
            Rad:sensor_band_bit_depth = 10b ;
            Rad:valid_range = 0s, 1022s ;
            Rad:scale_factor = 0.8121064f ;
            Rad:add_offset = -25.93665f ;
            Rad:units = "W m-2 sr-1 um-1" ;
            Rad:resolution = "y: 0.000028 rad x: 0.000028 rad" ;
            Rad:coordinates = "band_id band_wavelength t y x" ;
            Rad:grid_mapping = "goes_imager_projection" ;
            Rad:cell_methods = "t: point area: point" ;
            Rad:ancillary_variables = "DQF" ;
        byte DQF(y, x) ;
            DQF:_FillValue = -1b ;
            DQF:long_name = "ABI L1b Radiances data quality flags" ;
            DQF:standard_name = "status_flag" ;
            DQF:_Unsigned = "true" ;
            DQF:valid_range = 0b, 3b ;
            DQF:units = "1" ;
            DQF:coordinates = "band_id band_wavelength t y x" ;
            DQF:grid_mapping = "goes_imager_projection" ;
            DQF:cell_methods = "t: point area: point" ;
            DQF:flag_values = 0b, 1b, 2b, 3b ;
            DQF:flag_meanings = "good_pixel_qf conditionally_usable_pixel_qf out_of_range_pixel_qf no_value_pixel_qf" ;
            DQF:number_of_qf_values = 4b ;
            DQF:percent_good_pixel_qf = 0.9995786f ;
            DQF:percent_conditionally_usable_pixel_qf = 0.f ;
            DQF:percent_out_of_range_pixel_qf = 0.0004213f ;
            DQF:percent_no_value_pixel_qf = 0.f ;
        double t ;
            t:long_name = "J2000 epoch mid-point between the start and end image scan in seconds" ;
            t:standard_name = "time" ;
            t:units = "seconds since 2000-01-01 12:00:00" ;
            t:axis = "T" ;
            t:bounds = "time_bounds" ;
        short y(y) ;
            y:scale_factor = -2.8e-05f ;
            y:add_offset = 0.128226f ;
            y:units = "rad" ;
            y:axis = "Y" ;
            y:long_name = "GOES fixed grid projection y-coordinate" ;
            y:standard_name = "projection_y_coordinate" ;
        short x(x) ;
            x:scale_factor = 2.8e-05f ;
            x:add_offset = -0.101346f ;
            x:units = "rad" ;
            x:axis = "X" ;
            x:long_name = "GOES fixed grid projection x-coordinate" ;
            x:standard_name = "projection_x_coordinate" ;
        double time_bounds(number_of_time_bounds) ;
            time_bounds:long_name = "Scan start and end times in seconds since epoch (2000-01-01 12:00:00)" ;
        int goes_imager_projection ;
            goes_imager_projection:long_name = "GOES-R ABI fixed grid projection" ;
            goes_imager_projection:grid_mapping_name = "geostationary" ;
            goes_imager_projection:perspective_point_height = 35786023. ;
            goes_imager_projection:semi_major_axis = 6378137. ;
            goes_imager_projection:semi_minor_axis = 6356752.31414 ;
            goes_imager_projection:inverse_flattening = 298.2572221 ;
            goes_imager_projection:latitude_of_projection_origin = 0. ;
            goes_imager_projection:longitude_of_projection_origin = -75. ;
            goes_imager_projection:sweep_angle_axis = "x" ;
        float y_image ;
            y_image:long_name = "GOES-R fixed grid projection y-coordinate center of image" ;
            y_image:standard_name = "projection_y_coordinate" ;
            y_image:units = "rad" ;
            y_image:axis = "Y" ;
        float y_image_bounds(number_of_image_bounds) ;
            y_image_bounds:long_name = "GOES-R fixed grid projection y-coordinate north/south extent of image" ;
            y_image_bounds:units = "rad" ;
        float x_image ;
            x_image:long_name = "GOES-R fixed grid projection x-coordinate center of image" ;
            x_image:standard_name = "projection_x_coordinate" ;
            x_image:units = "rad" ;
            x_image:axis = "X" ;
        float x_image_bounds(number_of_image_bounds) ;
            x_image_bounds:long_name = "GOES-R fixed grid projection x-coordinate west/east extent of image" ;
            x_image_bounds:units = "rad" ;
        float nominal_satellite_subpoint_lat ;
            nominal_satellite_subpoint_lat:long_name = "nominal satellite subpoint latitude (platform latitude)" ;
            nominal_satellite_subpoint_lat:standard_name = "latitude" ;
            nominal_satellite_subpoint_lat:_FillValue = -999.f ;
            nominal_satellite_subpoint_lat:units = "degrees_north" ;
        float nominal_satellite_subpoint_lon ;
            nominal_satellite_subpoint_lon:long_name = "nominal satellite subpoint longitude (platform longitude)" ;
            nominal_satellite_subpoint_lon:standard_name = "longitude" ;
            nominal_satellite_subpoint_lon:_FillValue = -999.f ;
            nominal_satellite_subpoint_lon:units = "degrees_east" ;
        float nominal_satellite_height ;
            nominal_satellite_height:long_name = "nominal satellite height above GRS 80 ellipsoid (platform altitude)" ;
            nominal_satellite_height:standard_name = "height_above_reference_ellipsoid" ;
            nominal_satellite_height:_FillValue = -999.f ;
            nominal_satellite_height:units = "km" ;
        float geospatial_lat_lon_extent ;
            geospatial_lat_lon_extent:long_name = "geospatial latitude and longitude references" ;
            geospatial_lat_lon_extent:geospatial_westbound_longitude = -152.1093f ;
            geospatial_lat_lon_extent:geospatial_northbound_latitude = 56.76145f ;
            geospatial_lat_lon_extent:geospatial_eastbound_longitude = -52.94688f ;
            geospatial_lat_lon_extent:geospatial_southbound_latitude = 14.57134f ;
            geospatial_lat_lon_extent:geospatial_lat_center = 30.083f ;
            geospatial_lat_lon_extent:geospatial_lon_center = -87.09695f ;
            geospatial_lat_lon_extent:geospatial_lat_nadir = 0.f ;
            geospatial_lat_lon_extent:geospatial_lon_nadir = -75.f ;
            geospatial_lat_lon_extent:geospatial_lat_units = "degrees_north" ;
            geospatial_lat_lon_extent:geospatial_lon_units = "degrees_east" ;
        byte yaw_flip_flag ;
            yaw_flip_flag:long_name = "Flag indicating the spacecraft is operating in yaw flip configuration" ;
            yaw_flip_flag:_Unsigned = "true" ;
            yaw_flip_flag:_FillValue = -1b ;
            yaw_flip_flag:valid_range = 0b, 1b ;
            yaw_flip_flag:units = "1" ;
            yaw_flip_flag:coordinates = "t" ;
            yaw_flip_flag:flag_values = 0b, 1b ;
            yaw_flip_flag:flag_meanings = "false true" ;
        byte band_id(band) ;
            band_id:long_name = "ABI band number" ;
            band_id:standard_name = "sensor_band_identifier" ;
            band_id:units = "1" ;
        float band_wavelength(band) ;
            band_wavelength:long_name = "ABI band central wavelength" ;
            band_wavelength:standard_name = "sensor_band_central_radiation_wavelength" ;
            band_wavelength:units = "um" ;
        float esun ;
            esun:long_name = "bandpass-weighted solar irradiance at the mean Earth-Sun distance" ;
            esun:standard_name = "toa_shortwave_irradiance_per_unit_wavelength" ;
            esun:_FillValue = -999.f ;
            esun:units = "W m-2 um-1" ;
            esun:coordinates = "band_id band_wavelength t" ;
            esun:cell_methods = "t: mean" ;
        float kappa0 ;
            kappa0:long_name = "Inverse of the incoming top of atmosphere radiance at current earth-sun distance (PI d2 esun-1)-1, where d is the ratio of instantaneous Earth-Sun distance divided by the mean Earth-Sun distance, esun is the bandpass-weighted solar irradiance and PI is a standard constant used to convert ABI L1b radiance to reflectance" ;
            kappa0:_FillValue = -999.f ;
            kappa0:units = "(W m-2 um-1)-1" ;
            kappa0:coordinates = "band_id band_wavelength t" ;
            kappa0:cell_methods = "t: mean" ;
        float planck_fk1 ;
            planck_fk1:long_name = "wavenumber-dependent coefficient (2 h c2/ nu3) used in the ABI emissive band monochromatic brightness temperature computation, where nu =central wavenumber and h and c are standard constants" ;
            planck_fk1:_FillValue = -999.f ;
            planck_fk1:units = "W m-1" ;
            planck_fk1:coordinates = "band_id band_wavelength" ;
        float planck_fk2 ;
            planck_fk2:long_name = "wavenumber-dependent coefficient (h c nu/b) used in the ABI emissive band monochromatic brightness temperature computation, where nu = central wavenumber and h, c, and b are standard constants" ;
            planck_fk2:_FillValue = -999.f ;
            planck_fk2:units = "K" ;
            planck_fk2:coordinates = "band_id band_wavelength" ;
        float planck_bc1 ;
            planck_bc1:long_name = "spectral bandpass correction offset for brightness temperature (B(nu) - bc_1)/bc_2 where B()=planck_function() and nu=wavenumber" ;
            planck_bc1:_FillValue = -999.f ;
            planck_bc1:units = "K" ;
            planck_bc1:coordinates = "band_id band_wavelength" ;
        float planck_bc2 ;
            planck_bc2:long_name = "spectral bandpass correction scale factor for brightness temperature (B(nu) - bc_1)/bc_2 where B()=planck_function() and nu=wavenumber" ;
            planck_bc2:_FillValue = -999.f ;
            planck_bc2:units = "1" ;
            planck_bc2:coordinates = "band_id band_wavelength" ;
        int valid_pixel_count ;
            valid_pixel_count:long_name = "number of good and conditionally usable pixels" ;
            valid_pixel_count:_FillValue = -1 ;
            valid_pixel_count:units = "count" ;
            valid_pixel_count:coordinates = "band_id band_wavelength t y_image x_image" ;
            valid_pixel_count:grid_mapping = "goes_imager_projection" ;
            valid_pixel_count:cell_methods = "t: sum area: sum (interval: 0.000028 rad comment: good and conditionally usable quality pixels only)" ;
        int missing_pixel_count ;
            missing_pixel_count:long_name = "number of missing pixels" ;
            missing_pixel_count:_FillValue = -1 ;
            missing_pixel_count:units = "count" ;
            missing_pixel_count:coordinates = "band_id band_wavelength t y_image x_image" ;
            missing_pixel_count:grid_mapping = "goes_imager_projection" ;
            missing_pixel_count:cell_methods = "t: sum area: sum (interval: 0.000028 rad comment: missing ABI fixed grid pixels only)" ;
        int saturated_pixel_count ;
            saturated_pixel_count:long_name = "number of saturated pixels" ;
            saturated_pixel_count:_FillValue = -1 ;
            saturated_pixel_count:units = "count" ;
            saturated_pixel_count:coordinates = "band_id band_wavelength t y_image x_image" ;
            saturated_pixel_count:grid_mapping = "goes_imager_projection" ;
            saturated_pixel_count:cell_methods = "t: sum area: sum (interval: 0.000028 rad comment: radiometrically saturated geolocated/not missing pixels only)" ;
        int undersaturated_pixel_count ;
            undersaturated_pixel_count:long_name = "number of undersaturated pixels" ;
            undersaturated_pixel_count:_FillValue = -1 ;
            undersaturated_pixel_count:units = "count" ;
            undersaturated_pixel_count:coordinates = "band_id band_wavelength t y_image x_image" ;
            undersaturated_pixel_count:grid_mapping = "goes_imager_projection" ;
            undersaturated_pixel_count:cell_methods = "t: sum area: sum (interval: 0.000028 rad comment: radiometrically undersaturated geolocated/not missing pixels only)" ;
        float min_radiance_value_of_valid_pixels ;
            min_radiance_value_of_valid_pixels:long_name = "minimum radiance value of pixels" ;
            min_radiance_value_of_valid_pixels:standard_name = "toa_outgoing_radiance_per_unit_wavelength" ;
            min_radiance_value_of_valid_pixels:_FillValue = -999.f ;
            min_radiance_value_of_valid_pixels:valid_range = -25.93665f, 804.0361f ;
            min_radiance_value_of_valid_pixels:units = "W m-2 sr-1 um-1" ;
            min_radiance_value_of_valid_pixels:coordinates = "band_id band_wavelength t y_image x_image" ;
            min_radiance_value_of_valid_pixels:grid_mapping = "goes_imager_projection" ;
            min_radiance_value_of_valid_pixels:cell_methods = "t: sum area: minimum (interval: 0.000028 rad comment: good and conditionally usable quality pixels only)" ;
        float max_radiance_value_of_valid_pixels ;
            max_radiance_value_of_valid_pixels:long_name = "maximum radiance value of pixels" ;
            max_radiance_value_of_valid_pixels:standard_name = "toa_outgoing_radiance_per_unit_wavelength" ;
            max_radiance_value_of_valid_pixels:_FillValue = -999.f ;
            max_radiance_value_of_valid_pixels:valid_range = -25.93665f, 804.0361f ;
            max_radiance_value_of_valid_pixels:units = "W m-2 sr-1 um-1" ;
            max_radiance_value_of_valid_pixels:coordinates = "band_id band_wavelength t y_image x_image" ;
            max_radiance_value_of_valid_pixels:grid_mapping = "goes_imager_projection" ;
            max_radiance_value_of_valid_pixels:cell_methods = "t: sum area: maximum (interval: 0.000028 rad comment: good and conditionally usable quality pixels only)" ;
        float mean_radiance_value_of_valid_pixels ;
            mean_radiance_value_of_valid_pixels:long_name = "mean radiance value of pixels" ;
            mean_radiance_value_of_valid_pixels:standard_name = "toa_outgoing_radiance_per_unit_wavelength" ;
            mean_radiance_value_of_valid_pixels:_FillValue = -999.f ;
            mean_radiance_value_of_valid_pixels:valid_range = -25.93665f, 804.0361f ;
            mean_radiance_value_of_valid_pixels:units = "W m-2 sr-1 um-1" ;
            mean_radiance_value_of_valid_pixels:coordinates = "band_id band_wavelength t y_image x_image" ;
            mean_radiance_value_of_valid_pixels:grid_mapping = "goes_imager_projection" ;
            mean_radiance_value_of_valid_pixels:cell_methods = "t: sum area: mean (interval: 0.000028 rad comment: good and conditionally usable quality pixels only)" ;
        float std_dev_radiance_value_of_valid_pixels ;
            std_dev_radiance_value_of_valid_pixels:long_name = "standard deviation of radiance values of pixels" ;
            std_dev_radiance_value_of_valid_pixels:standard_name = "toa_outgoing_radiance_per_unit_wavelength" ;
            std_dev_radiance_value_of_valid_pixels:_FillValue = -999.f ;
            std_dev_radiance_value_of_valid_pixels:units = "W m-2 sr-1 um-1" ;
            std_dev_radiance_value_of_valid_pixels:coordinates = "band_id band_wavelength t y_image x_image" ;
            std_dev_radiance_value_of_valid_pixels:grid_mapping = "goes_imager_projection" ;
            std_dev_radiance_value_of_valid_pixels:cell_methods = "t: sum area: standard_deviation (interval: 0.000028 rad comment: good and conditionally usable quality pixels only)" ;
        float percent_uncorrectable_L0_errors ;
            percent_uncorrectable_L0_errors:long_name = "percent data lost due to uncorrectable L0 errors" ;
            percent_uncorrectable_L0_errors:_FillValue = -999.f ;
            percent_uncorrectable_L0_errors:valid_range = 0.f, 1.f ;
            percent_uncorrectable_L0_errors:units = "percent" ;
            percent_uncorrectable_L0_errors:coordinates = "t y_image x_image" ;
            percent_uncorrectable_L0_errors:grid_mapping = "goes_imager_projection" ;
            percent_uncorrectable_L0_errors:cell_methods = "t: sum area: sum (uncorrectable L0 errors only)" ;
        float earth_sun_distance_anomaly_in_AU ;
            earth_sun_distance_anomaly_in_AU:long_name = "earth sun distance anomaly in astronomical units" ;
            earth_sun_distance_anomaly_in_AU:_FillValue = -999.f ;
            earth_sun_distance_anomaly_in_AU:units = "ua" ;
            earth_sun_distance_anomaly_in_AU:coordinates = "t" ;
            earth_sun_distance_anomaly_in_AU:cell_methods = "t: mean" ;
        int algorithm_dynamic_input_data_container ;
            algorithm_dynamic_input_data_container:long_name = "container for filenames of dynamic algorithm input data" ;
            algorithm_dynamic_input_data_container:input_ABI_L0_data = "OR_ABI-L0-C-M3_G16_s20190621802131_e20190621804504_c*.nc" ;
        int processing_parm_version_container ;
            processing_parm_version_container:long_name = "container for processing parameter filenames" ;
            processing_parm_version_container:L1b_processing_parm_version = "OR-PARM-RAD_G16_v01r00.zip" ;
        int algorithm_product_version_container ;
            algorithm_product_version_container:long_name = "container for algorithm package filename and product version" ;
            algorithm_product_version_container:algorithm_version = "OR_ABI-L1b-ALG-RAD_v01r00.zip" ;
            algorithm_product_version_container:product_version = "v01r00" ;
        double t_star_look(num_star_looks) ;
            t_star_look:long_name = "J2000 epoch time of star observed in seconds" ;
            t_star_look:standard_name = "time" ;
            t_star_look:units = "seconds since 2000-01-01 12:00:00" ;
            t_star_look:axis = "T" ;
        float band_wavelength_star_look(num_star_looks) ;
            band_wavelength_star_look:long_name = "ABI band central wavelength associated with observed star" ;
            band_wavelength_star_look:standard_name = "sensor_band_central_radiation_wavelength" ;
            band_wavelength_star_look:units = "um" ;
        short star_id(num_star_looks) ;
            star_id:long_name = "ABI star catalog identifier associated with observed star" ;
            star_id:_Unsigned = "true" ;
            star_id:_FillValue = -1s ;
            star_id:coordinates = "band_id band_wavelength_star_look t_star_look" ;
    
    // global attributes:
            :naming_authority = "gov.nesdis.noaa" ;
            :Conventions = "CF-1.7" ;
            :Metadata_Conventions = "Unidata Dataset Discovery v1.0" ;
            :standard_name_vocabulary = "CF Standard Name Table (v35, 20 July 2016)" ;
            :institution = "DOC/NOAA/NESDIS > U.S. Department of Commerce, National Oceanic and Atmospheric Administration, National Environmental Satellite, Data, and Information Services" ;
            :project = "GOES" ;
            :production_site = "WCDAS" ;
            :production_environment = "OE" ;
            :spatial_resolution = "1km at nadir" ;
            :orbital_slot = "GOES-East" ;
            :platform_ID = "G16" ;
            :instrument_type = "GOES R Series Advanced Baseline Imager" ;
            :scene_id = "CONUS" ;
            :instrument_ID = "FM1" ;
            :title = "ABI L1b Radiances" ;
            :summary = "Single reflective band ABI L1b Radiance Products are digital maps of outgoing radiance values at the top of the atmosphere for visible and near-IR bands." ;
            :keywords = "SPECTRAL/ENGINEERING > VISIBLE WAVELENGTHS > VISIBLE RADIANCE" ;
            :keywords_vocabulary = "NASA Global Change Master Directory (GCMD) Earth Science Keywords, Version 7.0.0.0.0" ;
            :iso_series_metadata_id = "a70be540-c38b-11e0-962b-0800200c9a66" ;
            :license = "Unclassified data.  Access is restricted to approved users only." ;
            :processing_level = "National Aeronautics and Space Administration (NASA) L1b" ;
            :cdm_data_type = "Image" ;
            :dataset_name = "OR_ABI-L1b-RadC-M3C01_G16_s20190621802131_e20190621804504_c20190621804546.nc" ;
            :production_data_source = "Realtime" ;
            :timeline_id = "ABI Mode 3" ;
            :date_created = "2019-03-03T18:04:54.6Z" ;
            :time_coverage_start = "2019-03-03T18:02:13.1Z" ;
            :time_coverage_end = "2019-03-03T18:04:50.4Z" ;
            :id = "4a42da74-0ae8-43ea-896d-6d3e4fb85975" ;
    }
    
    
    
    
    ###############################################################################
    SO-reproj/SO-reproj.R
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/SO-reproj/SO-reproj.R' had
    status 1
    
    
    
    
    ###############################################################################
    ssh05d19921006.nc
    
    
    
    netcdf ssh05d19921006 {
    dimensions:
        time = 1 ;
        depth = 1 ;
        latitude = 360 ;
        longitude = 720 ;
    variables:
        int woce_date(time) ;
            woce_date:long_name = "WOCE date" ;
            woce_date:units = "yyyymmdd" ;
            woce_date:F_format = "I8" ;
            woce_date:start_date = 19921002 ;
            woce_date:end_date = 19921011 ;
            woce_date:time_interval = "ten days" ;
        float woce_time_of_day(time) ;
            woce_time_of_day:long_name = "WOCE time convention as hhmmss.dd" ;
            woce_time_of_day:units = "Universal Time Coordinate" ;
            woce_time_of_day:F_format = "F9.2" ;
            woce_time_of_day:start_time = 0.f ;
            woce_time_of_day:end_time = 235959.f ;
        short julian_day_1990(time) ;
            julian_day_1990:long_name = "Julian day equivalent of WOCE date, set to 1 for 1990-01-01" ;
            julian_day_1990:units = "dddd" ;
            julian_day_1990:F_format = "I4" ;
            julian_day_1990:start_date = 1006s ;
            julian_day_1990:end_date = 1015s ;
            julian_day_1990:time_interval = "ten days" ;
        float depth(time) ;
            depth:long_name = "depth" ;
            depth:units = "meters" ;
            depth:F_format = "F3.0" ;
            depth:valid_min = 0.f ;
            depth:valid_max = 0.f ;
        float latitude(latitude) ;
            latitude:long_name = "latitude" ;
            latitude:units = "degrees_north" ;
            latitude:spatial_resolution = "0.5 degree" ;
            latitude:F_format = "F6.2" ;
            latitude:valid_min = -89.75f ;
            latitude:valid_max = 89.75f ;
        float longitude(longitude) ;
            longitude:long_name = "longitude" ;
            longitude:units = "degrees_east" ;
            longitude:spatial_resolution = "0.5 degree" ;
            longitude:F_format = "F6.2" ;
            longitude:valid_min = 0.25f ;
            longitude:valid_max = 359.75f ;
        short sea_level(latitude, longitude) ;
            sea_level:long_name = "sea_level" ;
            sea_level:zero_level = "1993-1996 time mean" ;
            sea_level:units = "millimeters" ;
            sea_level:instrument = "TOPEX/POSEIDON altimeters" ;
            sea_level:F_format = "I5" ;
            sea_level:valid_min = -1500s ;
            sea_level:valid_max = 1500s ;
            sea_level:fill_value = 32767s ;
            sea_level:land_value = 32766s ;
        byte bin_count(latitude, longitude) ;
            bin_count:long_name = "number of data points per bin" ;
            bin_count:F_format = "I2" ;
            bin_count:valid_min = 0b ;
            bin_count:valid_max = 33b ;
    
    // global attributes:
            :title = "TOPEX/POSEIDON SEA LEVEL" ;
            :spatial_resolution = "0.5 degree" ;
            :temporal_resolution = "Ten Day Average" ;
            :version = "WOCE CD-ROM V2.00-MGDRB" ;
            :creation_date = "Wed Jul  5 13:51:06 2000" ;
            :originating_center = "NASA JPL PO.DAAC" ;
    }
    
    
    
    
    ###############################################################################
    swapped/3A-DAY.nc
    
    
    
    netcdf \3A-DAY {
    dimensions:
        AD = 2 ;
        chn = 2 ;
        nlon = 1440 ;
        nlat = 536 ;
    variables:
        float precipRateNearSurfMean(AD, chn, nlon, nlat) ;
            precipRateNearSurfMean:DimensionNames = "AD,chn,nlon,nlat" ;
            precipRateNearSurfMean:Units = "mm/hr" ;
            precipRateNearSurfMean:units = "mm/hr" ;
            precipRateNearSurfMean:CodeMissingValue = "-9999.9" ;
            precipRateNearSurfMean:origname = "precipRateNearSurfMean" ;
            precipRateNearSurfMean:fullnamepath = "/GRID/precipRateNearSurfMean" ;
            precipRateNearSurfMean:_FillValue = -9999.9f ;
        int AD(AD) ;
            AD:comment = "Ascending or descending half of the orbit." ;
            AD:units = "level" ;
        int chn(chn) ;
            chn:comment = "Number of channels:Ku,Ka,KaHS,DPR." ;
            chn:units = "level" ;
        float nlat(nlat) ;
            nlat:units = "degrees_north" ;
        float nlon(nlon) ;
            nlon:units = "degrees_east" ;
    
    // global attributes:
            :FileHeader = "DOI=10.5067/GPM/DPR/3A-DAY/05;\n",
                "DOIauthority=http://dx.doi/org/;\n",
                "DOIshortName=3DPRD;\n",
                "AlgorithmID=3DPRD;\n",
                "AlgorithmVersion=V2.20170410;\n",
                "FileName=3A-DAY.GPM.DPR.V2-20170410.20180915-S000000-E235959.258.V05B.HDF5;\n",
                "SatelliteName=GPM;\n",
                "InstrumentName=DPR;\n",
                "GenerationDateTime=2018-09-17T08:43:57.000Z;\n",
                "StartGranuleDateTime=2018-09-15T00:00:00.000Z;\n",
                "StopGranuleDateTime=2018-09-15T23:59:59.999Z;\n",
                "GranuleNumber=;\n",
                "NumberOfSwaths=0;\n",
                "NumberOfGrids=1;\n",
                "GranuleStart=;\n",
                "TimeInterval=DAY;\n",
                "ProcessingSystem=PPS;\n",
                "ProductVersion=V05B;\n",
                "EmptyGranule=NOT_EMPTY;\n",
                "MissingData=;\n",
                "" ;
            :FileInfo = "DataFormatVersion=ch;\n",
                "TKCodeBuildVersion=1;\n",
                "MetadataVersion=ch;\n",
                "FormatPackage=HDF5-1.8.9;\n",
                "BlueprintFilename=GPM.V1.3DPRD.blueprint.xml;\n",
                "BlueprintVersion=BV_53;\n",
                "TKIOVersion=3.80.26;\n",
                "MetadataStyle=PVL;\n",
                "EndianType=LITTLE_ENDIAN;\n",
                "" ;
            :JAXAInfo = "GranuleFirstScanUTCDateTime=;\n",
                "GranuleLastScanUTCDateTime=;\n",
                "TotalQualityCode=Good;\n",
                "FirstScanLat=;\n",
                "FirstScanLon=;\n",
                "LastScanLat=;\n",
                "LastScanLon=;\n",
                "NumberOfRainPixelsNS=;\n",
                "NumberOfRainPixelsMS=;\n",
                "NumberOfRainPixelsHS=;\n",
                "ProcessingSubSystem=;\n",
                "ProcessingMode=;\n",
                "LightSpeed=;\n",
                "DielectricConstantKa=;\n",
                "DielectricConstantKu=;\n",
                "" ;
            :GRID.GridHeader = "BinMethod=ARITHMETIC_MEAN;\n",
                "Registration=CENTER;\n",
                "LatitudeResolution=0.25;\n",
                "LongitudeResolution=0.25;\n",
                "NorthBoundingCoordinate=67;\n",
                "SouthBoundingCoordinate=-67;\n",
                "EastBoundingCoordinate=180;\n",
                "WestBoundingCoordinate=-180;\n",
                "Origin=SOUTHWEST;\n",
                "" ;
            :GRID.fullnamepath = "/GRID" ;
            :history = "2018-10-11 12:37:07 GMT Hyrax-1.13.4 https://gpm1.gesdisc.eosdis.nasa.gov:443/opendap/GPM_L3/GPM_3DPRD.05/2018/09/3A-DAY.GPM.DPR.V2-20170410.20180915-S000000-E235959.258.V05B.HDF5.nc?precipRateNearSurfMean,AD,chn,nlon,nlat" ;
    }
    
    
    
    
    ###############################################################################
    swapped/gdal-dev-readme.txt
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/swapped/gdal-dev-
    readme.txt' had status 1
    
    
    
    
    ###############################################################################
    test.nc_60/num60.R
    Warning in system(sprintf("ncdump -h %s", file.path("extdata",
    files[i])), : running command 'ncdump -h extdata/test.nc_60/num60.R' had
    status 1
    
    
    
    
    ###############################################################################
    test.nc_60/test.nc
    
    
    
    netcdf test {
    dimensions:
        time = UNLIMITED ; // (1 currently)
        bnds = 2 ;
        x = 424 ;
        y = 412 ;
    variables:
        double time(time) ;
            time:standard_name = "time" ;
            time:bounds = "time_bnds" ;
            time:units = "days since 1949-12-01 00:00:00" ;
            time:calendar = "proleptic_gregorian" ;
            time:axis = "T" ;
        double time_bnds(time, bnds) ;
        double lon(y, x) ;
            lon:standard_name = "longitude" ;
            lon:long_name = "longitude" ;
            lon:units = "degrees_east" ;
            lon:_CoordinateAxisType = "Lon" ;
        double lat(y, x) ;
            lat:standard_name = "latitude" ;
            lat:long_name = "latitude" ;
            lat:units = "degrees_north" ;
            lat:_CoordinateAxisType = "Lat" ;
        float pr(time, y, x) ;
            pr:standard_name = "precipitation_flux" ;
            pr:long_name = "Precipitation" ;
            pr:units = "kg m-2 s-1" ;
            pr:coordinates = "lat lon" ;
            pr:_FillValue = 1.e+20f ;
            pr:missing_value = 1.e+20f ;
            pr:cell_methods = "time: mean" ;
    
    // global attributes:
            :CDI = "Climate Data Interface version 1.9.1 (http://mpimet.mpg.de/cdi)" ;
            :history = "Wed Oct 03 11:53:06 2018: cdo -C seltimestep,1 /home/netapp-clima-scratch/fraffael/SPI/EC-EARTH_HIRHAM5/prOK_mon_2071-2098.nc /dev/shm/test.nc\n",
                "Mon Oct 01 18:02:40 2018: cdo mulc,86400 pr_mon_2071-2098.nc prOK_mon_2071-2098.nc\n",
                "Mon Oct 01 12:24:12 2018: cdo selyear,2071/2098 pr_mon_2071-2100.nc pr_mon_2071-2098.nc\n",
                "Mon Oct  1 12:23:45 2018: ncrcat /home/esp-shared-a/RegionalModels/CORDEX/EUR-11/rcp85/MM/EC-EARTH_HIRHAM5/pr_EUR-11_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_207101-208012.nc /home/esp-shared-a/RegionalModels/CORDEX/EUR-11/rcp85/MM/EC-EARTH_HIRHAM5/pr_EUR-11_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_208101-209012.nc /home/esp-shared-a/RegionalModels/CORDEX/EUR-11/rcp85/MM/EC-EARTH_HIRHAM5/pr_EUR-11_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_209101-210012.nc pr_mon_2071-2100.nc\n",
                "Mon Nov 18 04:53:38 2013: /usr/local/bin/ncks --mk_rec_dmn time pr_EUR-11_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_207101-208012.nc out1.nc\n",
                "Fri Dec 07 08:23:08 2012: cdo setday,16 NAM-44/DMI/DMI-ECEARTH/rcp85/r3i1p1/DMI-HIRHAM5/v1/mon/tas/tas_NAM-44_DMI-ECEARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_207101-208012.nc NAM-44/DMI/DMI-ECEARTH/rcp85/r3i1p1/DMI-HIRHAM5/v1/mon/tas/tas_NAM-44_DMI-ECEARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_207101-208012_sub.nc\n",
                "Fri Dec 07 08:23:07 2012: cdo monmean NAM-44/DMI/DMI-ECEARTH/rcp85/r3i1p1/DMI-HIRHAM5/v1/mon/tas/tas_NAM-44_DMI-ECEARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_20710101-20801231.nc NAM-44/DMI/DMI-ECEARTH/rcp85/r3i1p1/DMI-HIRHAM5/v1/mon/tas/tas_NAM-44_DMI-ECEARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_207101-208012.nc\n",
                "Fri Dec 07 08:22:56 2012: cdo mergetime NAM-44/DMI/DMI-ECEARTH/rcp85/r3i1p1/DMI-HIRHAM5/v1/day/tas/tas_NAM-44_DMI-ECEARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_day_20710101-20751231.nc NAM-44/DMI/DMI-ECEARTH/rcp85/r3i1p1/DMI-HIRHAM5/v1/day/tas/tas_NAM-44_DMI-ECEARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_day_20760101-20801231.nc NAM-44/DMI/DMI-ECEARTH/rcp85/r3i1p1/DMI-HIRHAM5/v1/mon/tas/tas_NAM-44_DMI-ECEARTH_rcp85_r3i1p1_DMI-HIRHAM5_v1_mon_20710101-20801231.nc" ;
            :institution = "Danish Meteorological Institute" ;
            :Conventions = "CF-1.6" ;
            :tracking_id = "e9cc9b3b-9755-400b-b101-49c24b811781" ;
            :contact = "obc@dmi.dk" ;
            :creation_date = "2012-12-03 03:14:15" ;
            :driving_model_ensemble_member = "r3i1p1" ;
            :institute_id = "DMI" ;
            :model_id = "DMI-HIRHAM5" ;
            :rcm_version_id = "v1" ;
            :project_id = "CORDEX" ;
            :product = "output" ;
            :frequency = "mon" ;
            :NCO = "\"4.6.4\"" ;
            :experiment = "Scenario run using ECEARTH as driving model" ;
            :experiment_id = "rcp85" ;
            :driving_experiment_name = "rcp85" ;
            :CORDEX_domain = "EUR-11" ;
            :driving_experiment = "ICHEC-EC-EARTH,rcp85,r3i1p1" ;
            :driving_model_id = "ICHEC-EC-EARTH" ;
            :nco_openmp_thread_number = 1 ;
            :CDO = "Climate Data Operators version 1.9.1 (http://mpimet.mpg.de/cdo)" ;
    }
    
    
    
    
    ###############################################################################
    timeseries.nc
    
    
    
    netcdf timeseries {
    dimensions:
        station = 10 ;
        time = 20 ;
    variables:
        int num(station) ;
            num:long_name = "Station number" ;
            num:cf_role = "timeseries_id" ;
        int time(time) ;
            time:units = "days since 1970-01-01 00:00:00 UTC" ;
            time:long_name = "time" ;
            time:calendar = "gregorian" ;
        float pr(station, time) ;
            pr:units = "kg m-2 s-1" ;
            pr:_FillValue = -10.f ;
            pr:long_name = "Total precipitation flux" ;
            pr:coordinates = "lat lon alt num" ;
            pr:standard_name = "precipitation_flux" ;
        float lat(station) ;
            lat:units = "degrees_north" ;
            lat:long_name = "Station latitude" ;
            lat:standard_name = "latitude" ;
        float lon(station) ;
            lon:units = "degrees_east" ;
            lon:long_name = "Station longitude" ;
            lon:standard_name = "longitude" ;
        float alt(station) ;
            alt:units = "m" ;
            alt:long_name = "Vertical distance above the surface" ;
            alt:standard_name = "height" ;
    
    // global attributes:
            :featureType = "timeSeries" ;
            :Conventions = "CF-1.7" ;
    }
    
    
    
    
    ###############################################################################
    tricky_grids/OR_ABI-L1b-RadC-M3C01_G16_s20190621802131_e20190621804504_c20190621804546.nc
    
    
    
    netcdf OR_ABI-L1b-RadC-M3C01_G16_s20190621802131_e20190621804504_c20190621804546 {
    dimensions:
        y = 3000 ;
        x = 5000 ;
        number_of_time_bounds = 2 ;
        band = 1 ;
        number_of_image_bounds = 2 ;
        num_star_looks = 24 ;
    variables:
        short Rad(y, x) ;
            Rad:_FillValue = 1023s ;
            Rad:long_name = "ABI L1b Radiances" ;
            Rad:standard_name = "toa_outgoing_radiance_per_unit_wavelength" ;
            Rad:_Unsigned = "true" ;
            Rad:sensor_band_bit_depth = 10b ;
            Rad:valid_range = 0s, 1022s ;
            Rad:scale_factor = 0.8121064f ;
            Rad:add_offset = -25.93665f ;
            Rad:units = "W m-2 sr-1 um-1" ;
            Rad:resolution = "y: 0.000028 rad x: 0.000028 rad" ;
            Rad:coordinates = "band_id band_wavelength t y x" ;
            Rad:grid_mapping = "goes_imager_projection" ;
            Rad:cell_methods = "t: point area: point" ;
            Rad:ancillary_variables = "DQF" ;
        byte DQF(y, x) ;
            DQF:_FillValue = -1b ;
            DQF:long_name = "ABI L1b Radiances data quality flags" ;
            DQF:standard_name = "status_flag" ;
            DQF:_Unsigned = "true" ;
            DQF:valid_range = 0b, 3b ;
            DQF:units = "1" ;
            DQF:coordinates = "band_id band_wavelength t y x" ;
            DQF:grid_mapping = "goes_imager_projection" ;
            DQF:cell_methods = "t: point area: point" ;
            DQF:flag_values = 0b, 1b, 2b, 3b ;
            DQF:flag_meanings = "good_pixel_qf conditionally_usable_pixel_qf out_of_range_pixel_qf no_value_pixel_qf" ;
            DQF:number_of_qf_values = 4b ;
            DQF:percent_good_pixel_qf = 0.9995786f ;
            DQF:percent_conditionally_usable_pixel_qf = 0.f ;
            DQF:percent_out_of_range_pixel_qf = 0.0004213f ;
            DQF:percent_no_value_pixel_qf = 0.f ;
        double t ;
            t:long_name = "J2000 epoch mid-point between the start and end image scan in seconds" ;
            t:standard_name = "time" ;
            t:units = "seconds since 2000-01-01 12:00:00" ;
            t:axis = "T" ;
            t:bounds = "time_bounds" ;
        short y(y) ;
            y:scale_factor = -2.8e-05f ;
            y:add_offset = 0.128226f ;
            y:units = "rad" ;
            y:axis = "Y" ;
            y:long_name = "GOES fixed grid projection y-coordinate" ;
            y:standard_name = "projection_y_coordinate" ;
        short x(x) ;
            x:scale_factor = 2.8e-05f ;
            x:add_offset = -0.101346f ;
            x:units = "rad" ;
            x:axis = "X" ;
            x:long_name = "GOES fixed grid projection x-coordinate" ;
            x:standard_name = "projection_x_coordinate" ;
        double time_bounds(number_of_time_bounds) ;
            time_bounds:long_name = "Scan start and end times in seconds since epoch (2000-01-01 12:00:00)" ;
        int goes_imager_projection ;
            goes_imager_projection:long_name = "GOES-R ABI fixed grid projection" ;
            goes_imager_projection:grid_mapping_name = "geostationary" ;
            goes_imager_projection:perspective_point_height = 35786023. ;
            goes_imager_projection:semi_major_axis = 6378137. ;
            goes_imager_projection:semi_minor_axis = 6356752.31414 ;
            goes_imager_projection:inverse_flattening = 298.2572221 ;
            goes_imager_projection:latitude_of_projection_origin = 0. ;
            goes_imager_projection:longitude_of_projection_origin = -75. ;
            goes_imager_projection:sweep_angle_axis = "x" ;
        float y_image ;
            y_image:long_name = "GOES-R fixed grid projection y-coordinate center of image" ;
            y_image:standard_name = "projection_y_coordinate" ;
            y_image:units = "rad" ;
            y_image:axis = "Y" ;
        float y_image_bounds(number_of_image_bounds) ;
            y_image_bounds:long_name = "GOES-R fixed grid projection y-coordinate north/south extent of image" ;
            y_image_bounds:units = "rad" ;
        float x_image ;
            x_image:long_name = "GOES-R fixed grid projection x-coordinate center of image" ;
            x_image:standard_name = "projection_x_coordinate" ;
            x_image:units = "rad" ;
            x_image:axis = "X" ;
        float x_image_bounds(number_of_image_bounds) ;
            x_image_bounds:long_name = "GOES-R fixed grid projection x-coordinate west/east extent of image" ;
            x_image_bounds:units = "rad" ;
        float nominal_satellite_subpoint_lat ;
            nominal_satellite_subpoint_lat:long_name = "nominal satellite subpoint latitude (platform latitude)" ;
            nominal_satellite_subpoint_lat:standard_name = "latitude" ;
            nominal_satellite_subpoint_lat:_FillValue = -999.f ;
            nominal_satellite_subpoint_lat:units = "degrees_north" ;
        float nominal_satellite_subpoint_lon ;
            nominal_satellite_subpoint_lon:long_name = "nominal satellite subpoint longitude (platform longitude)" ;
            nominal_satellite_subpoint_lon:standard_name = "longitude" ;
            nominal_satellite_subpoint_lon:_FillValue = -999.f ;
            nominal_satellite_subpoint_lon:units = "degrees_east" ;
        float nominal_satellite_height ;
            nominal_satellite_height:long_name = "nominal satellite height above GRS 80 ellipsoid (platform altitude)" ;
            nominal_satellite_height:standard_name = "height_above_reference_ellipsoid" ;
            nominal_satellite_height:_FillValue = -999.f ;
            nominal_satellite_height:units = "km" ;
        float geospatial_lat_lon_extent ;
            geospatial_lat_lon_extent:long_name = "geospatial latitude and longitude references" ;
            geospatial_lat_lon_extent:geospatial_westbound_longitude = -152.1093f ;
            geospatial_lat_lon_extent:geospatial_northbound_latitude = 56.76145f ;
            geospatial_lat_lon_extent:geospatial_eastbound_longitude = -52.94688f ;
            geospatial_lat_lon_extent:geospatial_southbound_latitude = 14.57134f ;
            geospatial_lat_lon_extent:geospatial_lat_center = 30.083f ;
            geospatial_lat_lon_extent:geospatial_lon_center = -87.09695f ;
            geospatial_lat_lon_extent:geospatial_lat_nadir = 0.f ;
            geospatial_lat_lon_extent:geospatial_lon_nadir = -75.f ;
            geospatial_lat_lon_extent:geospatial_lat_units = "degrees_north" ;
            geospatial_lat_lon_extent:geospatial_lon_units = "degrees_east" ;
        byte yaw_flip_flag ;
            yaw_flip_flag:long_name = "Flag indicating the spacecraft is operating in yaw flip configuration" ;
            yaw_flip_flag:_Unsigned = "true" ;
            yaw_flip_flag:_FillValue = -1b ;
            yaw_flip_flag:valid_range = 0b, 1b ;
            yaw_flip_flag:units = "1" ;
            yaw_flip_flag:coordinates = "t" ;
            yaw_flip_flag:flag_values = 0b, 1b ;
            yaw_flip_flag:flag_meanings = "false true" ;
        byte band_id(band) ;
            band_id:long_name = "ABI band number" ;
            band_id:standard_name = "sensor_band_identifier" ;
            band_id:units = "1" ;
        float band_wavelength(band) ;
            band_wavelength:long_name = "ABI band central wavelength" ;
            band_wavelength:standard_name = "sensor_band_central_radiation_wavelength" ;
            band_wavelength:units = "um" ;
        float esun ;
            esun:long_name = "bandpass-weighted solar irradiance at the mean Earth-Sun distance" ;
            esun:standard_name = "toa_shortwave_irradiance_per_unit_wavelength" ;
            esun:_FillValue = -999.f ;
            esun:units = "W m-2 um-1" ;
            esun:coordinates = "band_id band_wavelength t" ;
            esun:cell_methods = "t: mean" ;
        float kappa0 ;
            kappa0:long_name = "Inverse of the incoming top of atmosphere radiance at current earth-sun distance (PI d2 esun-1)-1, where d is the ratio of instantaneous Earth-Sun distance divided by the mean Earth-Sun distance, esun is the bandpass-weighted solar irradiance and PI is a standard constant used to convert ABI L1b radiance to reflectance" ;
            kappa0:_FillValue = -999.f ;
            kappa0:units = "(W m-2 um-1)-1" ;
            kappa0:coordinates = "band_id band_wavelength t" ;
            kappa0:cell_methods = "t: mean" ;
        float planck_fk1 ;
            planck_fk1:long_name = "wavenumber-dependent coefficient (2 h c2/ nu3) used in the ABI emissive band monochromatic brightness temperature computation, where nu =central wavenumber and h and c are standard constants" ;
            planck_fk1:_FillValue = -999.f ;
            planck_fk1:units = "W m-1" ;
            planck_fk1:coordinates = "band_id band_wavelength" ;
        float planck_fk2 ;
            planck_fk2:long_name = "wavenumber-dependent coefficient (h c nu/b) used in the ABI emissive band monochromatic brightness temperature computation, where nu = central wavenumber and h, c, and b are standard constants" ;
            planck_fk2:_FillValue = -999.f ;
            planck_fk2:units = "K" ;
            planck_fk2:coordinates = "band_id band_wavelength" ;
        float planck_bc1 ;
            planck_bc1:long_name = "spectral bandpass correction offset for brightness temperature (B(nu) - bc_1)/bc_2 where B()=planck_function() and nu=wavenumber" ;
            planck_bc1:_FillValue = -999.f ;
            planck_bc1:units = "K" ;
            planck_bc1:coordinates = "band_id band_wavelength" ;
        float planck_bc2 ;
            planck_bc2:long_name = "spectral bandpass correction scale factor for brightness temperature (B(nu) - bc_1)/bc_2 where B()=planck_function() and nu=wavenumber" ;
            planck_bc2:_FillValue = -999.f ;
            planck_bc2:units = "1" ;
            planck_bc2:coordinates = "band_id band_wavelength" ;
        int valid_pixel_count ;
            valid_pixel_count:long_name = "number of good and conditionally usable pixels" ;
            valid_pixel_count:_FillValue = -1 ;
            valid_pixel_count:units = "count" ;
            valid_pixel_count:coordinates = "band_id band_wavelength t y_image x_image" ;
            valid_pixel_count:grid_mapping = "goes_imager_projection" ;
            valid_pixel_count:cell_methods = "t: sum area: sum (interval: 0.000028 rad comment: good and conditionally usable quality pixels only)" ;
        int missing_pixel_count ;
            missing_pixel_count:long_name = "number of missing pixels" ;
            missing_pixel_count:_FillValue = -1 ;
            missing_pixel_count:units = "count" ;
            missing_pixel_count:coordinates = "band_id band_wavelength t y_image x_image" ;
            missing_pixel_count:grid_mapping = "goes_imager_projection" ;
            missing_pixel_count:cell_methods = "t: sum area: sum (interval: 0.000028 rad comment: missing ABI fixed grid pixels only)" ;
        int saturated_pixel_count ;
            saturated_pixel_count:long_name = "number of saturated pixels" ;
            saturated_pixel_count:_FillValue = -1 ;
            saturated_pixel_count:units = "count" ;
            saturated_pixel_count:coordinates = "band_id band_wavelength t y_image x_image" ;
            saturated_pixel_count:grid_mapping = "goes_imager_projection" ;
            saturated_pixel_count:cell_methods = "t: sum area: sum (interval: 0.000028 rad comment: radiometrically saturated geolocated/not missing pixels only)" ;
        int undersaturated_pixel_count ;
            undersaturated_pixel_count:long_name = "number of undersaturated pixels" ;
            undersaturated_pixel_count:_FillValue = -1 ;
            undersaturated_pixel_count:units = "count" ;
            undersaturated_pixel_count:coordinates = "band_id band_wavelength t y_image x_image" ;
            undersaturated_pixel_count:grid_mapping = "goes_imager_projection" ;
            undersaturated_pixel_count:cell_methods = "t: sum area: sum (interval: 0.000028 rad comment: radiometrically undersaturated geolocated/not missing pixels only)" ;
        float min_radiance_value_of_valid_pixels ;
            min_radiance_value_of_valid_pixels:long_name = "minimum radiance value of pixels" ;
            min_radiance_value_of_valid_pixels:standard_name = "toa_outgoing_radiance_per_unit_wavelength" ;
            min_radiance_value_of_valid_pixels:_FillValue = -999.f ;
            min_radiance_value_of_valid_pixels:valid_range = -25.93665f, 804.0361f ;
            min_radiance_value_of_valid_pixels:units = "W m-2 sr-1 um-1" ;
            min_radiance_value_of_valid_pixels:coordinates = "band_id band_wavelength t y_image x_image" ;
            min_radiance_value_of_valid_pixels:grid_mapping = "goes_imager_projection" ;
            min_radiance_value_of_valid_pixels:cell_methods = "t: sum area: minimum (interval: 0.000028 rad comment: good and conditionally usable quality pixels only)" ;
        float max_radiance_value_of_valid_pixels ;
            max_radiance_value_of_valid_pixels:long_name = "maximum radiance value of pixels" ;
            max_radiance_value_of_valid_pixels:standard_name = "toa_outgoing_radiance_per_unit_wavelength" ;
            max_radiance_value_of_valid_pixels:_FillValue = -999.f ;
            max_radiance_value_of_valid_pixels:valid_range = -25.93665f, 804.0361f ;
            max_radiance_value_of_valid_pixels:units = "W m-2 sr-1 um-1" ;
            max_radiance_value_of_valid_pixels:coordinates = "band_id band_wavelength t y_image x_image" ;
            max_radiance_value_of_valid_pixels:grid_mapping = "goes_imager_projection" ;
            max_radiance_value_of_valid_pixels:cell_methods = "t: sum area: maximum (interval: 0.000028 rad comment: good and conditionally usable quality pixels only)" ;
        float mean_radiance_value_of_valid_pixels ;
            mean_radiance_value_of_valid_pixels:long_name = "mean radiance value of pixels" ;
            mean_radiance_value_of_valid_pixels:standard_name = "toa_outgoing_radiance_per_unit_wavelength" ;
            mean_radiance_value_of_valid_pixels:_FillValue = -999.f ;
            mean_radiance_value_of_valid_pixels:valid_range = -25.93665f, 804.0361f ;
            mean_radiance_value_of_valid_pixels:units = "W m-2 sr-1 um-1" ;
            mean_radiance_value_of_valid_pixels:coordinates = "band_id band_wavelength t y_image x_image" ;
            mean_radiance_value_of_valid_pixels:grid_mapping = "goes_imager_projection" ;
            mean_radiance_value_of_valid_pixels:cell_methods = "t: sum area: mean (interval: 0.000028 rad comment: good and conditionally usable quality pixels only)" ;
        float std_dev_radiance_value_of_valid_pixels ;
            std_dev_radiance_value_of_valid_pixels:long_name = "standard deviation of radiance values of pixels" ;
            std_dev_radiance_value_of_valid_pixels:standard_name = "toa_outgoing_radiance_per_unit_wavelength" ;
            std_dev_radiance_value_of_valid_pixels:_FillValue = -999.f ;
            std_dev_radiance_value_of_valid_pixels:units = "W m-2 sr-1 um-1" ;
            std_dev_radiance_value_of_valid_pixels:coordinates = "band_id band_wavelength t y_image x_image" ;
            std_dev_radiance_value_of_valid_pixels:grid_mapping = "goes_imager_projection" ;
            std_dev_radiance_value_of_valid_pixels:cell_methods = "t: sum area: standard_deviation (interval: 0.000028 rad comment: good and conditionally usable quality pixels only)" ;
        float percent_uncorrectable_L0_errors ;
            percent_uncorrectable_L0_errors:long_name = "percent data lost due to uncorrectable L0 errors" ;
            percent_uncorrectable_L0_errors:_FillValue = -999.f ;
            percent_uncorrectable_L0_errors:valid_range = 0.f, 1.f ;
            percent_uncorrectable_L0_errors:units = "percent" ;
            percent_uncorrectable_L0_errors:coordinates = "t y_image x_image" ;
            percent_uncorrectable_L0_errors:grid_mapping = "goes_imager_projection" ;
            percent_uncorrectable_L0_errors:cell_methods = "t: sum area: sum (uncorrectable L0 errors only)" ;
        float earth_sun_distance_anomaly_in_AU ;
            earth_sun_distance_anomaly_in_AU:long_name = "earth sun distance anomaly in astronomical units" ;
            earth_sun_distance_anomaly_in_AU:_FillValue = -999.f ;
            earth_sun_distance_anomaly_in_AU:units = "ua" ;
            earth_sun_distance_anomaly_in_AU:coordinates = "t" ;
            earth_sun_distance_anomaly_in_AU:cell_methods = "t: mean" ;
        int algorithm_dynamic_input_data_container ;
            algorithm_dynamic_input_data_container:long_name = "container for filenames of dynamic algorithm input data" ;
            algorithm_dynamic_input_data_container:input_ABI_L0_data = "OR_ABI-L0-C-M3_G16_s20190621802131_e20190621804504_c*.nc" ;
        int processing_parm_version_container ;
            processing_parm_version_container:long_name = "container for processing parameter filenames" ;
            processing_parm_version_container:L1b_processing_parm_version = "OR-PARM-RAD_G16_v01r00.zip" ;
        int algorithm_product_version_container ;
            algorithm_product_version_container:long_name = "container for algorithm package filename and product version" ;
            algorithm_product_version_container:algorithm_version = "OR_ABI-L1b-ALG-RAD_v01r00.zip" ;
            algorithm_product_version_container:product_version = "v01r00" ;
        double t_star_look(num_star_looks) ;
            t_star_look:long_name = "J2000 epoch time of star observed in seconds" ;
            t_star_look:standard_name = "time" ;
            t_star_look:units = "seconds since 2000-01-01 12:00:00" ;
            t_star_look:axis = "T" ;
        float band_wavelength_star_look(num_star_looks) ;
            band_wavelength_star_look:long_name = "ABI band central wavelength associated with observed star" ;
            band_wavelength_star_look:standard_name = "sensor_band_central_radiation_wavelength" ;
            band_wavelength_star_look:units = "um" ;
        short star_id(num_star_looks) ;
            star_id:long_name = "ABI star catalog identifier associated with observed star" ;
            star_id:_Unsigned = "true" ;
            star_id:_FillValue = -1s ;
            star_id:coordinates = "band_id band_wavelength_star_look t_star_look" ;
    
    // global attributes:
            :naming_authority = "gov.nesdis.noaa" ;
            :Conventions = "CF-1.7" ;
            :Metadata_Conventions = "Unidata Dataset Discovery v1.0" ;
            :standard_name_vocabulary = "CF Standard Name Table (v35, 20 July 2016)" ;
            :institution = "DOC/NOAA/NESDIS > U.S. Department of Commerce, National Oceanic and Atmospheric Administration, National Environmental Satellite, Data, and Information Services" ;
            :project = "GOES" ;
            :production_site = "WCDAS" ;
            :production_environment = "OE" ;
            :spatial_resolution = "1km at nadir" ;
            :orbital_slot = "GOES-East" ;
            :platform_ID = "G16" ;
            :instrument_type = "GOES R Series Advanced Baseline Imager" ;
            :scene_id = "CONUS" ;
            :instrument_ID = "FM1" ;
            :title = "ABI L1b Radiances" ;
            :summary = "Single reflective band ABI L1b Radiance Products are digital maps of outgoing radiance values at the top of the atmosphere for visible and near-IR bands." ;
            :keywords = "SPECTRAL/ENGINEERING > VISIBLE WAVELENGTHS > VISIBLE RADIANCE" ;
            :keywords_vocabulary = "NASA Global Change Master Directory (GCMD) Earth Science Keywords, Version 7.0.0.0.0" ;
            :iso_series_metadata_id = "a70be540-c38b-11e0-962b-0800200c9a66" ;
            :license = "Unclassified data.  Access is restricted to approved users only." ;
            :processing_level = "National Aeronautics and Space Administration (NASA) L1b" ;
            :cdm_data_type = "Image" ;
            :dataset_name = "OR_ABI-L1b-RadC-M3C01_G16_s20190621802131_e20190621804504_c20190621804546.nc" ;
            :production_data_source = "Realtime" ;
            :timeline_id = "ABI Mode 3" ;
            :date_created = "2019-03-03T18:04:54.6Z" ;
            :time_coverage_start = "2019-03-03T18:02:13.1Z" ;
            :time_coverage_end = "2019-03-03T18:04:50.4Z" ;
            :id = "4a42da74-0ae8-43ea-896d-6d3e4fb85975" ;
    }
