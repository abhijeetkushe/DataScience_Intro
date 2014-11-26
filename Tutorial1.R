setwd("~/POINT_SRC_CODE/datasci_course_materials")

#load train
train <- read.csv("~/POINT_SRC_CODE/datasci_course_materials/train.csv")

#load test
test <- read.csv("~/POINT_SRC_CODE/datasci_course_materials/test.csv")

#fill Survived column in test
test$Survived <- rep(0, 418)

submit <- data.frame(PassengerId = test$PassengerId, Survived = test$Survived)

write.csv(submit, file = "theyallperish.csv", row.names = FALSE)