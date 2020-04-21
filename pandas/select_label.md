# Selection by label

- [Selection by label](#selection-by-label)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [Slicing with labels](#slicing-with-labels)
  - [运行检查](#%e8%bf%90%e8%a1%8c%e6%a3%80%e6%9f%a5)

2020-04-21, 14:41
*** *

## 简介

使用 `.loc` 进行选择，如果对应的标签不存在，抛出 `KeyError`。

通过 `.loc` 切片，返回的结果包含起始和结尾的元素。

`.loc` 的有效输入：

- 单个标签，如 `5` 或 `'a'`（此处 `5` 按照标签解析，而非索引）
- 标签数组或列表，如 `['a', 'b', 'c']`
- 切片标签，如 `'a':'f'`（包含首尾元素）
- boolean 数组
- `callable`

例如，对 `Series`:

- `s1.loc['c':]`, 选择 `Series` 'c' 及其后所有数据
- `s1.loc['b']`, 选择标签为 'b' 的单个数据
- `s1.loc['c':] = 0` 设置 'c' 及其后所有数据为 0

对 `DataFrame`:

- `df1.loc[['a', 'b', 'd'], :]`, 选择 'a', 'b', 'd' 行，所有列
- `df1.loc['d':, 'A':'C']`，选择 'd' 行，'A' 到 'C' 列。
- `df1.loc['a']`，选择 'a' 行，等价于 `df.xs('a')`
- `df1.loc[:, df1.loc['a'] > 0]`，选择 'a' 行值大于 0 的所有列。
- `df1.loc['a', 'A']` 选择 'a' 行 'A' 列处的值，等价于 `df1.at['a', 'A']`

## Slicing with labels

使用 `.loc` 进行切片时，包含首尾元素。例如：

```py
In [52]: s = pd.Series(list('abcde'), index=[0, 3, 2, 5, 4])

In [53]: s.loc[3:5] # 此处 3 和 5 都是标签
Out[53]:
3    b
2    c
5    d
dtype: object
```

如果首尾 index 至少有一个越界，但是 index 排序过，并且可以和首尾的 label 对比，则切片依然可以执行：

```py
In [54]: s.sort_index()
Out[54]:
0    a
2    c
3    b
4    e
5    d
dtype: object

In [55]: s.sort_index().loc[1:6]
Out[55]:
2    c
3    b
4    e
5    d
dtype: object
```

如果 index 没有排序，抛出错误。

## 运行检查

对不兼容的 index 类型，`.loc` 会抛出 `TypeError`。例如：

```py
In [35]: dfl = pd.DataFrame(np.random.randn(5, 4),
   ....:                    columns=list('ABCD'),
   ....:                    index=pd.date_range('20130101', periods=5))
   ....:

In [36]: dfl
Out[36]:
                   A         B         C         D
2013-01-01  1.075770 -0.109050  1.643563 -1.469388
2013-01-02  0.357021 -0.674600 -1.776904 -0.968914
2013-01-03 -1.294524  0.413738  0.276662 -0.472035
2013-01-04 -0.013960 -0.362543 -0.006154 -0.923061
2013-01-05  0.895717  0.805244 -1.206412  2.565646
```

```py
In [4]: dfl.loc[2:3]
TypeError: cannot do slice indexing on <class 'pandas.tseries.index.DatetimeIndex'> with these indexers [2] of <type 'int'>
```

对字符串类型切片，如果可以转换为对应 index 类型，则可以正常工作：

```py
In [37]: dfl.loc['20130102':'20130104']
Out[37]:
                   A         B         C         D
2013-01-02  0.357021 -0.674600 -1.776904 -0.968914
2013-01-03 -1.294524  0.413738  0.276662 -0.472035
2013-01-04 -0.013960 -0.362543 -0.006154 -0.923061
```
