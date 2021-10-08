# Python 类型

- [Python 类型](#python-类型)
  - [概念](#概念)
  - [内置对象类型](#内置对象类型)
  - [数据类型转换](#数据类型转换)

## 概念

Python 程序可以按如下分解：

1. 程序（program）由模块（module）组成；
2. 模块包含语句（statement）；
3. 语句由表达式（expression）组成；
4. 表达式负责创关键和处理对象。

Python 提供了大量的内置类型，使得编程更容易，而且大多数内置类型经过大量优化，在性能和效率上都有保障。

## 内置对象类型

|类型|说明|
|---|---|
|Numbers|1234, 3.1415, 3+4j, ob111, Decimal(), Fraction()|
|Strings|'spam', "Lilei's", b'a\x01c', u'sp\xc4m'|
|Lists|[1, [2, 'three'], 4.5], list(range(10))|
|Dictionaries|{'food': 'spam', 'taste': 'yum'}, dict(hours=10)|
|Tuples|(1, 'spam', 4, 'U'), tuple('spam'), namedtuple|
|Files|open('eggs.txt'), open(r'C:\ham.bin', 'wb')|
|Sets|set('abc'), {'a', 'b', 'c'}|
|Other core types|Booleans, types, None|
|Program unit types|Functions, modules, classes|
|Implementation-related types|Compiled code, stack tracebacks|

可以看到，程序的基本单元，函数、模块和类都是内置类型。Python 中一切都是对象，我们看到的程序、编译代码、简单类型以及集合等，无不是对象。

## 数据类型转换

| 函数  | 功能   |
| ----- | ------ |
| int(x [,base])        | 将 x 转换为 integer。若 x 为字符串，base 表示基 |
| long(x [,base])       | 将 x 转换为 long。若 x 为字符串，base 表示基    |
| float(x)              | 将 x 转换为 float  |
| complex(real [,imag]) | 创建复数           |
| str(x)     | x 转换为字符串表示      |
| repr(x)    | x转换为字符串表示       |
| eval(str)  | 计算字符串，返回一个对象 |
| tuple(s)   | s 转换为 tuple           |
| list(s)    | s 转换为 list            |
| set(s)     | s 转换为 set             |
| dict(d)       | 创建字典。d 必须为 (key,value) tuple 序列|
| frozenset(s)  | s 转换为 frozen set          |
| chr(x)        | integer 转换为字符           |
| unichr(x)     | integer 转换为 Unicode 字符  |
| ord(x)        | 字符转换为其整数形式         |
| hex(x)        | 整数转换为十六进制字符串     |
| oct(x)        | 整数转换为八进制字符串       |
