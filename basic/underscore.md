# 下划线

- [下划线](#下划线)
  - [1. 简介](#1-简介)
  - [2. 前缀单下划线](#2-前缀单下划线)
  - [3. 后缀单下划线](#3-后缀单下划线)
  - [4. 前缀双下划线](#4-前缀双下划线)
  - [5. 前后双下划线](#5-前后双下划线)
  - [6. 单下划线](#6-单下划线)
  - [7. 总结](#7-总结)

Last updated: 2023-01-10, 16:18
****

## 1. 简介

Python 变量和方法名称中的**单下划线**和**双下划线**，有些是习惯用法，有些是 Python 解释器强制要求。

下划线使用主要包括：

- 前缀单下划线：`_var`
- 后缀单下划线：`var_`
- 前缀双下划线：`__var`
- 前后双下划线：`__var__`
- 单下划线

## 2. 前缀单下划线

变量和方法名的前缀下划线为习惯用法，表示该变量或方法只在内部使用，在 PEP8 代码样式指南中有约定，不过 Python 解释器不作强制要求。例如：

```python
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
```

`_bar` 以下划线开头，表示**建议作为私有变量使用**，但是 Python 解释器不作强制要求，依然可以访问：

```python
>>> t = Test()
>>> t.foo
11
>>> t._bar
23
```

- 不过**前缀下划线影响从模块中导入名称**。假设 `my_module` 定义如下：

```python
# my_module.py:

def external_func():
    return 23

def _internal_func():
    return 42
```

如果使用通配符从 `my_module` 导入所有名称，Python 不会导入带前缀下划线的名称（在 `__all__` 中显式定义除外）：

```python
>>> from my_module import *
>>> external_func()
23
>>> _internal_func()
NameError: "name '_internal_func' is not defined"
```

> 不建议使用通配符导入

- 常规导入不受前缀单下划线命名规则影响：

```python
>>> import my_module
>>> my_module.external_func()
23
>>> my_module._internal_func()
42
```

## 3. 后缀单下划线

有时，最合适的变量名已被用作 Python 语言关键字，如 `class` 或 `def` 等关键字都不能用作变量名。此时可以在关键字后面添加下划线来避免命名冲突：

```python
>>> def make_object(name, class):
SyntaxError: "invalid syntax"

>>> def make_object(name, class_):
... pass
```

简而言之，后缀单下划线没有特殊含义，一般**用来避免与 Python 关键字的命名冲突**，该习惯用法在 PEP8 中有定义。

## 4. 前缀双下划线

前缀双下划线表示由 Python 解释器重写属性名，以避免与子类中的命名冲突，也称为**名称错位**（name mangling）。例如：

```python
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23
```

使用 `dir()` 查看该对象的属性：

```python
>>> t = Test()
>>> dir(t)
['_Test__baz', '__class__', '__delattr__', '__dict__',
'__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__gt__', '__hash__', '__init__',
'__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__',
'__setattr__', '__sizeof__', '__str__',
'__subclasshook__', '__weakref__', '_bar', 'foo']
```

可以看到：

- `self.foo` 变量名称不变，在属性列表中为 `foo`
- `self._bar` 变量名称也不变
- `self.__baz` 变量名称被修改为 '_Test__baz'

下面创建 `ExtendedTest` 类，扩展 `Test` 并尝试覆盖已有属性：

```python
class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'
```

`ExtendedTest` 的 `foo`, `_bar` 和 `__baz` 的属性值：

```python
>>> t2 = ExtendedTest()
>>> t2.foo
'overridden'
>>> t2._bar
'overridden'
>>> t2.__baz
AttributeError:
"'ExtendedTest' object has no attribute '__baz'"
```

访问 `__baz` 抛出 `AttributeError`。继续查看 `ExtendedTest` 属性：

```python
>>> dir(t2)
['_ExtendedTest__baz', '_Test__baz', '__class__',
'__delattr__', '__dict__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__',
'__gt__', '__hash__', '__init__', '__le__', '__lt__',
'__module__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__',
'__weakref__', '_bar', 'foo', 'get_vars']
```

可以看到，`__baz` 被转换为 `_ExtendedTest__baz`，且父类的 `_Test__baz` 也依然存在。

```python
>>> t2._ExtendedTest__baz
'overridden'
>>> t2._Test__baz
42
```

- 前缀双下划线名称在类中可以自由访问

```python
class ManglingTest:
    def __init__(self):
        self.__mangled = 'hello'
    
    def get_mangled(self):
        return self.__mangled

>>> ManglingTest().get_mangled()
'hello'
>>> ManglingTest().__mangled
AttributeError:
"'ManglingTest' object has no attribute '__mangled'"
```

- 名称错位也可用于方法名

```python
class MangledMethod:
    def __method(self):
        return 42
    
    def call_it(self):
        return self.__method()

>>> MangledMethod().__method()
AttributeError:
"'MangledMethod' object has no attribute '__method'"
>>> MangledMethod().call_it()
42
```

- 另一个特殊的示例

```python
_MangledGlobal__mangled = 23

class MangledGlobal:
    def test(self):
        return __mangled

>>> MangledGlobal().test()
23
```

这里定义全局变量 `_MangledGlobal__mangled`，然后在类 `MangledGlobal` 中访问变量，由于名称错位，在 `test()` 方法中可以用 `__mangled` 来访问全局变量 `_MangledGlobal__mangled`。

简而言之，因为 `__mangled` 以双下划线开头，Python 解释器根据名称错位规则自动将其扩展为 `_MangledGlobal__mangled`。这说明名称错位并没有与类属性绑定在一起，它适用于在类中使用的任何以两个下划线开头的任何名称。

## 5. 前后双下划线

如果名称前后都有双下划线，不会应用名称错位。例如：

```python
class PrefixPostfixTest:
    def __init__(self):
        self.__bam__ = 42

>>> PrefixPostfixTest().__bam__
42
```

在 Python 中，同时具有前后双下划线的名称具有特殊含义。如 `__init__` 用于构造函数，`__call__` 使得对象可调用。

在实际应用中，自定义函数应当避免使用前后双下划线名称，以避免与 Python 特殊名称冲突。

## 6. 单下划线

单下划线是有效的变量名，一般用来表示临时变量或无关紧要的变量，是一种约定用法，无特殊含义。

- 例如，下面的循环中，因为不需要访问循环索引，所以用 `_` 来命名：

```python
>>> for _ in range(32):
...     print('Hello, World.')
```

- 也可以在解包表达式用单下划线来忽略特定值。

例如，下面将一个 tuple 解包为单独变量，我们只对 `color` 和 `mileage` 感兴趣，但是为了解包成功需要对 tuple 的所有值命名，此时对不感兴趣的变量可以用 `_`：

```python
>>> car = ('red', 'auto', 12, 3812.4)
>>> color, _, _, mileage = car
>>> color
'red'
>>> mileage
3812.4
>>> _
12
```

- 除了用作临时变量，在大多数 REPL 中 `_` 表示解释器计算的最后一个表达式的值。例如：

```python
>>> 20 + 3
23
>>> _
23
>>> print(_)
23
```

## 7. 总结

- 前缀单下划线 `_var`：习惯用法，定义内部使用名称。
- 后缀单下划线 `var_`：习惯用法，避免与 Python 关键字冲突。
- 前缀双下划线 `__var`：在类定义中触发名称错位。
- 前后双下划线 `__var__`：Python 中特殊方法定义。
- 单下划线 `_`：作为临时变量或不重要变量名称，在 REPL 中表示上一个表达式结果。
