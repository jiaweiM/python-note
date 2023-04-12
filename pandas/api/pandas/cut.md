# pandas.cut

## 简介

```python
pandas.cut(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True)
```

将数值划分为离散区间。

`cut` 用来将数值分隔和排序到 bin 中。常用来将连续变量转换为分类变量。例如，`cut` 可以将年龄转换为年龄范围。

**参数：**

- **retbins**: bool, default False

是否返回 bins。当 bins 以标量提供时很有用。

**示例：**

- 划分为三个等长 bins

```python
>>> pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3)
... 
[(0.994, 3.0], (5.0, 7.0], (3.0, 5.0], (3.0, 5.0], (5.0, 7.0], ...
Categories (3, interval[float64, right]): [(0.994, 3.0] < (3.0, 5.0] ...
```

```python
>>> pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3, retbins=True)
... 
([(0.994, 3.0], (5.0, 7.0], (3.0, 5.0], (3.0, 5.0], (5.0, 7.0], ...
Categories (3, interval[float64, right]): [(0.994, 3.0] < (3.0, 5.0] ...
array([0.994, 3.   , 5.   , 7.   ]))
```

## 参考

- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html