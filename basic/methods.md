# 实例方法、类方法和静态方法

- [实例方法、类方法和静态方法](#实例方法类方法和静态方法)
  - [简介](#简介)
  - [实例方法](#实例方法)
  - [类方法](#类方法)
  - [静态方法](#静态方法)
  - [示例 1](#示例-1)
  - [示例 2：class method](#示例-2class-method)
  - [示例 3：static method](#示例-3static-method)

***

## 简介

**核心概念**：

- 实例方法（instance method）需要类实例，通过 `self` 访问实例；
- 类方法（class method，`@classmethod`）不需要类实例，不能访问实例（`self`），但是可以通过 `cls` 访问类本身；
- 静态方法（static method，`@staticmethod`）不能访问 `cls` 和 `self`。其功能与常规函数一样，但属于类的命名空间。

下面介绍类方法、静态方法和常规的实例方法（instance method）的区别。先在一个类中定义三种方法：

```python
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
```

## 实例方法

上面的 `method` 是实例方法。实例方法有一个 `self` 参数，当调用该方法时，`self` 指向 `MyClass` 的一个实例。

通过 `self` 参数，实例方法可以自由访问同一对象的属性和其它方法。当设计修改**对象状态**时，实例方法权限最大。

另外，实例方法还可以通过 `self.__class__` 访问类本身。这意味着实例方法还能修改**类的状态**。

## 类方法

类方法使用 `@classmethod` 装饰器标记。

类方法没有 `self` 参数，而是 `cls` 参数。`cls` 在调用时指向 class，而不对对象实例。

类方法只能访问 `cls` 参数，因此不能修改对象实例状态，但是可以通过修改 class 来影响所有类实例。

## 静态方法

静态方法用 `@staticmethod` 装饰器标识。

这类方法没有 `self` 或 `cls` 参数，当然，它可以接受任意的其它参数。

静态方法不能修改对象状态或类状态，根据输入的参数进行操作。

## 示例 1

上面定义的 `MyClass` 类中定义了三种方法，每个方法都返回一个 tuple。下面分别调用：

-  实例方法

```python
>>> obj = MyClass()
>>> obj.method()
('instance method called', <__main__.MyClass at 0x1ca37910d60>)
```

输出信息表明实例方法 `method` 可以访问对象实例。

调用实例方法时，Python 将 `self` 替换为示例对象 `obj`。我们可以忽略 `obj.method()` 这种语法糖调用形式，手动传递实例对象获得相同结果：


```python
>>> MyClass.method(obj)
('instance method called', <__main__.MyClass at 0x2de29f94e50>)
```

另外，实例方法可以通过 `self.__class__` 访问 class 本身。因此从访问权限角度来说，实例方法非常强大，它可以自由修改对象实例和类本身的状态。

- 类方法

```python
>>> obj.classmethod()
('class method called', __main__.MyClass)
```

可以看到，类方法只能访问 `MyClass`，而不能访问其实例。

需要注意的是，`self` 和 `cls` 参数命名是一种约定，你也可以将其命名为 `the_object` 和 `the_class`，得到的结果相同。关键是它们必须是方法的第一个参数。

- 静态方法

```python
>>> obj.staticmethod()
'static method called'
```

有没有发现，用类的实例也可以调用静态方法。

静态方法既不能访问对象实例状态，也不能访问类状态。静态方法和常规函数一样，只是归属于这个类（以及每个实例）的命名空间。

- 不创建实例，直接用类调用这些方法

```python
>>> MyClass.classmethod()
('class method called', __main__.MyClass)
>>> MyClass.staticmethod()
'static method called'
>>> MyClass.method()
TypeError: method() missing 1 required positional argument: 'self'
```

可以直接调用 `classmethod()` 和 `staticmethod()`，因为它们都不需要对象实例访问权限，而调用 `method()` 不可以。

## 示例 2：class method

下面继续用例子来说明这些方法的应用场景。

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        
    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
```

```python
>>> Pizza(['cheese', 'tomatoes'])
Pizza(['cheese', 'tomatoes'])
```

Pizza 有很多种类别，要创建各种不同的 Pizza，一个可选的方式是用类方法实现创建 Pizza 的工厂函数：

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])
    
    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
```

需要注意的是，上面用的 `cls` 参数，而不是直接调用 Pizza 的构造函数。

这算是一个小技巧，这样以后若想重命名这个类，我们不需要更新工厂方法中的名称。

然后就能用这些工厂方法创建 Pizza：

```python
>>> Pizza.margherita()
Pizza(['mozzarella', 'tomatoes'])

>>> Pizza.prosciutto()
Pizza(['mozzarella', 'tomatoes', 'ham'])
```

> Python 每个类只允许有一个 `__init__` 方法，这种工厂函数形式提供了可选的构造方法。

## 示例 3：static method

```python
import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi
```

静态方法不能访问对象实例和类，其实是个独立的函数。

