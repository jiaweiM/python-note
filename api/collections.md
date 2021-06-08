# collections

- [collections](#collections)
  - [namedtuple](#namedtuple)
    - [_make](#_make)
    - [_addict](#_addict)
    - [_replace](#_replace)
    - [_fields](#_fields)
    - [_field_defaults](#_field_defaults)
    - [扩展类](#扩展类)

2021-06-08, 12:08
@author Jiawei Mao
***

## namedtuple

```py
collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
```

创建名为 `typename` 的 tuple 子类。新的子类可以通过属性、索引以及迭代查看字段。子类的实例可以提供 docstring以及 `__repr__()` 方法，从而使得内容更为清晰。

`field_names` 是字符串序列，例如 `['x', 'y']`。也可以提供空格或逗号分隔字段的**单个字符串**，如 `'x y'` 或 `'x, y'`。

字段名称可以是任何不以下划线开头的有效 Python 识别符。

如果 `rename=True`，则自动以位置替代无效识别符。例如 `['abc', 'def', 'ghi', 'abc']`被自动替换为 `['abc', '_1', 'ghi', '_3']`，无效识别符 `def` 和重复的 `'abc'` 被自动替换。

`defaults` 可以为 `None` 或默认值的 iterable 对象。因为带默认值的字段必须在无默认值字段的后面，因此 `defaults` 只能用于右边的参数。例如，如果字段名称为 `['x', 'y', 'z']`，默认值为 `(1, 2)`，则 x 为必须参数，`y` 默认为 1，`z` 默认为 2.

`module` 参数用于设置 namedtuple 的 `__module__` 属性。

- 例 1

```py
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)  # 可以使用位置参数或关键字参数
assert p[0] + p[1] == 33

x, y = p
assert x == 11
assert y == 22
```

- 例 2

命名元组对应创建 csv 或 sqlite3 模块返回的结果特别合适。

```py
EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print(emp.name, emp.title)

import sqlite3
conn = sqlite3.connect('/companydata')
cursor = conn.cursor()
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)
```

除了从元组继承的方法，命名元祖还有额外的三种方法和两种属性。

- 例 3：查询

查询指定字段值，使用 `getattr()` 函数：

```py
>>> getattr(p, 'x')
11
```

- 例 4：将 dict 转换命名元组

使用 `**` 拆分参数即可：

```py
>>> d = {'x': 11, 'y': 22}
>>> Point(**d)
Point(x=11, y=22)
```

### _make

从序列或可迭代对象创建实例。例如：

```py
>>> t = [11, 22]
>>> Point._make(t)
Point(x=11, y=22)
```

### _addict

映射字段名称和值，创建一个 `dict`。例如：

```py
>>> p = Point(x=11, y=22)
>>> p._asdict()
{'x': 11, 'y': 22}
```

### _replace

替换指定字段后，创建一个新的实例。例如：

```py
>>> p = Point(x=11, y=22)
>>> p._replace(x=33)
Point(x=33, y=22)

>>> for partnum, record in inventory.items():
...     inventory[partnum] = record._replace(price=newprices[partnum], timestamp=time.now())
```

### _fields

字符串 tuple，列出所有字段名称。方便使用已有名称元组创建新的命名元组：

```py
>>> p._fields            # view the field names
('x', 'y')

>>> Color = namedtuple('Color', 'red green blue')
>>> Pixel = namedtuple('Pixel', Point._fields + Color._fields)
>>> Pixel(11, 22, 128, 255, 0)
Pixel(x=11, y=22, red=128, green=255, blue=0)
```

### _field_defaults

字段名称和默认值映射的 dict。例如：

```py
>>> Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
>>> Account._field_defaults
{'balance': 0}
>>> Account('premium')
Account(type='premium', balance=0)
```

### 扩展类

因为命名元组是常规的 Python 类，因此可以很容易扩展 namedtuple 并添加函数。例如，下面扩展 `Point` 添加计算和打印格式方法：

```py
>>> class Point(namedtuple('Point', ['x', 'y'])):
...     __slots__ = ()
...     @property
...     def hypot(self):
...         return (self.x ** 2 + self.y ** 2) ** 0.5
...     def __str__(self):
...         return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

>>> for p in Point(3, 4), Point(14, 5/7):
...     print(p)
Point: x= 3.000  y= 4.000  hypot= 5.000
Point: x=14.000  y= 0.714  hypot=14.018
```

如果要添加新的字段，没必要扩展类，直接创建一个新的命名字段更合适：

```py
Point3D = namedtuple('Point3D', Point._fields + ('z',))
```
