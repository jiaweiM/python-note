2023-05-04
****

## 方法签名

```python
Series.sort_index(*,
				axis=0, 
				level=None, 				  
				ascending=True, 
				inplace=False,
				kind='quicksort',
				na_position='last',
				sort_remaining=True,
				ignore_index=False,
				key=None)
```

对 `Series` 按 index label 排序。

如果 `inplace` 为 `False`，则返回按 label 排序的新 `Series`，否则更新原 `Series`，返回 `None`。

**参数：**

- **axis**：{0 or 'index'}

未使用。与 `DataFrame` 兼容所需参数。

- **level**：`int`, optional

如果不是 None，则对指定 index level 的值进行排序。

- **ascending**：`bool` or list-like of bools, default `True`

升序或降序排序。当 index 为 `MultiIndex` 时，可以单独控制每个 level 的排序方向。

- **inplace**：`bool`, default `False`

`True` 表示原地排序。

- **kind**：{'quicksort', 'mergesort', 'heapsort', 'stable'}, default 'quicksort'

选择排序算法类型。更多信息可参考 [numpy.sort()](https://numpy.org/doc/stable/reference/generated/numpy.sort.html) 。唯有 'mergesort' 和 'stable' 是稳定算法。对 `DataFrame`，此选项只对单个 column 或 label 时使用。

- **na_position**：{'first', 'last'}, default 'last'

'first' 表示将 NaN 值放在开头，'last' 表示将 NaN 值放在末尾。没有为 MultiIndex 实现。

- **sort_remaining**：`bool`, default `True`

如果 True 且按 level 和 index 排序是多层的，则在按指定 level 排序后，对余下 level 也按顺序排序。

- **ignore_index**：bool, default False

如果 `True`，则结果的 axis 被标记为 0, 1, …, n - 1。

- **key**：callable, optional

如果不是 `None`，则在排序之前对索引值应用 `key` 函数。这与内置的 sorted() 函数的 key 参数类似，只是这个 `key` 函数需要是向量化的。其输入为 `Index`，返回相同 shape 的 `Index`。

**返回：**

- Series 或 None

按标签排序后的 `Series`，如果 `inplace=True`，则返回 `None`。

## 示例

- 默认排序
```python
>>> s = pd.Series(['a', 'b', 'c', 'd'], index=[3, 2, 1, 4])
>>> s.sort_index()
1    c
2    b
3    a
4    d
dtype: object
```

- 降序排序

```python
>>> s.sort_index(ascending=False)
4    d
3    a
2    b
1    c
dtype: object
```

- NaN 值默认在末尾，使用 `na_position` 调整

```python
>>> s = pd.Series(['a', 'b', 'c', 'd'], index=[3, 2, 1, np.nan])
>>> s.sort_index(na_position='first')
NaN     d
 1.0    c
 2.0    b
 3.0    a
dtype: object
```

- 指定 index level

```python
>>> arrays = [np.array(['qux', 'qux', 'foo', 'foo',
...                     'baz', 'baz', 'bar', 'bar']),
...           np.array(['two', 'one', 'two', 'one',
...                     'two', 'one', 'two', 'one'])]
>>> s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=arrays)
>>> s.sort_index(level=1)
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

- 不对余下 level 排序

```python
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

- 排序前应用 key 函数

```python
>>> s = pd.Series([1, 2, 3, 4], index=['A', 'b', 'C', 'd'])
>>> s.sort_index(key=lambda x : x.str.lower())
A    1
b    2
C    3
d    4
dtype: int64
```

## 参考

- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sort_index.html