# DataFrame

- [DataFrame](#dataframe)
  - [简介](#简介)
  - [属性](#属性)
    - [size](#size)
    - [shape](#shape)
  - [创建 `DataFrame`](#创建-dataframe)
    - [`Series` dict](#series-dict)
      - [为 dict 提供 index](#为-dict-提供-index)
      - [为 dict 提供 index 和 columns](#为-dict-提供-index-和-columns)
    - [通过 `ndarray` 或 list 的 `dict` 创建](#通过-ndarray-或-list-的-dict-创建)
    - [创建时提供 index](#创建时提供-index)
    - [通过 `ndarray` 创建](#通过-ndarray-创建)
  - [DataFrame 操作](#dataframe-操作)
  - [添加 column](#添加-column)
    - [索引](#索引)
    - [DataFrame.sort_values](#dataframesort_values)
    - [DataFrame.sort_index](#dataframesort_index)
    - [DataFrame.pivot_table](#dataframepivot_table)
  - [索引和迭代](#索引和迭代)
    - [pop](#pop)
    - [iterrows](#iterrows)
    - [itertuples](#itertuples)
    - [xs](#xs)
  - [索引、选择和标签操作](#索引选择和标签操作)
    - [set_index](#set_index)
    - [drop](#drop)

2020-05-19, 12:26
***

## 简介

`DataFrame` 在 pandas 中是二维带标签数组，你可以将其看做 Excel 表格、SQL表格或值类型为 `Series` 的字典。`DataFrame` 不同列的数据类型可以不同，在Pandas 中使用最为广泛。另外：

- 每列的数据类型相同
- 每行包含索引 0…n

如下所示：

![dataframe](images/2019-08-28-15-19-03.png)

如果将 Dates 设置为 index:

![index](images/2019-08-28-15-19-25.png)

## 属性

| 属性  | 说明                            |
| ----- | ------------------------------- |
| index | DataFrame 的索引（行标签）      |
| size  | 元素个数                        |
| shape | 返回表示 DataFrame 维数的 tuple |
|columns|columns labels|

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

## 添加 column

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

## 索引和迭代

### pop

```py
DataFrame.pop(item)
```

删除并返回指定列。如果 `DataFrame` 中没有，抛出 `KeyError`。

|参数|类型|说明|
|---|---|---|
|`item`|标签|移除的列标签|

返回 `Series`。

例如：

```py
>>> df = pd.DataFrame([('falcon', 'bird', 389.0),
...                   ('parrot', 'bird', 24.0),
...                   ('lion', 'mammal', 80.5),
...                   ('monkey', 'mammal', np.nan)],
...                  columns=('name', 'class', 'max_speed'))
>>> df
     name   class  max_speed
0  falcon    bird      389.0
1  parrot    bird       24.0
2    lion  mammal       80.5
3  monkey  mammal        NaN
```

- 删除并返回 `class` 列

```py
>>> df.pop('class')
0      bird
1      bird
2    mammal
3    mammal
Name: class, dtype: object
```

```py
>>> df
     name  max_speed
0  falcon      389.0
1  parrot       24.0
2    lion       80.5
3  monkey        NaN
```

### iterrows

```py
DataFrame.iterrows()
```

以 `(index, Series)` 形式迭代 `DataFrame` 行。

|返回值|类型|说明|
|---|---|---|
|`index`|标签或标签 tuple|行的index，对 MultiIndex 为 tuple|
|`data`|`Series`|以 `Series` 的形式返回行|

由于 `iterrows` 以 `Series` 的形式返回行，所以不保存 `dtype`。例如：

```py
>>> df = pd.DataFrame([[1, 1.5]], columns=['int', 'float'])
>>> row = next(df.iterrows())[1]
>>> row
int      1.0
float    1.5
Name: 0, dtype: float64
>>> print(row['int'].dtype)
float64
>>> print(df['int'].dtype)
int64
```

要保留 `dtype`，最好使用 `itertuples()`，该方法返回命名元组，并且一般比 `iterrows` 快。

### itertuples

```py
DataFrame.itertuples(index=True, name='Pandas')
```

以命名元组的形式迭代返回 `DataFrame` 的行。

|参数|类型|说明|
|---|---|---|
|index|bool, default True|如果 True



### xs

## 索引、选择和标签操作

### set_index

```py
DataFrame.set_index(self, keys, drop=True, append=False, inplace=False, verify_integrity=False)
```

将现有的 columns 设置为 index.

将一个或多个 columns 或 arrays (相同长度)设置为 index (row labels)。新添加的 index 可以替换或扩展原有 index。

1. keys

支持类型：

- 单个 column key
- 和 `DataFrame` 等长的array
- 任意数目的 column keys 和 array 的组合 list。

这个 array 可以是 `Series`, `Index`, `np.ndarray` 以及 `Iterator`。

2. drop

bool, default True。

删除用作索引的列。

3. append

bool, default False。

### drop

从行或列中删除指定标签。

```py
DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
```

通过标签名称、列名称、索引等删除行或列。当使用 MultiIndex 时，不同 level 的标签可以通过指定 level 删除。

|参数|类型|说明|
|---|---|---|
|`labels`|标签或标签列表|用于指定删除的索引或列|
|`axis`|0 for 'index', 1 for 'column'，默认0|指定删除行还是列|
|`index`|标签或标签列表|指定删除的行，这样就不用指定 `axis=0`|
|`columns`|标签或标签列表|指定删除的列，这样就不用指定 `axis=1`|
|`inplace`|bool, default False|False 返回副本，True 原位操作，返回 `None`|

例如：

```py
>>> df = pd.DataFrame(np.arange(12).reshape(3, 4),
...                  columns=['A', 'B', 'C', 'D'])
>>> df
   A  B   C   D
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
```

- 删除列

```py
>>> df.drop(['B', 'C'], axis=1) # axis=1 表示删除列
   A   D
0  0   3
1  4   7
2  8  11
```

```py
>>> df.drop(columns=['B', 'C'])
   A   D
0  0   3
1  4   7
2  8  11
```

- 删除行

通过 index 删除行：

```py
>>> df.drop([0, 1])
   A  B   C   D
2  8  9  10  11
```
