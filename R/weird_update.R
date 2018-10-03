unlink("weird.tar.gz")
system("tar cvzf weird.tar.gz extdata")
library(piggyback)
pb_upload("weird.tar.gz", tag = "v0.0.2")
