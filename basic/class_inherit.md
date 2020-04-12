# Inheritance

- [Inheritance](#inheritance)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [super](#super)
  - [继承解析](#%e7%bb%a7%e6%89%bf%e8%a7%a3%e6%9e%90)
  - [扩展 property](#%e6%89%a9%e5%b1%95-property)

2020-04-12, 21:36
***

## 简介

继承是一种使用已有类的信息创建新类的方法，新创建的类称为子类，原有类称为父类。

例如：

```py
# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
```

Out:

```console
Bird is ready
Penguin is ready
Penguin
Swim faster
Run faster
```

在上例中，创建了两个类 `Bird` (父类)和 `Penguin` (子类)。

- 子类继承了父类的函数 `swim()`
- 修改父类函数 `whoisThis()`
- 添加了新函数 `run()`

另外，在 `__init__()` 方法中调用了 `super()`，执行父类中的初始化工作。

## super

可以使用 `super()` 调用父类方法，比如：

```py
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()  # Call parent spam()
```

`super()` 函数的一个常见用于是在 `__init__()` 方法中确保父类被正确初始化了：

```py
class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1
```

`super()` 另一个常见用法是用在覆盖 Python 的特殊方法中：

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

## 继承解析

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

可能两次调用 `Base.__init__()` 有时候没问题，但有些情况就影响很大。 而使用 `super()` 就没有这问题：

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

这里我们解释下Python是如何实现继承的。对于定义的每一个类，Python会计算出一个所谓的方法解析顺序(MRO)表。 这个MRO列就是一个简单的所有基类的线性顺序表。例如：

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

`super()` 有个令人吃惊的地方是它并不一定去查找某个类在MRO中下一个直接父类，你甚至可以在一个没有直接父类的类中使用它。例如，考虑如下这个类：

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

## 扩展 property

如下：

```py
class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")
```

