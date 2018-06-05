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

clf = svm(Purchased ~ .,
          data = train,
          kernel = 'radial',
          type = 'C-classification')

y_pred = predict(clf, type = 'response', newdata = test[-3])
cm

# Confusion matrix
cm = table(test[, 3], y_pred)

plot(clf, data = train)
