needed.packages <- c("readxl","data.table")
new.packages <- needed.packages[!(needed.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages)

lapply(needed.packages, library, character.only = TRUE)

xlsx.files <- list.files(pattern = ".xlsx")

data <- rbindlist(lapply(xlsx.files, read_excel))
data <- data[,c(2,7,8)]
colnames(data) <- c("company","email","contact.no")
data <- data[grepl(".*@.*\\..*",data$email),]
data <- data[!duplicated(data$email)]
write.csv(data, file = "people.csv", na = "")