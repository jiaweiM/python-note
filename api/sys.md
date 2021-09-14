# sys

- [sys](#sys)
  - [简介](#简介)
  - [sys.argv](#sysargv)
  - [sys.exit](#sysexit)
  - [sys.path](#syspath)
  - [sys.version](#sysversion)

2021-03-26, 10:10
***

## 简介

`sys` 模块提供解释器使用或维护的一些变量的访问功能，以及和解释器交互的一些函数。

## sys.argv

包含传递给 Python 脚本的命令行参数列表。

- `argv[0]` 是脚本名称。

## sys.exit

退出 Python 程序。

## sys.path

包含模块搜索路径的列表。由环境变量 `PYTHONPATH` 初始化，加上安装依赖的默认值。

在程序启动时，该列表的第一项 `path[0]` 是执行脚本所在的目录。如果脚本所在目录不可用（如以交互式调用解释器，或从标准输入读取脚本），则 `path[0]` 为空。

可以根据需求修改该列表，不过只接受字符串和 bytes 类型，其他类型自动忽略。

## sys.version

字符串，包含 Python 的版本号，构建号以及编译器的附加信息。例如：

```py
import sys

print(sys.version)

# 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)]
```
