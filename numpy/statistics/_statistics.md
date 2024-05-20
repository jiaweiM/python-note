# 统计

## 顺序统计量

| 方法                                                                                                                                                           | 功能                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| [`ptp`](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp "numpy.ptp")(a[, axis, out, keepdims])                                       | Range of values (maximum - minimum) along an axis.                                          |
| [percentile](percentile.md)(a, q[, axis, out, ...])                                                                                                          | 沿指定 axis 计算数据的第 q 个百分位数                                                       |
| [`nanpercentile`](https://numpy.org/doc/stable/reference/generated/numpy.nanpercentile.html#numpy.nanpercentile "numpy.nanpercentile")(a, q[, axis, out, ...]) | Compute the qth percentile of the data along the specified axis, while ignoring nan values. |
| [`quantile`](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#numpy.quantile "numpy.quantile")(a, q[, axis, out, overwrite_input, ...])    | Compute the q-th quantile of the data along the specified axis.                             |
| [`nanquantile`](https://numpy.org/doc/stable/reference/generated/numpy.nanquantile.html#numpy.nanquantile "numpy.nanquantile")(a, q[, axis, out, ...])         | Compute the qth quantile of the data along the specified axis, while ignoring nan values.   |


## 相关性

### numpy.corrcoef

```python
numpy.corrcoef(x, y=None, 
    rowvar=True, 
    bias=<no value>, 
    ddof=<no value>, 
    *, 
    dtype=None)
```

计算皮尔逊相关系数。皮尔逊相关系数是两个随机变量线性关系的度量。

## 参考

- https://numpy.org/doc/stable/reference/routines.statistics.html