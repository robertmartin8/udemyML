"""
Created on Tue Mar 14 19:52:52 2017

@author: Robert
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.regression.linear_model as sm
from statsmodels.tools.tools import add_constant


# Dataset
ds = pd.read_csv('50_startups.csv')
X = ds.iloc[:, 0:4].values
y = ds.iloc[:, -1].values

# Exploratory analysis
import seaborn as sns
sns.set(style="ticks", color_codes=True)
g = sns.pairplot(ds, kind="reg")

# Categorical data
labelencoder_X = LabelEncoder()
X[:, -1] = labelencoder_X.fit_transform(X[:, -1])
onehotencoder = OneHotEncoder(categorical_features=[-1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]

# Train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# Backward elimination
X_opt = add_constant(X, prepend=True)
regressor_ols = sm.OLS(endog=y, exog=X_opt).fit()
initial_summary = regressor_ols.summary()
pvalues = regressor_ols.pvalues

while max(pvalues > 0.05):
    max_index = np.argmax(pvalues)
    X_opt = np.delete(X_opt, max_index, axis=1)
    regressor_ols = sm.OLS(endog=y, exog=X_opt).fit()
    pvalues = regressor_ols.pvalues

final_summary = regressor_ols.summary()


    
