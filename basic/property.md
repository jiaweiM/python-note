# Property

- [Property](#property)
  - [简介](#简介)
  - [不用 getter 和 setter](#不用-getter-和-setter)
  - [用 getter 和 setter](#用-getter-和-setter)
  - [property 类](#property-类)
  - [装饰器](#装饰器)
  - [使用建议](#使用建议)
  - [参考](#参考)

2020-04-12, 20:19
***

## 简介

Python 内置对 property 支持，对面向对象编程，简化了 getter 和 setter 方法的定义。`@property` 装饰器进一步简化了属性定义。

## 不用 getter 和 setter

定义一个表示摄氏温度的类，并实现了一个转换为华氏温度的方法：

```python
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
```

然后可以直接引用 `temperature` 属性进行操作：

```python
# Basic method of setting and getting attributes in Python
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


# Create a new object
human = Celsius()

# Set the temperature
human.temperature = 37

# Get the temperature attribute
print(human.temperature)

# Get the to_fahrenheit method
print(human.to_fahrenheit())
```

当添加或检索对象的任何属性时，例如 `temperature`，Python 在对象的内置 dict `__dict__` 检索该属性，例如：

```python
print(human.__dict__) 
# Output: {'temperature': 37}
```

所以 `human.temperature` 内部为 `human.__dict__['temperature']`。

## 用 getter 和 setter

假设想要为 `Celsius` 添加检查功能，如温度不低于 -273.15。新的实现如下：

```python
# Making Getters and Setter methods
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value
```

上面引入两个新方法 `get_temperature()` 和 `set_temperature()`。将 `temperature` 替换为 `_temperature`，下划线表示为私有变量。

下面使用新的实现：

```python
# Making Getters and Setter methods
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value


# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter
print(human.get_temperature())

# Get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit())

# new constraint implementation
human.set_temperature(-300)

# Get the to_fahreheit method
print(human.to_fahrenheit())
```

新的实现可以检查温度，确保温度不会低于 -273.15。

该更新的主要问题：所有使用上一个类的程序都要修改代码，将 `obj.temperature` 重命名为 `obj.get_temperature()`，将 `obj.temperature = val` 重命名为 `obj.set_temperature(val)`。

## property 类

`property` 进一步简化了属性定义。使用 `property` 更新上述代码：

```python
# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)
```

添加的 `print()` 方法是为了清除观察这些方法在运行。

最后一行 `temperature = property(get_temperature, set_temperature)` 创建了一个 `property` 对象。简而言之，`property` 将一些代码（`get_temperature` 和 `set_temperature`）附加到成员属性 `temperature`。

使用方法：

```python
# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)


human = Celsius(37)

print(human.temperature) # getter

print(human.to_fahrenheit())

human.temperature = -300 # setter
```

查看 `temperature` 值的操作被自动调用 `get_temperature()`，不再是查询 `__dict__`。

设置 `temperature` 值的操作被自动调用 `set_temperature()`。

另外，下面的操作：

```python
human = Celsius(37) # prints Setting value...
```

`__init__` 中的 `self.temperature = temperature` 其实也是用的属性，调用 `set_temperature()`，因此支持数值检查。

## 装饰器

property 其实是绑定在一起的一系列相关方法。`property()` 签名如下：

```py
class property(fget=None, fset=None, fdel=None, doc=None):
```

| 参数 | 说明 |
|---|---|
| fget | 用于获得属性值的方法 |
| fset | 用于设置属性值的方法 |
| fdel | 用于删除属性值的方法 |
| doc() | 属性文档 |

`property` 对象有三个方法： `getter()`, `setter()` 和 `deleter()`，分别用来指定 `fget`, `fset` 和 `fdel`。所以：

```python
temperature = property(get_temperature,set_temperature)
```

与下面是等价的：

```python
# make empty property
temperature = property()

# assign fget
temperature = temperature.getter(get_temperature)

# assign fset
temperature = temperature.setter(set_temperature)
```

使用 `@property` decorator 进一步简化前面的示例：

```python
# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

coldest_thing = Celsius(-300)
```

上述代码中有三个关联方法，它们名字必须相同。

第一个是 `getter` 函数，它使得 `temperature` 成为属性。

其它两个方法给 `temperature` 属性添加了 `setter` 和 `deleter` 函数。需要强调的是，只有定义了 `temperature` 属性，后面的连个装饰器 `@temperature.setter` 和 `@temperature.deleter` 才能被定义。

property 看上去和普通的 attribute 类似，但是访问它的时候会自动触发 `getter`, `setter` 和 `deleter` 方法。例如：

在实现 property 时，底层数据依然需要存储在某个变量。因此，在 `getter` 和 `setter` 方法中可以看到对 `_temperature` 属性的操作，这也是实际数据保存的地方。

另外，`__init__()` 方法中使用 `self.temperature` 而不是 `self._temperature` 设置值，因为这样才能在初始化时调用 `setter` 方法检查值。

## 使用建议

在需要对 attribute 执行额外的操作时才使用 property。有些从其它编程语言（如 Java）过来的程序员总认为所有访问都应该通过 getter 和 setter，所以它们认为代码都应像下面这样：

```py
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
```

这种没有任何其它额外操作的 property 没有任何意义，不要这么写。

还可以使用 property 定义动态计算 attribute 的方法。这种类型的 attributes 不会被存储，而是在需要时计算出来。比如：

```py
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
```

这里通过 property，将所有访问形式统一起来，对半径、直径、周长和面积都通过属性访问，就跟访问简单的 attribute 一样。如果不这样，就需要在代码中混合使用属性访问和方法调用。实例：

```py
>>> c = Circle(4.0)
>>> c.radius
4.0
>>> c.area  # Notice lack of ()
50.26548245743669
>>> c.perimeter  # Notice lack of ()
25.132741228718345
```

## 参考

- https://www.programiz.com/python-programming/property
