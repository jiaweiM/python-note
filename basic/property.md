
# 简介
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

# getter 和 setter
如果我们想为 `temperature` 提供检查支持，例如温度范围检查，可以采用如下方式：
```py
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

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

    temperature = property(get_temperature,set_temperature)
```
其功能是，在添加了自定义参数检查的同时，可以通过 `.temperature` 的语法赋值和取值。

上面的 `property()` 是一个函数，其签名如下：
```py
property(fget=None, fset=None, fdel=None, doc=None):
```
| 参数  | 说明                 |
| ----- | -------------------- |
| fget  | 用于获得属性值的方法 |
| fset  | 用于设置属性值的方法 |
| fdel  | 用于删除属性值的方法 |
| doc() | 属性文档             |

上面的语法还可以使用 `@property` decorator 进一步简化：
```py
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature() * 1.8) + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
```
