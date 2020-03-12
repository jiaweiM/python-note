# Indexing and selecting data

pandas 对象的轴标签（axis labeling）有许多用途：

- 作为数据标签，方便数据分析、可视化和交互。

## Boolean indexing

布尔向量常用来过滤数据。操作符有:

- `|`, `or`
- `&`, `and`
- `~`, `not`

这些操作必须用括号进行分组，因为默认情况下 `df['A'] > 2 & df['B'] < 3` 会按照 `df['A'] > (2 & df['B']) < 3`，而并非预想的 `(df['A > 2) & (df['B'] < 3)`。

使用布尔向量索引 `Series` 和 `ndarray` 完全相同：

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

使用 `map` 方法可以生成更复杂的规则，例如：

```

```