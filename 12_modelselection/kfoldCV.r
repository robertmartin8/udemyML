
# Reading in Data
ds = read.csv('Social_Network_Ads.csv')
ds = ds[, 3:5]

# Scaling and splitting
library(caTools)
ds[,1:2] = scale(ds[,1:2])

split = sample.split(ds$Purchased, SplitRatio = 0.75)
train = subset(ds, split == TRUE)
test = subset(ds, split == FALSE)

#SVM
library(e1071)

# k-Fold Cross Validation

library(caret)
folds = createFolds(train$Purchased, k = 10)
cv = lapply(folds, function(x) {
    train_fold = train[-x, ]
    test_fold = train[x, ]
    
    clf = svm(Purchased ~ .,
              data = train,
              kernel = 'radial',
              type = 'C-classification')
    
    y_pred = predict(clf, type = 'response', newdata = test_fold)
    cm = table(test_fold[, 3], y_pred)
    acc = (cm[1,1] + cm[2,2])/sum(cm)
})

accuracy = mean(as.numeric(cv))

plot(clf, data = train)
