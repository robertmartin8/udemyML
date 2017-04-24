
# Reading in Data
ds = read.csv('Churn_Modelling.csv')
ds = ds[4:14]

ds$Geography = as.numeric(as.factor(ds$Geography))
ds$Gender = as.numeric(as.factor(ds$Gender))

# Scaling and splitting
library(caTools)
ds[-11] = scale(ds[-11])

split = sample.split(ds$Exited, SplitRatio = 0.8)
train = subset(ds, split == TRUE)
test = subset(ds, split == FALSE)

# Fitting the ANN
library('h2o')
h2o.init(nthreads = -1)

clf = h2o.deeplearning(y = 'Exited',
                       training_frame = as.h2o(train),
                       standardize = FALSE,
                       activation = "Rectifier",
                       hidden = c(6,6),
                       epochs = 100,
                       train_samples_per_iteration = -2)

# Predicting
prob_pred = h2o.predict(clf, newdata = as.h2o(test[-11]))
y_pred = as.vector(prob_pred > 0.5)


cm = table(test[,11], y_pred)

h2o.shutdown()
