import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')


# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Training/testing
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3,
                                                    random_state=0)

# Regressor
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# Visualisation
plt.scatter(X_train, y_train, color = '#31b254')
plt.plot(X_train, regressor.predict(X_train))
plt.title("Relationship between years of experience and salary")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()
