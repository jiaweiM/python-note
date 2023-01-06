# 输入和输出

## Text files

### numpy.ndarray.tolist

```python
ndarray.tolist()
```

将数组数据的副本以 Python list 类型返回。数据通过 `item` 函数转换为最接近的兼容的 Python 类型。

当 `a.ndim` 为 0，直接返回一个 Python 标量。

例如：

- 对 1D 数组，`a.tolist()` 与 `list(a)` 几乎一样，只是 `tolist` 会将 numpy 标量转换为 Python 标量

```python
>>> import numpy as np
>>> a = np.uint32([1, 2])
>>> a_list = list(a)
>>> a_list
[1, 2]
>>> type(a_list[0])
<class 'numpy.uint32'>
>>> a_tolist = a.tolist()
>>> a_tolist
[1, 2]
>>> type(a_tolist[0])
<class 'int'>
```

- 对 2D 数组，递归应用 `tolist`

```python
>>> a = np.array([[1, 2], [3, 4]])
>>> list(a)
[array([1, 2]), array([3, 4])]
>>> a.tolist()
[[1, 2], [3, 4]]
```

- 递归的最基础情况是 0D 数组

```python
>>> a = np.array(1)
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list(a)
TypeError: iteration over a 0-d array
>>> a.tolist()
1
```

## 参考

- https://numpy.org/doc/stable/reference/routines.io.html
