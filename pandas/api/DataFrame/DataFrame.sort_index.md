2023-05-04
****

## 方法签名

```python
DataFrame.sort_index(*, 
					 axis=0, 
					 level=None, 
					 ascending=True, 
					 inplace=False,
					 kind='quicksort',
					 na_position='last',
					 sort_remaining=True, 
					 ignore_index=False, key=None)
```

沿指定 axis 对 DataFrame 按 label 排序。

如果 `inplace` 为 `False`，则返回按 label 排序的新 `DataFrame`，否则更新原 `DataFrame`，返回 `None`。

**参数：**

- **axis**：{0 or 'index', 1 or 'columns'}, default 0

排序 axis。0 表示 row，1表示 columns。

- **level**：`int` or level name or list of ints or list of level names

如果不是 None，则对指定 index level 的值进行排序。

- **ascending**：`bool` or list-like of bools, default `True`

升序或降序排序。当 index 为 `MultiIndex` 时，可以单独控制每个 level 的排序方向。

- **inplace**：`bool`, default `False`

`True` 表示原地排序。

- **kind**：{'quicksort', 'mergesort', 'heapsort', 'stable'}, default 'quicksort'

选择排序算法类型。更多信息可参考 [numpy.sort()](https://numpy.org/doc/stable/reference/generated/numpy.sort.html) 。唯有 'mergesort' 和 'stable' 是稳定算法。对 `DataFrame`，此选项只对单个 column 或 label 时应用。

- **na_position**：{'first', 'last'}, default 'last'

'first' 表示将 NaN 值放在开头，'last' 表示将 NaN 值放在末尾。没有为 MultiIndex 实现。

- **sort_remaining**：`bool`, default `True`

如果 `True` 且按 level 和 index 排序是多层的，则在按指定 level 排序后，对余下 level 也按顺序排序。

- **ignore_index**：bool, default False

如果 `True`，则结果的 axis 被标记为 0, 1, …, n - 1。

- **key**：callable, optional

如果不是 `None`，则在排序之前对索引值应用 `key` 函数。这与内置的 sorted() 函数的 key 参数类似，只是这个 `key` 函数需要是向量化的。其输入为 `Index`，返回相同 shape 的 `Index`。

**返回：**

- DataFrame 或 None

按标签排序后的 `DataFrame`，如果 `inplace=True`，则返回 `None`。

## 示例

- 默认排序

```python
>>> df = pd.DataFrame([1, 2, 3, 4, 5], index=[100, 29, 234, 1, 150],
...                   columns=['A'])
>>> df.sort_index()
     A
1    4
29   2
100  1
150  5
234  3
```

- 降序排序

```python
>>> df.sort_index(ascending=False)
     A
234  3
150  5
100  1
29   2
1    4
```

- 排序前应用 key 函数

对 MultiIndex，将分别应用于每个 level。

```python
>>> df = pd.DataFrame({"a": [1, 2, 3, 4]}, index=['A', 'b', 'C', 'd'])
>>> df.sort_index(key=lambda x: x.str.lower())
   a
A  1
b  2
C  3
d  4
```

## 参考

- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_index.html