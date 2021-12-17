# 快速入门

- [快速入门](#快速入门)
  - [生成 Request](#生成-request)
  - [在 URL 中传递参数](#在-url-中传递参数)
  - [Response Content](#response-content)
  - [参考](#参考)

2021-12-14, 18:22
***

## 生成 Request

首先导入 Requests 模块：

```python
>>> import requests
```

然后，获取网页。例如，获得 GitHub 的 public timeline 页面：

```python
>>> r = requests.get('https://api.github.com/events')
```

现在我们有了一个名为 `r` 的 `Response` 对象。我们可以从该对象获得所需的所有信息。

Requests 的 API 设计以简单为主。例如，发出 HTTP POST 请求：

```python
>>> r = requests.post('https://httpbin.org/post', data={'key': 'value'})
```

其它类型的 HTTP 请求：PUT, DELETE, HEAD 以及 OPTIONS

```python
>>> r = requests.put('https://httpbin.org/put', data={'key': 'value'})
>>> r = requests.delete('https://httpbin.org/delete')
>>> r = requests.head('https://httpbin.org/get')
>>> r = requests.options('https://httpbin.org/get')
```

## 在 URL 中传递参数

如果手动构造 URL，则可以将数据以键值对的形式在 URL 后面的问号中给出，例如 `httpbin.org/get?key=val`。Requests 提供以字符串 dict 提供参数的功能，以 `params` 关键字参数给出。例如：

```python
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('https://httpbin.org/get', params=payload)
```

输出 URL，可以看到 URL 已被正确编码：

```python
>>> print(r.url)
https://httpbin.org/get?key2=value2&key1=value1
```

dict 中值为 `None` 的键值被忽略，不添加到 URL 的 query 字符串中。

值可以为 list 类型：

```python
>>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
>>> r = requests.get('https://httpbin.org/get', params=payload)
>>> print(r.url)
https://httpbin.org/get?key1=value1&key2=value2&key2=value3
```

## Response Content

可以读取服务器响应的内容。

## 参考

- https://docs.python-requests.org/en/latest/user/quickstart/
