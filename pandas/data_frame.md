# DataFrame

- [DataFrame](#dataframe)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [属性](#%e5%b1%9e%e6%80%a7)
    - [size](#size)
    - [shape](#shape)
  - [创建 `DataFrame`](#%e5%88%9b%e5%bb%ba-dataframe)
    - [`Series` dict](#series-dict)
      - [为 dict 提供 index](#%e4%b8%ba-dict-%e6%8f%90%e4%be%9b-index)
      - [为 dict 提供 index 和 columns](#%e4%b8%ba-dict-%e6%8f%90%e4%be%9b-index-%e5%92%8c-columns)
    - [通过 `ndarray` 或 list 的 `dict` 创建](#%e9%80%9a%e8%bf%87-ndarray-%e6%88%96-list-%e7%9a%84-dict-%e5%88%9b%e5%bb%ba)
    - [创建时提供 index](#%e5%88%9b%e5%bb%ba%e6%97%b6%e6%8f%90%e4%be%9b-index)
    - [通过 `ndarray` 创建](#%e9%80%9a%e8%bf%87-ndarray-%e5%88%9b%e5%bb%ba)
  - [DataFrame 操作](#dataframe-%e6%93%8d%e4%bd%9c)
    - [索引](#%e7%b4%a2%e5%bc%95)
    - [DataFrame.sort_values](#dataframesortvalues)
    - [DataFrame.sort_index](#dataframesortindex)
    - [DataFrame.pivot_table](#dataframepivottable)

## 简介

`DataFrame` 在 pandas 中是二维带标签数组，你可以将其看做 Excel 表格、SQL表格或值类型为 `Series` 的字典。`DataFrame` 不同列的数据类型可以不同，在Pandas 中使用最为广泛。另外：

- 每列的数据类型相同
- 每行包含索引 0…n

如下所示：

![](images/2019-08-28-15-19-03.png)

如果将 Dates 设置为 index:

![](images/2019-08-28-15-19-25.png)

## 属性

| 属性  | 说明                            |
| ----- | ------------------------------- |
| index | DataFrame 的索引（行标签）      |
| size  | 元素个数                        |
| shape | 返回表示 DataFrame 维数的 tuple |

### size

返回对象中元素个数。对 `Series` 返回行数，对 `DataFrame`，返回行数乘以列数。

例如：

```py
def test_series_size():
    s = pd.Series({'a': 1, 'b': 2, 'c': 3})
    assert s.size == 3


def test_dataframe_size():
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    assert df.size == 4
```

### shape

返回表示 DataFrame 维度的 tuple 对象。例如：

```py
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
assert df.shape == (2, 2)
df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4], "col3": [5, 6]})
assert df.shape == (2, 3)
```

## 创建 `DataFrame`

构造函数：

```py
DataFrame(data, index=, columns= )
```

`DataFrame` 接受多种类型的输入：

- 1D `ndarray`、lists、dicts 或 `Series`  的 dict
- 2D `numpy.ndarray`
- `Series`
- 其它 `DataFrame`

除了数据，创建 `DataFrame` 时还可以设置 index (行标签)和 columns (列标签)。如果创建时提供了 index / columns，则为了保证标签对应，不符合要求的数据被舍弃。

> 如果输入数据为 `dict` 类型，且没有指定 `columns`，则 `DataFrame` 的列根据 dict 的插入顺序排序。

### `Series` dict

输出的 indexes 为不同 `Series` index的并集，例：

```py
dict1 = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
         'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(dict1)
print(df)
```

对应数据为：
|     | one | two |
| --- | --- | --- |
| a   | 1.0 | 1.0 |
| b   | 2.0 | 2.0 |
| c   | 3.0 | 3.0 |
| d   | NaN | 4.0 |

其中 columns 为自动创建，row index 为两个 `Series`的并集。`one` 的缺失值由 `NaN` 填充。

#### 为 dict 提供 index

```py
df = pd.DataFrame(dict1, index=['d', 'b', 'a'])
```

对应数据为：
|     | one | two |
| --- | --- | --- |
| d   | NaN | 4.0 |
| b   | 2.0 | 2.0 |
| a   | 1.0 | 1.0 |

即，将 index 对应的 row 对应的数据提取出来创建 `DataFrame`.

#### 为 dict 提供 index 和 columns

```py
df = pd.DataFrame(dict1, index=['d', 'b', 'a'], columns=['two', 'three'])
```

两者对数据进行筛选，获得如下结果：
|     | two | three |
| --- | --- | ----- |
| d   | 4.0 | NaN   |
| b   | 2.0 | NaN   |
| a   | 1.0 | NaN   |

获取 index 和 columns 信息：

```py
df.index
df.columns
```

### 通过 `ndarray` 或 list 的 `dict` 创建

`ndarray` s的长度必须相同，如果提供 index，index的长度也必须和数组相同。如果不提供 index，则默认 index 为 `range(n)`，n为数组长度。

```py
d = {'one': [1., 2., 3., 4.],
     'two': [4., 3., 2., 1.]}
df = pd.DataFrame(d)
```

数据如下：
|     | one | two |
| --- | --- | --- |
| 0   | 1.0 | 4.0 |
| 1   | 2.0 | 3.0 |
| 2   | 3.0 | 2.0 |
| 3   | 4.0 | 1.0 |

### 创建时提供 index

```py
df = pd.DataFrame(d, index=['a', 'b', 'c', 'd'])
```

数据如下：
|     | one | two |
| --- | --- | --- |
| a   | 1.0 | 4.0 |
| b   | 2.0 | 3.0 |
| c   | 3.0 | 2.0 |
| d   | 4.0 | 1.0 |

以如下的表格为例：第一列为索引
|       | a   | b   | c   |
| ----- | --- | --- | --- |
| **1** | 4   | 7   | 10  |
| **2** | 5   | 8   | 11  |
| **3** | 6   | 9   | 12  |

指定每行的数据
```py
df = pd.DataFrame(
        [[4, 7, 10],
        [5, 8, 11],
        [6, 9, 12]],
        index=[1, 2, 3],
        columns=['a', 'b', 'c'])
```
包含多种索引
```py
df = pd.DataFrame(
        {"a" : [4 ,5, 6],
        "b" : [7, 8, 9],
        "c" : [10, 11, 12]},
        index = pd.MultiIndex.from_tuples(
                [('d',1),('d',2),('e',2)],
                        names=['n','v'])))
```

![](images/2019-08-28-15-26-40.png)

### 通过 `ndarray` 创建

```py
import numpy as np
import pandas as pd

data = np.array([['', 'Col1', 'Col2'],
                 ['Row1', 1, 2],
                 ['Row2', 3, 4]])
print(data[1:])
# 使用二维 ndarray 创建 DataFrame.
# data 为第1行、第1列开始；index 是从第一个1开始的第1列；columns 是第0行从1开始的所有值
df = pd.DataFrame(data=data[1:, 1:],
                  index=data[1:, 0],
                  columns=data[0, 1:])
print(df)
```


## DataFrame 操作

### 索引

| 操作                          | 语法            | 返回类型    |
| ----------------------------- | --------------- | ----------- |
| 选择列                        | `df[colName]`   | `Series`    |
| 通过标签选择行                | `df.loc[label]` | `Series`    |
| 通过索引选择行                | `df.iloc[loc]`  | `Series`    |
| Slice rows                    | `df[5:10]`      | `DataFrame` |
| Select rows by boolean vector | `df[bool_vec]`  | `DataFrame` |

其他操作
| 操作                                  | 说明                                                                                                                                                                                    |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| df.head(n=5)                          | 获得开头的 n 行数据，默认为5                                                                                                                                                            |
| df.tail(n=5)                          | 获得末尾的 n 行数据，默认为5                                                                                                                                                            |
| df.iloc[:3]                           | 前三行                                                                                                                                                                                  |
| df.iloc[1:5, 2:4]                     | [1, 5)行，[2, 4)列, 0-based                                                                                                                                                             |
| df.iloc[[1, 3, 5], [1, 3]]            | 选择 1, 3, 5行，1, 3, 列                                                                                                                                                                |
| df.iloc[1:3, :]                       | 选择[1,3)行，所有列                                                                                                                                                                     |
| df.iloc[:, 1:3]                       | 选择所有行，[1,3)列                                                                                                                                                                     |
| df.iloc[1, 1]                         | 第二行第二个                                                                                                                                                                            |
| df.iloc[1]                            | 第二行                                                                                                                                                                                  |
| df.sort_index(axis=0, ascending=True) | 按照行的 index label 进行排序，返回排序后的DataFrame, 原始数据不变.axis 指定排序用行还是列，默认采用每一行的index label，axis=1采用列的 index label.ascending, 默认升序，可以设置为降序 |

### DataFrame.sort_values

`DataFrame.sort_values(self,by,axis=0,asecending=True,inplace=False,kind='quicksort',na_position='last',ignore_index=False)`

根据值进行排序。

参数：

1. by, str or list of str

根据指定名称（或名称列表）对应值进行排序：
  
- 如果 `axis` 为 0 或 'index'，则 `by` 为index level 标签 and/or column labels
- 如果 `axis` 为 1 或 'columns'，则 `by` 为 column level and/or index labels.

2. axis, {0 or 'index', 1 or 'columns'}, default 0

用于排序的轴。

3. ascending, bool or list of bool, default True

升序或降序排序。指定多个值时，其长度要和 `by` 的长度相同。

4. inplace, bool, default False

是否为原位排序。

5. kind, {'quicksort', 'mergesort', 'heapsort'}, default 'quicksort'

用于选择排序算法。参考 `ndarray.np.sort` 查看更多信息。对 `DataFrame`，只有第单列或单个 label 排序时该参数才有效。

6. na_position: {'first', 'last'}, default 'last'

'first' 表示将 NaN 放在最前面，`last` 表示放在最后面。

7. ignore_index, bool, default False

如果为 True, axis 为标记为 0,1,...,n-1。

返回：

排序后的 `DataFrame` 或 `None`。

如果 `inplace=False`，返回排序后的 `DataFrame`，否则返回 None.

- 例如：按 'col1' 排序

```py
df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3]
})
df1 = df.sort_values(by=['col1'])
```

Out:

```cmd
  col1  col2  col3
0    A     2     0
1    A     1     1
2    B     9     9
5    C     4     3
4    D     7     2
3  NaN     8     4
```

- sort by multiple columns

```py
df.sort_values(by=['col1', 'col2'])
```

Out:

```cmd
    col1 col2 col3
1   A    1    1
0   A    2    0
2   B    9    9
5   C    4    3
4   D    7    2
3   NaN  8    4
```

### DataFrame.sort_index

`DataFrame.sort_index(self,axis=0,level=None,ascending=True,inplace=False,kind='quicksort',na_position='last',sort_remaining=True,ignore_index:bool=False)`

根据标签排序。

参数：

1. axis, {0 or 'index', 1 or 'columns'}, default 0

排序的轴。0 表示行，1表示列。

2. level, int or level name or list of ints or list of level names

如果不是 None，则对指定索引级别中的值进行排序。

3. ascending: bool, default True

升序或降序排列。

4. inplace: bool, default False

是否原位排序。

5. kind: {‘quicksort’, ‘mergesort’, ‘heapsort’}, default ‘quicksort’

排序算法。对 DataFrame，仅对单列或单个标签排序时有效。

6. na_position{‘first’, ‘last’}, default ‘last’
7. sort_remaining bool, default True

### DataFrame.pivot_table

`DataFrame.pivot_table(self, values=None, index=None)`