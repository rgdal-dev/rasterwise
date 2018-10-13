unlink("weird.tar.gz")
system("tar cvzf weird.tar.gz extdata")
files <- list.files("extdata", recursive = TRUE, pattern = "nc$") ## not always an extension
writeLines(files, "weirdlist.txt")
library(piggyback)
pb_upload("weird.tar.gz", tag = "v0.0.7")
