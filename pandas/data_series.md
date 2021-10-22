# Series

- [Series](#series)
  - [简介](#简介)
  - [创建 Series](#创建-series)
    - [data 参数](#data-参数)
    - [index 参数](#index-参数)
    - [dtype 参数](#dtype-参数)
    - [`Series` 和 `ndarray` 类似](#series-和-ndarray-类似)
  - [Series 常用属性](#series-常用属性)
    - [name](#name)
    - [index](#index)
    - [values](#values)
  - [Series 常用方法](#series-常用方法)
    - [基本数组操作](#基本数组操作)
    - [应用 Python 内置函数](#应用-python-内置函数)
  - [函数应用](#函数应用)
    - [值函数应用-apply](#值函数应用-apply)
  - [查询方法](#查询方法)
    - [head](#head)
    - [tail](#tail)
  - [索引和选择](#索引和选择)
    - [默认索引](#默认索引)
    - [设置索引](#设置索引)
    - [选择值](#选择值)
    - [reset_index](#reset_index)
  - [排序](#排序)
    - [按值排序](#按值排序)
      - [值顺序](#值顺序)
      - [na 值位置](#na-值位置)
      - [字符串值排序](#字符串值排序)
      - [排序前处理值](#排序前处理值)
    - [按 index 排序](#按-index-排序)
  - [label 对齐](#label-对齐)
  - [缺失值处理](#缺失值处理)
    - [dropna](#dropna)
    - [isnull](#isnull)
    - [fillna](#fillna)
  - [数学运算](#数学运算)
    - [add](#add)
    - [mul](#mul)
    - [round](#round)
  - [统计计算](#统计计算)
    - [between](#between)
    - [eq](#eq)
    - [ne](#ne)
    - [cumsum](#cumsum)
    - [count](#count)
    - [pct_change](#pct_change)
    - [unique](#unique)
    - [nunique](#nunique)
    - [非冗余值计数和区间计数](#非冗余值计数和区间计数)
    - [获得最大的 n 个值](#获得最大的-n-个值)
    - [获得最小的 n 个值](#获得最小的-n-个值)
  - [广播](#广播)
  - [原位操作](#原位操作)
  - [参考](#参考)
    - [map](#map)
    - [Series.equals](#seriesequals)

2020-04-21, 14:34
***

## 简介

Pandas 中 `Series` 为一维标记数组。其基本特征为：

- 可以保存任意数据类型；
- 一个 `Series` 只能保存一种类型的数据。

`Series` 是 `ndarray` 的子类，所以包含 `ndarray` 的所有方法。

作为标记数据，每个数据还有一个标签，所以 `Series` 访问数据方式有两种:

- 通过位置索引
- 通过标签

标签不需要唯一，但是必须是可哈希类型。

## 创建 Series

构造函数：

```py
class pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
```

创建空 `Series`：

```py
import pandas as pd

pd.Series()

# DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
```

> 由于没有提供任何值，Pandas 无法推断数据类型，因此输出如上所示的警告信息。

### data 参数

参数 `data` 提供创建 `Series` 的数据，支持类型有：

- array-like
- iterable
- dict
- scalar value

**例1**，`list` 是 iterable 对象，可用于创建 `Series`：

```py
>>> import pandas as pd
>>> cities = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen']
>>> city_series = pd.Series(cities)
>>> city_series
0      Beijing
1     Shanghai
2    Guangzhou
3     Shenzhen
dtype: object
```

**例2**，使用 `dict` 对象创建 `Series`：

说明：通过 `dict` 创建 `Series`

- 如果未指定 `index`, 则 `dict` 的 `key` 自动转换为 `index`；
- 如果指定了 `index`，则以 `index` 作为键值从 dict 取值创建 Series，如果 dict 中没有对应的键值，则以 NaN 作为结果。

不指定 `index`，以字典的 key 作为 index：

```py
>>> d1 = {'Mon': 33, 'Tue': 19, 'Wed': 15}
>>> s = pd.Series(d1)
>>> s
Mon    33
Tue    19
Wed    15
dtype: int64
```

指定 `index`，`Series` 按照 `index` 的顺序排列，没有的值采用 `NaN`：

```py
>>> d1 = {'Mon': 33, 'Tue': 19, 'Wed': 15}
>>> s = pd.Series(d1, index=['Tue', 'Wed', 'Fri'])
>>> s
Tue    19.0
Wed    15.0
Fri     NaN
dtype: float64
```

可以看到，`Series` 的索引和提供的 `index` 完全一样，由于索引值没有 `'Mon'`，所以输出的 `Series` 也没有；由于 dict 中没有 `'Fri'` 键，生成的 `Series` 中对应的值为 `NaN`。

**例3**，pandas 对缺失值统一用 `NaN` 表示：

```py
>>> import numpy as np

>>> temperatures = [94, 88, np.nan, 91]
>>> pd.Series(temperatures)
0    94.0
1    88.0
2     NaN
3    91.0
dtype: float64
```

> 在遇到 `NaN` 时 pandas 自动将类型转换为 `float64`，而不是我们期望的 `int64`。

**例4**，`tuple` 是可迭代类型，可以用来创建 `Series`：

```py
>>> color = ('Red', 'Green', 'Blue')
>>> pd.Series(color)
0      Red
1    Green
2     Blue
dtype: object
```

**例5**，如果希望 `Series` 保存 `tuple`，可以将 `tuple` 包装在 `list` 中：

```py
>>> rgb_colors = [(120, 41, 26), (196, 165, 45)]
>>> pd.Series(rgb_colors)
0     (120, 41, 26)
1    (196, 165, 45)
dtype: object
```

**例6**，`set` 是无序非冗余集合，`Series` 是有序集合类型，不支持直接从 `set` 创建：

```py
>>> a_set = {"Beijing", "Shanghai"}
>>> pd.Series(a_set)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    pd.Series(a_set)
  File "D:\Python\Python39\lib\site-packages\pandas\core\series.py", line 439, in __init__
    data = sanitize_array(data, index, dtype, copy)
  File "D:\Python\Python39\lib\site-packages\pandas\core\construction.py", line 559, in sanitize_array
    raise TypeError(f"'{type(data).__name__}' type is unordered")
TypeError: 'set' type is unordered
```

**例7**，可以用 numpy 的 `ndarray` 提供数据：

```py
>>> random_data = np.random.randint(1, 101, 10)
>>> random_data
array([34, 38, 15, 77, 32, 68, 40, 34, 97, 29])
>>> pd.Series(random_data)
0    34
1    38
2    15
3    77
4    32
5    68
6    40
7    34
8    97
9    29
dtype: int32
```

### index 参数

`index` 是轴标签，为 array-like 或 `Index` 类型（1d）。

- `index` 的值必须为可哈希类型，长度和 `data` 等长；
- 允许重复值；
- 如果未提供索引，默认为 `RangeIndex(0, 1, 2, .., n)`；
- 如果 `data` 是 dict-like 类型，`index` 为 `None`，则将字典 key 作为 index；
- 如果 `index` 不为 `None`，生成的 `Series` 会根据 index 值重新索引。

**例1**，自定义索引，索引长度和数据长度必须相同：

```py
>>> data = [33, 19, 14, 89, 11, -5, 9]
>>> index = ['Mon', "Tue", 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
>>> s = pd.Series(data, index=index)
>>> s
Mon    33
Tue    19
Wed    14
Thu    89
Fri    11
Sat    -5
Sun     9
dtype: int64
```

这里将 `index` 设置为一周的每一天。

通过 `Series.index` 属性可以查看索引：

```py
>>> s.index
Index(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], dtype='object')
```

**例2**，索引允许重复值：

```py
>>> data = [33, 19, 14, 89, 11, -5, 9]
>>> index = ['Mon', "Mon", 'Mon', 'Thu', 'Fri', 'Sat', 'Sun']
>>> s = pd.Series(data, index=index)
>>> s
Mon    33
Mon    19
Mon    14
Thu    89
Fri    11
Sat    -5
Sun     9
dtype: int64
```

> 虽然允许重复值，但是建议尽可能避免。

**例3**，如果不提供索引，默认为顺序整数：

```py
>>> cities = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen']
>>> city_series = pd.Series(cities)
>>> city_series
0      Beijing
1     Shanghai
2    Guangzhou
3     Shenzhen
dtype: object
>>> city_series.index
RangeIndex(start=0, stop=4, step=1)
```

### dtype 参数

用于指定 `Series` 的数据类型，`dtype`默认为 `None`，此时 pandas 会根据提供的数据 `data` 自动推断数据类型。

`dtype` 支持三种类型：`str`, `numpy.dtype` 以及 `ExtensionDtype`。

例如：

```py
>>> lucky_numbers = [4, 7, 8, 27]
>>> pd.Series(lucky_numbers, dtype = 'float')
0     4.0
1     7.0
2     8.0
3    27.0
dtype: float64
```

### `Series` 和 `ndarray` 类似

- 例：演示 Series 类似于 ndarray 的操作

```py
s=pd.Series(np.random.randn(5),index=['a','b','c','d','e'])s
```

Out:

```cmd
a   -1.184990
b   -0.404359
c    0.636425
d   -0.750244
e    0.957961
dtype: float64
```

- np 函数操作
```
np.exp(s)
```
Out:
```
a    0.305749
b    0.667405
c    1.889713
d    0.472251
e    2.606376
dtype: float64
```

- 使用 index label切片
```
s['b':'d']
```
Out
```
b   -0.404359
c    0.636425
d   -0.750244
dtype: float64
```

- 使用 index pos 获得特定位置的值：

| 操作 | 说明             |
| ----- | ------------- |
| s[0]               | 获得第一个值     |
| s[0]=100           | 使用 offset 为 s复制 |
| s.index            | 获得 Series 的 index 信息  |
| s[:3]              | 获得 Series 的前三个值   |
| s['a']             | 获得 Series 和 a (index label)对应的值，如果s中不存在该label，抛出 KeyError |
| 'e' in s           | s 中是否包含 'e' (index label)                                              |
| s.get('f')         | 获得和'f'对应的值，如果不存在在 index label，返回 None.                     |
| s.get('f', np.nan) | 获得和 'f' 对应的值，如果不存在，返回 np.nan.                               |
| s[s>s.median()]    | 返回大于 s 中值的所有值                                                     |

## Series 常用属性

|属性|说明|
|---|---|
|`Series.dtype`|底层数据的 `dtype` 类型|
|`Series.shape`|以 tuple 类型返回数据 shape|
|`Series.size`|数据个数|
|`Series.is_unique`|如果不包含重复值，返回 True|
|`Series.is_monotonic`|如果值是单调递增的，返回 True|

### name

`Series` 名称。

在 `DataFrame` 中，Series.name 作为 `Series` 的 index 或 column 名称使用。

例如，可以在创建 `Series` 通过 `name` 参数指定名称，而且可以随时通过该属性修改：

```py
>>> s = pd.Series([1, 2, 3], dtype=np.int64, name='Numbers')
>>> s
0    1
1    2
2    3
Name: Numbers, dtype: int64
>>> s.name = "Integers" # 修改 name
>>> s
0    1
1    2
2    3
Name: Integers, dtype: int64
```


### index

返回 `Series` 的 index（轴标签）。例如：

```py
>>> color = pd.Series(['Red', 'Green', 'Blue'])
>>> color.index
RangeIndex(start=0, stop=3, step=1)
>>> type(color.index)
<class 'pandas.core.indexes.range.RangeIndex'>
```

可以看到，默认索引为 `RangeIndex` 类型。

而自义定的 `index` 为 `pandas.core.indexes.base.Index` 类型：

```py
>>> s = pd.Series([2, 3, 1], index=["Two", "Three", "One"])
>>> s.index
Index(['Two', 'Three', 'One'], dtype='object')
>>> type(s.index)
<class 'pandas.core.indexes.base.Index'>
```

### values

以 `ndarray` 或 `ndarray-like` 类型返回 `Series` 包含的数据。

> pandas 不建议通过该属性获得底层数据，建议用 `Series.array` 属性查看底层数据，用 `Series.to_numpy` 获得相同数据的 `ndarray` 类型。

**例1**，返回 `int64` 类型的 `ndarray`：

```py
>>> pd.Series([1, 2, 3]).values
array([1, 2, 3], dtype=int64)
```

**例2**，字符串对应 `object` 类型的 `ndarray`：

```py
>>> pd.Series(list('aabc')).values
array(['a', 'a', 'b', 'c'], dtype=object)
```

**例3**，分类类型则以 `Categories` 存储：

```py
>>> pd.Series(list('aabc')).astype('category').values
['a', 'a', 'b', 'c']
Categories (3, object): ['a', 'b', 'c']
```

## Series 常用方法

| 操作 | 说明 |
| --- | --- |
| s[0] | 获得第一个值  |
| s[0]=100           | 使用 offset 为 s复制  |
| s.index            | 获得 Series 的 index 信息                                                   |
| s[:3]              | 获得 Series 的前三个值                                                      |
| s['a']             | 获得 Series 和 a (index label)对应的值，如果s中不存在该label，抛出 KeyError |
| 'e' in s           | s 中是否包含 'e' (index label)                                              |
| s.get('f')         | 获得和'f'对应的值，如果不存在在 index label，返回 None.                     |
| s.get('f', np.nan) | 获得和 'f' 对应的值，如果不存在，返回 np.nan.                               |
| s[s>s.median()]    | 返回大于 s 中值的所有值    |
| s.iloc[:3]         | 返回前三个值   |
| s.iloc[:3]=0       | 前三个设置为0     |
| s.iloc[3]          | 返回第4个值     |
| s.iloc[start:end]  | 切片，即使超过范围也没事儿  |
| s.sort_index()     | 按照 index label 进行排序，返回排序后的 Series，原Series不变  |

### 基本数组操作

### 应用 Python 内置函数

- `len(Series)` 返回 `Series` 包含的元素个数，包括 nan 值。

```py
>>> cities = pd.Series(['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', np.nan])
>>> len(cities)
5
```

- `type(Series)` 返回 `Series` 的类型

```py
>>> type(cities)
<class 'pandas.core.series.Series'>
```

- `dir` 函数以字符串的形式返回对象的属性和方法列表

```py
>>> dir(cities)
['T',
 '_AXIS_LEN', 
 '_AXIS_ORDERS', 
 '_AXIS_REVERSED', 
 'squeeze', 
  ..., 
  'values', 
  'var', 
  'view', 
  'where', 
  'xs']
```

由于值太多，输出中省略了中间的属性和方法值。

- `list` 使用 `Series` 的值生成一个新的 `list`

```py
>>> list(cities)
['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', nan]
```

- `dict` 使用 `Series` 的 index 和 values 创建字典

```py
>>> dict(cities)
{0: 'Beijing', 1: 'Shanghai', 2: 'Guangzhou', 3: 'Shenzhen', 4: nan}
```

- 使用 `in` 关键字查询 `Series` 的 **index** 是否包含指定值

```py
>>> cities
0      Beijing
1     Shanghai
2    Guangzhou
3     Shenzhen
4          NaN
dtype: object
>>> 'Beijing' in cities
False
>>> 0 in cities
True
```

如果要查询 `Series` 是否包含指定值，可以用 `Series.values` 属性，该属性的 `ndarray` 对象也支持 `in` 查询操作：

```py
>>> 'Beijing' in cities.values
True
```

## 函数应用

### 值函数应用-apply

```py
Series.apply(self, func, convert_dtype=True,args=(), **kwds)
```

对 `Series` 的值分别应用函数。`func` 可以是 ufunc（应用于整个 `Series` 的 NumPy 函数），也可以是应用于单值的 Python 函数。

| 参数| 类型 | 说明 |
| --- | --- | --- |
| func | function | 应用的 Python 函数或 NumPy ufunc 函数|
| convert_dtype: | bool, default `True` | 根据函数返回值尝试找到合适的数据类型。如果为 `False`，`dtype=object` |
| args  | tuple | 在 `Series` 值后面传递给函数的位置参数 |
| **kwds         |   | 传递给函数的额外参数 |

返回值：`Series` 或 `DataFrame`

对每个值应用函数后，返回的值组成一个新的 `Series` 返回。如果应用的函数返回类型为 `Series`，则返回值为 `DataFrame` 类型。

**例1**，应用 `round` 函数：

```py
>>> s = pd.Series([20.1, 21.2, 12.6], index=['Beijing', 'Shanghai', 'Shenzhen'])
>>> s
Beijing     20.1
Shanghai    21.2
Shenzhen    12.6
dtype: float64
>>> s.apply(round)
Beijing     20
Shanghai    21
Shenzhen    13
dtype: int64
```

**例2**，`apply` 也可以使用自定义函数

```py
>>> def square(x):
       return x ** 2

>>> s.apply(square)
Beijing     404.01
Shanghai    449.44
Shenzhen    158.76
dtype: float64
```

例如：

```py
def test_apply():
    s = pd.Series([20, 21, 12], index=['London', 'New York', 'Helsinki'])

    def square(x):
        return x ** 2

    s1 = s.apply(square)
    np.array_equal(s.values, np.array([20, 21, 12]))
    np.array_equal(s1.values, np.array([400, 441, 144]))
```

- 采用匿名函数

```py
def test_apply_lambda():
    s = pd.Series([20, 21, 12], index=['London', 'New York', 'Helsinki'])
    s1 = s.apply(lambda x: x ** 2)
    np.array_equal(s1.values, np.array([400, 441, 144]))
```

- 采用多个参数

```py
def test_apply_args():
    def subtract_custom_value(x, custom_value):
        return x - custom_value

    s = pd.Series([20, 21, 12])
    s1 = s.apply(subtract_custom_value, args=(5,))
    np.array_equal(s1.values, np.array([15, 16, 7]))
```

- 采用关键字参数

```py
def test_apply_keyword():
    def add_custom_values(x, **kwargs):
        for month in kwargs:
            x += kwargs[month]
        return x

    s = pd.Series([20, 21, 12])
    s1 = s.apply(add_custom_values, june=30, july=20, august=25)
    np.array_equal(s1.values, np.array([95, 96, 87]))
```

- 采用 Numpy 库函数

```py
def test_apply_numpy_func():
    s = pd.Series([20, 21, 12])
    s1 = s.apply(np.log)
```


## 查询方法

### head

```py
Series.head(n=5)
```

返回 `Series` 的前 `n` 行。由于 `Series` 只有一列，所以返回前 `n` 个元素。

- n 默认为 5；
- 如果 `n` 为负值，则返回除最后 `n` 行的所有值，等价于 `series[:-n]`。

该方法在快速查询数据类型十分有用。

```py
>>> nums = pd.Series(range(0, 500, 5))
>>> nums
0       0
1       5
2      10
3      15
4      20
     ... 
95    475
96    480
97    485
98    490
99    495
Length: 100, dtype: int64
>>> nums.head(3) # 返回前 3 行
0     0
1     5
2    10
dtype: int64
>>> nums.head() # n 默认为 5
0     0
1     5
2    10
3    15
4    20
dtype: int64
>>> nums.head(-10) # 除最后 10 行的所有值
0       0
1       5
2      10
3      15
4      20
     ... 
85    425
86    430
87    435
88    440
89    445
Length: 90, dtype: int64
```

### tail

```py
Series.tail(n=5)
```

`tail` 返回 `Series` 的后 `n` 行。和 [head](#head) 对应的方法。

- n 默认为 5；
- 如果 n 为负值，在返回除前 n 行的所有数据，登记员 `series[n:]`。

`tail` 适合于在排序或附加数据后快速验证。


## 索引和选择

`Series` 可以看作定长、有序的 dict，实现索引到值的映射。例如：

```py
In [1]: obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
In [2]: 'b' in obj2
Out[2]: True
In [3]: 'e' in obj2
Out[3]: False
```

### 默认索引

例如：

```py
In [1]: obj = pd.Series([4, 7, -5, 3])
In [2]: obj
Out[2]: 
0    4
1    7
2   -5
3    3
dtype: int64
```

虽然我们没有指定索引，依然有默认索引，值为 0 到 N-1。

可以使用 `values` 和 `index` 索引查询值和索引：

```py
In [13]: obj.values
Out[13]: array([ 4,  7, -5,  3])

In [14]: obj.index  # like range(4)
Out[14]: RangeIndex(start=0, stop=4, step=1)
```

### 设置索引

```py
In [15]: obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

In [16]: obj2
Out[16]: 
d    4
b    7
a   -5
c    3
dtype: int64

In [17]: obj2.index
Out[17]: Index(['d', 'b', 'a', 'c'], dtype='object')
```

应该注意，指定的字符串索引类型，和默认索引的 `RangeIndex` 类型不同。

通过索引可以选择及设置值：

```py
In [18]: obj2['a']
Out[18]: -5

In [19]: obj2['d'] = 6 # 将索引 d 处的值设置为 6

In [20]: obj2[['c', 'a', 'd']] # 选择索引列表对应的所有值
Out[20]: 
c    3
a   -5
d    6
dtype: int64
```

### 选择值

使用 NumPy 函数或类似 NumPy 的操作，如 boolean 数字过滤、标量乘法、应用函数等，索引和值的对应关系不变：

```py
In [15]: obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
In [21]: obj2[obj2 > 0] # 选择所有 > 0 的值
Out[21]: 
d    6
b    7
c    3
dtype: int64

In [22]: obj2 * 2 # 标量乘法
Out[22]: 
d    12
b    14
a   -10
c     6
dtype: int64

In [23]: np.exp(obj2) # 指数
Out[23]: 
d     403.428793
b    1096.633158
a       0.006738
c      20.085537
dtype: float64
```


### reset_index

`Series.reset_index(self, level=None, drop=False, name=None, inplace=False)`

创建重置 index的 Series 或 DataFrame。

当需要将 index 添加为 column 时很有用，或者去除无意义的 index，将其重置为默认值。

1. level: int, str, tuple, or list, default optional

对 `MultiIndex`的 `Series`，只移除指定 level 的 index。默认移除所有 levels.

2. drop: bool, default False

如果为 true，直接舍弃 index，而不添加为 column。

3. name: object, optional

原 Series 值对应column 名称，默认为`self.name`。如果 `drop` 为 True，则不添加新列，所以返回值为 `Series`，就不需要该参数，直接忽略。

4. inplace: bool, default False

修改原 `Series`，而不创建新对象。

**返回**：Series 或 DataFrame

- 如果 `drop` 为 False (默认值)，返回 DataFrame。新添加的 column 为 DataFrame 的第一列，随后是原 `Series` 的值。
- 如果 `drop` 为 True，返回 Series。
- 如果 `inplace=True`，不返回值。

例如：

```py
>>> s = pd.Series([1, 2, 3, 4], name='foo',
              index=pd.Index(['a', 'b', 'c', 'd'], name='idx'))
```

- `drop` 默认为 false，即默认返回 DataFrame，新的 column 名称为 index 中 `Index` 的 `name` 字段，原 Series 的 column 名称为 Series 的 `name` 字段。

```py
>>> s.reset_index()
  idx  foo
0   a    1
1   b    2
2   c    3
3   d    4
```

- 使用 `name` 参数修改原 `Series` 值的 column 名称：

```py
>>> s.reset_index(name='values')
  idx  values
0   a       1
1   b       2
2   c       3
3   d       4
```

- 将 `drop` 设置为 True，获得新的 Series

```py
>>> s.reset_index(drop=True)
0    1
1    2
2    3
3    4
Name: foo, dtype: int64
```

- 将 `replace` 设置为 True，不返回值，修改原 Series

```py
>>> s.reset_index(inplace=True, drop=True)
>>> s
0    1
1    2
2    3
3    4
Name: foo, dtype: int64
```

对包含多层 index 的 `Series` 对象，`level` 参数很有用

```py
>>> arrays = [np.array(['bar', 'bar', 'baz', 'baz']),
          np.array(['one', 'two', 'one', 'two'])]
>>> s2 = pd.Series(range(4), name='foo',
    index=pd.MultiIndex.from_arrays(arrays, names=['a', 'b']))
```

- 移除指定 level 的 index

```py
>>> s2.reset_index(level='a')
       a  foo
b
one  bar    0
two  bar    1
one  baz    2
two  baz    3
```

- 如果不指定 level，移除所有 index

```py
>>> s2.reset_index()
     a    b  foo
0  bar  one    0
1  bar  two    1
2  baz  one    2
3  baz  two    3
```

## 排序

### 按值排序

使用 `sort_values` 方法对值进行排序。

```py
Series.sort_values(axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
```

该方法值排序后的一个新的 `Series`。

#### 值顺序

`ascending` 参数用于控制排序顺序。

**例1**，默认升序排序：

```py
>>> import pandas as pd
>>> import numpy as np
>>> s = pd.Series([np.nan, 1, 3, 10, 5])
>>> s
0     NaN
1     1.0
2     3.0
3    10.0
4     5.0
dtype: float64
>>> s.sort_values(ascending=True) # 默认 ascending=True，可以省略该参数
1     1.0
2     3.0
4     5.0
3    10.0
0     NaN
dtype: float64
```

**例2**，降序排序：

```py
>>> s.sort_values(ascending=False)
3    10.0
4     5.0
2     3.0
1     1.0
0     NaN
dtype: float64
```

#### na 值位置

`na_position` 参数用于控制 NaN 的位置，可选值：

- 'first'，将 NaN 值放在开头
- 'last' 将 NaN 值放在结尾，默认

例如：

```py
>>> s = pd.Series([np.nan, 1, 3, 10, 5])
>>> s
0     NaN
1     1.0
2     3.0
3    10.0
4     5.0
dtype: float64
>>> s.sort_values() # NaN 值默认在结尾
1     1.0
2     3.0
4     5.0
3    10.0
0     NaN
dtype: float64
>>> s.sort_values(na_position='first') # 将 NaN 值放在开头
0     NaN
1     1.0
2     3.0
4     5.0
3    10.0
dtype: float64
```

#### 字符串值排序

字符串默认按照字母顺序排序，大小字母比小写字母靠前：

```py
>>> s = pd.Series(['z', 'b', 'd', 'A','a', 'c'])
>>> s
0    z
1    b
2    d
3    A
4    a
5    c
dtype: object
>>> s.sort_values()
3    A
4    a
1    b
5    c
2    d
0    z
dtype: object
```

#### 排序前处理值

`key` 参数用于指定应用于值的函数，在排序前与 series 值先进行处理。`key` 函数必须是向量化的，即以 `Series` 为参数，返回 array-like 对象。例如：

```py
>>> s = pd.Series(['a', 'B', 'c', 'D', 'e'])
>>> s.sort_values()
1    B
3    D
0    a
2    c
4    e
dtype: object
>>> s.sort_values(key=lambda x: x.str.lower()) # 将值转换为小写再排序
0    a
1    B
2    c
3    D
4    e
dtype: object
```

### 按 index 排序

```py
Series.sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, ignore_index=False, key=None)
```

`sort_index`  用于按索引进行排序。

`sort_index` 的方法签名和 `sort_values` 基本一致，参数的功能也几近相同。

**例1**，按索引排序，默认升序：

```py
>>> s = pd.Series(['a', 'b', 'c', 'd'], index=[3, 2, 1, 4])
>>> s
3    a
2    b
1    c
4    d
dtype: object
>>> s.sort_index()
1    c
2    b
3    a
4    d
dtype: object
```

**例2**，按索引降序排序：

```py
>>> s.sort_index(ascending=False)
4    d
3    a
2    b
1    c
dtype: object
```

**例3**，原位排序：

```py
>>> s.sort_index(inplace=True)
>>> s
1    c
2    b
3    a
4    d
dtype: object
```

**例4**，NaN 默认放在最后，使用 `na_position` 设置 NaN 值位置：

```py
>>> s = pd.Series(['a', 'b', 'c', 'd'], index=[3, 2, 1, np.nan])
>>> s
3.0    a
2.0    b
1.0    c
NaN    d
dtype: object
>>> s.sort_index(na_position='first')
NaN    d
1.0    c
2.0    b
3.0    a
dtype: object
```

**例5**，`level` 用于指定索引排序优先级：

```py
>>> arrays = [np.array(['qux', 'qux', 'foo', 'foo',
                        'baz', 'baz', 'bar', 'bar']),
              np.array(['two', 'one', 'two', 'one',
                        'two', 'one', 'two', 'one'])]
>>> s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=arrays)
>>> s
qux  two    1
     one    2
foo  two    3
     one    4
baz  two    5
     one    6
bar  two    7
     one    8
dtype: int64
>>> s.sort_index() # 默认对所有 index 排序，从前到后依次排序
bar  one    8
     two    7
baz  one    6
     two    5
foo  one    4
     two    3
qux  one    2
     two    1
dtype: int64
>>> s.sort_index(level=1) # 依然对所有 index 排序，只是先排序 level=1
bar  one    8
baz  one    6
foo  one    4
qux  one    2
bar  two    7
baz  two    5
foo  two    3
qux  two    1
dtype: int64
```

**例6**，使用 `sort_remaining=False` 可以只对指定 index 排序，不再对余下 index 排序：

```py
>>> s.sort_index(level=1, sort_remaining=False)
qux  one    2
foo  one    4
baz  one    6
bar  one    8
qux  two    1
foo  two    3
baz  two    5
bar  two    7
dtype: int64
```

**例7**，对日期进行排序：

```py
>>> index = ['2020-01-25', '2020-01-18', '2020-01-22', '2020-01-21', '']
>>> values = ['b', 'c', 'd', 'a', 'e']
>>> s = pd.Series(values, index)
>>> s
2020-01-25    b
2020-01-18    c
2020-01-22    d
2020-01-21    a
              e
dtype: object
>>> s.index = pd.to_datetime(s.index)
>>> s
2020-01-25    b
2020-01-18    c
2020-01-22    d
2020-01-21    a
NaT           e
dtype: object
```

可以看到，缺失的日期用 `NaT` 类型，表示 not a time。

```py
>>> s.sort_index() # 日期排序，默认按照时间顺序排序
2020-01-18    c
2020-01-21    a
2020-01-22    d
2020-01-25    b
NaT           e
dtype: object
```


## label 对齐

在算术运算中，`Series` 会自动根据索引标签自动对齐：

```py
In [1]: obj3
Out[1]: 
Ohio      35000
Oregon    16000
Texas     71000
Utah       5000
dtype: int64

In [2]: obj4
Out[2]: 
California        NaN
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
dtype: float64

In [3]: obj3 + obj4
Out[3]: 
California         NaN
Ohio           70000.0
Oregon         32000.0
Texas         142000.0
Utah               NaN
dtype: float64
```

## 缺失值处理

### dropna

```py
Series.dropna(axis=0, inplace=False)
```

移除 NaN 值，返回一个新的 `Series`。

> 该方法仅针对值，不针对 index。

**例1**，移除 Series 的 NaN 值：

```py
>>> s = pd.Series([1., 2., np.nan])
>>> s
0    1.0
1    2.0
2    NaN
dtype: float64
>>> s.dropna()
0    1.0
1    2.0
dtype: float64
```

**例2**，`inplace` 设置为 True 表示原位操作，返回 `None`

```py
>>> s.dropna(inplace=True)
>>> s
0    1.0
1    2.0
dtype: float64
```

### isnull

```py
Series.isnull()
```

检测缺失值。返回一个和原 `Series` 等长的布尔类型 `Series`，如果原 `Series` 对应位置为缺失值，则为 `True`，否则为 `False`。缺失值包括 `None` 和 `numpy.NaN`。

例如：

```py
>>> ser = pd.Series([1, 2, np.NaN])
>>> ser
0    1.0
1    2.0
2    NaN
dtype: float64
>>> ser.isnull()
0    False
1    False
2     True
dtype: bool
```

也可以通过 pandas 的 `isnull` 和 `notnull` 函数判断是否为缺失值：

```py
In [1]: pd.isnull(obj4)
Out[1]: 
California     True
Ohio          False
Oregon        False
Texas         False
dtype: bool

In [2]: pd.notnull(obj4)
Out[2]:
California    False
Ohio           True
Oregon         True
Texas          True
dtype: bool
```

### fillna

```py
Series.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
```

使用指定方法替换 NA 值。

`method` 用于指定替换方法：

- 'backfill', 'bfill'，将下一个有效值向上传播；
- 'ffill', 'pad'，将上一个有效值向下传播；
- None，默认值

**例1**，用 0 替换 NA 值

```py
>>> df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5],
                   [np.nan, 3, np.nan, 4]],
                  columns=list("ABCD"))
>>> df
     A    B   C  D
0  NaN  2.0 NaN  0
1  3.0  4.0 NaN  1
2  NaN  NaN NaN  5
3  NaN  3.0 NaN  4
>>> df.fillna(0)
     A    B    C  D
0  0.0  2.0  0.0  0
1  3.0  4.0  0.0  1
2  0.0  0.0  0.0  5
3  0.0  3.0  0.0  4
```

## 数学运算

### add

```py
Series.add(other, level=None, fill_value=None, axis=0)[source]
```

逐元素相加，等价于 `series + other`。

- 这里 `other` 可以是 `Series` 或标量值；
- `fill_value`，当相加的两个 `Series` 其中一个对应位置缺失，用该值替换，如果两个都缺失，则以缺失处理；

例如：

```py
>>> a = pd.Series([1, 2, 3, np.nan], index=['a', 'b', 'c', 'd'])
>>> a
a    1.0
b    2.0
c    3.0
d    NaN
dtype: float64
>>> b = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
>>> b
a    1.0
b    NaN
d    1.0
e    NaN
dtype: float64
>>> a.add(b, fill_value=0)
a    2.0
b    2.0
c    3.0
d    1.0
e    NaN
dtype: float64
>>> a.add(b)
a    2.0
b    NaN
c    NaN
d    NaN
e    NaN
dtype: float64
```

该相加操作有两个需要注意的点：

- 索引对齐，在相加时，`index` 相同的值进行相加；
- 缺失值替换，如果相加的两个值只有一个缺失，用 `fill_value` 替换，上面替换值为 0；
- 如果没有设置 `fill_value`，则任意一个值缺失，返回 `NaN`。

如果 `other` 是标量值，则自动进行广播，逐元素相加：

```py
>>> a + 1
a    2.0
b    3.0
c    4.0
d    NaN
dtype: float64
```

### mul

```py
Series.mul(other, level=None, fill_value=None, axis=0)
```

乘法，等价于 `series * other`。

**例1**，和标量乘：

```py
>>> a = pd.Series([1, 2, 3, np.nan], index=['a', 'b', 'c', 'd'])
>>> a
a    1.0
b    2.0
c    3.0
d    NaN
dtype: float64
>>> a * 2 # 和标量乘
a    2.0
b    4.0
c    6.0
d    NaN
dtype: float64
```

**例2**，和另一个 series乘：

```py
>>> b = pd.Series([1, np.nan, 2, np.nan], index=['a', 'b', 'd', 'e'])
>>> b
a    1.0
b    NaN
d    2.0
e    NaN
dtype: float64
>>> a.mul(b)
a    1.0
b    NaN
c    NaN
d    NaN
e    NaN
dtype: float64
```

此时会先根据 index 对齐数据，NaN 值想成总是 NaN.

**例3**，填充缺失值：

`fill_value` 参数用于替换缺失值。

```py
>>> a.mul(b, fill_value=0)
a    1.0
b    0.0
c    0.0
d    0.0
e    NaN
dtype: float64
```

对 `index=e`，由于两者都缺失，返回相乘依然缺失。

### round

```py
Series.round(decimals=0, *args, **kwargs)
```

四舍五入到指定的小数点。

**例1**，默认保留整数：

`decimals`参数用于指定保留的小数点后位数，如果指定为负数，则表示小数点左侧位数。

```py
>>> s = pd.Series([0.1, 1.3, 2.7])
>>> s.round()
0    0.0
1    1.0
2    3.0
dtype: float64
```

## 统计计算

### between

```py
Series.between(left, right, inclusive='both')
```

返回 left <= series <= right 的 boolean Series。

`between` 函数一个布尔向量，如果值在 left 和 right 之间，对应位置为 True，否则为 False。NA 值作为 False 处理。

`left` 指定区间左侧，scalar 或 list-like。

`right` 指定区间右侧，scalar 或 lilst-like。

`inclusive` 是否包含边界：

- "both"，包含两侧边界，默认值；
- "neither"，不包含边界；
- "left"，只包含左侧边界；
- "right"，只包含右侧边界。

该函数等价于 `(left <= ser) & (ser <= right)`。

**例1**，默认包含边界：

```py
>>> s = pd.Series([2, 0, 4, 8, np.nan])
>>> s.between(1, 4)
0     True
1    False
2     True
3    False
4    False
dtype: bool
```

**例2**，设置 `inclusive="neither"` 不包含边界

```py
>>> s.between(1, 4, inclusive="neither")
0     True
1    False
2    False
3    False
4    False
dtype: bool
```

**例3**，`left` 和 `right` 可以是任意标量值，包括字符串

```py
>>> s = pd.Series(['Alice', 'Bob', 'Carol', 'Eve'])
>>> s.between('Anna', 'Daniel')
0    False
1     True
2     True
3    False
dtype: bool
```

### eq

```py
Series.eq(other, level=None, fill_value=None, axis=0)
```

等价于 `series == other` 操作，额外支持 `fill_value` 替换缺失值。例如：

```py
>>> a
a    1.0
b    2.0
c    3.0
d    NaN
dtype: float64
>>> b
a    1.0
b    NaN
d    1.0
e    NaN
dtype: float64
>>> a.eq(b, fill_value=0) # 缺失值用 0 代替
a     True
b    False
c    False
d    False
e    False
dtype: bool
>>> a.eq(b, fill_value=2) # 缺失值用 2 代替
a     True
b     True
c    False
d    False
e    False
dtype: bool
```

### ne

```py
Series.ne(other, level=None, fill_value=None, axis=0)
```

等价于 `series != other` 操作，额外支持 `fill_value` 替换缺失值。例如：

```py
>>> a
a    1.0
b    2.0
c    3.0
d    NaN
dtype: float64
>>> b
a    1.0
b    NaN
d    1.0
e    NaN
dtype: float64
>>> a.ne(b, fill_value=0)
a    False
b     True
c     True
d     True
e     True
dtype: bool
```

### cumsum

```py
Series.cumsum(axis=None, skipna=True, *args, **kwargs)
```

返回累计和，返回的 `Series` 和原 `Series` 等长。

### count

```py
Series.count(level=None)
```

返回 `Series` 中 non-NA/null 值的个数。例如：

```py
>>> numbers = pd.Series([1, 2, 3, np.nan, 4, 5])
>>> numbers
0    1.0
1    2.0
2    3.0
3    NaN
4    4.0
5    5.0
dtype: float64
>>> numbers.count()
5
```

### pct_change

```py
Series.pct_change(periods=1, fill_method='pad', limit=None, freq=None, **kwargs)
```

当前元素和前一个元素的变化百分比。

例如：

```py
>>> s = pd.Series([90, 91, 85])
>>> s
0    90
1    91
2    85
dtype: int64
>>> s.pct_change()
0         NaN
1    0.011111
2   -0.065934
dtype: float64
```

### unique

```py
Series.unique()
```

按照值出现的顺序返回 `Series` 中的非冗余值。返回值类型为 `ndarray` 或 `ExtensionArray`。如下类型返回 `ExtensionArray`：

- Categorical
- Period
- Datetime with Timezone
- Interval
- Sparse
- IntegerNA

例如：

```py
>>> pd.Series([2, 1, 3, 3], name='A').unique()
array([2, 1, 3], dtype=int64)
```

### nunique

```py
Series.nunique(dropna=True)
```

返回 `Series` 中的非冗余值。默认不包括 NA 值。例如：

```py
>>> import pandas as pd
>>> s = pd.Series([1, 3, 5, 7, 7])
>>> s.nunique()
4
```

### 非冗余值计数和区间计数

```py
Series.value_counts(self, normalize=False, sort=True, ascending=False, bins=None, dropna=True)
```

该方法用于非冗余值计数，返回包含各个值数目的 `Series`，`Series` 的inndex为非冗余值，而 values 为各个值出现的次数。

返回的对象按降序排列，所以返回 `Series` 的第一个元素是出现次数最多的。默认排除 NA 值。

**例1**，默认不包含 NaN 值：

```py
>>> index = pd.Index([3, 1, 2, 3, 4, np.nan])
>>> index.value_counts()
3.0    2
4.0    1
2.0    1
1.0    1
dtype: int64
>>> s.value_counts(dropna=False) # 不去除 NaN
3.0    2
1.0    1
2.0    1
4.0    1
NaN    1
dtype: int64
```

**例2**，将个数归一化为比例

若将 `normalize` 参数设置为 True，用数值总和归一化所有个数值：

```py
>>> s = pd.Series([3, 1, 2, 3, 4, np.nan])
>>> s.value_counts(normalize=True)
3.0    0.4
4.0    0.2
2.0    0.2
1.0    0.2
dtype: float64
```

**例3**，返回值的顺序

- `sort` 参数用于设置是否对返回 `Series` 排序，默认为 True；
- `ascending` 用于确定是升序还是降序，默认按降序排列。

**例4**，区间计数

参数 `bins` 可用于指定区间，从而进行区间计数：

```py
>>> buckets = [0, 200, 400, 600, 800, 1000, 1200, 1400]
>>> google.value_counts(bins = buckets)
(200.0, 400.0]      1568
(-0.001, 200.0]      595
(400.0, 600.0]       575
(1000.0, 1200.0]     406
(600.0, 800.0]       380
(800.0, 1000.0]      207
(1200.0, 1400.0]      93
Name: Close, dtype: int64
```

可以看到，在区间 (200.0, 400.0] 范围内的值最多。如果区间按照顺序显示，可以额外加一个索引排序，或者计数时禁用排序：

```py
>>> google.value_counts(bins = buckets, sort = False) # 和下面的效果一样
>>> google.value_counts(bins = buckets).sort_index()
(-0.001, 200.0]      595
(200.0, 400.0]      1568
(400.0, 600.0]       575
(600.0, 800.0]       380
(800.0, 1000.0]      207
(1000.0, 1200.0]     406
(1200.0, 1400.0]      93
Name: Close, dtype: int64
```

需要注意的是，第一个区间左侧取了 -0.001，而不是 0。`Series` 在进行区间计数时，左右两侧都可能扩展 .1%，由于左侧是开区间，(-0.001 就可以把 0 涵盖进去。

另外，`bins` 参数也可以直接使用整数，此时 pandas 会根据该数值计算 `bins` 个均匀分布的区间（由于边缘可能会扩展 .1%，所以边缘的 bin 大小可能不同）。例如：

```py
>>> s = pd.Series([3, 1, 2, 3, 4, np.nan])
>>> s.value_counts(bins=3)
(0.996, 2.0]    2
(2.0, 3.0]      2
(3.0, 4.0]      1
dtype: int64
```

### 获得最大的 n 个值

```py
Series.nlargest(n=5, keep='first')
```

以 `Series` 返回最大的 n 个元素，值降序排列。

**例1**，获得最大的 n 个值：

```py
>>> countries_population = {"Italy": 59000000, "France": 65000000,
                            "Malta": 434000, "Maldives": 434000,
                            "Brunei": 434000, "Iceland": 337000,
                            "Nauru": 11300, "Tuvalu": 11300,
                            "Anguilla": 11300, "Montserrat": 5200}
>>> s = pd.Series(countries_population)
>>> s
Italy         59000000
France        65000000
Malta           434000
Maldives        434000
Brunei          434000
Iceland         337000
Nauru            11300
Tuvalu           11300
Anguilla         11300
Montserrat        5200
dtype: int64
>>> s.nlargest()
France      65000000
Italy       59000000
Malta         434000
Maldives      434000
Brunei        434000
dtype: int64
```

**例2**，重复值处理

`keep` 参数用于处理重复值情况：

- 'first'，保留先出现的，默认
- 'last'，保留后出现的
- 'all'，保留所有重复值，此时保留的值可能大于 n

```py
>>> s.nlargest(3) # 最大的 3 个值，重复值取先出现的
France    65000000
Italy     59000000
Malta       434000
dtype: int64
>>> s.nlargest(3, keep='last') # 最大的 3 个值，重复值取后出现的
France    65000000
Italy     59000000
Brunei      434000
dtype: int64
>>> s.nlargest(3, keep='all') # 最大的 3 个值，重复值则全部保留
France      65000000
Italy       59000000
Malta         434000
Maldives      434000
Brunei        434000
dtype: int64
```

### 获得最小的 n 个值

```py
Series.nsmallest(n=5, keep='first')
```

使用方法和 `nlargest` 一样。

## 广播

广播功能在 numpy 中应用十分广泛，pandas 数据底层也采用了 numpy 的 `ndarray`，因此在执行数学运算时，也广泛支持广播操作。

## 原位操作

`Series` 的很多方法都有 `inplace` 参数，使用该参数不返回新的副本。不过在内置实现 pandas 依然创建了副本，如下两个操作：

```py
s.sort_values(inplace = True)
s = s.sort_values()
```

从技术上来说是等价的，所以我不怎么推荐使用 `inplace` 参数。

## 参考

- https://pandas.pydata.org/docs/reference/series.html
- Pandas in Action.Boris Paskhaver.MANNING.2021

pandas 特别详细，而且大部分方法的文档都有实例，感觉看文档就够了。

### map

根据输入映射 `Series` 值。

### Series.equals

```r
Series.equals(other)
```

测试两个对象是否包含相同的元素。

- 对比两个 `Series` 或 `DataFrames` 是否具有相同的 shape 和元素。
- 相同位置的 `NaN` 认为相等。
- column 标题不需要是相同类型，但是相同 column 的元素值必须为相同 dtype。

```py
df = pd.DataFrame({1: [10], 2: [20]})
df_equal = pd.DataFrame({1: [10], 2: [20]})
assert df.equals(df_equal)

different_col_type = pd.DataFrame({1.0: [10], 2.0: [20]})
assert df.equals(different_col_type)

different_data_type = pd.DataFrame({1: [10.0], 2: [20.0]})
assert not df.equals(different_data_type)
```
