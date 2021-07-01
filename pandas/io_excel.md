# Pandas Excel

- [Pandas Excel](#pandas-excel)
  - [简介](#简介)
  - [读 Excel](#读-excel)
    - [读取单个 Sheet](#读取单个-sheet)
    - [读取多个 Sheet](#读取多个-sheet)
    - [指定读取的表格](#指定读取的表格)
    - [读取 `MultiIndex`](#读取-multiindex)
    - [解析指定列](#解析指定列)
    - [解析日期](#解析日期)
    - [Cell converters](#cell-converters)
    - [指定 dtype](#指定-dtype)
  - [写 Excel](#写-excel)
    - [输出 index](#输出-index)

2020-04-20, 20:54
***

## 简介

读取 Excel 功能：

- pandas 的 `read_excel()` 方法使用 `xlrd` 模块读取 Excel 2003 (.xls) 文件。
- 使用 `xlrd` 或 `openpyxl` 读取 Excel 2007+ (.xlsx) 文件。
- 使用 `pyxlsb` 读取 Binary Excel (.xlsb) 文件。

`to_excel()` 方法用于将 `DataFrame` 保存为 Excel。

## 读 Excel

### 读取单个 Sheet

使用 `read_excel()` 读取 Excel 文件，`sheet_name` 指定读取的 sheet:

```py
pd.read_excel('path_to_file.xls', sheet_name='Sheet1')
```

如果未指定 `sheet_name`，其默认为 0，即第一个 sheet。

### 读取多个 Sheet

要一次读取多个 sheets，需要用到 `ExcelFile` 类，该类包装 Excel 文件。

这种方式一次性读取所有 excel 内容到内存，速度较快。

```py
xlsx = pd.ExcelFile('path_to_file.xls')
df = pd.read_excel(xlsx, 'Sheet1')
```

或者使用 context manager：

```py
with pd.ExcelFile('path_to_file.xls') as xls:
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')
```

`ExcelFile` 的 `sheet_names` 属性获得文件的所有 sheet 名称。

使用 `ExcelFile` 可以使用不同参数解析 sheets:

```py
data = {}
# For when Sheet1's format differs from Sheet2
with pd.ExcelFile('path_to_file.xls') as xls:
    data['Sheet1'] = pd.read_excel(xls, 'Sheet1', index_col=None,
                                   na_values=['NA'])
    data['Sheet2'] = pd.read_excel(xls, 'Sheet2', index_col=1)
```

`index_col` 用于指定用于行索引的列。如果没有这类列，可以用 `None`。

如果使用相同的参数读取所有 sheets，则可以直接将所有 sheet 的名称传递给 `read_excel` 方法，不会降低性能。

```py
# using the ExcelFile class
data = {}
with pd.ExcelFile('path_to_file.xls') as xls:
    data['Sheet1'] = pd.read_excel(xls, 'Sheet1', index_col=None,
                                   na_values=['NA'])
    data['Sheet2'] = pd.read_excel(xls, 'Sheet2', index_col=None,
                                   na_values=['NA'])

# equivalent using the read_excel function
data = pd.read_excel('path_to_file.xls', ['Sheet1', 'Sheet2'],
                     index_col=None, na_values=['NA'])
```

也可以使用 `xlrd.book.Book` 对象创建 `ExcelFile`。使用该方法可以控制读取 excel 文件的方式。例如：设置 `xlrd.open_workbook()` 参数 `on_demand=True`，可以在需要时载入 sheets:

```py
import xlrd
xlrd_book = xlrd.open_workbook('path_to_file.xls', on_demand=True)
with pd.ExcelFile(xlrd_book) as xls:
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')
```

### 指定读取的表格

说明：

- `read_excel` 的第二个参数为 `sheet_name`，不要和 `ExcelFile.sheet_names` 混淆。
- `ExcelFile` 的 `sheet_names` 用于访问 sheets 列表。
- 使用 `sheet_name` 可以指定读取 sheet[s]。
- 默认的 `sheet_name` 为 0，即第一个 sheet。
- 字符串类型的 `sheet_name` 参数表示 sheet 的名称。
- integer 类型的 `sheet_name` 参数表示 sheet 的索引。
- 传入 string 或 int 列表参数，返回 sheets 字典。
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

- 使用默认值，获得第一个 sheet 的 DataFrame

```py
# Returns a DataFrame
pd.read_excel('path_to_file.xls')
```

- 使用 `None` 获得所有 sheets 的字典

```py
# Returns a dictionary of DataFrames
pd.read_excel('path_to_file.xls', sheet_name=None)
```

- 使用列表读取多个 sheets

```py
# Returns the 1st and 4th sheet, as a dictionary of DataFrames.
pd.read_excel('path_to_file.xls', sheet_name=['Sheet1', 3])
```

> 从这里可以看出，`sheet_name` 中可以混合使用名称和索引。

### 读取 `MultiIndex`

`read_excel` 可以通过将 columns 列表传递给 `index_col` 读取 `MultiIndex` 索引；也可以通过将 rows 列表传递给 `header` 读取 `MultiIndex` column。

如果 index 或 columns 具有序列化级别的名称，则可以通过指定对应级别的 rows/columns 读取它们。

例如，通过 `index_col` 读取 `MultiIndex`：

```py
In [316]: df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8]},
   .....:                   index=pd.MultiIndex.from_product([['a', 'b'], ['c', 'd']]))
   .....:

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

如果 index 包含名称，也可以读取：

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
   .....:

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

### 解析指定列

`read_excel` 通过 `usecols` 关键字参数指定需要解析的列。

> deprecated, `usecols` 不推荐使用单个整个作为参数。而使用包含 0 到 `usecols` 的整数替代。

- `usecols` 为整数，表示解析的最后一列，即解析第一列到 `usecols`指定的列

```py
pd.read_excel('path_to_file.xls', 'Sheet1', usecols=2)
```

- 也可以使用逗号分隔的column字符串，column 范围字符串：

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

如果 `usecols` 为 callable，则 callable 函数根据 column 计算，返回结果为 True 的 column 名称。

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

该选项能处理缺失值，对 converters 中出现异常的值，也转换为缺失值。

转换逐个 cell 进行，所以 dtype 无法保障。例如，具有缺失值的 interger 类型 column 可能无法转换为 integer dtype 的数组，因为 NaN 严格来说是 float。对这种情况，可以手动转换值：

```py
def cfun(x):
    return int(x) if x else -1

pd.read_excel('path_to_file.xls', 'Sheet1', converters={'MyInts': cfun})
```

### 指定 dtype

除了使用 converters，整个 column 的类型可以使用 `dtype` 关键字指定，dict 类型参数，包含 column 名称到类型的映射。例如：

```py
pd.read_excel('path_to_file.xls', dtype={'MyInts': 'int64', 'MyText': str})
```

## 写 Excel

```py
DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', ﬂoat_format=None,
  columns=None, header=True, index=True, index_label=None, startrow=0,
  startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf',
  verbose=True, freeze_panes=None, storage_options=None)
```

### 输出 index

设置参数 `index=True` （默认）数出索引。