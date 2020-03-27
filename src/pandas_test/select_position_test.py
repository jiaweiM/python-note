import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from pandas.testing import assert_series_equal
from numpy.testing import assert_array_equal


def test_index():
    s1 = pd.Series([3, 5, 1])
    assert s1.iloc[0] == 3
    assert s1.iloc[2] == 1


def test_multiple_index():
    s1 = pd.Series([1, 2, 3, 4])
    s2 = s1.iloc[[1, 3]]
    assert_array_equal(s2, np.array([2, 4]))


def test_slice():
    s1 = pd.Series([1, 3, 5, 7, 11])
    s2 = s1.iloc[:3]

    assert_series_equal(s2, pd.Series([1, 3, 5]))


def test_slice_dataframe():
    df = pd.DataFrame({"col1": [1, 2, 3],
                       "col2": [4, 5, 6],
                       "col3": [7, 8, 9]},
                      index=["row1", "row2", "row3"])
    df2 = df.iloc[:2]
    assert_frame_equal(df2, pd.DataFrame({
        "col1": [1, 2],
        "col2": [4, 5],
        "col3": [7, 8]
    }, index=["row1", "row2"]))
    df3 = df.iloc[1:3, 1:3]
    assert_frame_equal(df3, pd.DataFrame({
        "col2": [5, 6], "col3": [8, 9]},
        index=['row2', 'row3']))


def test_index_frame():
    df = pd.DataFrame({"col1": [1, 2, 3],
                       "col2": [4, 5, 6],
                       "col3": [7, 8, 9]},
                      index=["row1", "row2", "row3"])
    df1 = df.iloc[[0, 2], [1, 2]]
    assert_frame_equal(df1, pd.DataFrame(
        {"col2": [4, 6],
         "col3": [7, 9]},
        index=["row1", "row3"]
    ))


def test_int_int():
    df = pd.DataFrame({"col1": [1, 2],
                       "col2": [3, 4]},
                      index=["row1", "row2"])
    assert df.iloc[1, 1] == 4
    assert df.iloc[0, 1] == 3


def test_frame_int():
    df = pd.DataFrame({"col1": [1, 2],
                       "col2": [3, 4]},
                      index=["row1", "row2"])
    s1 = df.iloc[1]
    assert_series_equal(s1, pd.Series(
        [2, 4], name="row2", index=['col1', 'col2']))


def test_set():
    s1 = pd.Series([1, 2, 3])
    s1.iloc[:2] = 0
    assert_series_equal(s1, pd.Series([0, 0, 3]))
