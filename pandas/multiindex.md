# MultiIndex

- [MultiIndex](#multiindex)
  - [分层索引](#分层索引)
  - [创建 MultiIndex 对象](#创建-multiindex-对象)
    - [from_tuples](#from_tuples)
    - [from_product](#from_product)
    - [from_frame](#from_frame)
    - [from_arrays](#from_arrays)
    - [传递 index 参数](#传递-index-参数)
    - [names 参数](#names-参数)
  - [选择](#选择)
    - [index 查询](#index-查询)
  - [参考](#参考)

2021-10-22, 12:38
@author Jiawei Mao
***

## 分层索引

分层/多层索引方便复杂数据的分析和操作，特别是高维数据。从本质上讲，分层索引技术使得低维数据结构如 `Series` (1d) 和 `DataFrame` (2d) 可以存储和处理任意维度的数据。

## 创建 MultiIndex 对象

相对标准 `Index` 对象，`MultiIndex` 分层存储 axis labels。可以将 `MultiIndex` 看作 tuple 数组，每个 tuple 为 unique。

```py
class pandas.MultiIndex(levels=None, codes=None, sortorder=None, names=None, dtype=None, copy=False, name=None, verify_integrity=True)
```

可以使用多种对象创建 `MultiIndex`：

- 数组列表（`MultiIndex.from_arrays()`）
- tuple 数组（`MultiIndex.from_tuples()`）
- 交叉的可迭代对象（`MultiIndex.from_product()`）
- DataFrame （`MultiIndex.from_frame()`）

### from_tuples

```py
classmethod MultiIndex.from_tuples(tuples, sortorder=None, names=None)
```

将 tuple 列表转换为 `MultiIndex`。

`names` 用于指定各个 level 的名称。

**例1**，使用 tuple 列表创建 MultiIndex

```py
>>> tuples = [(1, 'red'), (1, 'blue'),
          (2, 'red'), (2, 'blue')]
>>> pd.MultiIndex.from_tuples(tuples, names=('number', 'color'))
MultiIndex([(1,  'red'),
            (1, 'blue'),
            (2,  'red'),
            (2, 'blue')],
           names=['number', 'color'])
```

### from_product

```py
classmethod MultiIndex.from_product(iterables, sortorder=None, names=NoDefault.no_default)
```

使用多个 `iterable` 对象的的组合生成 MultiIndex.

`names` 用于指定 MultiIndex 不同 level 的名称。

**例1**，使用两个 iterables 的所有组合生成 MultiIndex：

```py
>>> numbers = [0, 1, 2]
>>> colors = ['green', 'purple']
>>> pd.MultiIndex.from_product([numbers, colors],
                           names=['number', 'color'])
MultiIndex([(0,  'green'),
            (0, 'purple'),
            (1,  'green'),
            (1, 'purple'),
            (2,  'green'),
            (2, 'purple')],
           names=['number', 'color'])
```

`MultiIndex.from_frame()` 从 `DataFrame` 创建 `MultiIndex`，这是 `MultiIndex.to_frame` 的互补方法。

### from_frame

```py
classmethod MultiIndex.from_frame(df, sortorder=None, names=None)
```

使用 `DataFrame` 创建 `MultiIndex`。和 `MultiIndex.to_frame` 方法互补。

`names` 用于指定不同 level 的名称，默认使用 `DataFrame` 的 column 名称。

**例1**，使用 `DataFrame` 创建 `MultiIndex`

```py
>>> df = pd.DataFrame([['HI', 'Temp'], ['HI', 'Precip'],
                   ['NJ', 'Temp'], ['NJ', 'Precip']],
                  columns=['a', 'b'])
>>> df
    a       b
0  HI    Temp
1  HI  Precip
2  NJ    Temp
3  NJ  Precip
>>> pd.MultiIndex.from_frame(df)
MultiIndex([('HI',   'Temp'),
            ('HI', 'Precip'),
            ('NJ',   'Temp'),
            ('NJ', 'Precip')],
           names=['a', 'b'])
```

**例2**，显式指定 leveel 名称

```py
>>> pd.MultiIndex.from_frame(df, names=['state', 'observation'])
MultiIndex([('HI',   'Temp'),
            ('HI', 'Precip'),
            ('NJ',   'Temp'),
            ('NJ', 'Precip')],
           names=['state', 'observation'])
```

### from_arrays

```py
classmethod MultiIndex.from_arrays(arrays, sortorder=None, names=NoDefault.no_default)
```

将数组转换为 `MultiIndex`。

例如：

```py
>>> arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
>>> pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))
MultiIndex([(1,  'red'),
            (1, 'blue'),
            (2,  'red'),
            (2, 'blue')],
           names=['number', 'color'])
```

### 传递 index 参数

在创建 `Series` 或 `DataFrame` 时，如果传入的 `index` 索引是多维的，内部会自动转换为 `MultiIndex` 类型。

**例1**，创建带 `MultiIndex` 的 `Series`

```py
>>> arrays = [
    np.array(["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"]),
    np.array(["one", "two", "one", "two", "one", "two", "one", "two"]),
]
>>> s = pd.Series(np.random.randn(8), index=arrays)
>>> s
bar  one    0.456034
     two    0.580636
baz  one   -0.797437
     two   -1.450854
foo  one    0.272339
     two    1.037776
qux  one    1.106939
     two    0.119283
dtype: float64
```

**例2**，创建带 `MultiIndex` 的 `DataFrame`

```py
>>> arrays = [
    np.array(["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"]),
    np.array(["one", "two", "one", "two", "one", "two", "one", "two"]),
]
>>> df = pd.DataFrame(np.random.randn(8, 4), index=arrays)
>>> df
                0         1         2         3
bar one -0.510182 -1.079527 -0.394485 -1.081719
    two  0.242275 -0.510917  1.778759  0.011121
baz one  0.093268 -0.270851  2.559709  1.104044
    two  0.978914  1.105512 -0.224353  0.756967
foo one -0.824231 -0.304421 -0.956938  0.583522
    two  1.120575  0.967208  0.338452 -0.401019
qux one  0.116859 -0.486545 -0.797360 -0.531531
    two -0.252874 -0.412538 -0.940929 -0.277799
```

### names 参数

所有的 `MultiIndex` 构造方法都支持 `names` 参数，用于指定不同 level 的名称。如果没有指定 `names`，默认为 `None`。

## 选择

### index 查询

```py
MultiIndex.get_level_values(level)
```

返回指定 level 的标签值。

**例1**，根据 level 位置查询 index 值

```py
>>> mi = pd.MultiIndex.from_arrays((list('abbc'), list('deff')))
>>> mi.names = ['level_1', 'level_2']
>>> mi
MultiIndex([('a', 'd'),
            ('b', 'e'),
            ('b', 'f'),
            ('c', 'f')],
           names=['level_1', 'level_2'])
>>> mi.get_level_values(0) # 获得 level 0 的 index
Index(['a', 'b', 'b', 'c'], dtype='object', name='level_1')
```

**例2**，根据 level 名称查询 index

```py
>>> mi.get_level_values("level_2")
Index(['d', 'e', 'f', 'f'], dtype='object', name='level_2')
```

## 参考

- https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html
- https://pandas.pydata.org/docs/reference/indexing.html
