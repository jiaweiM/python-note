# dict

- [dict](#dict)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [可哈希对象](#%e5%8f%af%e5%93%88%e5%b8%8c%e5%af%b9%e8%b1%a1)
  - [创建字典](#%e5%88%9b%e5%bb%ba%e5%ad%97%e5%85%b8)
  - [方法](#%e6%96%b9%e6%b3%95)
    - [list](#list)
    - [len](#len)
    - [d[key]](#dkey)
    - [d[key] = value](#dkey--value)
    - [del d[key]](#del-dkey)
    - [key in d](#key-in-d)
    - [iter(d)](#iterd)
    - [clear](#clear)
    - [copy](#copy)
    - [fromkeys](#fromkeys)
    - [get](#get)
    - [items](#items)
    - [keys](#keys)
    - [pop](#pop)
    - [popitem](#popitem)
    - [reversed(d)](#reversedd)
    - [setdefault](#setdefault)
    - [update](#update)
    - [values](#values)
  - [视图](#%e8%a7%86%e5%9b%be)
  - [应用](#%e5%ba%94%e7%94%a8)
    - [映射多个值](#%e6%98%a0%e5%b0%84%e5%a4%9a%e4%b8%aa%e5%80%bc)
    - [运算](#%e8%bf%90%e7%ae%97)
    - [字典集合操作](#%e5%ad%97%e5%85%b8%e9%9b%86%e5%90%88%e6%93%8d%e4%bd%9c)

***

## 简介

保存键值对的集合类型， mutable.

键必须可计算哈希值，值则可为任意类型。

python 字典会保留插入时的顺序。对键的更新不会影响顺序。删除并再次添加的键将被插入到末尾。

## 可哈希对象

一个对象的哈希值（实现 `__hash__()` 方法）如果在生命周期内不改变，称其为可哈希对象，且可以和其它对象比较（实现 `__eq__()` 方法）。可哈希对象如果相等，两者的哈希值必然相同。

可哈希对象才能作为 dict 的键和 set 成员，这两个集合对象内部都使用哈希值。

Python 哈希支持：

- Python 内置的大部分 immutable 对象是可哈希的；
- mutable 容器（如 list, dict）不支持哈希；
- 对immutable 容器（如 tuple, frozenset）如果其元素支持哈希，它们也支持哈希。
- 用于自定义对象默认支持哈希，它们的哈希值从 `id()` 得到，除了自身，和任何对象对比都是 unequal。

## 创建字典

构造函数：

```py
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
```

使用可选的位置参数和可能为空的关键字参数初始化字典。

- 如果没有位置参数，将创建一个空字典。
- 如果给出一个位置参数并且是映射对象，将创建一个具有与映射对象相同键值对的字典。
- 如果位置参数不是映射对象，则必须是 `iterable` 对象，且该可迭代对象中的每一项必须是包含两个元素的可迭代对象。每一项的第一个为键，第二个为值。 如果一个键出现多次，该键的最后一个值将成为其在新字典中对应的值。
- 如果给出了关键字参数，则关键字参数及其值会被加入到基于位置参数创建的字典。如果要加入的键已存在，则来自关键字参数的值将覆盖来自位置参数的值。

下面以多种方式创建字典 `{"one": 1, "two": 2, "three": 3}`:

```py
>>> a = dict(one=1, two=2, three=3) # 关键字参数
>>> b = {'one': 1, 'two': 2, 'three': 3} # 直接创建
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3])) # 可迭代对象位置参数
>>> d = dict([('two', 2), ('one', 1), ('three', 3)]) # 可迭代对象位置参数
>>> e = dict({'three': 3, 'one': 1, 'two': 2}) # 映射对象位置参数
>>> a == b == c == d == e
True
```

大括号 {} 创建字段，不同元素以逗号分开。

```py
friends = {
  'tom' : '111-222-333',
  'jerry': '666-33-111'
}
```

## 方法

### list

`list(d)`

返回字典 d 所有key的列表。例如：

```py
d = {"one": 1, "two": 2, "three": 3, "four": 4}
keys = list(d)
assert keys == ['one', 'two', 'three', 'four']
```

字典会保持元素插入时的顺序，对键的更新不影响顺序。

### len

`len(d)`

字典 `d` 中元素的个数。

```py
d = {1: 'apple', 2: 'ball'}
assert len(d) == 2
```

### d[key]

返回键对应的值：

```py
d['key']
```

如果对应键不存在，抛出 `KeyError`。

如果字典的子类定义了 `__missing__()` 方法并且 `key` 不存在，则 `d[key]` 将调用该方法。如果未定义 `__missing__()`，抛出 `KeyError`。

例如：

```py
>>> class Counter(dict):
...     def __missing__(self, key):
...         return 0
>>> c = Counter()
>>> c['red']
0
>>> c['red'] += 1
>>> c['red']
1
```

这是 `collections.Counter` 实现的部分代码。

### d[key] = value

添加或修改值，将 `d[key]` 设为 value。

```py
d[key] = value
```

### del d[key]

删除值：如果找到键，删除，如果没找到，抛出 KeyError

```py
del d['key']
```

### key in d

`key in d`

如果 d 中存在键 key，则返回 `True`，否则返回 `False`

`key not in d`

等价于 `not key in d`

### iter(d)

返回字典键的迭代器，等价于 `iter(d.keys())`。

### clear

删除字典所有元素。

### copy

`copy()`

返回字典的浅拷贝。

### fromkeys

`classmethod fromkeys(iterable[, value])`

使用来自 `iterable` 的键创建一个新字典，并将键值设为 `value`。

`fromkeys()` 是类方法，创建一个新的字典。 `value` 默认为 `None`。 所有值都只引用一个单独的实例，因此让 value 成为一个可变对象例如空列表通常是没有意义的。要获取不同的值，使用字典推导式。

### get

`get(key[, default])`

如果字典中存在 `key`，返回其值，否则返回 `default`，如果未设置 `default`，返回 `None`。所以这个方法不抛出 `KeyError`。

### items

返回包含字典 `(key, value)` 对的新视图。

### keys

返回包含字典 keys 的视图。

### pop

`pop(key[, default])`

如果字典中包含 `key`，移除并返回其值，否则返回 `default`。

如果未指定 `default`，且字典中不包含 `key`，抛出 `KeyError`。

### popitem

从字典中移除并返回一个 `(key, value)` 对。键值对按 LIFO 的顺序返回。

popitem() 适用于对字典进行消耗性的迭代。如果字典为空，调用 `popitem()` 将引发 `KeyError`。

### reversed(d)

返回一个逆序字典键的迭代器。为 reversed(d.keys()) 的快捷方式。

### setdefault

`setdefault(key[, default])`

如果字典存在 `key` ，返回其值。如果不存在，插入 `(key, default)` 并返回 default 。 default 默认为 `None`。

### update

`update([other])`

使用来自 `other` 的键/值对更新字典，覆盖原有的键。

返回 `None`。

`update()` 接受另一个字典对象，或者包含键/值对（长度为2的元组或其它可迭代对象）的可迭代对象。 如果给出了关键字参数，则会以其所指定的键/值对更新字典: `d.update(red=1, blue=2)`。

### values

返回由字典值组成的视图。

```py
sales = {'apple': 2, 'orange': 3, 'grapes': 4}
assert list(sales.values()) == [2, 3, 4]
sales['apple'] = 5
assert list(sales.values()) == [5, 3, 4]
```

两个 `dict.values()` 视图之间的相等性比较将总是返回 `False`。 这在 `dict.values()` 与其自身比较时也同样适用:

```py
>>> d = {'a': 1}
>>> d.values() == d.values()
False
```

两个字典的比较当且仅当它们具有相同的 (键, 值) 对时才会相等（不考虑顺序）。 排序比较 ('<', '<=', '>=', '>') 会引发 TypeError。

## 视图

`dict.keys()`, `dict.values` 和 `dict.items()` 返回对象视图。视图对象为字典的动态视图，随着字典的改变而改变。

字典视图可以被迭代，也支持成员检测。

len(dictview)，返回字典中的条目。

## 应用

### 映射多个值

字典一个键映射一个值，如果要映射多个值，就需要将多个值放到另外的容器，比如列表或者set中。例如：

```py
d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}
e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}
```

选择使用列表还是集合取决于实际需求。如果想保持元素的插入顺序，就使用列表，如果要去掉重复元素，就使用集合。

也可以使用 `collections` 的 `defaultdict` 构造这样的词典。

`defaultdict` 使用更方便，具体参考 [collections.defaultdict](../api/collections_defaultdict.md)。

### 运算

比如要计算字典值的最小值、最大值、排序等。

考虑下面的股票名和价格映射字典：

```py
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
```

- 如果对字典执行数学运算，它仅仅作用于键，而不是值，例如：

```py
min(prices) # Returns 'AAPL'
max(prices) # Returns 'IBM'
```

这个结果并不是我们想要的，因为我们想在字典的值集合上执行这些计算。

- 我们可以使用 `values()` 方法解决这个问题：

```py
min(prices.values()) # Returns 10.75
max(prices.values()) # Returns 612.78
```

但是这种方式不知道对应的键的信息。

我们可以在 `min()` 和 `max()` 函数中提供 `key` 参数来获取最大值或最小值对应的键的信息。比如：

```py
min(prices, key=lambda k: prices[k]) # Returns 'FB'
max(prices, key=lambda k: prices[k]) # Returns 'AAPL'
```

如果想要得到最小值，需要再执行一次查找操作：

```py
min_value = prices[min(prices, key=lambda k: prices[k])]
```

- 最简洁的方式是使用 `zip()` 函数

先用 `zip()` 将键和值反转过来。比如，下面查找最小和最大股票价格及其名称：

```py
min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')
```

在比较元祖时，值会先进行比较，然后才是键。这样就能通过一条简单的语句实现字典上求极值和排序操作。

类似的，可以使用 `zip()` 和 `sorted()` 函数排列字典数据：

```py
prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]
```

执行这些计算的时候需要注意，`zip()` 函数创建的是一个只能访问一次的迭代器。比如，下面的代码会出错：

```py
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # OK
print(max(prices_and_names)) # ValueError: max() arg is an empty sequence
```

另外需要注意的是，如果最大值或最小值有重复，结果会根据键的排序返回：

```py
>>> prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
>>> min(zip(prices.values(), prices.keys()))
(45.23, 'AAA')
>>> max(zip(prices.values(), prices.keys()))
(45.23, 'ZZZ')
```

### 字典集合操作

字典的 `keys()` 返回键视图对象。键视图支持集合操作，包括并、交、差集等运算。

字典的 `items()` 返回包含（键，值）对元素视图对象。这个对象同样支持集合操作。

字典的 `values()` 返回虽然也是视图对象，但是不支持集合操作。

考虑下面两个字典：

```py
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}
```

通过 `keys()` 或者 `items()` 方法返回结果执行集合操作。比如：

```py
# keys 交集
a.keys() & b.keys() # { 'x', 'y' }
# keys 差集
a.keys() - b.keys() # { 'z' }
# (key, value) 交集
a.items() & b.items() # { ('y', 2) }
```

这些结果可用来修改或过滤字典。比如，移除指定键：

```py
# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}
```
