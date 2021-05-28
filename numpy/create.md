# 创建数组

- [创建数组](#创建数组)
  - [简介](#简介)
  - [将 Python 数据结构转换为 NumPy 数组](#将-python-数据结构转换为-numpy-数组)
  - [`empty`](#empty)
  - [`empty_like`](#empty_like)
  - [`array`](#array)
  - [Ones and zeros](#ones-and-zeros)
    - [zeros](#zeros)
  - [从已有数据创建](#从已有数据创建)
    - [array](#array-1)
  - [参考](#参考)

## 简介

创建 NumPy 数组有 5 种方法：

1. 将其它 Python 数据结构（如 list, tuples）转换为数组
2. numpy 内置的创建方法（如 arange, ones, zeros 等）
3. 从硬盘读取数组
4. 通过字符串或缓存从字节创建数组
5. 使用特定的库函数

## 将 Python 数据结构转换为 NumPy 数组

使用 `array()` 函数将 Python 中类数组解构转换为 NumPy 数组。

## `empty`
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

## `empty_like`
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

## `array` 

## Ones and zeros

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

- 

## 从已有数据创建

### array

```py
numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)
```



## 参考

- [Array creation routines](https://numpy.org/doc/stable/reference/routines.array-creation.html)
- [Array creation](https://numpy.org/doc/stable/user/basics.creation.html#arrays-creation)
