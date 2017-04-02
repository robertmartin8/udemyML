"""
Created on Fri Mar 31 21:41:34 2017

@author: Robert
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')
import matplotlib.cm
cmap = matplotlib.cm.get_cmap('plasma')

import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

ds = pd.read_csv('Mall_Customers.csv')
X = ds.iloc[:, [3,4]].values

k = 5
# Dendrogram
plt.cla()
plt.figure(1)
z = sch.linkage(X, method = 'ward')
dendrogram = sch.dendrogram(z)
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()

hc = AgglomerativeClustering(n_clusters = k, affinity = "euclidean",
                             linkage = 'ward')
y_hc = hc.fit_predict(X)

labels = [('Cluster ' + str(i+1)) for i in range(k)]
colours = ['red', 'green', 'blue', 'cyan', 'magenta']


plt.figure(2)
for i in range(k):
    plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], s = 20,
                c = cmap(i/k), label = labels[i]) 
    
plt.xlabel('Age')
plt.ylabel('Spending score')
plt.title('HC cluster plot')
plt.legend()
plt.show()
#    