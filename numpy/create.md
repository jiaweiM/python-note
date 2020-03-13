- [简介](#%e7%ae%80%e4%bb%8b)
- [将 Python 对象转换为 NumPy 数组](#%e5%b0%86-python-%e5%af%b9%e8%b1%a1%e8%bd%ac%e6%8d%a2%e4%b8%ba-numpy-%e6%95%b0%e7%bb%84)
- [NumPy 创建方法](#numpy-%e5%88%9b%e5%bb%ba%e6%96%b9%e6%b3%95)
  - [`empty`](#empty)
  - [`empty_like`](#emptylike)
  - [`array`](#array)

# [简介](https://numpy.org/doc/1.17/user/basics.creation.html#arrays-creation)

创建数组有 5 种机制：
1. 将其它Python数据结构（如 list, tuples）转换为数组
2. numpy 创建方法（如 arange, ones, zeros 等）
3. 从硬盘读取数组
4. 通过字符串或缓存从字节创建数组
5. 使用特定的库函数

# 将 Python 对象转换为 NumPy 数组

# NumPy 创建方法

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