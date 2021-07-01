# 数据的索引和选择

- [数据的索引和选择](#数据的索引和选择)
  - [简介](#简介)
  - [索引类型](#索引类型)
  - [索引运算符](#索引运算符)
    - [额外说明](#额外说明)
    - [范围切片](#范围切片)
  - [以属性访问](#以属性访问)
  - [以标签访问](#以标签访问)
    - [loc](#loc)
    - [loc 切片](#loc-切片)
    - [类型检查](#类型检查)
    - [at](#at)
    - [不推荐使用包含缺失值的标签列表](#不推荐使用包含缺失值的标签列表)
  - [以整数索引访问](#以整数索引访问)
    - [iloc](#iloc)
      - [Series.iloc](#seriesiloc)
      - [DataFrame.iloc](#dataframeiloc)
    - [iloc 切片](#iloc-切片)
      - [iloc 越界切片](#iloc-越界切片)
      - [DataFrame 越界切片](#dataframe-越界切片)
    - [iat](#iat)
  - [以 callable 访问](#以-callable-访问)
  - [组合使用位置和标签索引](#组合使用位置和标签索引)
  - [Boolean indexing](#boolean-indexing)
    - [使用布尔向量选择行](#使用布尔向量选择行)
    - [List 推导和 map](#list-推导和-map)
    - [组合使用](#组合使用)
  - [where](#where)
    - [选择行](#选择行)
  - [参考](#参考)

2020-04-30, 12:57
@Jiawei Mao
***

## 简介

pandas 对象的轴标签（axis labeling）信息有许多用途：

- 作为数据标签，方便数据分析、可视化和交互；
- 辅助数据对齐;
- 获取和设置数据集的子集。

下面讨论最后一条，即如何获取和修改 pandas 数据。重点放在 `Series` 和 `DataFrame` 的操作上。

Python 和 NumPy 的索引运算符 `[]` 及属性运算符 `.` 可用于快速访问 pandas 数据结构。但是，由于预先不知道要访问的数据类型，直接**使用标准运算符存在优化限制**。对于生产代码，建议使用本章中优化过的 pandas 数据访问方法。

## 索引类型

pandas 目前支持三种多轴（multi-axis）索引：

- `.loc`
- `.iloc`
- `[]`

这三种多轴索引都可以使用 `callable` 函数作为索引。

使用多轴选择方法获取值的语法如下（这里以 `.loc` 为例，对 `.iloc` 语法一样）

| 对象类型 | 索引 |
| --- | --- |
| Series    | `s.loc[indexer]` or `s.iloc[indexer]`                      |
| DataFrame | `df.loc[row_indexer, column_indexer]` or `df.loc[row, column]` |

所有的轴索引默认为 null 切片 `:`，即**未指定的索引默认为 `:`**，例如 `p.loc['a']` 等价于 `p.loc['a', :, :]`

## 索引运算符

`[]` 索引（即 `__getitem__`）主要用于低维切片。下面是 pandas 对象使用 `[]` 索引返回的对象：

| 类型        | 选择             | 返回类型              |
| ----------- | ---------------- | --------------------- |
| `Series`    | `series[label]`  | scalar value          |
| `DataFrame` | `frame[colname]` | 对应col名称的`Series` |

下面用一个简单的时间序列数据集解释该索引功能：

```py
In [1]: dates = pd.date_range('1/1/2000', periods=8)

In [2]: df = pd.DataFrame(np.random.randn(8, 4),
   ...:                   index=dates, columns=['A', 'B', 'C', 'D'])
   ...: 

In [3]: df
Out[3]: 
                   A         B         C         D
2000-01-01  0.469112 -0.282863 -1.509059 -1.135632
2000-01-02  1.212112 -0.173215  0.119209 -1.044236
2000-01-03 -0.861849 -2.104569 -0.494929  1.071804
2000-01-04  0.721555 -0.706771 -1.039575  0.271860
2000-01-05 -0.424972  0.567020  0.276232 -1.087401
2000-01-06 -0.673690  0.113648 -1.478427  0.524988
2000-01-07  0.404705  0.577046 -1.715002 -1.039268
2000-01-08 -0.370647 -1.157892 -1.344312  0.844885
```

- 使用 `[]` 索引

```py
In [4]: s = df['A'] # 返回 'A' 列数据的 Series
In [5]: s[dates[5]] # 选择 index=5 的 date 对应的值

Out[5]: -0.6736897080883706
```

- `[]` 接受 columns 列表

可以指定 column 列表选择数据。如果 `DataFrame` 不包含指定 column，抛出异常。使用该方式还能同时给多列赋值。

例如，选择 B、A 两列，将其赋值为 A、B，以交换 A, B 两列：

```py
In [6]: df
Out[6]: 
                   A         B         C         D
2000-01-01  0.469112 -0.282863 -1.509059 -1.135632
2000-01-02  1.212112 -0.173215  0.119209 -1.044236
2000-01-03 -0.861849 -2.104569 -0.494929  1.071804
2000-01-04  0.721555 -0.706771 -1.039575  0.271860
2000-01-05 -0.424972  0.567020  0.276232 -1.087401
2000-01-06 -0.673690  0.113648 -1.478427  0.524988
2000-01-07  0.404705  0.577046 -1.715002 -1.039268
2000-01-08 -0.370647 -1.157892 -1.344312  0.844885

In [7]: df[['B', 'A']] = df[['A', 'B']] # [] 中是 column 名称列表

In [8]: df
Out[8]: 
                   A         B         C         D
2000-01-01 -0.282863  0.469112 -1.509059 -1.135632
2000-01-02 -0.173215  1.212112  0.119209 -1.044236
2000-01-03 -2.104569 -0.861849 -0.494929  1.071804
2000-01-04 -0.706771  0.721555 -1.039575  0.271860
2000-01-05  0.567020 -0.424972  0.276232 -1.087401
2000-01-06  0.113648 -0.673690 -1.478427  0.524988
2000-01-07  0.577046  0.404705 -1.715002 -1.039268
2000-01-08 -1.157892 -0.370647 -1.344312  0.844885
```

该方法对于原地交换部分列十分有用。

### 额外说明

使用 `.loc` 和 `.iloc` 方法设置 `Series` 和 `DataFrame` 时会对齐所有 axes。

由于列对齐先于赋值，所有无法修改 `df`。例如：

```py
In [9]: df[['A', 'B']]
Out[9]: 
                   A         B
2000-01-01 -0.282863  0.469112
2000-01-02 -0.173215  1.212112
2000-01-03 -2.104569 -0.861849
2000-01-04 -0.706771  0.721555
2000-01-05  0.567020 -0.424972
2000-01-06  0.113648 -0.673690
2000-01-07  0.577046  0.404705
2000-01-08 -1.157892 -0.370647

In [10]: df.loc[:, ['B', 'A']] = df[['A', 'B']] # 无法交换两列

In [11]: df[['A', 'B']]
Out[11]: 
                   A         B
2000-01-01 -0.282863  0.469112
2000-01-02 -0.173215  1.212112
2000-01-03 -2.104569 -0.861849
2000-01-04 -0.706771  0.721555
2000-01-05  0.567020 -0.424972
2000-01-06  0.113648 -0.673690
2000-01-07  0.577046  0.404705
2000-01-08 -1.157892 -0.370647
```

可以发现 A,B 两列并没有交换，正确交换列的方式是采用原始值赋值。

```py
In [12]: df.loc[:, ['B', 'A']] = df[['A', 'B']].to_numpy()

In [13]: df[['A', 'B']]
Out[13]: 
                   A         B
2000-01-01  0.469112 -0.282863
2000-01-02  1.212112 -0.173215
2000-01-03 -0.861849 -2.104569
2000-01-04  0.721555 -0.706771
2000-01-05 -0.424972  0.567020
2000-01-06 -0.673690  0.113648
2000-01-07  0.404705  0.577046
2000-01-08 -0.370647 -1.157892
```

### 范围切片

`iloc` 是范围切片最稳健的方法。这里单纯介绍一下 pandas 可以用 `[]` 进行切片。

对 `Series` 来说，其语法与 ndarray 完全一样：

```py
In [27]: s[:5]
Out[27]: 
2000-01-01    0.469112
2000-01-02    1.212112
2000-01-03   -0.861849
2000-01-04    0.721555
2000-01-05   -0.424972
Freq: D, Name: A, dtype: float64

In [28]: s[::2]
Out[28]: 
2000-01-01    0.469112
2000-01-03   -0.861849
2000-01-05   -0.424972
2000-01-07    0.404705
Freq: 2D, Name: A, dtype: float64

In [29]: s[::-1]
Out[29]: 
2000-01-08   -0.370647
2000-01-07    0.404705
2000-01-06   -0.673690
2000-01-05   -0.424972
2000-01-04    0.721555
2000-01-03   -0.861849
2000-01-02    1.212112
2000-01-01    0.469112
Freq: -1D, Name: A, dtype: float64
```

- 也可以用来设置值

```py
In [30]: s2 = s.copy()

In [31]: s2[:5] = 0

In [32]: s2
Out[32]: 
2000-01-01    0.000000
2000-01-02    0.000000
2000-01-03    0.000000
2000-01-04    0.000000
2000-01-05    0.000000
2000-01-06   -0.673690
2000-01-07    0.404705
2000-01-08   -0.370647
Freq: D, Name: A, dtype: float64
```

对 `DataFrame`，使用 `[]` 切片提取**行**。该操作非常方便，因此是很常见的操作：

```py
In [33]: df[:3]
Out[33]: 
                   A         B         C         D
2000-01-01  0.469112 -0.282863 -1.509059 -1.135632
2000-01-02  1.212112 -0.173215  0.119209 -1.044236
2000-01-03 -0.861849 -2.104569 -0.494929  1.071804

In [34]: df[::-1]
Out[34]: 
                   A         B         C         D
2000-01-08 -0.370647 -1.157892 -1.344312  0.844885
2000-01-07  0.404705  0.577046 -1.715002 -1.039268
2000-01-06 -0.673690  0.113648 -1.478427  0.524988
2000-01-05 -0.424972  0.567020  0.276232 -1.087401
2000-01-04  0.721555 -0.706771 -1.039575  0.271860
2000-01-03 -0.861849 -2.104569 -0.494929  1.071804
2000-01-02  1.212112 -0.173215  0.119209 -1.044236
2000-01-01  0.469112 -0.282863 -1.509059 -1.135632
```

## 以属性访问

可以直接以属性的方式访问 `Series` 的 index，或 `DataFrame` 的 column。

限制条件：

- 索引必须是有效的 Python 识别符，如 `s.1` 这种不允许；
- 当属性名称和已有方法名冲突时不可用，如 `s.min` 不可用，此时可以用 `s['min']`；
- 与以下值冲突也不可用：`index`, `major_axis`, `minor_axis`, `items`；
- 在这些情况下，标准索引依然可用，如 `S['1']`, `S['min']`, `s['index']`。

实例：

- 例如：访问 Series 的 index='b'

```py
In [14]: sa = pd.Series([1, 2, 3], index=list('abc'))

In [15]: dfa = df.copy()
In [16]: sa.b # 将 index 作为属性访问
Out[16]: 2
```

- 访问 `DataFrame` 的 'A' 列：

```py
In [17]: dfa.A
Out[17]: 
2000-01-01    0.469112
2000-01-02    1.212112
2000-01-03   -0.861849
2000-01-04    0.721555
2000-01-05   -0.424972
2000-01-06   -0.673690
2000-01-07    0.404705
2000-01-08   -0.370647
Freq: D, Name: A, dtype: float64
```

- Series 属性赋值

```py
In [18]: sa.a = 5

In [19]: sa
Out[19]: 
a    5
b    2
c    3
dtype: int64
```

- DataFrame 属性赋值

```py
In [20]: dfa.A = list(range(len(dfa.index)))  # A 原来的值被覆盖

In [21]: dfa
Out[21]: 
            A         B         C         D
2000-01-01  0 -0.282863 -1.509059 -1.135632
2000-01-02  1 -0.173215  0.119209 -1.044236
2000-01-03  2 -2.104569 -0.494929  1.071804
2000-01-04  3 -0.706771 -1.039575  0.271860
2000-01-05  4  0.567020  0.276232 -1.087401
2000-01-06  5  0.113648 -1.478427  0.524988
2000-01-07  6  0.577046 -1.715002 -1.039268
2000-01-08  7 -1.157892 -1.344312  0.844885

In [22]: dfa['A'] = list(range(len(dfa.index)))  # 使用该语法创建新列

In [23]: dfa
Out[23]: 
            A         B         C         D
2000-01-01  0 -0.282863 -1.509059 -1.135632
2000-01-02  1 -0.173215  0.119209 -1.044236
2000-01-03  2 -2.104569 -0.494929  1.071804
2000-01-04  3 -0.706771 -1.039575  0.271860
2000-01-05  4  0.567020  0.276232 -1.087401
2000-01-06  5  0.113648 -1.478427  0.524988
2000-01-07  6  0.577046 -1.715002 -1.039268
2000-01-08  7 -1.157892 -1.344312  0.844885
```

- 可以使用 `dict` 给 `DataFrame` 的行赋值：

```py
In [24]: x = pd.DataFrame({'x': [1, 2, 3], 'y': [3, 4, 5]})

In [25]: x.iloc[1] = {'x': 9, 'y': 99}

In [26]: x
Out[26]: 
   x   y
0  1   3
1  9  99
2  3   5
```

可以通过属性访问、修改 Series 的值和 `DataFrame` 的列；不过要小心使用，因为通过属性创建新列，创建的属性，而不是一个新的 column，在 0.21.0 之后，使用该语法抛出 `UserWarning`：

```py
In [1]: df = pd.DataFrame({'one': [1., 2., 3.]})
In [2]: df.two = [4, 5, 6]
UserWarning: Pandas doesn't allow Series to be assigned into nonexistent columns - see https://pandas.pydata.org/pandas-docs/stable/indexing.html#attribute_access
In [3]: df
Out[3]:
   one
0  1.0
1  2.0
2  3.0
```

## 以标签访问

> 设置操作返回副本还是引用取决于上下文。

pandas 提供了一套基于标签的索引：

- 每个请求的标签必须在索引中，否则抛出 `KeyError`；
- 在进行切片时，首尾索引都会包含在结果中；
- 整数是有效的标签，但它们作为标签使用，而不是位置。

### loc

`.loc` 是基于标签的主要访问方法，通过标签或 boolean 数组访问多行或多列数据，其有效输入包括：

- 单个标签，如 `5` 或 `'a'`（此处 `5` 按照标签解析，而非位置）；
- 标签数组或列表，如 `['a', 'b', 'c']`；
- 切片标签，如 `'a':'f'`（包含首尾元素）；
- boolean 数组，`NA` 值以 `False` 处理；
- 包含单个参数（调用的 `Series` 或 `DataFrame`）的`callable` 函数，该函数返回上面索引形式的一种。

当对应项找不到时，`.loc` 抛出 `KeyError`。

例如，对 `Series`:

- `s1.loc['c':]`, 选择 `Series` 'c' 及其后所有数据
- `s1.loc['b']`, 选择标签为 'b' 的单个数据

```py
In [38]: s1 = pd.Series(np.random.randn(6), index=list('abcdef'))

In [39]: s1
Out[39]: 
a    1.431256
b    1.340309
c   -1.170299
d   -0.226169
e    0.410835
f    0.813850
dtype: float64

In [40]: s1.loc['c':]
Out[40]: 
c   -1.170299
d   -0.226169
e    0.410835
f    0.813850
dtype: float64

In [41]: s1.loc['b']
Out[41]: 1.3403088497993827
```

- `s1.loc['c':] = 0` 设置 'c' 及其后所有数据为 0

```py
In [42]: s1.loc['c':] = 0

In [43]: s1
Out[43]: 
a    1.431256
b    1.340309
c    0.000000
d    0.000000
e    0.000000
f    0.000000
dtype: float64
```

对 `DataFrame`:

- `df1.loc[['a', 'b', 'd'], :]`, 选择 'a', 'b', 'd' 行，所有列

```py
In [44]: df1 = pd.DataFrame(np.random.randn(6, 4),
   ....:                    index=list('abcdef'),
   ....:                    columns=list('ABCD'))
   ....: 

In [45]: df1
Out[45]: 
          A         B         C         D
a  0.132003 -0.827317 -0.076467 -1.187678
b  1.130127 -1.436737 -1.413681  1.607920
c  1.024180  0.569605  0.875906 -2.211372
d  0.974466 -2.006747 -0.410001 -0.078638
e  0.545952 -1.219217 -1.226825  0.769804
f -1.281247 -0.727707 -0.121306 -0.097883

In [46]: df1.loc[['a', 'b', 'd'], :]
Out[46]: 
          A         B         C         D
a  0.132003 -0.827317 -0.076467 -1.187678
b  1.130127 -1.436737 -1.413681  1.607920
d  0.974466 -2.006747 -0.410001 -0.078638
```

- `df1.loc['d':, 'A':'C']`，选择 'd' 行，'A' 到 'C' 列。

```py
In [47]: df1.loc['d':, 'A':'C']
Out[47]: 
          A         B         C
d  0.974466 -2.006747 -0.410001
e  0.545952 -1.219217 -1.226825
f -1.281247 -0.727707 -0.121306
```

- `df1.loc['a']`，选择 'a' 行，等价于 `df.xs('a')`

```py
In [48]: df1.loc['a']
Out[48]: 
A    0.132003
B   -0.827317
C   -0.076467
D   -1.187678
Name: a, dtype: float64
```

- 使用 boolean 数组选择，`df1.loc[:, df1.loc['a'] > 0]`，选择 'a' 行值大于 0 的所有列。

```py
In [49]: df1.loc['a'] > 0
Out[49]: 
A     True
B    False
C    False
D    False
Name: a, dtype: bool

In [50]: df1.loc[:, df1.loc['a'] > 0]
Out[50]: 
          A
a  0.132003
b  1.130127
c  1.024180
d  0.974466
e  0.545952
f -1.281247
```

- `df1.loc['a', 'A']` 选择 'a' 行 'A' 列处的值，等价于 `df1.at['a', 'A']`

```py
# this is also equivalent to ``df1.at['a','A']``
In [54]: df1.loc['a', 'A']
Out[54]: 0.13200317033032932
```

### loc 切片

使用 `.loc` 进行切片，包含首尾元素。例如：

```py
In [52]: s = pd.Series(list('abcde'), index=[0, 3, 2, 5, 4])

In [53]: s.loc[3:5] # 此处 3 和 5 都是标签
Out[53]:
3    b
2    c
5    d
dtype: object
```

如果首尾 index 至少有一个越界，但是 index 排序过，并且可以和首尾的 label 对比，则切片依然可以执行：

```py
In [54]: s.sort_index()
Out[54]:
0    a
2    c
3    b
4    e
5    d
dtype: object

In [55]: s.sort_index().loc[1:6]
Out[55]:
2    c
3    b
4    e
5    d
dtype: object
```

如果 index 没有排序，且存在越界情况，则抛出错误。例如，上例中如果没有排序直接调用 `s.loc[1:6]`，就会抛出 `KeyError`。

### 类型检查

对不兼容的 index 类型，`.loc` 会抛出 `TypeError`。例如：

```py
In [35]: dfl = pd.DataFrame(np.random.randn(5, 4),
   ....:                    columns=list('ABCD'),
   ....:                    index=pd.date_range('20130101', periods=5))
   ....:

In [36]: dfl
Out[36]:
                   A         B         C         D
2013-01-01  1.075770 -0.109050  1.643563 -1.469388
2013-01-02  0.357021 -0.674600 -1.776904 -0.968914
2013-01-03 -1.294524  0.413738  0.276662 -0.472035
2013-01-04 -0.013960 -0.362543 -0.006154 -0.923061
2013-01-05  0.895717  0.805244 -1.206412  2.565646
```

```py
In [4]: dfl.loc[2:3]
TypeError: cannot do slice indexing on <class 'pandas.tseries.index.DatetimeIndex'> with these indexers [2] of <type 'int'>
```

对字符串类型切片，如果可以转换为对应 index 类型，则可以正常工作：

```py
In [37]: dfl.loc['20130102':'20130104']
Out[37]:
                   A         B         C         D
2013-01-02  0.357021 -0.674600 -1.776904 -0.968914
2013-01-03 -1.294524  0.413738  0.276662 -0.472035
2013-01-04 -0.013960 -0.362543 -0.006154 -0.923061
```

### at

### 不推荐使用包含缺失值的标签列表

在早期版本，使用 `.loc[list-of-labels]` 语法，只要其中有一个 key 能找到，就能执行。在 1.0.0 版本之后，只要有一个 key 找不到，就抛出 `KeyError`。推荐使用 [.reindex()](reindex.md) 方法应对有缺失值的情况。

例如：

```py
In [103]: s = pd.Series([1, 2, 3])

In [104]: s
Out[104]: 
0    1
1    2
2    3
dtype: int64
```

- 所有标签都存在不影响

```py
In [105]: s.loc[[1, 2]]
Out[105]: 
1    2
2    3
dtype: int64
```

- 在 1.0.0 之前可以执行如下操作

```py
In [4]: s.loc[[1, 2, 3]]
Out[4]:
1    2.0
2    3.0
3    NaN
dtype: float64
```

- 现在这样操作抛出错误

```py
In [4]: s.loc[[1, 2, 3]]
Passing list-likes to .loc with any non-matching elements will raise
KeyError in the future, you can use .reindex() as an alternative.

See the documentation here:
https://pandas.pydata.org/pandas-docs/stable/indexing.html#deprecate-loc-reindex-listlike

Out[4]:
1    2.0
2    3.0
3    NaN
dtype: float64
```

## 以整数索引访问

> 对设置操作，返回副本还是引用取决于上下文。

pandas 提供了一组基于整数索引操作的方法。其语法严格遵循 Python 和 NumPy 切片语法。

- 索引以 0 开始；
- 对切片，包括起始索引，排除结束索引；
- 使用非整数索引，抛出 `IndexError`。

`iloc` 是基于整数索引访问的主要方法。

### iloc

```py
property Series.iloc
```

`.iloc` 基于整数位置（0 到 length-1）使用，也能和布尔数组一起使用。

索引超出范围时 `.iloc` 抛出 `IndexError`，但是在切片时允许索引越界，这与 Python 及 NumPy 切片一致。

`.iloc` 属性是基于索引访问的主要方法，有效输入包括：

- 整数，如 `5`；
- 整数列表或数组，如 `[4, 3, 0]`；
- slice 对象，如 `1 : 7`；
- boolean 数组，`NA` 值以 `False` 处理；
- `callable` 对象，包含单个参数（调用该方法的 `Series` 或 `DataFrame`）的 `callable` 函数，该函数返回上面索引形式的一种。

#### Series.iloc

- 选择单个值

```py
s1 = pd.Series([3, 5, 1])
assert s1.iloc[0] == 3
assert s1.iloc[2] == 1
```

- 基于索引切片

```py
In [61]: s1 = pd.Series(np.random.randn(5), index=list(range(0, 10, 2)))

In [62]: s1
Out[62]: 
0    0.695775
2    0.341734
4    0.959726
6   -1.110336
8   -0.619976
dtype: float64

In [63]: s1.iloc[:3]
Out[63]: 
0    0.695775
2    0.341734
4    0.959726
dtype: float64

In [64]: s1.iloc[3]
Out[64]: -1.110336102891167
```

- 使用索引列表选择

```py
s1 = pd.Series([1, 2, 3, 4])
s2 = s1.iloc[[1, 3]]
assert_array_equal(s2, np.array([2, 4]))
```

- 使用索引设置值

`iloc` 语法也可用来设置值。

```py
In [65]: s1.iloc[:3] = 0

In [66]: s1
Out[66]: 
0    0.000000
2    0.000000
4    0.000000
6   -1.110336
8   -0.619976
dtype: float64
```

```py
s1 = pd.Series([1, 2, 3])
s1.iloc[:2] = 0
pd.testing.assert_series_equal(s1, pd.Series([0, 0, 3]))
```

#### DataFrame.iloc

```py
In [67]: df1 = pd.DataFrame(np.random.randn(6, 4),
   ....:                    index=list(range(0, 12, 2)),
   ....:                    columns=list(range(0, 8, 2)))
   ....: 

In [68]: df1
Out[68]: 
           0         2         4         6
0   0.149748 -0.732339  0.687738  0.176444
2   0.403310 -0.154951  0.301624 -2.179861
4  -1.369849 -0.954208  1.462696 -1.743161
6  -0.826591 -0.345352  1.314232  0.690579
8   0.995761  2.396780  0.014871  3.357427
10 -0.317441 -1.236269  0.896171 -0.487602
```

- 切片选择

```py
In [69]: df1.iloc[:3]
Out[69]: 
          0         2         4         6
0  0.149748 -0.732339  0.687738  0.176444
2  0.403310 -0.154951  0.301624 -2.179861
4 -1.369849 -0.954208  1.462696 -1.743161

In [70]: df1.iloc[1:5, 2:4]
Out[70]: 
          4         6
2  0.301624 -2.179861
4  1.462696 -1.743161
6  1.314232  0.690579
8  0.014871  3.357427
```

- 使用整数列表参数选择

```py
In [71]: df1.iloc[[1, 3, 5], [1, 3]]
Out[71]: 
           2         6
2  -0.154951 -2.179861
6  -0.345352  0.690579
10 -1.236269 -0.487602
```

```py
In [72]: df1.iloc[1:3, :]
Out[72]: 
          0         2         4         6
2  0.403310 -0.154951  0.301624 -2.179861
4 -1.369849 -0.954208  1.462696 -1.743161
```

```py
In [73]: df1.iloc[:, 1:3]
Out[73]: 
           2         4
0  -0.732339  0.687738
2  -0.154951  0.301624
4  -0.954208  1.462696
6  -0.345352  1.314232
8   2.396780  0.014871
10 -1.236269  0.896171
```

- 提供两个索引获得单个值，等价于 `df.iat[1, 1]`

```py
# this is also equivalent to ``df1.iat[1,1]``
In [74]: df1.iloc[1, 1]
Out[74]: -0.1549507744249032
```

```py
df = pd.DataFrame({"col1": [1, 2],
                    "col2": [3, 4]},
                  index=["row1", "row2"])
assert df.iloc[1, 1] == 4
assert df.iloc[0, 1] == 3
```

- 如果只提供一个索引，表示行，等价于 `df.xs(1)`

获取的行，以 `Series` 对象返回。

```py
In [75]: df1.iloc[1] # 第二行
Out[75]: 
0    0.403310
2   -0.154951
4    0.301624
6   -2.179861
Name: 2, dtype: float64
```

```py
df = pd.DataFrame({"col1": [1, 2],
                    "col2": [3, 4]},
                  index=["row1", "row2"])
s1 = df.iloc[1] # 第二行
assert_series_equal(s1, pd.Series(
    [2, 4], name="row2", index=['col1', 'col2']))
```

- 选择

### iloc 切片

- Series 切片

```py
s1 = pd.Series([1, 3, 5, 7, 11])
s2 = s1.iloc[:3]
pd.testing.assert_series_equal(s2, pd.Series([1, 3, 5]))
```

- DataFrame 切片

```py
df = pd.DataFrame({"col1": [1, 2, 3],
                    "col2": [4, 5, 6],
                    "col3": [7, 8, 9]},
                    index=["row1", "row2", "row3"])
```

选择前两行：

```py
df2 = df.iloc[:2] # 前两行
assert_frame_equal(df2, pd.DataFrame({
    "col1": [1, 2], "col2": [4, 5], "col3": [7, 8],
    index=["row1", "row2"]}))
```

选择二三行，二三列：

```py
df3 = df.iloc[1:3, 1:3]
assert_frame_equal(df3, pd.DataFrame({
    "col2": [4, 5], "col3": [7, 8],
    index=['row2', 'row3']
}))
```

#### iloc 越界切片

> 越界只在切片中允许，对索引或索引列表中，越界抛出 `IndexError`

```py
# 在 Python/Numpy 中切片索引允许越界
In [76]: x = list('abcdef')

In [77]: x
Out[77]: ['a', 'b', 'c', 'd', 'e', 'f']

In [78]: x[4:10] # 单边越界
Out[78]: ['e', 'f']

In [79]: x[8:10] # 双边越界
Out[79]: []

In [80]: s = pd.Series(x)

In [81]: s
Out[81]: 
0    a
1    b
2    c
3    d
4    e
5    f
dtype: object

In [82]: s.iloc[4:10] # 单边越界
Out[82]: 
4    e
5    f
dtype: object

In [83]: s.iloc[8:10] # 双边越界，返回空 Series
Out[83]: Series([], dtype: object)
```

#### DataFrame 越界切片

DataFrame 处理方式一样，完全越界返回空的 DataFrame，单边越界则到对应 axis 末尾。

```py
In [79]: dfl = pd.DataFrame(np.random.randn(5, 2), columns=list('AB'))

In [80]: dfl
Out[80]:
          A         B
0 -0.082240 -2.182937
1  0.380396  0.084844
2  0.432390  1.519970
3 -0.493662  0.600178
4  0.274230  0.132885

In [81]: dfl.iloc[:, 2:3] # 双边越界，返回空 DataFrame
Out[81]:
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 4]

In [82]: dfl.iloc[:, 1:3] # 单边越界，从第2列到最后一列，不过这里最大直到第2列
Out[82]:
          B
0 -2.182937
1  0.084844
2  1.519970
3  0.600178
4  0.132885

In [83]: dfl.iloc[4:6] # 4 到 5 行，由于最大行索引为4，所以只有第4行
Out[83]:
         A         B
4  0.27423  0.132885
```

如果不是切片，而是索引列表，则任意索引越界，抛出 `IndexError`：

```py
>>> dfl.iloc[[4, 5, 6]]
IndexError: positional indexers are out-of-bounds

>>> dfl.iloc[:, 4]
IndexError: single positional indexer is out-of-bounds
```

### iat

访问指定位置（行/列）的单个值：

```py
property Series.iat
```

与 `iloc` 类似，两者都基于整数索引查找值。如果只需要查询、设置单个值，就使用 `iat`。例如：

```py
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
```

## 以 callable 访问

`.loc`, `.iloc` 和 `[]` 索引都接受 `callable` 作为索引参数。`callable` 必须是返回有效索引的函数。

```py
In [89]: df1 = pd.DataFrame(np.random.randn(6, 4),
   ....:                    index=list('abcdef'),
   ....:                    columns=list('ABCD'))
   ....: 

In [90]: df1
Out[90]: 
          A         B         C         D
a -0.023688  2.410179  1.450520  0.206053
b -0.251905 -2.213588  1.063327  1.266143
c  0.299368 -0.863838  0.408204 -1.048089
d -0.025747 -0.988387  0.094055  1.262731
e  1.289997  0.082423 -0.055758  0.536580
f -0.489682  0.369374 -0.034571 -2.484478

In [91]: df1.loc[lambda df: df['A'] > 0, :] # lambda 函数
Out[91]: 
          A         B         C         D
c  0.299368 -0.863838  0.408204 -1.048089
e  1.289997  0.082423 -0.055758  0.536580

In [92]: df1.loc[:, lambda df: ['A', 'B']]
Out[92]: 
          A         B
a -0.023688  2.410179
b -0.251905 -2.213588
c  0.299368 -0.863838
d -0.025747 -0.988387
e  1.289997  0.082423
f -0.489682  0.369374

In [93]: df1.iloc[:, lambda df: [0, 1]]
Out[93]: 
          A         B
a -0.023688  2.410179
b -0.251905 -2.213588
c  0.299368 -0.863838
d -0.025747 -0.988387
e  1.289997  0.082423
f -0.489682  0.369374

In [94]: df1[lambda df: df.columns[0]]
Out[94]: 
a   -0.023688
b   -0.251905
c    0.299368
d   -0.025747
e    1.289997
f   -0.489682
Name: A, dtype: float64
```

在 `Series` 用于一样：

```py
In [95]: df1['A'].loc[lambda s: s > 0]
Out[95]: 
c    0.299368
e    1.289997
Name: A, dtype: float64
```

使用这种索引形式，可以执行串联操作：

```py
In [96]: bb = pd.read_csv('data/baseball.csv', index_col='id')

In [97]: (bb.groupby(['year', 'team']).sum()
   ....:    .loc[lambda df: df['r'] > 100])
   ....: 
Out[97]: 
           stint    g    ab    r    h  X2b  X3b  hr    rbi    sb   cs   bb     so   ibb   hbp    sh    sf  gidp
year team                                                                                                      
2007 CIN       6  379   745  101  203   35    2  36  125.0  10.0  1.0  105  127.0  14.0   1.0   1.0  15.0  18.0
     DET       5  301  1062  162  283   54    4  37  144.0  24.0  7.0   97  176.0   3.0  10.0   4.0   8.0  28.0
     HOU       4  311   926  109  218   47    6  14   77.0  10.0  4.0   60  212.0   3.0   9.0  16.0   6.0  17.0
     LAN      11  413  1021  153  293   61    3  36  154.0   7.0  5.0  114  141.0   8.0   9.0   3.0   8.0  29.0
     NYN      13  622  1854  240  509  101    3  61  243.0  22.0  4.0  174  310.0  24.0  23.0  18.0  15.0  48.0
     SFN       5  482  1305  198  337   67    6  40  171.0  26.0  7.0  235  188.0  51.0   8.0  16.0   6.0  41.0
     TEX       2  198   729  115  200   40    4  28  115.0  21.0  4.0   73  140.0   4.0   5.0   2.0   8.0  16.0
     TOR       4  459  1408  187  378   96    2  58  223.0   4.0  2.0  190  265.0  16.0  12.0   4.0  16.0  38.0
```

## 组合使用位置和标签索引

如果你想获得 'A' 列的第 0 和 第 2 个元素：

```py
In [98]: dfd = pd.DataFrame({'A': [1, 2, 3],
   ....:                     'B': [4, 5, 6]},
   ....:                    index=list('abc'))
   ....: 

In [99]: dfd
Out[99]: 
   A  B
a  1  4
b  2  5
c  3  6

In [100]: dfd.loc[dfd.index[[0, 2]], 'A']
Out[100]: 
a    1
c    3
Name: A, dtype: int64
```

- 对多级索引，使用 `.get_indexer`

```py
In [102]: dfd.iloc[[0, 2], dfd.columns.get_indexer(['A', 'B'])]
Out[102]: 
   A  B
a  1  4
c  3  6
```

- 也可以使用 `.loc` 实现

```py
In [101]: dfd.iloc[[0, 2], dfd.columns.get_loc('A')]
Out[101]: 
a    1
c    3
Name: A, dtype: int64
```

## Boolean indexing

布尔向量主要用于过滤数据。

| 操作符 | 对应关键字 |
| ------ | ---------- |
| `|`    | or         |
| `&`    | and        |
| `~`    | not        |

这些操作需要用括号进行分组，因为默认情况下，`df['A'] > 2 & df['B'] < 3` 会按照 `df['A'] > (2 & df['B']) < 3`，而并非 `(df['A > 2) & (df['B'] < 3)`。

使用布尔向量索引 `Series` 和 `ndarray` 完全相同：

```py
s = pd.Series(range(-3, 4))
s1 = s[s > 0]

np.testing.assert_array_equal(s1.values, np.array([1, 2, 3]))
```

- 或

```py
s = pd.Series(range(-3, 4))

s2 = s[(s < -1) | (s > 0.5)]
np.testing.assert_array_equal(s2.values, np.array([-3, -2, 1, 2, 3]))
```

- 非

```py
s = pd.Series(range(-3, 4))

s3 = s[~(s < 0)]
np.testing.assert_array_equal(s3.values, np.array([0, 1, 2, 3]))
```

### 使用布尔向量选择行

可以使用和 `DataFrame` 索引等长（即和 DataFrame 行数相同）的布尔向量选择 rows，例如，使用 DataFrame 的某一列构建的布尔向量：

```py
df = pd.DataFrame({'A': [1, 2, 3], 'B': [7, 8, 9]})
df1 = df[df['A'] > 1]
np.array_equal(df1.values, pd.DataFrame({"A": [2, 3], "B": [8, 9]}).values)
```

### List 推导和 map

`Series` 的 List 推导 (List comprehensions) 和 `map` 方法可以生成更复杂的规则。

```py
df = pd.DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
                     'b': ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
                     'c': [1, 2, 3, 4, 5, 6, 7]})
criterion = df['a'].map(lambda x: x.startswith('t')) # 只保留 a 中以 't' 开头的行
df1 = df[criterion]
assert_frame_equal(df1.reset_index(drop=True),
                     pd.DataFrame({'a': ['two', 'three', 'two'],
                                   'b': ['y', 'x', 'y'],
                                   'c': [3, 4, 5]}))
```

用 List 实现相同功能（更慢）

```py
df[[x.startswith('t') for x in df['a']]]
```

Out:

```cmd
       a  b         c
2    two  y -0.545678
3  three  x  1.323958
4    two  y -1.561873
```

- 多重规则

```py
df[criterion & (df['b'] == 'x')]
```

Out:

```cmd
       a  b         c
3  three  x  0.378387
```

### 组合使用

将 boolean vector 和选择方法 `Selection by Label`, `Selection by Position` 以及 `Advanced Indexing` 结合使用，可以实现多 axis 选择。

例如：

```py
df.loc[criterion & (df['b'] == 'x'), 'b': 'c']
```

输出：

```cmd
   b         c
3  x  0.155084
```

## where

使用布尔向量从 `Series` 中选择一般返回数据的子集。为了保证选择的结果和原数据具有相同的 shape，可以使用 `Series` 和 `DataFrame` 的 `where` 方法。

where 方法签名：

```py
Series.where(self,cond,other=nan,inplace=False,axis=None,level=None,errors='raise',try_cast=False)
```

对`cond` 为 False 的数值，用 `other` 替换其值。

|参数|类型|说明|
|---|---|---|
|`cond`|bool Series/DataFrame, array-like, or callable|如果 `cond` 为 True，保留原值；否则以 `other` 替换。如果 `cond` 为 `callable`，则根据 Series/DataFrame 的值进行计算，返回值必须为 boolean 类型的 `Series`/`DataFrame` 或数组。`callable` 不能修改输入的 Series/DataFrame|
|`other`|scalar, Series/DataFrame, or callable|对 `cond` 为 False 的数据，以 `other` 替代。如果 `other` 为 `callable` 类型，则根据原数据进行计算，返回值必须为 scalar, Series/DataFrame 类型。callable 不允许修改输入 Series/DataFrame|
|`inplace`|bool, default False|是否对数据进行原位操作|
|`axis`|int, default None|是否对齐 axis|
|`level`|int, default None|Alignment level if needed|
|`errors`|str, {‘raise’, ‘ignore’}, default ‘raise’|该参数不影响结果，结果总会转换为合适的 dtype。(1) 'raise'，抛出异常。(2) 'ignore'，抑制异常。|
|`try_cast`|bool, default False|尝试将结果转换为输入类型|

返回：和调用者相同的类型。

> `DataFrame.where()` 签名和 `numpy.where()` 略有不同，`df1.where(m, df2)` 基本上等价于 `np.where(m, df1, df2)`。

### 选择行

- 只返回选择的行

```py
In [182]: s = pd.Series(range(5))
In [183]: s[s > 0]
Out[183]: 
3    1
2    2
1    3
0    4
dtype: int64
```

- 默认替换值为 nan

使用 `where` 替换不匹配值

```py
s = pd.Series(range(5))
s1 = s.where(s > 0)
```

Out:

```cmd
0    NaN
1    1.0
2    2.0
3    3.0
4    4.0
dtype: float64
```

使用 boolean 从 `DataFrame` 选择值目前也保持 shape。底层就是使用 `where` 实现的，下面代码等价于 `df.where(df < 0)`：

```py
In [185]: df[df < 0]
Out[185]: 
                   A         B         C         D
2000-01-01 -2.104139 -1.309525       NaN       NaN
2000-01-02 -0.352480       NaN -1.192319       NaN
2000-01-03 -0.864883       NaN -0.227870       NaN
2000-01-04       NaN -1.222082       NaN -1.233203
2000-01-05       NaN -0.605656 -1.169184       NaN
2000-01-06       NaN -0.948458       NaN -0.684718
2000-01-07 -2.670153 -0.114722       NaN -0.048048
2000-01-08       NaN       NaN -0.048788 -0.808838
```

## 参考

- https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
