# operator

- [operator](#operator)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [对象比较函数](#%e5%af%b9%e8%b1%a1%e6%af%94%e8%be%83%e5%87%bd%e6%95%b0)
  - [逻辑运算函数](#%e9%80%bb%e8%be%91%e8%bf%90%e7%ae%97%e5%87%bd%e6%95%b0)
  - [数学运算符](#%e6%95%b0%e5%ad%a6%e8%bf%90%e7%ae%97%e7%ac%a6)
  - [查找方法](#%e6%9f%a5%e6%89%be%e6%96%b9%e6%b3%95)
    - [attrgetter](#attrgetter)
      - [查询单个属性](#%e6%9f%a5%e8%af%a2%e5%8d%95%e4%b8%aa%e5%b1%9e%e6%80%a7)
      - [查询多个属性](#%e6%9f%a5%e8%af%a2%e5%a4%9a%e4%b8%aa%e5%b1%9e%e6%80%a7)
      - [带点号查询](#%e5%b8%a6%e7%82%b9%e5%8f%b7%e6%9f%a5%e8%af%a2)
    - [itemgetter](#itemgetter)
      - [实例](#%e5%ae%9e%e4%be%8b)
      - [根据某个关键字排序字典](#%e6%a0%b9%e6%8d%ae%e6%9f%90%e4%b8%aa%e5%85%b3%e9%94%ae%e5%ad%97%e6%8e%92%e5%ba%8f%e5%ad%97%e5%85%b8)
      - [min, max](#min-max)

## 简介

`operator` 模块定义了一系列和 Python 运算符对应的函数。例如 `operator.add(x, y)` 等效于 `x+y`。许多函数名是用于特殊方法的名称，没有双下划线。为了先后兼容，其中许多还保留双下划线版本。

推荐使用不带双下划线的版本。

`operators`函数按照功能可以分为对象比较、逻辑运算、数学运算和序列运算。

下列方法都隐藏了 `operator.` 前缀。

## 对象比较函数

| 推荐方法   | 兼容方法       | 运算符 |
| ---------- | -------------- | ------ |
| `lt(a, b)` | `__lt__(a, b)` | `<`    |
| `le(a, b)` | `__le__(a, b)` | `<=`   |
| `eq(a, b)` | `__eq__(a, b)` | `==`   |
| `ne(a, b)` | `__ne__(a, b)` | `!=`   |
| `ge(a, b)` | `__ge__(a, b)` | `>=`   |
| `gt(a, b)` | `__gt__(a, b)` | `>`    |

## 逻辑运算函数

| 推荐方法       | 兼容方法       | 运算符       |
| -------------- | -------------- | ------------ |
| `not_(obj)`    | `__not__(obj)` | `not obj`    |
| `truth(obj)`   |                | `bool(obj)`  |
| `is_(a, b)`    |                | `a is b`     |
| `is_not(a, b)` |                | `a is not b` |

## 数学运算符

| 推荐方法         | 兼容方法             |
| ---------------- | -------------------- |
| `abs(obj)`       | `__abs__(obj`)       |
| `add(a, b)`      | `__add__(a, b)`      |
| `and_(a, b)`     | `__and__(a, b)`      |
| `floordiv(a, b)` | `__floordiv__(a, b)` |
| `index(a)`       | `__index__(a)`       |
| `inv(obj)`       | `__inv__(obj)`       |
| `invert(obj)`    | `__invert__(obj)`    |
| `lshift(a, b)`   | `__lshift__(a, b)`   |
| `mod(a, b)`      | `__mod__(a, b)`      |

## 查找方法

下列方法对接受函数参数的函数，如 `map()`, `sorted()`, `itertools.groupby()` 等提供了快速提取字段的方法。

### attrgetter

`operator.attrgetter(attr)`

`operator.attrgetter(*attrs)`

返回一个 `callable` 对象，该对象从其操作数中提取 `attr`。如果查询多个属性，返回 tuple 类型。属性名称可以包含点号。

等价于：

```py
def attrgetter(*items):
    if any(not isinstance(item, str) for item in items):
        raise TypeError('attribute name must be a string')
    if len(items) == 1:
        attr = items[0]
        def g(obj):
            return resolve_attr(obj, attr)
    else:
        def g(obj):
            return tuple(resolve_attr(obj, attr) for attr in items)
    return g

def resolve_attr(obj, attr):
    for name in attr.split("."):
        obj = getattr(obj, name)
    return obj
```

#### 查询单个属性

设置 `f = attrgetter('name')`，则 `f(b)` 返回 `b.name`。例如：

```py
class User:
    def __init__(self, name):
        self.name = name

get_name = attrgetter('name')
assert get_name(User('swan')) == 'swan'
```

#### 查询多个属性

设置 `f = attrgetter('name', 'date')`，调用 `f(b)` 返回 `(b.name, b.date)`

#### 带点号查询

设置 `f = attrgetter('name.first', 'name.last')`后，调用 `f(b)` 返回 `(b.name.first, b.name.last)`

### itemgetter

`operator.itemgetter(item)`

`operator.itemgetter(*items)`

返回一个 `callable` 对象，该对象使用操作数的 `__getitem__()` 方法从操作数中获得对应项。如果指定了多项，返回 tuple。例如

- 设置 `f = itemgetter(2)` 后，调用 `f(r)` 返回 `r[2]`
- 设置 `g = itemgetter(2, 5, 3)`后，调用 `g(r)` 返回 `(r[2], r[5], r[3])`

等价于：

```py
def itemgetter(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g
```

#### 实例

其中 `items` 可以是任何 `__getitem__()` 接受的参数。dict 接受任何 hashable 值。list, tuple 和 string 接受索引和切片：

```py
# dict
assert itemgetter('name')({'name': 'swan', 'age': 18}) == 'swan'
# string
assert itemgetter(1)('ABCDEFG') == 'B'
assert itemgetter(1, 3, 5)('ABCDEFG') == ('B', 'D', 'F')
assert itemgetter(slice(2, None))('ABCDEFG') == 'CDEFG'
```

#### 根据某个关键字排序字典

通过 `itemgetter` 获取字典的指定值，然后根据该值排序。假设你从数据库中检索出来网站会员信息列表，并且以下列的数据结构返回：

```py
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
```

根据任意的字段排序：

```py
>>> from operator import itemgetter
>>> rows_by_fname = sorted(rows, key=itemgetter('fname'))
[{'fname': 'Big', 'uid': 1004, 'lname': 'Jones'},
{'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'},
{'fname': 'David', 'uid': 1002, 'lname': 'Beazley'},
{'fname': 'John', 'uid': 1001, 'lname': 'Cleese'}]

>>> rows_by_uid = sorted(rows, key=itemgetter('uid'))
[{'fname': 'John', 'uid': 1001, 'lname': 'Cleese'},
{'fname': 'David', 'uid': 1002, 'lname': 'Beazley'},
{'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'},
{'fname': 'Big', 'uid': 1004, 'lname': 'Jones'}]
```

`sorted()` 函数的 `key` 是 `callable` 类型，负责从 `rows` 每个元素提取用来排序的值。这里 `itemgetter`就是用来创建 `callable` 对象。

`itemgetter` 支持多个 keys，返回 tuple 类型：

```py
>>> rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
[{'fname': 'David', 'uid': 1002, 'lname': 'Beazley'},
{'fname': 'John', 'uid': 1001, 'lname': 'Cleese'},
{'fname': 'Big', 'uid': 1004, 'lname': 'Jones'},
{'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'}]
```

`itemgetter` 也可以用 `lambda` 表达式代替。例如：

```py
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))
```

这个方法也不错，不过使用 `itemgetter()` 会稍微快点。

#### min, max

`min()` 和 `max()` 函数也有一个 `key` 参数，可以用 `itemgetter` 提供 `callable` 对象：

```py
>>> min(rows, key=itemgetter('uid'))
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
>>> max(rows, key=itemgetter('uid'))
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
```
