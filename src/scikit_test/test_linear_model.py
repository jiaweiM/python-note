from sklearn import linear_model
from sklearn import datasets

diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

diabetes_X_train = diabetes_X[:-20]
diabetes_y_train = diabetes_y[:-20]

diabetes_X_test = diabetes_X[-20:]
diabetes_y_test = diabetes_y[-20:]

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
print(regr.coef_)