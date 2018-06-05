from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

df = "insert your data here"
X_train, X_test, y_train, y_test = train_test_split(df)

# Comparing multiple classifiers at once
models = [
    ("KNN", KNeighborsClassifier()),
    ("Random forest", RandomForestClassifier(n_estimators=100, criterion="entropy")),
    ("NB", GaussianNB()),
    ("KernelSVM", SVC(kernel="rbf")),
]

for name, model in models:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("---------- model: " + name + "-------------------")
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("acurracy:", round(accuracy_score(y_test, y_pred), 2))
    print("precision:", round(precision_score(y_test, y_pred), 2))
    print("recall:", round(recall_score(y_test, y_pred), 2))
    print("F1 score:", round(f1_score(y_test, y_pred), 2))
