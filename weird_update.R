unlink("weird.tar.gz")
system("tar cvzf weird.tar.gz extdata")
files <- list.files("extdata", recursive = TRUE) ## not always an extension
writeLines(files, "weirdlist.txt")
library(piggyback)

## HEY don't forget to change the version number listed in the readme!
## also, creating the tag and push the tarball seems to take two runs of this:
pb_upload("weird.tar.gz", tag = "v0.5.0")

## (or learn how to do this properly ...)
