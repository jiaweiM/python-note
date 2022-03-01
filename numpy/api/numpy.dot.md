# numpy.dot

2022-02-15, 14:59
***

## 简介

```python
numpy.dot(a, b, out=None)
```

计算两个数组的点积：

- 如果 a 和 b 都是一维数组，则计算两个向量的内积
- 如果 a 和 b 都是二维数组，则为矩阵乘法，不过对矩阵乘法推荐使用 `matmul` 或 `a @ b`
- 如果 a 或 b 是标量，则等价于 `multiply`，推荐使用 `numpy.multiply(a, b)` 或 `a * b`
- 如果 a 是 N 维数组，b 是一维数组，

## 实例

```python
>>> np.dot(3, 4)
12
```

## 参考

- https://numpy.org/doc/stable/reference/generated/numpy.dot.html#
