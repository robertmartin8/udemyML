# Dataset
ds = read.csv('Data.csv')

# Missing Data
ds$Age = ifelse(is.na(ds$Age), 
                ave(ds$Age, FUN = function(x) mean(x, na.rm = TRUE)), 
                ds$Age)

ds$Salary = ifelse(
  is.na(ds$Salary),
  ave(ds$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
  ds$Salary
)

# Catgorical Data
ds$Country = factor(
  ds$Country,
  levels = c('France', 'Spain', 'Germany'),
  labels = c(1, 2, 3)
  )

ds$Purchased = factor(
  ds$Purchased,
  levels = c('No', 'Yes'),
  labels = c(0,1)
  )

# Training set and test set
library(caTools)
split = sample.split(ds$Purchased, SplitRatio = .8)
training_set = subset(ds, split == TRUE)
testing_set = subset(ds, split == FALSE)

# Feature scaling
training_set[, 2:3] = scale(training_set[, 2:3])
testing_set[, 2:3] = scale(testing_set[, 2:3])
