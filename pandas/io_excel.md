# Pandas Excel

- [Pandas Excel](#pandas-excel)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [读取 Excel](#%e8%af%bb%e5%8f%96-excel)
    - [读取单个 Sheet](#%e8%af%bb%e5%8f%96%e5%8d%95%e4%b8%aa-sheet)
    - [读取多个 Sheet](#%e8%af%bb%e5%8f%96%e5%a4%9a%e4%b8%aa-sheet)
    - [指定读哪个表格](#%e6%8c%87%e5%ae%9a%e8%af%bb%e5%93%aa%e4%b8%aa%e8%a1%a8%e6%a0%bc)
    - [读取 MultiIndex](#%e8%af%bb%e5%8f%96-multiindex)
  
***

## 简介

功能：

- pandas 的 `read_excel()` 方法使用 `xlrd` 模块读取 Excel 2003 (.xls) 文件。
- 使用 `xlrd` 或 `openpyxl` 读取 Excel 2007+ (.xlsx) 文件。
- 使用 `pyxlsb` 读取 Binary Excel (.xlsb) 文件。

`to_excel()` 方法用于将 `DataFrame` 保存为 Excel。

## 读取 Excel

`pandas.read_excel`

读取 Excel 文件，保存为 pandas DataFrame。

支持 xls, xlsx, xlsm, xlsb 以及 odf 文件格式。支持从本地和 URL 读取文件。

### 读取单个 Sheet

使用 `read_excel()` 读取 Excel 文件，`sheet_name` 指定读取的 sheet:

```py
pd.read_excel('path_to_file.xls', sheet_name='Sheet1')
```

### 读取多个 Sheet

要一次读取多个 sheets，需要用到 `ExcelFile` 类，该类包装 Excel 文件。

这种方式一次性读取所有 excel 内容到内存，速度较快。

```py
xlsx = pd.ExcelFile('path_to_file.xls')
df = pd.read_excel(xlsx, 'Sheet1')
```

或者：

```py
with pd.ExcelFile('path_to_file.xls') as xls:
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')
```

使用 `ExcelFile` 方便使用不同的参数解析 sheets:

```py
data = {}
# For when Sheet1's format differs from Sheet2
with pd.ExcelFile('path_to_file.xls') as xls:
    data['Sheet1'] = pd.read_excel(xls, 'Sheet1', index_col=None,
                                   na_values=['NA'])
    data['Sheet2'] = pd.read_excel(xls, 'Sheet2', index_col=1)
```

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

也可以使用 `xlrd.book.Book` 对象创建 `ExcelFile`。使用该方法可以控制读取 excel 文件的方式。例如：设置 `xlrd.open_workbook()` 参数 `on_demand=True`，可以在需要时才载入 sheets:

```py
import xlrd
xlrd_book = xlrd.open_workbook('path_to_file.xls', on_demand=True)
with pd.ExcelFile(xlrd_book) as xls:
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')
```

### 指定读哪个表格

说明：

- `read_excel` 的第二个参数为 `sheet_name`，不要和 `ExcelFile.sheet_names` 混淆。
- `ExcelFile` 的 `sheet_names` 用于访问 sheets 列表。
- 使用 `sheet_name` 可以指定读哪一个 sheet。
- 默认的 `sheet_name` 为 0，即第一个 sheet。
- 字符串类型的 `sheet_name` 参数表示 sheet 的名称。
- integer 类型的 `sheet_name` 参数表示 sheet 的索引。
- 传入 string 或 int 列表参数，返回 sheets 字典。
- 传入 `None` 返回所有 sheets 的字典。

例如，使用 sheet 名称:

```py
# Returns a DataFrame
pd.read_excel('path_to_file.xls', 'Sheet1', index_col=None, na_values=['NA'])
```

使用索引：

```py
# Returns a DataFrame
pd.read_excel('path_to_file.xls', 0, index_col=None, na_values=['NA'])
```

全部使用默认值，获得第一个 sheet 的 DataFrame:

```py
# Returns a DataFrame
pd.read_excel('path_to_file.xls')
```

使用 `None` 获得所有 sheets 的字典：

```py
# Returns a dictionary of DataFrames
pd.read_excel('path_to_file.xls', sheet_name=None)
```

使用列表读取多个 sheets:

```py
# Returns the 1st and 4th sheet, as a dictionary of DataFrames.
pd.read_excel('path_to_file.xls', sheet_name=['Sheet1', 3])
```

> 从这里可以看出，`sheet_name` 中可以混合使用名称和索引。

### 读取 MultiIndex

