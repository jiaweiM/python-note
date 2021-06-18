# functools

- [functools](#functools)
  - [简介](#简介)
  - [partial](#partial)
    - [partial 对象](#partial-对象)
    - [partial 函数](#partial-函数)
  - [reduce](#reduce)

2021-06-16, 09:29
@author Jiawei Mao
***

## 简介

functools 模块为高阶函数设计，高阶函数为以函数为参数或返回函数的函数。

## partial

### partial 对象

`partial` 是 `partial()` 方法创建的可调用对象。包含三个只读属性：

- `partial.func`，可调用对象或函数；
- `partial.args`，最左侧位置参数；
- `partial.keywords`，关键字参数。

`partial` 对象和函数对象类似，可调用、弱引用，并且具有属性。也有一些差异，例如不会自动创建 `__name__` 和 `__doc__` 属性。另外，在类中定义的 `partial` 对象和静态方法类似，在实例属性查找时不会转换为绑定方法。

### partial 函数

```py
functools.partial(func, /, *args, **keywords)
```

创建一个 `partial` 对象，该对象行为与使用位置参数 `args` 和关键字参数 `keywords` 调用函数 `func` 的效果类似。额外参数自动附加到 `args`，额外关键字参数自动附加到 `keywords`。大致等同于：

```py
def partial(func, /, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = {**keywords, **fkeywords}
        return func(*args, *fargs, **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
```

`partial()` 主要用于冻结函数的部分参数，从而生成简化签名的函数对象。例如，使用 `partial()` 创建一个可调用对象，将 `int()` 函数的 `base` 参数设置为 2：

```py
>>> from functools import partial
>>> basetwo = partial(int, base=2)
>>> basetwo.__doc__ = 'Convert base 2 string to an int.'
>>> basetwo('10010')
18
```



## reduce

```py
functools.reduce(function, iterable[, initializer])
```

`function` 为两个参数的函数，将该函数从左到右应用到 `iterable` 对象，最终获得单个值。例如 `reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])` 计算 `((((1+2)+3)+4)+5)` 获得加和值。lambda 函数中，左侧 `x` 保存累积值，右侧 `y` 表示可迭代对象的值。

`initializer` 为初始化，如果 `iterable` 为空，就是默认的返回值。

该函数大致等价于：

```py
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
```

