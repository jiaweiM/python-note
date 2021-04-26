# Tensor 操作

- [Tensor 操作](#tensor-操作)
  - [合并和拆分](#合并和拆分)
    - [tf.concat](#tfconcat)
    - [tf.repeat](#tfrepeat)
    - [tf.stack](#tfstack)
    - [tf.unstack](#tfunstack)
    - [tf.tile](#tftile)
  - [排序](#排序)
    - [tf.sort](#tfsort)
    - [tf.argsort](#tfargsort)
    - [tf.math.top_k](#tfmathtop_k)
    - [tf.math.maximum](#tfmathmaximum)
    - [tf.math.minimum](#tfmathminimum)
  - [限幅](#限幅)
    - [tf.clip_by_value](#tfclip_by_value)
    - [tf.clip_by_norm](#tfclip_by_norm)
    - [tf.nn.relu](#tfnnrelu)
    - [tf.clip_by_global_norm](#tfclip_by_global_norm)
  - [选择](#选择)
    - [where](#where)

2021-04-13, 10:38

## 合并和拆分

### tf.concat

在一个维度合并 tensor。

```py
tf.concat(
    values, axis, name='concat'
)
```

沿着 `axis` 维度合并 tensor 列表 `values`。

如果 `values[i].shape = [D0, D1, ... Daxis(i),...Dn]`，则串联后的 shape 为：

```py
[D0, D1, ... Raxis, ...Dn]
```

其中：

```py
Raxis = sum(Daxis(i))
```

即，输入 tensors 沿着维度 `axis` 合并。

输入 tensor 维数必须匹配，除了 `axis` 外，其他维度必须相等。

### tf.repeat

```py
tf.repeat(
    input, repeats, axis=None, name=None
)
```

重复 `input` 中的元素。


### tf.stack

将一组 rank 为 `R` 的 tensors 合并为一个 rank `R+1` 的 tensor。

```py
tf.stack(
    values, axis=0, name='stack'
)
```

将 `values` 中的一组 tensors 沿着 `axis` 堆叠为一个 rank 值大一个的 tensor。

如果有 `N` 个 tensor，shape 均为 `(A, B, C)`：

- 如果 `axis == 0`，则输出 tensor 的 shape 为 `(N, A, B, C)`
- 如果 `axis == 1`，则输出 tensor 的 shape 为 `(A, N, B, C)`

例如：

```py
x = tf.constant([1, 4])
y = tf.constant([2, 5])
z = tf.constant([3, 6])
v = tf.stack([x, y, z])
tf.assert_equal(v, tf.constant([[1, 4], [2, 5], [3, 6]]))

v1 = tf.stack([x, y, z], axis=1)
tf.assert_equal(v1, tf.constant([[1, 2, 3], [4, 5, 6]]))
```

### tf.unstack

```py
tf.unstack(
    value, num=None, axis=0, name='unstack'
)
```



### tf.tile

通过重复一个 tensor 多次来创建一个新的 tensor.

```py
tf.tile(
    input, multiples, name=None
)
```

通过重复 `input` tensor `multiples` 次创建新 tensor：
- 输出 tensor 的第 i 维包含 `input.dims(i) * multiples[i]` 个元素
- `input` 的值在第 i 维重复 `multiples[i]` 次。

例如：

```py
a = tf.constant([[1, 2, 3], [4, 5, 6]], tf.int32)
b = tf.constant([1, 2], tf.int32)

v = tf.tile(a, b)
tf.assert_equal(v, tf.constant([[1, 2, 3, 1, 2, 3], [4, 5, 6, 4, 5, 6]], tf.int32))

c = tf.constant([2, 1], tf.int32)
v = tf.tile(a, c)
tf.assert_equal(v, tf.constant([[1, 2, 3], [4, 5, 6],
                                [1, 2, 3], [4, 5, 6]]))

d = tf.constant([2, 2], tf.int32)
v = tf.tile(a, d)
tf.assert_equal(v, tf.constant([[1, 2, 3, 1, 2, 3],
                                [4, 5, 6, 4, 5, 6],
                                [1, 2, 3, 1, 2, 3],
                                [4, 5, 6, 4, 5, 6]]))
```

`multiples` 为 `Tensor`，类型必须为 `int32`, `int64`。长度必须和 `input` 的 rank 相同。

## 排序

### tf.sort

### tf.argsort

### tf.math.top_k

### tf.math.maximum

### tf.math.minimum

## 限幅

### tf.clip_by_value

### tf.clip_by_norm

### tf.nn.relu

### tf.clip_by_global_norm

根据范数和进行限幅。

```py
tf.clip_by_global_norm(
    t_list, clip_norm, use_norm=None, name=None
)
```

对 tensor 列表 `t_list` 和

## 选择

### where


