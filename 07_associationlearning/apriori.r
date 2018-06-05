# Reading in data
library(arules)
ds = read.transactions('Market_Basket.csv', sep = ',', rm.duplicates = TRUE)

# Overview of the data
summary(ds)
itemFrequencyPlot(ds, topN = 50, cex = 0.7, main = paste("Most frequently purchased items"))

# Training apriori on the data
rules = apriori(ds, parameter = list(supp = 0.005, conf = 0.1))

# Visualising

inspect(sort(rules, decreasing = TRUE, by = 'lift')[1:10])