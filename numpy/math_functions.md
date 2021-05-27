# 数学函数

- [数学函数](#数学函数)
  - [三角函数](#三角函数)
  - [算术运算](#算术运算)
    - [multiply](#multiply)
  - [参考](#参考)

2021-05-26, 18:35
@Jiawei Mao
***

## 三角函数

## 算术运算

|方法|说明|
|---|---|
|multiply|逐个元素相乘|

### multiply

```py
numpy.multiply(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) = <ufunc 'multiply'>
```

参数逐个元素相乘。

1. 对标量，直接相乘

```py
assert np.multiply(2.0, 4.0) == 8.0
```

2. 当 shape 不一致，支持广播

```py
x1 = np.arange(9.0).reshape((3, 3))
x2 = np.arange(3.0)
c = np.multiply(x1, x2)
np.testing.assert_array_equal(c, np.array([[0, 1, 4],
                                            [0, 4, 10],
                                            [0, 7, 16]]))
```

3. `*` 和 `np.multiply` 等价

```py
x1 = np.arange(9.0).reshape((3, 3))
x2 = np.arange(3.0)
c = x1 * x2
np.testing.assert_array_equal(c, np.array([[0, 1, 4],
                                            [0, 4, 10],
                                            [0, 7, 16]]))
```

## 参考

- [Mathematical functions](https://numpy.org/devdocs/reference/routines.math.html)
