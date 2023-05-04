# DataFrame 排序

2023-05-04
***

## 简介

pandas 支持三种类型的排序：

- index label 排序
- column 值排序
- 以上两者组合排序

## 按索引排序（sort_index）

[Series.sort_index()](../api/Series/Series.sort_index.md)

```python
DataFrame.sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, ignore_index=False, key=None)
```

如果 `inplace=False`，返回根据指定 label 排序后的新的 `DataFrame`，否则更新原 `DataFrame`，返回 `None`。

`axis` 用于指定排序的轴：

- 0 或 'index' 表示行，默认值；
- 1 或 'columns' 表示列。

**例1**，默认按照 index 排序：

```py
>>> df = pd.DataFrame([1, 2, 3, 4, 5], index=[100, 29, 234, 1, 150],
                  columns=['A'])
>>> df
     A
100  1
29   2
234  3
1    4
150  5
>>> df.sort_index()
     A
1    4
29   2
100  1
150  5
234  3
```

**例2**，降序排序

`ascending` 参数用于指定是否升序：

- bool 值，对单值排序，默认 True；
- bool list，对多值排序，对 MultiIndex 分别指定排序规则。

```py
>>> df.sort_index(ascending=False)
     A
234  3
150  5
100  1
29   2
1    4
```

**例3**，应用函数

`key` 参数用于指定应用到索引值的函数。

```py
>>> df = pd.DataFrame({"a": [1, 2, 3, 4]}, index=['A', 'b', 'C', 'd'])
>>> df.sort_index(key=lambda x: x.str.lower())
   a
A  1
b  2
C  3
d  4
```

## 按值排序（sort_values）

```py
DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
```

按指定 `axis` 对值进行排序。

`by` 参数用于指定排序的参考值，str 或 str list：

- 如果 `axis` 为 0 或 'index'，则 `by` 包含 index level 和 column labels；
- 如果 `axis` 为 1 或 'collumns'，则 `by` 包含 column levevls 和 index labels。

**例1**，按 'col1' 排序：

```py
>>> df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
    })
>>> df
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
>>> df.sort_values(by=['col1'])
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D
```

**例2**，按多列排序：

使用 `by` 可以指定 columns 名称列表，从而按多列排序。

```py
>>> df.sort_values(by=['col1', 'col2'])
  col1  col2  col3 col4
1    A     1     1    B
0    A     2     0    a
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D
```

**例3**，降序排序：

`ascending` 参数用于指定是否升序：

- bool，单值排序，默认 True；
- list of bool，针对多值排序，此时 ascending 列表长度和 by 一致。

```py
>>> df.sort_values(by='col1', ascending=False)
  col1  col2  col3 col4
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B
3  NaN     8     4    D
```

对 'col1' 升序，对 'col2' 降序：

```py
>>> df.sort_values(by=['col1', 'col2'], ascending=[True, False])
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D
```

**例4**，指定 NA 值得位置

使用 `na_position` 参数可以指定 NA 值的位置：

- 'first'，将 NA 值放在开头；
- 'last'，将 NA 值放在末尾，默认值。

```py
>>> df.sort_values(by='col1', ascending=False, na_position='first')
  col1  col2  col3 col4
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B
```

**例5**，在排序前对值应用函数

`key` 参数用于指定应用的函数，该 `key` 函数必须是向量化的，即参数和返回值都是 `Series` 类型，且长度相同。

```py
>>> df.sort_values(by='col4', key=lambda col: col.str.lower())
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
```

## 参考

- https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#sorting
- 