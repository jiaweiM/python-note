# Descriptive statistics

- [Descriptive statistics](#descriptive-statistics)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [方法总结](#%e6%96%b9%e6%b3%95%e6%80%bb%e7%bb%93)
  - [Value counts](#value-counts)

2020-04-22, 11:16
***

## 简介

`Series` 和 `DataFrame` 包含大量描述统计学相关方法。其中大多数为聚合操作（即生成低维数据），如 `sum()`, `means()`, `quantile()` 等，不过部分函数生成等 size 的对象，如 `cumsum()`, `cumprod()`。

一般来说，这些方法需要 `axis` 参数指定统计的维度，可以通过名称或 integer 指定。

- `Series`，无需 axis 参数
- `DataFrame`："index" (axis=0, default), "columns" (axis=1)

例如：

```py
In [77]: df
Out[77]:
        one       two     three
a  1.394981  1.772517       NaN
b  0.343054  1.912123 -0.050390
c  0.695246  1.478369  1.227435
d       NaN  0.279344 -0.613172

In [78]: df.mean(0)
Out[78]:
one      0.811094
two      1.360588
three    0.187958
dtype: float64

In [79]: df.mean(1)
Out[79]:
a    1.583749
b    0.734929
c    1.133683
d   -0.166914
dtype: float64
```

所有这类方法都有一个 `skipna` 可选项，是否排除缺失值（默认 `True`）：

```py
In [80]: df.sum(0, skipna=False)
Out[80]:
one           NaN
two      5.442353
three         NaN
dtype: float64

In [81]: df.sum(axis=1, skipna=True)
Out[81]:
a    3.167498
b    2.204786
c    3.401050
d   -0.333828
dtype: float64
```

和其它计算行为结合，可以很方便的执行各种统计学操作，如标准化：

```py
In [82]: ts_stand = (df - df.mean()) / df.std()

In [83]: ts_stand.std()
Out[83]:
one      1.0
two      1.0
three    1.0
dtype: float64

In [84]: xs_stand = df.sub(df.mean(1), axis=0).div(df.std(1), axis=0)

In [85]: xs_stand.std(1)
Out[85]:
a    1.0
b    1.0
c    1.0
d    1.0
dtype: float64
```

`cumsum()` 和 `cumprod()` 这类方法保留 `NaN` 值。例如：

```py
In [86]: df.cumsum()
Out[86]:
        one       two     three
a  1.394981  1.772517       NaN
b  1.738035  3.684640 -0.050390
c  2.433281  5.163008  1.177045
d       NaN  5.442353  0.563873
```

## 方法总结

对包含分层索引的对象，还带有一个 `level` 参数。

| 函数     | 功能                                       |
| -------- | ------------------------------------------ |
| count    | Number of non-NA observations              |
| sum      | Sum of values                              |
| mean     | Mean of values                             |
| mad      | Mean absolute deviation                    |
| median   | Arithmetic median of values                |
| min      | Minimum                                    |
| max      | Maximum                                    |
| mode     | Mode                                       |
| abs      | Absolute Value                             |
| prod     | Product of values                          |
| std      | Bessel-corrected sample standard deviation |
| var      | Unbiased variance                          |
| sem      | Standard error of the mean                 |
| skew     | Sample skewness (3rd moment)               |
| kurt     | Sample kurtosis (4th moment)               |
| quantile | Sample quantile (value at %)               |
| cumsum   | Cumulative sum                             |
| cumprod  | Cumulative product                         |
| cummax   | Cumulative maximum                         |
| cummin   | Cumulative minimum                         |

需要注意，部分 NumPy 方法，如 `mean`, `std` 和 `sum` 默认排除 NA 值：

```py
In [87]: np.mean(df['one'])
Out[87]: 0.8110935116651192

In [88]: np.mean(df['one'].to_numpy())
Out[88]: nan
```

`Series.nunique()` 返回 `Series` 中unique non-NA值数目：

```py
In [89]: series = pd.Series(np.random.randn(500))

In [90]: series[20:500] = np.nan

In [91]: series[10:20] = 5

In [92]: series.nunique()
Out[92]: 11
```

## Value counts

`Series.value_counts(self, normalize=False, sort=True, ascending=False, bins=None, dorpna=True)`

`Series` 的 `value_counts()` 方法计算一维数组的直方图。也可以应用于常规数组，例如：

```py
In [117]: data = np.random.randint(0, 7, size=50)

In [118]: data
Out[118]:
array([6, 6, 2, 3, 5, 3, 2, 5, 4, 5, 4, 3, 4, 5, 0, 2, 0, 4, 2, 0, 3, 2,
       2, 5, 6, 5, 3, 4, 6, 4, 3, 5, 6, 4, 3, 6, 2, 6, 6, 2, 3, 4, 2, 1,
       6, 2, 6, 1, 5, 4])

In [119]: s = pd.Series(data)

In [120]: s.value_counts()
Out[120]:
6    10
2    10
4     9
5     8
3     8
0     3
1     2
dtype: int64

In [121]: pd.value_counts(data)
Out[121]:
6    10
2    10
4     9
5     8
3     8
0     3
1     2
dtype: int64
```

类似的，使用 `mode()` 方法可以获得 `Series` 或 `DataFrame` 中出现最频繁的值：

```py
In [122]: s5 = pd.Series([1, 1, 3, 3, 3, 5, 5, 7, 7, 7])

In [123]: s5.mode()
Out[123]:
0    3
1    7
dtype: int64

In [124]: df5 = pd.DataFrame({"A": np.random.randint(0, 7, size=50),
   .....:                     "B": np.random.randint(-10, 15, size=50)})
   .....:

In [125]: df5.mode()
Out[125]:
     A   B
0  1.0  -9
1  NaN  10
2  NaN  13
```
