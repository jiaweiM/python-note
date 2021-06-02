# os

- [os](#os)
  - [简介](#简介)
  - [os.mkdir](#osmkdir)
  - [os.makedirs](#osmakedirs)
  - [os.walk](#oswalk)

2021-05-31, 09:53
@Jiawei Mao
***

## 简介

`os` 模块包含获取本地目录、文件、进程和环境变量的函数。

## os.mkdir

`os.mkdir(path, mode=0o777, *, dir_fd=None)`

以 `mode` 模式创建目录 `path`。

如果目录已存在，抛出 `FileExistsError`。

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