# shutil

2022-03-01, 15:53
***

## 简介

`shutil` 模块提供了许多对文件集合和文件夹的高级操作。特别是提供了文件复制和删除函数。对单个文件的操作，可以使用 [os.path](os.path.md) 模块。

## shutil.rmtree

```python
shutil.rmtree(path, ignore_errors=False, onerror=None)
```

删除整个目录树，`path` 必须指向某个目录（不能是指向目录的符号链接）。

如果 `ignore_errors` 为 true，则忽略删除失败导致的错误，如果为 false，这些错误将通过调用 `onerror` 指定的处理程序来处理，如果省略 `onerror`，则引发异常。

## 参考

- https://docs.python.org/3/library/shutil.html
