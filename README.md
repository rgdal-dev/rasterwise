
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

    bad_examples_62/example1.nc
    bad_examples_62/example2.nc
    bad_examples_62/example3.nc
    dt_ref_global_merged_madt_uv_19921014_19921014_20060315.nc
    EURO-CORDEX_81_DOMAIN000_54/EURO-CORDEX_81_DOMAIN000.nc
    file.nc
    get1index_64/test.nc
    hmr_ita.nc
    nhsce_v01r01_19661004_20140203.nc
    oscar_gdr_5d1993.nc
    R13352.nc
    rectlinear/19911203.nc
    ssh05d19921006.nc
    swapped/3A-DAY.nc
    test.nc_60/test.nc
    timeseries.nc

## The ncdumps -h

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
    rectlinear/19911203.nc
    
    
    
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
