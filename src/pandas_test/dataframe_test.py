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
