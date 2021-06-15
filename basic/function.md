# Python 函数

- [Python 函数](#python-函数)
  - [简介](#简介)
  - [创建函数](#创建函数)
  - [函数返回值](#函数返回值)
  - [局部变量和全局变量](#局部变量和全局变量)
  - [参数](#参数)
    - [关键字参数](#关键字参数)
    - [仅关键字参数](#仅关键字参数)
    - [默认参数](#默认参数)
    - [可变参数 *args](#可变参数-args)
    - [**kwargs](#kwargs)
  - [拆分参数列表](#拆分参数列表)
  - [Lambda 函数](#lambda-函数)
  - [高阶函数](#高阶函数)
    - [map、filter](#mapfilter)
    - [reduce](#reduce)
  - [可调动类型](#可调动类型)
  - [函数内省](#函数内省)
    - [`__dict__`](#__dict__)
    - [`__annotations__`](#__annotations__)

2021-06-02, 11:05
*****

## 简介

函数是可重复使用的代码片段。

形参：parameters
实参：arguments

## 创建函数

语法：

```python
def function_name(arg1, arg2, arg3, … argN):
  # statement inside function
```

## 函数返回值

return 后不带任何值，则返回 `None` .

可以一次返回多个值，值之间以逗号分开，为 tuple 类型。

## 局部变量和全局变量

如果局部变量和全局变量同名，则全局变量被覆盖，如果要在函数内修改全局变量的值，需加 `global` ：

```python
t = 1
def increment():
  global t   # now t inside the function is same as t outside the function
  t = t + 1
  print(t)   # Displays 2

increment()
print(t)  # Displays 2
```

声明的global 变量时不能赋值，下面的做法是错误的：

```python
t = 1
def increment():
  # global t = 1   # this is error
  global t
  t = 100   # this is okay
  t = t + 1
  print(t)  # Displays 101

increment()
print(t)  # Displays 101
```

可以在函数内部声明全局变量：

```python
def foo():
  global x  # x is declared as global so it is available outside the function
  x  = 100

foo()
print(x)
```

即，在函数内部访问全局变量，需要通过 `global` 关键字。

## 参数

### 关键字参数

给方法传递参数的方法有两种：根据位置和根据关键字。
关键字参数：

```py
def named_args(name, greeting):
  print(greeting + " " + name)
```

调用：使用关键字，参数的顺序无所谓

```py
named_args(name='jim', greeting='Hello')
# Hello jim

named_args(greeting = 'Hello', name='jim')
# Hello jim
```

可以混合使用基于位置和基于关键字的参数，不过基于位置的参数必须在基于关键字参数之前。

### 仅关键字参数

仅关键字参数是 Python 3 新增特性，如下所示，`cls` 参数只能通过关键字参数指定，它不会捕获未命名的定位参数。定义函数时若想指定仅关键字参数，需要把它定义在 `*` 参数后面。

```py
def tag(name, *content, cls=None, **attrs):
    """生成一个或多个 HTML 标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


def test_tag():
    assert tag('br') == "<br />"  # 单个标签

    s = tag('p', 'hello')  # 单个内容
    assert s == "<p>hello</p>"

    s = tag('p', 'hello', 'world')  # 多个内容
    assert s == "<p>hello</p>\n<p>world</p>"

    s = tag('p', 'hello', id=33)  # 标签+内容+属性
    assert s == '<p id="33">hello</p>'

    s = tag('p', 'hello', 'world', cls='sidebar')  # 标签+内容*2+cls
    assert s == '<p class="sidebar">hello</p>\n<p class="sidebar">world</p>'

    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jpg', 'cls': 'framed'}
    s = tag(**my_tag)  # 在 my_tag 前面加上 **，字典中的所有元素作为单个参数传入，同名键会绑定到对应的具名参数上，余下的则被 **attrs 捕获
    assert s == '<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'
```

如果不想支持数量不定的定位参数，但是想支持仅关键字参数，可以在签名中放一个 `*`，例如：

```py
>>> def f(a, *, b):
...     return a, b
...
>>> f(1, b=2)
(1, 2)
```

### 默认参数

在定义函数时给参数赋值即可：

```py
def func(i, j=100):
  print(i, j)
```

默认参数应该放在函数参数列表的末尾。

### 可变参数 *args

`*args` 和 `**kwargs` 在函数定义中将不定数目的参数传递给函数。

使用 `*args` 传递可变数目的非关键字参数给函数。例如，下面是包含两个参数的函数：

```py
def sum(a, b):
    print("sum is", a+b)
```

如果希望传递多个参数进去，此时可以用 `*args` 定义函数：

```py
def sum(*args):
    s = 0
    for i in args:
        s += i
    print("sum is", s)
```

> 注意：args 只是一个传统命名，此处可以使用任意有效的标识符，如 *myargs等。

- `*` 将序列/集合解压缩为位置参数

例如：

```py
def my_three(a, b, c):
    print(a, b, c)

a = [1,2,3]
my_three(*a) # here list is broken into three elements
```

该方法只有在**参数和列表元素数目相同**时才可行。

### **kwargs

`**kwargs` 可用于传递可变数目的关键字参数。

例如：

```py
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

>>> greet_me(name="yasoob")
name = yasoob
```

- 方法调用中作为参数传递

```py
def my_three(a, b, c):
    print(a, b, c)

a = {'a': "one", 'b': "two", 'c': "three" }
my_three(**a) # 关键字参数，其实就是字典
```

使用前提：

- 参数名和键名相同;
- 参数数目和字典大小相同。

如果要在函数中同时使用 `*args` 和 `**kwargs`，顺序如下：

```py
some_func(fargs, *args, **kwargs)
```

## 拆分参数列表

如果参数已在 list 或 tuple 中，但是调用函数需要单独的位置参数。例如 `range()` 函数需要 `start` 和 `stop` 参数。如果两者是一起存在的，可以使用 `*` 运算符从 list 或 tuple 中拆分参数：

```py
>>> list(range(3, 6))            # 使用参数正常调用
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # 使用拆分参数语法
[3, 4, 5]
```

`range(*args)` 等价于 `range(3, 6)`。

- 类似的，字典可以通过 `**` 运算符传递关键字参数

```py
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```

## Lambda 函数

Lambda 语法用于创建匿名函数。一般用于创建简单函数，作为其它函数的参数。Python 限制 lambda 函数的定义只能使用纯表达式，换句话说，lambda 函数的定义中不能赋值，也不能使用 while 和 try 等 Python 语句。例如：

```python
def multiple(x, y):
  return x * y
```

其lambda 定义形式：

```py
r = lambda x, y: x * y
r(12, 3) # 调用 lambda 函数，返回36
```

除了作为参数传给高阶函数外，Python 很少使用匿名函数。

## 高阶函数

接收函数为参数，或者把函数作为结果返回的函数就是**高阶函数**（higher-order function）。`map` 函数就是，内置函数 `sorted` 也是，其 `key` 参数用于提供一个函数。例如：

```py
>>> fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
>>> sorted(fruits, key=len)
['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']
```

在函数式编程中，`map`, `filter`, `reduce` 和 `apply` 是最为人熟知的高阶函数。`apply` 函数在 Python 3 中被移除。`map`, `filter`, `reduce` 还能见到，不过多数场景都有更好的替代品。

### map、filter

由于引入了列表推导和生成器，所以 `map`, `filter`就没那么重要了。例如：

```py
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


def test_map_listgen():
    fact = factorial
    l = list(map(fact, range(6)))
    assert l == [1, 1, 2, 6, 24, 120]

    l2 = [fact(n) for n in range(6)]
    assert l2 == [1, 1, 2, 6, 24, 120]

    l = list(map(factorial, filter(lambda n: n % 2, range(6))))
    assert l == [1, 6, 120]

    l2 = [factorial(n) for n in range(6) if n % 2]
    assert l2 == [1, 6, 120]
```

可以看到，列表推导比 `map` 函数使用起来给为简洁。

### reduce

在 Python 2 中，`reduce` 是内置函数，但在 Python 3 中放到了 `functools` 模块中。

## 可调动类型

可以使用内置的 `callable()` 函数判断对象能够调用，Python 数据模型列出了 7 种可调用对象：

- 用户定义的函数，即使用 def 语句或 lambda 表达式创建的函数；
- 内置函数，使用 C 语言（CPython）实现的函数，如 `len` 或 `time.strftime`；
- 内置方法，使用 C 语言实现的方法，如 `dict.get()`；
- 方法，在类中定义的函数；
- 类，调用类时会运行类的 `__new__` 方法创建一个实例，然后运行 `__init__` 方法 初始化实例，最后把实例返回给调用方，因为 Python 没有 `new` 运算符，所以调用类相当于调用函数；
- 类的实例：如果类定义了 `__call__()` 方法，那么它的实例可以作为函数调用；
- 生成器函数，使用 `yield` 关键字的函数或方法。调用生成器函数返回的是生成器对象。

例如：

```py
class BingoCage:
    def __init__(self, items):
        self._items = list(items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BiogoCage')

    def __call__(self, *args, **kwargs):
        return self.pick()


def test_biongo():
    bingo = BingoCage(range(3))
    assert bingo.pick() == 2
    assert bingo() == 1
```

`BingoCage` 中定义 `__call__` 为 `self.pick()`，这样就能用 `bingo()` 替代调用 `pick()`。

## 函数内省

除了 `__doc__`，函数对象还有许多属性，其中大多数属性是 Python 对象共有的。

|名称|类型|说明|
|---|---|---|
|`__annotations__`|`dict`|将参数和返回值的注解|
|`__call__`|`method-wrapper`|实现 `()` 运算符，即可调用对象协议|
|`__closure__`|`tuple`|函数闭包，即自由变量的绑定，通常是 `None`|
|`__code__`|code|编译成字节码的函数元数据和函数定义体|
|`__defaults__`|`tuple`|形式参数的默认值|
|`__get__`|`method-wrapper`|实现只读描述符协议|
|`__globals__`|`dict`|函数所在模块中的全局变量|
|`__kwdefaults__`|`dict`|关键字形参默认值|
|`__name__`|`str`|函数名称|
|`__qualname__`|`str`|函数的限定名称|

例如：

```py
def clip(text, max_len=80):
    """
    在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()


def test_info():
    assert clip.__defaults__ == (80,) # 返回形参默认值，tuple 类型

```

### `__dict__`

与用户定义的常规类一样，函数使用 `__dict__` 属性存储赋予它的用户属性。

### `__annotations__`

存放参数和返回值的注解。Python 不做检查、不做强制、不做验证，什么操作都不做。换句话说，注解对Python 解释器没有任何意义，只是元数据，可以供 IDE、框架和装饰器等工具使用。

添加注解的函数如下所示：

```py
def clip(text: str, max_len: 'int > 0' = 80) -> str:
    """在max_len前面或后面的第一个空格处截断文本
        """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()
```

查看注解：

```py
>>> from clip_annot import clip
>>> clip.__annotations__
{'text': <class 'str'>, 'max_len': 'int > 0', 'return': <class 'str'>}
```

