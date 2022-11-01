# 基本功能

Last updated: 2022-11-01, 14:10
***

## 迭代

在 pandas 对象上的迭代取决于数据类型：

- 对 `Series`，按照数组进行迭代，迭代生成对应的值
- 对 `DataFrame`，迭代类似于 dict，对 keys 进行迭代。

简而言之，使用 `for i in object` 迭代方式，生成的值为：

- `Series`: values
- `DataFrame`: column labels

因此，对 `DataFrame` 迭代获得 column 名称：

```py
df = pd.DataFrame({"col1": np.random.randn(3), "col2": np.random.randn(3)}, index=["a", "b", "c"])
for col in df:
    print(col)
# col1
# col2
```

pandas 也有类似于字典 `items()` 迭代 (key, value) 对的方法。

可以使用如下方法迭代 `DataFrame` 的行：

- `iterrows()`：以 `(index, Series)` 方式迭代 DataFrame 的行。将行转换为 `Series`，会转换 dtypes，且影响性能。
- `itertuples()`：以命名 tuple 的方式迭代 DataFrame 的行。比 `iterrows()` 快许多，是迭代 DataFrame 值的推荐方式。

迭代 pandas 对象一般**很慢**。而且大多数情况可以使用以下方式避免迭代 rows：

- 向量化方案：许多操作可以使用内置方法或 NumPy 函数实现；
- 如果是函数，无法一次应用于所有 DataFrame/Series，可以使用 `apply()` 函数；
- 如果确实需要迭代，且性能很重要，可以考虑使用 cython 或 numba。

> **Warning:** 迭代时不要修改迭代内容。根据数据类型不同，迭代可能返回 copy 而不是 view，因此写入操作没有效果。
> 例如，在以下情况设置值无效：

```python
In [256]: df = pd.DataFrame({"a": [1, 2, 3], "b": ["a", "b", "c"]})

In [257]: for index, row in df.iterrows():
   .....:     row["a"] = 10
   .....: 

In [258]: df
Out[258]: 
   a  b
0  1  a
1  2  b
2  3  c
```

### items

### iterrows

### itertuples

Last updated: 2022-11-01, 14:22

`itertuples()` 返回一个 iterator，为 `DataFrame` 的每一行生成一个命令 tuple。tuple 的第一个元素是 row 对应的 index 值，其余为对应 row 的值。

例如：

```python
In [272]: for row in df.itertuples():
   .....:     print(row)
   .....: 
Pandas(Index=0, a=1, b='a')
Pandas(Index=1, a=2, b='b')
Pandas(Index=2, a=3, b='c')
```

此方法不讲 row 转换为 Series 对象，仅仅以 namedtuple 返回值，因此保留值的类型，通常比 `iterrows()` 快。

> **Note:** 如果 column 名称是无效的 Python 标识符、重复或以下划线开头，则 column 名被重命名为位置名。如果包含大量 column (>255)，则返回常规 tuple，而非 namedtule。

## 参考

- https://pandas.pydata.org/docs/user_guide/basics.html
