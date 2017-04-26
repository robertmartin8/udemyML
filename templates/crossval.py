"""
Created on Fri Apr  7 19:03:12 2017

@author: Robert
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


models = []

models.append(('KNN', KNeighborsClassifier()))
models.append(('Random forest', 
               RandomForestClassifier(n_estimators = 100,
                                      criterion = 'entropy')))
models.append(('NB', GaussianNB()))
models.append(('KernelSVM', SVC(kernel='rbf')))

for name, model in models:
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    
    print ("---------- model: " + name + '-------------------')
    print("Acurracy: " + str(accuracy_score(y_test, y_pred)))

    TP, TN, FP, FN = cm[1][1], cm[0][0], cm[0][1], cm[1][0]
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    F1 = 2 * precision * recall / (precision + recall)
    
    print("Precision: " + str(round(precision, 2)))
    print("Recall: " + str(round(recall, 2)))
    print("F1: " + str(round(F1, 2)))
    
