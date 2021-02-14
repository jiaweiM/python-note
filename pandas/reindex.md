# 重新索引

- [重新索引](#重新索引)
  - [简介](#简介)
  - [Series 使用](#series-使用)
  - [DataFrame 使用](#dataframe-使用)
  - [axis 参数](#axis-参数)
  - [Index 共享](#index-共享)

2021-02-14, 21:31
***

## 简介

`reindex()` 是 pandas 数据对齐的基本操作方法，几乎所有依赖标签对齐的其它功能都使用该方法实现。重新索引（reindex）使数据与特定轴上的一组标签匹配，实现了如下效果：

- 对已有数据重新排序以匹配标签；
- 如果标签对应的位置缺少数据，插入 NA；
- 也可以自定义缺失值。

## Series 使用

```py
import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])

# a    0.145818
# b   -0.300408
# c    0.515304
# d    1.589980
# e   -1.673086
# dtype: float64
```

```py
s1 = s.reindex(["e", "b", "f", "d"])
# e   -0.665193
# b    0.738253
# f         NaN
# d    0.367754
# dtype: float64
```

这里，`f` 是新的标签，没有对应的数据，默认以 `NaN` 填充；指定的其它标签（e, b, f, d）对应的数据被提取出来。

## DataFrame 使用

对 `DataFrame`，可以同时对 index 和 columns 重新索引：

```py
df = pd.DataFrame(
    {"one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
        "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"])
        }
)
# one       two     three
# a -0.173296  0.942775       NaN
# b  0.538511  2.370050 -1.082425
# c -0.325984  0.773878 -0.688420
# d       NaN  0.329996  0.551655

df1 = df.reindex(index=['c', 'f', 'b'], columns=["three", "two", "one"])
#       three       two       one
# c -0.688420  0.773878 -0.325984
# f       NaN       NaN       NaN
# b -1.082425  2.370050  0.538511
```

可以看到：

- 对 index 提取了 c, f, b 行，因为 f 不存在，所以全部是 `NaN`。
- 对 columns 提取了 `"three", "two", "one"`，其实就是重新排序了一下。

## axis 参数

可以使用 `axis` 参数指定对哪个轴重新索引，例如：

```py
df = pd.DataFrame(
    {"one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
     "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
     "three": pd.Series(np.random.randn(3), index=["b", "c", "d"])
    }
)
#         one       two     three
# a  1.622340  1.116409       NaN
# b  1.534885  0.353686 -0.171910
# c -0.679127  0.528687  0.275503
# d       NaN  0.957281 -0.204305

df1 = df.reindex(["c", "f", "b"], axis="index")
#         one       two     three
# c -0.679127  0.528687  0.275503
# f       NaN       NaN       NaN
# b  1.534885  0.353686 -0.171910
```

这里用 `axis="index"` 指定对 index 重新索引，提取了 c, f, b 行。

或者对 "columns" 重新索引：

```py
df2 = df.reindex(["three", "two", "one"], axis="columns")
#       three       two       one
# a       NaN  0.766008 -1.215344
# b  0.330652  0.310886  0.175389
# c  1.016581 -0.487880 -2.389178
# d  0.433645  0.198953       NaN
```

## Index 共享

包含实际轴标签的 `Index` 对象可以在不同对象间共用。如果我们有一个 `Series` 和一个 `DataFrame`，则可以用 `DataFrame` 的 index 对 `Series` 重新索引，反之亦然。例如：

```py
s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
df = pd.DataFrame(
    {"one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
     "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
     "three": pd.Series(np.random.randn(3), index=["b", "c", "d"])
    }
)

rs = s.reindex(df.index)
print(rs)
# a   -0.503893
# b    0.767475
# c    0.955267
# d    1.257989
# dtype: float64

assert rs.index is df.index
```

这里重新索引的 `Series` 的 index 和 `DataFrame` 是同一个 Index 对象。

