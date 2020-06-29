# Index object

- [Index object](#index-object)
  - [简介](#简介)
  - [设置 metadata](#设置-metadata)
  - [集合操作](#集合操作)
  - [缺失值](#缺失值)

2020-06-08, 16:10
*** *

## 简介

pandas `Index` 及其子类可以看做实现了 *ordered multiset* 的集合，允许重复值。但它并不是真的集合，将 `Index` 转换为 `set` 会抛出错误。

`Index` 提供了查找、数据对齐和重建索引的功能。

创建 `Index` 的最简单方式是将 `list` 或其它序列传递给 `Index` 构造函数：

```py
index = pd.Index(['e', 'd', 'a', 'b'])
assert type(index) == pd.Index
assert index.dtype == object
assert 'd' in index
```

还可以给该索引一个名称 `name`:

```py
index = pd.Index(['e', 'd', 'a', 'b'], name='something')
assert index.name == 'something'
```

如果设置了名称，在输出时会显示：

```py
>>> index = pd.Index(list(range(5)), name='rows')

>>> columns = pd.Index(['A', 'B', 'C'], name='cols')

>>> df = pd.DataFrame(np.random.randn(5, 3), index=index, columns=columns)
>>> df
cols         A         B         C
rows
0     1.295989  0.185778  0.436259
1     0.678101  0.311369 -0.528378
2    -0.674808 -1.103529 -0.656157
3     1.889957  2.076651 -1.102192
4    -1.211795 -0.791746  0.634724

>>> df['A']
rows
0    1.295989
1    0.678101
2   -0.674808
3    1.889957
4   -1.211795
Name: A, dtype: float64
```

可以看到，`columns` 和 `index` 都是 `Index` 对象，对表格的行和列分别进行索引。

## 设置 metadata

Indexes 是 immutable的，但是其 metadata 可以修改，如 `name`（`MultiIndex` 的 `levels` 和 `codes`）。

可以使用 `rename`, `set_names`, `set_levels` 和 `set_codes` 方法设置这些属性。默认返回copy，设置 `inplace=True` 则原位修改。

```py
ind = pd.Index([1, 2, 3])
ind2 = ind.rename("apple")
assert ind2.name == 'apple'

ind.set_names(['apple'], inplace=True)
assert ind.name == 'apple'

ind.name = 'bob'
assert ind.name == 'bob'
```

`set_names`, `set_levels` 和 `set_codes` 均有一个可选的 `level` 参数。

```py
>>> index = pd.MultiIndex.from_product([range(3), ['one', 'two']], names=['first', 'second'])
>>> index
MultiIndex([(0, 'one'),
            (0, 'two'),
            (1, 'one'),
            (1, 'two'),
            (2, 'one'),
            (2, 'two')],
           names=['first', 'second'])
>>> index.levels[1]
Index(['one', 'two'], dtype='object', name='second')
>>> index.set_levels(["a", "b"], level=1)
MultiIndex([(0, 'a'),
            (0, 'b'),
            (1, 'a'),
            (1, 'b'),
            (2, 'a'),
            (2, 'b')],
           names=['first', 'second'])
```

## 集合操作

两个主要集合操作：并集（`union (|)`）和交集（`intersection (&)`）。可以直接通过实例方法调用，也可以使用重载运算符。

差集使用 `.difference()` 方法。

例如：

```py
>>> a = pd.Index(['c', 'b', 'a'])
>>> b = pd.Index(['c', 'e', 'd'])
>>> a | b
Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

>>> a & b
Index(['c'], dtype='object')

>>> a.difference(b)
Index(['a', 'b'], dtype='object')
```

还有对称差集 `symmetric_difference (^)`，返回两者并集和交集的差集，即出现在 `idx1` 和 `idx2` 中，但是不出现在交集中的元素。等价于 `idx1.difference(idx2).union(idx2.difference(idx1))`。

```py
>>> idx1 = pd.Index([1, 2, 3, 4])
>>> idx2 = pd.Index([2, 3, 4, 5])

>>> idx1.symmetric_difference(idx2)
Int64Index([1, 5], dtype='int64')

>>> idx1 ^ idx2
Int64Index([1, 5], dtype='int64')
```

> 集合操作得到的索引升序排列。

当对不同 `dtype` 的 indexes 执行 `Index.union()` 操作，索引必须转换为共同的 `dtype`。大多时候为 `object`，`integer` 和 `float` 数据例外，此时 integer 值转换为 float 值：

```py
>>> idx1 = pd.Index([0, 1, 2])
>>> idx2 = pd.Index([0.5, 1.5])

>>> idx1 | idx2
Float64Index([0.0, 0.5, 1.0, 1.5, 2.0], dtype='float64')
```

## 缺失值

> 虽然 `Index` 可以包含缺失值（`NaN`），但是应该避免，以免出现不可预期的结果。

`Index.fillna` 以指定的标量值填充缺失值。

```py
>>> idx1 = pd.Index([1, np.nan, 3, 4])
>>> idx1
Float64Index([1.0, nan, 3.0, 4.0], dtype='float64')

>>> idx1.fillna(2)
Float64Index([1.0, 2.0, 3.0, 4.0], dtype='float64')

>>> idx2 = pd.DatetimeIndex([pd.Timestamp('2011-01-01'),
   .....:                          pd.NaT,
   .....:                          pd.Timestamp('2011-01-03')])
>>> idx2
DatetimeIndex(['2011-01-01', 'NaT', '2011-01-03'], dtype='datetime64[ns]', freq=None)

>>> idx2.fillna(pd.Timestamp('2011-01-02'))
DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03'], dtype='datetime64[ns]', freq=None)
```
