# operator

- [operator](#operator)
  - [简介](#简介)
  - [对象比较函数](#对象比较函数)
  - [逻辑运算函数](#逻辑运算函数)
  - [数学运算符](#数学运算符)
  - [查找方法](#查找方法)
    - [attrgetter](#attrgetter)
      - [查询单个属性](#查询单个属性)
      - [查询多个属性](#查询多个属性)
      - [带点号查询](#带点号查询)
    - [itemgetter](#itemgetter)
      - [根据某个关键字排序字典](#根据某个关键字排序字典)
      - [min, max](#min-max)
  - [methodcaller](#methodcaller)
  - [参考](#参考)

2021-06-16, 09:20
@author Jiawei Mao
***

## 简介

`operator` 模块定义了一系列和 Python 运算符对应的函数。例如 `operator.add(x, y)` 等效于 `x+y`。许多函数名是用于特殊方法的名称，没有双下划线。为了向后兼容，其中许多还保留双下划线版本。

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

比价函数可能返回任何值，不一定是布尔值。

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

```py
operator.attrgetter(attr)
operator.attrgetter(*attrs)
```

`attrgetter` 和 `itemgetter` 类似，它创建函数根据名称提取属性。返回一个 `callable` 对象，该对象从其操作数中提取 `attr`。如果查询多个属性，返回 tuple 类型。属性名称可以包含点号。

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

```py
operator.itemgetter(item)
operator.itemgetter(*items)
```

返回一个 `callable` 对象，该对象使用操作数的 `__getitem__()` 方法从操作数中获得对应项。如果指定了多项，返回 tuple。例如

- 设置 `f = itemgetter(2)`，调用 `f(r)` 返回 `r[2]`
- 设置 `g = itemgetter(2, 5, 3)`，调用 `g(r)` 返回 `(r[2], r[5], r[3])`

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

其中 `items` 可以是任何 `__getitem__()` 接受的参数。对 dict 可以是任何 hashable 值。对 list, tuple 和 string 可以是索引和切片：

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

## methodcaller

```py
operator.methodcaller(name, /, *args, **kwargs)
```

返回一个可调用对象，该对象在其操作数上调用方法名。如果提供了额外的参数，则作为调用方法的参数。例如：

- 设置 `f = methodcaller('name')`，则调用 `f(b)` 等价于 `b.name()`；
- 设置 `f = methodcaller('name', 'foo', bar=1)`，则调用 `f(b)` 等价于 `b.name('foo', bar=1)`

该方法等价于：

```py
def methodcaller(name, /, *args, **kwargs):
    def caller(obj):
        return getattr(obj, name)(*args, **kwargs)
    return caller
```

## 参考

- https://docs.python.org/3/library/operator.html
