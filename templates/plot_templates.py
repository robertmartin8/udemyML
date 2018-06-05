# Simple classifcation plot
import matplotlib.pyplot as plt

plt.scatter(X1, X2, color=["green" if i else "red" for i in y])


# Regression pairplot
import seaborn as sns
import numpy as np

sns.set(style="ticks", color_codes=True)
g = sns.pairplot(df, kind="reg")

# Visualising regression results
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color="red")
plt.plot(X_grid, regressor.predict(X_grid), color="blue")
plt.title("Title")
plt.xlabel("Independent variable")
plt.ylabel(list(df)[-1])
plt.show()


# Classifier with two dependent variables
from matplotlib.colors import ListedColormap

X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
    np.arange(X_set[:, 0].min() - 1, X_set[:, 0].max() + 1, step=0.01),
    np.arange(X_set[:, 1].min() - 1, X_set[:, 1].max() + 1, step=0.01),
)
boundary = clf.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape)
plt.contourf(X1, X2, boundary, alpha=0.75, cmap=ListedColormap(("#fc7a74", "#6ff785")))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green"))(i),
        label=j,
        s=8,
    )
plt.title("Title")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.show()


# Clustering diagram, requires a parameter k for the number of clusters.
k = 5
labels = [("Cluster " + str(i + 1)) for i in range(k)]
colours = ["red", "green", "blue", "cyan", "magenta"]

for i in range(k):
    plt.scatter(
        X[y_kmeans == i, 0], X[y_kmeans == i, 1], s=20, c=colours[i], label=labels[i]
    )

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=100,
    c="black",
    label="Centroids",
    marker="X",
)
plt.xlabel("X1")
plt.ylabel("X2")
plt.title("Title")
plt.legend()
plt.show()


# Prettier cluster diagram
import matplotlib.cm

cmap = matplotlib.cm.get_cmap("plasma")  # change this for swag
for i in range(k):
    plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], s=20, c=cmap(i / k), label=labels[i])
plt.xlabel("Age")
plt.ylabel("Spending score")
plt.title("HC cluster plot")
plt.legend()
plt.show()


# 3d scatterplot
fig = plt.figure()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
plt.show()


# 3D clusterplot
y_kmeans = kmeans.fit(X)
labels = y_kmeans.labels_

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels.astype(np.float))
ax.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    kmeans.cluster_centers_[:, 2],
    s=100,
    c="black",
    label="Centroids",
    marker="X",
)
ax.set_xlabel("Age")
ax.set_ylabel("Annual Income")
ax.set_zlabel("Spending score")
plt.title("Kmeans cluster plot")
plt.legend()
plt.show()


# Dendrogram
z = sch.linkage(X, method="ward")
dendrogram = sch.dendrogram(z)
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean distances")
plt.show()


# Bar chart with two lists
width = 0.35  # width of bar
ind = np.arange(d)  # d is a numerical category
fig, ax = plt.subplots()
rects1 = ax.bar(ind, LIST1, width)
rects2 = ax.bar(ind + width, LIST2, width)
ax.set_xlabel("x categories")
# ax.set_yticks([])
ax.set_xticks(range(d))
ax.legend((rects1[0], rects2[0]), ("LIST1", "LIST2"))
ax.set_title("")
plt.show()
