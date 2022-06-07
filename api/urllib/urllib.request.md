# urllib.request

2022-03-23, 21:31
***

## 简介

`urllib.request` 模块定义了打开 URL 的函数和类。

## 遗留接口

以下函数和类是从 Python 2 的 `urllib` 模块移植来的，在未来某个时候可能会被弃用。

### urllib.request.urlretrieve

```python
urllib.request.urlretrieve(url, filename=None, reporthook=None, data=None)
```

将 URL 表示的网络对象复制到本地文件。如果 URL 指向本地文件，则除非提供 `filename`，否则不会复制对象。返回 `(filename, headers)` tuple，其中 `filename` 为保存对象位置，`headers` 是 `urlopen()` 方法返回的对象的 `info()` 返回的信息。





## 参考

- https://docs.python.org/3/library/urllib.request.html
