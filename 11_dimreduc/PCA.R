ds = read.csv('Wine.csv')

library(caTools)
library(caret)
library(e1071)

# Scale and apply PCA.
pca = preProcess(ds[-14], method = c('scale', 'pca'), pcaComp=2)
ds = predict(pca, ds)
ds = ds[c(2,3,1)]

# Split the dataset
split = sample.split(ds$Customer_Segment, SplitRatio = 0.8)
train = subset(ds, split == TRUE)
test = subset(ds, split == FALSE)

# SVM classifier

clf = svm(Customer_Segment ~ .,
          data = train,
          kernel = 'radial',
          type = 'C-classification')

y_pred = predict(clf, type = 'response', newdata = test[-3])

# Confusion matrix
cm = table(test[, 3], y_pred)

plot(clf, data = train)


# Plotting
library('ElemStatLearn')
set = train
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('PC1', 'PC2')
prob_set = predict(clf, type = 'response', newdata = grid_set)
y_grid = prob_set
plot(set[, -3],
     main = 'SVM with PCA',
     xlab = 'PC1', ylab = 'PC2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 2, 'deepskyblue', ifelse(y_grid == 1, 'springgreen3', 'tomato')))
points(set, pch = 21, bg = ifelse(set[, 3] == 2, 'blue3', ifelse(set[, 3] == 1, 'green4', 'red3')))