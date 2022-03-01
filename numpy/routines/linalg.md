# 线性代数（`numpy.linalg`）

2022-02-15, 14:48
***

## 简介

NumPy 线性代数函数依赖于 BLAS 和 LAPACK 提供标准线性代数算法的高效底层实现。

SciPy 也包含一个 `linalg` 子模块，SciPy 和 NumPy 线性代数模块提供的功能有所重叠。SciPy 包含 `numpy.linalg` 中没有的函数，例如 LU 分解和 Schur 分解相关函数等。两者都有的函数，在 `scipy.linalg` 中往往进行了增强。NumPy 的最大优点是部分函数具有灵活的广播选项。例如，`numpy.linalg.solve` 可以处理“堆叠”的数组，而 `scipy.linalg.solve` 只接受正方形数组作为第一个参数。

## @ 操作符

在 NumPy 1.10.0 引入的 `@` 运算符是计算二维数组之间的矩阵乘积的推荐方法，函数 `numpy.matmul` 函数实现了该运算符。

## 矩阵和向量乘积



## 乘积运算

### dot

```py
numpy.dot(a, b, out=None)
```

计算 a 和 b 的点乘。

|参数|说明|
|---|---|
|a|数组|
|b|数组|
|out|`ndarray`，输出结果|

- 如果 a 或  b 有一个是标量，则等价于 `multiply`，推荐使用 `numpy.multiply(a, b)` 或 `a * b` 计算；
- 如果 a 是 N-D 数组，b 是 1D 数组，

1. 如果 a 和 b 都是标量，返回乘积

```py
c = np.dot(4, 5)
assert c == 20
```

2. 如果 a 和 b 有一个是标量，计算

2. 如果 a 和 b 都是 1-D 数组，返回两个向量的内积

```py
c = np.dot([1, 2], [3, 4])
assert c == 11
```

3. 如果 a 和 b 都是 2-D 数组，执行矩阵乘法

```py
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
c = np.dot(a, b)
np.testing.assert_array_equal(c, np.array([[4, 1], [2, 2]]))
```

矩阵乘法建议用 `matmul` 方法或者 `a @ b` 这种语法。

4. 



## 参考

- https://numpy.org/doc/stable/reference/routines.linalg.html
