u <- "https://www.ecad.eu/download/ensembles/data/Grid_0.25deg_reg_ensemble/pp_ens_mean_0.25deg_reg_v19.0e.nc"
#dir.create("extdata/large-mem")
f <- file.path("extdata/large-mem", basename(u))
curl::curl_download(u, f)
