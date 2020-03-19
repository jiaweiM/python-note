# Content
- [Content](#content)
- [简介](#%e7%ae%80%e4%bb%8b)
- [内存 workbook 操作](#%e5%86%85%e5%ad%98-workbook-%e6%93%8d%e4%bd%9c)
- [文件读取](#%e6%96%87%e4%bb%b6%e8%af%bb%e5%8f%96)
- [只读模式](#%e5%8f%aa%e8%af%bb%e6%a8%a1%e5%bc%8f)
- [Pandas 和 Numpy 支持](#pandas-%e5%92%8c-numpy-%e6%94%af%e6%8c%81)

# 简介
openpyxl 是用于读写 Excel 2010 xlsx/xlsm/xltx/xltm 文件的 python 库。


# 内存 workbook 操作
首先，创建一个 Workbook:
```py
from openpyxl import Workbook
wb = Workbook()
```

workbook 创建后，至少有一个 sheet，可以通过 `active()` 属性获得该 sheet:
```py
ws = wb.active
```
NOTE：该属性使用 `_active_sheet_index` 属性，其默认值为 0，如果不主动修改，使用上面的方法总会返回第一个 sheet。

创建 sheet:
```py
ws1 = wb.create_sheet("Mysheet") # insert at the end (default)
```

或者在指定位置插入 sheet:
```py
ws2 = wb.create_sheet("Mysheet", 0)
```

在创建 sheet，其命名默认为 (Sheet, Sheet1, Sheet2, …)这种数字系，可以通过 sheet 的 `title` 属性设置标题：
```py
ws.title = 'New Title'
```

标题的背景色默认为 white。

# 文件读取
使用 `load_workbook()` 打开文件：
```py
wb2 = load_workbook('test.xlsx')
```

# 只读模式
对非常大的 XLSX 文件，无法一次性载入内存，此时可以采用只读模式，对应类为：
	`openpyxl.worksheet.read_only.ReadOnlyWorksheet`

使用方法：
```py
from openpyxl import load_workbook

wb = load_workbook(filename="large_file.xlsx", read_only=True)
ws = wb['big_data']

for row in ws.rows:
    for cell in row:
        print(cell.value)
```
其中返回的 Cell 并非常规的 `openpyxl.cell.cell.Cell`，而是 `openpyxl.cell.read_only.ReadOnlyCell`.

# Pandas 和 Numpy 支持
openpyxl 内置支持 NumPy float, integer 和 boolean 类型。DateTimes 则通过 Pandas 的 `Timestamp` 类型支持。
