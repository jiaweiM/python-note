# os

- [os](#os)
  - [简介](#简介)
  - [os.mkdir](#osmkdir)
  - [os.makedirs](#osmakedirs)

## 简介

`os` 模块包含获取本地目录、文件、进程和环境变量的函数。

## os.mkdir

`os.mkdir(path, mode=0o777, *, dir_fd=None)`

以 `mode` 模式创建目录 `path`。

如果目录已存在，抛出 `FileExistsError`。



## os.makedirs

`os.makedirs(name, mode=0o777, exist_ok=False)`

递归创建目录。功能和 `mkdir()` 类似，但是保证所有中间级目录包含叶目录。

