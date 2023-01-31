# Class

- [Class](#class)
  - [简介](#简介)
  - [类](#类)
  - [对象](#对象)
  - [方法](#方法)
  - [封装](#封装)
    - [单下划线](#单下划线)
    - [双下划线](#双下划线)
    - [使用建议](#使用建议)
  - [运算符重载](#运算符重载)
  - [Magic Method](#magic-method)
  - [Properties](#properties)
  - [方法重载](#方法重载)
    - [字符串表示方法](#字符串表示方法)
    - [自定义格式化字符串](#自定义格式化字符串)
    - [with 支持](#with-支持)
  - [继承](#继承)
    - [super](#super)
    - [多重继承](#多重继承)
    - [MRO](#mro)
  - [参考](#参考)

Last updated: 2023-01-31, 18:38
****

## 简介

Python 是一种多范式编程语言，支持不同的编程方法。编程语言中一种流行方法是创建对象，就是所谓的面向对象编程（OOP）。

每个对象包含两个特征：

- 属性
- 行为

例如，鹦鹉（Parrot）是一个对象：

- 属性：name, age, color
- 行为：singing, dancing

Python 中的 OOP 概念专注于创建可重用代码，此概念也称为 DRY (Don't Repeat Yourself)。

在 Python 中，OOP 概念支持如下原则：

- 继承（Inheritance）
- 封装（Encapsulation），隐藏类中的私有信息，不让其他对象访问
- 多态（Polymorphism），行为的多种实现方法

## 类

类（class）是对象的模板，以 `class` 关键字定义：

```py
class Parrot:
    """This is a docstring. I have created a Parrot"""
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)
```

每个类都创建一个本地命名空间，包含其定义的所有属性（数据和函数）。

类创建后，还额外包含一些默认属性，以双下划线 `__` 开头。例如 `__doc__` 表示类的 docstring。

特殊函数 `__init__` 为构造函数。

上例创建了一个 `Parrot`类，包含字段 `name`, `age`.

类中所有方法的第一个参数为 `self`，表示对象自身的引用。

## 对象

对象是类的一个实例。

例如创建对象：

```py
obj = Parrot()
```

这里 `obj` 是类 `Parrot` 的一个对象。

使用对象：

```py
# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species)) # Blu is a bird
print("Woo is also a {}".format(woo.__class__.species)) # Woo is also a bird

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age)) # Blu is 10 years old
print("{} is {} years old".format( woo.name, woo.age)) # Woo is 15 years old
```

上例中，类属性使用 `__class__.species` 访问。类属性对所有的实例都相同。

实例属性使用 `blu.name` 形式访问，不同实例可以有不同的实例属性。

## 方法

方法用于定义对象的行为。上例的 `sing()` 和 `dance()` 都是实例方法。

```py
# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'")) # Blu sings 'Happy'
print(blu.dance()) # Blu is now dancing
```

## 封装

python 没有 private 关键字，也没有强制将字段或方法隐藏的方法，而只有建议的方法。在方法或属性名前加 `_`。这只是一个传统建议方式，并不能阻止外部访问。不过 `from module_name import *` 不会导入以下划线开头的变量。

### 单下划线

例如：

```py
class A:
    def __init__(self):
        self._internal = 0 # An internal attribute
        self.public = 1 # A public attribute

    def public_method(self):
        '''
        A public method
        '''
        pass

    def _internal_method(self):
        pass
```

Python 不会真的阻止别人访问内部名称。

### 双下划线

特别强调隐藏的，在前面加**两个下划线** `__`，这种方式会导致访问名称变成其它形式。这类字段在类外部无法直接访问，得换个方式，

如：类 `Spam` 中的 `__privatemethod`，在外部，需要以 `_Spam__privatemethod` 形式访问。即 Python 修改该字段的内部名。

为了隐藏字段，需要将字段定义为 private。

- 在字段名前加两个下划线，字段自动为 private。
- 在方法名前加两个下划线，方法也成为 private。

例如：

```py
class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()
```

私有字段被重命名为 `_B__private` 和 `_B__private_method`。

这样重命名的主要目的是继承——这种属性通过继承无法被覆盖。例如：

```py
class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1 # Does not override B.__private

    # Does not override B.__private_method()
    def __private_method(self):
        pass
```

这里，私有名称 `__private` 和 `__private_method` 被重命名为 `_C__private` 和 `_C__private_method`，这样就和父类 `B` 中的名称完全不同了。

### 使用建议

大多数情况，对私有名称使用单下划线开头。

如果你确定你的代码涉及到子类，并且有些内部属性应该在子类中隐藏起来，此时考虑使用双下划线。

有时候你定义的变量和关键字冲突，此时可以使用单下划线后缀区分：

```py
lambda_ = 2.0 # Trailing _ to avoid clash with lambda keyword
```

这里不使用单下划线前缀，是为了避免和私有字段的下划线区分。

## 运算符重载

| 运算符        | 重载方法                    |
| ------------- | --------------------------- |
| +             | `__add__(self, other)`      |
| -             | `__sub__(self, other)`      |
| *             | `__mul__(self, other)`      |
| /             | `__truedive__(self, other)` |
| //            | `__floordiv__`              |
| **            | `__pow__`                   |
| %             | `__mod__(self, other)`      |
| <             | `__lt__(self, other)`       |
| <=            | `__le__(self, other)`       |
| ==            | `__eq__(self, other)`       |
| !=            | `__ne__(self, other)`       |
| >             | `__gt__(self, other)`       |
| >=            | `__ge__(self, other)`       |
| &             | `__and__`                   |
| ^             | `__xor__`                   |
| `|`           | `__or__`                    |
| [index]       | `__getitem__(self, index)`  |
| 通过index赋值 | `__setitem__`               |
| 通过index删除 | `__delitem__`               |
| 迭代          | `__iter__`                  |
| in            | `__contains__(self, value)` |
| len           | `__len__(self)`             |
| str           | `__str__(self)`             |

如果没有实现 `__ne__`重载，则返回 `__eq__`的相反值。

## Magic Method

Magic 方法指方法名带两个下划线的方法，如 `__init__`，这些方法一般有特定功能。

常执行的功能如运算符重载。

## Properties

`@property`
被标记的方法，当访问和方法名相同的属性，以调用方法代替。适合将属性设置为只读。

属性的 setter 和 getter:
setter 的标记，需要在属性名后加 .setter

```py
@property
def pineapple_allowed(self):
    return self._pineapple_allowed

@pineapple_allowed.setter
def pineapple_allowed(self, value):
    if value:
        password = input("Enter the password: ")
    if password == "Sw0rdf1sh!":
        self._pineapple_allowed = value
    else:
        raise ValueError("Alert! Intruder!")
```

## 方法重载

### 字符串表示方法

Python 提供了两种获取对象字符串表示的方法：

- `repr()`，以开发者容易理解的方式返回对象的字符串表示形式；
- `str()`，以用户容易理解的方式返回对象的字符标识形式。

我们需要实现 `__str__()` 和 `__repr__()` 方法，为 `repr()`和 `str()` 提供支持。

另外还有 `__bytes__` 方法，`bytes()` 函数调用它获取对象的字节序列表示形式。

`__format__` 方法，`format()` 和 `str.format()` 方法调用它以格式化字符串。

`__repr__()` 定义实例的代码表示形式，通常用来重新构造这个实例。内置的 `repr()` 函数返回这个字符串。和交互式解释器显示的值一样。

`__repr__()` 实现的标准做法是使得 `eval(repr(x)) == x` 为真。如果实在无法做到，应该创建一个描述性文本，用 `<>` 括起来。例如：

```py
>>> f = open('file.dat')
>>> f
<_io.TextIOWrapper name='file.dat' mode='r' encoding='UTF-8'>
```

`__str__()` 将实例转换为字符串，`str()` 和 `print()` 函数输出这个字符串。如果 `__str__()` 没有定义，会使用 `__repr__()` 代替输出。

例如：

```py
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


def test_repr():
    p = Pair(3, 4)
    assert p.__repr__() == 'Pair(3, 4)'


def test_str():
    p = Pair(3, 4)
    assert str(p) == '(3, 4)'
```

其中 `!r` 格式化代码表示输出使用 `__repr__()` 代替默认的 `__str__()`。

格式化代码 `{0.x}` 表示第一个参数的 `x` 属性。所以 `{0.x!r}` 表示以 `__repr__()`输出第一个参数的 x 属性。

用上例测试：

```py
>>> p = Pair(3, 4)
>>> print('p is {0!r}'.format(p))
p is Pair(3, 4)
>>> print('p is {0}'.format(p))
p is (3, 4)
```

### 自定义格式化字符串

要自定义字符串的格式化，需要定义 `__format__()` 方法。例如：

```py
_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)
```

现在 `Date` 类的实例支持格式化操作，例如：

```py
>>> d = Date(2012, 12, 21)
>>> format(d)
'2012-12-21'
>>> format(d, 'mdy')
'12/21/2012'
>>> 'The date is {:ymd}'.format(d)
'The date is 2012-12-21'
>>> 'The date is {:mdy}'.format(d)
'The date is 12/21/2012'
```

> 格式化代码的解析工作完全由类自己决定。因此，格式化代码可以是任何值。

### with 支持

让对象支持上下文管理协议（with 语句），需要实现 `__enter__()` 和 `__exit__()` 方法。

- 当出现 `with` 语句时，对象的 `__enter__()` 方法被触发，它返回的值被赋值给 `as` 声明的变量。
- 然后 `with` 语句里面的代码开始执行
- 最后，`__exit__()` 方法被触发进行清理工作

不管 `with` 代码块中发生什么，上面的控制流都会执行完，就算代码块中发生异常也是如此。

事实上 `__exit__(self, exc_type, exc_val, exc_tb)` 的第三个参数包含了异常类型、异常值和追溯信息。`__exit__()`方法能自己决定怎样利用这个异常信息，或者忽略它并返回 `None`。如果 `__exit__()` 返回 `True`，异常被清空，`with` 语句后面的程序继续正常执行。

例如，下面是一个创建网络连接的类：

```py
from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None
```

这个类的主要特点是，它表示网络连接，但是初始化时不建立连接，而是在 `with` 语句自动完成建立和关闭：

```py
from functools import partial

conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed
```

还有一个问题就是 `LazyConnection` 是否允许多个 `with` 语句嵌套使用连接。很显然，上面的定义不允许。不过可以像下面修改：

```py
from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()

# Example use
from functools import partial

conn = LazyConnection(('www.python.org', 80))
with conn as s1:
    pass
    with conn as s2:
        pass
        # s1 and s2 are independent sockets
```

在这个版本中，`LazyConnection` 可以看作是连接工厂。在内部，一个列表被用来构造一个栈，每次 `__enter__()` 执行创建一个新的连接并加入到栈，`__exit__()`从栈中弹出最后一个连接并关闭它。

在需要管理一些资源比如文件、网络连接和锁的编程环境中，使用上下文管理器是很普遍。 这些资源的一个主要特征是它们必须被手动的关闭或释放来确保程序的正确运行。 例如，如果你请求了一个锁，那么你必须确保之后释放了它，否则就可能产生死锁。 通过实现 `__enter__()` 和 `__exit__()` 方法并使用 `with` 语句可以很容易的避免这些问题， 因为 `__exit__()` 方法可以让你无需担心这些。

## 继承

Python 继承语法如下：

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

其中 `BaseClassName` 必须定义在 `DerivedClassName` 所在的 scope。如果 `BaseClassName` 在其它模块，可以用如下方式：

```python
class DerivedClassName(modname.BaseClassName):
```

### super

```python
class super(type, object_or_type=None)
```

`super` 返回一个代理对象，将对方法的调用委托给父类或 `type` 类型的同级类。这对调用父类方法很有用。`super()` 有两个参数：

- `type` 指定 MRO 链的起点，通过类名指定
- `object_or_type` 指定要搜索的 MRO，一般是 `self`

在 Python 3 中可以用 `super().xxx` 代替 `super(Class, self).xxx`。

例如，如果 `object_or_type` 的 `__mro__` 为 `D -> B -> C -> A -> object`，`type` 值为 `B`，则 `super()` 搜索 `C -> A -> object`。

`object_or_type` 的 `__mro__` 属性列出了 `getattr()` 和 `super()` 使用的方法解析搜索顺序。该属性是动态的，当更新继承层次结构都可以更改。

- 如果忽略该参数，则返回的 `super` 对象没有绑定。
- 如果为对象，则 `isinstance(obj, type)` 必须为 true
- 如果是类型，则 `issubclass(type2, type)` 必须为 true。

`super` 有两个典型用法：

- 在单继承中，`super` 可以引用父类，从而不用显式命名，和其它编程语言的 super 用法一致。
- 对多继承的支持。

例如：

```py
class C(B):
    def method(self, arg):
        super().method(arg)  # 调用父类方法，等价于 super(C, self).method(arg)
```

即 `type` 默认为当前类，即 `C`，`object_or_type` 默认为 `self`。

- `super()` 常用在 `__init__()` 中确保父类被正确初始化了：

```py
class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1
```

- `super()` 用于覆盖 Python 的特殊方法

```py
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value) # Call original __setattr__
        else:
            setattr(self._obj, name, value)
```

在上例中，`__setattr__()` 的实现包含一个名字检查。如果某个属性名以下划线 `_` 开头，就通过 `super()` 调用父类的 `__setattr__()`，否则就委派给代码对象 `self._obj` 去处理。

子类调用父类的语法有三种：

```py
super().__init__()
Parent.__init__(self)
super(类名, self).__init__()
```

### 多重继承

Python 支持多重继承，即继承多个基类：

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

在大多数情况，从父类继承的属性的搜索顺序按照深度优先、从左到右的策略，如果要找一个类属性，按照如下顺序：

1. 先在 `DerivedClassName` 找，如果没找到，下一步；
2. 在 `Base1` 中搜索，然后递归地在 `Base1` 的基类中递归搜索，如果没找到，下一步；
3. 在 `Base2` 中搜索，依此类推。

实际的情况比这个更复杂一些，方法解析顺序（Method Resolution Order, MRO）会根据 `super()` 调用动态变化。

动态排序是必要的，因为在多重继承中菱形关系不可避免（菱形指从一个派生类到父类可以有多条路径）。例如，所有类都继承自 `object`，因此多重继承中到 `object` 的路径必然不止一条。为了避免多次访问基类，动态算法将搜索顺序线性化，以保证每个派生类的基类都是从左到右的顺序，且只调用每个父类一次。

### MRO

MRO 使用 C3 算法实现，基本步骤：

1. 选择一个入度为 0 的顶点并输出
2. 从继承网络中删除该顶点以及所有边
3. 重复 1、2 直到所有点被遍历

使用继承，有时候会看到下面这种直接调用父类的情况：

```py
class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')
```

尽管对大部分代码而言没有问题，但是在涉及到多继承的代码中就有可能导致奇怪的问题发生。比如：

```py
class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')

class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')
```

如果你运行这段代码就会发现 `Base.__init__()` 被调用两次，如下所示：

```py
>>> c = C()
Base.__init__
A.__init__
Base.__init__
B.__init__
C.__init__
```

这里两次调用了 `Base.__init__()`，有时候没问题，但有些情况影响很大。而使用 `super()` 可以避免该问题：

```py
class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')
```

运行这个新版本后，你会发现每个 `__init__()` 方法只会被调用一次了：

```py
>>> c = C()
Base.__init__
B.__init__
A.__init__
C.__init__
```

这里我们解释下Python是如何实现继承的。对于定义的每一个类，Python会计算出一个所谓的方法解析顺序(MRO)表。 这个 MRO 就是所有基类的线性顺序表。例如：

```py
>>> C.__mro__
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>,
<class '__main__.Base'>, <class 'object'>)
```

为了实现继承，Python会在MRO表上从左到右开始查找基类，直到找到第一个匹配这个属性的类为止。

而这个MRO表是通过C3线性化算法实现的。 我们不去深究这个算法的数学原理，它实际上就是合并所有父类的MRO表并遵循如下三条准则：

- 子类会先于父类被检查
- 多个父类会根据它们在列表中的顺序被检查
- 如果对下一个类存在两个合法的选择，选择第一个父类

MRO表中的类顺序是的类层级关系变得有意义。

当你使用 `super()` 函数，Python会在MRO表上继续搜索下一个类。 只要每个重定义的方法统一使用 `super()` 并只调用一次， 那么控制流最终会遍历完整个MRO表，每个方法也只会被调用一次。 这也是为什么在第二个例子中你不会调用两次 `Base.__init__()`。

`super()` 一个重要特点是它并不一定会查找某个类在 MRO 中下一个直接父类，你甚至可以在一个没有直接父类的类中使用它。例如，考虑如下这个类：

```py
class A:
    def spam(self):
        print('A.spam')
        super().spam()
```

如果直接使用这个类就会出错：

```py
>>> a = A()
>>> a.spam()
A.spam
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 4, in spam
AttributeError: 'super' object has no attribute 'spam'
```

但是，如果你使用多继承的话看看会发生什么：

```py
>>> class B:
...     def spam(self):
...         print('B.spam')
...
>>> class C(A,B):
...     pass
...
>>> c = C()
>>> c.spam()
A.spam
B.spam
```

你可以看到在类A中使用 `super().spam()` 实际上调用的是跟类 `A` 毫无关系的类 `B` 中的 `spam()` 方法。这个用类 `C` 的MRO表就可以完全解释清楚了：

```py
>>> C.__mro__
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>,
<class 'object'>)
```

## 参考

- https://docs.python.org/3/tutorial/classes.html
- Expert Python Programming, 4ed
- https://rhettinger.wordpress.com/2011/05/26/super-considered-super/