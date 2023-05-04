2023-05-04
****

## 方法签名

```python
DataFrame.sort_values(by, 
					  *,
					  axis=0,
					  ascending=True,
					  inplace=False,
					  kind='quicksort',
					  na_position='last',
					  ignore_index=False,
					  key=None)
```

沿指定 axis 按值排序。

**参数：**

- **by**：str or list of str

要排序的 name 或 name list：

- 如果 `axis` 是 0 或 'index'，则 `by` 包含 index levels and/or column labels
- 如果 `axis` 是 1 或 'columns'，则 `by` 包含 column levels and/or index labels.

- **axis**：{{0 or 'index', 1 or 'columns'}, default 0

待排序 axis。

- **ascending**：bool or list of bools, default `True`

True 表示升序排序，否则降序。对多轴排序，需要指定 `list` of `bool`，且长度与 `by` 相同。

- **inplace**：bool, default False

True 表示原位排序。

- **kind**：{'quicksort', 'mergesort', 'heapsort', 'stable'}, default 'quicksort'

选择排序算法类型。更多信息可参考 [numpy.sort()](https://numpy.org/doc/stable/reference/generated/numpy.sort.html) 。唯有 'mergesort' 和 'stable' 是稳定算法。对 DataFrame，该选项仅在对单个 column 或 label 排序时应用。

- **na_position**：{'first' or 'last'}, default 'last'

'first' 表示将 NaN 值放在开头，'last' 表示将 NaN 值放在末尾。

- **ignore_index**：bool, default False

如果 `True`，则结果的 axis 被标记为 0, 1, …, n - 1。

- **key**：callable, optional

如果不是 `None`，则在排序之前对 series 值应用 `key` 函数。这与内置的 sorted() 函数的 `key` 参数类似，只是这个 `key` 函数需要是向量化的。其输入为 `Series`，返回相同 shape 的 Series。它将单独应用于 `by` 的每一列。

**返回：**

- DataFrame 或 None

按值排序后的 `DataFrame`，如果 `inplace=True` 返回 `None`。

## 示例

```python
>>> df = pd.DataFrame({
...     'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
...     'col2': [2, 1, 9, 8, 7, 4],
...     'col3': [0, 1, 9, 4, 2, 3],
...     'col4': ['a', 'B', 'c', 'D', 'e', 'F']
... })
>>> df
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
```

- 按 col1 排序

```python
>>> df.sort_values(by=['col1'])
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D
```

- 多列排序

```python
>>> df.sort_values(by=['col1', 'col2'])
  col1  col2  col3 col4
1    A     1     1    B
0    A     2     0    a
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D
```

- 降序

```python
>>> df.sort_values(by='col1', ascending=False)
  col1  col2  col3 col4
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B
3  NaN     8     4    D
```

- NA 优先

```python
>>> df.sort_values(by='col1', ascending=False, na_position='first')
  col1  col2  col3 col4
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B
```

- key 函数

```python
>>> df.sort_values(by='col4', key=lambda col: col.str.lower())
   col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
```

- 使用 `key` 参数自然排序，使用 natsort <https://github.com/SethMMorton/natsort> 包

```python
>>> df = pd.DataFrame({
...    "time": ['0hr', '128hr', '72hr', '48hr', '96hr'],
...    "value": [10, 20, 30, 40, 50]
... })
>>> df
    time  value
0    0hr     10
1  128hr     20
2   72hr     30
3   48hr     40
4   96hr     50
>>> from natsort import index_natsorted
>>> df.sort_values(
...     by="time",
...     key=lambda x: np.argsort(index_natsorted(df["time"]))
... )
    time  value
0    0hr     10
3   48hr     40
2   72hr     30
4   96hr     50
1  128hr     20
```

## 参考

- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sort_values.html