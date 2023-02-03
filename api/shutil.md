# shutil

- [shutil](#shutil)
  - [简介](#简介)
  - [目录和文件操作](#目录和文件操作)
    - [shutil.rmtree](#shutilrmtree)
  - [归档操作](#归档操作)
  - [](#)
  - [参考](#参考)


2022-03-01, 15:53
***

## 简介

`shutil` 模块提供了许多对文件集合和文件夹的高级操作。特别是提供了文件复制和删除函数。对单个文件的操作，可以使用 [os.path](os.path.md) 模块。

## 目录和文件操作

### shutil.rmtree

```python
shutil.rmtree(path, ignore_errors=False, onerror=None, *, dir_fd=None)
```

删除整个目录树，`path` 必须指向某个目录（不能是指向目录的符号链接）。

`ignore_errors` 为 true 时忽略删除失败导致的错误；为 false 时使用`onerror` 指定的函数处理错误；如果省略 `onerror`，则引发异常。

## 归档操作

## 

## 参考

- https://docs.python.org/3/library/shutil.html
