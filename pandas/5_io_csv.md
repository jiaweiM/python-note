# CSV

- [CSV](#csv)
  - [read_csv()](#readcsv)

pandas 用于读取文本文件的函数主要为 `read_csv()` 和 `read_table()`。两者使用相同的解析代码将表格数据转换为 `DataFrame` 对象。

`read_csv()` 和 `read_table()` 的共有参数：
| 参数               | 类型                   | 说明                                                                                          |
| ------------------ | ---------------------- | --------------------------------------------------------------------------------------------- |
| filepath_or_buffer |                        | 文件路径（str, pathlib.Path or py._path.local.LocalPath）, URL 或其它包含 `read()` 方法的对象 |
| sep                | str                    | 分隔符号                                                                                      |
| delimiter          | str, default None      | sep 的备选                                                                                    |
| delim_whitespace   | boolean, default false | default=False, 是否将空格作为 delimiter                                                       |

## read_csv()

最简单的使用方式：

```py
import pandas as pd
df = pd.read_csv('sample.csv')
```

`read_csv` 参数：
| 参数            | 说明                                                              |
| --------------- | ----------------------------------------------------------------- |
| `names`         | 指定列的名称。如果文件没有标题行，应该指定 `header=None`          |
| `skiprows=None` | list-like or integer or callable. 跳过的文件开头的行（0-indesed） |

- index_col, int, str, sequence of int/str, False, default `None`

用作 DataFrame 行标签的列，以字符串名称或 column index 的形式给出。如果是 int/str 序列，则使用 `MultiIndex`。
