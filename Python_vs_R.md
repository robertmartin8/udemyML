# Python versus R

Which language should I use for which algorithm?

For a number of algorithms, the language does not make a difference so choose based on coherence with the rest of the project:
- Random forest regression and classification
- K-nearest neighbours
- Naïve Bayes classification

## Data preprocessing

- R requires far fewer packages, and we never have to deal with instantiating objects etc.
- In python it is easier to split into training/testing sets, and to impute values.
- However, everything else is easier in R.
- OneHotEncoder, although cumbersome to use, often makes life a lot easier down the road.

Verdict: **R, unless we need OneHotEncoder**.

## General data visualisation

- R has many convenient built in plot functions for specific algorithms, e.g the SVM and decision tree.
- Plots by default seem to be a bit prettier in R. But ggplot is pretty nasty to use.
- However, the coloured scatterplot for classification is noticeably slower in R than python.
- Seaborn is beautiful.

Verdict: **Slight python**

## Linear regression

- All of the functions are built in for R. Very intuitive syntax
- Backward elimination to improve the model requires about 10 lines of code in python, but it is a single line builtin in R.

**Verdict: Strong R**

## Polynomial regression

- The method presented in the Udemy tutorial for fitting a polynomial regression model in R is terrible. However, there is in fact a built in function called `poly()` which makes things a lot easier.

**Verdict: R, but only if you use** `poly()`

## SVR

- The python library requires us to scale our values, while the R library e1071 takes care of it.

**Verdict: R**

## Decision tree regression

- Easy to implement in both languages, but it is slightly more intuitive in python.

**Verdict: Python**


## Logistic regression

- Much more intuitive in python.

**Verdict: Python**

## SVM classification

- About the same ease of use in both.
- But R has a default plot function for the SVM classifier which, in one line, does what normally requires 15 in both R and python.

**Verdict: R, because of the plot()**

## Decision tree classification

- About the same difficulty in both
- As with SVM, R has a very convenient way of visualising the tree.

**Verdict: R because of the tree visualisation**

## Clustering

- kmeans is a built-in in R, and it is marginally easier to use than the python version
- Likewise, hierarchical clustering is slightly easier in R.
- However, the plots in python are *so* much prettier.

**Verdict: python if you need visualisation**


## Association rule learning

- The `arules` package in R is very easy to use, and the output is very readable.
- This is contrasted to the particular formatting required by `apyori`, and the awful output.

**Verdict: strong R**

## Reinforcement learning

- I coded the UCB and Thompson sampling algorithms from scratch. Any time I have to code something from scratch, python is a better choice.
- In any case, the R code was adapted straight from the python code.

**Verdict: python**

## Natural language processing

- Interacting with the corpus is a pain in R.
- However, you can clean the text and create the sparse matrix in one simple function (though Hadelin chooses not to do this).

**Verdict: strong R**

## Neural Networks

- Neural networks seem to be much slower in python, because R connects to an external server which does the computation for us. The difference is massive.
- However, R still doesn't have strong support for convolutional neural networks.

**Verdict: strong R, unless you need convolutional NNs**

## Model selection

- Cross validation is overall a bit nicer in python.
- The `sklearn` grid search is far more intuitive, and seems to allow tuning of more different parameters, however there is a lot of hard coding required.
- The `caret` library in R on the other hand is almost mystical.

**Verdict: slight python **

## XGBoost

- The installation in python is nightmarish, but it is just `install.packages('xgboost')` in R!
- But after it is installed, it is just as easy to run in both R and python. Thus it's a matter of which syntax you prefer.

**Verdict: slight R, but mostly because it is hard to install for python**
