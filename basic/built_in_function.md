# Python 内置函数

- [Python 内置函数](#python-内置函数)
  - [总结](#总结)
    - [数学函数](#数学函数)
    - [字符串函数](#字符串函数)
  - [abs](#abs)
  - [ascii](#ascii)
  - [all](#all)
  - [any](#any)
  - [enumerate](#enumerate)
  - [filter](#filter)
  - [format](#format)
  - [getattr](#getattr)
  - [hasattr](#hasattr)
  - [int](#int)
  - [isinstance](#isinstance)
  - [len](#len)
  - [list](#list)
  - [map](#map)
  - [min](#min)
  - [ord](#ord)
  - [pow](#pow)
  - [print](#print)
  - [range](#range)
  - [reversed](#reversed)
  - [round](#round)
  - [sorted](#sorted)
    - [非原生比较对象排序](#非原生比较对象排序)
  - [type](#type)
  - [zip](#zip)
    - [无参数](#无参数)
    - [一个参数](#一个参数)
    - [多个参数](#多个参数)
    - [set 参数](#set-参数)
    - [参数长度不等](#参数长度不等)
    - [zip in Python 2](#zip-in-python-2)
    - [unzipping](#unzipping)
  - [参考](#参考)
  
Last updated: 2022-09-20, 15:00
***

## 总结

Python 解释器内置了许多函数，如下表所示：

|函数|功能|
|---|---|
| [abs(x)](#abs) | 对整数或浮点数返回绝对值；对复数，返回模|
| ascii(object)  | As `repr()`, return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by `repr()` using \x, \u or \U excapes. This generates a string similar to the returned by `repr|()` in Python 2. |
| dir(a_moduleName)     | 返回当前模块下所有定义的命名(方法和变量)   |
| enumerate() | 返回可迭代对象索引和对应数据  |
|[getattr](#getattr) |查询对象的属性值|
| globals()   | 以 dict 的形式返回当前 global names 及其值|
|[hasattr](#hasattr) |对象是否包含指定名称属性|
| float([x]) | |
| id()       | 返回一个Python对象的内存地址|
| int(str)   | 将字符串或另一个数转换为整数，截断，而不是四舍五入 |
| list()     | 创建一个新的空列表 |
| max(lst)   | 获得列表的最大值 |
| min(lst)   | 获得列表的最小值   |
| next()     | 返回一个可迭代数据结构中的下一项 |
| isinstance(object, class_type) | 验证变量是否是指定类型 |
| str.encode('coding')           | 将字符串转换为指定编码的字节|
| b'bytes'.decode('encoding')    | 以指定编码解析字节 |
| dir(a_var)                     | 列出变量所有的方法   |
| range(a, b)                    | 返回 [a, b-1] 之间的整数序列 |
| range(a)                       | 返回[0, a)之间的整数序列，返回 range 对象 |
| range(a, b, step)  | 以指定步长返回 [a, b)之间的整数序列  |
| sum(lst)           | 获得列表所有元素的加和    |

### 数学函数

| 方法     | 说明     |
| -------- | -------- |
| round(number[, ndigits]) | rounds the number, you can also specify precision | in the second argument |
| power(a, b)              | Return a raise to the power of b                  |

| max(x1, x2, …, xn)       | Return largest value among supplied arguments     |
| min(x1, x2, …, xn)       | Returns smallest value among supplied arguments   |


### 字符串函数

| 函数 | 说明   |
| ---- | ------ |
| ord()                    | 获得字符的编码（ASCII 编号）   |
| chr()                    | 将字符编码转换为字符           |
| a in b                   | a 是否是 b 的子字符串          |
| endswith(s1: str): bool  | true if strings ends with substring s1      |
| startwith(s1: str): bool | true if strings starts with substring s1    |
| count(s1: str): int      | number of occurrence of s1 in the string    |
| find(s1: str): int       | return lowest index from where s1 starts in the string, if string not found returns -1      |
| rfind(s1): int           | Returns the highest index from where s1 starts in the string, if string not found returns -1|
| capitalize(): str        | Returns a copy of this string with only the first character capitalized                     |
| lower(): str             | Return string by converting every character to lowercase                                    |
| upper(): str             | Return string by converting every character to uppercase                                    |
| title(): str             | This function return string by caplitalizing first letter of every word in the string       |
| swapcase(): str          | Return a string in which the lowercase letter is converted to uppercase and uppercase to lowercase |
| replace(old, new): str   | This function returns new string by replacing the occurrence of old string with new string         |
| isalnum()                | true, 字母数字      |
| isalpha()                | true, 只有字母      |
| isdigit()                | true, 为数字        |
| isidentifier()           | true, 有效标识符    |
| islower()                | 为小写              |
| isupper()                | 为大写              |
| isspace                  | 为空格              |
| len(a_str)               | 获得字符串长度      |
| max()                    | 返回编码ASCII 值最大的字符  |
| min()                    | 返回编码ASCII值最小的字符   |
| str()                    | 创建一个空字符串            |
| map                      | 以 iterable 和 function 为参数，将 function 作用在 iterable 对象上，返回一个新的 iterable对象 |
| filter                   | 以 predicate 函数和 iterable 为参数，过滤 iterable 后返回一个新的 iterable |

## abs

```python
abs(x)
```

如果 x 为整数或浮点数，返回数值的绝对值；若为复数，返回模；也可以是实现 `__abs__()` 的对象。

- 对数值，返回绝对值

```python
integer = -20
assert abs(integer) == 20

floating = - 30.33
assert abs(floating) == 30.33
```

- 对复数，返回模

```python
complex = (3 - 4j)
assert abs(complex) == 5
```

- 如果 `x` 定义了 `__abs__()` 函数，`abs(x)` 返回 `x.__abs__()`.


## ascii

[`ascii(object)`](../src/python_test/builtin_func/ascii_test.py)

功能和 `repr()` 类似，返回对象可打印形式的字符串表示，但是对 `repr()` 返回字符串中的非 ASCII 字符，使用 `\x`, `\u` 或 `\U` 进行转义。和 Python 2 中 `repr()` 返回的字符串类似。


## all

如果 `iterable` 的所有元素为 true，返回 `True`。等价于：

```py
def all(iterable):
  for element in iterable:
    if not element:
      return False
  return True
```

如果可迭代对象为空，也返回 True。

- list 实例

```python
l = [1, 3, 4, 5]
assert all(l)

l.append('') # 空字符串为 false
assert not all(l)

# all values false
l = [0, False]
assert not all(l)

# one false value
l = [1, 3, 4, 0]
assert not all(l)

# one true value
l = [0, False, 5]
assert not all(l)

# empty iterable
assert all([])
```

- tuple 实例

```python
t = ('Tuple')
assert all(t)

t1 = ('Tuple', '')
assert not all(t1)
```

## any

`iterable` 的任意对象为 true，返回 `True`。如果 iterable 为空，返回 `False`。等价于：

```py
def any(iterable):
  for element in iterable:
    if element:
      return True
  return False
```

- list 实例

```python
# 空 list，或其中全是 0 或 False，返回 False
lst = ['', 0, False, 0.0, None]
assert not any(lst)

l = [1, 3, 4, 0]
assert any(l)

l = [0, False]
assert not any(l)

l = [0, False, 5]
assert any(l)

assert not any([])
```

## enumerate

`enumerate()` 方法给 iterable 对象添加了一个计数器。语法：

`enumerate(iterable, start=0)`

- `iterable`，支持迭代的任意对象
- `start`，其实计数值，默认 **0**

返回 `enumerate` 对象，可以使用 `list()` 和 `tuple()` 等转换为其它序列对象。

## filter

`filter(function, iterable)`

返回一个迭代器，迭代所有 `function` 函数计算结果为 true 的 `iterable` 元素。

如果 `function` 为 `None`，则为 `identity` 函数。

## format

`format(value[, format_spec])`

根据 `format_spec` 将 `value` 转换为格式化表示形式。

`format_spec` 的解析依赖于 `value` 的类型。

`format_spec` 默认为空字符串，结果等效于 `str(value)`。

调用 `format(value, format_spec)` 被转换为 `type(value.__format__(value, format_spec))`，在搜索 `value` 的 `__format__()` 方法时，直接跳过了实例字典。

## getattr

```python
getattr(object, name[, default])
```

返回 `object` 的命名属性的值，`name` 为 string 类型。

- 如果 `name` 是 `object` 的属性名称，返回属性值。例如 `getattr(x, 'foobar')` 等价于 `x.foobar`
- 如果 `object` 没有名称为 `name` 的属性，如果设置了 `default`，则返回 `default`，否则抛出 `AttributeError`。

## hasattr

```python
hasattr(object, name)
```

`object` 参数为一个对象，`name` 为字符串。如果 `object` 包含名称为 `name` 的 attribute，返回 True，否则返回 False。

通过 `getattr(object, name)` 实现，通过是否抛出 `AttributeError` 判断。

## int

```py
int([x])
int(x, base=10)
```

参数：

- `x` ，可以转换为整数的数值或字符串；
- `base` ，数值格式，默认为 10 进制。

`int()` 函数将指定值转换为整数类型：

- 将数字或字符串 `x` 转换为 integer 对象，如果不提供参数，返回 `0`。
- 如果 `x` 定义了 `__int__()`，`int(x)` 返回 `x.__int__()`
- 如果 `x` 定义了 `__index__()`，返回 `x.__index__()`
- 如果 `x` 定义了 `__trunc__()`，返回 `x.__trunc__()`
- 如果 `value` 是浮点数，则向零取整。

如果 x 不是数字，或者提供了 `base` 参数，则 `x` 必须为 string, `bytes` 或 `bytearray`。

字符串：

```python
x = int('12')
assert x == 12
```

## isinstance

`isinstance()` 检查对象是否为指定类型的实例。语法：

```py
isinstance(object, classinfo)
```

| 参数      | 说明                                      |
| --------- | ----------------------------------------- |
| Object    | 待检查对象                                |
| classinfo | class, type, or tuple of clases and types |

- 类测试

```py
class Foo:
    a = 5


def test_param():
    foo_ins = Foo()
    assert isinstance(foo_ins, Foo)
    assert not isinstance(foo_ins, (list, tuple))
    assert isinstance(foo_ins, (list, tuple, Foo))
```

只要实例是 tuple 中任意一个类型的实例，返回 `true`.

- 基本类型测试

```py
def test_native():
    numbers = [1, 2, 3]

    assert isinstance(numbers, list)
    assert not isinstance(numbers, dict)
    assert isinstance(numbers, (dict, list))

    number = 5
    assert not isinstance(number, list)
    assert isinstance(number, int)
```

## len

返回对象长度，即对象包含的元素个数。对象类型可以是序列（如字符串、字节、元祖、列表或 range）或集合（如 dict, set）。语法：

```python
len(object)
```

- 列表长度

```python
mylist = ['apple', 'banana', 'cherry']
assert len(mylist) == 3
```

- 字符串长度

```python
s = 'Hello'
assert len(s) == 5
```

## list

## map

```py
map(function, iterable, ...)
```

将函数依次应用于 `iterable` 对象的元素，将返回的值作为迭代器返回。

`map` 函数使得将函数应用到多个元素的操作更为简洁，例如，取每个值的平方：

```py
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
```

如果用 `map` 函数：

```py
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```

如果提供多个 `iterable` 对象，则 `function` 参数个数要和 `iterable` 个数相同，然后 `function` 并行应用于所有元素。

对多个 `iterables`，迭代器在最短的迭代对象耗尽时结束。

例如：

```py
def square(x):
    return x ** 2


def test_map():
    val = map(square, [1, 2, 3])
    assert list(val) == [1, 4, 9]


def plus(a, b):
    return a + b


def test_map_2():
    val = map(plus, [1, 2, 3], [4, 5, 6])
    assert list(val) == [5, 7, 9]
```

## min

```py
min(iterable, *[, key, default])
min(arg1, arg2, *args[, key])
```

返回 `iterable` 或多个参数中的最小项。

- 如果只提供了一个位置参数，则必须为 `iterable` 类型。返回其最小项。
- 如果提供了多个位置参数，则返回最小的位置参数。

有两个可选的关键字参数。

- `key` 用于指定排序函数，和 `list.sort()` 函数使用的参数类似
- `default` 指定 `iterable` 为空时返回的对象。

如果不提供 `default` 且 `iterable` 为空，抛出 `ValueError`。

如果出现多个相同的最小值，返回第一次出现的值。

## ord

```python
ord(c)
```

对一个 Unicode 字符，返回该字符的 Unicode 整数编码。例如，`ord('a')` 返回整数 97，`ord('€')` 返回 8364.

`ord` 是 `chr()` 的逆操作。

## pow

[`pow(base, exp[, mod])`](../src/python_test/builtin_func/pow_test.py)

返回 `base` 的 `exp` 指数；如果指定 `mod`，则对指数结果相对 `mod` 取模，效率比 `pow(base, exp) % mod` 高。

两个参数的形式 `pow(base, exp)` 等价于 `base ** exp`。

参数必须为数字类型。对混合参数类型，规则和二进制算数运算规则相同。对 `int` 操作数，如果第二个参数为 `int`，结果为 `int` 类型；如果第二个参数为负数，所有参数转换为 `float`，返回浮点数类型。例如：`10**2=100`, `10*-2=0.01`。

- 指定 `mod`

`mod` 必须为非零整数。如果 `exp` 为负，则


## print

参考 [IO 部分](../io/python_io.md#print)。

## range

range 用于生成 immutable 整数序列，一般用在 for 循环中指定循环次数。`range` 也是一种序列类型。方法签名：

```py
class range(stop)
class range(start, stop[, step])
```

- 例：生成 1 到 10 之间的整数序列，`step` 默认为 1

```py
  seq = list(range(1, 10))
  assert len(seq) == 9
  assert seq == list([1, 2, 3, 4, 5, 6, 7, 8, 9])
```

- 起始值 `start` 默认为 0

```py
  seq = list(range(10))
  assert len(seq) == 10
  assert seq == list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

- 通过 `step` 指定步长

```py
seq = list(range(2, 14, 2))
assert len(seq) == 6
assert seq == list([2, 4, 6, 8, 10, 12])
```

- 如果 step 为 0，抛出 `ValueError`

```py
with pytest.raises(ValueError):
    range(1, 10, 0)
```

- 如果 step 为负值，序列指可以通过 $r[i] = start + step*i$ 计算

```py
seq = list(range(0, -10, -1))
assert seq == [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
```


## reversed

`reversed()`函数返回序列的**反向迭代器**。

`reversed(seq)`

序列是支持序列协议：`__len__()` 和 `__getitem__()` 方法。例如 `tuple`, `string`, `list`, `range` 等。

也可以对实现 `__reverse__()` 方法的对象使用 `reversed(seq)`。

例如，用于字符串：

```py
seq = 'Python'
a = list(reversed(seq))
assert a == ['n', 'o', 'h', 't', 'y', 'P']
```

用于 tuple:

```py
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
a = list(reversed(seq_tuple))
assert a == ['n', 'o', 'h', 't', 'y', 'P']
```

用于实现 `__reverse__()` 的对象：

```py
class Vowerls:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __reversed__(self):
        return reversed(self.vowels)


def test_object():
    v = Vowerls()
    a = list(reversed(v))
    assert a == ['u', 'o', 'i', 'e', 'a']
```

## round

`round(number[, ndigits])`

舍入到小数点后 `ndigits` 位精度。

- 如果未提供 `ndigits`，或者为 `None`，返回最近的整数
- 对支持 `round()` 的内置类型，四舍五入到最接近的值；如果两边的值相等，选择偶数，例如 `round(0.5)` 和 `round(-0.5)` 为 0，`round(1.5)` 为 2.
- `ndigits` 为整数类型
- 如果未提供 `ndigits` 或为 `None`，则返回整数；否则返回类型和 `number` 相同。

如果 `number` 为常规 Python 类型，`round` 调用 `number.__round__。

> `round()` 对浮点数的舍入行为有时候可能出乎意料：例如 `round(2.675, 2)` 结果为 `2.67` 而不是 `2.68`，这是因为浮点数无法完全表示小数位数。

## sorted

Last updated: 2022-07-21, 14:12

```python
sorted(iterable, /, *, key=None, reverse=False)
```

将 `iterable` 中的元素排序后，放入一个新的 list 返回。有两个可选参数：

- `key` 用来指定包含单个参数的函数，用来从元素中提取用于比对的信息，例如 `key=str.lower`，默认为 `None`，即直接比对元素。
- `reverse` boolean 参数，设置为 `True` 表示反向排序。

`sorted()` 函数是稳定的。排序算法稳定的意思是，不改变相等元素原来的顺序。

排序算法仅使用 `<` 比较元素。虽然只定义 `__lt__()` 方法就可以排序，但是 PEP8 建议实现所有 6 个比较（`<`, `>`, `==`, `>=`, `<=`, `!=`）。这样可以避免相同数据在依赖不同底层方法的排序工具（如 `max()`）中出现 bugs。实现所有 6 个比较方法还有助于避免混淆混合类型比较。

```py
py_list = ['e', 'a', 'u', 'o', 'i']
sorted_list = sorted(py_list)
assert sorted_list == ['a', 'e', 'i', 'o', 'u']
```

> list 也有 `sort()` 方法，效果和 `sorted()` 类似，差别是，不返回值，list 是原位排序。

### 非原生比较对象排序

对不支持原生比较对象的排序，可以将 `callable` 对象传递给 `key` 参数。`callable` 对象对每个传入的元素返回一个值，`sorted()` 函数根据该值排序元素。

假设你需要对 `User` 实例排序，如下：

```py
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(3), User(1), User(9)]
sorted_users = sorted(users, key=lambda u: u.user_id)
assert sorted_users[0].user_id == 1
assert sorted_users[1].user_id == 3
assert sorted_users[2].user_id == 9
```

还可以使用 `operator.attrgetter()` 代替 lambda 函数：

```py
>>> from operator import attrgetter
>>> sorted(users, key=attrgetter('user_id'))
[User(3), User(23), User(99)]
```

而且 `operator.attrgetter()` 通常会快一点，并且还能同时允许多个字段进行比较。

## type

`type()` 函数有两种形式：

```python
type(object) # 返回参数类型
type(name, bases, dict) # 创建一个新的类型
```

- 单个参数返回参数类型，例如：

```python
number_list = [1, 2]
assert type(number_list) == list
number_dict = {1: 'one', 2: 'two'}
assert type(number_dict) == dict

assert type([]) is list
assert type(()) is tuple
assert type({}) is dict

class Foo:
    a = 0

foo = Foo()
assert type(foo) == Foo
```

建议使用 `isinstance()` 查看对象类型，因为它考虑了子类。 `type()` 判断类型比较严格，不认为子类是父类类型；而 `isinstance()` 则会认为子类是父类类型。例如：

```python
class Shape():
    pass

class Circle(Shape):
    pass

assert type(Shape()) == Shape
assert not (type(Circle()) == Shape)
assert isinstance(Circle(), Shape)
```

`Circle` 是 `Shape` 子类，然而 `type(Circle()) == Shape` 为 `False` 。所以在判断类型上，用 `isinstance` 更合适。

- 创建新类型

返回一个新的 `type` 对象，这是 `class` 语句的动态形式。

| 参数 | 说明 |
| --- | --- |
| name | 类名，对应 `__name__` 属性 |
| bases | tuple 类型，逐项列出基类，对应 `__bases__` 属性 |
| dict | dict 类型，包含类型定义的主体，对应 `__dict__` 属性 |

例如：

```python
o1 = type('X', (object,), dict(a='Foo', b=12))
assert type(o1) == type
```


## zip

`zip(*iterables)`

将多个 iterable 对象聚合在一起构成一个迭代器。

返回 tuple 迭代器。

可以传入任意数目的 iterable 对象：

- 第 i 个 tuple 包含所有iterable对象的第 i 个元素。当最短的iterable对象耗尽，迭代器停止。
- 无参数，返回空 iterator。
- 一个参数，返回的iterator 的 tuple 长度为1。
- 多个参数，tuple 长度为iterable参数个数。

对 lists, tuples, strings 等可迭代对象，迭代的顺序保持不变。

### 无参数

无参数，返回空 iterator

```py
zipped = zip()
l = list(zipped)
assert l == []
```

`zip()` 只迭代到最短对象的长度，如果不希望截断，可以使用 `itertools.zip_longest()`。

### 一个参数

一个参数，返回的 iterator 的 tuple 长度为1.

```py
a = [1, 2, 3]
zipped = zip(a)
l = list(zipped)
assert l[0] == (1,)
assert l[1] == (2,)
assert l[2] == (3,)
```

### 多个参数

```py
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
zips = list(zipped)
assert zips[0] == (1, 'a')
assert zips[1] == (2, 'b')
assert zips[2] == (3, 'c')
```

### set 参数

对 set 顺序无法保证

```py
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
l1 = list(zip(s1, s2))
print(l1)
```

Out:

```cmd
[(1, 'c'), (2, 'a'), (3, 'b')]
```

### 参数长度不等

如果参数长度不等，`zip()` 返回元素的个数和最短的iterable长度相同。哪些较长 iterable 参数余下元素忽略。例如：

```py
l = list(zip(range(3), range(100)))
assert len(l) == 3
assert l[0] == (0, 0)
assert l[1] == (1, 1)
assert l[2] == (2, 2)
```

### zip in Python 2

在 Python 2中，`zip()` 返回 tuple `list`。`list` 长度和输入最短的 iterable 对象相同。如果无输入参数，返回空 `list`。

而 Python 3 中，`zip()` 返回的是 iterator。使用 iterator 的好处是在需要时才生成数据，内存占用更少。

### unzipping

有 `zip()` 函数，为什么没有 `unzip()` 函数。因为`zip` 和 `*` 结合就实现了 unzip 功能。

假如你有一个 tuple 列表，然后你希望将 tuple 分解，获得独立的列表。实现方式如下：

```py
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
assert numbers == (1, 2, 3, 4)
assert letters == ('a', 'b', 'c', 'd')
```

## 参考

- [Built-in Functions](https://docs.python.org/3/library/functions.html)
