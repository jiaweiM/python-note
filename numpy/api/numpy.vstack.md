# numpy.vstack

```python
numpy.vstack(tup)
```

按顺序（行方向）堆叠数组。

这个函数对三维以下的数组比较有用。例如，包含宽度（第一维）、高度（第二维）和像素通道（第三维）的图像数据。函数 `concatenate`, `stack` 和 `block` 提供了更通用的堆叠和串联操作。

## 参数

- `tuple`

数组序列。

这些数组除了第一个轴，其它轴的 shape 要一样。对一维数组，则必须长度相同。

## 实例

- 堆叠两个 1D 数组

```python
>>> a = np.array([1, 2, 3])
>>> b = np.array([4, 5, 6])
>>> np.vstack((a,b))
array([[1, 2, 3],
       [4, 5, 6]])
```

- 堆叠两个 2D 数组

```python
>>> a = np.array([[1], [2], [3]])
>>> b = np.array([[4], [5], [6]])
>>> np.vstack((a,b))
array([[1],
       [2],
       [3],
       [4],
       [5],
       [6]])
```

`a` 和 `b` 是两个 shape 为 (3, 1)的 2D 数组，第一个轴堆叠起来，变为 (6, 1) 的数组。

## 参考

- https://numpy.org/devdocs/reference/generated/numpy.vstack.html
