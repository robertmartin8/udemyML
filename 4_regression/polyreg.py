"""
Created on Sat Mar 18 18:34:06 2017

@author: Robert
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')


ds = pd.read_csv('Position_Salaries.csv')
X = ds.iloc[:,1:2].values
y = ds.iloc[:, -1].values

# Linear regression
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X,y)

# Polynomial regression
from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(3)
X_poly = poly_reg.fit_transform(X)
regressor = LinearRegression()
regressor.fit(X_poly, y)

# So that we can see the complete prediction curve
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)

plt.scatter(X, y)
plt.plot(X_grid, regressor.predict(poly_reg.fit_transform(X_grid)))
plt.plot(X, lin_reg.predict(X))
plt.xlabel('Position')
plt.ylabel('Salary')
plt.title('Polynomial regression salary progression')
plt.show()

