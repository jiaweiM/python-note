import numpy as np
import pandas as pd


def test_series_size():
    s = pd.Series({'a': 1, 'b': 2, 'c': 3})
    assert s.size == 3


def test_dataframe_size():
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    assert df.size == 4


def test_shape():
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    assert df.shape == (2, 2)
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4], "col3": [5, 6]})
    assert df.shape == (2, 3)


def test_sort_values():
    df = pd.DataFrame({
        'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
        'col2': [2, 1, 9, 8, 7, 4],
        'col3': [0, 1, 9, 4, 2, 3]
    })
    df1 = df.sort_values(by=['col1'])

    print(df)
    print(df1)
