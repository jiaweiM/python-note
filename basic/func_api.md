# Python 内置函数

- [Python 内置函数](#python-%e5%86%85%e7%bd%ae%e5%87%bd%e6%95%b0)
  - [基本函数](#%e5%9f%ba%e6%9c%ac%e5%87%bd%e6%95%b0)
  - [字符串函数](#%e5%ad%97%e7%ac%a6%e4%b8%b2%e5%87%bd%e6%95%b0)
  - [数学函数](#%e6%95%b0%e5%ad%a6%e5%87%bd%e6%95%b0)
  - [math 模块](#math-%e6%a8%a1%e5%9d%97)
  - [函数](#%e5%87%bd%e6%95%b0)
    - [abs](#abs)
    - [all](#all)
    - [any](#any)
    - [range](#range)
    - [zip](#zip)
      - [unzipping](#unzipping)
    - [type()](#type)
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

## math 模块

| 方法     | 说明                                                 |
| -------- | ---------------------------------------------------- |
| ceil(x)  | Rounds the number up and returns its nearest integer |
| floor(x) | Rounds the down up and returns its nearest integer   |
| sqrt(x)  | Returns the square root of the number                |
| sin(x)   | Returns sin of x where x is in radian                |
| cos(x)   | Returns cosine of x where x is in radian             |
| tan(x)   | Returns tangent of x where x is in radian            |

## 函数

### [abs](../src/python_test/abs_test.py)

`abs(x)`

计算绝对值。`x` 可以为整数或浮点数。对复数返回模。

- 整数
- 浮点数
- 复数

如果 `x` 定义了 `__abs__()` 函数，`abs(x)` 返回 `x.__abs__()`.

### [all](../src/python_test/all_test.py)

`all(iterable)`

如果 `iterable` 的所有元素为 true，返回 `True`。等价于：

```py
def all(iterable):
  for element in iterable:
    if not element:
      return False
  return True
```

### [any](../src/python_test/any_test.py)

`any(iterable)`

`iterable` 的任意对象为 true，返回 `True`。如果 iterable 为空，返回 `False`。等价于：

```py
def any(iterable):
  for element in iterable:
    if element:
      return True
  return False
```

### range

`range(stop)`

`range(start, stop[, step])`

range 类型表示 immutable 数字序列，一般用在 for 循环中指定循环次数：

- 生成 [start, stop) 之间的整数序列
- step 表示增量值，默认为 1
- 如果 step 为 0 或负值，返回 empty 序列
- 如果 step 为 0，抛出 `ValueError`

[使用实例](../src/python_test/range_test.py)

### zip

`zip(*iterables)`

将多个 iterable 对象聚合在一起构成一个迭代器。

返回 tuple 迭代器，可以传入任意数目的 iterable 对象：

- 第 i 个 tuple 包含所有iterable对象的第 i 个元素。当最短的iterable对象耗尽，迭代器停止。
- 无参数，返回空 iterator。
- 一个参数，返回的iterator 的 tuple 长度为1。
- 多个参数，tuple 长度为iterable参数个数。

对 lists, tuples, strings 等可迭代对象，迭代的顺序保持不变。

- 多个参数

```py
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
zips = list(zipped)
assert zips[0] == (1, 'a')
assert zips[1] == (2, 'b')
assert zips[2] == (3, 'c')
```

- set 参数

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

- 无参数

无参数，返回空 iterator

```py
zipped = zip()
l = list(zipped)
assert l == []
```

`zip()` 只迭代到最短对象的长度，如果不希望截断，可以使用 `itertools.zip_longest()`。

- 一个参数

一个参数，返回的 iterator 的 tuple 长度为1.

```py
a = [1, 2, 3]
zipped = zip(a)
l = list(zipped)
assert l[0] == (1,)
assert l[1] == (2,)
assert l[2] == (3,)
```

- 参数长度不等

如果参数长度不等，`zip()` 返回元素的个数和最短的iterable长度相同。哪些较长 iterable 参数余下元素忽略。例如：

```py
l = list(zip(range(3), range(100)))
assert len(l) == 3
assert l[0] == (0, 0)
assert l[1] == (1, 1)
assert l[2] == (2, 2)
```

- zip in Python 2

在 Python 2中，`zip()` 返回 tuple `list`。`list` 长度和输入最短的 iterable 对象相同。如果无输入参数，返回空 `list`。

而 Python 3 中，`zip()` 返回的是 iterator。使用 iterator 的好处是在需要时才生成数据，内存占用更少。

#### unzipping

有 `zip()` 函数，为什么没有 `unzip()` 函数。因为`zip` 和 `*` 结合就实现了 unzip 功能。

假如你有一个 tuple 列表，然后你希望将 tuple 分解，获得独立的列表。实现方式如下：

```py
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
assert numbers == (1, 2, 3, 4)
assert letters == ('a', 'b', 'c', 'd')
```

### type()

`type()` 函数有两种形式：

```py
type(object) # return type of the given object
type(name, bases, dict) # return a new type object
```

### isinstance

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
