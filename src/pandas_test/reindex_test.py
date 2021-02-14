import numpy as np
import pandas as pd


def test_series():
    s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
    print(s)
    s1 = s.reindex(["e", "b", "f", "d"])
    print(s1)
    print(s)


def test_frame():
    df = pd.DataFrame(
        {"one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
         "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
         "three": pd.Series(np.random.randn(3), index=["b", "c", "d"])
         }
    )
    print(df)
    df1 = df.reindex(index=['c', 'f', 'b'], columns=["three", "two", "one"])
    print(df1)


def test_frame_axis():
    df = pd.DataFrame(
        {"one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
         "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
         "three": pd.Series(np.random.randn(3), index=["b", "c", "d"])
         }
    )
    print(df)
    df1 = df.reindex(["c", "f", "b"], axis="index")
    print(df1)
    df2 = df.reindex(["three", "two", "one"], axis="columns")
    print(df2)


def test_share_index():
    s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
    df = pd.DataFrame(
        {"one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
         "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
         "three": pd.Series(np.random.randn(3), index=["b", "c", "d"])
         }
    )

    rs = s.reindex(df.index)
    print(rs)
    assert rs.index is df.index
