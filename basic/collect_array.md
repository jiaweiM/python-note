# array.array

## 简介

数组（`array.array`）用于紧凑地存储基本类型，包括字符、整数和浮点数，效率比 `list` 高。数组支持所有跟可变序列有关的操作，包括 `.pop`、`.insert` 和 `.extend` 等。另外，数组还提供从文件读取和存入文件的更快的方法，如 `.frombytes` 和 `.tofile`。

数组支持的对象类型有限，类型代码以单个字符指定，如下所示：

|类型代码|C 类型|Python 类型|最小字节数|
|---|---|---|---|
|`'b'`|signed char|int|1|
|`'B'`|unsigned char|int|1|
|`'u'`|wchar_t|Unicode character|2|
|`'h'`|signed short|int|2|
|`'H'`|unsigned short|int|2|
|`'i'`|signed int|int|2|
|`'I'`|unsigned int|int|2|
|`'l'`|signed long|int|4|
|`'L'`|unsigned long|int|4|
|`'q'`|signed long long|int|8|
|`'Q'`|unsigned long long|int|8|
|`'f'`|float|float|4|
|`'d'`|double|float|8|

类型码用于指定在底层 C  语言应该存放怎样的数据类型。

## 创建数组

```py
array.array(typecode[, initializer])
```

这里必须指定 `typecode` 类型码，后面为可选的初始化器。初始化器可以是任意可迭代对象类型。

如果 `initializer` 为 `list` 或字符串，则内部使用 `fromlist()`、`frombytes()`或 `fromunicode()` 方法初始化数组。对其他可迭代对象，则使用 `extend()` 方法初始化。

例如：

```py

```

## 参考

- https://docs.python.org/3/library/array.html
