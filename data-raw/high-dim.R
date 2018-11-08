#https://www.unidata.ucar.edu/mailing_lists/archives/galeon/2005/msg00138.html
# https://trac.osgeo.org/gdal/ticket/2582


## https://trac.osgeo.org/gdal/ticket/2583
## R code to create 5D NetCDF file, MDSumner 2009-11-09
## mdsumner@utas.edu.au

## this example is provided to test the patch for #2583
## http://trac.osgeo.org/gdal/ticket/2583


## -------------------------------------------------------------------------
## Generate NetCDF file in R
## -------------------------------------------------------------------------


## load NetCDF package
## - can be installed easily on Windows with install.packages("RNetCDF")
library(RNetCDF)

## generate 4D data - 1:N
dims <- c(2, 3, 2, 2)
m <- array(data = 1:prod(dims), dim = dims)

## 5D array - m, m + const, m * const
a <- array(data = c(m, m + 0.1, m * 2), dim = c(2, 3, 2, 2, 3))

## check the data
range(m)  ##[1]  1 24
## apply range across 5th dimension
apply(a, MARGIN = 5, FUN = range)
##     [,1] [,2] [,3]
##[1,]    1  1.1    2
##[2,]   24 24.1   48

## create NetCDF file
nc <- create.nc("extdata/high-dim/test-1.nc")

## coordinate values for NetCDF (to test transform and band metadata)
x <- seq(0, 5, length = dim(a)[1])
y <- seq(0, 2, length = dim(a)[2])
c3 <- seq(0, 1, length = dim(a)[3])
c4 <- seq(0, 1, length = dim(a)[4])
c5 <- seq(0, 1, length = dim(a)[5])

## dimensions
dim.def.nc(nc, "x", length(x))
dim.def.nc(nc, "y", length(y))
dim.def.nc(nc, "c3", length(c3))
dim.def.nc(nc, "c4", length(c4))
dim.def.nc(nc, "c5", length(c5))

## variables
var.def.nc(nc, "a", "NC_DOUBLE", c(0, 1, 2, 3, 4))
var.def.nc(nc, "x", "NC_DOUBLE", 0)
var.def.nc(nc, "y", "NC_DOUBLE", 1)
var.def.nc(nc, "c3", "NC_DOUBLE", 2)
var.def.nc(nc, "c4", "NC_DOUBLE", 3)
var.def.nc(nc, "c5", "NC_DOUBLE", 4)


## write the data (all at once, no start/count)
var.put.nc(nc, "a", a)
var.put.nc(nc, "x", x)
var.put.nc(nc, "y", y)
var.put.nc(nc, "c3", c3)
var.put.nc(nc, "c4", c4)
var.put.nc(nc, "c5", c5)

## finish up
close.nc(nc)

## with the patch (notice how the band metadata changes for c4 correctly, but stays constant without the patch)

## system("C:/path/to/patchedGDAL/gdalinfo test-1.nc")

## Warning 1: No UNIDATA NC_GLOBAL:Conventions attribute
## Driver: netCDF/Network Common Data Format
## Files: test-1.nc
## Size is 2, 3
## Coordinate System is `'
## Origin = (-2.500000000000000,2.500000000000000)
## Pixel Size = (5.000000000000000,-1.000000000000000)
## Corner Coordinates:
## Upper Left  (  -2.5000000,   2.5000000)
## Lower Left  (  -2.5000000,  -0.5000000)
## Upper Right (   7.5000000,   2.5000000)
## Lower Right (   7.5000000,  -0.5000000)
## Center      (   2.5000000,   1.0000000)
## Band 1 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=0
## Band 2 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=1
## Band 3 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0
##     NETCDF_DIMENSION_c4=1
##     NETCDF_DIMENSION_c3=0
## Band 4 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0
##     NETCDF_DIMENSION_c4=1
##     NETCDF_DIMENSION_c3=1
## Band 5 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0.5
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=0
## Band 6 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0.5
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=1
## Band 7 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0.5
##     NETCDF_DIMENSION_c4=1
##     NETCDF_DIMENSION_c3=0
## Band 8 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0.5
##     NETCDF_DIMENSION_c4=1
##     NETCDF_DIMENSION_c3=1
## Band 9 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=1
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=0
## Band 10 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=1
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=1
## Band 11 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=1
##     NETCDF_DIMENSION_c4=1
##     NETCDF_DIMENSION_c3=0
## Band 12 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=1
##     NETCDF_DIMENSION_c4=1
##     NETCDF_DIMENSION_c3=1




## without the patch GDAL 1.7.0  dev, FWTools 2.4.3, released 2009/07/27
system("gdalinfo test-1.nc")
## Warning 1: No UNIDATA NC_GLOBAL:Conventions attribute
## Driver: netCDF/Network Common Data Format
## Files: test-1.nc
## Size is 2, 3
## Coordinate System is `'
## Origin = (-2.500000000000000,2.500000000000000)
## Pixel Size = (5.000000000000000,-1.000000000000000)
## Corner Coordinates:
## Upper Left  (  -2.5000000,   2.5000000)
## Lower Left  (  -2.5000000,  -0.5000000)
## Upper Right (   7.5000000,   2.5000000)
## Lower Right (   7.5000000,  -0.5000000)
## Center      (   2.5000000,   1.0000000)
## Band 1 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=0
## Band 2 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=1
## Band 3 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=0
## Band 4 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=0
## Band 5 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0.5
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=0
## Band 6 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0.5
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=1
## Band 7 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0.5
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=0
## Band 8 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=0.5
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=0
## Band 9 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=1
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=0
## Band 10 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=1
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=1
## Band 11 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=1
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=0
## Band 12 Block=2x1 Type=Float64, ColorInterp=Undefined
##   NoData Value=9.969209968386869e+036
##   Metadata:
##     NETCDF_VARNAME=a
##     NETCDF_DIMENSION_c5=1
##     NETCDF_DIMENSION_c4=0
##     NETCDF_DIMENSION_c3=0


