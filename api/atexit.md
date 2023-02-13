# atexit

- [atexit](#atexit)
  - [简介](#简介)
  - [atexit.register](#atexitregister)
  - [atexit.unregister](#atexitunregister)
  - [示例](#示例)
  - [参考](#参考)

Last updated: 2023-02-13, 19:25
****

## 简介

`atexit` 模块包含注册和取消注册执行清理函数的功能：

- 注册的清理函数在解释器正常终止时自动执行；
- `atexit` 以与注册顺序的相反的顺序执行这些函数；
- 例如，注册 `A`, `B`, `C`，在解释器终止时，按 `C`, `B`, `A` 的顺序执行。

> **NOTE**
> 当 Python 程序被 Python 以外的方法终止、发生严重内部错误，或者调用 `os._exit()` 时，`atexit` 注册的函数不会被调用。

## atexit.register

```python
atexit.register(func, *args, **kwargs)
```

将 `func` 注册为在解释器终止时执行的函数。

任何要传递给 `func` 的参数都必须作为参数传递给 `register()`。可以多次注册相同的函数和参数。

在程序正常终止时（如调用 `sys.exit()` 或程序正常执行完成），所有注册的函数按**后进先出**的顺序调用。

如果在执行退出处理程序期间引发异常，则打印 traceback 信息。在所有退出处理程序运行后，将重新引发最后一个异常。

该函数返回 `func`，因此可以用作装饰器。

## atexit.unregister

```python
atexit.unregister(func)
```

将 `func` 从注册函数列表中删除。如果 `func` 之前没有注册，`unregister` 不执行任何操作。如果 `func` 注册过多次，所有都删除。

在取消注册中使用 `==` 判断是否相等，因此函数引用的标识不需要相同。

## 示例

在导入文件时从文件中初始化计数器，在程序终止时保存计数器的更新值。

```python
try:
    with open('counterfile') as infile:
        _count = int(infile.read())
except FileNotFoundError:
    _count = 0

def incrcounter(n):
    global _count
    _count = _count + n

def savecounter():
    with open('counterfile', 'w') as outfile:
        outfile.write('%d' % _count)

import atexit

atexit.register(savecounter)
```

可以传入位置参数和关键字参数：

```python
def goodbye(name, adjective):
    print('Goodbye %s, it was %s to meet you.' % (name, adjective))

import atexit

atexit.register(goodbye, 'Donny', 'nice')
# or:
atexit.register(goodbye, adjective='nice', name='Donny')
```

作为装饰器使用：

```python
import atexit

@atexit.register
def goodbye():
    print('You are now leaving the Python sector.')
```

装饰器只适用于没有参数的函数。

## 参考

- https://docs.python.org/3/library/atexit.html
