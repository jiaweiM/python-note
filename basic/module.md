# 模块

- [模块](#模块)
  - [简介](#简介)
  - [导入模块](#导入模块)
    - [重命名导入](#重命名导入)
    - [from...import](#fromimport)
    - [导入所有定义](#导入所有定义)
    - [相对导入](#相对导入)
  - [Python 模块搜索路径](#python-模块搜索路径)
  - [重载模块](#重载模块)
  - [dir() 函数](#dir-函数)
  - [作为脚本执行模块](#作为脚本执行模块)
  - [编译 Python 文件](#编译-python-文件)

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

导入 `re` 模块：

```py
import re
my_regex = re.compile("[0-9]+", re.I)
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

### 相对导入

使用相对导入，很容易出现错误 `ImportError: attempted relative import with no known parent package`。

加载 Python 文件的方法有两种：

- 作为顶级脚本加载
- 作为模块加载

如果直接执行，则该文件作为顶级脚本加载。如果在其它文件中使用 `import` 语句导入，则是模块。一次只能有一个顶级脚本。

**命名**

加载文件时，会给该文件一个名称（`__name__` 属性）。如果作为顶级脚本加载，其名称为 `__main__`；如果作为模块加载，其名称为文件名加上包的前缀。

例如：

```python
package/
    __init__.py
    subpackage1/
        __init__.py
        moduleX.py
    moduleA.py
```

如果导入 `moduleX`，其名称为 `package.subpackage1.moduleX`；如果导入 `moduleA`，其名称为 `package.moduleA`。

然而，如果在命令行直接运行 `moduleX`，其名称为 `__main__`；如果直接运行 `moduleA`，其名称也是 `__main__`。即，如果模块作为顶层脚本运行，它会丢失常规名称，取而代之的是 `__main__`。

**不是从模块所在的包访问模块**

还有一个问题，模块的名称取决于它是直接从它所在的目录导入，还是通过包导入。导入相同目录或子目录下的模块时会有差别。例如，如果在目录 `package/subpackage1` 启动 Python 解释器，然后 `import moduleX`，此时 `moduleX` 的名称为 `moduleX`，而不是 `package.subpackage1.moduleX`。这是因为当解释器你以交互式方式进入时，Python 会将当前目录添加到搜索路径，如果 Python 在当前路径中找到要导入的模块，就不知道该目录是包的一部分，因此包的信息也不会出现在模块名称中。

**相对导入**

如果模块的名称为 `__main__`，则不被作为在 package 中，因为也没 parent package，此时使用 `from .. import` 语句就会出错。


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
