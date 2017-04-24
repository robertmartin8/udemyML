ds = read.csv('Social_Network_Ads.csv')
ds = ds[, 3:5]

# Scaling and splitting
library(caTools)
ds[,1:2] = scale(ds[,1:2])

split = sample.split(ds$Purchased, SplitRatio = 0.75)
train = subset(ds, split == TRUE)
test = subset(ds, split == FALSE)

# Kernel PCA
library(kernlab)
kpca = kpca(~., data = train[-3], kernel = 'rbfdot', features = 2)
train_pca = as.data.frame(predict(kpca, train))
train_pca$Purchased = train$Purchased

test_pca = as.data.frame(predict(kpca, test))
test_pca$Purchased = test$Purchased


# Classifier
clf = glm(formula = Purchased ~ ., 
          data = train_pca,
          family = binomial)

prob_pred = predict(clf, type = 'response', newdata = test_pca[-3])
y_pred = ifelse(prob_pred >= 0.5, 1, 0)

cm = table(test_pca[, 3], y_pred)

# Plotting
library('ElemStatLearn')
set = train_pca
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('V1', 'V2')
prob_set = predict(clf, type = 'response', newdata = grid_set)
y_grid = ifelse(prob_set > 0.5, 1, 0)
plot(set[, -3],
     main = 'Kernel PCA',
     xlab = 'Pc1', ylab = 'PC2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))