ds = read.csv("Position_Salaries.csv")
ds = ds[, 2:3]

# Fitting and predicting
lin_reg = lm(Salary ~.,
             data = ds)

poly_reg = lm(Salary ~ poly(Level, 4),
              data = ds)
y_pred = predict(poly_reg, data.frame(Level =6.5))

# Plotting
X_grid = seq(min(ds$Level), max(ds$Level), 0.1)

library(ggplot2)
ggplot() +
    geom_point(aes(x= ds$Level, y = ds$Salary), 
               colour = 'red') +
    geom_line(aes(x=ds$Level, y = predict(lin_reg, new_data = X_grid)),
              colour = 'blue') +
    geom_line(aes(x = X_grid, y = predict(poly_reg, newdata = data.frame(Level = X_grid))),
              colour = 'black') +
    ggtitle("Polynomial regression salary progression") +
    xlab("Position") +
    ylab("Salary")
