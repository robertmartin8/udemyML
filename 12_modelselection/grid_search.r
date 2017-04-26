
# Reading in Data
ds = read.csv('Social_Network_Ads.csv')
ds = ds[, 3:5]

ds[,3] = as.factor(ds[,3])

# Scaling and splitting
library(caTools)
ds[,1:2] = scale(ds[,1:2])

split = sample.split(ds$Purchased, SplitRatio = 0.75)
train = subset(ds, split == TRUE)
test = subset(ds, split == FALSE)

#SVM
library(caret)

# k-Fold Cross Validation
clf = train(form = Purchased ~., data = train, method = 'svmRadial')
clf$bestTune
