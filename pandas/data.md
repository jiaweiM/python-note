# 数据结构

- [数据结构](#%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [查询 - position](#%e6%9f%a5%e8%af%a2---position)
  - [filter](#filter)
  - [reset_index](#resetindex)

## 简介

Pandas 包含三种类型数据：

- `Series`
- `DataFrame`
- `Panel`

分别对应一维、二维、三维数据。

它们在创建后，均可以动态修改数值，即是 value mutable。`Series`在创建后，长度不再改变。

`Panel` 在 0.25.0 移除。

## 查询 - position

Pandas 提供了基于索引的操作方法。

以 `.iloc` 属性开始，接收如下输入：

- 整数
- 整数列表，如 [4, 3, 0]
- 整数类型切片对象，如 1:7
- boolean 数组
- `callable`

## filter

根据 label 选择 series 或 dataframe 的子集

要注意该方法是基于 index 的 label 尽心过滤，而不是基于数据。

`filter(self, items=None, like:Union[str, NoneType]=None,regex:Union[str, NoneType]=None, axis=None)`

返回过滤后的 DataFrame 或 Series.

**返回**：返回类型和输入类型相同。

1. items

类 list 对象，该方法会保留 `items` 标签对应的数据。

2. like: str

保留满足 `like in label == True` 的数据，即保留 like 为标签的子字符串。

其语法等效于：`s[[like in i for i in s.index]]`

3. regex: str

保留满足 `re.search(regex, label) == True` 的数据。

4. axis: {0 or 'index', 1 or 'columns', None}, default None

指定对哪个 axis 进行过滤，可以是索引（int）或名称（str）。其默认为 info axis，对 Series 为 'index'，对 DataFrames 为 'columns'。

> 上面的 `items`, `like` 和 `regex` 参数是互斥的，即只需要指定一个，也只用到一个。

- 选择指定列

```py
df = pd.DataFrame(np.array(([1, 2, 3], [4, 5, 6])),
                  index=['mouse', 'rabbit'],
                  columns=['one', 'two', 'three'])
df1 = df.filter(items=['one', 'three'])
assert_frame_equal(df1, pd.DataFrame(np.array(([1, 3], [4, 6])),
                                      index=['mouse', 'rabbit'],
                                      columns=['one', 'three']))
```

- 按照正则表达式选择

```py
>>> # select columns by regular expression
>>> df.filter(regex='e$', axis=1)
         one  three
mouse     1      3
rabbit    4      6
```

- 选择子字符串选择

```py
>>> # select rows containing 'bbi'
>>> df.filter(like='bbi', axis=0)
         one  two  three
rabbit    4    5      6
```

## reset_index

`reset_index(level=None, drop=False, name=None, inplace=False)`

生成一个新的 `DataFrame` 或 `Series`，其 index 重置。

当需要将 index 视作 column，或者索引无意义，需要在其它操作前进行重置。

