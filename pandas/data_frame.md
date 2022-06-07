# DataFrame

- [DataFrame](#dataframe)
  - [简介](#简介)
  - [创建 DataFrame](#创建-dataframe)
    - [list dict](#list-dict)
    - [Series dict](#series-dict)
      - [为 dict 提供 index](#为-dict-提供-index)
      - [为 dict 提供 index 和 columns](#为-dict-提供-index-和-columns)
    - [ndarray dict](#ndarray-dict)
    - [2D ndarray](#2d-ndarray)
    - [指定 column 名称](#指定-column-名称)
    - [指定 index](#指定-index)
  - [属性](#属性)
    - [size](#size)
    - [shape](#shape)
    - [columns](#columns)
  - [方法](#方法)
    - [info](#info)
  - [索引和选择](#索引和选择)
    - [选择单值](#选择单值)
      - [单值标签（at）](#单值标签at)
      - [单值索引（iat）](#单值索引iat)
    - [选择单列](#选择单列)
      - [属性（column label）](#属性column-label)
      - [索引运算符](#索引运算符)
    - [选择多列](#选择多列)
      - [索引运算符（多列）](#索引运算符多列)
      - [特定类型列（select_dtypes）](#特定类型列select_dtypes)
    - [选择行和列](#选择行和列)
      - [标签（loc）](#标签loc)
      - [位置（iloc）](#位置iloc)
    - [抽样（sample）](#抽样sample)
    - [设置索引（set_index）](#设置索引set_index)
    - [重置 index（reset_index）](#重置-indexreset_index)
    - [重命名标签（rename）](#重命名标签rename)
  - [过滤](#过滤)
    - [单个布尔表达式](#单个布尔表达式)
    - [组合逻辑运算](#组合逻辑运算)
    - [isin](#isin)
    - [filter](#filter)
  - [重复值](#重复值)
    - [查找重复值（duplicated）](#查找重复值duplicated)
    - [删除重复值（drop_duplicates）](#删除重复值drop_duplicates)
  - [设置值](#设置值)
    - [基于标签设置（loc）](#基于标签设置loc)
  - [添加](#添加)
    - [添加标量值作为列](#添加标量值作为列)
    - [通过已有列计算](#通过已有列计算)
    - [插入指定位置](#插入指定位置)
    - [已有列派生-assign](#已有列派生-assign)
  - [删除](#删除)
    - [使用标签删除（drop）](#使用标签删除drop)
    - [删除缺失值](#删除缺失值)
  - [删除列](#删除列)
  - [索引和迭代](#索引和迭代)
    - [pop](#pop)
    - [iterrows](#iterrows)
    - [itertuples](#itertuples)
  - [应用函数](#应用函数)
    - [apply](#apply)
    - [应用 elementwise 函数](#应用-elementwise-函数)
  - [转置](#转置)
  - [排序](#排序)
    - [按索引排序（sort_index）](#按索引排序sort_index)
    - [按值排序（sort_values）](#按值排序sort_values)
  - [统计](#统计)
    - [count](#count)
    - [nunique](#nunique)
  - [reshape](#reshape)
    - [nlargest](#nlargest)
  - [转换](#转换)
    - [类型转换（astype）](#类型转换astype)
  - [缺失值](#缺失值)
    - [检测缺失值（isnull）](#检测缺失值isnull)
    - [检测非缺失值（notnull）](#检测非缺失值notnull)
    - [检测缺失值（isna）](#检测缺失值isna)
    - [删除缺失值（dropna）](#删除缺失值dropna)
    - [fillna](#fillna)
    - [替换（replace）](#替换replace)
  - [参考](#参考)

2020-05-19, 12:26
@author Jiawei Mao
***

## 简介

`DataFrame` 是 pandas 提供的二维带标签数组，是 pandas 的主力。可以将其看做 Excel 表格、SQL表格或值类型为 `Series` 的字典。`DataFrame` 不同列的数据类型可以相同，也可以不同，在Pandas 中使用最为广泛。和 `Series` 一样，`DataFrame` 的每行都包含位置索引和标签索引两种索引方式，另外要求每列的数据类型必须相同。

如下所示：

![dataframe](images/2019-08-28-15-19-03.png)

如果将 Dates 设置为 index:

![index](images/2019-08-28-15-19-25.png)

## 创建 DataFrame

```py
class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)
```

`DataFrame` 接受多种类型的输入：

- 1D `ndarray`、lists、dicts 或 `Series`  的 dict
- 2D `numpy.ndarray`
- `Series`
- 其它 `DataFrame`

除了数据，创建 `DataFrame` 时还可以设置 index (行标签)和 columns (列标签)。如果创建时提供了 index / columns，则为了保证标签对应，不符合要求的数据被舍弃。

### list dict

使用 list dict 创建 `DataFrame`：

```py
>>> import pandas as pd
>>> import numpy as np
>>> city_date = {
    "City": ["New York City", "Paris", "Barcelona", "Rome"],
    "Country": ["United States", "France", "Spain", "Italy"],
    "Population": [8600000, 2141000, 5515000, 2873000]
}
>>> cities = pd.DataFrame(city_date)
>>> cities
            City        Country  Population
0  New York City  United States     8600000
1          Paris         France     2141000
2      Barcelona          Spain     5515000
3           Rome          Italy     2873000
```

在输入数据为 `dict` 类型时，如果没有指定 `columns`，则 `DataFrame` 的列根据 dict 的插入顺序排序。

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

### ndarray dict

说明：

- `ndarray` 的长度必须相同；
- 如果提供 `index`，`index` 的长度必须和数据相同；
- 如果不提供 index，则默认 index 为 `range(n)`，n 为数组长度。

```py
>>> data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
>>> frame = pd.DataFrame(data)
>>> frame
    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
4  Nevada  2002  2.9
5  Nevada  2003  3.2
```

### 2D ndarray

使用二维 ndarray 创建 `DataFrame`：

```py
>>> random_data = np.random.randint(1, 101, [3, 5])
>>> random_data
array([[12, 24, 97, 50, 50],
       [79, 36, 82, 68,  1],
       [54, 52, 99, 38, 33]])
>>> pd.DataFrame(data=random_data)
    0   1   2   3   4
0  12  24  97  50  50
1  79  36  82  68   1
2  54  52  99  38  33
```

由于没有提供 index 和 columns，所以行和列的名称都是默认的索引值。

### 指定 column 名称

`columns` 参数用于指定列名称：

- 如果没有指定列名称，默认为 `RangeIndex(0, 1, 2, ...,n)`；
- 如果列已有名称，则根据名称从数据中提取对应的列创建 `DataFrame`。

**例1**，根据 `columns` 指定 column 顺序：

```py
>>> data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
>>> pd.DataFrame(data, columns=["year", "state", "pop"])
   year   state  pop
0  2000    Ohio  1.5
1  2001    Ohio  1.7
2  2002    Ohio  3.6
3  2001  Nevada  2.4
4  2002  Nevada  2.9
5  2003  Nevada  3.2
```

**例2**，如果指定的 `columns` 不存在，则该列全部填充 NaN 值：

```py
>>> pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'])
   year   state  pop debt
0  2000    Ohio  1.5  NaN
1  2001    Ohio  1.7  NaN
2  2002    Ohio  3.6  NaN
3  2001  Nevada  2.4  NaN
4  2002  Nevada  2.9  NaN
5  2003  Nevada  3.2  NaN
```

### 指定 index

`index` 用于 row 的索引。默认为 `RangeIndex`。

**例1**，指定 index：

```py
>>> frame = pd.DataFrame(
        [[4, 7, 10],
        [5, 8, 11],
        [6, 9, 12]],
        index=[1, 2, 3],
        columns=['a', 'b', 'c'])
>>> frame
   a  b   c
1  4  7  10
2  5  8  11
3  6  9  12
```

**例2**，使用 `MultiIndex` 指定多级索引：

```py
>>> pd.DataFrame(
        {"a" : [4 ,5, 6],
        "b" : [7, 8, 9],
        "c" : [10, 11, 12]
        },
        index = pd.MultiIndex.from_tuples(
                [('d',1),('d',2),('e',2)],
                        names=['n','v']))
     a  b   c
n v          
d 1  4  7  10
  2  5  8  11
e 2  6  9  12
```

其结构如下所示：

![](images/2019-08-28-15-26-40.png)

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

### columns

`columns` 属性保存了 `DataFrame` 的 column 标签。

使用 `columns` 属性可以查询 `DataFrame` 的 column 标签，也可以直接使用该属性修改 column 标签。也可以使用 [rename](#重命名标签rename) 方法重命名 column 标签。

**例1**，column 标签操作

```py
>>> df
    A   B   C
0   0   2   3
1   0   4  10
2  10  20  30
>>> df.columns # 查询 column 标签，类型为 Index
Index(['A', 'B', 'C'], dtype='object') 
>>> df.columns = ['AA', 'BB', 'CC'] # 修改 column 标签
>>> df
   AA  BB  CC
0   0   2   3
1   0   4  10
2  10  20  30
```

## 方法

以下 `frame` 指代 `DataFrame` 对象。

|方法|说明|
|---|---|
|`frame.head(n)`|返回开始的 `n` 行|
|`frame.tail(n)`|返回末尾的 `n` 行|
|`len(frame)`|frame 行数|

### info

```py
DataFrame.info(verbose=None, buf=None, max_cols=None, memory_usage=None, show_counts=None, null_counts=None)
```

打印 `DataFrame` 的简要说明。

**例1**，输出所有 column 的信息

`verbose` 参数指定是否输出详细信息。

```py
>>> int_values = [1, 2, 3, 4, 5]
>>> text_values = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
>>> float_values = [0.0, 0.25, 0.5, 0.75, 1.0]
>>> df = pd.DataFrame({"int_col": int_values, "text_col": text_values,
                  "float_col": float_values})
>>> df
   int_col text_col  float_col
0        1    alpha       0.00
1        2     beta       0.25
2        3    gamma       0.50
3        4    delta       0.75
4        5  epsilon       1.00
>>> df.info(verbose=True)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   int_col    5 non-null      int64  
 1   text_col   5 non-null      object 
 2   float_col  5 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 248.0+ bytes
```

**例2**，输出简要信息

设置 `verbose=False` 可以只输出 column 数及其 dtypes：

```py
>>> df.info(verbose=False)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Columns: 3 entries, int_col to float_col
dtypes: float64(1), int64(1), object(1)
memory usage: 248.0+ bytes
```

**例3**，内存占用

## 索引和选择

`DataFrame` 是 `Series` 对象的集合，pandas 提供了多种提取数据的方法。

### 选择单值

#### 单值标签（at）

```py
property DataFrame.at
```

根据 row/column 标签选择单个值。

**例1**，选择单值

```py
>>> df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                  index=[4, 5, 6], columns=['A', 'B', 'C'])
>>> df
    A   B   C
4   0   2   3
5   0   4   1
6  10  20  30
>>> df.at[4, 'B']
2
```

**例2**，设置值

```py
>>> df.at[4, 'B'] = 10
>>> df
    A   B   C
4   0  10   3
5   0   4   1
6  10  20  30
```

**例3**，通过 `Series` 的 `at` 方法查询值

这里 `loc[5]` 选择了标签为 `5` 的行，以 `Series` 返回，然后用 `.at['B']` 选择 `Series` 标签为 `B` 的值。

```py
>>> df.loc[5].at['B']
4
```

#### 单值索引（iat）

```py
property DataFrame.iat
```

使用 row/column 位置访问单值。

**例1**，访问单值

```py
>>> df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                  columns=['A', 'B', 'C'])
>>> df
    A   B   C
0   0   2   3
1   0   4   1
2  10  20  30
>>> df.iat[1, 2]
1
```

**例2**，设置单值

```py
>>> df.iat[1, 2] = 10
>>> df
    A   B   C
0   0   2   3
1   0   4  10
2  10  20  30
```

**例3**，通过 `Series` 的 `iat` 方法访问

```py
>>> df.loc[0].iat[1]
2
```

### 选择单列

#### 属性（column label）

可以直接通过 column 的名称以属性的方式访问 column:

```py
>>> df = pd.DataFrame({'month': [1, 4, 7, 10],
                   'year': [2012, 2014, 2013, 2014],
                   'sale': [55, 40, 84, 31]})
>>> df
   month  year  sale
0      1  2012    55
1      4  2014    40
2      7  2013    84
3     10  2014    31
>>> df.month
0     1
1     4
2     7
3    10
Name: month, dtype: int64
```

返回 `Series` 类型。

#### 索引运算符

使用语法 `frame[colname]` 可以选择单列，使用该语法的优点是，名称中有空格也可以使用。该语法适用于所有情况，所以推荐使用。

```py
>>> df["month"]
0     1
1     4
2     7
3    10
Name: month, dtype: int64
```

### 选择多列

#### 索引运算符（多列）

使用索引运算丰富可以一次选择多列值，此时 `[]` 中包含一个列表，返回的 `DataFrame` columns 按照列表中的顺序排序：

```py
>>> df
   month  year  sale
0      1  2012    55
1      4  2014    40
2      7  2013    84
3     10  2014    31
>>> df[['sale', 'month']]
   sale  month
0    55      1
1    40      4
2    84      7
3    31     10
```

#### 特定类型列（select_dtypes）

```py
DataFrame.select_dtypes(include=None, exclude=None)
```

基于 column 的 dtype 选择部分 columns 返回。返回 `DataFrame` 类型。

- `include` 指定包含的类型；
- `exclude` 指定排除的类型。

例如：

- 使用 `np.number` 或 `'number'` 选择而数值类型；
- 选择字符串用 `object`，但是有个问题，这样会选择所有 `object` 类型的列，不仅是字符串；
- 使用 `np.datetime64`, `'datetime'` 或 `'datetime64'` 选择日期；
- 使用 `np.timedelta64`, `'timedelta'` 或 `'timedelta64'` 选择时间差；
- 使用 `'category'` 选择 Pandas 分类类型；
- 使用 `'datetimetz'` 或 `'datetime64[ns, tz]'` 选择 Pandas datetimetz 类型。

**例1**，选择 bool 类型

```py
>>> df = pd.DataFrame({'a': [1, 2] * 3,
                   'b': [True, False] * 3,
                   'c': [1.0, 2.0] * 3})
>>> df
   a      b    c
0  1   True  1.0
1  2  False  2.0
2  1   True  1.0
3  2  False  2.0
4  1   True  1.0
5  2  False  2.0
>>> df.select_dtypes(include='bool')
       b
0   True
1  False
2   True
3  False
4   True
5  False
```

**例2**，选择浮点类型

```py
>>> df.select_dtypes(include=['float64'])
     c
0  1.0
1  2.0
2  1.0
3  2.0
4  1.0
5  2.0
```

**例3**，排除整数类型

```py
>>> df.select_dtypes(exclude=['int64'])
       b    c
0   True  1.0
1  False  2.0
2   True  1.0
3  False  2.0
4   True  1.0
5  False  2.0
```

### 选择行和列

#### 标签（loc）

```py
property DataFrame.loc
```

使用标签或 boolean 数组访问一组 rows 和 columns。支持的输入包括：

- 单个标签，如 `5` 或 `'a'`，注意这里 `5` 是标签而不是索引；
- 标签的数组或列表，如 `['a', 'b', 'c']`；
- 切片对象，如 `'a':'f'`，和 Python 切片不同，这里首位都包含；
- 和指定 axis 等长的 boolean 数组，如 `[True, False, True]`；
- 可对齐的 boolean `Series`，即选择前先对齐索引；
- 可对齐的 Index；
- 返回以上有效索引的函数。

**例1**，使用标签选择单行：

返回的数据为 `Series` 类型。

```py
>>> df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
>>> df
            max_speed  shield
cobra               1       2
viper               4       5
sidewinder          7       8
>>> df.loc['viper']
max_speed    4
shield       5
Name: viper, dtype: int64
```

**例2**，选择多行

此时返回的数据类型为 `DataFrame`。

```py
>>> df.loc[['viper', 'sidewinder']]
            max_speed  shield
viper               4       5
sidewinder          7       8
```

**例3**，选择单个值

使用 `.loc` 可以同时指定行和列，从而选择指定值：

```py
>>> df.loc['cobra', 'shield']
2
```

这里 `'cobra'` 为行标签，`'shield'` 为列标签，两者用逗号分开。

**例4**，切片选择

`.loc` 语法支持切片，行和列标签都可以使用切片：

```py
>>> df
            max_speed  shield
cobra               1       2
viper               4       5
sidewinder          7       8
>>> df.loc['cobra':'viper', 'max_speed']
cobra    1
viper    4
Name: max_speed, dtype: int64
```

**例4**，选择和 row axis 等长的 boolean 列表选择

```py
>>> df
            max_speed  shield
cobra               1       2
viper               4       5
sidewinder          7       8
>>> df.loc[[False, False, True]]
            max_speed  shield
sidewinder          7       8
```

**例5**，使用可对齐的 boolean `Series` 选择

```py
>>> df
            max_speed  shield
cobra               1       2
viper               4       5
sidewinder          7       8
>>> df.loc[pd.Series([False, True, False],
       index=['viper', 'sidewinder', 'cobra'])]
            max_speed  shield
sidewinder          7       8
```

**例6**，使用 Index 选择

```py
>>> df
            max_speed  shield
cobra               1       2
viper               4       5
sidewinder          7       8
>>> df.loc[pd.Index(["cobra", "viper"], name="foo")]
       max_speed  shield
foo                     
cobra          1       2
viper          4       5
```

**例7**，使用返回 boolean `Series` 的表达式选择

```py
>>> df
            max_speed  shield
cobra               1       2
viper               4       5
sidewinder          7       8
>>> df.loc[df['shield'] > 6]
            max_speed  shield
sidewinder          7       8
```

**例8**，同时使用布尔 `Series` 和 column 标签选择

```py
>>> df
            max_speed  shield
cobra               1       2
viper               4       5
sidewinder          7       8
>>> df.loc[df['shield'] > 6, ['max_speed']]
            max_speed
sidewinder          7
>>> df.loc[df['shield'] > 6, 'max_speed']
sidewinder    7
Name: max_speed, dtype: int64
```

需要注意的是，上面使用 `['max_speed']` 和 `'max_speed'` 返回的数据类型不同，前者是 `DataFrame`，后者是 `Series`。

**例9**，使用返回 boolean `Series` 的函数：

```py
>>> df
            max_speed  shield
cobra               1       2
viper               4       5
sidewinder          7       8
>>> df.loc[lambda df: df['shield'] == 8]
            max_speed  shield
sidewinder          7       8
```

**例10**，对整数标签的 `DataFrame`

```py
>>> df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=[7, 8, 9], columns=['max_speed', 'shield'])
>>> df
   max_speed  shield
7          1       2
8          4       5
9          7       8
>>> df.loc[7:9]
   max_speed  shield
7          1       2
8          4       5
9          7       8
>>> df.loc[7:8] # 切片的首尾都包含
   max_speed  shield
7          1       2
8          4       5
```

**例11**，选择 MultiIndex 的 `DataFrame`

```py
>>> tuples = [
   ('cobra', 'mark i'), ('cobra', 'mark ii'),
   ('sidewinder', 'mark i'), ('sidewinder', 'mark ii'),
   ('viper', 'mark ii'), ('viper', 'mark iii')
]
>>> index = pd.MultiIndex.from_tuples(tuples)
>>> values = [[12, 2], [0, 4], [10, 20],
        [1, 4], [7, 1], [16, 36]]
>>> df = pd.DataFrame(values, columns=['max_speed', 'shield'], index=index)
>>> df
                     max_speed  shield
cobra      mark i           12       2
           mark ii           0       4
sidewinder mark i           10      20
           mark ii           1       4
viper      mark ii           7       1
           mark iii         16      36
>>> df.loc['cobra'] # 返回 DataFrame
         max_speed  shield
mark i          12       2
mark ii          0       4
```

使用 tuple 提供 MultiIndex 的两个标签值，返回 `Seris`：

```py
>>> df.loc[('cobra', 'mark ii')]
max_speed    0
shield       4
Name: (cobra, mark ii), dtype: int64
```

提供两个标签，和使用 tuple 效果一样，也返回 `Series`：

```py
>>> df.loc['cobra', 'mark i']
max_speed    12
shield        2
Name: (cobra, mark i), dtype: int64
```

如果将 tuple 用 `[]` 括起来，则返回 `DataFrame`：

```py
>>> df.loc[[('cobra', 'mark ii')]]
               max_speed  shield
cobra mark ii          0       4
```

可以使用 tuple 指定 row label，然后再提供 column label：

```py
>>> df.loc[('cobra', 'mark i'), 'shield']
2
```

可以使用 tuple 和 单值 label 进行切片：

```py
>>> df
                     max_speed  shield
cobra      mark i           12       2
           mark ii           0       4
sidewinder mark i           10      20
           mark ii           1       4
viper      mark ii           7       1
           mark iii         16      36
>>> df.loc[('cobra', 'mark i'):'sidewinder']
                    max_speed  shield
cobra      mark i          12       2
           mark ii          0       4
sidewinder mark i          10      20
           mark ii          1       4
```

也可以使用两个 tuple label 进行切片：

```py
>>> df.loc[('cobra', 'mark i'):('viper', 'mark ii')]
                    max_speed  shield
cobra      mark i          12       2
           mark ii          0       4
sidewinder mark i          10      20
           mark ii          1       4
viper      mark ii          7       1
```

#### 位置（iloc）

```py
property DataFrame.iloc
```

`iloc` 是纯粹基于位置提取值的方法。

支持的输入包括：

- 整数，如 `5`；
- 整数列表或数组，如 `[4, 3, 0]`；
- 整数切片，如 `1:7`；
- boolean 数组；
- 返回以上有效索引的函数。

**例1**，选取单行

```py
>>> mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
>>> df = pd.DataFrame(mydict)
>>> df
      a     b     c     d
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000
>>> df.iloc[0]
a    1
b    2
c    3
d    4
Name: 0, dtype: int64
>>> type(df.iloc[0])
<class 'pandas.core.series.Series'>
```

此时返回 `Series` 类型。

**例2**，选择多行

此时 `iloc` 中使用整数列表，返回 `DataFrame` 对象

```py
>>> df.iloc[[0]]
   a  b  c  d
0  1  2  3  4
>>> type(df.iloc[[0]])
<class 'pandas.core.frame.DataFrame'>
>>> df.iloc[[0, 1]]
     a    b    c    d
0    1    2    3    4
1  100  200  300  400
```

**例3**，使用切片选择

```py
>>> df.iloc[:3]
      a     b     c     d
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000
```

**例4**，使用 boolean 列表

```py
>>> df
      a     b     c     d
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000
>>> df.iloc[[True, False, True]]
      a     b     c     d
0     1     2     3     4
2  1000  2000  3000  4000
```

**例5**，使用函数

```py
>>> df.iloc[lambda x: x.index % 2 == 0]
      a     b     c     d
0     1     2     3     4
2  1000  2000  3000  4000
```

**例7**，选择单行、单列

```py
>>> df
      a     b     c     d
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000
>>> df.iloc[0, 1]
2
```

**例8**，选择多行和多列

```py
>>> df.iloc[[0, 2], [1, 3]]
      b     d
0     2     4
2  2000  4000
```

**例9**，使用切片选择多行、多列

```py
>>> df.iloc[1:3, 0:3]
      a     b     c
1   100   200   300
2  1000  2000  3000
```

**例10**，混合使用 boolean 数组和切片

```py
>>> df.iloc[:, [True, False, True, False]]
      a     c
0     1     3
1   100   300
2  1000  3000
```

**例11**，在 column 索引中中使用函数

下面选择了第1列和第3列：

```py
>>> df.iloc[:, lambda df: [0, 2]]
      a     c
0     1     3
1   100   300
2  1000  3000
```

### 抽样（sample）

```py
DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None, ignore_index=False)
```

随机抽样。

`n` 指定返回的样本数：

- int，默认为 1，不能和 `frac` 同时使用。

`frac` 指定返回样本的比例：

- float，不能和 `n` 同时使用。

### 设置索引（set_index）

```py
DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)
```

将现有的 columns 设置为 index。

将一个或多个 columns 或 arrays (相同长度)设置为 index。新添加的 index 可以替换或扩展原有 index。

`keys` 用于指定索引：

- label，单个 column 的名称，指定对应的 column 为索引；
- array-like，和 `DataFrame` 等长的数组用作索引；
- list of labels，将多个 column 设置为 index；
- list of arrays，将多个 数组设置为 index；
- labels 和 arrays 的混合。

**例1**，设置单个 column 为 index

```py
>>> df = pd.DataFrame({'month': [1, 4, 7, 10],
                   'year': [2012, 2014, 2013, 2014],
                   'sale': [55, 40, 84, 31]})
>>> df
   month  year  sale
0      1  2012    55
1      4  2014    40
2      7  2013    84
3     10  2014    31
>>> df.set_index('month')
       year  sale
month            
1      2012    55
4      2014    40
7      2013    84
10     2014    31
```

**例2**，将多个 columns 设置为 index

```py
>>> df = df.set_index(['year', 'month'])
>>> df
            sale
year month      
2012 1        55
2014 4        40
2013 7        84
2014 10       31
>>> df.index
MultiIndex([(2012,  1),
            (2014,  4),
            (2013,  7),
            (2014, 10)],
           names=['year', 'month'])
```

可以看到，此时的 index 类型为 `MultiIndex`。

**例3**，混合使用 Index 和 column 创建索引

```py
>>> df
   month  year  sale
0      1  2012    55
1      4  2014    40
2      7  2013    84
3     10  2014    31
>>> df.set_index([pd.Index([1, 2, 3, 4]), 'year'])
        month  sale
  year             
1 2012      1    55
2 2014      4    40
3 2013      7    84
4 2014     10    31
```

**例4**，使用两个 `Series` 创建 `MultiIndex`

```py
>>> s = pd.Series([1, 2, 3, 4])
>>> df.set_index([s, s**2])
      month  year  sale
1 1       1  2012    55
2 4       4  2014    40
3 9       7  2013    84
4 16     10  2014    31
```

### 重置 index（reset_index）

```py
DataFrame.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
```

重置 `DataFrame` 的 index，使用默认 index。如果 `DataFrame` 包含 `MultiIndex`，使用该发方法可以移除一个或多个 index level。

**例1**，重置索引

重置 index 时，原 index 添加为 column，索引设置为基于位置的序列索引：

```py
>>> df = pd.DataFrame([('bird', 389.0),
                   ('bird', 24.0),
                   ('mammal', 80.5),
                   ('mammal', np.nan)],
                  index=['falcon', 'parrot', 'lion', 'monkey'],
                  columns=('class', 'max_speed'))
>>> df
         class  max_speed
falcon    bird      389.0
parrot    bird       24.0
lion    mammal       80.5
monkey  mammal        NaN
>>> df.reset_index()
    index   class  max_speed
0  falcon    bird      389.0
1  parrot    bird       24.0
2    lion  mammal       80.5
3  monkey  mammal        NaN
>>> 
```

**例2**，丢弃原 index

`drop` bool, 设置是否将原 index 丢弃，不添加为 column，默认为 False。

```py
>>> df.reset_index(drop=True)
    class  max_speed
0    bird      389.0
1    bird       24.0
2  mammal       80.5
3  mammal        NaN
```

**例3**，MultiIndex 重置索引

多 `MultiIndex`，可以使用 `level` 指定需要重置的 index：

```py
>>> index = pd.MultiIndex.from_tuples([('bird', 'falcon'),
                                   ('bird', 'parrot'),
                                   ('mammal', 'lion'),
                                   ('mammal', 'monkey')],
                                  names=['class', 'name'])
>>> columns = pd.MultiIndex.from_tuples([('speed', 'max'),
                                     ('species', 'type')])
>>> df = pd.DataFrame([(389.0, 'fly'),
                   ( 24.0, 'fly'),
                   ( 80.5, 'run'),
                   (np.nan, 'jump')],
                  index=index,
                  columns=columns)
>>> df
               speed species
                 max    type
class  name                 
bird   falcon  389.0     fly
       parrot   24.0     fly
mammal lion     80.5     run
       monkey    NaN    jump
>>> df.reset_index(level='class') # 重置 class 索引
         class  speed species
                  max    type
name                         
falcon    bird  389.0     fly
parrot    bird   24.0     fly
lion    mammal   80.5     run
monkey  mammal    NaN    jump
```

'class' 作为新的 column 加入，其名称默认以 col_level=0 加入。

**例4**，指定 column label 插入 level

在重置 MultiIndex 后，原 index 添加为新的 column，其名称作为 column 的 top level label，可以使用 `col_level` 修改该默认行为：

```py
>>> df.reset_index(level='class', col_level=1) # 以第二级 column level 插入
                speed species
         class    max    type
name                         
falcon    bird  389.0     fly
parrot    bird   24.0     fly
lion    mammal   80.5     run
monkey  mammal    NaN    jump
```

**例5**，对缺失的 column level，可以用 `col_fill` 指定缺失值：

```py
>>> df.reset_index(level='class', col_level=1, col_fill='species')
       species  speed species
         class    max    type
name                         
falcon    bird  389.0     fly
parrot    bird   24.0     fly
lion    mammal   80.5     run
monkey  mammal    NaN    jump
```

这里可以指定没有的 column label，pandas 会自动创建：

```py
>>> df.reset_index(level='class', col_level=1, col_fill='genus')
         genus  speed species
         class    max    type
name                         
falcon    bird  389.0     fly
parrot    bird   24.0     fly
lion    mammal   80.5     run
monkey  mammal    NaN    jump
```

### 重命名标签（rename）

```py
DataFrame.rename(mapper=None, index=None, columns=None, axis=None, copy=True, inplace=False, level=None, errors='ignore')
```

重命名的指定方式有两种：

- dict-like
- function

即通过字典或函数指定现有标签到新标签的映射关系。

`mapper` 支持两种类型调用方式：

- (index=index_mapper, columns=columns_mapper, ...)
- (mapper, axis={'index', 'columns'}, ...)

推荐使用第一个方式，使用关键字参数明确映射关系。

`axis` 用于指定应用 mapper 的轴：

- 0 或 'index' 对应行，默认值，`(mapper, axis=0)` 等价于 `index=mapper`；
- 1 或 'columns' 对应列，`(mapper, axis=1)` 等价于 `columns=mapper`。

**例1**，重命名 column

```py
>>> df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
>>> df
   A  B
0  1  4
1  2  5
2  3  6
>>> df.rename(columns={"A": "a", "B": "c"})
   a  c
0  1  4
1  2  5
2  3  6
```

**例2**，重命名 index

```py
>>> df.rename(index={0: "x", 1: "y", 2: "z"})
   A  B
x  1  4
y  2  5
z  3  6
```

**例3**，应用函数转换 index 类型

```py
>>> df.index
RangeIndex(start=0, stop=3, step=1)
>>> df.rename(index=str).index
Index(['0', '1', '2'], dtype='object')
```

**例4**，错误处理

`errors` 参数用于指定对错误的处理方式：

- 'ignore'，默认值，对已有的 key 重命名，未知的忽略；
- 'raise'，如果 dict 中包含未知 key，抛出 `KeyError`。

```py
>>> df
   A  B
0  1  4
1  2  5
2  3  6
>>> df.rename(columns={"A": "a", "B": "b", "C": "c"}, errors="raise")
Traceback (most recent call last):
......
KeyError: "['C'] not found in axis"
```

**例5**，使用 `axis` 风格语法，不推荐

```py
>>> df.rename(str.lower, axis='columns')
   a  b
0  1  4
1  2  5
2  3  6
>>> df.rename({1: 2, 2: 4}, axis='index')
   A  B
0  1  4
2  2  5
4  3  6
```

## 过滤

过滤和选择，从某种意义上来说是一样的。

### 单个布尔表达式

**例1**，过滤选择 'val' 值大于 0.5 的所有行：

```py
>>> df = pd.DataFrame({
      'name':['Jane','John','Ashley','Mike','Emily','Jack','Catlin'],
      'ctg':['A','A','C','B','B','C','B'],
      'val':np.random.random(7).round(2),
      'val2':np.random.randint(1,10, size=7)
    })
>>> df
     name ctg   val  val2
0    Jane   A  0.57     5
1    John   A  0.04     4
2  Ashley   C  0.69     6
3    Mike   B  0.25     1
4   Emily   B  0.18     5
5    Jack   C  0.72     9
6  Catlin   B  0.35     1
>>> df[df.val > 0.5]
     name ctg   val  val2
0    Jane   A  0.57     5
2  Ashley   C  0.69     6
5    Jack   C  0.72     9
```

**例2**，对字符串使用布尔表达式

```py
>>> df[df.name > 'Jane']
   name ctg   val  val2
1  John   A  0.04     4
3  Mike   B  0.25     1
```

### 组合逻辑运算

运算符 `|` 或 `or`, `&` 或 `and`, `~` 或 `not` 都可用于逻辑运算。

**例1**，执行 与 运算：

```py
>>> df
     name ctg   val  val2
0    Jane   A  0.57     5
1    John   A  0.04     4
2  Ashley   C  0.69     6
3    Mike   B  0.25     1
4   Emily   B  0.18     5
5    Jack   C  0.72     9
6  Catlin   B  0.35     1
>>> df[(df.val > 0.2) & (df.val2 == 1)]
     name ctg   val  val2
3    Mike   B  0.25     1
6  Catlin   B  0.35     1
```

**例2**，执行 或 运算：

```py
>>> df[(df.val < 0.5) | (df.val2 == 1)]
     name ctg   val  val2
1    John   A  0.04     4
3    Mike   B  0.25     1
4   Emily   B  0.18     5
6  Catlin   B  0.35     1
```

### isin

```py
DataFrame.isin(values)
```

用于检查 `DataFrame` 中的元素是否包含在 `values` 中，`values` 支持多种类型：

- `iterable`，包含待检查值的集合
- `Series`，index 要匹配
- `dict`，其 key 必须是 column 名称
- `DataFrame`，index 和 column labels 都要匹配

`isin` 返回一个包含 boolean 值的 `DataFrame`。

**例1**，iterable 参数

```py
>>> df = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]},
                  index=['falcon', 'dog'])
>>> df
        num_legs  num_wings
falcon         2          2
dog            4          0
>>> df.isin([0, 2])
        num_legs  num_wings
falcon      True       True
dog        False       True
```

**例2**，如果 `values` 是 `dict` 类型，则可以对不同列设置不同的检测值：

```py
>>> df
        num_legs  num_wings
falcon         2          2
dog            4          0
>>> df.isin({'num_wings': [0, 3]})
        num_legs  num_wings
falcon     False      False
dog        False       True
```

**例3**，如果 `values` 是 `Series` 或 `DataFrame` 类型，则 index 和 column 都要匹配

```py
>>> df
        num_legs  num_wings
falcon         2          2
dog            4          0
>>> other = pd.DataFrame({'num_legs': [8, 2], 'num_wings': [0, 2]},
                     index=['spider', 'falcon'])
>>> other
        num_legs  num_wings
spider         8          0
falcon         2          2                     
>>> df.isin(other)
        num_legs  num_wings
falcon      True       True
dog        False      False
```

**例4**，将 `isin` 生成的布尔向量传入 `DataFrame` 或 `Series`，就可以过滤数据

```py
>>> s = pd.Series(np.arange(5), index=np.arange(5)[::-1], dtype='int64')
>>> s
4    0
3    1
2    2
1    3
0    4
dtype: int64
>>> s.isin([2, 4, 6])
4    False
3    False
2     True
1    False
0     True
dtype: bool
>>> s[s.isin([2, 4, 6])]
2    2
0    4
dtype: int64
```

### filter

```py
DataFrame.filter(items=None, like=None, regex=None, axis=None)
```

根据指定的索引标签对行或列取子集。

> 该方法不对 DataFrame 的内容进行过滤，而是应用于索引标签。


## 重复值

### 查找重复值（duplicated）

```py
DataFrame.duplicated(subset=None, keep='first')
```

返回标记重复 row 的布尔 `Series`。

`subset` 用于指定查找重复值的 column，默认使用全部 column，即所有 column 值相同才认为是重复值。

`keep` 用于指定对重复值的处理方法：

- 'first' 表示除了第一个值，后续的重复值标记为 True，默认值；
- 'last' 表示除了最后一个值，余下重复值标记为 True；
- False 表示将所有重复值标记为 True。

**例1**，对重复值默认保留最先出现的值

```py
>>> df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})
>>> df
     brand style  rating
0  Yum Yum   cup     4.0
1  Yum Yum   cup     4.0
2  Indomie   cup     3.5
3  Indomie  pack    15.0
4  Indomie  pack     5.0
>>> df.duplicated()
0    False
1     True
2    False
3    False
4    False
dtype: bool
```

**例2**，对重复值，保留最后出现的值

```py
>>> df.duplicated(keep='last')
0     True
1    False
2    False
3    False
4    False
dtype: bool
```

**例3**，设置 `keep=False` 不保留任何重复值

```py
>>> df.duplicated(keep=False)
0     True
1     True
2    False
3    False
4    False
dtype: bool
```

**例4**，使用 `subset` 设置查找重复值的 columns

```py
>>> df
     brand style  rating
0  Yum Yum   cup     4.0
1  Yum Yum   cup     4.0
2  Indomie   cup     3.5
3  Indomie  pack    15.0
4  Indomie  pack     5.0
>>> df.duplicated(subset=['brand'])
0    False
1     True
2    False
3     True
4     True
dtype: bool
```

### 删除重复值（drop_duplicates）

```py
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
```

返回删除重复行的 `DataFrame`。

`subset` 用于设置检测重复 row 的 column，默认使用所有 column 的值。

`keep`用于指定如何处理重复值：

- 'first'，保留第一个；
- 'last'，保留最后一个；
- False，删除所有重复值。

**例1**，默认匹配所有 column 查找重复值

```py
>>> df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})
>>> df
     brand style  rating
0  Yum Yum   cup     4.0
1  Yum Yum   cup     4.0
2  Indomie   cup     3.5
3  Indomie  pack    15.0
4  Indomie  pack     5.0
>>> df.drop_duplicates()
     brand style  rating
0  Yum Yum   cup     4.0
2  Indomie   cup     3.5
3  Indomie  pack    15.0
4  Indomie  pack     5.0
```

**例2**，根据指定 column 查找重复值，即主要指定 column 值相同，就认为是重复的

使用 `subset` 设置查找的 column。

```py
>>> df.drop_duplicates(subset=['brand'])
     brand style  rating
0  Yum Yum   cup     4.0
2  Indomie   cup     3.5
```

**例3**，设置 `keep='last'`，对重复值保留最后出现的一项

```py
>>> df.drop_duplicates(subset=['brand', 'style'], keep='last')
     brand style  rating
1  Yum Yum   cup     4.0
2  Indomie   cup     3.5
4  Indomie  pack     5.0
```

## 设置值

### 基于标签设置（loc）

**例1**，选择特定位置设置值

```py
>>> df
            max_speed  shield
cobra               1       2
viper               4       5
sidewinder          7       8
>>> df.loc[['viper', 'sidewinder'], ['shield']] = 50
>>> df
            max_speed  shield
cobra               1       2
viper               4      50
sidewinder          7      50
```

**例2**，设置特定行的值

```py
>>> df
            max_speed  shield
cobra               1       2
viper               4      50
sidewinder          7      50
>>> df.loc['cobra'] = 10
>>> df
            max_speed  shield
cobra              10      10
viper               4      50
sidewinder          7      50
```

**例3**，设置特定列的值

```py
>>> df
            max_speed  shield
cobra              10      10
viper               4      50
sidewinder          7      50
>>> df.loc[:, 'max_speed'] = 30
>>> df
            max_speed  shield
cobra              30      10
viper              30      50
sidewinder         30      50
```

**例4**，根据函数设置值

```py
>>> df
            max_speed  shield
cobra              30      10
viper              30      50
sidewinder         30      50
>>> df.loc[df['shield'] > 35] = 0 # 将 shield 值 > 35 的所有行设置为 0
>>> df
            max_speed  shield
cobra              30      10
viper               0       0
sidewinder          0       0
```

## 添加

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

## 删除

### 使用标签删除（drop）

从行或列中删除指定标签。

```py
DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
```

通过标签名称、列名称、索引等删除行或列。当使用 MultiIndex 时，不同 level 的标签可以通过指定 level 删除。

`labels` 为标签或标签列表，用于指定待删除的 column 或 index labels。

`axis` 指定删除行或列：

- 0 or 'index' 对应行，默认；
- 1 或 'columns' 对应列。

`index` 删除 index 专用，`index=labels` 等价于 `(labels, axis=0)`。删除行时推荐。

`columns` 删除列专用，`columns=labels` 等价于 `(labels, axis=1)`。

`level` 用于 MultiIndex，指定删除的 index label。

**例1**，删除 'B', 'C' 两列

```py
>>> df = pd.DataFrame(np.arange(12).reshape(3, 4),
                  columns=['A', 'B', 'C', 'D'])
>>> df
   A  B   C   D
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
>>> df.drop(['B', 'C'], axis=1) # 等价于 drop(columns=['B', 'C'])
   A   D
0  0   3
1  4   7
2  8  11
```

**例2**，删除行

```py
>>> df
   A  B   C   D
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
>>> df.drop([0,1]) # axis 默认为0，即默认删除行
   A  B   C   D
2  8  9  10  11
```

**例3**，MultiIndex 删除操作

```py
>>> midx = pd.MultiIndex(levels=[['lama', 'cow', 'falcon'],
                             ['speed', 'weight', 'length']],
                     codes=[[0, 0, 0, 1, 1, 1, 2, 2, 2],
                            [0, 1, 2, 0, 1, 2, 0, 1, 2]])
>>> df = pd.DataFrame(index=midx, columns=['big', 'small'],
                  data=[[45, 30], [200, 100], [1.5, 1], [30, 20],
                        [250, 150], [1.5, 0.8], [320, 250],
                        [1, 0.8], [0.3, 0.2]])
>>> df
                 big  small
lama   speed    45.0   30.0
       weight  200.0  100.0
       length    1.5    1.0
cow    speed    30.0   20.0
       weight  250.0  150.0
       length    1.5    0.8
falcon speed   320.0  250.0
       weight    1.0    0.8
       length    0.3    0.2
>>> df.drop(index='cow', columns='small') # 删除 'cow' 行和 'small' 列
                 big
lama   speed    45.0
       weight  200.0
       length    1.5
falcon speed   320.0
       weight    1.0
       length    0.3
>>> df.drop(index='length', level=1) # 删除 level=1 的length 行
                 big  small
lama   speed    45.0   30.0
       weight  200.0  100.0
cow    speed    30.0   20.0
       weight  250.0  150.0
falcon speed   320.0  250.0
       weight    1.0    0.8
>>> 
```

### 删除缺失值

参考 [dropna](#移除缺失值dropna)。

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

## 转置

使用 `transpose()` 方法或 `.T` 属性可以获得 `DataFrame` 的转置，即调换行和列。

属性 `.T` 内部访问 `transpose()` 访问，效果一样。

```py
DataFrame.transpose(*args, copy=False)
```

> 对混合类型的 `DataFrame`，转置后类型变为 `object`，此时即使 `copy=False`，也会执行 `copy` 操作。

**例1**，所有列数据类型相同：

```py
>>> d = {'col1': [1, 2], 'col2': [3, 4]}
>>> df = pd.DataFrame(data=d)
>>> df
   col1  col2
0     1     3
1     2     4
>>> df_transposed = df.T
>>> df_transposed
      0  1
col1  1  2
col2  3  4
>>> df.dtypes
col1    int64
col2    int64
dtype: object
>>> df_transposed.dtypes
0    int64
1    int64
dtype: object
```

**例2**，混合类型：

```py
>>> cities
            City        Country  Population
0  New York City  United States     8600000
1          Paris         France     2141000
2      Barcelona          Spain     5515000
3           Rome          Italy     2873000
>>> cities.dtypes
City          object
Country       object
Population     int64
dtype: object
>>> cities_transposed = cities.T
>>> cities_transposed
                        0        1          2        3
City        New York City    Paris  Barcelona     Rome
Country     United States   France      Spain    Italy
Population        8600000  2141000    5515000  2873000
>>> cities_transposed.dtypes
0    object
1    object
2    object
3    object
dtype: object
```

转置后，类型全部变为 `object`。

## 排序

pandas 支持三种类型的排序：

- index label 排序
- column 值排序
- 以上两者组合排序

### 按索引排序（sort_index）

```py
DataFrame.sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, ignore_index=False, key=None)
```

如果 `inplace=False`，返回根据指定 label 排序后的新的 `DataFrame`，否则更新原 `DataFrame`，返回 `None`。

`axis` 用于指定排序的轴：

- 0 或 'index' 表示行，默认值；
- 1 或 'columns' 表示列。

**例1**，默认按照 index 排序：

```py
>>> df = pd.DataFrame([1, 2, 3, 4, 5], index=[100, 29, 234, 1, 150],
                  columns=['A'])
>>> df
     A
100  1
29   2
234  3
1    4
150  5
>>> df.sort_index()
     A
1    4
29   2
100  1
150  5
234  3
```

**例2**，降序排序

`ascending` 参数用于指定是否升序：

- bool 值，对单值排序，默认 True；
- bool list，对多值排序，对 MultiIndex 分别指定排序规则。

```py
>>> df.sort_index(ascending=False)
     A
234  3
150  5
100  1
29   2
1    4
```

**例3**，应用函数

`key` 参数用于指定应用到索引值的函数。

```py
>>> df = pd.DataFrame({"a": [1, 2, 3, 4]}, index=['A', 'b', 'C', 'd'])
>>> df.sort_index(key=lambda x: x.str.lower())
   a
A  1
b  2
C  3
d  4
```

### 按值排序（sort_values）

```py
DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
```

按指定 `axis` 对值进行排序。

`by` 参数用于指定排序的参考值，str 或 str list：

- 如果 `axis` 为 0 或 'index'，则 `by` 包含 index level 和 column labels；
- 如果 `axis` 为 1 或 'collumns'，则 `by` 包含 column levevls 和 index labels。

**例1**，按 'col1' 排序：

```py
>>> df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
    })
>>> df
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
>>> df.sort_values(by=['col1'])
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D
```

**例2**，按多列排序：

使用 `by` 可以指定 columns 名称列表，从而按多列排序。

```py
>>> df.sort_values(by=['col1', 'col2'])
  col1  col2  col3 col4
1    A     1     1    B
0    A     2     0    a
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D
```

**例3**，降序排序：

`ascending` 参数用于指定是否升序：

- bool，单值排序，默认 True；
- list of bool，针对多值排序，此时 ascending 列表长度和 by 一致。

```py
>>> df.sort_values(by='col1', ascending=False)
  col1  col2  col3 col4
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B
3  NaN     8     4    D
```

对 'col1' 升序，对 'col2' 降序：

```py
>>> df.sort_values(by=['col1', 'col2'], ascending=[True, False])
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D
```

**例4**，指定 NA 值得位置

使用 `na_position` 参数可以指定 NA 值的位置：

- 'first'，将 NA 值放在开头；
- 'last'，将 NA 值放在末尾，默认值。

```py
>>> df.sort_values(by='col1', ascending=False, na_position='first')
  col1  col2  col3 col4
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B
```

**例5**，在排序前对值应用函数

`key` 参数用于指定应用的函数，该 `key` 函数必须是向量化的，即参数和返回值都是 `Series` 类型，且长度相同。

```py
>>> df.sort_values(by='col4', key=lambda col: col.str.lower())
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
```

## 统计

### count

```py
DataFrame.count(axis=0, level=None, numeric_only=False)
```

计算每列/行的 non-NA 单元格数。

`axis` 用于指定计数行还是列：

- 0 或 'index'，针对每列计数，默认值
- 1 或 'columns'，针对每行计数

`level`  针对 `MultiIndex`，即对特定 level 计数：

- int，使用 level 位置指定 level；
- str, 使用 level 名称指定 level。

`numeric_only` 是否只对数值计数，包括 float, int 和 boolean 数据。

例如：

```py
>>> df = pd.DataFrame({
                   "Person": ["John", "Myla", "Lewis", "John", "Myla"],
                   "Age": [24., np.nan, 21., 33, 26],
                   "Single": [False, True, True, True, False]})
>>> df
  Person   Age  Single
0   John  24.0   False
1   Myla   NaN    True
2  Lewis  21.0    True
3   John  33.0    True
4   Myla  26.0   False
>>> df.count() # 默认对 column 计数
Person    5
Age       4
Single    5
dtype: int64
>>> df.count(axis='columns') # 指定对每行计数，稍微有点迷惑，这个 columns 表示统计每行各个 column 的 NaN 值个数
0    3
1    2
2    3
3    3
4    3
dtype: int64
```

### nunique

```py
DataFrame.nunique(axis=0, dropna=True)
```

计算指定 `axis` 不同元素的个数：

- 0 或 'index'，默认值
- 1 或 'columns'

`dropna` 默认 True，表示计数时不考虑 NaN 值。

返回 `Series` 类型，包含各个元素的个数。

**例1**，计算每列不同元素的个数

```py
>>> import pandas as pd
>>> df = pd.DataFrame({'A': [4, 5, 6], 'B': [4, 1, 1]})
>>> df
   A  B
0  4  4
1  5  1
2  6  1
>>> df.nunique()
A    3
B    2
dtype: int64
```

例2，计算每行不同元素的个数

```py
>>> df.nunique(axis=1)
0    1 # 第一行有 1 个
1    2 # 第二行有 2 个
2    2 # 第三行有 3 个
dtype: int64
```

## reshape

### nlargest

```py
DataFrame.nlargest(n, columns, keep='first')
```

以 `columns` 排序返回最大的 n 行，结果降序排列。

该方法等价于 `df.sort_values(columns, ascending=False).head(n)`，但是性能更好。

`n`, int 指定返回的行数；

`columns`, label 或 list of labels，指定排序的列；

`keep` 用于处理冗余值：

- 'first'，保留最先出现的值；
- 'last'，保留最后出现的值；
- 'all'，不剔除冗余值，全部保留。

该方法对 `object` 或 `category` 的 column 类型，抛出 `TypeError`。

## 转换

### 类型转换（astype）

```py
DataFrame.astype(dtype, copy=True, errors='raise')
```

转换数据类型。可以使用多种方式指定 dtype：

- 单个 numpy.dtype 或 Python type，表示转换整个 pandas 对象为 `dtype` 类型；
- 使用 {col:dtype,...} 字典类型，col 为 column 标签，表示将指定列转换为指定类型。

**例1**，转换所有 column 类型

将 `int64` 类型转换为 `int32`。

```py
>>> d = {'col1': [1, 2], 'col2': [3, 4]}
>>> df = pd.DataFrame(data=d)
>>> df.dtypes
col1    int64
col2    int64
dtype: object
>>> df.astype('int32').dtypes
col1    int32
col2    int32
dtype: object
```

**例2**，转换单个 column 类型

```py
>>> df.astype({'col1': 'int32'}).dtypes
col1    int32
col2    int64
dtype: object
```

**例3**，转换 `Series` 类型

`Series` 支持 astype 方法，可以直接使用该方法转换类型：

```py
>>> ser = pd.Series([1, 2], dtype='int32')
>>> ser
0    1
1    2
dtype: int32
>>> ser.astype('int64')
0    1
1    2
dtype: int64
```

## 缺失值

### 检测缺失值（isnull）

```py
DataFrame.isnull()
```

返回原对象等 size 的布尔 `DataFrame`。

**例1**，`DataFrame` 缺失值检测：

```py
>>> df = pd.DataFrame(dict(age=[5, 6, np.NaN],
                   born=[pd.NaT, pd.Timestamp('1939-05-27'),
                         pd.Timestamp('1940-04-25')],
                   name=['Alfred', 'Batman', ''],
                   toy=[None, 'Batmobile', 'Joker']))
>>> df
   age       born    name        toy
0  5.0        NaT  Alfred       None
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker
>>> df.isnull()
     age   born   name    toy
0  False   True  False   True
1  False  False  False  False
2   True  False  False  False
```

**例2**，`Series` 缺失值检测

```py
>>> ser = pd.Series([5, 6, np.NaN])
>>> ser
0    5.0
1    6.0
2    NaN
dtype: float64
>>> ser.isnull()
0    False
1    False
2     True
dtype: bool
```

### 检测非缺失值（notnull）

```py
DataFrame.notnull()
```

**例1**，检测 `DataFrame` 的非缺失值

```py
>>> df = pd.DataFrame(dict(age=[5, 6, np.NaN],
                   born=[pd.NaT, pd.Timestamp('1939-05-27'),
                         pd.Timestamp('1940-04-25')],
                   name=['Alfred', 'Batman', ''],
                   toy=[None, 'Batmobile', 'Joker']))
>>> df
   age       born    name        toy
0  5.0        NaT  Alfred       None
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker
>>> df.notnull()
     age   born  name    toy
0   True  False  True  False
1   True   True  True   True
2  False   True  True   True
```

**例2**，检测 `Series` 非缺失值

```py
>>> ser = pd.Series([5, 6, np.NaN])
>>> ser
0    5.0
1    6.0
2    NaN
dtype: float64
>>> ser.notna()
0     True
1     True
2    False
dtype: bool
```

### 检测缺失值（isna）

```py
DataFrame.isna()
```



### 删除缺失值（dropna）

```py
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
```

`axis` 用于确定移除行还是列：

- 0 或 'index'，移除包含缺失值的 row，默认；
- 1 或 'columns'，移除包含缺失值的 column。

`how` 用于选择方式：

- 'any'，只要有一个 NA 值，就移除；
- 'all'，所有值都是 NA 值，才移除。

`subset` 用于指定在哪些 column 或 row 查找缺失值。

`thresh` 用于指定最小 non-NA 值。

**例1**，移除包含缺失值的行

```py
>>> df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})
>>> df
       name        toy       born
0    Alfred        NaN        NaT
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT
>>> df.dropna()
     name        toy       born
1  Batman  Batmobile 1940-04-25
```

**例2**，移除包含缺失值的 column

```py
>>> df.dropna(axis='columns')
       name
0    Alfred
1    Batman
2  Catwoman
```

**例3**，移除所有值都缺失的 row

```py
>>> df.dropna(how='all')
       name        toy       born
0    Alfred        NaN        NaT
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT
```

**例4**，保留至少包含2个非缺失值的 row

```py
>>> df.dropna(thresh=2)
       name        toy       born
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT
```

**例5**，指定查找缺失值的 column

```py
>>> df.dropna(subset=['name', 'toy'])
       name        toy       born
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT
```

### fillna

```py
DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
```

使用指定方法填充 NA/NaN 值。

`value` 支持多种形式：

- 标量值；
- 指定特定 column 替换值得 `dict`, `Series` 或 `DataFrame`；  

对后一种参数形式，不在 dict 中的值不会被替换。

`method` 指定填充的方式：

- `backffill`/`bfill`，使用下一个有效值向上填充；
- `ffill` / `pad`，使用上一个有效值向下填充。
- `None`，默认行为。

`axis`：

- 0 或 `index`
- 1 或 `columns`

`limit`, int：

- 如果指定了 `method`，这是向前/向后连续填充 NaN 值得最大数目。换句话说，如果连续 NaN 值个数超过这个值，则只部分填充 NaN 值;
- 如果未指定 `method`，则是沿这个轴最大条目数。
- 如果不是 `None`，则必须大于 0.

**例1**，将 所有 NaN 替换为 0

```py
>>> import pandas as pd
>>> import numpy as np
>>> df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                       [3, 4, np.nan, 1],
                       [np.nan, np.nan, np.nan, 5],
                       [np.nan, 3, np.nan, 4]],
                     columns=list("ABCD"))
>>> df.fillna(0)
     A    B    C  D
0  0.0  2.0  0.0  0
1  3.0  4.0  0.0  1
2  0.0  0.0  0.0  5
3  0.0  3.0  0.0  4
```

**例2**，向前填充：

```py
>>> df
     A    B   C  D
0  NaN  2.0 NaN  0
1  3.0  4.0 NaN  1
2  NaN  NaN NaN  5
3  NaN  3.0 NaN  4
>>> df.fillna(method="ffill")
    A   B   C   D
0   NaN 2.0 NaN 0
1   3.0 4.0 NaN 1
2   3.0 4.0 NaN 5
3   3.0 3.0 NaN 4
```

**例3**，替换 column 'A', 'B', 'C' 和 'D' 列的 NaN 值，分别替换为 0， 1， 2， 3：

```py
>>> values = {"A": 0, "B": 1, "C": 2, "D": 3}
>>> df.fillna(value=values)
    A   B   C   D
0   0.0 2.0 2.0 0
1   3.0 4.0 2.0 1
2   0.0 1.0 2.0 5
3   0.0 3.0 2.0 4
```

### 替换（replace）

```py
DataFrame.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad')
```

将 `to_replace` 替换为 `value`。

`to_place` 支持多种类型，单值类型：

- str，待替换的字符串；
- numeric，替换和 `to_replace` 相同的数字；
- regex，匹配的正则表达式

列表类型：

- 如果 `to_place` 和 `value` 都是 list，它们长度必须相同；
- 如果 `regex=True`，两个 list 中的字符串都作为 regex 解析，否则直接作为字符串解析

**例1**，标量值替换

```py
>>> s = pd.Series([0, 1, 2, 3, 4])
>>> s.replace(0, 5)
0    5
1    1
2    2
3    3
4    4
dtype: int64
>>> df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})
>>> df
   A  B  C
0  0  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e
>>> df.replace(0, 5)
   A  B  C
0  5  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e
```

**例2**，`to_replace` 为 list 类型，`value` 为单个值，所有值被替换为指定值

```py
>>> df
   A  B  C
0  0  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e
>>> df.replace([0, 1, 2, 3], 4)
   A  B  C
0  4  5  a
1  4  6  b
2  4  7  c
3  4  8  d
4  4  9  e
```

**例3**，`to_replace` 和 `value` 都是 list，两者长度相同，替换值一一对应

```py
>>> df
   A  B  C
0  0  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e
>>> df.replace([0, 1, 2, 3], [4, 3, 2, 1])
   A  B  C
0  4  5  a
1  3  6  b
2  2  7  c
3  1  8  d
4  4  9  e
```

**例4**，可以不指定 `value`，用 `method` 设置值：

- 'pad'
- 'ffill'
- 'bfill'，用后面的值替换前面需要替换的值
- None

```py
>>> s
0    0
1    1
2    2
3    3
4    4
dtype: int64
>>> s.replace([1, 2], method='bfill')
0    0
1    3
2    3
3    3
4    4
dtype: int64
```

**例5**，如果使用 dict 类型，可以指定替换值的对应关系

```py
>>> df
   A  B  C
0  0  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e
>>> df.replace({0: 10, 1: 100})
     A  B  C
0   10  5  a
1  100  6  b
2    2  7  c
3    3  8  d
4    4  9  e
```

**例6**，使用 dict 还可以指定不同列的替换值

将 A 列的 0 和 B 列的 5 替换为 100.

```py
>>> df.replace({'A': 0, 'B': 5}, 100)
     A    B  C
0  100  100  a
1    1    6  b
2    2    7  c
3    3    8  d
```

**例7**，使用嵌套 dict，可以指定不同列不同值的替换关系

将 A 列的 0 替换为 100；A 列的 4 替换为 400.

```py
>>> df
   A  B  C
0  0  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e
>>> df.replace({'A': {0: 100, 4: 400}})
     A  B  C
0  100  5  a
1    1  6  b
2    2  7  c
3    3  8  d
4  400  9  e
```

## 参考

- https://pandas.pydata.org/docs/reference/frame.html
- Pandas in Action.Boris Paskhaver.MANNING.2021
