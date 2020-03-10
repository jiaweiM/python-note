
# <font color="purple">概述</font>
pandas I/O API 提供了许多读写函数，读取文件的函数命名类似于`pandas.read_csv()` 返回一个 pandas 对象。对应的输出函数类似于 `DataFrame.to_csv()`。下面列举了所有的I/O方法：

|格式类型|格式|读方法|写方法|
|---|---|---|---|
|text|CSV|read_csv|to_csv|
|text|JSON|read_json|to_json|
|text|HTML|read_html|to_html|
|text|Local clipboard|read_clipboard|to_clipboard|
|binary|MS_Excel|read_excel|to_excel|
|binary|OpenDocument|read_excel|	 |
|binary|HDF5 Format|read_hdf|to_hdf|
|binary|Feather Format|read_feather|to_feather|
|binary|Parquet Format|read_parquet|to_parquet|
|binary|Msgpack	|read_msgpack|to_msgpack|
|binary|Stata	|read_stata|to_stata|
|binary|SAS	read_sas||	 |
|binary|Python Pickle Format|read_pickle|to_pickle|
|SQL|SQL|read_sql	|to_sql|
|SQL|Google Big Query	|read_gbq|to_gbq|

# CSV

pandas 用于读取文本文件的函数主要为 `read_csv()` 和 `read_table()`。两者使用相同的解析代码将表格数据转换为 `DataFrame` 对象。

`read_csv()` 和 `read_table()` 的共有参数：
|参数|类型|说明|
|---|---|---|
|filepath_or_buffer|	|文件路径（str, pathlib.Path or py._path.local.LocalPath）, URL 或其他包含 `read()` 方法的对象|
|sep|str|分隔符号|
|delimiter|str|sep 的备选|
|delim_whitespace|boolean|default=False, 是否将空格作为 delimiter|

## read_csv()
最简单的使用方式：
```py
import pandas as pd
df = pd.read_csv('sample.csv')
```
`read_csv` 参数：
|参数|说明|
|---|---|
|`names`|指定列的名称。如果文件没有标题行，应该指定 `header=None`|
|`skiprows=None`|list-like or integer or callable. 跳过的文件开头的行（0-indesed）|