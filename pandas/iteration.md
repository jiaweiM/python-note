# Iteration

- [Iteration](#iteration)
  - [简介](#%e7%ae%80%e4%bb%8b)

2020-04-20, 21:53
***

## 简介

在 pandas 对象上的迭代取决于数据类型：

- 对 `Series`，按照数组进行迭代，迭代生成对应的值
- 对 `DataFrame`，迭代类似于 dict，对 keys 进行迭代。

简而言之，使用 `for i in object` 迭代方式，生成的值为：

- `Series`: values
- `DataFrame`: column labels

因此，对 `DataFrame` 迭代获得 column 名称：

```py
In [250]: df = pd.DataFrame({'col1': np.random.randn(3),
   .....:                    'col2': np.random.randn(3)}, index=['a', 'b', 'c'])
   .....:

In [251]: for col in df:
   .....:     print(col)
   .....:
col1
col2
```

要迭代 `DataFrame` 的行，使用如下方式：

- `iterrows()`：以 `(index, Series)` 方式迭代 DataFrame 的行。将行转换为 `Series`，会转换 dtypes，且影响性能。
- `itertuples()`：以命名 tuple 的方式迭代 DataFrame 的行。比 `iterrows()` 快许多，是迭代 DataFrame 值的推荐方式。

迭代 pandas 对象一般**很慢**。而且大多数情况可以使用以下方式避免迭代 rows：

- 向量化方案：许多操作可以使用内置的方法或 NumPy 函数实现。
- 如果是函数，无法一次应用于所有 DataFrame/Series，可以使用 `apply()` 函数
- 如果确实需要迭代，可以考虑使用 cython 或 numba。

