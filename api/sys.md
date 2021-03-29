# sys

- [sys](#sys)
  - [简介](#简介)
  - [sys.argv](#sysargv)
  - [sys.exit](#sysexit)
  - [sys.version](#sysversion)

2021-03-26, 10:10
***

## 简介

`sys` 模块提供使用或维护的一些变量，以及和解释器交互的一些函数。

## sys.argv

包含传递给 Python 脚本的命令行参数列表。

- `argv[0]` 是脚本名称。

## sys.exit

退出 Python 程序。



## sys.version

字符串，包含 Python 的版本号，构建号以及编译器的附加信息。例如：

```py
import sys

print(sys.version)

# 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)]
```
