# 快速入门

- [快速入门](#快速入门)
  - [基础](#基础)
    - [示例](#示例)
    - [创建数组](#创建数组)
    - [打印数组](#打印数组)
    - [基本操作](#基本操作)
    - [通用函数](#通用函数)
    - [索引、切片和迭代](#索引切片和迭代)
  - [Shape 操作](#shape-操作)
    - [改变 shape](#改变-shape)
    - [堆叠数组](#堆叠数组)

2020-06-05, 09:54
***

## 基础

NumPy 的主要对象是齐次多维数组，存储相同类型的元素，通过非负整数元祖索引。NumPy 数组的维度称为 `axes`。

例如，3D 空间的数据点 `[1, 2, 1]` 包含一个 axis。该 axis 包含 3 个元素，所以其长度为 3。下方的数组包含 2 个 axes。第一个长度为 2，第二个长度为 3，即 $2\times 3$ 数组：

```py
[[ 1., 0., 0.],
 [ 0., 1., 2.]]
```

> 多维数组，按照从外到内的方式进行编号。

NumPy 数组类为 `ndarray`，别名为 `array`。不过 `numpy.array` 和标准 Python 库 `array.array` 不同，该库只能处理一维数组，而且提供的功能较少。

`ndarray` 对象的重要属性如下：

|属性|说明|
|---|---|
|ndarray.ndim|维度|
|ndarray.shape|数组 shape|
|ndarray.size|总元素个数。等于 shape 元素乘积|
|ndarray.dtype|元素类型，可以使用标准 Python 类型，也可以使用 NumPy 类型|
|ndarray.itemsize|元素大小 bytes。例如 `float64` 为 8 字节|
|ndarray.data|包含实际元素的缓冲|

### 示例

```py
>>> import numpy as np
>>> a = np.arange(15).reshape(3, 5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> a.shape
(3, 5)
>>> a.ndim
2
>>> a.dtype.name
'int32'
>>> a.itemsize
4
>>> a.size
15
>>> type(a)
<class 'numpy.ndarray'>
>>> b = np.array([6, 7, 8])
>>> b
array([6, 7, 8])
>>> type(b)
<class 'numpy.ndarray'>
```

### 创建数组

创建数组的方式有多种。

- 可以使用 `array` 函数从Python 列表或元组创建。数组类型会自动通过元素类型推断

```py
>>> import numpy as np
>>> a = np.array([2, 3, 4])
>>> a
array([2, 3, 4])
>>> a.dtype
dtype('int64')
>>> b = np.array([1.2, 3.5, 5.1])
>>> b.dtype
dtype('float64')
```

- 使用 `array` 函数常见错误时，忘了使用序列类型

```py
>>> a = np.array(1, 2, 3, 4)    # WRONG
Traceback (most recent call last):
  ...
TypeError: array() takes from 1 to 2 positional arguments but 4 were given
>>> a = np.array([1, 2, 3, 4])  # RIGHT
```

- 对嵌套序列，`array` 将其转换为多维数组

```py
>>> b = np.array([(1.5, 2, 3), (4, 5, 6)])
>>> b
array([[1.5, 2. , 3. ],
       [4. , 5. , 6. ]])
```

- 在创建数组时，可以指定类型

```py
>>> c = np.array([[1, 2], [3, 4]], dtype=complex)
>>> c
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 4.+0.j]])
```

通常来说，在使用数组时，一般时先确定数组大小，然后才确定元素值。因此，NumPy 提供了几个函数用来创建指定大小的数组。

- 函数 `zeros` 创建元素全为 0 的数组；
- 函数 `ones` 创建元素全为 1 的数组；
- 函数 `empty` 创建初始内容随机的数组，元素具体值取决于内存状态；

创建数组的默认类型为 `float64`，可以通过 `dtype` 参数指定其它类型。

```py
>>> np.zeros((3, 4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> np.ones((2, 3, 4), dtype=np.int16)
array([[[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]],

       [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]], dtype=int16)
>>> np.empty((2, 3))
array([[3.73603959e-262, 6.02658058e-154, 6.55490914e-260],  # may vary
       [5.30498948e-313, 3.14673309e-307, 1.00000000e+000]])
```

- NumPy 提供了 `arange` 函数创建数值序列，该函数和 Python 的内置函数 `range` 功能类似，但是返回数组。

```py
>>> np.arange(10, 30, 5)
array([10, 15, 20, 25])
>>> np.arange(0, 2, 0.3)  # it accepts float arguments
array([0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
```

当使用浮点参数时，由于精度问题 `arange` 函数生成的数组包含元素个数就不确定。因此推荐使用 `linspace` 生成浮点数组：

```py
>>> from numpy import pi
>>> np.linspace(0, 2, 9)                   # 9 numbers from 0 to 2
array([0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ])
>>> x = np.linspace(0, 2 * pi, 100)        # useful to evaluate function at lots of points
>>> f = np.sin(x)
```

### 打印数组

当打印数组时，NumPy 以类似嵌套列表的方式显示：

- 最后一个 axis 从左到右打印；
- 导数第二 axis 从上到下打印；
- 余下也是从上到下打印，切片之间以空行分隔。

一维数组单行显示，二维以矩阵显示，三维数组则以矩阵列表显示：

```py
>>> a = np.arange(6)                    # 1d array
>>> print(a)
[0 1 2 3 4 5]
>>>
>>> b = np.arange(12).reshape(4, 3)     # 2d array
>>> print(b)
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
>>>
>>> c = np.arange(24).reshape(2, 3, 4)  # 3d array
>>> print(c)
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
```

如果数组太大，NumPy 会自动跳过中间部分，只打印几个角：

```py
>>> print(np.arange(10000))
[   0    1    2 ... 9997 9998 9999]
>>>
>>> print(np.arange(10000).reshape(100, 100))
[[   0    1    2 ...   97   98   99]
 [ 100  101  102 ...  197  198  199]
 [ 200  201  202 ...  297  298  299]
 ...
 [9700 9701 9702 ... 9797 9798 9799]
 [9800 9801 9802 ... 9897 9898 9899]
 [9900 9901 9902 ... 9997 9998 9999]]
```

要强制 NumPy 打印整个数组，可以使用 `set_printoptions` 函数设置：

```py
>>> np.set_printoptions(threshold=sys.maxsize)  # sys module should be imported
```

### 基本操作

数学运算逐元素计算。计算结果以新数组返回：

```py
>>> a = np.array([20, 30, 40, 50])
>>> b = np.arange(4)
>>> b
array([0, 1, 2, 3])
>>> c = a - b
>>> c
array([20, 29, 38, 47])
>>> b**2
array([0, 1, 4, 9])
>>> 10 * np.sin(a)
array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
>>> a < 35
array([ True,  True, False, False])
```

和矩阵运算不同，NumPy 中乘积运算符 `*` 是逐元素乘积。而矩阵乘用 `@` 运算符或 `dot` 函数：

```py
>>> A = np.array([[1, 1],
...               [0, 1]])
>>> B = np.array([[2, 0],
...               [3, 4]])
>>> A * B     # elementwise product
array([[2, 0],
       [0, 4]])
>>> A @ B     # matrix product
array([[5, 4],
       [3, 4]])
>>> A.dot(B)  # another matrix product
array([[5, 4],
       [3, 4]])
```

部分运算符 `+=`, `*=` 原位操作，不创建新数组，而是修改原数组：

```py
>>> rg = np.random.default_rng(1)  # create instance of default random number generator
>>> a = np.ones((2, 3), dtype=int)
>>> b = rg.random((2, 3))
>>> a *= 3
>>> a
array([[3, 3, 3],
       [3, 3, 3]])
>>> b += a
>>> b
array([[3.51182162, 3.9504637 , 3.14415961],
       [3.94864945, 3.31183145, 3.42332645]])
>>> a += b  # b is not automatically converted to integer type
Traceback (most recent call last):
    ...
numpy.core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int64') with casting rule 'same_kind'
```

当操作不同类型的数组时，所得数组类型和更精确的数组类型一致：

```py
>>> a = np.ones(3, dtype=np.int32)
>>> b = np.linspace(0, pi, 3)
>>> b.dtype.name
'float64'
>>> c = a + b
>>> c
array([1.        , 2.57079633, 4.14159265])
>>> c.dtype.name
'float64'
>>> d = np.exp(c * 1j)
>>> d
array([ 0.54030231+0.84147098j, -0.84147098+0.54030231j,
       -0.54030231-0.84147098j])
>>> d.dtype.name
'complex128'
```

许多一元运算，如计算数组中所有元素的和，包含在 `ndarray` 类中：

```py
>>> a = rg.random((2, 3))
>>> a
array([[0.82770259, 0.40919914, 0.54959369],
       [0.02755911, 0.75351311, 0.53814331]])
>>> a.sum()
3.1057109529998157
>>> a.min()
0.027559113243068367
>>> a.max()
0.8277025938204418
```

这些操作默认应用于整个数组元素，无论其 shape 是何样式。但是通过指定 `axis` 参数，可以将操作应用到指定轴：

```py
>>> b = np.arange(12).reshape(3, 4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
>>> b.sum(axis=0)     # sum of each column
array([12, 15, 18, 21])
>>>
>>> b.min(axis=1)     # min of each row
array([0, 4, 8])
>>>
>>> b.cumsum(axis=1)  # cumulative sum along each row
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]])
```

### 通用函数

NumPy 提供了我们熟悉的各种数学函数，这些函数称为通用函数（universal functions, ufunc）。在 NumPy 中，这些函数逐元素执行，返回相同 shape 的数组：

```py
>>> B = np.arange(3)
>>> B
array([0, 1, 2])
>>> np.exp(B)
array([1.        , 2.71828183, 7.3890561 ])
>>> np.sqrt(B)
array([0.        , 1.        , 1.41421356])
>>> C = np.array([2., -1., 4.])
>>> np.add(B, C)
array([2., 0., 6.])
```

### 索引、切片和迭代

NumPy 一维数组可以和 Python 序列一样索引、切片和迭代。

```py
>>> a = np.arange(10)**3
>>> a
array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
>>> a[2]
8
>>> a[2:5]
array([ 8, 27, 64])
>>> # equivalent to a[0:6:2] = 1000;
>>> # from start to position 6, exclusive, set every 2nd element to 1000
>>> a[:6:2] = 1000
>>> a
array([1000,    1, 1000,   27, 1000,  125,  216,  343,  512,  729])
>>> a[::-1]  # reversed a
array([ 729,  512,  343,  216,  125, 1000,   27, 1000,    1, 1000])
>>> for i in a:
...     print(i**(1 / 3.))
...
9.999999999999998
1.0
9.999999999999998
3.0
9.999999999999998
4.999999999999999
5.999999999999999
6.999999999999999
7.999999999999999
8.999999999999998
```

多维数组在每个 axis 都可以有一个索引。这些索引以元组类型提供：

```py
>>> def f(x, y):
...     return 10 * x + y
...
>>> b = np.fromfunction(f, (5, 4), dtype=int)
>>> b
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])
>>> b[2, 3]
23
>>> b[0:5, 1]  # each row in the second column of b
array([ 1, 11, 21, 31, 41])
>>> b[:, 1]    # equivalent to the previous example
array([ 1, 11, 21, 31, 41])
>>> b[1:3, :]  # each column in the second and third row of b
array([[10, 11, 12, 13],
       [20, 21, 22, 23]])
```

当提供的索引少于 axis 数，缺失索引默认为完整切片：

```py
>>> b[-1]   # the last row. Equivalent to b[-1, :]
array([40, 41, 42, 43])
```

表达式 `b[i]` 被解析为 `i` 后面跟着多个 `:`，以补全 axes。也可以使用 `b[i, ...]` 表示。

这三个点号 `...` 表示补全冒号以生成完整的索引元组。例如，如果 `x` 是包含 5 个 axes 的数组，则：

- `x[1, 2, ...]` 等价于 `x[1, 2, :, :, :]`
- `x[..., 3]` 等价于 `x[;, :, :, :, 3]`
- `x[4, ..., 5, :]` 等价于 `x[4, :, :, 5, :]`

```py
>>> c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
...                [ 10, 12, 13]],
...               [[100, 101, 102],
...                [110, 112, 113]]])
>>> c.shape
(2, 2, 3)
>>> c[1, ...]  # same as c[1, :, :] or c[1]
array([[100, 101, 102],
       [110, 112, 113]])
>>> c[..., 2]  # same as c[:, :, 2]
array([[  2,  13],
       [102, 113]])
```

迭代多维数组是对第一个 axis 进行的：

```py
>>> for row in b:
...     print(row)
...
[0 1 2 3]
[10 11 12 13]
[20 21 22 23]
[30 31 32 33]
[40 41 42 43]
```

如果想对每个元素依次迭代，可以使用 `flat` 属性，返回逐元素的迭代器：

```py
>>> for element in b.flat:
...     print(element)
...
0
1
2
3
10
11
12
13
20
21
22
23
30
31
32
33
40
41
42
43
```

## Shape 操作

### 改变 shape

shape 是数组在不同 axis 的元素个数：

```py
>>> a = np.floor(10 * rg.random((3, 4)))
>>> a
array([[3., 7., 3., 4.],
       [1., 4., 2., 2.],
       [7., 2., 4., 9.]])
>>> a.shape
(3, 4)
```

改变数组 shape 的方法有多种。以下三个函数返回修改后的数组，但是不改变原数组：

```py
>>> a.ravel()  # returns the array, flattened
array([3., 7., 3., 4., 1., 4., 2., 2., 7., 2., 4., 9.])
>>> a.reshape(6, 2)  # returns the array with a modified shape
array([[3., 7.],
       [3., 4.],
       [1., 4.],
       [2., 2.],
       [7., 2.],
       [4., 9.]])
>>> a.T  # returns the array, transposed
array([[3., 1., 7.],
       [7., 4., 2.],
       [3., 2., 4.],
       [4., 2., 9.]])
>>> a.T.shape
(4, 3)
>>> a.shape
(3, 4)
```

使用 `ravel` 生成数组的元素顺序为 C-样式，即最右边的元素改变最快，所以元素 `a[0, 0]` 后面的元素为 `a[0, 1]` 而不是 `a[1, 0]`。

不过 `ravel` 和 `reshape` 都有一个可选参数，可以将其设置为 FORTRAIN-样式，此时左侧索引变化最快。

`reshape` 函数返回一个新的数组，而 `ndarray.resize` 方法则修改原数组：

```py
>>> a
array([[3., 7., 3., 4.],
       [1., 4., 2., 2.],
       [7., 2., 4., 9.]])
>>> a.resize((2, 6))
>>> a
array([[3., 7., 3., 4., 1., 4.],
       [2., 2., 7., 2., 4., 9.]])
```

在 reshape 操作中，如果某个 axis 指定为 -1，则自定计算其值：

```py
>>> a.reshape(3, -1)
array([[3., 7., 3., 4.],
       [1., 4., 2., 2.],
       [7., 2., 4., 9.]])
```

### 堆叠数组

多个数组可以沿不同 axes 堆叠在一起：

```py
>>> a = np.floor(10 * rg.random((2, 2)))
>>> a
array([[9., 7.],
       [5., 2.]])
>>> b = np.floor(10 * rg.random((2, 2)))
>>> b
array([[1., 9.],
       [5., 1.]])
>>> np.vstack((a, b))
array([[9., 7.],
       [5., 2.],
       [1., 9.],
       [5., 1.]])
>>> np.hstack((a, b))
array([[9., 7., 1., 9.],
       [5., 2., 5., 1.]])
```

`column_stack` 函数将 1D 数组作为 column 添加到 2D 数组：

```py
>>> from numpy import newaxis
>>> np.column_stack((a, b))  # with 2D arrays
array([[9., 7., 1., 9.],
       [5., 2., 5., 1.]])
>>> a = np.array([4., 2.])
>>> b = np.array([3., 8.])
>>> np.column_stack((a, b))  # returns a 2D array
array([[4., 3.],
       [2., 8.]])
>>> np.hstack((a, b))        # the result is different
array([4., 2., 3., 8.])
>>> a[:, newaxis]  # view `a` as a 2D column vector
array([[4.],
       [2.]])
>>> np.column_stack((a[:, newaxis], b[:, newaxis]))
array([[4., 3.],
       [2., 8.]])
>>> np.hstack((a[:, newaxis], b[:, newaxis]))  # the result is the same
array([[4., 3.],
       [2., 8.]])
```
