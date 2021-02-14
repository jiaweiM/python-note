# 数据的索引和选择

- [数据的索引和选择](#数据的索引和选择)
  - [简介](#简介)
    - [.loc](#loc)
  - [索引基础](#索引基础)
    - [额外说明](#额外说明)
  - [按属性访问](#按属性访问)

2020-04-30, 12:57
***

## 简介

pandas 对象的轴标签（axis labeling）信息有许多用途：

- 作为数据标签，方便数据分析、可视化和交互。
- 辅助数据对齐。
- 方便直观地获取和设置数据集的子集。

下面讨论最后一条，即切片以及获取、设置 pandas 数据。重点放在 `Series` 和 `DataFrame` 上。

> Python 和 NumPy 索引运算符 `[]` 及属性运算符 `.` 可用于快速访问 pandas 数据结构的功能。不过，由于预先不知道要访问的数据类型，直接使用标准运算符存在优化限制。对于生产代码，建议使用本章中优化过的 pandas 数据访问方法。

pandas 目前支持三种多轴（multi-axis）索引：

- `.loc`
- `.iloc`
- `[]`

这三种多轴索引都可以使用 `callable` 函数作为索引。

使用多轴选择方法获取值的语法如下（这里以 `.loc` 为例，对 `.iloc` 语法一样）

| 对象类型  | 索引                                  |
| --------- | ------------------------------------- |
| Series    | `s.loc[indexer]`                      |
| DataFrame | `df.loc[row_indexer, column_indexer]` |

所有的轴索引默认为 null 切片 `:`，即**未指定的索引默认为 `:`**，例如 `p.loc['a']` 等价于 `p.loc['a', :, :]`

### .loc

`.loc` 基于标签，但也可以和布尔数组一起使用。

当对应项找不到时，`.loc` 抛出 `KeyError`。

`.loc` 允许的输入：

- 单个标签，如 `5` 或 `a`（这里的 `5` 是按照索引标签解析，而不是索引位置）
- 标签列表或数组，如 `['a', 'b', 'c']`
- 切片标签如 `'a':'f'` （和 Python 不同，这里起点和终点都包含在结果中）
- 布尔数组
- 包含单个参数（调用的 `Series` 或 `DataFrame`）的`callable` 函数，该函数返回上面索引形式的一种。

## 索引基础

`[]` 索引（即 `__getitem__`）主要用于低维切片。下面是pandas 对象使用 `[]` 索引返回的对象：

| 类型        | 选择             | 返回类型              |
| ----------- | ---------------- | --------------------- |
| `Series`    | `series[label]`  | scalar value          |
| `DataFrame` | `frame[colname]` | 对应col名称的`Series` |

下面用一个简单的时间序列数据集解释该索引功能：

```py
dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.default_rng().standard_normal(size=(8, 4)),
                  index=dates, columns=['A', 'B', 'C', 'D'])
df
```

Out:

![data](images/2020-03-13-14-35-54.png)

- 使用 `[]` 索引

```py
s = df['A'] # 选择 A 列 `Series` 对象
s[dates[5]] # 选择 index=5 的 date 对应的值
```

Out:

```cmd
-0.4583529612763085
```

- `[]` 接受 columns 列表

如果 `DataFrame` 不包含指定 column，抛出异常。使用该方式还能给多个 column 赋值。

例如，选择 B, A 两列，将其赋值为 A, B,达到交换 A, B 两列的目的：

```py
df[['B', 'A']] = df[['A', 'B']]
df
```

Out:

![swap](images/2020-03-13-14-48-26.png)

该方法对于原地交换部分列十分有用。

### 额外说明

`.loc` 和 `.iloc` 方法在设置 `Series` 和 `DataFrame` 时会对齐所有 axes。

由于列对齐先于赋值，所有无法修改 `df`。例如：

```py
df[['A', 'B']]
```

Out:

![AB](images/2020-03-13-15-10-03.png)

```py
df.loc[:, ['B', 'A']] = df[['A', 'B']]
df[['A', 'B']]
```

Out:

![AB](images/2020-03-13-15-10-39.png)

可以发现 A,B 并没有交换值，交换列的正确方式是采用原始值赋值。

```py
df.loc[:, ['B', 'A']] = df[['A', 'B']].to_numpy()
df[['A', 'B']]
```

Out:

![BA](images/2020-03-13-15-13-09.png)

## 按属性访问

访问 `Series` 的 index，或 `DataFrame` 的 column可以直接采用属性方式。

- 例如：访问 Series 的 index='b'

```py
sa = pd.Series([1, 2, 3], index=list('abc'))
sa.b
```

Out:

```cmd
2
```

- 访问 `DataFrame` 的 'A' 列：

```py
dfa = df.copy()
dfa.A
```

Out:

```cmd
2000-01-01    0.619623
2000-01-02   -0.846276
2000-01-03   -0.630945
2000-01-04    1.367082
2000-01-05   -0.950411
2000-01-06   -0.920991
2000-01-07    0.775974
2000-01-08   -0.600853
Freq: D, Name: A, dtype: float64
```

- Series 属性赋值

```py
sa.a = 5
sa
```

Out:

```cmd
a    5
b    2
c    3
dtype: int64
```

- DataFrame 属性赋值

```py
dfa.A = list(range(len(dfa.index))) # A 原来的值被覆盖
dfa
```

Out:

![dataframe](images/2020-03-13-19-48-00.png)
