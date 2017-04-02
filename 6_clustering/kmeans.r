ds = read.csv('Mall_Customers.csv')
X = ds[4:5]

wcss = vector()

for (i in 1:10) 
    wcss[i] =sum(kmeans(X, i)$withinss)

plot(1:10, wcss, type = 'b', main=paste("Elbow method"), xlab = 'number clusters' )

kmeans = kmeans(X, 5)

# library(cluster)
# clusplot(X,r
#          kmeans$cluster,
#          shade = TRUE,
#          color = TRUE,
#          labels= 4)
# 
# y_kmeans = kmeans$cluster

# Visualising the clusters
library(cluster)
clusplot(X,
         kmeans$cluster,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste('Clusters of customers'),
         xlab = 'Annual Income',
         ylab = 'Spending Score')