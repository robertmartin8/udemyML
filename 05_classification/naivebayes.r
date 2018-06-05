
# Reading in Data
ds = read.csv('Social_Network_Ads.csv')
ds = ds[, 3:5]

# Scaling and splitting
library(caTools)
ds[,1:2] = scale(ds[,1:2])
ds$Purchased = factor(ds$Purchased, labels = c(0,1))

split = sample.split(ds$Purchased, SplitRatio = 0.75)
train = subset(ds, split == TRUE)
test = subset(ds, split == FALSE)

library(e1071)
clf = naiveBayes(x = train[-3], y = train$Purchased)
y_pred = predict(clf, newdata = test[-3])

# Confusion matrix
cm = table(test[, 3], y_pred)

# Plot
library('ElemStatLearn')
set = train
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
y_grid = predict(clf, newdata = grid_set)

plot(set[, -3],
     main = 'Naive Bayes',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))