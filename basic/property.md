# Property

- [Property](#property)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [getter 和 setter](#getter-%e5%92%8c-setter)
    - [设置方法](#%e8%ae%be%e7%bd%ae%e6%96%b9%e6%b3%95)
    - [用已有方法定义 property](#%e7%94%a8%e5%b7%b2%e6%9c%89%e6%96%b9%e6%b3%95%e5%ae%9a%e4%b9%89-property)
    - [annotation 定义](#annotation-%e5%ae%9a%e4%b9%89)
  - [使用建议](#%e4%bd%bf%e7%94%a8%e5%bb%ba%e8%ae%ae)

2020-04-12, 20:19
***

## 简介

Python 内置对 property 支持，对面向对象编程，简化了 getter 和 setter 方法。

假设我们定义一个摄氏温度的类：

```py
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
```

然后可以直接引用 `temperature` 属性进行操作：

```py
man = Celsius()
man.temperature = 37
assert man.temperature == 37
assert man.to_fahrenheit() == pytest.approx(98.6)
```

当我们将属性添加到对象中，例如 `temperature`，Python 将该其放到对象的 `__dict__` 中，此时 `temperature` 的内部形式就是 `man.__dict__['temperature']`。

## getter 和 setter

一个 property 其实是绑定在一起的一系列相关方法。`property()` 是一个函数，其签名如下：

```py
property(fget=None, fset=None, fdel=None, doc=None):
```

| 参数  | 说明                 |
| ----- | -------------------- |
| fget  | 用于获得属性值的方法 |
| fset  | 用于设置属性值的方法 |
| fdel  | 用于删除属性值的方法 |
| doc() | 属性文档             |

其属性就是类里面的普通方法。

### 设置方法

如果我们想为 `temperature` 提供检查支持，例如温度范围检查，可以采用如下方式：

```py
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


man = Celsius()
man.set_temperature(-287)
```

下划线 `_` 将 `temperature` 设置为了 private 变量。通过 `set_temperature` 方法设置值，而我们在 `set_temperature` 中添加了对温度值的检查。

不过应当注意，Python 其实不支持 private 变量。上面在变量前加下划线定义 private 变量只是定义的一个规范，并非强制；关键通过 set 方法赋值总归更复杂了些，没有直接引用方便。所以 Python 引入了 property。

### 用已有方法定义 property

```py
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    def del_temperature(self):
        raise AttributeError("Can't delete attribute")

    temperature = property(get_temperature,set_temperature, del_temperature)
```

property 的功能是，在添加了自定义参数检查的同时，可以通过 `.temperature` 的语法赋值和取值。

### annotation 定义

上面的语法还可以使用 `@property` decorator 进一步简化：

```py
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

    @temperature.deleter
    def temperature(self):
        raise AttributeError("Can't delete attribute")
```

上述代码中有三个关联方法，它们名字必须相同。

第一个是 `getter` 函数，它使得 `temperature` 成为属性。

其它两个方法给 `temperature` 属性添加了 `setter` 和 `deleter` 函数。需要强调的是，只有定义了 `temperature` 属性，后面的连个装饰器 `@temperature.setter` 和 `@temperature.deleter` 才能被定义。

property 看上去和普通的 attribute 类似，但是访问它的时候会自动触发 `getter`, `setter` 和 `deleter` 方法。例如：

```py
c = Celsius(37)
assert c.temperature == 37
with pytest.raises(ValueError):
    c.temperature = -275
with pytest.raises(AttributeError):
    del c.temperature
```

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
