# Pandas Excel

- [Pandas Excel](#pandas-excel)
  - [简介](#简介)
  - [读 Excel](#读-excel)
    - [单个 Sheet](#单个-sheet)
    - [多个 Sheet](#多个-sheet)
    - [指定读取的表格](#指定读取的表格)
    - [读取 `MultiIndex`](#读取-multiindex)
    - [解析指定列](#解析指定列)
    - [解析日期](#解析日期)
    - [Cell converters](#cell-converters)
    - [指定 dtype](#指定-dtype)
  - [写 Excel](#写-excel)
    - [写入 disk](#写入-disk)
    - [写入内存](#写入内存)
  - [Excel writer engines](#excel-writer-engines)
  - [样式和格式](#样式和格式)
  - [参考](#参考)

Last updated: 2023-03-16, 18:39
****

## 简介

pandas `read_excel()` 函数读取 Excel，内部实现为：

- 使用 `xlrd` 模块读取 Excel 2003 (.xls) 文件；
- 使用 `openpyxl` 读取 Excel 2007+ (.xlsx) 文件；
- 使用 `pyxlsb` 读取 Binary Excel (.xlsb) 文件。

`to_excel()` 函数将 `DataFrame` 保存为 Excel。

> **Warning:** 不再维护输出 `.xls` 文件的 `xlwt` 包。`xlrd` 包只用于读取老式的 `.xls` 文件。
> 在 pandas 1.3.0 之前，`read_excel()` 的 `engine=None` 参数默认使用 `xlrd` 引擎，包括 Excel 2007+（`.xlsx`）文件。pandas 现在默认使用 `openpyxl` 引擎。
> 强烈建议安装 `openpyxl` 来读取 .xlsx 文件。不再支持使用 `xlrd` 读取 `.xlsx` 文件。

## 读 Excel

### 单个 Sheet

使用 `read_excel()` 读取 Excel 文件，`sheet_name` 指定读取的 sheet:

```py
# 返回 DataFrame
pd.read_excel('path_to_file.xls', sheet_name='Sheet1')
```

如果未指定 `sheet_name`，其默认为 0，即第一个 sheet。

### 多个 Sheet

要一次读取多个 sheets，需要用到 `ExcelFile` 类，该类包装 Excel 文件。

这种方式一次性读取所有 excel 内容到内存，速度较快。

```python
xlsx = pd.ExcelFile('path_to_file.xls')
df = pd.read_excel(xlsx, 'Sheet1')
```

或者使用 context manager：

```python
with pd.ExcelFile('path_to_file.xls') as xls:
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')
```

`ExcelFile` 的 `sheet_names` 属性获得文件的所有 sheet 名称。

`ExcelFile` 主要用来支持使用不同参数解析 sheets:

```python
data = {}
# Sheet1 的格式与 Sheet2 不同时使用
with pd.ExcelFile('path_to_file.xls') as xls:
    data['Sheet1'] = pd.read_excel(xls, 'Sheet1', index_col=None,
                                   na_values=['NA'])
    data['Sheet2'] = pd.read_excel(xls, 'Sheet2', index_col=1)
```

`index_col` 指定用于行索引的列。如果没有这类列，可以用 `None`。

如果使用相同的参数读取所有 sheets，则可以直接将所有 sheet 的名称传递给 `read_excel`，不会降低性能。

```py
# 使用 ExcelFile 类
data = {}
with pd.ExcelFile('path_to_file.xls') as xls:
    data['Sheet1'] = pd.read_excel(xls, 'Sheet1', index_col=None,
                                   na_values=['NA'])
    data['Sheet2'] = pd.read_excel(xls, 'Sheet2', index_col=None,
                                   na_values=['NA'])

# 使用 read_excel 函数效果一样
data = pd.read_excel('path_to_file.xls', ['Sheet1', 'Sheet2'],
                     index_col=None, na_values=['NA'])
```

也可以使用 `xlrd.book.Book` 创建 `ExcelFile`。使用该方法可以控制读取 excel 文件的方式。例如：设置 `xlrd.open_workbook()` 参数 `on_demand=True`，只在需要时载入 sheets:

```python
import xlrd
xlrd_book = xlrd.open_workbook('path_to_file.xls', on_demand=True)
with pd.ExcelFile(xlrd_book) as xls:
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')
```

### 指定读取的表格

说明：

- `read_excel` 的第二个参数为 `sheet_name`，不要和 `ExcelFile.sheet_names` 混淆；
- `ExcelFile` 的 `sheet_names` 用于访问 sheets 列表；
- 使用 `sheet_name` 可以指定要读取的一个或多个 sheet；
- `sheet_name` 默认为 0，即第一个 sheet；
- 字符串类型的 `sheet_name` 参数表示 sheet 的名称；
- integer 类型的 `sheet_name` 参数表示 sheet 的索引，索引以 0 开始；
- 传入 string 或 int 列表参数，返回 sheets 字典；
- 传入 `None` 返回所有 sheets 的字典。

例如：

- 使用 sheet 名称

```py
# Returns a DataFrame
pd.read_excel('path_to_file.xls', 'Sheet1', index_col=None, na_values=['NA'])
```

- 使用索引

```py
# Returns a DataFrame
pd.read_excel('path_to_file.xls', 0, index_col=None, na_values=['NA'])
```

- 全部使用默认值，获得第一个 sheet 的 DataFrame

```py
# Returns a DataFrame
pd.read_excel('path_to_file.xls')
```

- 使用 `None` 获得所有 sheets 的字典

```py
# Returns a dictionary of DataFrames
pd.read_excel('path_to_file.xls', sheet_name=None)
```

- 使用 list 读取多个 sheets

```py
# Returns the 1st and 4th sheet, as a dictionary of DataFrames.
pd.read_excel('path_to_file.xls', sheet_name=['Sheet1', 3])
```

> 从这里可以看出，`sheet_name` 中可以混合使用名称和索引。

### 读取 `MultiIndex`

`read_excel` 可以通过将 columns 列表传递给 `index_col` 读取 `MultiIndex` index；也可以通过将 rows 列表传递给 `header` 读取 `MultiIndex` column。

如果 index 或 columns 具有序列化 level 名称，则可以通过指定对应 level 的 rows/columns 读取它们。

例如，通过 `index_col` 读取 `MultiIndex`：

```py
In [316]: df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8]},
   .....:                   index=pd.MultiIndex.from_product([['a', 'b'], ['c', 'd']]))
In [317]: df.to_excel('path_to_file.xlsx')
In [318]: df = pd.read_excel('path_to_file.xlsx', index_col=[0, 1])
In [319]: df
Out[319]:
     a  b
a c  1  5
  d  2  6
b c  3  7
  d  4  8
```

如果 `index` 包含 level 名称，也可以使用相同参数读取：

```py
In [320]: df.index = df.index.set_names(['lvl1', 'lvl2'])
In [321]: df.to_excel('path_to_file.xlsx')
In [322]: df = pd.read_excel('path_to_file.xlsx', index_col=[0, 1])
In [323]: df
Out[323]:
           a  b
lvl1 lvl2
a    c     1  5
     d     2  6
b    c     3  7
     d     4  8
```

如果源文件的 index 和 columns 同时为 `MultiIndex`，则需要通过 `index_col` 指定索引列，通过 `header` 指定索引行：

```py
In [324]: df.columns = pd.MultiIndex.from_product([['a'], ['b', 'd']],
   .....:                                         names=['c1', 'c2'])
In [325]: df.to_excel('path_to_file.xlsx')
In [326]: df = pd.read_excel('path_to_file.xlsx', index_col=[0, 1], header=[0, 1])
In [327]: df
Out[327]:
c1         a
c2         b  d
lvl1 lvl2
a    c     1  5
     d     2  6
b    c     3  7
     d     4  8
```

`index_col` 指定的 columns 中缺失的值将被前向填充，以支持 `to_excel` 的 `merged_cells=True`。要避免前向填充缺失值，在读取数据后使用 `set_index` 代替 `index_col`。

### 解析指定列

用户常插入列在 Excel 中执行临时计算，而你可能不想读入这些列。`read_excel` 通过 `usecols` 关键字参数指定需要解析的列。

> `usecols` 传入单个整个作为参数无效。应使用包含 0 到 `usecols` 的整数 list 替代。

- 使用逗号分隔的column字符串，column 范围字符串

```py
pd.read_excel('path_to_file.xls', 'Sheet1', usecols='A,C:E')
```

- 整数列表

表示需要解析的 column indices。

```py
pd.read_excel('path_to_file.xls', 'Sheet1', usecols=[0, 2, 3])
```

这种情况忽略顺序，`usecols=[0, 1]` 等价于 `[1, 0]`。

- 字符串列表

表示 column name。文件的 column 名称由 `names` 参数提供，或者通过推断文件标题行获得。例如，指定待解析的列：

```py
pd.read_excel('path_to_file.xls', 'Sheet1', usecols=['foo', 'bar'])
```

顺序无所谓。`usecols=['baz', 'joe']` 和 `['joe', 'baz']` 等价。

- callable

如果 `usecols` 是 callable，则 callable 函数根据 column 计算，返回结果为 True 的 column 名称。

```py
pd.read_excel('path_to_file.xls', 'Sheet1', usecols=lambda x: x.isalpha())
```

### 解析日期

Datetime 值一般自动转换为合适的 dtype 类型。对不确定的数值，可以使用 `parse_dates` 指定特定列转换为 datetimes:

```py
pd.read_excel('path_to_file.xls', 'Sheet1', parse_dates=['date_strings'])
```

### Cell converters

通过 `converters` 选项可以将 Excel cells 的内容转换为特定类型。例如，将 column 转换为 boolean:

```py
pd.read_excel('path_to_file.xls', 'Sheet1', converters={'MyBools': bool})
```

该选项能处理缺失值，对 `converters` 中出现异常的值转换为缺失值。

转换逐个 cell 进行，而不是整个 column 一起转换，所以无法保障整个 column 的 dtype 一致。例如，包含缺失值的 interger 类型 column 可能无法转换为 integer dtype 的数组，因为 NaN 严格来说是 float。对这种情况，可以手动转换值：

```py
def cfun(x):
    return int(x) if x else -1

pd.read_excel('path_to_file.xls', 'Sheet1', converters={'MyInts': cfun})
```

### 指定 dtype

除了使用 `converters`，整个 column 的类型可以使用 `dtype` 关键字指定，`dtype` 参数使用 dict 类型参数，包含 column 名称到类型的映射。对无需类型推断的数据，使用 `str` 或 `object` 类型。例如：

```py
pd.read_excel('path_to_file.xls', dtype={'MyInts': 'int64', 'MyText': str})
```

## 写 Excel

### 写入 disk

使用 `to_excel` 将一个 `DataFrame` 对象写入 Excel 文件的单个 sheet。其参数与 `to_csv` 基本相同，第一个参数为 excel 文件名，第二个可选参数为 sheet 名称。例如：

```python
df.to_excel("path_to_file.xlsx", sheet_name="Sheet1")
```

`.xls` 扩展的文件用 xlwt 输出，`.xlsx` 扩展则用 `xlsxwriter` (如果有)或 `openpyxl` 输出。

`DataFrame` 将以模拟 REPL 输出的方式写入 excel。`index_label` 写入第二行而不是第一行，将 `to_excel()` 的 `meerge_cells` 设置为 `False` 可以写入第一行：

```python
df.to_excel("path_to_file.xlsx", index_label="label", merge_cells=False)
```

为了将不同的 `DataFrame` 写入单个 Excel 文件的不同 sheet，可以使用 `ExcelWriter`：

```python
with pd.ExcelWriter("path_to_file.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Sheet1")
    df2.to_excel(writer, sheet_name="Sheet2")
```

### 写入内存

pandas 支持使用 `ExcelWriter` 将 Excel 文件写入缓冲区对象，如 `StringIO` 或 `BytesIO`：

```python
from io import BytesIO

bio = BytesIO()

# By setting the 'engine' in the ExcelWriter constructor.
writer = pd.ExcelWriter(bio, engine="xlsxwriter")
df.to_excel(writer, sheet_name="Sheet1")

# Save the workbook
writer.save()

# Seek to the beginning and read to copy the workbook to a variable in memory
bio.seek(0)
workbook = bio.read()
```

> **Note:** `engine` 参数可选，但是推荐使用。设置 engine 决定生成的 workbook 版本。设置 `engine='xlrd'` 生成 Excel 2003 格式的 workbook，使用 `'openpyxl'` 或 `'xlsxwriter'` 生成 Excel 2007+ 格式的 workbook。如果省略，默认生成 Excel 2007 格式。

## Excel writer engines

> **Deprecated:** 由于不再维护 `xlwt` 包，`xlwt` engine 将在 pandas 未来版本中删除。由于 `xlwt` 是唯一支持写入 `.xls` 文件的引擎，所以未来 pandas 应该不再支持写入 .xls 文件。

pandas 通过两种方式选择 Excel writer：

1. 使用 `engine` 关键字参数
2. 通过文件扩展名（通过 config 选项指定的默认值）

pandas 默认对 `.xlsx` 文件使用 `XlsxWriter`，对 `.xlsm` 使用 `openpyxl`，对 `.xls` 使用 `xlwt`。如果安装了多个 engines，可以通过设置 config 选项 `io.excel.xlsx.writer` 和 `io.excel.xls.writer` 设置默认 engine。对 `.xslx` 如果 `XlsxWriter` 不可用，则改用 `openpyxl`。

在 `to_excel` 和 `ExcelWriter` 中可使用 `engine` 参数指定引擎。内置引擎：

- openpyxl
- xlsxwriter
- xlwt

```python
# By setting the 'engine' in the DataFrame 'to_excel()' methods.
df.to_excel("path_to_file.xlsx", sheet_name="Sheet1", engine="xlsxwriter")

# By setting the 'engine' in the ExcelWriter constructor.
writer = pd.ExcelWriter("path_to_file.xlsx", engine="xlsxwriter")

# Or via pandas configuration.
from pandas import options  # noqa: E402

options.io.excel.xlsx.writer = "xlsxwriter"

df.to_excel("path_to_file.xlsx", sheet_name="Sheet1")
```

## 样式和格式

可以使用 `DataFrame` 的 `to_excel` 方法的如下参数设置样式：

- `float_format`: 格式化浮点数的字符串，默认 `None`
- `freeze_panes`：包含两个整数的 tuple，表示要冻结的最底 row 和最右 column。这两个参数都是 1-based，所以 (1,1) 表示冻结第一行和第一列（默认 `None`）。

XlsxWriter 引擎为 `to_excel` 提供了许多格式选项。在 XlsxWriter 文档中提供了许多优秀示例。

## 参考

- https://pandas.pydata.org/docs/user_guide/io.html#excel-files
