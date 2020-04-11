# Python 内置函数

- [Python 内置函数](#python-%e5%86%85%e7%bd%ae%e5%87%bd%e6%95%b0)
  - [基本函数](#%e5%9f%ba%e6%9c%ac%e5%87%bd%e6%95%b0)
  - [字符串函数](#%e5%ad%97%e7%ac%a6%e4%b8%b2%e5%87%bd%e6%95%b0)
  - [数学函数](#%e6%95%b0%e5%ad%a6%e5%87%bd%e6%95%b0)
  - [abs](#abs)
  - [all](#all)
  - [any](#any)
  - [ascii](#ascii)
  - [enumerate](#enumerate)
  - [int](#int)
  - [min](#min)
  - [pow](#pow)
  - [print](#print)
  - [range](#range)
  - [round](#round)
  - [sorted](#sorted)
  - [reversed](#reversed)
  - [zip](#zip)
    - [无参数](#%e6%97%a0%e5%8f%82%e6%95%b0)
    - [一个参数](#%e4%b8%80%e4%b8%aa%e5%8f%82%e6%95%b0)
    - [多个参数](#%e5%a4%9a%e4%b8%aa%e5%8f%82%e6%95%b0)
    - [set 参数](#set-%e5%8f%82%e6%95%b0)
    - [参数长度不等](#%e5%8f%82%e6%95%b0%e9%95%bf%e5%ba%a6%e4%b8%8d%e7%ad%89)
    - [zip in Python 2](#zip-in-python-2)
    - [unzipping](#unzipping)
  - [type()](#type)
    - [type(object)](#typeobject)
    - [type(name, bases, dict)](#typename-bases-dict)
  - [isinstance](#isinstance)

## 基本函数

| 内置函数                       | 说明                                                                                                                                                                                                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| abs(x)                         | 返回数值的绝对值，x 为整数或浮点数。若为复数，返回模                                                                                                                                                                                                          |
| all(iterable)                  | Return True if all elements of the iterable are true (or if the                                                                                                                                                                                               | iterable is empty)               |
| any(iterable)                  | Return True if any element of the `iterable` is true. If the                                                                                                                                                                                                  | iterablbe is empty, return False |
| ascii(object)                  | As `repr()`, return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by `repr()` using \x, \u or \U excapes. This generates a string similar to the returned by `repr|()` in Python 2. |
| dir(a_moduleName)              | 返回当前模块下所有定义的命名(方法和变量)                                                                                                                                                                                                                      |
| enumerate()                    | 返回可迭代对象索引和对应数据                                                                                                                                                                                                                                  |
| globals()                      | 以 dict 的形式返回当前 global names 及其值                                                                                                                                                                                                                    |
| float([x])                     |                                                                                                                                                                                                                                                               |
| id()                           | 返回一个Python对象的内存地址                                                                                                                                                                                                                                  |
| int(str)                       | 将字符串或另一个数转换为整数，截断，而不是四舍五入                                                                                                                                                                                                            |
| list()                         | 创建一个新的空列表                                                                                                                                                                                                                                            |
| max(lst)                       | 获得列表的最大值                                                                                                                                                                                                                                              |
| min(lst)                       | 获得列表的最小值                                                                                                                                                                                                                                              |
| next()                         | 返回一个可迭代数据结构中的下一项                                                                                                                                                                                                                              |
| type()                         | 获得数据或变量类型                                                                                                                                                                                                                                            |
| isinstance(object, class_type) | 验证变量是否是指定类型                                                                                                                                                                                                                                        |
| str.encode('coding')           | 将字符串转换为指定编码的字节                                                                                                                                                                                                                                  |
| b'bytes'.decode('encoding')    | 以指定编码解析字节                                                                                                                                                                                                                                            |
| len(str)                       | 计算字符串长度                                                                                                                                                                                                                                                |
| dir(a_var)                     | 列出变量所有的方法                                                                                                                                                                                                                                            |
| range(a, b)                    | 返回 [a, b-1] 之间的整数序列                                                                                                                                                                                                                                  |
| range(a)                       | 返回[0, a)之间的整数序列，返回 range 对象                                                                                                                                                                                                                     |
| range(a, b, step)              | 以指定步长返回 [a, b)之间的整数序列                                                                                                                                                                                                                           |
| sum(lst)                       | 获得列表所有元素的加和                                                                                                                                                                                                                                        |

## 字符串函数

| 函数                     | 说明                                                                                               |
| ------------------------ | -------------------------------------------------------------------------------------------------- |
| ord()                    | 获得字符的编码（ASCII 编号）                                                                       |
| chr()                    | 将字符编码转换为字符                                                                               |
| a in b                   | a 是否是 b 的子字符串                                                                              |
| endswith(s1: str): bool  | true if strings ends with substring s1                                                             |
| startwith(s1: str): bool | true if strings starts with substring s1                                                           |
| count(s1: str): int      | number of occurrence of s1 in the string                                                           |
| find(s1: str): int       | return lowest index from where s1 starts in the string, if string not found returns -1             |
| rfind(s1): int           | Returns the highest index from where s1 starts in the string, if string not found returns -1       |
| capitalize(): str        | Returns a copy of this string with only the first character capitalized                            |
| lower(): str             | Return string by converting every character to lowercase                                           |
| upper(): str             | Return string by converting every character to uppercase                                           |
| title(): str             | This function return string by caplitalizing first letter of every word in the string              |
| swapcase(): str          | Return a string in which the lowercase letter is converted to uppercase and uppercase to lowercase |
| replace(old, new): str   | This function returns new string by replacing the occurrence of old string with new string         |
| isalnum()                | true, 字母数字                                                                                     |
| isalpha()                | true, 只有字母                                                                                     |
| isdigit()                | true, 为数字                                                                                       |
| isidentifier()           | true, 有效标识符                                                                                   |
| islower()                | 为小写                                                                                             |
| isupper()                | 为大写                                                                                             |
| isspace                  | 为空格                                                                                             |
| len(a_str)               | 获得字符串长度                                                                                     |
| max()                    | 返回编码ASCII 值最大的字符                                                                         |
| min()                    | 返回编码ASCII值最小的字符                                                                          |
| str()                    | 创建一个空字符串                                                                                   |
| map                      | 以 iterable 和 function 为参数，将 function 作用在 iterable 对象上，返回一个新的 iterable对象      |
| filter                   | 以 predicate 函数和 iterable 为参数，过滤 iterable 后返回一个新的 iterable                         |

## 数学函数

| 方法                     | 说明                                              |
| ------------------------ | ------------------------------------------------- |
| round(number[, ndigits]) | rounds the number, you can also specify precision | in the second argument |
| power(a, b)              | Return a raise to the power of b                  |
| abs(x)                   | 对整数或浮点数返回绝对值；对复数，返回模          |
| max(x1, x2, …, xn)       | Return largest value among supplied arguments     |
| min(x1, x2, …, xn)       | Returns smallest value among supplied arguments   |

## abs

[`abs(x)`](../src/python_test/builtin_func/abs_test.py)

计算绝对值。

`x` 可以为整数或浮点数。对复数返回模。

- 整数
- 浮点数
- 复数

如果 `x` 定义了 `__abs__()` 函数，`abs(x)` 返回 `x.__abs__()`.

## all

[`all(iterable)`](../src/python_test/builtin_func/all_test.py)

如果 `iterable` 的所有元素为 true，返回 `True`。等价于：

```py
def all(iterable):
  for element in iterable:
    if not element:
      return False
  return True
```

## any

[`any(iterable)`](../src/python_test/builtin_func/any_test.py)

`iterable` 的任意对象为 true，返回 `True`。如果 iterable 为空，返回 `False`。等价于：

```py
def any(iterable):
  for element in iterable:
    if element:
      return True
  return False
```

## ascii

[`ascii(object)`](../src/python_test/builtin_func/ascii_test.py)

功能和 `repr()` 类似，返回对象可打印形式的字符串表示，但是对 `repr()` 返回字符串中的非 ASCII 字符，使用 `\x`, `\u` 或 `\U` 进行转义。和 Python 2 中 `repr()` 返回的字符串类似。

## enumerate

`enumerate()` 方法给 iterable 对象添加了一个计数器。语法：

`enumerate(iterable, start=0)`

- `iterable`，支持迭代的任意对象
- `start`，其实计数值，默认0

返回 `enumerate` 对象，可以使用 `list()` 和 `tuple()` 等转换为其它序列对象。

## int

`int([x])`

`int(x, base=10)`

功能说明：

- 将数字或字符串 `x` 转换为 integer 对象，如果不提供参数，返回 `0`。
- 如果 `x` 定义了 `__int__()`，`int(x)` 返回 `x.__int__()`
- 如果 `x` 定义了 `__index__()`，返回 `x.__index__()`
- 如果 `x` 定义了 `__trunc__()`，返回 `x.__trunc__()`

如果 x 不是数字，或者提供了 `base` 参数，则 `x` 必须为 string, `bytes` 或 `bytearray`

## min

`min(iterable, *[, key, default])`

`min(arg1, arg2, *args[, key])`

返回 `iterable` 或多个参数中的最小项。

- 如果只提供了一个位置参数，则必须为 `iterable` 类型。返回其最小项。
- 如果提供了多个位置参数，则返回最小的位置参数。

有两个可选的关键字参数。

- `key` 用于指定排序函数，和 `list.sort()` 函数使用的参数类似
- `default` 指定 `iterable` 为空时返回的对象。

如果不提供 `default` 且 `iterable` 为空，抛出 `ValueError`。

如果出现多个相同的最小值，返回第一次出现的值。

## pow

[`pow(base, exp[, mod])`](../src/python_test/builtin_func/pow_test.py)

返回 `base` 的 `exp` 指数；如果指定 `mod`，则对指数结果相对 `mod` 取模，效率比 `pow(base, exp) % mod` 高。

两个参数的形式 `pow(base, exp)` 等价于 `base ** exp`。

参数必须为数字类型。对混合参数类型，规则和二进制算数运算规则相同。对 `int` 操作数，如果第二个参数为 `int`，结果为 `int` 类型；如果第二个参数为负数，所有参数转换为 `float`，返回浮点数类型。例如：`10**2=100`, `10*-2=0.01`。

- 指定 `mod`

`mod` 必须为非零整数。如果 `exp` 为负，则

## print

参考 [io](io.md)

## range

`range(stop)`

`range(start, stop[, step])`

range 类型表示 immutable 数字序列，一般用在 for 循环中指定循环次数：

- 生成 [start, stop) 之间的整数序列
- step 表示增量值，默认为 1
- 如果 step 为 0 或负值，返回 empty 序列
- 如果 step 为 0，抛出 `ValueError`

[使用实例](../src/python_test/range_test.py)

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

`sorted(iterable, *, key=None, reverse=False)`

返回 `iterable` 排序后的列表。

可选参数 `key` 指定从元素中提取用于比对的信息，例如 `key=str.lower`，默认为 `None`，即直接比对元素。

参数 `reverse` 如果设置为 `True`，反向排序。

该内置的 `sorted()` 函数保证稳定。排序算法稳定的意思是，不改变相等元素原来的顺序。

```py
py_list = ['e', 'a', 'u', 'o', 'i']
sorted_list = sorted(py_list)
assert sorted_list == ['a', 'e', 'i', 'o', 'u']
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

## type()

`type()` 函数有两种形式：

- `type(object)`
- `type(name, bases, dict)`

### type(object)

单参数形式，返回 `object` 类型。例如：

```py
number_list = [1, 2]
assert type(number_list) == list

number_dict = {1: 'one', 2: 'two'}
assert type(number_dict) == dict

class Foo:
    a = 0

foo = Foo()
assert type(foo) == Foo
```

建议使用 `isinstance()` 查看对象类型，因为它还考虑了子类。`type()` 判断类型比较严格，不会认为子类是一种父类类型，而 `isinstance()` 则会认为子类是一种父类类型。例如：

```py
class Shape():
    pass

class Circle(Shape):
    pass

assert type(Shape()) == Shape
assert not (type(Circle()) == Shape)
assert isinstance(Circle(), Shape)
```

`Circle` 是 `Shape` 子类，然而 `type(Circle()) == Shape` 为 `False`。

所以在判断类型上，用 `isinstance` 更合适。

### type(name, bases, dict)

返回一个新的 type 对象。这是 `class` 语句的动态形式。

- `name` 为类名，对应 `__name__` 属性
- `bases` tuple 逐项列出基类，对应 `__bases__` 属性
- `dict` 为包含 class 定义的命名空间，复制到标准 dict，对应 `__dict__` 属性

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
