# 模块

- [模块](#%e6%a8%a1%e5%9d%97)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [导入模块](#%e5%af%bc%e5%85%a5%e6%a8%a1%e5%9d%97)
    - [导入声明](#%e5%af%bc%e5%85%a5%e5%a3%b0%e6%98%8e)
    - [重命名导入](#%e9%87%8d%e5%91%bd%e5%90%8d%e5%af%bc%e5%85%a5)
    - [from...import](#fromimport)
    - [导入所有定义](#%e5%af%bc%e5%85%a5%e6%89%80%e6%9c%89%e5%ae%9a%e4%b9%89)
  - [Python 模块搜索路径](#python-%e6%a8%a1%e5%9d%97%e6%90%9c%e7%b4%a2%e8%b7%af%e5%be%84)
  - [重载模块](#%e9%87%8d%e8%bd%bd%e6%a8%a1%e5%9d%97)
  - [dir() 函数](#dir-%e5%87%bd%e6%95%b0)
  - [作为脚本执行模块](#%e4%bd%9c%e4%b8%ba%e8%84%9a%e6%9c%ac%e6%89%a7%e8%a1%8c%e6%a8%a1%e5%9d%97)
  - [编译 Python 文件](#%e7%bc%96%e8%af%91-python-%e6%96%87%e4%bb%b6)

2020-04-12, 13:20
***

## 简介

模块是包含 Python 定义和声明的文件。

文件名是模块名加上 `.py` 后缀。模块的名称可以通过全局变量 `__name__` 获得。

下面创建一个 `example.py` 文件，对应模块名为 `example`:

```py
# Python Module example

def add(a, b):
   """This program adds two
   numbers and return the result"""

   result = a + b
   return result
```

其中定义了 `add()` 函数。

## 导入模块

我们可以将一个模块中的定义导入另一个模块，或导入 Python 交互解释器。

使用 `import` 关键字导入模块。例如将上面的模块 导入解释器：

```py
>>> import example
```

这种方式不直接导入模块中的函数，而是导入模块名。

通过模块名加 `.` 可以访问函数。例如：

```py
>>> example.add(4,5.5)
9.5
```

### 导入声明

即，使用 `import` 语句导入模块，同构 `.` 访问函数，同上：

```py
import math
print("The value of pi is", math.pi)
```

### 重命名导入

导入模块，并重命名模块：

```py
import math as m
print("The value of pi is", m.pi)
```

这里将模块 `math` 重命名为 `m`。这样可以节省打字时间和代码显式空间。

### from...import

通过如下导入语句可以只导入模块的部分定义，而不是导入模块全部内容：

```py
from math import pi
print("The value of pi is", pi)
```

这里只导入了 `math` 模块的 `pi` 属性。而且使用时不用 `.` 运算符。

还可以一次导入多个属性：

```py
>>> from math import pi, e
>>> pi
3.141592653589793
>>> e
2.718281828459045
```

### 导入所有定义

使用 `*` 可以导入模块内所有定义：

```py
from math import *
print("The value of pi is", pi)
```

使用 `*` 导入了除下划线开头命名的所有内容。

## Python 模块搜索路径

导入模块，如 `example`，解释器先搜索 `sys.path` 变量给出的目录列表中查找。检索路径：

- 当前目录
- 环境变量 `PYTHONPATH` 包含的目录列表
- Python 默认安装路径

例如：

```py
>>> import sys
>>> sys.path
['',
'C:\\Python33\\Lib\\idlelib',
'C:\\Windows\\system32\\python33.zip',
'C:\\Python33\\DLLs',
'C:\\Python33\\lib',
'C:\\Python33',
'C:\\Python33\\lib\\site-packages']
```

有需要你可以在添加新的路径到 `sys.path`。

## 重载模块

出于性能考虑，每个模块在每个解释器中只导入一次。假设我们有一个 `my_module` 模块：

```py
# This module shows the effect of
#  multiple imports and reload

print("This code got executed")
```

导入模块：

```py
>>> import my_module
This code got executed
>>> import my_module
>>> import my_module
```

可以看到，重复导入模块也只在第一次执行。这表明模块只导入一次。

假设在程序运行期间模块修改了，我们修改了模块，此时就需要重新载入。使用 `imp` 模块的 `reload()` 函数可以重新载入一个模块：

```py
>>> import imp
>>> import my_module
This code got executed
>>> import my_module
>>> imp.reload(my_module)
This code got executed
<module 'my_module' from '.\\my_module.py'>
```

## dir() 函数

内置函数 `dir()` 用于按模块名搜索模块定义，它返回一个字符串类型的有序列表，对应模块内定义的内容。

例如，查看前面定义的 `example` 模块内容：

```py
>>> dir(example)
['__builtins__',
'__cached__',
'__doc__',
'__file__',
'__initializing__',
'__loader__',
'__name__',
'__package__',
'add']
```

除了 `add`，其它以下划线开头的定义时 Python 中模块的默认属性。

`__name__` 为模块名称：

```py
>>> import example
>>> example.__name__
'example'
```

无参数调用时，`dir()` 返回当前命名空间的所有定义：

```py
>>> a = 1
>>> b = "hello"
>>> import math
>>> dir()
['__builtins__', '__doc__', '__name__', 'a', 'b', 'math', 'pyscripter']
```

## 作为脚本执行模块

当你使用如下方式运行 Python 模块时，模块中的代码便会执行。

```py
python fibo.py <arguments>
```

不过此时模块的 `__name__` 被设置为 `__main__`。所以在模块后加入如下代码：

```py
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

可以在模块作为脚本执行时，传入参数。例如：

```py
$ python fibo.py 50
1 1 2 3 5 8 13 21 34
```

## 编译 Python 文件

为了加快模块加载的速度，Python 会在 `__pycache__` 目录以 `module.version.pyc` 名字缓存每个模块编译后的版本。

Python 会检查源文件与编译版的修改日期，以确定编译版是否过期以确定是否需要重新编译。

技巧：

- 为了减少编译模块的大小，可以使用 `-O` 或 `-OO` 命令。`-O` 删除了断言语句，`-OO` 删除断言语句和 `__doc__` 字符串。

优化后的模块后缀为 `.pyo`。

- 来自 `.pyc`或 `.pyo` 文件的程序不比来自 `.py` 文件运行快，`.pyc` 或 `.pyo` 只是加载快。
