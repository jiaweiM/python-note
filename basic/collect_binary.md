# Binary Sequence

- [Binary Sequence](#binary-sequence)
  - [简介](#简介)
  - [字节对象](#字节对象)
  - [memoryview](#memoryview)
    - [使用](#使用)
    - [cast](#cast)

2021-06-15, 14:23
***

## 简介

用于操作二进制数据的内置类型主要为 `bytes` 和 `bytearray`。

## 字节对象

Bytes 是不可变单字节序列。由于许多主要的二进制协议都是基于 ASCII 编码的，所以 `bytes` 提供了几种处理 ASCII 数据的方法。



## memoryview

缓冲区协议提供了一种访问对象内部数据的方法，这个内部数据是一个内存数组或缓冲区。缓冲区协议允许一个对象公开内部数据（缓冲区），而另一个对象不需要复制就可以访问这些缓冲区。

`memoryview` 是 Python 公开缓冲区协议的一种安全方式，允许创建内存视图对象访问对象的内部缓冲区。

当对象执行某些操作（如调用函数，切片数组），Python 往往需要创建对象的副本。如果我们有大量数据，此时创建副本的开销就很大。使用缓冲区协议，就给另一个对象访问、修改大数据，而不需要复制它。从而减少了程序的内存占用，提供了执行速度。

### 使用

```py
memoryview(object)
```

创建引用 `object` 对象的内存视图。`object` 必须是支持缓冲协议的对象，支持缓冲协议的内置类型有 `bytes` 和 `bytearray`。

例如：

```py
random_byte_array = bytearray('ABC', 'utf-8')
mv = memoryview(random_byte_array)

assert mv[0] == 65
assert bytes(mv[0:2]) == b'AB'
assert list(mv[0:3]) == [65, 66, 67]
```

通过 `memoryview` 修改值：

```py
random_byte_array = bytearray('ABC', 'utf-8')
assert bytes(random_byte_array) == b'ABC'

mv = memoryview(random_byte_array)
mv[1] = 90  # 对应字母 Z
assert bytes(random_byte_array) == b'AZC'
```

### cast

```py
cast(format[, shape])
```

将 memoryview 转换为新的格式或 shape。shape 默认为 `[byte_length//new_itemsize]`，即新视图为一维。返回一个新的 `memoryview`，但是不复制缓冲区。

支持 1D-> C-contiguous 和 C-contiguous->1D 转换。目标格式仅限于 `struct` 语法中的单元素本机格式。另一个格式必须为 byte 格式（'B', 'b', 'c'）。结果字节长度必须和原长度相同。

- 将 1D/long 转换为 1D/unsigned bytes

```py
>>> import array
>>> a = array.array('l', [1,2,3])
>>> x = memoryview(a)
>>> x.format
'l'
>>> x.itemsize
8
>>> len(x)
3
>>> x.nbytes
24
>>> y = x.cast('B')
>>> y.format
'B'
>>> y.itemsize
1
>>> len(y)
24
>>> y.nbytes
24
```

- 将 1D/unsigned bytes 转换为 1D/char

```py
>>> b = bytearray(b'zyz')
>>> x = memoryview(b)
>>> x[0] = b'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: memoryview: invalid value for format "B"
>>> y = x.cast('c')
>>> y[0] = b'a'
>>> b
bytearray(b'ayz')
```

- 将 1D/bytes 转换为 3D/ints 或 1D/signed char

```py
>>> import struct
>>> buf = struct.pack("i"*12, *list(range(12)))
>>> x = memoryview(buf)
>>> y = x.cast('i', shape=[2,2,3])
>>> y.tolist()
[[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
>>> y.format
'i'
>>> y.itemsize
4
>>> len(y)
2
>>> y.nbytes
48
>>> z = y.cast('b')
>>> z.format
'b'
>>> z.itemsize
1
>>> len(z)
48
>>> z.nbytes
48
```

- 将 1D/unsigned long 转换为 2D/unsigned long

```py
>>> buf = struct.pack("L"*6, *list(range(6)))
>>> x = memoryview(buf)
>>> y = x.cast('L', shape=[2,3])
>>> len(y)
2
>>> y.nbytes
48
>>> y.tolist()
[[0, 1, 2], [3, 4, 5]]
```
