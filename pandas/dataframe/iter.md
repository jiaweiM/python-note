# DataFrame 迭代

- [DataFrame 迭代](#dataframe-迭代)
  - [iterrows](#iterrows)
  - [itertuples](#itertuples)

***

## iterrows

```py
DataFrame.iterrows()
```

以 `(index, Series)` 形式迭代 `DataFrame` 行。

|返回值|类型|说明|
|---|---|---|
|`index`|标签或标签 tuple|行的index，对 MultiIndex 为 tuple|
|`data`|`Series`|以 `Series` 的形式返回行|

由于 `iterrows` 以 `Series` 的形式返回行，所以不保存 `dtype`。例如：

```py
>>> df = pd.DataFrame([[1, 1.5]], columns=['int', 'float'])
>>> row = next(df.iterrows())[1]
>>> row
int      1.0
float    1.5
Name: 0, dtype: float64
>>> print(row['int'].dtype)
float64
>>> print(df['int'].dtype)
int64
```

要保留 `dtype`，最好使用 `itertuples()`，该方法返回命名元组，并且比 `iterrows` 快。


## itertuples

```py
DataFrame.itertuples(index=True, name='Pandas')
```

以命名元组的形式按行迭代。

**参数：**

- **index**: `bool`, default True

True 表示返回元组的第一个元素为索引。

- **name**: `str` or `None`, default “Pandas”

命名元祖的名称，`None` 表示返回常规元祖。

**返回：**

- iterator

DataFrame 行的迭代器，以命名元组的形式返回每一行，其中第一个字段可以是索引，后面为对应 column 的值。

> **NOTE**
> 如果列名是无效的 Python 识别符、重复值或以下划线开头，则重命名为位置名称。

**示例：**

```py
>>> df = pd.DataFrame({'num_legs': [4, 2], 'num_wings': [0, 2]},
...                  index=['dog', 'hawk'])
>>> df
      num_legs  num_wings
dog          4          0
hawk         2          2
>>> for row in df.itertuples():
...    print(row)
...
Pandas(Index='dog', num_legs=4, num_wings=0)
Pandas(Index='hawk', num_legs=2, num_wings=2)
```

- 如果将 `index` 设置为 `False`，则移除索引

```py
>>> for row in df.itertuples(index=False):
...    print(row)
...
Pandas(num_legs=4, num_wings=0)
Pandas(num_legs=2, num_wings=2)
```

- `name` 用于自定义命名元祖的名称

```py
>>> for row in df.itertuples(name='Animal'):
...    print(row)
...
Animal(Index='dog', num_legs=4, num_wings=0)
Animal(Index='hawk', num_legs=2, num_wings=2)
```