import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal


def test_series():
    s = pd.Series(range(-3, 4))
    s1 = s[s > 0]
    np.testing.assert_array_equal(s1.values, np.array([1, 2, 3]))

    s2 = s[(s < -1) | (s > 0.5)]
    np.testing.assert_array_equal(s2.values, np.array([-3, -2, 1, 2, 3]))

    s3 = s[~(s < 0)]
    np.testing.assert_array_equal(s3.values, np.array([0, 1, 2, 3]))


def test_select_dataframe_rows():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [7, 8, 9]})
    df1 = df[df['A'] > 1]
    np.array_equal(df1.values, pd.DataFrame({"A": [2, 3], "B": [8, 9]}).values)


def test_map():
    df = pd.DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
                       'b': ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
                       'c': [1, 2, 3, 4, 5, 6, 7]})
    criterion = df['a'].map(lambda x: x.startswith('t'))
    df1 = df[criterion]
    assert_frame_equal(df1.reset_index(drop=True),
                       pd.DataFrame({'a': ['two', 'three', 'two'],
                                     'b': ['y', 'x', 'y'],
                                     'c': [3, 4, 5]}))
