"""
Created on Mon Mar 27 21:02:14 2017

@author: Robert
"""

"""
This code creates a number of classification plots with different 
penalty parameters, so you can visualise how the algorithm punishes
overfitting. I compiled some images I created into a gif, which can be 
found elsewhere in this repo.  


"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

# Reading in data
ds = pd.read_csv("Social_Network_Ads.csv")
X = ds.iloc[:, 2:4].values
y = ds.iloc[:,4].values


# Splitting and scaling
X_train, X_test, y_train, y_test = train_test_split(X,y)

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

# Plot
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap

numplots = 30
increment = 10

for c in range(increment, increment*numplots + 1,increment):
    clf = SVC(kernel='rbf', C = c/10)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print((cm[0][0]+cm[1][1])/sum(sum(cm)))

    X_set, y_set = X_train, y_train
    X1, X2 = np.meshgrid(np.arange(X_set[:,0].min() - 1, 
                                   X_set[:,0].max() + 1, 
                                   step = 0.01),
                         np.arange(X_set[:,1].min() - 1, 
                                   X_set[:,1].max() + 1, 
                                   step = 0.01))
    boundary = clf.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape)
    
    fig = plt.figure(int(c/10))
    plt.contourf(X1, X2, boundary, alpha = 0.75, 
                 cmap = ListedColormap(('#fc7a74', '#6ff785')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    for i,j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                    c = ListedColormap(('red', 'green'))(i), 
                    label = j, s = 8)
        
    title = "Penalty parameter = " + str(c/10) + ", error = " + str((cm[0][0]+cm[1][1])/sum(sum(cm)))
    plt.title(title)
    plt.xlabel('Age')
    plt.ylabel('Salary')
    plt.legend()
    plt.figure()
    fname = str(c/10) + '.png'
    fig.savefig(fname)
    plt.cla()
    
    