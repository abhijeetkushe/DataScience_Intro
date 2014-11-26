setwd("~/POINT_SRC_CODE/datasci_course_materials")

#load train
train <- read.csv("~/POINT_SRC_CODE/datasci_course_materials/train.csv")

#load test
test <- read.csv("~/POINT_SRC_CODE/datasci_course_materials/test.csv")

#assign 0s to Survive column
test$Survived <- 0
test$Survived[test$Sex == 'female'] <- 1

submit <- data.frame(PassengerId = test$PassengerId, Survived = test$Survived)

write.csv(submit, file = "allMenperish.csv", row.names = FALSE)

train$Child <- 0

train$Child[train$Age < 18] <- 1

aggregate(Survived ~ Child + Sex, data=train, FUN=sum)

aggregate(Survived ~ Child + Sex, data=train, FUN=function(x) {sum(x)/length(x)})

train$Fare2 <- '30+'train$Fare2[train$Fare < 30 & train$Fare >= 20] <- '20-30'

train$Fare2[train$Fare < 20 & train$Fare >= 10] <- '10-20'

train$Fare2[train$Fare < 10] <- '<10'

aggregate(Survived ~ Fare2 + Pclass + Sex, data=train, FUN=function(x) {sum(x)/length(x)})

test$Survived <- 0

test$Survived[test$Sex == 'female'] <- 1

test$Survived[test$Sex == 'female' & test$Pclass == 3 & test$Fare >= 20] <- 0

submit <- data.frame(PassengerId = test$PassengerId, Survived = test$Survived)

write.csv(submit, file = "allThirdClassMenperish.csv", row.names = FALSE)

