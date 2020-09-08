# Boolean indexing

- [Boolean indexing](#boolean-indexing)
  - [简介](#简介)
  - [Series 布尔向量索引](#series-布尔向量索引)
    - [或](#或)
    - [非](#非)
  - [使用布尔向量选择行](#使用布尔向量选择行)
  - [List 推导和 map](#list-推导和-map)
    - [map 方法](#map-方法)
    - [List 推导](#list-推导)
    - [组合使用](#组合使用)

2020-04-30, 12:54
*** *

## 简介

布尔向量可用于过滤数据。

| 操作符 | 对应关键字 |
| ------ | ---------- |
| `|`    | or         |
| `&`    | and        |
| `~`    | not        |

这些操作需要用括号进行分组，因为默认情况下，`df['A'] > 2 & df['B'] < 3` 会按照 `df['A'] > (2 & df['B']) < 3`，而并非 `(df['A > 2) & (df['B'] < 3)`。

## Series 布尔向量索引

使用布尔向量索引 `Series` 和 `ndarray` 完全相同

```py
s = pd.Series(range(-3, 4))
s1 = s[s > 0]

np.testing.assert_array_equal(s1.values, np.array([1, 2, 3]))
```

### 或

```py
s = pd.Series(range(-3, 4))

s2 = s[(s < -1) | (s > 0.5)]
np.testing.assert_array_equal(s2.values, np.array([-3, -2, 1, 2, 3]))
```

### 非

```py
s = pd.Series(range(-3, 4))

s3 = s[~(s < 0)]
np.testing.assert_array_equal(s3.values, np.array([0, 1, 2, 3]))
```

## 使用布尔向量选择行

可以使用和 `DataFrame` 索引等长（即和 DataFrame 行数相同）的布尔向量选择 rows，例如，使用 DataFrame 的某一列构建的布尔向量：

```py
df = pd.DataFrame({'A': [1, 2, 3], 'B': [7, 8, 9]})
df1 = df[df['A'] > 1]
np.array_equal(df1.values, pd.DataFrame({"A": [2, 3], "B": [8, 9]}).values)
```

## List 推导和 map

`Series` 的 List 推导 (List comprehensions) 和 `map` 方法可以生成更复杂的规则。

### map 方法

```py
df = pd.DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
                     'b': ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
                     'c': [1, 2, 3, 4, 5, 6, 7]})
criterion = df['a'].map(lambda x: x.startswith('t')) # 只保留 a 中以 't' 开头的行
df1 = df[criterion]
assert_frame_equal(df1.reset_index(drop=True),
                     pd.DataFrame({'a': ['two', 'three', 'two'],
                                   'b': ['y', 'x', 'y'],
                                   'c': [3, 4, 5]}))
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
