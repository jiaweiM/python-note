# 上下文管理器

- [上下文管理器](#上下文管理器)
  - [1. 简介](#1-简介)
    - [1.1 文件资源管理](#11-文件资源管理)
    - [1.2 线程资源管理](#12-线程资源管理)
  - [2. 自定义 with](#2-自定义-with)
    - [2.1 使用类实现](#21-使用类实现)
    - [2.2 使用 contextlib 实现](#22-使用-contextlib-实现)
  - [3. 上下文管理器的使用](#3-上下文管理器的使用)

Last updated: 2023-01-06, 13:44
****

## 1. 简介

Python 中的 `with` 语句可以帮助编写更清晰、易读的资源管理代码。

### 1.1 文件资源管理

`with` 语句对一些常见的资源管理模式进行抽象，简化了这些模式的使用。以内置的 `open()` 函数为例：

```python
with open('hello.txt', 'w') as f:
    f.write('hello, world!')
```

通常建议使用 `with` 语句打开文件，因为它可以确保在执行完 `with` 语句后自动关闭打开的文件。在 Python 内部，上面的代码自动转换为：

```python
f = open('hello.txt', 'w')
try:
    f.write('hello, world')
finally:
    f.close()
```
显然 `with` 语句要简洁很多。另外需要强调的是，上面的 `try...finally` 语句是必须的，如果按如下方式执行：

```python
f = open('hello.txt', 'w')
f.write('hello, world')
f.close()
```

当 `f.write()` 执行期间出现异常，这个实现不能保证关闭文件，从而有内存泄露风险。**`with` 语句使得获取和释放资源更容易**。

### 1.2 线程资源管理

`with` 语句还可以用于线程管理，以 `threading.Lock` 类为例：

```python
some_lock = threading.Lock()

# Harmful:
some_lock.acquire()
try:
    # Do something...
finally:
    some_lock.release()

# 推荐:
with some_lock:
    # Do something...
```

对文件和线程，`with` 语句都可以抽象出大部分资源处理逻辑，不必每次编写 `try...finally` 语句。

## 2. 自定义 with

### 2.1 使用类实现

上下文管理器是一个简单的协议（或接口），实现该接口就能支持 `with` 语句。简而言之，只需要在类中实现 `__enter__` 和 `__exit__` 方法，Python 会在资源管理期间自动调用这两个方法。

下面是 `open()` 上下文管理器的简单实现：

```python
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
```

`ManagedFile` 实现了上下文管理器接口，和 `open()` 一样支持 `with` 语句：

```python
with ManagedFile('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')
```

Python 执行到 with 语句时调用 `__enter__` 以持有资源；执行到 `with` 语句结束时，Python 调用 `__exit__` 以释放资源。

### 2.2 使用 contextlib 实现

基于类的上下文管理器不是实现 `with` 语句的唯一方法。标准库中的 `contextlib` 模块对基本的上下文管理器进一步进行了抽象，使得定义上下文管理器更简单。

使用 `contextlib.contextmanager` 装饰器注释基于生成器的工厂函数，即可支持 `with` 语句。下面使用该方法重写上面 `ManagedFile`：

```python
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

with managed_file('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')
```

`managed_file()` 是一个生成器，首先获取资源，然后挂起执行，由调用者用获取的资源执行相关操作（如写入文件），当离开 `with` 上下文时，生成器继续执行，执行余下的清理和释放资源步骤。

基于类和基于生成器的实现本质上是等价的。如何选择取决于你喜欢哪种代码风格。

## 3. 上下文管理器的使用

上下文管理器非常灵活，应用广泛。例如，如果所谓的资源是文本的缩进级别呢？如下：

```python
with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('bonjour')
    indent.print('hey')
```

使用 `with` 控制缩进级别，运行此代码输出如下：

```python
hi!
    hello
        bonjour
hey
```

`Indenter` 的实现如下：

```python
class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print(' ' * self.level + text)
```

是不是很有意思！进入 `Indenter` with 语句，缩进 +1 （`self.level += 1`），离开 `Indenter` with 语句，缩进 -1.

