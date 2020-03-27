# MultiIndex / advanced indexing

- [MultiIndex / advanced indexing](#multiindex--advanced-indexing)
  - [分层索引（MultiIndex）](#%e5%88%86%e5%b1%82%e7%b4%a2%e5%bc%95multiindex)
    - [创建 MultiIndex 对象](#%e5%88%9b%e5%bb%ba-multiindex-%e5%af%b9%e8%b1%a1)

***

## 分层索引（MultiIndex）

分层/多层索引方便复杂数据的分析和操作，特别是高维数据。从本质上讲，分层索引技术可以用低维数据结构如 `Series` (1d) 和 `DataFrame` (2d) 存储和处理任意维度的数据。

下面将展示“分层”索引的含义，以及如何和 pandas 的索引功能集成。

### 创建 MultiIndex 对象

相对标准 `Index` 对象，`MultiIndex` 分层存储 axis labels。可以将 `MultiIndex` 看作 tuple 数组，每个 tuple 为 unique。

可以使用多种对象创建 `MultiIndex`：

- 数组列表（`MultiIndex.from_arrays()`）
- tuple 数组（`MultiIndex.from_tuples()`）
- 交叉的可迭代对象（`MultiIndex.from_product()`）
- DataFrame （`MultiIndex.from_frame()`）

当将 tuples 列表传递给 `Index` 构造函数，会返回 `MultiIndex`。下面演示创建 MultiIndex 的各种方法：

```py
In [1]: arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
   ...:           ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
   ...:

In [2]: tuples = list(zip(*arrays))

In [3]: tuples
Out[3]:
[('bar', 'one'),
 ('bar', 'two'),
 ('baz', 'one'),
 ('baz', 'two'),
 ('foo', 'one'),
 ('foo', 'two'),
 ('qux', 'one'),
 ('qux', 'two')]

In [4]: index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

In [5]: index
Out[5]:
MultiIndex([('bar', 'one'),
            ('bar', 'two'),
            ('baz', 'one'),
            ('baz', 'two'),
            ('foo', 'one'),
            ('foo', 'two'),
            ('qux', 'one'),
            ('qux', 'two')],
           names=['first', 'second'])

In [6]: s = pd.Series(np.random.randn(8), index=index)

In [7]: s
Out[7]:
first  second
bar    one       0.469112
       two      -0.282863
baz    one      -1.509059
       two      -1.135632
foo    one       1.212112
       two      -0.173215
qux    one       0.119209
       two      -1.044236
dtype: float64
```

如果你希望获得两个 iterables 的所有组合，可以使用 `MultiIndex.from_product()` 方法：

```py
In [8]: iterables = [['bar', 'baz', 'foo', 'qux'], ['one', 'two']]

In [9]: pd.MultiIndex.from_product(iterables, names=['first', 'second'])
Out[9]:
MultiIndex([('bar', 'one'),
            ('bar', 'two'),
            ('baz', 'one'),
            ('baz', 'two'),
            ('foo', 'one'),
            ('foo', 'two'),
            ('qux', 'one'),
            ('qux', 'two')],
           names=['first', 'second'])
```

`MultiIndex.from_frame()` 从 `DataFrame` 创建 `MultiIndex`，这是 `MultiIndex.to_frame` 的互补方法。

```

```