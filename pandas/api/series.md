# Series

## Accessors

pandas 提供了特定于 dtype 的访问器，放在 `Series` 单独的名称空间中。

|数据类型|访问器|
|---|---|
|Datetime, Timedelta, Period|dt|
|String|str|
|Categorical|cat|
|Sparse|sparse|

### Datatimelike properties

`Series.dt` 可用于访问 datetimelike 

## 绘图

## map

Last updated: 2022-06-21, 17:03

```python
Series.map(arg, na_action=None)
```

根据输入映射或函数映射 `Series` 值。

用于将 `Series` 中的值替换为从函数、字典或 `Series` 派生的另一个值。

|参数|类型|说明|
|---|---|---|
|`arg`|function, collections.abc.Mapping subclass or Series|映射定义|
|`na_action`|{None, ‘ignore’}|default None|

`‘ignore’` 表示直接把 NaN 值传过去，不作映射处理。

**返回**：`Series`，与调用 Series 索引相同。

> [!NOTE]
> 当 `arg` 是 dict，Series 中不在 dict 中的值转换为 NaN。如果 dict 是定义了 `__missing__`（即定义了默认值），则使用默认值而非 NaN。

```python
>>> s = pd.Series(['cat', 'dog', np.nan, 'rabbit'])
>>> s
0       cat
1       dog
2       NaN
3    rabbit
dtype: object
```

- `map` 支持 `dict` 或 `Series`。dict 中找不到的值转换为 NaN，除非 dict 定义了默认值，如 `defaultdict`

```python
>>> s.map({'cat': 'kitten', 'dog': 'puppy'})
0    kitten
1     puppy
2       NaN
3       NaN
dtype: object
```

- 也支持函数

```python
>>> s.map('I am a {}'.format)
0       I am a cat
1       I am a dog
2       I am a nan
3    I am a rabbit
dtype: object
```

- 为了避免函数应用到缺失值，可以使用 `na_action='ignore'`

```python
>>> s.map('I am a {}'.format, na_action='ignore')
0       I am a cat
1       I am a dog
2              NaN
3    I am a rabbit
dtype: object
```
