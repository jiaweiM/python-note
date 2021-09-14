# Python tuple

- [Python tuple](#python-tuple)
  - [简介](#简介)
  - [创建 tuple](#创建-tuple)
  - [访问值](#访问值)
  - [元组的相对不可变性](#元组的相对不可变性)
  - [作为 dict 的 key](#作为-dict-的-key)
  - [namedtuple](#namedtuple)
    - [_make](#_make)
    - [_asdict](#_asdict)
    - [_replace](#_replace)
    - [_fields](#_fields)
    - [_field_defaults](#_field_defaults)
    - [扩展类](#扩展类)

2020-04-21, 11:32
****

## 简介

Python Tuple 和 list 十分类似，但是不能修改值。可以将 tuple 看作不可变的 list。

使用 tuple 更安全，因此建议能使用 tuple 的地方尽量使用 tuple：

- Tuple 比 list快，如果不修改内容，使用 Tuple 更好；
- Tuple 是 `comparable` 且 `hashable` ，所以可以作为字典的 key 值，List 则不可以。

尝试修改 Tuple 的值抛出 `TypeError` .

Tuple 不可变，所以它没有 list 的任何修改内容的方法，如 append(), extend(), insert(), remove() 和 pop()。这些方法Tuple 都没有。

all(), any(), enumerate(), max(), min(), sorted(), len(), tuple() 等内置函数可用于 Tuple。

|方法|列表|元组|说明|
|---|---|---|---|
|`s.__add__(s2)`|✔️|✔️|s+s2，拼接|
|`s.__iadd_(s2)`|✔️|❌|s += s2，原地拼接|
|`s.append(e)`|✔️|❌|在尾部添加一个新元素|
|`s.clear()`|✔️|❌|删除所有元素|
|`s.__contains__(e)`|✔️|✔️|s 是否包含 e|
|`s.copy()`|✔️|❌|列表的浅复制|
|`s.count(e)`|✔️|✔️|e 在 s 中出现的次数|
|`s.__delitem__(p)`|✔️|❌|把位于 p 的元素删除|
|`s.extend(it)`|✔️|❌|把可迭代对象 it 追加给 s|
|`s.__getitem__(p)`|✔️|✔️|s[p]，获取位置 p 的元素|
|`s.__getnewargs__()`|❌|✔️|在 pickle 中支持更加优化的序列化|
|`s.index(e)`|✔️|✔️|在 s 中找到元素 e 第一次出现的位置|
|`s.insert(p, e)`|✔️|❌|在位置 p 之前插入元素 e|
|`s.__iter__()`|✔️|✔️|获取 s 的迭代器|
|`s.__len__()`|✔️|✔️|len(s)，元素的数量|
|`s.__mul__(n)`|✔️|✔️|s * n，n 个 s 的重复拼接|
|`s.__imul__(n)`|✔️|❌|s *= n，就地重复拼接|
|`s.__rmul__(n)`|✔️|✔️| n * s，反向拼接|
|`s.pop([p])`|✔️|❌|删除最后或者位于 p 的元素，并返回它的值|
|`s.remove(e)`|✔️|❌|删除 s 中第一次出现的 e|
|`s.reverse()`|✔️|❌|就地把 s 的元素倒序排列|
|`s.__reversed__()`|✔️|❌|返回 s 的倒序迭代器|
|`s__setitem__(p, e)`|✔️|❌|s[p] = e，把元素 e 放在位置 p，替代已有的元素|
|`s.sort([key], [reverse])`|✔️|❌|就地对 s 中的元素进行排序|

## 创建 tuple

以圆括号创建，元素之间以逗号分隔。如下：

```py
t1 = () # 创建空的 tuple
t2 = (50, ) # 创建一个元素的 tuple，必须包含括号
t2 = (11, 22, 33)
t3 = tuple([1, 2, 3, 4, 5, ]) # tuple from array
t4 = tuple("abc")  # tuple from string
t5 = 1, 2, 3 # 可以不带括号
```

Tuple 可以和List 相互转换，`tuple()` 函数将 list 转换为 tuple, `list()` 函数将 tuple 转换为 list.

max, min, len, sum 可以在 tuples 中使用。

## 访问值

## 元组的相对不可变性

元组与多数 Python 集合（list, dict, set 等）一样，保存的是对象的引用。如果引用的对象是可变的，即使元组本身不可变，元素依然可变。即元组的不可变性其实指的是 tuple 数据结构的物理内容（即保存的引用）不可变，与引用的对象无关。

> str, bytes 和 array.array 等单一类型的序列是扁平的，保存的不是引用，而是数据本身。

例如：

```py
t1 = (1, 2, [30, 40]) # t1 不可变，但是 t1[-1] 可变
t2 = (1, 2, [30, 40])
assert t1 == t2 # 虽然 t1 和 t2 是不同对象，但是值相同，所以相等

id1 = id(t1[-1])
t1[-1].append(99)
assert t1 == (1, 2, [30, 40, 99])

id2 = id(t1[-1])
assert t1 != t2
assert id1 == id2
```

## 作为 dict 的 key

由于 tuple 是 hashable，所以可以将 tuple 作为 dict 的键。

```py
a_dict[key_a, key_b] = number

for key_a, key_b in a_dict:
  …
```

a_dict.items() 返回值为 tuple 集合，每个 tuple 包含 dict 的键值对。

## namedtuple

`collections.namedtuple` 是一个工厂函数，用来创建一个带字段名称的元组和一个有名字的类。

```py
collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
```

用 `namedtuple` 构建的类所消耗的内存跟元组一样，因为字段名存在对应的类里面，这个实例比普通的对象实例要小一点，因为 Python 不会用 `__dict__` 存放这些实例的属性。

- 创建名为 `typename` 的 tuple 子类。新的子类可以通过属性、索引以及迭代查看字段。子类的实例可以提供 docstring以及 `__repr__()` 方法，从而使得内容更为清晰。
- `field_names` 是字符串序列，例如 `['x', 'y']`。也可以提供空格或逗号分隔字段的**单个字符串**，如 `'x y'` 或 `'x, y'`。
- 字段名称可以是任何不以下划线开头的有效 Python 识别符。
- 如果 `rename=True`，则自动以位置替代无效识别符。例如 `['abc', 'def', 'ghi', 'abc']`被自动替换为 `['abc', '_1', 'ghi', '_3']`，无效识别符 `def` 和重复的 `'abc'` 被自动替换。
- `defaults` 可以为 `None` 或默认值的 iterable 对象。因为带默认值的字段必须在无默认值字段的后面，因此 `defaults` 只能用于右边的参数。例如，如果字段名称为 `['x', 'y', 'z']`，默认值为 `(1, 2)`，则 x 为必须参数，`y` 默认为 1，`z` 默认为 2.
- `module` 参数用于设置 namedtuple 的 `__module__` 属性。

实例：

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

### _asdict

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
