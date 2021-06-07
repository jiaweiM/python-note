# 重建索引

- [重建索引](#重建索引)
  - [简介](#简介)
    - [Series 使用](#series-使用)
    - [DataFrame 使用](#dataframe-使用)
    - [axis 参数](#axis-参数)
    - [Index 共享](#index-共享)
    - [reindex-axis](#reindex-axis)
  - [重建索引和另一个对象对齐-reindex_like](#重建索引和另一个对象对齐-reindex_like)
  - [互相对齐-align](#互相对齐-align)

2021-02-14, 21:31
***

## 简介

`reindex()` 是 pandas 数据对齐的基本操作方法，几乎所有依赖标签对齐的功能都使用该方法实现。重建索引（reindex）使数据与特定轴上的一组标签匹配，实现了如下效果：

- 对已有数据重新排序以匹配标签；
- 如果标签对应的位置缺少数据，插入 NA；
- 也可以自定义缺失值。

### Series 使用

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

### DataFrame 使用

对 `DataFrame`，可以同时对 index 和 columns 重新索引：

```py
df = pd.DataFrame(
    {"one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
        "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"])
        }
)
#         one       two     three
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

### axis 参数

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

### Index 共享

包含实际轴标签的 `Index` 对象可以在不同对象间共用。如果我们有一个 `Series` 和一个 `DataFrame`，则可以用 `DataFrame` 的 index 对 `Series` 重建索引，反之亦然。例如：

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

### reindex-axis

`DataFrame.reindex()` 也支持 axis 参数。例如：

```py
In [208]: df
Out[208]: 
        one       two     three
a  1.394981  1.772517       NaN
b  0.343054  1.912123 -0.050390
c  0.695246  1.478369  1.227435
d       NaN  0.279344 -0.613172

In [214]: df.reindex(["c", "f", "b"], axis="index")
Out[214]: 
        one       two     three
c  0.695246  1.478369  1.227435
f       NaN       NaN       NaN
b  0.343054  1.912123 -0.050390

In [215]: df.reindex(["three", "two", "one"], axis="columns")
Out[215]: 
      three       two       one
a       NaN  1.772517  1.394981
b -0.050390  1.912123  0.343054
c  1.227435  1.478369  0.695246
d -0.613172  0.279344       NaN
```

> MultiIndex 是重建索引更简洁的方式。

## 重建索引和另一个对象对齐-reindex_like

如果你希望对一个对象重建索引，以与另一个对象的标签相同。此时可以使用 `reindex_like()` 方法实现：

```py
In[1]: df1 = pd.DataFrame([[24.3, 75.7, 'high'],
                           [31, 87.8, 'high'],
                           [22, 71.6, 'medium'],
                           [35, 95, 'medium']],
                   columns=['temp_celsius', 'temp_fahrenheit', 'windspeed'],
                   index=pd.date_range(start='2014-02-12', end='2014-02-15', freq='D'))
In[2]: df1
Out[2]:
            temp_celsius  temp_fahrenheit windspeed
2014-02-12          24.3             75.7      high
2014-02-13          31.0             87.8      high
2014-02-14          22.0             71.6    medium
2014-02-15          35.0             95.0    medium

In[3]: df2 = pd.DataFrame([[28, 'low'],
                           [30, 'low'],
                           [35.1, 'medium']],
                   columns=['temp_celsius', 'windspeed'],
                   index=pd.DatetimeIndex(['2014-02-12', '2014-02-13', '2014-02-15']))

In[4]: df2
Out[4]:
            temp_celsius windspeed
2014-02-12          28.0       low
2014-02-13          30.0       low
2014-02-15          35.1    medium

In[5]: df2.reindex_like(df1)
Out[5]:
            temp_celsius  temp_fahrenheit windspeed
2014-02-12          28.0              NaN       low
2014-02-13          30.0              NaN       low
2014-02-14           NaN              NaN       NaN
2014-02-15          35.1              NaN    medium
```

操作之后，`df2` 的索引和 `df1` 完全相同。在 columns 轴，额外添加了 `temp_fahrenheit`，在 index 轴，额外添加了 `2014-02-14`。

## 互相对齐-align

`align()` 方法是对齐两个对象的最快方法。其 `join` 参数使用：

- `join='outer'`：采用索引并集（默认）
- `join='left'`：采用调用对象的索引
- `join='right'`：采用参数对象的索引
- `join='inner'`：采用索引交集

例如：

- 返回包含重建索引 `Series` 的 tuple

```py
In [219]: s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])

In [220]: s1 = s[:4] # 前 4 个元素

In [221]: s2 = s[1:] # 后 4 个元素

In [222]: s1.align(s2) # 默认取并集
Out[222]: 
(a   -0.186646
 b   -1.692424
 c   -0.303893
 d   -1.425662
 e         NaN
 dtype: float64,
 a         NaN
 b   -1.692424
 c   -0.303893
 d   -1.425662
 e    1.114285
 dtype: float64)

In [223]: s1.align(s2, join="inner") # 取交集
Out[223]: 
(b   -1.692424
 c   -0.303893
 d   -1.425662
 dtype: float64,
 b   -1.692424
 c   -0.303893
 d   -1.425662
 dtype: float64)

In [224]: s1.align(s2, join="left")
Out[224]: 
(a   -0.186646
 b   -1.692424
 c   -0.303893
 d   -1.425662
 dtype: float64,
 a         NaN
 b   -1.692424
 c   -0.303893
 d   -1.425662
 dtype: float64)
```

- 对 `DataFrame`，