# Selection by position

- [Selection by position](#selection-by-position)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [整数索引](#%e6%95%b4%e6%95%b0%e7%b4%a2%e5%bc%95)
    - [Series 索引](#series-%e7%b4%a2%e5%bc%95)
    - [DataFrame 索引](#dataframe-%e7%b4%a2%e5%bc%95)
      - [双值索引](#%e5%8f%8c%e5%80%bc%e7%b4%a2%e5%bc%95)
      - [单值索引](#%e5%8d%95%e5%80%bc%e7%b4%a2%e5%bc%95)
  - [索引列表](#%e7%b4%a2%e5%bc%95%e5%88%97%e8%a1%a8)
    - [Series 索引列表](#series-%e7%b4%a2%e5%bc%95%e5%88%97%e8%a1%a8)
    - [DataFrame 索引列表](#dataframe-%e7%b4%a2%e5%bc%95%e5%88%97%e8%a1%a8)
  - [切片](#%e5%88%87%e7%89%87)
    - [Series 切片](#series-%e5%88%87%e7%89%87)
    - [DataFrame 切片](#dataframe-%e5%88%87%e7%89%87)
    - [越界切片](#%e8%b6%8a%e7%95%8c%e5%88%87%e7%89%87)
      - [Series 越界切片](#series-%e8%b6%8a%e7%95%8c%e5%88%87%e7%89%87)
      - [DataFrame 越界切片](#dataframe-%e8%b6%8a%e7%95%8c%e5%88%87%e7%89%87)
  - [设置值](#%e8%ae%be%e7%bd%ae%e5%80%bc)

***

## 简介

> 对一个设置操作，返回副本还是引用取决于上下文。

pandas 提供了一组基于索引操作的方法。其语法严格遵循 Python 和 NumPy 切片语法。

- 索引以 0 开始。
- 进行切片时，包括起始索引，排除结束索引。
- 使用非整数索引，抛出 `IndexError`。

`.iloc` 主要基于整数位置（0 到 length-1），但也能和布尔数组一起使用。

索引超出范围，`.iloc` 抛出 `IndexError`，但是在切片时允许索引越界，这和 Python 及 NumPy 切片一致。

`.iloc` 属性是基于索引访问的主要方法，有效输入包括：

- 整数索引，如 `5`
- 整数列表或数组，如 `[4, 3, 0]`
- slice 对象，如 `1 : 7`
- boolean 数组
- `callable` 对象，包含单个参数（调用该方法的 `Series` 或 `DataFrame`）的 `callable` 函数，该函数返回上面索引形式的一种。

## 整数索引

### Series 索引

```py
s1 = pd.Series([3, 5, 1])
assert s1.iloc[0] == 3
assert s1.iloc[2] == 1
```

### DataFrame 索引

#### 双值索引

提供两个索引获得单个值，等价于 `df.iat[1, 1]`

```py
df = pd.DataFrame({"col1": [1, 2],
                    "col2": [3, 4]},
                  index=["row1", "row2"])
assert df.iloc[1, 1] == 4
assert df.iloc[0, 1] == 3
```

#### 单值索引

如果只提供一个索引，表示行。

获取的行，以 `Series` 对象返回。

```py
df = pd.DataFrame({"col1": [1, 2],
                    "col2": [3, 4]},
                  index=["row1", "row2"])
s1 = df.iloc[1] # 第二行
assert_series_equal(s1, pd.Series(
    [2, 4], name="row2", index=['col1', 'col2']))
```

## 索引列表

### Series 索引列表

```py
s1 = pd.Series([1, 2, 3, 4])
s2 = s1.iloc[[1, 3]]
assert_array_equal(s2, np.array([2, 4]))
```

### DataFrame 索引列表

```py
df = pd.DataFrame({"col1": [1, 2, 3],
                    "col2": [4, 5, 6],
                    "col3": [7, 8, 9]},
                  index=["row1", "row2", "row3"])
df1 = df.iloc[[0, 2], [1, 2]]
assert_frame_equal(df1, pd.DataFrame(
    {"col2": [4, 6],
      "col3": [7, 9]},
    index=["row1", "row3"]
))
```

`iloc[[0, 2], [1, 2]]` 选择了第一行和第二行，第二列和第三列。

## 切片

### Series 切片

```py
s1 = pd.Series([1, 3, 5, 7, 11])
s2 = s1.iloc[:3]
pd.testing.assert_series_equal(s2, pd.Series([1, 3, 5]))
```

### DataFrame 切片

```py
df = pd.DataFrame({"col1": [1, 2, 3],
                    "col2": [4, 5, 6],
                    "col3": [7, 8, 9]},
                    index=["row1", "row2", "row3"])
```

选择前两行：

```py
df2 = df.iloc[:2] # 前两行
assert_frame_equal(df2, pd.DataFrame({
    "col1": [1, 2], "col2": [4, 5], "col3": [7, 8],
    index=["row1", "row2"]}))
```

选择二三行，二三列：

```py
df3 = df.iloc[1:3, 1:3]
assert_frame_equal(df3, pd.DataFrame({
    "col2": [4, 5], "col3": [7, 8],
    index=['row2', 'row3']
}))
```

### 越界切片

> 越界只在切片中允许，对索引或索引列表中，越界抛出 `IndexError`

#### Series 越界切片

在 Python/Numpy 中切片索引允许越界，例如：

```py
In [71]: x = list('abcdef')

In [72]: x
Out[72]: ['a', 'b', 'c', 'd', 'e', 'f']

In [73]: x[4:10]
Out[73]: ['e', 'f']

In [74]: x[8:10]
Out[74]: []
```

越界的索引被忽略。

在 pandas 中对越界切片的处理方法相同：

```py
In [75]: s = pd.Series(x)

In [76]: s
Out[76]:
0    a
1    b
2    c
3    d
4    e
5    f
dtype: object

In [77]: s.iloc[4:10] # 索引部分越界，从起始到 Series 末尾
Out[77]:
4    e
5    f
dtype: object

In [78]: s.iloc[8:10] # 索引完全越界，返回空 Series
Out[78]: Series([], dtype: object)
```

#### DataFrame 越界切片

DataFrame 处理方式一样，完全越界返回空的 DataFrame，部分越界则到对应 axis 末尾。

```py
In [79]: dfl = pd.DataFrame(np.random.randn(5, 2), columns=list('AB'))

In [80]: dfl
Out[80]:
          A         B
0 -0.082240 -2.182937
1  0.380396  0.084844
2  0.432390  1.519970
3 -0.493662  0.600178
4  0.274230  0.132885

In [81]: dfl.iloc[:, 2:3] # 完全越界，返回空 DataFrame
Out[81]:
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 4]

In [82]: dfl.iloc[:, 1:3] # 部分越界，从第2列到最后一列，不过这里最大直到第2列
Out[82]:
          B
0 -2.182937
1  0.084844
2  1.519970
3  0.600178
4  0.132885

In [83]: dfl.iloc[4:6] # 4 到 5 行，由于最大行索引为4，所以只有第4行
Out[83]:
         A         B
4  0.27423  0.132885
```

## 设置值

`iloc` 语法也可用来设置值。

```py
s1 = pd.Series([1, 2, 3])
s1.iloc[:2] = 0
pd.testing.assert_series_equal(s1, pd.Series([0, 0, 3]))
```
