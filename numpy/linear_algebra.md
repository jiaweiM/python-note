# 线性代数运算

- [线性代数运算](#线性代数运算)
  - [简介](#简介)
  - [@ 操作符](#-操作符)
  - [乘积运算](#乘积运算)
    - [dot](#dot)
  - [参考](#参考)

2021-05-26, 16:52
@Jiawei Mao
***

## 简介

NumPy 使用 BLAS 和 LAPACK 提供高效的线性代数算法的底层实现。SciPy 包也包含一个 `linalg` 子模块，SciPy 和 NumPy 子模块提供的功能存在重叠，而且 SciPy 包含 `numpy.linalg` 中没有的函数，例如 LU 分解和 Schur 分解函数；两者都有的函数，在 scipy.linalg 中往往进行了增强。NumPy 的最大优点是某些功能具有灵活的广播选项。

## @ 操作符

在 NumPy 1.10.0 中引入的 `@` 运算符是计算矩阵乘积的推荐方法，函数 `numpy.matmul` 函数实现了该运算符。

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

- [Linear algebra](https://numpy.org/devdocs/reference/routines.linalg.html)
