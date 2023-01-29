# sys

- [sys](#sys)
  - [简介](#简介)
  - [解释器设置](#解释器设置)
    - [解释器实现](#解释器实现)
    - [命令行选项](#命令行选项)
    - [默认 Unicode](#默认-unicode)
    - [交互提示](#交互提示)
  - [sys.argv](#sysargv)
  - [sys.exit](#sysexit)
  - [sys.path](#syspath)
  - [sys.stdin, stdout, stderr](#sysstdin-stdout-stderr)
    - [stderr](#stderr)
    - [stdin](#stdin)
  - [应用](#应用)
  - [参考](#参考)

2021-03-26, 10:10
***

## 简介

`sys` 模块提供解释器信息访问和交互功能。

## 解释器设置

`sys` 包含访问解释器编译时或运行时配置的属性和函数。

解释器版本有多种形式：

- `sys.version`，可读字符串，通常包含Python版本号、构建日期、编译器和平台。
- `sys.hexversion`，一个整数，便于用来检查解释器版本。
- `sys.version_info`，包含版本号的 namedtuple (长度 5)。
- `sys.api_version`，当前解释器使用的 C API 版本。

```python
import sys

print('Version info:')
print()
print('sys.version =', repr(sys.version))
print('sys.version_info =', sys.version_info)
print('sys.hexversion =', hex(sys.hexversion))
print('sys.api_version =', sys.api_version)
```

```txt
Version info:

sys.version = '3.9.15 (main, Nov 24 2022, 14:39:17) [MSC v.1916 64 bit (AMD64)]'
sys.version_info = sys.version_info(major=3, minor=9, micro=15, releaselevel='final', serial=0)
sys.hexversion = 0x3090ff0
sys.api_version = 1013
```

- 构建解释器的平台保存在 `sys.platform`

```python
print('This interpreter was built for:', sys.platform)
```

```txt
This interpreter was built for: win32
```

### 解释器实现

CPython 解释器是 Python 语言的几个实现之一。`sys.implementation` 提供当前解释器实现信息：

```python
print('Name:', sys.implementation.name)
print('Version:', sys.implementation.version)
print('Cache tag:', sys.implementation.cache_tag)
```

```txt
Name: cpython
Version: sys.version_info(major=3, minor=9, micro=15, releaselevel='final', serial=0)
Cache tag: cpython-39
```

对 CPython，`sys.implementation.version` 和 `sys.version_info` 相同，对其它解释器实现则可能不同。

### 命令行选项

CPython 解释器支持多个命令选项来设置其行为，如下表所示。其中一些选项可以通过 `sys.flags` 检查。

|选项|属性|功能|
|---|---|---|
|-B|dont_write_bytecode|在导入模块时不写入 .pyc 文件|
|-b|bytes_warning|当比较 bytes 或 bytearray 与 str 或 bytes 和 int 时发出警告，指定两次 `-bb` 则发出错误|
|-d|debug|启用 parser debug 输出|
|-E|ignore_environment|忽略 PYTHON* 环境变量，如 `PYTHONPATH`|
|-i|interactive|当脚本为第一个参数，或使用 `-c` 选项，在执行脚本或命令后进行交互模式|
|-O|optimize|删除 assert 语句和以 `__debug__` 值为条件的代码|
|-OO|optimize|除了执行 `-O` 优化，还要删除 docstrings|
|-s|no_user_site|不将用户站点目录添加到 `sys.path`|
|-S|no_site|初始化时不运行 “import site”|
|-v|Verbose||

```python
import sys

if sys.flags.bytes_warning:
    print('Warning on bytes/str errors')
if sys.flags.debug:
    print('Debuging')
if sys.flags.inspect:
    print('Will enter interactive mode after running')
if sys.flags.optimize:
    print('Optimizing byte-code')
if sys.flags.dont_write_bytecode:
    print('Not writing byte-code files')
if sys.flags.no_site:
    print('Not importing "site"')
if sys.flags.ignore_environment:
    print('Ignoring environment')
if sys.flags.verbose:
    print('Verbose mode')
```

使用解释器选项 -S -E -b 运行，输出：

```txt
Warning on bytes/str errors
Not importing "site"
Ignoring environment
```

### 默认 Unicode

`getdefaultencoding()` 返回解释器使用的默认 Unicode 编码。该值在解释器启动时设置，启动后不能更改。

对部分操作系统，内部默认编码和文件系统编码可能不同，`getfilesystemencoding()` 返回将 Unicode 文件名转换为 OS 文件名的编码。

```python
print('Default encoding :', sys.getdefaultencoding())
print('File system encoding :', sys.getfilesystemencoding())
```

```txt
Default encoding : utf-8
File system encoding : utf-8
```

### 交互提示



## sys.argv

包含传递给 Python 脚本的命令行参数列表。

- `argv[0]` 是脚本名称。

## sys.exit

退出 Python 程序。

## sys.path

包含模块搜索路径的列表。由环境变量 `PYTHONPATH` 初始化，加上安装依赖的默认值。

在程序启动时，该列表的第一项 `path[0]` 是执行脚本所在的目录。如果脚本所在目录不可用（如以交互式调用解释器，或从标准输入读取脚本），则 `path[0]` 为空。

可以根据需求修改该列表，不过只接受字符串和 bytes 类型，其他类型自动忽略。


## sys.stdin, stdout, stderr

解释器使用的标准输入、输出和错误文件对象：

- `stdin` 用于所有交互输入（包括 `input()` 调用）；
- `stdout` 用于 `print()` 的输出以及 `input()` 的提示信息输出；
- `stderr` 用于解释器的提示信息和错误信息输出。

### stderr

stderr 即标准错误流，它和 stdout 类似，都是向控制台输出信息，不同之处在于 stderr 只输出错误信息。例如：

```py
sys.stderr.write('This is an error message')
```

### stdin

`stdin` 是 Python 的标准输入流，用于从


## 应用

- 确定 Python 版本不低于 3.9

```python
import sys

assert sys.version_info >= (3, 9)
```

## 参考

- https://docs.python.org/3/library/sys.html
