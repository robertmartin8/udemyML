# Reading in data
library(arules)
ds = read.transactions('Market_Basket.csv', sep = ',', rm.duplicates = TRUE)

# Overview of the data
summary(ds)
itemFrequencyPlot(ds, topN = 50, cex = 0.7, main = paste("Most frequently purchased items"))

# Training apriori on the data
rules = eclat(ds, parameter = list(support = 0.004, minlen = 2 ))

# Visualising
inspect(sort(rules, decreasing = TRUE, by = 'support')[1:10])