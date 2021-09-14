# 创建数组

- [创建数组](#创建数组)
  - [简介](#简介)
    - [1) 将 Python 序列转换为 NumPy 数组](#1-将-python-序列转换为-numpy-数组)
    - [2) NumPy 函数](#2-numpy-函数)
      - [创建 1D 数组](#创建-1d-数组)
      - [创建 2D 数组](#创建-2d-数组)
      - [通用数组创建函数](#通用数组创建函数)
    - [3) 复制、连接和修改已有数组](#3-复制连接和修改已有数组)
    - [4) 从文件读取数组](#4-从文件读取数组)
      - [标准二进制格式](#标准二进制格式)
      - [ASCII 格式](#ascii-格式)
    - [5) 通过字符串或缓冲的字节创建](#5-通过字符串或缓冲的字节创建)
    - [6. 使用其它库函数](#6-使用其它库函数)
  - [从 shape 或值创建](#从-shape-或值创建)
    - [`empty`](#empty)
    - [`empty_like`](#empty_like)
    - [zeros](#zeros)
  - [从已有数据创建](#从已有数据创建)
  - [创建 record 数组](#创建-record-数组)
  - [创建字符数组](#创建字符数组)
  - [数值范围](#数值范围)
  - [矩阵](#矩阵)
  - [矩阵类](#矩阵类)
  - [参考](#参考)

2021-06-23, 14:45, v1.1
***

## 简介

创建 NumPy 数组有 6 种机制：

1. 将其它 Python 数据结构（如 list, tuple）转换为数组
2. numpy 内置创建方法（如 arange, ones, zeros 等）
3. 复制、连接或修改已有数组
4. 从文件读取数组
5. 通过字符串或缓存从字节创建数组
6. 使用特定库的函数，如 pandas 等

### 1) 将 Python 序列转换为 NumPy 数组

可以用 Python 序列（如列表、元组）创建 ndarray:

- 数值列表转换为 1D array
- 内嵌一层的列表转换为 2D array
- 内嵌多层的列表转换为高维 array。

使用 `array()` 函数将 Python 序列转换为 NumPy 数组。

- 列表 -> 数组

```py
>>> a1D = np.array([1, 2, 3, 4])
>>> a2D = np.array([[1, 2], [3, 4]])
>>> a3D = np.array([[[1, 2], [3, 4]],
                    [[5, 6], [7, 8]]])
```

在使用 `numpy.array` 定义数组时，可以通过 `dtype` 参数指定数据类型。如果 `dtype` 设置不对，可能导致溢出，例如：

```py
>>> a = np.array([127, 128, 129], dtype=np.int8)
>>> a
array([ 127, -128, -127], dtype=int8)
```

8 字节的 signed 整数在 [-128, 127] 之间，128 和 129 超出该范围。

使用不兼容的 `dtype` 计算也会导致错误：

```py
>>> a = array([2, 3, 4], dtype = np.uint32)
>>> b = array([5, 6, 7], dtype = np.uint32)
>>> c_unsigned32 = a - b # 这里 c 是负数，而 uint32 只能表示正数
>>> print('unsigned c:', c_unsigned32, c_unsigned32.dtype)
unsigned c: [4294967293 4294967293 4294967293] uint32
>>> c_signed32 = a - b.astype(np.int32)
>>> print('signed c:', c_signed32, c_signed32.dtype)
signed c: [-3 -3 -3] int64
```

当使用相同的 `dtype:uint32` 类型计算，返回的数组也是该类型。如果执行不同类型 `dtype` 计算，NumPy 会返回一个满足所有元素的类型，这里 `uint32` 和 `int32` 都可以用 `int64` 表示。

NumPy 创建数组，整数类型默认用 `int64`，浮点数默认用 `float`。

### 2) NumPy 函数

NumPy 包含 40 多个创建数组的内置函数。这些函数根据创建的数组 shape 大致可以分为三类：

1. 1D 数组
2. 2D 数组
3. ndarray

#### 创建 1D 数组

1D 数组创建函数，如 `numpy.linspace` 和 `numpy.arange`，一般需要 2 个参数，`start` 和 `stop`。

- `numpy.arange` 按数值递增创建数组。例如：

```py
>>> np.arange(10) # 和 range() 函数类似
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.arange(2, 10, dtype=float)
array([ 2., 3., 4., 5., 6., 7., 8., 9.])
>>> np.arange(2, 3, 0.1) # 设置增量值
array([ 2. , 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9])
```

> `numpy.arange` 的参数 `start`, `end` 和 `step` 最好使用整数，对浮点数，由于四舍五入的影响，偶尔会包含 `stop` 值。

- `numpy.linsapce` 在指定区间创建包含指定元素个数的数组，元素之间等距。例如：

```py
>>> np.linspace(1., 4., 6)
array([ 1. ,  1.6,  2.2,  2.8,  3.4,  4. ])
```

该函数的优势在于肯定包含起点和终点，可以保证元素的数量。

#### 创建 2D 数组

创建 2D 数组函数如 `numpy.eye`, `numpy.diag` 和 `numpy.vander` 以 2D 数组的形式定义了一些特殊矩阵。

- `np.eye(n, m)` 创建 2D 单位矩阵，即 i=j 位置的元素为 1，其余位置元素为 0.例如：

```py
>>> np.eye(3)
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
>>> np.eye(3, 5)
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.]])
```

- `numpy.diag` 以指定值创建一个方形矩阵，对角线以指定值填充。例如：

```py
>>> np.diag([1, 2, 3])
array([[1, 0, 0],
       [0, 2, 0],
       [0, 0, 3]])
>>> np.diag([1, 2, 3], 1)
array([[0, 1, 0, 0],
       [0, 0, 2, 0],
       [0, 0, 0, 3],
       [0, 0, 0, 0]])
>>> a = np.array([[1, 2], [3, 4]])
>>> np.diag(a)
array([1, 4])
```

- `numpy.vander(x, n)` 以 2D NumPy 数组形式定义范德蒙矩阵

范德蒙矩阵的列为输入 1D 序列 `x` 的递减指数值，最高阶为 `n-1`。该函数在生成线性最小二乘模型时很有用，例如：

```py
>>> np.vander(np.linspace(0, 2, 5), 2)
array([[0.  , 0.  , 1.  ],
       [0.25, 0.5 , 1.  ],
       [1.  , 1.  , 1.  ],
       [2.25, 1.5 , 1.  ],
       [4.  , 2.  , 1.  ]])
>>> np.vander([1, 2, 3, 4], 2) # 1 次方和 0 次方
array([[1, 1],
       [2, 1],
       [3, 1],
       [4, 1]])
>>> np.vander((1, 2, 3, 4), 4) # 3，2，1次方
array([[ 1,  1,  1,  1],
       [ 8,  4,  2,  1],
       [27,  9,  3,  1],
       [64, 16,  4,  1]])
```

#### 通用数组创建函数

`numpy.ones`, `numpy.zeros` 和 `random` 根据指定 shape 创建函数。

`numpy.zeros` 创建全 0 数组，默认 `dtype` 为 `float64`：

```py
>>> np.zeros((2, 3))
array([[0., 0., 0.],
       [0., 0., 0.]])
>>> np.zeros((2, 3, 2))
array([[[0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0., 0.]]])
```

`numpy.ones` 创建全 1 数组。其它性质和 `numpy.zeros` 完全相同：

```py
>>> np.ones((2, 3))
array([[ 1., 1., 1.],
       [ 1., 1., 1.]])
>>> np.ones((2, 3, 2))
array([[[1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.]]])
```

`default_rng` 的 `random` 方法创建以 0,1 之间的随机值填充的数组。例如，创建 shape 为 (2,3) 和 (2,3,2) 两个数组。seed 设置为 42 以保证生成伪随机数的可重复性：

```py
>>> import numpy.random.default_rng
>>> default_rng(42).random((2,3))
array([[0.77395605, 0.43887844, 0.85859792],
       [0.69736803, 0.09417735, 0.97562235]])
>>> default_rng(42).random((2,3,2))
array([[[0.77395605, 0.43887844],
        [0.85859792, 0.69736803],
        [0.09417735, 0.97562235]],
       [[0.7611397 , 0.78606431],
        [0.12811363, 0.45038594],
        [0.37079802, 0.92676499]]])
```

### 3) 复制、连接和修改已有数组

对已有数组进行复制、连接或修改创建新数组。

- 使用 `numpy.copy` 复制数组

```py
>>> a = np.array([1, 2, 3, 4, 5, 6])
>>> b = a[:2]
>>> b += 1
>>> print('a =', a, '; b =', b)
a = [2 3 3 4 5 6]; b = [2 3]
```

这里使用 `a[:2]` 并没有创建一个新的数组，而是返回一个原数组的视图。所以在修改 `b` 后，`a` 对应元素的值也发生了改变。如果要复制数组，还是要用 `numpy.copy()`：

```py
>>> a = np.array([1, 2, 3, 4])
>>> b = a[:2].copy()
>>> b += 1
>>> print('a = ', a, 'b = ', b)
a =  [1 2 3 4 5 6] b =  [2 3]
```

连接已有数组的方法有许多，如 `numpy.vstack`, `numpy.hastack` 以及 `numpy.block`。下面使用 `block` 连接 4 个 2x2 数组，获得一个 4x4 数组：

```py
>>> A = np.ones((2, 2))
>>> B = np.eye((2, 2))
>>> C = np.zeros((2, 2))
>>> D = np.diag((-3, -4))
>>> np.block([[A, B],
              [C, D]])
array([[ 1.,  1.,  1.,  0. ],
       [ 1.,  1.,  0.,  1. ],
       [ 0.,  0., -3.,  0. ],
       [ 0.,  0.,  0., -4. ]])
```

其他方法使用类似的语法连接数组。

### 4) 从文件读取数组

这是创建大型数组的常用方式。具体细节取决于文件格式。下面大致介绍如何处理各种格式的文件。更多内容可以参考读写文件部分。

#### 标准二进制格式

许多领域有针对数组数据的标准格式。下面两个已知有 Python 库可以读取并返回 NumPy 数组：

- HDF5:h5py
- FITS:Astropy

有些不能直接返回 NumPy 数组，但是可以很容易转换为 NumPy 数组，例如 PIL 库（读写图片文件，如 jpg, png 等）.

#### ASCII 格式

分隔文件，如逗号分隔文件（csv）和 tab 分隔文件（tab），Python 都可以逐行读取。NumPy 有两个函数可用于读取这类文件，`numpy.loadtxt` 和 `numpy.genfromtxt`。在读写文件部分会详细介绍。下面是一个简单的 csv 文件 `simple.csv`：

```py
$ cat simple.csv
x, y
0, 0
1, 1
2, 4
3, 9
```

使用 `loadtxt` 导入 `simple.csv`：

```py
>>> np.loadtxt('simple.csv', delimiter = ',', skiprows = 1) 
array([[0., 0.],
       [1., 1.],
       [2., 4.],
       [3., 9.]])
```

一些更通用的ASCII 文件可以使用 `scipy.io` 和 `pandas` 读写。

### 5) 通过字符串或缓冲的字节创建

如果文件格式简单，则可以直接使用 NumPy 的 `fromfile()` 和 `.tofile()` 方法直接读写 NumPy 数组（需要注意 byteorder）。

### 6. 使用其它库函数

NumPy 是一个用于数组操作的 Python 数值计算库，许多其它 Python 库，如 SciPy, Pandas 以及 OpenCV，使用 NumPy 数组作为数据交换通用格式，这些库提供了创建和修改 NumPy 数组功能。

## 从 shape 或值创建

|函数|说明|
|---|---|
|[`empty(shape[, dtype, order, like])`](#empty)|以指定 shape 和 type 创建空数组|
|`empty_like(prototype[, dtype, order, subok, …])`|创建一个 shape 和 dtype 与指定数组相同的空数组|
|`eye(N[, M, k, dtype, order, like])`|创建对角线为 1，其余值为 0 的 2D 数组，即单位矩阵|
|`identity(n[, dtype, like])`|创建单位矩阵|
|`ones(shape[, dtype, order, like])`|以指定shape 和 dtype 创建 1 填充的数组|
|`ones_like(a[, dtype, order, subok, shape])`|类似 `empty_like`，以 1 填充|
|`zeros(shape[, dtype, order, like])`|创建 0 矩阵|
|`zeros_like(a[, dtype, order, subok, shape])`|类似 `ones_like`，以 0 填充|
|`full(shape, fill_value[, dtype, order, like])`|以指定 shape 和 type 创建以 `fill_value` 填充的数组|
|`full_like(a, fill_value[, dtype, order, …])`|类似 `ones_like`，填充值为 `fill_value`|

### `empty`

```py
numpy.empty(shape, dtype=float, order='C')
```

创建指定类型和大小的数组，不初始化值。
> `empty` 和 `zeros`的差别在于它不初始化数组，所以速度稍微快些。

|参数|类型|说明|
|---|---|---|
|shape|int or tuple of int|数组大小，如 (2, 3) 或 2|
|dtype|data-type, optional|数据类型，默认为 `numpy.float64`|
|order|{'C', 'F'}, default 'C'|数据保存方式，按行（C-style）或按列（Fortran-style）|

例：

```py
a = np.empty([2, 2])
assert a.shape == (2, 2)

# array with shape=(3, 2), values of the array are random
a = np.empty([3, 2], dtype=np.int32)
assert a.shape == (3, 2)
assert a.dtype == np.int32

a = np.empty([3, 3])
assert a.dtype == np.float64
```

### `empty_like`

```py
numpy.empty_like(prototype, dtype=None, order='K', subok=True, shape=None)
```

返回和指定数组相同大小和类型的数组。

|参数|类型|说明|
|---|---|---|
|prototype|array_like|该数组为新的数组具有相同的属性|
|dtype|data-type,optional|指定数据类型|
|order|{'C', 'F', 'A', 'K'}|'C', C-order; 'F', F-order; 'A', as prototype; 'K', match the layout of the prototype as closely as possible|
|subok|bool, optional|True,新数组为 'a' 的子类型；False，为基类数组类型|
|shape|int or sequence of ints||

### zeros

创建指定 shape 和 type 的全 0 数组。

```py
numpy.zeros(shape, dtype=float, order='C', *, like=None)
```

|参数|说明|
|---|---|
|shape|数组 shape|
|dtype|数组类型，默认类型 `numpy.float64`|
|order|以行（C）还是以列（F）存储数组|

- 创建一维数组

```py
>>> np.zeros(5)
array([ 0.,  0.,  0.,  0.,  0.])
```

- 指定类型

```py
>>> np.zeros((5,), dtype=int)
array([0, 0, 0, 0, 0])
```

## 从已有数据创建

|方法|说明|
|---|---|
|`array(object[, dtype, copy, order, subok, …])`|Create an array.|
|`asarray(a[, dtype, order, like])`|Convert the input to an array.|
|`asanyarray(a[, dtype, order, like])`|Convert the input to an ndarray, but pass ndarray subclasses through.|
|`ascontiguousarray(a[, dtype, like])`|Return a contiguous array (ndim >= 1) in memory (C order).|
|`asmatrix(data[, dtype])`|Interpret the input as a matrix.|
|`copy(a[, order, subok])`|Return an array copy of the given object.|
|`frombuffer(buffer[, dtype, count, offset, like])`|Interpret a buffer as a 1-dimensional array.|
|`fromfile(file[, dtype, count, sep, offset, like])`|Construct an array from data in a text or binary file.|
|`fromfunction(function, shape, *[, dtype, like])`|Construct an array by executing a function over each coordinate.|
|`fromiter(iter, dtype[, count, like])`|Create a new 1-dimensional array from an iterable object.|
|`fromstring(string[, dtype, count, sep, like])`|A new 1-D array initialized from text data in a string.|
|`loadtxt(fname[, dtype, comments, delimiter, …])`|Load data from a text file.|

## 创建 record 数组

> 推荐别名 `numpy.rec`

|方法|说明|
|---|---|
|`core.records.array(obj[, dtype, shape, …])`|Construct a record array from a wide-variety of objects.|
|`core.records.fromarrays(arrayList[, dtype, …])`|Create a record array from a (flat) list of arrays|
|`core.records.fromrecords(recList[, dtype, …])`|Create a recarray from a list of records in text form.|
|`core.records.fromstring(datastring[, dtype, …])`|Create a record array from binary data|
|`core.records.fromfile(fd[, dtype, shape, …])`|Create an array from binary file data|

## 创建字符数组

> 推荐别名 `numpy.char`

|方法|说明|
|---|---|
|`core.defchararray.array(obj[, itemsize, …])`|Create a chararray.|
|`core.defchararray.asarray(obj[, itemsize, …])`|Convert the input to a chararray, copying the data only if necessary.|

## 数值范围

|方法|说明|
|---|---|
|`arange([start,] stop[, step,][, dtype, like])`|Return evenly spaced values within a given interval.|
|`linspace(start, stop[, num, endpoint, …])`|Return evenly spaced numbers over a specified interval.|
|`logspace(start, stop[, num, endpoint, base, …])`|Return numbers spaced evenly on a log scale.|
|`geomspace(start, stop[, num, endpoint, …])`|Return numbers spaced evenly on a log scale (a geometric progression).|
|`meshgrid(*xi[, copy, sparse, indexing])`|Return coordinate matrices from coordinate vectors.|
|`mgrid`|nd_grid instance which returns a dense multi-dimensional “meshgrid”.|
|`ogrid`|nd_grid instance which returns an open multi-dimensional “meshgrid”.|

## 矩阵

|方法|说明|
|---|---|
|`diag(v[, k])`|Extract a diagonal or construct a diagonal array.|
|`diagflat(v[, k])`|Create a two-dimensional array with the flattened input as a diagonal.|
|`tri(N[, M, k, dtype, like])`|An array with ones at and below the given diagonal and zeros elsewhere.|
|`tril(m[, k])`|Lower triangle of an array.|
|`triu(m[, k])`|Upper triangle of an array.|
|`vander(x[, N, increasing])`|Generate a Vandermonde matrix.|

## 矩阵类

|方法|说明|
|---|---|
|·mat(data[, dtype])`|Interpret the input as a matrix.|
|·bmat(obj[, ldict, gdict])`|Build a matrix object from a string, nested sequence, or array.|

## 参考

- [Array creation routines](https://numpy.org/doc/stable/reference/routines.array-creation.html)
- [Array creation](https://numpy.org/doc/stable/user/basics.creation.html#arrays-creation)
