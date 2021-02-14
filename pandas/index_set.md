# Set/reset index

- [Set/reset index](#setreset-index)
  - [简介](#简介)
  - [设置 index](#设置-index)
  - [Reset the index](#reset-the-index)
  - [添加临时索引](#添加临时索引)

***

## 简介

有时候希望在创建 `DataFrame` 之后再添加 index。pandas 提供了多种方式。

## 设置 index

`DataFrame` 的 `set_index()` 方法使用 column 名称（用于常规 `Index`） 或 column 名称列表（`MultiIndex`）设置索引。

创建新的重新索引 DataFrame:

```py
>>> data
     a    b  c    d
0  bar  one  z  1.0
1  bar  two  y  2.0
2  foo  one  x  3.0
3  foo  two  w  4.0

>>> indexed1 = data.set_index('c') # 将 c 列设置为 index
>>> indexed1
     a    b    d
c
z  bar  one  1.0
y  bar  two  2.0
x  foo  one  3.0
w  foo  two  4.0

>>> indexed2 = data.set_index(['a', 'b']) # 将 a, b 列设置为 index
>>> indexed2
         c    d
a   b
bar one  z  1.0
    two  y  2.0
foo one  x  3.0
    two  w  4.0
```

使用 `append` 关键字参数可以保留之前的 index，将新的 column 添加到 MultiIndex:

```py
>>> frame = data.set_index('c', drop=False)
>>> frame = frame.set_index(['a', 'b'], append=True)
>>> frame
           c    d
c a   b
z bar one  z  1.0
y bar two  y  2.0
x foo one  x  3.0
w foo two  w  4.0
```

而 `drop` 表示是否保留设置为 index 的列，`inplace` 表示是否创建新的对象：

```py
>>> data.set_index('c', drop=False) # 保留 c 列
     a    b  c    d
c
z  bar  one  z  1.0
y  bar  two  y  2.0
x  foo  one  x  3.0
w  foo  two  w  4.0

>>> data.set_index(['a', 'b'], inplace=True)
>>> data
         c    d
a   b
bar one  z  1.0
    two  y  2.0
foo one  x  3.0
    two  w  4.0
```

## Reset the index

为了方便，`DataFrame` 添加了 `reset_index()` 函数，该函数将 index 值添加为新的列，然后添加简单的整数 index。该操作可以看做 `set_index()` 函数的逆操作。

```py
>>> data
         c    d
a   b
bar one  z  1.0
    two  y  2.0
foo one  x  3.0
    two  w  4.0

>>> data.reset_index()
     a    b  c    d
0  bar  one  z  1.0
1  bar  two  y  2.0
2  foo  one  x  3.0
3  foo  two  w  4.0
```

输出和 SQL 表格类似，从 index 派生的列的名称保存在 `names` 属性中。

使用 `level` 关键字可以只移除部分 index:

```py
>>> frame
           c    d
c a   b
z bar one  z  1.0
y bar two  y  2.0
x foo one  x  3.0
w foo two  w  4.0

>>> frame.reset_index(level=1) # 只移除第二个索引
         a  c    d
c b
z one  bar  z  1.0
y two  bar  y  2.0
x one  foo  x  3.0
w two  foo  w  4.0
```

`reset_index` 的可选参数 `drop` 如果设置为 true，则直接舍弃 index，而不添加到 `DataFrame` columns 中。

## 添加临时索引

如果自己创建索引，可以直接赋值给 `index` 字段：

```py
data.index = index
```
