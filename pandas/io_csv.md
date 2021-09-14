# CSV

- [CSV](#csv)
  - [简介](#简介)
  - [read_csv](#read_csv)
    - [filepath_or_buffer](#filepath_or_buffer)
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

2020-08-13, 10:35
***

## 简介

pandas 用于读取文本文件的函数主要为 `read_csv()` 和 `read_table()`。两者使用相同的解析代码将表格数据转换为 `DataFrame` 对象。

## read_csv

方法签名：

```py
pandas.read_csv(filepath_or_buffer, sep=<object object>, delimiter=None, header='infer',
names=None, index_col=None, usecols=None, squeeze=False, prefix=None,
mangle_dupe_cols=True, dtype=None, engine=None, converters=None,
true_values=None, false_values=None, skipinitialspace=False, skiprows=None,
skipfooter=0, nrows=None, na_values=None, keep_default_na=True,
na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_
datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False,
cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=
None, decimal='.', lineterminator=None, quotechar='"', quoting=0,
doublequote=True, escapechar=None, comment=None, encoding=None, dialect=
None, error_bad_lines=True, warn_bad_lines=True, delim_whitespace=False,
low_memory=True, memory_map=False, float_precision=None, storage_
options=None)
```

最简单的使用方式：

```py
import pandas as pd
df = pd.read_csv('sample.csv')
```

### filepath_or_buffer

文件路径（`str`, `pathlib.Path` 或 `py._path.local.LocalPath`）, URL（包括 http, ftp 和 S3） 或其它包含 `read()` 方法的对象。

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

输出问 `csv` 格式。

