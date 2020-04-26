import pandas as pd


def test_query2():
    df = pd.DataFrame({"a": [2, 3, 6, 2, 7],
                       "b": [7, 6, 1, 1, 4],
                       "c": [1, 7, 9, 4, 4]})

    df2 = pd.DataFrame({"a": [3, 3, 1],
                        "b": [2, 9, 3],
                        "c": [6, 9, 3]})

    expr = '0 <= a <= c <= 5'
    d = map(lambda frame: frame.query(expr), [df, df2])
    lst = list(d)
    assert lst[0] == pd.DataFrame({'a': [2], 'b': [1], "c": [4]})
    assert lst[1] == pd.DataFrame({'a': [1], 'b': [3], 'c': [3]})
