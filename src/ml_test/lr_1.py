import numpy as np
import pandas as pd

california_housing_dataframe = pd.read_csv("../datasets/california_housing_train.csv", sep=",")
california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe['median_house_value'] /= 1000.0
print(california_housing_dataframe.describe())

