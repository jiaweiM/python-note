# Python 内置函数

- [Python 内置函数](#python-内置函数)
  - [字符串函数](#字符串函数)
  - [数学函数](#数学函数)
  - [pow](#pow)
  - [round](#round)
  - [sorted](#sorted)
    - [非原生比较对象排序](#非原生比较对象排序)
  - [reversed](#reversed)
  - [zip](#zip)
    - [无参数](#无参数)
    - [一个参数](#一个参数)
    - [多个参数](#多个参数)
    - [set 参数](#set-参数)
    - [参数长度不等](#参数长度不等)
    - [zip in Python 2](#zip-in-python-2)
    - [unzipping](#unzipping)

2020-04-12, 17:41
***

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

## pow

[`pow(base, exp[, mod])`](../src/python_test/builtin_func/pow_test.py)

返回 `base` 的 `exp` 指数；如果指定 `mod`，则对指数结果相对 `mod` 取模，效率比 `pow(base, exp) % mod` 高。

两个参数的形式 `pow(base, exp)` 等价于 `base ** exp`。

参数必须为数字类型。对混合参数类型，规则和二进制算数运算规则相同。对 `int` 操作数，如果第二个参数为 `int`，结果为 `int` 类型；如果第二个参数为负数，所有参数转换为 `float`，返回浮点数类型。例如：`10**2=100`, `10*-2=0.01`。

- 指定 `mod`

`mod` 必须为非零整数。如果 `exp` 为负，则

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
