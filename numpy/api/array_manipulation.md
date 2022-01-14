# 数组操作

- [数组操作](#数组操作)
  - [基本操作](#基本操作)
    - [copyto](#copyto)
  - [修改数组形状](#修改数组形状)
    - [reshape](#reshape)
  - [修改维度数](#修改维度数)
  - [合并数组](#合并数组)
  - [参考](#参考)

2021-05-26, 10:44
@Jiawei Mao
***

## 基本操作

### copyto

```py
numpy.copyto(dst, src, casting='same_kind', where=True)
```

将值从一个数组赋值到另一个数组，必要时进行广播（broadcast）。


## 修改数组形状

|方法|功能|
|---|---|
|`reshape(a, newshape[, order])`|在不修改数据的情况下修改数组形状|

### reshape

修改数组形状。

```py
numpy.reshape(a, newshape, order='C')
```

- `a` 是待修改的数组
- `newshape`： int 或 tuple of ints

新的形状必须和原来的形状兼容：如果为整数，则新数组为该长度的一维数组；也可以为 -1，此时一维数组长度根据原数组的维度推算。

- `order`

按照该顺序读取原数组 `a` 的元素，并以该顺序放入新的数组。

'C' 表示以 C-like 索引顺序读写元素，最后一个轴的索引更改最快，第一个轴的更改最慢。

'F' 表示以 Fortran-like 索引顺序读写元素，与 C-like 相反。

'C' 和 'F' 选项不考虑底层数组的内存布局，只引用索引顺序。

'A' 即自动，采用和数组 `a` 一样的索引顺序。

> 有时候无法在不复制数据的情况下更改数组形状，如果希望在复制数据的抛出错误，

```py
a = np.array([[1,2,3], [4,5,6]])
np.reshape(a, 6)
# array([1, 2, 3, 4, 5, 6])

np.reshape(a, 6, order='F')
# array([1, 4, 2, 5, 3, 6])

np.reshape(a, (3,-1))       # the unspecified value is inferred to be 2
# array([[1, 2],
#        [3, 4],
#        [5, 6]])
```

## 修改维度数

|方法|功能|
|---|---|
|[expand_dims(a, axis)](numpy.expand_dims.md)|扩展数组 shape|

## 合并数组

|方法|功能|
|---|---|
|[vstack(tup)](numpy.vstack.md)|按顺序垂直（逐行）堆叠数组|

## 参考

- https://numpy.org/devdocs/reference/routines.array-manipulation.html
