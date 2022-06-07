# 快速入门

- [快速入门](#快速入门)
  - [生成 Request](#生成-request)
  - [在 URL 中传递参数](#在-url-中传递参数)
  - [Response Content](#response-content)
  - [Binary Response Content](#binary-response-content)
  - [JSON Response Content](#json-response-content)
  - [Raw Response Content](#raw-response-content)
  - [自定义 Headers](#自定义-headers)
  - [更复杂的 POST 请求](#更复杂的-post-请求)
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

`r` 是 `Response` 对象，我们所需的所有信息都从该对象获取。

Requests 的 API 设计以简单为主。所有的 HTTP 请求都显而易见。例如，发出 HTTP POST 请求：

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

如果手动构造 URL，则可以将数据以键值对的形式在 URL 后面的问号中给出，例如 `httpbin.org/get?key=val`。Requests 支持以字符串 dict 提供参数，以 `params` 关键字参数给出。例如：

```python
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('https://httpbin.org/get', params=payload)
```

输出 URL，可以看到 URL 已被正确编码：

```python
>>> print(r.url)
https://httpbin.org/get?key2=value2&key1=value1
```

参数 dict 中值为 `None` 的键值被忽略，不添加到 URL 的 query 字符串中。

值可以为 list 类型：

```python
>>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
>>> r = requests.get('https://httpbin.org/get', params=payload)
>>> print(r.url)
https://httpbin.org/get?key1=value1&key2=value2&key2=value3
```

## Response Content

可以读取服务器响应的内容。考虑 GitHub 时间轴页面：

```python
>>> import requests

>>> r = requests.get('https://api.github.com/events')
>>> r.text
'[{"repository":{"open_issues":0,"url":"https://github.com/...
```

request 会自动从服务器解码内容。大多数 unicode 字符集无缝解码。

当你发出请求，request 会根据 HTPP headers 猜测响应的编码。当访问 `r.text` 时，request 使用猜测的编码解码内容。使用 `r.encoding` 属性可以访问或修改编码：

```python
>>> r.encoding
'utf-8'
>>> r.encoding = 'ISO-8859-1'
```

如果更改编码，在调用 `r.text` 时 request 将使用新的 `r.encoding` 值。你可能希望在任何时候都能使用特殊的逻辑来计算内容编码，例如，HTML 和 XML 可以在 body 中指定编码，此时，你可以使用 `r.content` 来查找编码，然后设置 `r.encoding`。这样你就可以使用正确编码的 `t.text`。

在需要时 request 还能使用自定义编码。如果你创建了自己的编码，并使用 `codecs` 模块进行注册，则可以直接使用 codec 名称作为 `r.encoding` 的值，request 会自动处理解码。

## Binary Response Content

对非文本请求，可以以字节的形式访问响应正文：

```python
>>> r.content
b'[{"repository":{"open_issues":0,"url":"https://github.com/...
```

`gzip` 和 `deflate` 传输编码会自动解码。

如果安装了 brotli 或 brotlicffi 之类的 Brotli 库，`br` 传输编码也会自动进行解码。

例如，使用 request 返回的二进制数据创建图像，可以使用如下代码：

```python
>>> from PIL import Image
>>> from io import BytesIO

>>> i = Image.open(BytesIO(r.content))
```

## JSON Response Content

request 有一个内置的 JSON 解码器：

```python
>>> import requests

>>> r = requests.get('https://api.github.com/events')
>>> r.json()
[{'repository': {'open_issues': 0, 'url': 'https://github.com/...
```

如果 JSON 解码失败，`r.json()` 会抛出异常。例如，如果响应得到 204（No Content），或者响应包含无效的 JSON，此时使用 `r.json()` 抛出 `requests.exceptions.JSONDecodeError`。这个包装器异常为不同 Python 版本和 json 序列化库引发的多个异常提供了互操作性。

需要注意的是，调用 `r.json()` 成功不表示响应成功。有些服务器对失败响应可能返回 JSON 对象（例如 HTTP 500 的详细错误信息）。这种 JSON 被解码并返回。要检查 request 是否成功，使用 `r.raise_for_status()` 或检查 `r.status_code`。

## Raw Response Content

在少数情况下，你需要从服务器获取原始套接字响应，可以范围 `r.raw`。如果要执行该操作，确保在初始请求中设置 `stream=True`。如下：

```python
>>> r = requests.get('https://api.github.com/events', stream=True)
>>> r.raw
<urllib3.response.HTTPResponse object at 0x101194810>

>>> r.raw.read(10)
'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
```

通常情况下，应该使用下面的方式来保存内容到文件：

```python
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```

使用 `Response.iter_content` 比直接使用 `Response.raw` 更方便。在流式下载传输时，以上是查询内容的推荐方法。其中 `chunk_size` 是自由调整。

> `Response.iter_content` 会自动解码 `gzip` 和 `deflate` 传输编码。`Response.raw` 是原始字节流，它不会转换响应内容。如果你缺失需要访问返回的字节，使用 `Response.raw`。

## 自定义 Headers

如果你想向请求添加 HTTP headers，只需向 `headers` 参数传递一个 `dict` 。

例如，在上例中，我们没有指定用户代理：

```python
>>> url = 'https://api.github.com/some/endpoint'
>>> headers = {'user-agent': 'my-app/0.0.1'}

>>> r = requests.get(url, headers=headers)
```

自定义 headers 优先级低于更具体的信息源。例如：

- `auto=` 参数优先级高于 `.netrc` 参数文件，高于 `headers=` 设置的凭据。request 会在 `~/.netrc`, `~/_netrc` 或 `NETRC` 环境变量指定的路径查找 netrc 文件。
- 如果你被重定向出主机，则授权 header 将被删除；
- 代理授权 header 会被 URL 中提供的代理凭据覆盖；
- 当我们可以确定内容的长度时，content-length headers 会被覆盖。

> header 值支持类型 `string`, bytestring 或 unicode。建议避免使用 unicode header 值。

## 更复杂的 POST 请求

发送表单数据，只需向 `data` 参数传递一个字典。在发出请求时，自定的数据将自动进行表单编码：

```python
>>> payload = {'key1': 'value1', 'key2': 'value2'}

>>> r = requests.post("https://httpbin.org/post", data=payload)
>>> print(r.text)
{
  ...
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
  ...
}
```

`data` 参数的每个 key 可以有多个值。可以将 `data` 设置为 tuple 列表或以 list 作为值的 dict 实现。当表单中有多个值使用相同 key 时尤其有用：

```python
>>> payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
>>> r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
>>> payload_dict = {'key1': ['value1', 'value2']}
>>> r2 = requests.post('https://httpbin.org/post', data=payload_dict)
>>> print(r1.text)
{
  ...
  "form": {
    "key1": [
      "value1",
      "value2"
    ]
  },
  ...
}
>>> r1.text == r2.text
True
```

如果要发送非表单数据，可以传递 `string` 而不是 `dict`，这样数据就直接发布。

例如，GitHub API v3 接受 JSON 编码的 POST/PATCH 数据：

```python
>>> import json

>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}

>>> r = requests.post(url, data=json.dumps(payload))
```


## 参考

- https://docs.python-requests.org/en/latest/user/quickstart/
