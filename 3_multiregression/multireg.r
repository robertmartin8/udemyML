ds = read.csv("50_Startups.csv")

# Splitting dataset
library(caTools)
split = sample.split(ds, SplitRatio = 0.8)
training_set = subset(ds, split == TRUE)
test_set = subset(ds, split == FALSE)

# Dealing with categorical values
ds$State = factor(ds$State,
                  levels = c("New York", "California", "Florida"),
                  labels = c(1,2,3))

# Fitting regression model and predicting 
regressor = lm(formula = Profit ~.,
               data = training_set)
summary(regressor)
y_pred = predict(regressor, newdata = test_set)

# Backwards elimination
regressor_optimum = lm(formula = Profit~.,
                       data = ds)
step(regressor_optimum, direction = "backward")

summary(regressor)$r.square
summary(regressor_optimum)$r.square