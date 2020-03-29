# Class

- [Class](#class)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [创建对象](#%e5%88%9b%e5%bb%ba%e5%af%b9%e8%b1%a1)
    - [创建类](#%e5%88%9b%e5%bb%ba%e7%b1%bb)
  - [隐藏字段数据](#%e9%9a%90%e8%97%8f%e5%ad%97%e6%ae%b5%e6%95%b0%e6%8d%ae)
  - [运算符重载](#%e8%bf%90%e7%ae%97%e7%ac%a6%e9%87%8d%e8%bd%bd)
  - [继承和多态](#%e7%bb%a7%e6%89%bf%e5%92%8c%e5%a4%9a%e6%80%81)
  - [Magic Method](#magic-method)
  - [类方法（class method）](#%e7%b1%bb%e6%96%b9%e6%b3%95class-method)
  - [静态方法（Static Method）](#%e9%9d%99%e6%80%81%e6%96%b9%e6%b3%95static-method)
  - [Properties](#properties)
  - [重载字符串表示方法](#%e9%87%8d%e8%bd%bd%e5%ad%97%e7%ac%a6%e4%b8%b2%e8%a1%a8%e7%a4%ba%e6%96%b9%e6%b3%95)

## 简介

类是数据和函数的逻辑分组，它可以创建包含任意内容且容易访问的数据结构。

## 创建对象

Python 是面向对象的语言，在Python 中一切都是对象，包括 int, str, bool，甚至 modules, functions 也是对象。

### 创建类

定义方式：

```py
class Person:
       # constructor or initializer
      def __init__(self, name):
            self.name = name # name is data field also commonly known as instance variables

      # method which returns a string
     def whoami(self):
           return "You are " + self.name
```

特殊函数 `__init__` 为构造函数。

上例创建了一个 `Person`类，包含字段 `name` 和函数 `whoami()`.

类中所有方法的第一个参数为 `self`，表示对象自身的引用。

## 隐藏字段数据

python 没有 private 关键字，也没有强制将字段或方法隐藏的方法。而只有建议的方法，在方法名前加**一个下划线**。这只是一个传统建议方式，并不能阻止外部访问。不过 `from module_name import *` 不会导入以下划线开头的变量。

特别强调隐藏的，在前面加**两个下划线**。这类字段，在类外部无法直接访问，得换个方式，如：类 `Spam` 中的 `__privatemethod`，在外部，需要以 `_Spam__privatemethod` 形式访问。即 Python 修改该字段的内部名。

为了隐藏字段，需要将字段定义为 private。

- 在字段名前加两个下划线，字段自动为 private。
- 在方法名前加两个下划线，方法也成为 private。

例如：

```py
class BankAccount:
     # constructor or initializer
    def __init__(self, name, money):
         self.__name = name
         self.__balance = money   # __balance is private now, so it is only accessible inside the class

    def deposit(self, money):
         self.__balance += money

    def withdraw(self, money):
         if self.__balance > money :
             self.__balance -= money
             return money
         else:
             return "Insufficient funds"

    def checkbalance(self):
         return self.__balance

b1 = BankAccount('tim', 400)
print(b1.withdraw(500))
b1.deposit(500)
print(b1.checkbalance())
print(b1.withdraw(800))
print(b1.checkbalance())
```

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

## 继承和多态

## Magic Method

Magic 方法指方法名带两个下划线的方法，如 `__init__`，这些方法一般有特定功能。

常执行的功能如运算符重载。

## 类方法（class method）

其第一个参数是 `cls` 而不是 `self`.常用于创建工厂方法。
以 `@classmethod` 注释。

## 静态方法（Static Method）

类似于类方法，但是没有额外的参数，和常规函数相同，以：`@staticmethod` 注释。

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

## 重载字符串表示方法

要改变实例的字符串表示，可重载 `__str__()` 和 `__repr__()` 方法。

`__repr__()` 定义实例的代码表示形式，通常用来重新构造这个实例。内置的 `repr()` 函数返回这个字符串。和交互式解释器显示的值一样。

`__str__()` 将实例转换为字符串，`str()` 和 `print()` 函数输出这个字符串。

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