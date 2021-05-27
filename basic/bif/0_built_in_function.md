# Python 内置函数

- [Python 内置函数](#python-内置函数)
  - [总结](#总结)
  - [abs](#abs)
  - [all](#all)
  - [any](#any)
  - [len](#len)
  - [list](#list)
  - [int](#int)
  - [print](#print)
  - [range](#range)
  - [type](#type)
  - [参考](#参考)
  
2021-05-27, 13:38
***

## 总结

Python 解释器内置了许多函数，如下表所示：

|函数|功能|
|---|---|
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
| isinstance(object, class_type) | 验证变量是否是指定类型                                                                                                                                                                                                                                        |
| str.encode('coding')           | 将字符串转换为指定编码的字节                                                                                                                                                                                                                                  |
| b'bytes'.decode('encoding')    | 以指定编码解析字节                                                                                                                                                                                                                                            |
| dir(a_var)                     | 列出变量所有的方法                                                                                                                                                                                                                                            |
| range(a, b)                    | 返回 [a, b-1] 之间的整数序列                                                                                                                                                                                                                                  |
| range(a)                       | 返回[0, a)之间的整数序列，返回 range 对象                                                                                                                                                                                                                     |
| range(a, b, step)              | 以指定步长返回 [a, b)之间的整数序列                                                                                                                                                                                                                           |
| sum(lst)                       | 获得列表所有元素的加和                                                                                                                                                                                                                                        |

## abs

如果 x 为整数或浮点数，返回数值的绝对值；若为复数，返回模。

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

## all

当可迭代对象的所有值为 True 时，返回 True。

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

可迭代对象任何元素为 true，返回 true，否则返回 False.

如果可迭代对象为空，返回 False。

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

## int

`int()` 函数将指定值转换为整数类型：

- 如果没有参数，返回 0；
- 如果参数 `value` 定义了 `__int__()` 函数，则返回 `x.__int__()` ；
- 如果 `value` 定义了 `__index__()` 函数，则返回 `x.__index__()` ；
- 如果 `value` 定义了 `__trunc__()` 函数，则返回 `x.__trunc__()` ；
- 如果 `value` 是浮点数，则向零 取整。

```python
int(value, base)
```

参数：

- `value` ，可以转换为整数的数值或字符串；
- `base` ，数值格式，默认为 10 进制。

字符串：

```python
x = int('12')
assert x == 12
```

## print

参考 [IO 部分](https://www.yuque.com/crazyphilo/bt29bt/ihl5m8#print)。

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

## 参考

- [Built-in Functions](https://docs.python.org/3/library/functions.html)
