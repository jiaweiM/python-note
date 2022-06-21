# pandas.to_datetime

## 简介

```py
pandas.to_datetime(arg, errors='raise', dayfirst=False, yearfirst=False, utc=None, format=None, exact=True, unit=None, infer_datetime_format=False, origin='unix', cache=True)
```

将参数转换为 datetime。

该函数将 scalar, array-like `Series`, `DataFrame` 转换为 pandas datetime 对象。

## 示例

### 多种输入格式

将 `DataFrame` 多个 columns 的数据整合为 datatime。key 可以是常见的缩写 [‘year’, ‘month’, ‘day’, ‘minute’, ‘second’, ‘ms’, ‘us’, ‘ns’] 或对应复数形式。

```py
>>> df = pd.DataFrame({'year': [2015, 2016],
...                    'month': [2, 3],
...                    'day': [4, 5]})
>>> pd.to_datetime(df)
0   2015-02-04
1   2016-03-05
dtype: datetime64[ns]
```
