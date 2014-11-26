setwd("~/POINT_SRC_CODE/datasci_course_materials")

#load train
train <- read.csv("~/POINT_SRC_CODE/datasci_course_materials/train.csv")

#load test
test <- read.csv("~/POINT_SRC_CODE/datasci_course_materials/test.csv")

test$Survived <- NA
combi <- rbind(train, test)

combi$Name <- as.character(combi$Name)

strsplit(combi$Name[1], split='[,.]')

strsplit(combi$Name[1], split='[,.]')[[1]]

combi$Title <- strsplit(combi$Name, split='[,.]')[[1]][2]
combi$Title <- sub(' ', '', combi$Title)
combi$Title[combi$Title %in% c('Mme', 'Mlle')] <- 'Mlle'
combi$Title[combi$Title %in% c('Capt', 'Don', 'Major', 'Sir')] <- 'Sir'
combi$Title <- factor(combi$Title)

combi$FamilySize <- combi$SibSp + combi$Parch + 1combi$Surname <- sapply(combi$Name, FUN=function(x) {strsplit(x, split='[,.]')[[1]][1]})

combi$FamilyID <- paste(as.character(combi$FamilySize), combi$Surname, sep="")

combi$FamilyID[combi$FamilySize <= 2] <- 'Small'

table(combi$FamilyID)

famIDs <- data.frame(table(combi$FamilyID))

famIDs <- famIDs[famIDs$Freq <= 2,]

combi$FamilyID[combi$FamilyID %in% famIDs$Var1] <- 'Small'

combi$FamilyID <- factor(combi$FamilyID)

train <- combi[1:891,]

test <- combi[892:1309,]

fit <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked + Title + FamilySize + FamilyID,
             data=train, method="class")

Prediction <- predict(fit, test, type = "class")
submit <- data.frame(PassengerId = test$PassengerId, Survived = Prediction)

plot(fit)
text(fit)

install.packages('rattle')
install.packages('rpart.plot')
install.packages('RColorBrewer')
library(rattle)
library(rpart.plot)
library(RColorBrewer)

Prediction <- predict(fit, test, type = "class")
write.csv(submit, file = "mysixthdtree.csv", row.names = FALSE)