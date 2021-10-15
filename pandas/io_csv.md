# CSV

- [CSV](#csv)
  - [简介](#简介)
  - [读 CSV](#读-csv)
    - [指定索引列](#指定索引列)
    - [返回 Series 类型](#返回-series-类型)
    - [指定列](#指定列)
    - [解析日期列](#解析日期列)
    - [sep](#sep)
    - [delimiter](#delimiter)
    - [delim_whitespace](#delim_whitespace)
    - [header](#header)
  - [引号、压缩和文件格式](#引号压缩和文件格式)
    - [thousands](#thousands)
    - [encoding](#encoding)
  - [NA 和缺失值处理](#na-和缺失值处理)
    - [na_values](#na_values)
  - [to_csv](#to_csv)
  - [参考](#参考)

2020-08-13, 10:35
***

## 简介

pandas 用于读取文本文件的函数主要为 `read_csv()` 和 `read_table()`。两者使用相同的解析代码将表格数据转换为 `DataFrame` 对象。

## 读 CSV

方法签名：

```py
pandas.read_csv(filepath_or_buffer, sep=NoDefault.no_default, delimiter=None, header='infer', names=NoDefault.no_default, index_col=None, usecols=None, squeeze=False, prefix=NoDefault.no_default, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, error_bad_lines=None, warn_bad_lines=None, on_bad_lines=None, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None, storage_options=None)
```

- `filepath_or_buffer`

文件路径（`str`, `pathlib.Path` 或 `py._path.local.LocalPath`）, URL（包括 http, ftp 和 S3） 或其它包含 `read()` 方法的对象。

最简单的使用方式：

```py
import pandas as pd
df = pd.read_csv('sample.csv')
```

### 指定索引列

`index_col` 用于指定索引列，接受类型：

- int，指定索引的 column 作为索引列；
- str，指定名称的 column 作为索引列；
- int/str 序列，将多个 column 作为索引，此时使用 `MultiIndex`；
- Flase，使 pandas 不将第一列作为索引。

**例1**，使用指定名称的 column 作为索引：

```py
>>> pd.read_csv(filepath_or_buffer='pokemon.csv')
         Pokemon            Type
0      Bulbasaur  Grass / Poison
1        Ivysaur  Grass / Poison
2       Venusaur  Grass / Poison
3     Charmander            Fire
4     Charmeleon            Fire
..           ...             ...
804    Stakataka    Rock / Steel
805  Blacephalon    Fire / Ghost
806      Zeraora        Electric
807       Meltan           Steel
808     Melmetal           Steel

[809 rows x 2 columns]
```

现在我们将 'Pokemon' 这一列作为索引：

```py
>>> pd.read_csv(filepath_or_buffer='pokemon.csv', index_col='Pokemon')
                       Type
Pokemon                    
Bulbasaur    Grass / Poison
Ivysaur      Grass / Poison
Venusaur     Grass / Poison
Charmander             Fire
Charmeleon             Fire
...                     ...
Stakataka      Rock / Steel
Blacephalon    Fire / Ghost
Zeraora            Electric
Meltan                Steel
Melmetal              Steel

[809 rows x 1 columns]
```

### 返回 Series 类型

`squeeze`, bool 类型，如果为 `True`，当数据只有一列时以 `Series` 类型返回数据。例如：

```py
>>> pd.read_csv(filepath_or_buffer='pokemon.csv', index_col='Pokemon')
                       Type
Pokemon                    
Bulbasaur    Grass / Poison
Ivysaur      Grass / Poison
Venusaur     Grass / Poison
Charmander             Fire
Charmeleon             Fire
...                     ...
Stakataka      Rock / Steel
Blacephalon    Fire / Ghost
Zeraora            Electric
Meltan                Steel
Melmetal              Steel

[809 rows x 1 columns]
>>> pd.read_csv(filepath_or_buffer=r'pokemon.csv', index_col='Pokemon', squeeze=True) # 此时返回 Series 类型
Pokemon
Bulbasaur      Grass / Poison
Ivysaur        Grass / Poison
Venusaur       Grass / Poison
Charmander               Fire
Charmeleon               Fire
                    ...      
Stakataka        Rock / Steel
Blacephalon      Fire / Ghost
Zeraora              Electric
Meltan                  Steel
Melmetal                Steel
Name: Type, Length: 809, dtype: object
```

### 指定列

`usecols` 参数用于选择文件中的指定列：

- list-like，要么为索引列表，要么为 column 标题列表，例如 `[0, 1, 2]` 或 `['foo', 'bar', 'baz']`；
- callable，callable 函数用于识别 column 标题，保留返回 True 的列。

例如：

```py
>>> pd.read_csv('revolutionary_war.csv', index_col='Start Date', parse_dates=['Start Date'])
                                       Battle          State
Start Date                                                  
1774-09-01                       Powder Alarm  Massachusetts
1774-12-14  Storming of Fort William and Mary  New Hampshire
1775-04-19   Battles of Lexington and Concord  Massachusetts
1775-04-19                    Siege of Boston  Massachusetts
1775-04-20                 Gunpowder Incident       Virginia
...                                       ...            ...
1782-09-11                Siege of Fort Henry       Virginia
1782-09-13         Grand Assault on Gibraltar            NaN
1782-10-18          Action of 18 October 1782            NaN
1782-12-06          Action of 6 December 1782            NaN
1783-01-22          Action of 22 January 1783       Virginia

[232 rows x 2 columns]
```

现在我们不需要 'Battle' 列，只希望保留指定为索引的 'Start Date' 列和 'State'：

```py
>>> pd.read_csv('revolutionary_war.csv', index_col='Start Date', parse_dates=['Start Date'], usecols=['State', 'Start Date'], squeeze=True)
Start Date
1774-09-01    Massachusetts
1774-12-14    New Hampshire
1775-04-19    Massachusetts
1775-04-19    Massachusetts
1775-04-20         Virginia
                  ...      
1782-09-11         Virginia
1782-09-13              NaN
1782-10-18              NaN
1782-12-06              NaN
1783-01-22         Virginia
Name: State, Length: 232, dtype: object
```

### 解析日期列

`parse_date` 参数用于指定特定列，将其解析为日期类型：

- boolean, 尝试将 index 解析为日期；
- list or int or names，指定位置和名称的列解析为日期；
- list of lists，如 [[1, 3]]，表示将 1 和 3 列合并解析为 1 个日期；
- dict，如 {'foo': [1, 3]}，表示将 1 和 3 列解析为日期，并以 'foo' 保存。

如果指定的列因为一些原因无法解析为日期，例如存在无法解析的值，则依旧作为 object 数据类型处理。对非标准日期的解析，可以在读取文件后使用 `pd.to_datetime` 处理。

**例1**，将指定列解析为日期类型：

```py
>>> pd.read_csv(filepath_or_buffer='google_stocks.csv', parse_dates=['Date'], index_col='Date', squeeze=True)
Date
2004-08-19      49.98
2004-08-20      53.95
2004-08-23      54.50
2004-08-24      52.24
2004-08-25      52.80
               ...   
2019-10-21    1246.15
2019-10-22    1242.80
2019-10-23    1259.13
2019-10-24    1260.99
2019-10-25    1265.13
Name: Close, Length: 3824, dtype: float64
```

这里将 'Date' 类指定为索引，并作为日期类型解析，使用 `squeeze` 将数据以 `Series` 返回。


### sep

分隔符，`str` 类型, 对 `read_csv()` 默认为 `,`，对 `read_table()` 默认为 `\t`。

如果为 `None`，C 引擎无法自动检测分隔符，此时 Python 解析引擎使用 `csv.Sniffer` 检测分隔符。

如果分隔符长度 > 1，且不是 `\s+`，则作为正则表达式处理，且强制使用 Python 解析引擎。

### delimiter

`str`, default `None`。

`sep` 的备用参数名称。

### delim_whitespace

boolean, default False.

空白（如 ' ' 或 '\t'） 是否当作分隔符。等价于设置 `sep='\s+'`。如果启用该选项，不能同时使用 `delimiter` 选项。

### header

## 引号、压缩和文件格式

### thousands

`str`, default `None`。

用于指定千位分隔符。

### encoding

`str`, default `None`。

指定读写时使用的编码，例如 'utf-8'。

[Python 标准编码列表](https://docs.python.org/3/library/codecs.html#standard-encodings)

## NA 和缺失值处理

### na_values

`na_values`，scalar, str, list-like, or dict, default `None`。

识别为 `NA/NaN` 的额外字符串。如果使用 dict，则可以对每列单独设置。

## to_csv

```py
DataFrame.to_csv(path_or_buf=None, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)
```

输出为 `csv` 格式。

## 参考

- https://pandas.pydata.org/docs/reference/io.html
- https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
