# Preprocessing

Prior to applying machine learning algorithms, we must
preprocess the data.

## 1. Import data

### Python

```python
import pandas
pd.read_csv()
```

### R
```r
read.csv()
```

## 2. Missing data

Missing data needs to be filled in. A convenient way of doing so is by replacing the `NaN` with the mean of the other values.

### Python

In python, we use `sklearn.preprocessing.Imputer`. Instantiate the object, then fit and transform appropriately.

```python
from sklearn.preprocessing import Imputer

imputer = Imputer()
X[:, 1:3] = imputer.fit_transform(X[:, 1:3])
```

### R

In R, we use an if-else statement. If the datum is `NaN`, replace it with the mean, else pass.

```R
ds$Age = ifelse(is.na(ds$Age),
                ave(ds$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                ds$Age)
```

## 3. Dealing with categorical data

Categorical data needs to be converted to numerals, but we do not want these to be ordered.

### Python

Instantiate a LabelEncoder, then fit and transform. However, python by default will treat the labels of 0, 1, 2 etc as numerical values (which we don't want).

Use OneHotEncoder so that instead of an object belonging to one category, we treat the objects as having either a 0 or 1 value in every category.

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()

```

### R

Luckily, when you map the categories onto numerals, R treats these numerals as labels rather than numbers, so we don't need an equivalent of OneHotEncoder.

```R
y = factor(y, levels = c('No', 'Yes'), labels = c(0,1))
```

## 4. Splitting the data into training and testing sets

A general rule of thumb is to use an 80:20 training:testing split.

### Python

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

### R

In R, we need the `caTools` package.

```R
library(caTools)
split = sample.split(dataset$y, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)
```

## 5. Feature Scaling

It is important to scale features, otherwise one feature may be given excessive weight simply because its values are larger. Typically we want to map the X data to the interval [-1, 1]. We can do this by standardising or normalising.

![](images/2017/03/feature_scaling.png)

### Python

```python
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)

```

### R

```R
training_set = scale(training_set)
```
