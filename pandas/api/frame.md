# DataFrame

- [DataFrame](#dataframe)
  - [总结](#总结)
  - [索引、选择、标签操作](#索引选择标签操作)
    - [drop](#drop)
  - [参考](#参考)

## 总结

|操作|函数|
|---|---|
|删除行|[drop](#drop)|
|删除列|[drop](#drop)|

## 索引、选择、标签操作

### drop

Last updated: 2022-06-13, 13:26

```py
DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
```

从行或列中删除指定标签。

通过标签名称和对应轴、列名称或索引等删除行或列。当使用 MultiIndex 时，不同 level 的标签可以通过指定 level 删除。

**返回**：如果 `inplace=True`，返回删除后的 `DataFrame`；否则返回 None。

|参数|类型|说明|
|---|---|---|
|`labels`|single label or list-like|待删除的索引或 column 标签。tuple 作单个 label 处理|
|`axis`|{0 or ‘index’, 1 or ‘columns’}, default 0|指定删除行还是列|
|`index`|single label or list-like| 删除 index 专用，`index=labels` 等价于 `(labels, axis=0)`|
|`columns`|single label or list-like|删除列专用，`columns=labels` 等价于 `(labels, axis=1)`|
|`level`|int or level name, optional|MultiIndex 中指定删除 label 对应的 level|
|`inplace`|bool, default False|False，返回 copy；True，表示原位操作，返回 None|
|`errors`|{‘ignore’, ‘raise’}, default ‘raise’|'ignore' 表示抑制错误，只删除现有标签|

- 删除 'B', 'C' 两列

删除列时推荐使用 `columns` 参数，比使用 `(labels, axis=1)` 便捷。

```py
>>> df = pd.DataFrame(np.arange(12).reshape(3, 4),
                  columns=['A', 'B', 'C', 'D'])
>>> df
   A  B   C   D
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
>>> df.drop(['B', 'C'], axis=1) # 等价于 drop(columns=['B', 'C'])
   A   D
0  0   3
1  4   7
2  8  11
```

- 使用索引删除行

```py
>>> df
   A  B   C   D
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
>>> df.drop([0,1]) # axis 默认为0，即默认删除行
   A  B   C   D
2  8  9  10  11
```

- MultiIndex 删除操作

```py
>>> midx = pd.MultiIndex(levels=[['lama', 'cow', 'falcon'],
                             ['speed', 'weight', 'length']],
                     codes=[[0, 0, 0, 1, 1, 1, 2, 2, 2],
                            [0, 1, 2, 0, 1, 2, 0, 1, 2]])
>>> df = pd.DataFrame(index=midx, columns=['big', 'small'],
                  data=[[45, 30], [200, 100], [1.5, 1], [30, 20],
                        [250, 150], [1.5, 0.8], [320, 250],
                        [1, 0.8], [0.3, 0.2]])
>>> df
                 big  small
lama   speed    45.0   30.0
       weight  200.0  100.0
       length    1.5    1.0
cow    speed    30.0   20.0
       weight  250.0  150.0
       length    1.5    0.8
falcon speed   320.0  250.0
       weight    1.0    0.8
       length    0.3    0.2
```

- 删除特定组合的 MultiIndex

删除 `falcon` 和 `weight` 行。

```py
>>> df.drop(index=('falcon', 'weight'))
                big     small
lama    speed   45.0    30.0
        weight  200.0   100.0
        length  1.5     1.0
cow     speed   30.0    20.0
        weight  250.0   150.0
        length  1.5     0.8
falcon  speed   320.0   250.0
        length  0.3     0.2
```

- 删除特定的行和列

删除 `cow` 行和 `small` 列。

```py
>>> df.drop(index='cow', columns='small')
                 big
lama   speed    45.0
       weight  200.0
       length    1.5
falcon speed   320.0
       weight    1.0
       length    0.3
```

- 删除 level=1 中对应的 `length` 行

```py
>>> df.drop(index='length', level=1)
                 big  small
lama   speed    45.0   30.0
       weight  200.0  100.0
cow    speed    30.0   20.0
       weight  250.0  150.0
falcon speed   320.0  250.0
       weight    1.0    0.8
```

## 参考

- https://pandas.pydata.org/docs/reference/frame.html
