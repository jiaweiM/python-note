# os.path

- [os.path](#ospath)
  - [简介](#简介)
  - [os.path.join](#ospathjoin)

## 简介

该模块包含路径操作的诸多函数。对文件读写，参考 `open()`函数；对文件系统相关信息，参考 `os` 模块。path 参数可以为字符串或字节形式。推荐使用字符串。

- 在 Unix 上有些文件名不以字符串表示，所以在 Unix 系统上如果要支持以任意文件名，就需要使用字节表示文件名。
- 在 Windows 系统上部分文件名不能用字节表示，此时应该使用字符串表示所有文件名。



和 Unix shell 不同，Python 不执行任何自动路径扩展，如果需要类似 shell 的路径扩展，可以显示调用 `expanduser()`和 `expandvars()`之类的函数。

## os.path.join

`os.path.join(path, *paths)` 连接一个或多个路径。将 `path` 和后面的所有 `*paths` 以目录分隔符 `os.sep` 分隔。如果其中有绝对路径，则舍弃该绝对路径前面的所有组分。
