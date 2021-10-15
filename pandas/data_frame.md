# DataFrame

- [DataFrame](#dataframe)
  - [简介](#简介)
  - [属性](#属性)
    - [size](#size)
    - [shape](#shape)
  - [方法](#方法)
  - [创建 DataFrame](#创建-dataframe)
    - [Series dict](#series-dict)
      - [为 dict 提供 index](#为-dict-提供-index)
      - [为 dict 提供 index 和 columns](#为-dict-提供-index-和-columns)
    - [通过 ndarray 或 list 的 dict 创建](#通过-ndarray-或-list-的-dict-创建)
    - [创建时提供 index](#创建时提供-index)
    - [通过 `ndarray` 创建](#通过-ndarray-创建)
  - [索引和选择](#索引和选择)
    - [选择行](#选择行)
  - [添加列](#添加列)
    - [添加标量值作为列](#添加标量值作为列)
    - [通过已有列计算](#通过已有列计算)
    - [插入指定位置](#插入指定位置)
    - [已有列派生-assign](#已有列派生-assign)
  - [删除列](#删除列)
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
  - [应用函数](#应用函数)
    - [apply](#apply)
    - [应用 elementwise 函数](#应用-elementwise-函数)
  - [排序](#排序)
    - [index 排序](#index-排序)
    - [值排序](#值排序)
  - [参考](#参考)

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

| 属性  | 说明 |
| --- | --- |
|columns|columns labels|
|dtypes|每一列的类型|
| index | DataFrame 的索引（行标签） |
| size  | 单元格个数  |
| shape | 返回 DataFrame 的维数（tuple）|


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

## 方法

以下 `frame` 指代 `DataFrame` 对象。

|方法|说明|
|---|---|
|`frame.head(n)`|返回开始的 `n` 行|
|`frame.tail(n)`|返回末尾的 `n` 行|
|`len(frame)`|frame 行数|

## 创建 DataFrame

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

### Series dict

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

### 通过 ndarray 或 list 的 dict 创建

`ndarray` 的长度必须相同，如果提供 index，index的长度也必须和数组相同。如果不提供 index，则默认 index 为 `range(n)`，n 为数组长度。

```py
In [1]: data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
In [2]: frame = pd.DataFrame(data)
In [3]: frame
Out[3]: 
   pop   state  year
0  1.5    Ohio  2000
1  1.7    Ohio  2001
2  3.6    Ohio  2002
3  2.4  Nevada  2001
4  2.9  Nevada  2002
5  3.2  Nevada  2003
```

在创建时如果指定 columns，这 columns 会根据指定的 columns 排列：

```py
In [4]: pd.DataFrame(data, columns=['year', 'state', 'pop'])
Out[4]: 
   year   state  pop
0  2000    Ohio  1.5
1  2001    Ohio  1.7
2  2002    Ohio  3.6
3  2001  Nevada  2.4
4  2002  Nevada  2.9
5  2003  Nevada  3.2
```

如果指定的 columns 不存在，这全部以缺失值填充：

```py
In [5]: frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
   ....:                       index=['one', 'two', 'three', 'four',
   ....:                              'five', 'six'])

In [6]: frame2
Out[6]: 
       year   state  pop debt
one    2000    Ohio  1.5  NaN
two    2001    Ohio  1.7  NaN
three  2002    Ohio  3.6  NaN
four   2001  Nevada  2.4  NaN
five   2002  Nevada  2.9  NaN
six    2003  Nevada  3.2  NaN

In [7]: frame2.columns
Out[7]: Index(['year', 'state', 'pop', 'debt'], dtype='object')
```

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

## 索引和选择

| 操作 | 语法 | 返回类型 |
| --- | --- | --- |
| 选择列    | `frame[colName]`   | `Series`    |
| 通过行标签选择行  | `frame.loc[label]` | `Series`    |
| 通过行位置选择行 | `frame.iloc[loc]`  | `Series`    |
| 行切片| `frame[5:10]`      | `DataFrame` |
| 通过 boolean 向量选择行| `frame[bool_vec]`  | `DataFrame` |

### 选择行




## 添加列

### 添加标量值作为列

当插入标量值，会自动复制填充整个列：

```py
In [1]: df
Out[1]:
one flag
a 1.0 False
b 2.0 False
c 3.0 True
d NaN False

In [2]: df["foo"] = "bar"
In [3]: df
Out[3]:
one flag foo
a 1.0 False bar
b 2.0 False bar
c 3.0 True bar
d NaN False bar
```

### 通过已有列计算

```py
In[1]: d = {
  ...: "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
  ...: "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"])
}
In[2: df = pd.DataFrame(d)
In[3]: df["one"]
Out[3]: 
a    1.0
b    2.0
c    3.0
d    NaN
Name: one, dtype: float64

In[4]: df['three'] = df['one'] * df['two'] # 新 column 为已有两列的乘积
In[5]: df['flag'] = df['one'] > 2 # 新 column 为 one 列计算的 boolean 值
In[6]: df
Out[6]: 
   one  two  three   flag
a  1.0  1.0    1.0  False
b  2.0  2.0    4.0  False
c  3.0  3.0    9.0   True
d  NaN  4.0    NaN  False
```

如果插入的 `Series` 的 index 和 `DataFrame` 不同，会自动和 `DataFrame` 对齐：

```py
In [78]: df["one_trunc"] = df["one"][:2] # 不足自动填充 NaN

In [79]: df
Out[79]:
one flag foo one_trunc
a 1.0 False bar 1.0
b 2.0 False bar 2.0
c 3.0 True bar NaN
d NaN False bar NaN
```

### 插入指定位置

添加的列默认在最厚，可以通过 `insert` 函数在指定位置插入：

```py
In [80]: df.insert(1, "bar", df["one"]) # 插入到第二的位置

In [81]: df
Out[81]:
one bar flag foo one_trunc
a 1.0 1.0 False bar 1.0
b 2.0 2.0 False bar 2.0
c 3.0 3.0 True bar NaN
d NaN NaN False bar NaN
```

### 已有列派生-assign

```py
DataFrame.assign(**kwargs)
```

通过 `assign` 方法通过已有列派生新列：

```py
In [82]: iris = pd.read_csv("data/iris.data")

In [83]: iris.head()
Out[83]:
SepalLength SepalWidth PetalLength PetalWidth Name
0 5.1 3.5 1.4 0.2 Iris-setosa
1 4.9 3.0 1.4 0.2 Iris-setosa
2 4.7 3.2 1.3 0.2 Iris-setosa
3 4.6 3.1 1.5 0.2 Iris-setosa
4 5.0 3.6 1.4 0.2 Iris-setosa

In [84]: iris.assign(sepal_ratio=iris["SepalWidth"] / iris["SepalLength"]).head()
Out[84]:
SepalLength SepalWidth PetalLength PetalWidth Name sepal_ratio
0 5.1 3.5 1.4 0.2 Iris-setosa 0.686275
1 4.9 3.0 1.4 0.2 Iris-setosa 0.612245
2 4.7 3.2 1.3 0.2 Iris-setosa 0.680851
3 4.6 3.1 1.5 0.2 Iris-setosa 0.673913
4 5.0 3.6 1.4 0.2 Iris-setosa 0.720000
```

也可以使用以 `DataFrame` 为参数的函数传入进去：

```py
In [85]: iris.assign(sepal_ratio=lambda x: (x["SepalWidth"] / x["SepalLength"])).head()
Out[85]:
SepalLength SepalWidth PetalLength PetalWidth Name sepal_ratio
0 5.1 3.5 1.4 0.2 Iris-setosa 0.686275
1 4.9 3.0 1.4 0.2 Iris-setosa 0.612245
2 4.7 3.2 1.3 0.2 Iris-setosa 0.680851
3 4.6 3.1 1.5 0.2 Iris-setosa 0.673913
4 5.0 3.6 1.4 0.2 Iris-setosa 0.720000
```

`assign` 返回 `DataFrame` 的 copy，不回修改原 `DataFrame`。

使用 `callable` 而不是实际值，在串联操作时十分有用：

```py
In [86]: (
....: iris.query("SepalLength > 5")
....: .assign(
....: SepalRatio=lambda x: x.SepalWidth / x.SepalLength,
....: PetalRatio=lambda x: x.PetalWidth / x.PetalLength,
....: )
....: .plot(kind="scatter", x="SepalRatio", y="PetalRatio")
....: )
....:
Out[86]: <AxesSubplot:xlabel='SepalRatio', ylabel='PetalRatio'>
```

传入的函数基于 `DataFrame` 计算新 column 的值。

`assign` 函数签名参数为 `**kwargs`，key 是新 column 名称，而值为插入的值（如 `Series` 或 NumPy 数组），或者以 `DataFrame` 为参数的函数。返回插入新值的原 `DataFrame` 的 copy。

到 Python 3.6，`**kwargs` 键的顺序保留，这样就可以使用依赖型的赋值，即在一次 `assign` 调用中，`**kwargs` 后面的表达式可以使用前面表达式值，例如：

```py
In [87]: dfa = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

In [88]: dfa.assign(C=lambda x: x["A"] + x["B"], D=lambda x: x["A"] + x["C"])
Out[88]:
A B C D
0 1 4 5 6
1 2 5 7 9
2 3 6 9 12
```

第二个表达式中 `x['C']` 表示前面刚创建的子。



## 删除列

```py
In[1]: df
Out[2]: 
   one  two  three   flag
a  1.0  1.0    1.0  False
b  2.0  2.0    4.0  False
c  3.0  3.0    9.0   True
d  NaN  4.0    NaN  False

In [3]: del df["two"] # 使用 del 关键字删除

In [4]: three = df.pop("three") # 使用 pop 删除

In [75]: df
Out[75]:
one flag
a 1.0 False
b 2.0 False
c 3.0 True
d NaN False
```

## 索引

其他操作

| 操作  | 说明   |
| ------ | ----- |
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

要保留 `dtype`，最好使用 `itertuples()`，该方法返回命名元组，并且比 `iterrows` 快。

### itertuples

```py
DataFrame.itertuples(index=True, name='Pandas')
```

以命名元组的形式迭代 `DataFrame` 的行。

|参数|类型|说明|
|---|---|---|
|index|bool, default True|True 表示将索引作为元祖的第一个元素返回|
|name|str or None, default "Pandas"|命名元祖的名称，`None` 表示常规元祖|

如果列名是无效的 Python 识别符、重复或以下划线开头，则重命名为位置名称。

```py
>>> df = pd.DataFrame({'num_legs': [4, 2], 'num_wings': [0, 2]},
...                  index=['dog', 'hawk'])
>>> df
      num_legs  num_wings
dog          4          0
hawk         2          2
>>> for row in df.itertuples():
...    print(row)
...
Pandas(Index='dog', num_legs=4, num_wings=0)
Pandas(Index='hawk', num_legs=2, num_wings=2)
```

- 如果将 `index` 设置为 `False`，则移除索引

```py
>>> for row in df.itertuples(index=False):
...    print(row)
...
Pandas(num_legs=4, num_wings=0)
Pandas(num_legs=2, num_wings=2)
```

- `name` 用于自定义命名元祖的名称

```py
>>> for row in df.itertuples(name='Animal'):
...    print(row)
...
Animal(Index='dog', num_legs=4, num_wings=0)
Animal(Index='hawk', num_legs=2, num_wings=2)
```

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

## 应用函数

### apply

### 应用 elementwise 函数

不是所有函数都可以向量化，所以 `DataFrame` 提供了 `applymap()`， `Series` 提供了 `map()`，可以应用于单个参数单个返回值的函数。例如：

```py
In [197]: df4
Out[197]:
one two three
a 1.394981 1.772517 NaN
b 0.343054 1.912123 -0.050390
c 0.695246 1.478369 1.227435
d NaN 0.279344 -0.613172

In [198]: def f(x): # 单参数函数，返回当个值
.....: return len(str(x))
.....:

In [199]: df4["one"].map(f) # map 接受单参数函数
Out[199]:
a 18
b 19
c 18
d 3
Name: one, dtype: int64

In [200]: df4.applymap(f) # applymap 应用于所有元素
Out[200]:
one two three
a 18 17 3
b 19 18 20
c 18 18 16
d 3 19 19
```

## 排序

pandas 支持三种类型的排序：

- index label 排序
- column 值排序
- 以上两者组合排序

### index 排序

`Series.sort_index()` 和 `DataFrame.sort_index()` 方法用于 index 排序：

```py
In [300]: df = pd.DataFrame(
   .....: {
   .....: "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
   .....: "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
   .....: "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
   .....: }
   .....: )
   .....:
 
In [301]: unsorted_df = df.reindex(
   .....: index=["a", "d", "c", "b"], columns=["three", "two", "one"]
   .....: )
   .....:

In [302]: unsorted_df
Out[302]:
three two one
a NaN -1.152244 0.562973
d -0.252916 -0.109597 NaN
c 1.273388 -0.167123 0.640382
b -0.098217 0.009797 -1.299504

# DataFrame
In [303]: unsorted_df.sort_index() # 按 index 排序
Out[303]:
three two one
a NaN -1.152244 0.562973
b -0.098217 0.009797 -1.299504
c 1.273388 -0.167123 0.640382
d -0.252916 -0.109597 NaN

In [304]: unsorted_df.sort_index(ascending=False) # 降序
Out[304]:
three two one
d -0.252916 -0.109597 NaN
c 1.273388 -0.167123 0.640382
b -0.098217 0.009797 -1.299504
a NaN -1.152244 0.562973

In [305]: unsorted_df.sort_index(axis=1) # 按照行 index 排序
Out[305]:
one three two
a 0.562973 NaN -1.152244
d NaN -0.252916 -0.109597
c 0.640382 1.273388 -0.167123
b -1.299504 -0.098217 0.009797

# Series
In [306]: unsorted_df["three"].sort_index()
Out[306]:
a NaN
b -0.098217
c 1.273388
d -0.252916
Name: three, dtype: float64
```

- `sort_index` 可以使用一个 `key` 参数，该参数应用于待排序 index 的 callable 函数。对 `MultiIndex` 对象，`key` 通过 `level` 参数应用到指定 axis

```py
In [307]: s1 = pd.DataFrame({"a": ["B", "a", "C"], "b": [1, 2, 3], "c": [2, 3, 4]}).set_index(
   .....: list("ab")
   .....: )
   .....:
In [308]: s1
Out[308]:
    c
a b
B 1 2
a 2 3
C 3 4


In [309]: s1.sort_index(level="a") # 对 MultiIndex，通过 level='a' 指定排序的 index
Out[309]:
    c
a b
B 1 2
C 3 4
a 2 3

In [310]: s1.sort_index(level="a", key=lambda idx: idx.str.lower()) # 通过 key 指定函数
Out[310]:
    c
a b
a 2 3
B 1 2
C 3 4
```

### 值排序

`Series.sort_values()` 用于排序 `Series` 值。`DataFrame.sort_values()` 用于排序 `DataFrame` 的行或列值。例如：

```py
In [311]: df1 = pd.DataFrame(
   .....: {"one": [2, 1, 1, 1], "two": [1, 3, 2, 4], "three": [5, 4, 3, 2]}
   .....: )
   .....:

In [312]: df1.sort_values(by="two") # 排序
Out[312]:
one two three
0 2 1 5
2 1 2 3
1 1 3 4
3 1 4 2
```

- `by` 参数可以指定 column 名称列表

```py
In [313]: df1[["one", "two", "three"]].sort_values(by=["one", "two"])
Out[313]:
one two three
2 1 2 3
1 1 3 4
3 1 4 2
0 2 1 5
```

通过 `na_position` 参数可以指定 NA 值的位置：

```py
In [314]: s[2] = np.nan

In [315]: s.sort_values()
Out[315]:
0 A
3 Aaba
1 B
4 Baca
6 CABA
8 cat
7 dog
2 <NA>
5 <NA>
dtype: string

In [316]: s.sort_values(na_position="first")
Out[316]:
2 <NA>
5 <NA>
0 A
3 Aaba
1 B
4 Baca
6 CABA
8 cat
7 dog
dtype: string
```

- 同样也支持 `key` 参数，设置 callable 函数应用于待排序的值

```py
In [317]: s1 = pd.Series(["B", "a", "C"])
In [318]: s1.sort_values()
Out[318]:
0 B
2 C
1 a
dtype: object

In [319]: s1.sort_values(key=lambda x: x.str.lower())
Out[319]:
1 a
0 B
2 C
dtype: object
```

`key` 函数接受 `Series` 值，返回相同 shape 的 `Series` 或数组。对 `DataFrame`，`key` 应用于 column，因此参数为 `Series`，返回值也为 `Series`：

```py
In [320]: df = pd.DataFrame({"a": ["B", "a", "C"], "b": [1, 2, 3]})
In [321]: df.sort_values(by="a")
Out[321]:
  a b
0 B 1
2 C 3
1 a 2

In [322]: df.sort_values(by="a", key=lambda col: col.str.lower())
Out[322]:
  a b
1 a 2
0 B 1
2 C 3
```

## 参考
