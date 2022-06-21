# Reshaping

## 计算指示/虚拟变量

将分类变量转换为虚拟（dummy）或指示（indicator）`DataFrame`，例如，将 `DataFrame` 中具有 k 个不同值的列，可以使用 `get_dummies()` 生成 `k` 个值为 1 或 0 的列：

```py
>>> df = pd.DataFrame({"key": list("bbacab"), "data1": range(6)})
>>> df
  key  data1
0   b      0
1   b      1
2   a      2
3   c      3
4   a      4
5   b      5
>>> pd.get_dummies(df["key"])
   a  b  c
0  0  1  0
1  0  1  0
2  1  0  0
3  0  0  1
4  1  0  0
5  0  1  0
```

还可以给新生成的 column 名称前添加前缀：

```py
>>> dummies = pd.get_dummies(df["key"], prefix="key")
>>> dummies
   key_a  key_b  key_c
0      0      1      0
1      0      1      0
2      1      0      0
3      0      0      1
4      1      0      0
5      0      1      0
>>> df[["data1"]].join(dummies)
   data1  key_a  key_b  key_c
0      0      0      1      0
1      1      0      1      0
2      2      1      0      0
3      3      0      0      1
4      4      1      0      0
5      5      0      1      0
```

该函数通常与 `cut` 这样的离散化函数一起使用：

```py
>>> values = np.random.randn(10)
>>> values
array([-1.41461325,  0.29662127,  0.77298293,  0.43689857, -0.52881206,
        1.03895367, -0.50879659,  0.29085928,  0.48354226, -1.11607977])
>>> bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
>>> pd.get_dummies(pd.cut(values, bins))
   (0.0, 0.2]  (0.2, 0.4]  (0.4, 0.6]  (0.6, 0.8]  (0.8, 1.0]
0           0           0           0           0           0
1           0           1           0           0           0
2           0           0           0           1           0
3           0           0           1           0           0
4           0           0           0           0           0
5           0           0           0           0           0
6           0           0           0           0           0
7           0           1           0           0           0
8           0           0           1           0           0
9           0           0           0           0           0
```

`get_dummies()` 也可以应用于 `DataFrame`。默认将所有分类变量（统计意义上的分类变量，dtype 为 `object` 或 `categorical`） 编码为 dummy 变量：

```py
>>> df = pd.DataFrame({"A": ["a", "b", "a"], "B": ["c", "c", "b"], "C": [1, 2, 3]})
>>> df
   A  B  C
0  a  c  1
1  b  c  2
2  a  b  3
>>> pd.get_dummies(df)
   C  A_a  A_b  B_b  B_c
0  1    1    0    0    1
1  2    0    1    0    1
2  3    1    0    1    0
```

所有的 non-object columns 原封不动。使用 `columns` 参数可以设置编码的 columns:

```py
>>> pd.get_dummies(df, columns=["A"])
   B  C  A_a  A_b
0  c  1    1    0
1  c  2    0    1
2  b  3    1    0
```

可以看到 `B` 列依然在结果中，只是没有编码。

和 `Series` 版本一样，可以使用 `prefix` 和 `prefix_sep`。默认使用 column 名称作为前缀，`_` 作为前缀分隔符。指定 `prefix` 和 `prefix_sep` 有三种方式：


