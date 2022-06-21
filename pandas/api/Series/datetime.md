# Datetime

- [Datetime](#datetime)
  - [简介](#简介)
  - [Datetime properties](#datetime-properties)
    - [Series.dt.year](#seriesdtyear)

## 简介

## Datetime properties

### Series.dt.year

Last updated: 2022-06-15, 15:51

```py
Series.dt.year
```

datetime 的 year。

```py
>>> datetime_series = pd.Series(pd.date_range("2000-01-01", periods=3, freq="Y"))
>>> datetime_series
0   2000-12-31
1   2001-12-31
2   2002-12-31
dtype: datetime64[ns]
>>> datetime_series.dt.year
0    2000
1    2001
2    2002
dtype: int64
```
