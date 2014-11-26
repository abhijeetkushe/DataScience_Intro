setwd("~/POINT_SRC_CODE/datasci_course_materials")

#load train
train <- read.csv("~/POINT_SRC_CODE/datasci_course_materials/train.csv")

#load test
test <- read.csv("~/POINT_SRC_CODE/datasci_course_materials/test.csv")

library(rpart)

fit <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked, data=train, method="class")

plot(fit)
text(fit)

install.packages('rattle')
install.packages('rpart.plot')
install.packages('RColorBrewer')
library(rattle)
library(rpart.plot)
library(RColorBrewer)

fancyRpartPlot(fit)

Prediction <- predict(fit, test, type = "class")

submit <- data.frame(PassengerId = test$PassengerId, Survived = Prediction)
write.csv(submit, file = "myfirstdtree.csv", row.names = FALSE)

fit <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked, data=train,
             method="class", control=rpart.control(minsplit=2, cp=0,maxdepth=6))

fancyRpartPlot(fit)

fit <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked, data=train,
             +              method="class", control=rpart.control(minsplit=4, cp=0.003,maxdepth=6,minbucket=2))
Prediction <- predict(fit, test, type = "class")
write.csv(submit, file = "myfifthdtree.csv", row.names = FALSE)