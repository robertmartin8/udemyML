# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Salary_Data.csv')

# Splitting the dataset into the Training set and Test set
library(caTools)
split = sample.split(dataset, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Regressor
regressor = lm(Salary ~ YearsExperience, training_set)
y_pred = predict(regressor, newdata = test_set)

# Plot
# library(Cairo)
# Cairo(file="Cairo_PNG_96_dpi_adj.png", 
#       type="png",
#       units="in", 
#       width=15, 
#       height=12, 
#       pointsize=12*3, 
#       dpi=150)
#     
library(ggplot2)
ggplot() + 
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary vs Experience (training)') + 
  xlab('Years of experience') +
  ylab('Salary')

ggplot() + 
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary vs Experience (training)') + 
  xlab('Years of experience') +
  ylab('Salary')

# dev.off()