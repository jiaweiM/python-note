import numpy as np
from sklearn import datasets

iris_X, iris_Y = datasets.load_iris(return_X_y=True)

np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_Y_train = iris_Y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_Y_test = iris_Y[indices[-10:]]

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_Y_train)
print(knn.predict(iris_X_test))
print(iris_Y_test)
