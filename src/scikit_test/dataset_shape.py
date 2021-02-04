from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
data = iris.data
print(data.shape)

digits = datasets.load_digits()
print(digits.images.shape)

plt.imshow(digits.images[-1], cmap=plt.cm.gray_r)
