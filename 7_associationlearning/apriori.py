"""
Created on Sun Apr  2 20:41:48 2017

@author: Robert
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')


# Reading in data
ds = pd.read_csv('Market_Basket.csv', header = None)
ds = ds.values

# Creating the transactions list of lists
transactions = []

for i in range(ds.shape[0]):
    transactions.append([str(ds[i][j]) for j in range(ds.shape[1])])

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, 
                min_lift = 5, min_length = 2)

# Visualising the results
results = list(rules)