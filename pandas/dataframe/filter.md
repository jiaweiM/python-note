# DataFrame 过滤

过滤和[[select|选择]]，从某种意义上来说是一样的。

## 单个布尔表达式

**例1**，过滤选择 'val' 值大于 0.5 的所有行：

```python
>>> df = pd.DataFrame({
      'name':['Jane','John','Ashley','Mike','Emily','Jack','Catlin'],
      'ctg':['A','A','C','B','B','C','B'],
      'val':np.random.random(7).round(2),
      'val2':np.random.randint(1,10, size=7)
    })
>>> df
     name ctg   val  val2
0    Jane   A  0.57     5
1    John   A  0.04     4
2  Ashley   C  0.69     6
3    Mike   B  0.25     1
4   Emily   B  0.18     5
5    Jack   C  0.72     9
6  Catlin   B  0.35     1
>>> df[df.val > 0.5]
     name ctg   val  val2
0    Jane   A  0.57     5
2  Ashley   C  0.69     6
5    Jack   C  0.72     9
```

**例2**，对字符串使用布尔表达式

```py
>>> df[df.name > 'Jane']
   name ctg   val  val2
1  John   A  0.04     4
3  Mike   B  0.25     1
```

## 组合逻辑运算

运算符 `|` 或 `or`, `&` 或 `and`, `~` 或 `not` 都可用于逻辑运算。

**例1**，执行 与 运算：

```py
>>> df
     name ctg   val  val2
0    Jane   A  0.57     5
1    John   A  0.04     4
2  Ashley   C  0.69     6
3    Mike   B  0.25     1
4   Emily   B  0.18     5
5    Jack   C  0.72     9
6  Catlin   B  0.35     1
>>> df[(df.val > 0.2) & (df.val2 == 1)]
     name ctg   val  val2
3    Mike   B  0.25     1
6  Catlin   B  0.35     1
```

**例2**，执行 或 运算：

```py
>>> df[(df.val < 0.5) | (df.val2 == 1)]
     name ctg   val  val2
1    John   A  0.04     4
3    Mike   B  0.25     1
4   Emily   B  0.18     5
6  Catlin   B  0.35     1
```

## isin

```py
DataFrame.isin(values)
```

用于检查 `DataFrame` 中的元素是否包含在 `values` 中，`values` 支持多种类型：

- `iterable`，包含待检查值的集合
- `Series`，index 要匹配
- `dict`，其 key 必须是 column 名称
- `DataFrame`，index 和 column labels 都要匹配

`isin` 返回一个包含 boolean 值的 `DataFrame`。

**例1**，iterable 参数

```py
>>> df = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]},
                  index=['falcon', 'dog'])
>>> df
        num_legs  num_wings
falcon         2          2
dog            4          0
>>> df.isin([0, 2])
        num_legs  num_wings
falcon      True       True
dog        False       True
```

**例2**，如果 `values` 是 `dict` 类型，则可以对不同列设置不同的检测值：

```py
>>> df
        num_legs  num_wings
falcon         2          2
dog            4          0
>>> df.isin({'num_wings': [0, 3]})
        num_legs  num_wings
falcon     False      False
dog        False       True
```

**例3**，如果 `values` 是 `Series` 或 `DataFrame` 类型，则 index 和 column 都要匹配

```py
>>> df
        num_legs  num_wings
falcon         2          2
dog            4          0
>>> other = pd.DataFrame({'num_legs': [8, 2], 'num_wings': [0, 2]},
                     index=['spider', 'falcon'])
>>> other
        num_legs  num_wings
spider         8          0
falcon         2          2                     
>>> df.isin(other)
        num_legs  num_wings
falcon      True       True
dog        False      False
```

**例4**，将 `isin` 生成的布尔向量传入 `DataFrame` 或 `Series`，就可以过滤数据

```py
>>> s = pd.Series(np.arange(5), index=np.arange(5)[::-1], dtype='int64')
>>> s
4    0
3    1
2    2
1    3
0    4
dtype: int64
>>> s.isin([2, 4, 6])
4    False
3    False
2     True
1    False
0     True
dtype: bool
>>> s[s.isin([2, 4, 6])]
2    2
0    4
dtype: int64
```

## filter

```py
DataFrame.filter(items=None, like=None, regex=None, axis=None)
```

根据指定的索引标签对行或列取子集。

> 该方法不对 DataFrame 的内容进行过滤，而是应用于索引标签。

