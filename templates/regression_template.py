import pandas as pd
from sklearn.model_selection import train_test_split

# Importing the dataset
df = pd.read_csv("Data.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)

# Different regression algorithms
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

from sklearn.preprocessing import PolynomialFeatures

regressor = PolynomialFeatures(degree=4)
X_poly = regressor.fit_transform(X)

from sklearn.svm import SVR

regressor = SVR(kernel="rbf")

from sklearn.tree import DecisionTreeRegressor

regressor = DecisionTreeRegressor()

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=100)

# Fitting and predicting
regressor.fit(X, y)
y_pred = regressor.predict(10)
# In the case where we scaled the variables:
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[10]]))))


# Visualising the Regression results
import numpy as np
import matplotlib.pyplot as plt

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color="red")
plt.plot(X_grid, regressor.predict(X_grid), color="blue")
plt.title("Title")
plt.xlabel("Independent variable")
plt.ylabel(list(df)[-1])
plt.show()
