"""
Created on Wed Mar 29 21:42:38 2017

@author: Robert
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

ds = pd.read_csv('Mall_Customers.csv')
X = ds.iloc[:, [3,4]].values


# Choosing the value of k

wcss = []

for i in range(1,21):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit_transform(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,21), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()



plt.cla()
k = 5

kmeans = KMeans(n_clusters = k)
y_kmeans = kmeans.fit_predict(X)

labels = [('Cluster ' + str(i+1)) for i in range(k)]
colours = ['red', 'green', 'blue', 'cyan', 'magenta']

for i in range(k):
    plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s = 20,
                c = colours[i], label = labels[i]) 
    
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
            s = 100, c = 'black', label = 'Centroids', marker = 'X')
plt.xlabel('Age')
plt.ylabel('Spending score')
plt.title('Kmeans cluster plot')
plt.legend()
plt.show()
    