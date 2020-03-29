# Working with text data

- [Working with text data](#working-with-text-data)
  - [Text 数据类型](#text-%e6%95%b0%e6%8d%ae%e7%b1%bb%e5%9e%8b)
    - [行为差异](#%e8%a1%8c%e4%b8%ba%e5%b7%ae%e5%bc%82)
  - [提取子字符串](#%e6%8f%90%e5%8f%96%e5%ad%90%e5%ad%97%e7%ac%a6%e4%b8%b2)
  - [Concatenation](#concatenation)
    - [将一个 Series 转换为一个字符串](#%e5%b0%86%e4%b8%80%e4%b8%aa-series-%e8%bd%ac%e6%8d%a2%e4%b8%ba%e4%b8%80%e4%b8%aa%e5%ad%97%e7%ac%a6%e4%b8%b2)
    - [连接 Series 和 list-like 对象](#%e8%bf%9e%e6%8e%a5-series-%e5%92%8c-list-like-%e5%af%b9%e8%b1%a1)
    - [连接 Series 和 array-like](#%e8%bf%9e%e6%8e%a5-series-%e5%92%8c-array-like)
    - [连接 Series 和 index 对象](#%e8%bf%9e%e6%8e%a5-series-%e5%92%8c-index-%e5%af%b9%e8%b1%a1)
    - [连接 Series 和多个对象](#%e8%bf%9e%e6%8e%a5-series-%e5%92%8c%e5%a4%9a%e4%b8%aa%e5%af%b9%e8%b1%a1)
  - [子字符串](#%e5%ad%90%e5%ad%97%e7%ac%a6%e4%b8%b2)
  - [参考](#%e5%8f%82%e8%80%83)
    - [rfind](#rfind)

***

## Text 数据类型

在 pandas 中保存字符串的方式有两种：

1. `object` dtype NumPy array
2. `StringDtype` 扩展类型

pandas 推荐使用 `StringDtype` 保存文本数据。

在 pandas 1.0 之前只能使用 `object` dtype，使用该类型的缺点：

- 在 `object` dtype 数组中可能存储混合类型
- `object` dtype 会中断特定于 dtype 的操作，如 `DataFrame.select_dtypes()`。在 `object` dtype 列中没有明确只选择文本的犯法。
- `object` dtype 没有 `string` 清晰。

目前使用 `object` dtype 数组和 `arrays.StingArray` 性能差不多。

> `StringArray` 还在测试阶段

为了向后兼容，`object` 依然是字符串列表的默认推断类型。

```py
>>> pd.Series(['a', 'b', 'c'])
0    a
1    b
2    c
dtype: object
```

可以通过指定 `dtype` 设置 `string` 类型:

```py
>>> pd.Series(['a', 'b', 'c'], dtype="string")
0    a
1    b
2    c
dtype: string

>>> pd.Series(['a', 'b', 'c'], dtype=pd.StringDtype())
0    a
1    b
2    c
dtype: string
```

或者在创建后使用 `astype` 修改类型：

```py
>>> s = pd.Series(['a', 'b', 'c'])
>>> s
0    a
1    b
2    c
dtype: object

>>> s.astype("string")
0    a
1    b
2    c
dtype: string
```

### 行为差异

在以下方面 `StringDtype` 和 `object` 不同。

1. 对 `StringDtype`，返回数值的 `string accessor` 方法返回整数，而不像 `object` 在有 NA 值时返回 float，没有时返回 int。而返回 boolean 值的方法返回 nullable boolean.

```py
>>> s = pd.Series(["a", None, "b"], dtype="string")
>>> s
0       a
1    <NA>
2       b
dtype: string

>>> s.str.count("a")
0       1
1    <NA>
2       0
dtype: Int64

>>> s.dropna().str.count("a")
0    1
2    0
dtype: Int64
```

可以看到返回类型都是 `Int64`，下面是 `object` dtype 的情况：

```py
>>> s2 = pd.Series(["a", None, "b"], dtype="object")
>>> s2.str.count("a")
0    1.0
1    NaN
2    0.0
dtype: float64

>>> s2.dropna().str.count("a")
0    1
2    0
dtype: int64
```

在有 NA 值时，输出的是 `float64` 类型。返回 boolean 值的情况类似：

```py
>>> s.str.isdigit()
0    False
1     <NA>
2    False
dtype: boolean

>>> s.str.match("a")
0     True
1     <NA>
2    False
dtype: boolean
```

2. 部分字符串方法，如 `Series.str.decode()` 在 `StringArray` 中不可用，因为 `StringArray` 只保存字符串。

3. 在对其操作中，`arrays.StringArray` 以及 `StringArray` 类型的 `Series`，返回`BooleanDtype`，而不是 `bool` dtype。

余下所有部分，`string` 和 `object` 行为相同。 

## 提取子字符串


## Concatenation

串联 `Series` 或 `Index` 的方法有多种，但是都是基于 `cat()` 方法。

### 将一个 Series 转换为一个字符串

将整个 `Series` 或 `Index` 串联为一个字符串：

```py
>>> s = pd.Series(['a', 'b', 'c', 'd'], dtype="string")

>>> s.str.cat(sep=',')
'a,b,c,d'
```

如果不指定 `sep`，其默认为空字符串：

```py
>>> s.str.cat()
'abcd'
```

缺失值默认忽略，使用 `na_rep` 可用其它替代缺失值：

```py
>>> t = pd.Series(['a', 'b', np.nan, 'd'], dtype="string")

>>> t.str.cat(sep=',')
'a,b,d'

>>> t.str.cat(sep=',', na_rep='-')
'a,b,-,d'
```

### 连接 Series 和 list-like 对象

`cat()` 方法的第一个参数可以是 list-like 对象，其长度需要和调用的 `Series` 或 `Index` 相同，`Series` 和 list-like 元素逐个合并：

```py
>>> s.str.cat(['A', 'B', 'C', 'D'])
0    aA
1    bB
2    cC
3    dD
dtype: string
```

任意一侧出现确实值，结果为缺失值，除非用 `na_rep` 指定：

```py
>>> s = pd.Series(['a', 'b', 'c', 'd'], dtype="string")
>>> t = pd.Series(['a', 'b', np.nan, 'd'], dtype="string")
>>> s.str.cat(t)
0      aa
1      bb
2    <NA>
3      dd
dtype: string

>>> s.str.cat(t, na_rep='-')
0    aa
1    bb
2    c-
3    dd
dtype: string
```

### 连接 Series 和 array-like

参数 `others` 可以为二维，此时 rows 数目要和调用的 `Series` 或 `Index` 相同。

```py
>>> d = pd.concat([t, s], axis=1)
>>> s
0    a
1    b
2    c
3    d
dtype: string

>>> d
      0  1
0     a  a
1     b  b
2  <NA>  c
3     d  d

>>> s.str.cat(d, na_rep='-')
0    aaa
1    bbb
2    c-c
3    ddd
dtype: string
```

### 连接 Series 和 index 对象

对 `Series` 和 `DataFrame`，通过设置 `join` 参数可以在连接前对齐索引。

```py
>>> u = pd.Series(['b', 'd', 'a', 'c'], index=[1, 3, 0, 2], dtype="string")
>>> s
0    a
1    b
2    c
3    d
dtype: string
>>> u
1    b
3    d
0    a
2    c
dtype: string

>>> s.str.cat(u)
0    aa
1    bb
2    cc
3    dd
dtype: string

>>> s.str.cat(u, join='left')
0    aa
1    bb
2    cc
3    dd
dtype: string
```

> 如果不指定 `join` 参数，`cat()` 行为和 0.23.0 之前相同，但是如果有索引不同，会抛出 `FutureWarning`，因为未来默认行为会改为 `join='left'`

`join` 选项（"left", "outer", "inner", "right"）。有了对其选项，长度不同也能合并：

- left, 和左边的对象对其
- outer, 并集模式合并
- inner，交集模式合并

```py
>>> v = pd.Series(['z', 'a', 'b', 'd', 'e'], index=[-1, 0, 1, 3, 4],
   ....:               dtype="string")

>>> s
0    a
1    b
2    c
3    d
dtype: string

>>> v
-1    z
 0    a
 1    b
 3    d
 4    e
dtype: string

>>> s.str.cat(v, join='left', na_rep='-')
0    aa
1    bb
2    c-
3    dd
dtype: string

>>> s.str.cat(v, join='outer', na_rep='-')
-1    -z
 0    aa
 1    bb
 2    c-
 3    dd
 4    -e
dtype: string
```

`others` 为 `DataFrame` 也能对其。

```py
>>> f = d.loc[[3, 2, 1, 0], :]

>>> s
0    a
1    b
2    c
3    d
dtype: string

>>> f
      0  1
3     d  d
2  <NA>  c
1     b  b
0     a  a

>>> s.str.cat(f, join='left', na_rep='-')
0    aaa
1    bbb
2    c-c
3    ddd
dtype: string
```

### 连接 Series 和多个对象

多个 array-like 对象（`Series`, `Index`, 1D `np.ndarray`）可以合并为一个 list，然后进行连接。

```py
>>> s
0    a
1    b
2    c
3    d
dtype: string

>>> u
1    b
3    d
0    a
2    c
dtype: string

>>> s.str.cat([u, u.to_numpy()], join='left')
0    aab
1    bbd
2    cca
3    ddc
dtype: string
```

不包含索引的元素（如 `np.ndarray`）必须和调用的 `Series` 或 `Index` 长度相同，`Series` 和 `Index` 则可以采用任意前度（前提是没有 `join=None` 禁用对齐）。

```py
>>> v
-1    z
 0    a
 1    b
 3    d
 4    e
dtype: string

>>> s.str.cat([v, u, u.to_numpy()], join='outer', na_rep='-')
-1    -z--
 0    aaab
 1    bbbd
 2    c-ca
 3    dddc
 4    -e--
dtype: string
```

## 子字符串

## 参考

### rfind

`Series.str.rfind(self, sub, start=0, end=None)`

返回子字符串出现的最高索引。如果无匹配，返回 -1.等价于 `str.rfind()`

- sub: str

待搜索的子字符串。

- start: int

左边位置

- end: int

右边位置。

返回： 包含 int 的 `Series` 或 `Index`。

