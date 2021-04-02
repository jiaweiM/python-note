# urllib

- [urllib](#urllib)
  - [简介](#简介)
  - [提取网址](#提取网址)
  - [参考](#参考)

2021-03-29, 09:47
***

## 简介

urllib 用于 URL 的处理：

- `urllib.request` 用于打开和读取 URL
- `urllib.error` 包含 `urllib.request` 抛出的异常
- `urllib.parse` 用于解析 URL
- `urllib.robotparser` 用于解析 `robots.txt` 文件

## 提取网址

使用 `urllib.request` 最简单的方式是：

```py
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
```



## 参考

- [Python 文档](https://docs.python.org/3/library/urllib.html)
- [HOWTO Fetch Internet Resources Using the urllib Package](https://docs.python.org/3/howto/urllib2.html#urllib-howto)
