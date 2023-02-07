# os

- [os](#os)
  - [简介](#简介)
  - [文件名、命令行参数和环境变量](#文件名命令行参数和环境变量)
  - [UTF-8 模式](#utf-8-模式)
  - [参数处理](#参数处理)
  - [创建文件对象](#创建文件对象)
  - [文件描述符操作](#文件描述符操作)
  - [文件和目录](#文件和目录)
  - [进程管理](#进程管理)
  - [Scheduler 接口](#scheduler-接口)
  - [其它系统信息](#其它系统信息)
  - [随机数](#随机数)
  - [os.mkdir](#osmkdir)
  - [os.makedirs](#osmakedirs)
  - [os.walk](#oswalk)
  - [参考](#参考)

2021-05-31, 09:53
***

## 简介

`os` 提供了使用操作系统相关功能，包含获取本地目录、文件、进程和环境变量的函数。

注意事项：

- Python 内置的所有系统相关操作，只要有相同功能可用，就使用相同的接口；例如 `os.stat(path)` 

## 文件名、命令行参数和环境变量

## UTF-8 模式

## 参数处理

这些函数和数据提供当前进程和用户相关信息和操作。

## 创建文件对象

## 文件描述符操作

## 文件和目录

## 进程管理

## Scheduler 接口

这些函数控制操作系统如何分配进程的 CPU 时间，仅在某些 Unix 平台可用。

## 其它系统信息

## 随机数



## os.mkdir

```python
os.mkdir(path, mode=0o777, *, dir_fd=None)
```

以 `mode` 模式创建目录 `path`。

如果目录已存在，抛出 `FileExistsError`。

在某些系统上，`mode` 会被忽略，此时使用会被忽略。

## os.makedirs

`os.makedirs(name, mode=0o777, exist_ok=False)`

递归创建目录。功能和 `mkdir()` 类似，但是保证所有中间级目录包含叶目录。

## os.walk

对目录下的所有文件夹，生成三项值的 tuple：dirpath, dirnames, filenames。

| **返回值** | **说明** |
| --- | --- |
| dirpath | 目录路径 |
| dirnames | 子目录名称 |
| filenames | 所有的文件名 |

返回的名称仅仅包含名称，如果要获得完整路径：`os.path.join(dirpath, name)`

## 参考

- https://docs.python.org/3/library/os.html
