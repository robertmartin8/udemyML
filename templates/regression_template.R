# Importing the dataset
dataset = read.csv('Data.csv')
dataset = dataset[1:2]

# Splitting the dataset into the Training set and Test set
library(caTools)
split = sample.split(dataset$Depvar, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
training_set = scale(training_set)
test_set = scale(test_set)


# Linear/polynomial regression
regressor = lm(formula = Depvar ~.,
             data = training_set)
regressor = lm(Depvar ~ poly(Level, 4),
              data = training_set)

# Support Vector Regression
library(e1071)
regressor = svm(formula = Depvar ~.,
                data = training_set,
                type = 'eps-regression')

# Decision Tree Regression
library(rpart)
regressor = rpart(formula = Depvar~.,
                  data = training_set,
                  rpart.control(minsplit = 2))


# Random Forest regression
install.packages("randomForest")
library(randomForest)
regressor = randomForest(x = dataset[1],
                         y = dataset$Depvar,
                         ntree = 100)

# Predicting a new result
y_pred = predict(regressor, data.frame(Indvar = 6.5))


# Visualising the result
x_grid = seq(min(dataset$Indvar), max(dataset$Indvar), 0.01)
ggplot() +
  geom_point(aes(x = dataset$Indvar, y = dataset$Depvar),
             colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Indvar = x_grid))),
            colour = 'blue') +
  ggtitle('Title') +
  xlab('x variable') +
  ylab('y variable')
