# CSV 和文本文件

- [CSV 和文本文件](#csv-和文本文件)
  - [简介](#简介)
  - [解析选项](#解析选项)
    - [filepath_or_buffer](#filepath_or_buffer)
    - [sep](#sep)
    - [names](#names)
    - [na_values](#na_values)
  - [注释和空行](#注释和空行)
    - [忽略注释行和空行](#忽略注释行和空行)
  - [NA 值](#na-值)
  - [参考](#参考)

## 简介

`read_csv()` 是读取文本文件的主要函数。

## 解析选项

`read_csv()` 支持以下选项。

### filepath_or_buffer

支持：

- 文件路径（`str`, `pathlib.Path` 或 `py:py._path.local.LocalPath`）
- URL (包括 http, ftp 和 S3 位置)
- 带有 `read()` 方法的对象，如打开的文件或 `StringIO`。

### sep

- `sep`, str, defaults to `','` for `read_csv()`, `\t` for `read_table()`



### names

array-like, default `None`

column 名称列表。如果文件不包含标题行，则应该设置 `header=None`。该列表不允许重复值。

### na_values

- scalar, str, list-like, or dict, default `None`

额外可以识别为 NA/NaN 的字符串。对 `dict`，可以为每列指定 NA 值。

## 注释和空行

### 忽略注释行和空行

如果指定 `comment` 参数，则忽略注释行。默认忽略空白行。

```python

```

## NA 值



## 参考

- https://pandas.pydata.org/docs/user_guide/io.html
