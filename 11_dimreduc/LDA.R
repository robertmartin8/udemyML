ds = read.csv('Wine.csv')

# Scale and split the dataset
library(caTools)
ds[-14] = scale(ds[-14])
split = sample.split(ds$Customer_Segment, SplitRatio = 0.8)
train = subset(ds, split == TRUE)
test = subset(ds, split == FALSE)

# Applying LDA
library(MASS)
lda = lda(Customer_Segment ~., data = train)
train = as.data.frame(predict(lda, train))
train = train[c(5,6,1)]

test = as.data.frame(predict(lda, test))
test = test[c(5,6,1)]

# SVM classifier
library(e1071)
clf = svm(class ~ .,
          data = train,
          kernel = 'radial',
          type = 'C-classification')

y_pred = predict(clf, newdata = test[-3])

# Confusion matrix
cm = table(test[, 3], y_pred)
plot(clf, data = train)


# Plotting
library('ElemStatLearn')
set = train
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('x.LD1', 'x.LD2')
prob_set = predict(clf, type = 'response', newdata = grid_set)
y_grid = prob_set
plot(set[, -3],
     main = 'SVM with LDA',
     xlab = 'LD1', ylab = 'LD2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 2, 'deepskyblue', ifelse(y_grid == 1, 'springgreen3', 'tomato')))
points(set, pch = 21, bg = ifelse(set[, 3] == 2, 'blue3', ifelse(set[, 3] == 1, 'green4', 'red3')))