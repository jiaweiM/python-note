import numpy as np
import pandas as pd


def test_series():
    s = pd.Series(range(-3, 4))
    s1 = s[s > 0]
    assert s1.size == 3


def test_map():
    df2 = pd.DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
                        'b': ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
                        'c': np.random.randn(7)})
    # only want "two" and "three"
    criterion = df2['a'].map(lambda x: x.startswith('t'))
    var = df2[criterion]
    print(var)


def test_iloc():
    s1 = pd.Series(np.random.randn(6), index=list('abcdef'))
    s2 = s1.loc['c':]
    print(s2)


def test_iat():
    df = pd.DataFrame([[0, 2, 3],
                       [0, 4, 1],
                       [10, 20, 30]], columns=['A', 'B', 'C'])
    val = df.iat[1, 2]  # 1 行 2 列
    assert val == 1

    # set value
    df.iat[1, 2] = 10
    assert df.iat[1, 2] == 10

    # 获取 series 中的值
    val = df.loc[0].iat[1]
    assert val == 2
