
# Reading in Data
ds = read.csv('Social_Network_Ads.csv')
ds = ds[, 3:5]

# Scaling and splitting
library(caTools)

split = sample.split(ds$Purchased, SplitRatio = 0.75)
train = subset(ds, split == TRUE)
test = subset(ds, split == FALSE)

# Regressor
library(rpart)
clf = rpart(formula = Purchased ~.,
            data = train)

prob_pred = predict(clf, newdata = test[-3])
y_pred = ifelse(prob_pred > 0.5, 1, 0)

# Confusion matrix
cm = table(test[, 3], y_pred)

plot(clf, margin = 0.05, main='Decision Tree')
text(clf, cex = 0.5)

# Plot
library('ElemStatLearn')
set = train
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
prob_set = predict(clf, newdata = grid_set)
y_grid = ifelse(prob_set > 0.5, 1, 0)

plot(set[, -3],
     main = 'Title',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))