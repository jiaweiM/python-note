# 排序、检索和计数

- [排序、检索和计数](#排序检索和计数)
  - [排序](#排序)
  - [检索](#检索)
    - [argmax](#argmax)
  - [参考](#参考)

2021-06-23, 12:35
***

## 排序

## 检索

|方法|说明|
|---|---|
|`argmax(a[, axis, out])`|返回沿 `axis` 最大值的索引|
|`nanargmax(a[, axis])`|同上，忽略 NaN|
|`argmin(a[, axis, out])`|返回沿 `axis` 最小值的索引|
|`nanargmin(a[, axis])`|同上，忽略 NaN|
|`argwhere(a)`|返回所有非零元素的索引，按照元素分类|
|`nonzero(a)`|返回非零元素索引|
|`flatnonzero(a)`|返回 flatten 版本 `a` 中非零元素的索引|
|`where(condition, [x, y])`|根据 `condition` 选择从 x 或 y 选择的元素|
|`searchsorted(a, v[, side, sorter])`|查找排序状态下元素插入的位置|
|`extract(condition, arr)`|返回数组中满足条件的所有元素|

### argmax

```py
numpy.argmax(a, axis=None, out=None)
```

返回沿 `axis` 最大值的索引。

|参数|类型|说明|
|---|---|---|
|a|array_like|输入数组|
|axis|int, *optional*|默认返回 flatten 数组中的数组，否则按照 `axis` 指定的轴，返回每个维度的最大值|
|out|array, *optional*|结果存储数组，shape 和 dtype 需要满足要求|

返回 `index_array`，即 ndarray of ints。

如果最大值出现多次，返回第一次出现的位置。例如：

```py
>>> import numpy as np
>>> a = np.arange(6).reshape(2, 3) + 10
>>> a
array([[10, 11, 12],
       [13, 14, 15]])
>>> np.argmax(a) # 默认返回 flatten 数组形式中的索引
5
>>> np.argmax(a, axis=0) # axis=0 这一维所有最大值索引
array([1, 1, 1], dtype=int64) # 均为 1，即都是第二行的值
>>> np.argmax(a, axis=1) # axis=1 这一维所有最大值索引
array([2, 2], dtype=int64) # 均为 2，即都是第二列的值
```

- 获取最大值的 tuple 索引

```py
>>> ind = np.unravel_index(np.argmax(a, axis=None), a.shape) # 将 flatten 索引转换为 tuple 索引
>>> ind # 第 1 行第二列
(1, 2)
>>> a[ind]
15
```

```py
>>> x = np.array([[4, 2, 3], [1, 0, 3]])
>>> index_array = np.argmax(x, axis=-1)
>>> # 等价于 np.max(x, axis=-1, keepdims=True)
>>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1)
array([[4],
       [3]])
```




## 参考

- https://numpy.org/doc/stable/reference/routines.sort.html
