# Decoratoe

## 简介

Decorator 用于给已有的代码添加额外的功能。

在 Python 中一切都是对象，包括函数类型；每个对象都有对应的名称，用于对象的识别。一个函数可以有多个命令。例如：
```py
def first(msg):
    print(msg)


first("Hello")

second = first
second("Hello")
```

这里，`first` 和 `second` 指向相同的函数对象。

另外，在 Python 中函数可以作为其它函数的的参数。将其它函数作为参数的函数也称为高阶函数（higher order function），例如：
```py
def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operator(func, x):
    result = func(x)
    return result

assert operator(inc, 3) == 4
assert operator(dec, 3) == 2
```

`operator()` 函数为高阶函数。

另外，函数还可以返回一个函数对象，例如：
```py
def is_called():
    def is_returned():
        print("Hello")

    return is_returned


new = is_called()
new()
```
