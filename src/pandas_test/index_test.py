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