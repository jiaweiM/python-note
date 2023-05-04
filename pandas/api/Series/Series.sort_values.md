2023-05-04
****

## 方法签名

```python
Series.sort_values(*, 
				   axis=0,
				   ascending=True,
				   inplace=False,
				   kind='quicksort', 
				   na_position='last',
				   ignore_index=False,
				   key=None)
```

按值排序。

**参数：**

- **axis**：{0 or 'index'}

未使用。与 `DataFrame` 兼容所需参数。

- **ascending**：bool or list of bools, default `True`

True 表示升序排序，否则降序。

- **inplace**：bool, default False

True 表示原位排序。

- **kind**：{'quicksort', 'mergesort', 'heapsort', 'stable'}, default 'quicksort'

选择排序算法类型。更多信息可参考 [numpy.sort()](https://numpy.org/doc/stable/reference/generated/numpy.sort.html) 。唯有 'mergesort' 和 'stable' 是稳定算法。

- **na_position**：{'first' or 'last'}, default 'last'

'first' 表示将 NaN 值放在开头，'last' 表示将 NaN 值放在末尾。

- **ignore_index**：bool, default False

如果 `True`，则结果的 axis 被标记为 0, 1, …, n - 1。

- **key**：callable, optional

如果不是 `None`，则在排序之前对 series 值应用 `key` 函数。这与内置的 sorted() 函数的 `key` 参数类似，只是这个 `key` 函数需要是向量化的。其输入为 `Series`，返回相同 shape 的 array-like。

**返回：**

- Series 或 None

按值排序后的 `Series`，如果 `inplace=True` 返回 `None`。

## 示例

```python
>>> s = pd.Series([np.nan, 1, 3, 10, 5])
>>> s
0     NaN
1     1.0
2     3.0
3     10.0
4     5.0
dtype: float64
```

- 升序排序（默认）

```python
>>> s.sort_values(ascending=True)
1     1.0
2     3.0
4     5.0
3    10.0
0     NaN
dtype: float64
```

- 降序排序

```python
>>> s.sort_values(ascending=False)
3    10.0
4     5.0
2     3.0
1     1.0
0     NaN
dtype: float64
```

- NA 优先

```python
>>> s.sort_values(na_position='first')
0     NaN
1     1.0
2     3.0
4     5.0
3    10.0
dtype: float64
```

- 字符串排序

```python
>>> s = pd.Series(['z', 'b', 'd', 'a', 'c'])
>>> s
0    z
1    b
2    d
3    a
4    c
dtype: object
```

```python
>>> s.sort_values()
3    a
1    b
4    c
2    d
0    z
dtype: object
```

- key 函数

```python
>>> s = pd.Series(['a', 'B', 'c', 'D', 'e'])
>>> s.sort_values()
1    B
3    D
0    a
2    c
4    e
dtype: object
>>> s.sort_values(key=lambda x: x.str.lower())
0    a
1    B
2    c
3    D
4    e
dtype: object
```

- NumPy ufuncs 也能作为 key 函数

```python
>>> s = pd.Series([-4, -2, 0, 2, 4])
>>> s.sort_values(key=np.sin)
1   -2
4    4
2    0
0   -4
3    2
dtype: int64
```

- 使用更复杂的 key 函数

```python
>>> s.sort_values(key=lambda x: (np.tan(x.cumsum())))
0   -4
3    2
4    4
1   -2
2    0
dtype: int64
```

## 参考

- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sort_values.html