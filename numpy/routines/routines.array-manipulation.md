# 数组操作

## 修改维度数

### numpy.expand_dims

```python
numpy.expand_dims(a, axis)
```

扩展数组的维度，在 `axis` 位置插入一个新的维度。

**参数：**

- **a** - array_like

输入数组。

- **axis** - int or tuple of ints

插入新维度的位置。

**示例：**

```python
>>> x = np.array([1, 2])
>>> x.shape
(2,)
```


- 下面等价于 `x[np.newaxis, :]` 或 `x[np.newaxis]`

```python
>>> y = np.expand_dims(x, axis=0)
>>> y
array([[1, 2]])
>>> y.shape
(1, 2)
```

即 shape 从 (2,) 扩展为 (1, 2)，在前面插入了一个轴。

- 下面等价于 `x[:, newaxis]`

```python
>>> y = np.expand_dims(x, axis=1)
>>> y
array([[1],
       [2]])
>>> y.shape
(2, 1)
```

即 shape 从 (2,) 扩展为 (2, 1)，在后面插入了一个轴。`axis=1` 指定新轴的位置。

- `axis` 可以为 tuple

```python
>>> y = np.expand_dims(x, axis=(0, 1))
>>> y
array([[[1, 2]]])
>>> y.shape
(1, 1, 2)
```

`axis=(0, 1)` 表示在新数组的 0 和 1 位个插入一个轴，所以新的数组 shape 为 (1, 1, 2)。

- 间隔插入新轴

```python
>>> y = np.expand_dims(x, axis=(2, 0))
>>> y
array([[[1],
        [2]]])
>>> y.shape
(1, 2, 1)
```

在新数组的 2th 和 0th 插入新轴。

- 上面的 `np.newaxis` 其实就是 `None`，所以也可以用 `None`：

```python
>>> np.newaxis is None
True
```

```python
>>> y = x[np.newaxis, :]
>>> y
array([[1, 2]])
>>> y = x[None, :]
>>> y
array([[1, 2]])
```

## 参考

- https://numpy.org/doc/stable/reference/routines.array-manipulation.html
