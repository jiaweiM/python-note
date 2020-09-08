# CSV

- [CSV](#csv)
  - [简介](#简介)
  - [read_csv](#read_csv)
  - [基本参数](#基本参数)
    - [sep](#sep)
    - [delimiter](#delimiter)
  - [引号、压缩及文件格式参数](#引号压缩及文件格式参数)
    - [thousands](#thousands)
    - [encoding](#encoding)
  - [NA 和缺失值处理](#na-和缺失值处理)
  - [na_values](#na_values)

2020-08-13, 10:35
***

## 简介

pandas 用于读取文本文件的函数主要为 `read_csv()` 和 `read_table()`。两者使用相同的解析代码将表格数据转换为 `DataFrame` 对象。

`read_csv()` 和 `read_table()` 的共有参数：
| 参数               | 类型                   | 说明                                                                                          |
| ------------------ | ---------------------- | --------------------------------------------------------------------------------------------- |
| filepath_or_buffer |                        | 文件路径（str, pathlib.Path or py._path.local.LocalPath）, URL 或其它包含 `read()` 方法的对象 |
| sep                | str                    | 分隔符号                                                                                      |
| delimiter          | str, default None      | sep 的备选                                                                                    |
| delim_whitespace   | boolean, default false | default=False, 是否将空格作为 delimiter                                                       |

## read_csv

最简单的使用方式：

```py
import pandas as pd
df = pd.read_csv('sample.csv')
```

## 基本参数

### sep

str, 对 `read_csv()` 默认为 `,`，对 `read_table()` 默认为 `\t`。

分隔符。如果为 `None`，C 引擎无法自动检测分隔符，此时 Python 解析引擎使用 `csv.Sniffer` 检测分隔符。

如果分隔符长度 > 1，且不是 `\s+`，则作为正则表达式处理，且强制使用 Python 解析引擎。

### delimiter

str, default `None`。

`sep` 的备用参数名称。

| 参数            | 说明                                                              |
| --------------- | ----------------------------------------------------------------- |
| `names`         | 指定列的名称。如果文件没有标题行，应该指定 `header=None`          |
| `skiprows=None` | list-like or integer or callable. 跳过的文件开头的行（0-indesed） |
|thousands|str (None)，千分位分隔符|

- index_col, int, str, sequence of int/str, False, default `None`

用作 DataFrame 行标签的列，以字符串名称或 column index 的形式给出。如果是 int/str 序列，则使用 `MultiIndex`。

## 引号、压缩及文件格式参数

### thousands

str, default `None`。

千位分隔符。

### encoding

str, default `None`。

读写时采用的编码。

## NA 和缺失值处理

## na_values

`na_values`，scalar, str, list-like, or dict, default `None`。

识别为 `NA/NaN` 的额外字符串。如果使用 dict，则可以对每列单独设置。
