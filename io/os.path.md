# os.path

- [os.path](#ospath)
  - [简介](#简介)
  - [os.path..dirname](#ospathdirname)
  - [os.path.join](#ospathjoin)
  - [os.path.exists](#ospathexists)
  - [参考](#参考)

2021-05-31, 09:52
***

## 简介

该模块包含路径操作的诸多函数。对文件读写，参考 `open()`函数；对文件系统相关信息，参考 `os` 模块。path 参数可以为字符串或字节形式。推荐使用字符串。

- 在 Unix 上有些文件名不以字符串表示，所以在 Unix 系统上如果要支持以任意文件名，就需要使用字节表示文件名。
- 在 Windows 系统上部分文件名不能用字节表示，此时应该使用字符串表示所有文件名。

和 Unix shell 不同，Python 不执行任何自动路径扩展，如果需要类似 shell 的路径扩展，可以显示调用 `expanduser()`和 `expandvars()`之类的函数。

## os.path..dirname

```python
os.path.dirname(path)
```

返回路径 `path` 的目录名称。这是 `split()` 函数返回的 pair 的第一个元素。

## os.path.join

```py
os.path.join(path, *paths)
```

连接一个或多个路径。将 `path` 和后面的所有 `*paths` 以目录分隔符 `os.sep` 分隔。如果其中有绝对路径，则舍弃该绝对路径前面的所有组分。

## os.path.exists

```py
os.path.exists(path)
```

检测 `path` 是否指向已有路径或打开的文件描述符。对断开的符号链接，返回 False。在一些平台上，如果没有在被请求的文件上执行 `os.stat()` 的权限，这个函数也可能返回 `False`，即时该路径物理上存在。

## 参考

- https://docs.python.org/3/library/os.path.html
