"""
Created on Sat Mar 18 16:19:12 2017

@author: Robert
"""

import numpy as np
from functools import reduce

# Later on we need some way of doing a dot product of many matrices.
# It is easiest to write a helper function to do so. 

def mdot(*args):
    return reduce(np.dot, args)

# Just a warning, this is the first time in my life I have written a 
# class that isn't part of a tutorial. I still don't properly understand
# classes fully.

class LinearRegression:
    
    
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.beta = None
     
        
    def fit(self):
        # Beta is (n x 1) matrix of coefficients
        # The analytical solution for beta is: 
        #    b = inverse(X'.X).X'.y
        # where X' denotes the tranpose of x.
        
        # In reality, this solution is slow for large X, so 
        # this is not how people do it in reality. 

        self.beta = mdot(
                np.linalg.inv(np.dot(np.transpose(self.X), self.X)), 
                np.transpose(self.X), 
                self.y)

        
    def predict(self, X_test):
        # the prediction is simply the dot product of the beta matrix and
        # and X_test.
        return np.dot(X_test, self.beta)

# Example usage: 
'''     
regressor = LinearRegression(X_train,y_train)
regressor.fit()
y_pred = regressor.predict(X_test)
'''







