"""
Created on Tue Mar 21 19:50:08 2017

@author: Robert
"""
## Random forrest regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('seaborn-deep')

# Importing the dataset
ds = pd.read_csv('Position_Salaries.csv')
X = ds.iloc[:, -2:-1].values
y = ds.iloc[:, -1].values

# Fitting the Regression Model to the dataset
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators = 100, oob_score=True)
regressor.fit(X,y)

# Predicting a new result
y_pred = regressor.predict(6.5)


# Visualising the Regression results 
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y)
plt.plot(X_grid, regressor.predict(X_grid))
plt.title('Random forest salary progression')
plt.xlabel('Position')
plt.ylabel(list(ds)[-1])
plt.show()