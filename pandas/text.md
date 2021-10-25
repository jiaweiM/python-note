# 文本数据

- [文本数据](#文本数据)
  - [简介](#简介)
  - [文本数据类型](#文本数据类型)
    - [行为差异](#行为差异)
  - [删除空格（strip）](#删除空格strip)
  - [大小写](#大小写)
    - [小写（lower）](#小写lower)
    - [大写（upper）](#大写upper)
    - [首字母大写（capitalize）](#首字母大写capitalize)
    - [标题（title）](#标题title)
    - [大小写互换（swapcase）](#大小写互换swapcase)
  - [切片](#切片)
    - [子字符串（slice）](#子字符串slice)
    - [提取（get）](#提取get)
  - [匹配](#匹配)
    - [包含（contains）](#包含contains)
    - [startswith](#startswith)
    - [endswith](#endswith)
  - [拆分和连接](#拆分和连接)
    - [拆分（split）](#拆分split)
    - [右拆分（rsplit）](#右拆分rsplit)
    - [连接（join）](#连接join)
    - [将一个 Series 转换为一个字符串](#将一个-series-转换为一个字符串)
    - [连接 Series 和 list-like 对象](#连接-series-和-list-like-对象)
    - [连接 Series 和 array-like](#连接-series-和-array-like)
    - [连接 Series 和 index 对象](#连接-series-和-index-对象)
    - [连接 Series 和多个对象](#连接-series-和多个对象)
  - [长度（len）](#长度len)
  - [参考](#参考)
    - [rfind](#rfind)

2021-09-30, 15:25
@author Jiawei Mao
***

## 简介

`Series` 的 `str` 属性内嵌一个 `StringMethods` 对象，是一个功能强大的字符串处理工具。

```py
>>> s = pd.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
>>> s.str
<pandas.core.strings.accessor.StringMethods object at 0x000001958B2084F0>
```

在需要执行字符串操作时，都是通过 `StringMethods` 对象，而不是 `Series`。

## 文本数据类型

在 pandas 中保存字符串的方式有两种：

1. `object` dtype NumPy array
2. `StringDtype` 扩展类型

pandas 推荐使用 `StringDtype` 保存文本数据。

在 pandas 1.0 之前只能使用 `object` dtype，使用该类型有如下缺点：

1. 在 `object` dtype 数组中可能存储字符串和非字符串的混合类型，最好使用专门的 dtype 存储字符串；
2. `object` dtype 会中断特定于 dtype 的操作，如 `DataFrame.select_dtypes()`。在 `object` dtype 列中没有明确只选择文本的方法。
3. `object` dtype 没有 `string` 清晰。

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

对非字符串数据，也可以使用 "string" 类型，它会被转换为 dtype `string`：

```py
In [7]: s = pd.Series(["a", 2, np.nan], dtype="string")

In [8]: s
Out[8]:
0 a
1 2
2 <NA>
dtype: string

In [9]: type(s[1])
Out[9]: str
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



## 删除空格（strip）

```py
Series.str.lstrip(to_strip=None)
Series.str.rstrip(to_strip=None)
Series.str.strip(to_strip=None)
```

说明：

- `lstrip` 删除字符串开头的空格；
- `rstrip` 删除字符串末尾的空格；
- `strip` 则同时删除首尾的空格。

`to_strip` 指定要移除的字符。如果不指定，默认移除空格（包括换行符）。

**例1**，删除首尾空格

```py
>>> s = pd.Series(['1. Ant.  ', '2. Bee!\n', '3. Cat?\t', np.nan])
>>> s
0    1. Ant.  
1    2. Bee!\n
2    3. Cat?\t
3          NaN
dtype: object
>>> s.str.strip()
0    1. Ant.
1    2. Bee!
2    3. Cat?
3        NaN
dtype: object
```

左侧没有空格，删除了右侧的空格 `\n` 以及 `\t` 字符。

**例2**，指定左侧删除的字符

```py
>>> s.str.lstrip('123.')
0     Ant.  
1     Bee!\n
2     Cat?\t
3        NaN
dtype: object
```

**例3**，指定右侧删除的字符

```py
>>> s.str.rstrip('.!? \n\t')
0    1. Ant
1    2. Bee
2    3. Cat
3       NaN
dtype: object
```

**例4**，自定义字符

```py
>>> s.str.strip('123.!? \n\t')
0    Ant
1    Bee
2    Cat
3    NaN
dtype: object
```

## 大小写

### 小写（lower）

```py
Series.str.lower()
```

将字符串转换为小写。

例如：

```py
>>> s = pd.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
>>> s
0                 lower
1              CAPITALS
2    this is a sentence
3              SwApCaSe
dtype: object
>>> s.str.lower()
0                 lower
1              capitals
2    this is a sentence
3              swapcase
dtype: object
```

### 大写（upper）

```py
Series.str.upper()
```

字符串转换为大写。

例如：

```py
>>> s
0                 lower
1              CAPITALS
2    this is a sentence
3              SwApCaSe
dtype: object
>>> s.str.upper()
0                 LOWER
1              CAPITALS
2    THIS IS A SENTENCE
3              SWAPCASE
dtype: object
```

### 首字母大写（capitalize）

```py
Series.str.capitalize()
```

例如：

```py
>>> s
0                 lower
1              CAPITALS
2    this is a sentence
3              SwApCaSe
dtype: object
>>> s.str.capitalize()
0                 Lower
1              Capitals
2    This is a sentence
3              Swapcase
dtype: object
```

### 标题（title）

```py
Series.str.title()
```

`title()` 将每个单词的首字母大写。

例如：

```py
>>> s
0                 lower
1              CAPITALS
2    this is a sentence
3              SwApCaSe
dtype: object
>>> s.str.title()
0                 Lower
1              Capitals
2    This Is A Sentence
3              Swapcase
dtype: object
```

### 大小写互换（swapcase）

```py
Series.str.swapcase()
```

例如：

```py
>>> s
0                 lower
1              CAPITALS
2    this is a sentence
3              SwApCaSe
dtype: object
>>> s.str.swapcase()
0                 LOWER
1              capitals
2    THIS IS A SENTENCE
3              sWaPcAsE
dtype: object
```

## 切片

### 子字符串（slice）

```py
Series.str.slice(start=None, stop=None, step=None)
```

`start` 为起始位置，`stop` 为结束位置，`step` 指定切片跨度。

**例1**，positive 索引

```py
>>> s = pd.Series(["koala", "dog", "chameleon"])
>>> s
0        koala
1          dog
2    chameleon
dtype: object
>>> s.str.slice(start=1)
0        oala
1          og
2    hameleon
dtype: object
```

**例2**，negative 索引

```py
>>> s.str.slice(start=-1)
0    a
1    g
2    n
dtype: object
```

**例3**，指定 stop

```py
>>> s.str.slice(stop=2)
0    ko
1    do
2    ch
dtype: object
```

**例4**，指定 step

```py
>>> s.str.slice(step=2)
0      kaa
1       dg
2    caeen
dtype: object
```

**例5**，指定所有参数

也可以使用 `.str[start:stop:step]` 语法进行切片。

```py
>>> s.str.slice(start=0, stop=5, step=3)
0    kl
1     d
2    cm
dtype: object
>>> s.str[0:5:3]
0    kl
1     d
2    cm
dtype: object
```

### 提取（get）

```py
Series.str.get(i)
```

返回指定位置的元素：

- 对字符串，为字符；
- 对 list, tuple 等，就是对应位置的元素。

**例1**，返回位置1的元素

```py
>>> import pandas as pd
>>> s = pd.Series(["String",
              (1, 2, 3),
              ["a", "b", "c"],
              123,
              -456,
              {1: "Hello", "2": "World"}])
>>> s
0                        String
1                     (1, 2, 3)
2                     [a, b, c]
3                           123
4                          -456
5    {1: 'Hello', '2': 'World'}
dtype: object
>>> s.str.get(1)
0        t
1        2 
2        b
3      NaN
4      NaN
5    Hello
dtype: object
```

**例2**，也可以用 negative 索引

```py
>>> s.str.get(-1)
0       g
1       3
2       c
3     NaN
4     NaN
5    None
dtype: object
```

## 匹配

### 包含（contains）

```py
Series.str.contains(pat, case=True, flags=0, na=None, regex=True)
```

是否包含指定字符串或 pattern。

`pat` 指定字符串或正则表达式。

**例1**，是否包含指定字符串

`regex` 用于指定是否为正则表达式：

- True，表示 `pat` 是正则表达式，默认值；
- False，将 `pat` 以字符串字面量处理。

```py
>>> s1 = pd.Series(['Mouse', 'dog', 'house and parrot', '23', np.NaN])
>>> s1.str.contains('og', regex=False)
0    False
1     True
2    False
3    False
4      NaN
dtype: object
```

### startswith

```py
Series.str.startswith(pat, na=None)
```

是否以指定字符串开头。

`na` 用于指定对 NA 值的处理方式，默认 NaN，即缺失值显示为 NaN。

**例1**，是否以 'b' 开头

```py
>>> s = pd.Series(['bat', 'Bear', 'cat', np.nan])
>>> s
0     bat
1    Bear
2     cat
3     NaN
dtype: object
>>> s.str.startswith('b')
0     True
1    False
2    False
3      NaN
dtype: object
```

**例2**，设置 na 值的显示

```py
>>> s.str.startswith('b', na=False)
0     True
1    False
2    False
3    False
dtype: bool
```

### endswith

```py
Series.str.endswith(pat, na=None)
```

**例1**，测试是否以 't' 结尾

```py
>>> s = pd.Series(['bat', 'bear', 'caT', np.nan])
>>> s
0     bat
1    bear
2     caT
3     NaN
dtype: object
>>> s.str.endswith('t')
0     True
1    False
2    False
3      NaN
dtype: object
```

**例2**，将 na 值用 False 显示

```py
>>> s.str.endswith('t', na=False)
0     True
1    False
2    False
3    False
dtype: bool
```

## 拆分和连接

### 拆分（split）

```py
Series.str.split(pat=None, n=- 1, expand=False)
```

以指定分隔符拆分字符串。

`pat` 用于指定分隔符，支持字符串和正则表达式，默认为空格。

`n` 用于指定拆分出来的个数上限，`None`，0 和 -1 都表示返回所有拆分，默认 -1：

- 如果 splits > n，返回前 n 个；
- 如果 splits <= n，返回所有；
- 如果部分行 splits < n，且设置 `expand=True`，后面填充 None。

`expand` 用于设置返回类型，默认 False：

- True，返回 `DataFrame` 或 `MultiIndex`，即将拆分出来的值作为新的 column；
- False，返回 `Series` 或 `Index`，包含字符串列表，拆分值存入列表。

如果设置 `True`，`Series` 和 `Index` 分别返回 `DataFrame` 和 `MultiIndex`。

**例1**，默认以空格拆分

```py
>>> s = pd.Series(
    [
        "this is a regular sentence",
        "https://docs.python.org/3/tutorial/index.html",
        np.nan
    ]
)
>>> s
0                       this is a regular sentence
1    https://docs.python.org/3/tutorial/index.html
2                                              NaN
dtype: object
>>> s.str.split()
0                   [this, is, a, regular, sentence]
1    [https://docs.python.org/3/tutorial/index.html]
2                                                NaN
dtype: object
```

**例2**，如果不设置 `n`，`split` 和 `rsplit` 效果一样

```py
>>> s.str.rsplit()
0                   [this, is, a, regular, sentence]
1    [https://docs.python.org/3/tutorial/index.html]
2                                                NaN
dtype: object
```

**例3**，`n` 用于限制拆分出来的个数，设置该参数会使 `split` 和 `rsplit` 行为不一致

```py
>>> s.str.split(n=2)
0                     [this, is, a regular sentence]
1    [https://docs.python.org/3/tutorial/index.html]
2                                                NaN
dtype: object
>>> s.str.rsplit(n=2)
0                     [this is a, regular, sentence]
1    [https://docs.python.org/3/tutorial/index.html]
2                                                NaN
dtype: object
```

**例4**，自定义分隔符

```py
>>> s
0                       this is a regular sentence
1    https://docs.python.org/3/tutorial/index.html
2                                              NaN
dtype: object
>>> s.str.split(pat="/")
0                         [this is a regular sentence]
1    [https:, , docs.python.org, 3, tutorial, index...
2                                                  NaN
dtype: object
```

**例5**，当指定 `expand=True`，拆分出来的元素扩展为新的 column，如果存在 NaN值，扩展的 column 也填充 NaN 值

```py
>>> s
0                       this is a regular sentence
1    https://docs.python.org/3/tutorial/index.html
2                                              NaN
dtype: object
>>> s.str.split(expand=True)
                                               0     1     2        3         4
0                                           this    is     a  regular  sentence
1  https://docs.python.org/3/tutorial/index.html  None  None     None      None
2                                            NaN   NaN   NaN      NaN       NaN
```

**例6**，使用正则表达式

```py
>>> s = pd.Series(["1+1=2"])
>>> s
0    1+1=2
dtype: object
>>> s.str.split(r"\+|=", expand=True)
   0  1  2
0  1  1  2
```

### 右拆分（rsplit）

### 连接（join）

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

## 长度（len）

```py
Series.str.len()
```

计算 `Series`/`Index` 中每个元素的长度。返回等长 int 类型的  `Series` 或 `Index`。

这个长度可能是序列（字符串、list、tuple）的长度，也可能是集合（dict）的长度。

例如：

```py
>>> s = pd.Series(['dog',
                '',
                5,
                {'foo' : 'bar'},
                [2, 3, 5, 7],
                ('one', 'two', 'three')])
>>> s
0                  dog
1                     
2                    5
3       {'foo': 'bar'}
4         [2, 3, 5, 7]
5    (one, two, three)
dtype: object
>>> s.str.len()
0    3.0 # 字符串长度
1    0.0 # 字符串长度
2    NaN # 数值，没有长度概念
3    1.0 # dict
4    4.0 # list
5    3.0 # tuple
dtype: float64
```

## 参考

- https://pandas.pydata.org/docs/user_guide/text.html
- https://pandas.pydata.org/docs/reference/series.html

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

