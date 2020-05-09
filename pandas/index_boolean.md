# Boolean indexing

- [Boolean indexing](#boolean-indexing)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [Series boolean 向量索引](#series-boolean-%e5%90%91%e9%87%8f%e7%b4%a2%e5%bc%95)
    - [布尔：或](#%e5%b8%83%e5%b0%94%e6%88%96)
    - [布尔：非](#%e5%b8%83%e5%b0%94%e9%9d%9e)
  - [使用布尔向量选择行](#%e4%bd%bf%e7%94%a8%e5%b8%83%e5%b0%94%e5%90%91%e9%87%8f%e9%80%89%e6%8b%a9%e8%a1%8c)
  - [List 推导和 map](#list-%e6%8e%a8%e5%af%bc%e5%92%8c-map)
    - [map 方法](#map-%e6%96%b9%e6%b3%95)
    - [List 推导](#list-%e6%8e%a8%e5%af%bc)
    - [组合使用](#%e7%bb%84%e5%90%88%e4%bd%bf%e7%94%a8)

2020-04-30, 12:54
*** *

## 简介

布尔向量用于过滤数据。操作符有:

- `|`, `or`
- `&`, `and`
- `~`, `not`

这些操作必须用括号进行分组，因为默认情况下，`df['A'] > 2 & df['B'] < 3` 会按照 `df['A'] > (2 & df['B']) < 3`，而并非预想的 `(df['A > 2) & (df['B'] < 3)`。

## Series boolean 向量索引

使用布尔向量索引 `Series` 和 `ndarray` 完全相同

```py
s = pd.Series(range(-3, 4))
s1 = s[s > 0]
s1
```

out:

```cmd
4    1
5    2
6    3
dtype: int64
```

### 布尔：或

```py
s[(s < -1) | (s > 0.5)]
```

Out:

```cmd
0   -3
1   -2
4    1
5    2
6    3
dtype: int64
```

### 布尔：非

```py
s[~(s < 0)]
```

Out:

```cmd
3    0
4    1
5    2
6    3
dtype: int64
```

## 使用布尔向量选择行

可以使用和 `DataFrame` 索引等长（即和 DataFrame 行数相同）的布尔向量选择 rows，例如，使用 DataFrame 的某一列构建的布尔向量：

```py
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': [7, 8, 9]})
print(df[df.A > 1])
```

Out:

```cmd
   A  B
1  2  8
2  3  9
```

## List 推导和 map

`Series` 的 List 推导 (List comprehensions) 和 `map` 方法可以生成更复杂的规则。

### map 方法

```py
import pandas as pd
import numpy as np

df = pd.DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
                   'b': ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
                   'c': np.random.randn(7)})
```

现在只想要其中的 'two' 和 'three'：

```py
criterion = df['a'].map(lambda x: x.startswith('t'))
df[criterion]
```

Out:

```cmd
       a  b         c
2    two  y -1.103758
3  three  x  0.201518
4    two  y -1.033607
```

### List 推导

用 List 实现相同功能（更慢）

```py
df[[x.startswith('t') for x in df['a']]]
```

Out:

```cmd
       a  b         c
2    two  y -0.545678
3  three  x  1.323958
4    two  y -1.561873
```

- 多重规则

```py
df[criterion & (df['b'] == 'x')]
```

Out:

```cmd
       a  b         c
3  three  x  0.378387
```

### 组合使用

将 boolean vector 和选择方法 `Selection by Label`, `Selection by Position` 以及 `Advanced Indexing` 结合使用，可以实现多 axis 选择。

例如：

```py
df.loc[criterion & (df['b'] == 'x'), 'b': 'c']
```

输出：

```cmd
   b         c
3  x  0.155084
```
