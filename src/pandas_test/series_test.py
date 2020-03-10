import numpy as np
import pandas as pd


def test_create_ndarray():
    s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    print(s)
