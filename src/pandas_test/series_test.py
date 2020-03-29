import numpy as np
import pandas as pd
import pandas.testing as ptest


def test_create():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    assert s.size == 6


def test_sort_values():
    """sort by values"""
    s = pd.Series([np.nan, 1, 3, 10, 5])
    sorted_s = s.sort_values()

    # assert sorted_s.values == np.arange([1, 3, 5, 10, np.nan], dtype=np.float64)

    # ptest.assert_series_equal(sorted_s, )

    ptest.assert_series_equal(sorted_s, pd.Series(
        [1, 3, 5, 10, np.nan]), check_dtype=False)
    # assert sorted_s.equals(pd.Series([1.0, 3, 5, 10, np.nan]))
    print(sorted_s)


def test_create_ndarray():
    s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    print(s)


def test_iat():
    '''通过位置访问某个位置的值，需要获得或设置 Series 或 DataFrame 某个位置的单个值时使用'''
    df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                      columns=['A', 'B', 'C'])
    val = df.iat[1, 2]  # getter value at (2,3)
    assert val == 1

    df.iat[1, 2] = 10  # setter
    assert df.iat[1, 2] == 10


def test_apply():
    s = pd.Series([20, 21, 12], index=['London', 'New York', 'Helsinki'])

    def square(x):
        return x ** 2

    s1 = s.apply(square)
    np.array_equal(s.values, np.array([20, 21, 12]))
    np.array_equal(s1.values, np.array([400, 441, 144]))


def test_apply_lambda():
    s = pd.Series([20, 21, 12], index=['London', 'New York', 'Helsinki'])
    s1 = s.apply(lambda x: x ** 2)
    np.array_equal(s1.values, np.array([400, 441, 144]))


def test_apply_args():
    def subtract_custom_value(x, custom_value):
        return x - custom_value

    s = pd.Series([20, 21, 12])
    s1 = s.apply(subtract_custom_value, args=(5,))
    np.array_equal(s1.values, np.array([15, 16, 7]))


def test_apply_keyword():
    def add_custom_values(x, **kwargs):
        for month in kwargs:
            x += kwargs[month]
        return x

    s = pd.Series([20, 21, 12])
    s1 = s.apply(add_custom_values, june=30, july=20, august=25)
    np.array_equal(s1.values, np.array([95, 96, 87]))


def test_apply_numpy_func():
    s = pd.Series([20, 21, 12])
    s1 = s.apply(np.log)

