# urllib3

- [urllib3](#urllib3)
  - [发出请求](#发出请求)
  - [Response Content](#response-content)
    - [JSON Content](#json-content)
    - [使用 io Wrapper](#使用-io-wrapper)
  - [Request Data](#request-data)
    - [Query 参数](#query-参数)
  - [参考](#参考)

2022-03-23, 21:46
***

## 发出请求

通过 `PoolManager` 实例发出请求，该类会处理连接池和线程安全等内容，所以你不需要担心这些问题：

```python
http = urllib3.PoolManager()
```

使用 `request()` 发出请求：

```py
r = http.request('GET', 'http://httpbin.org/robots.txt')
assert r.data == b'User-agent: *\nDisallow: /deny\n'
```

`request()` 返回 `HTTPReponse` 对象，[Response Content](#response-content) 部分会解释如何处理各种响应。

`request()` 可以使用任意 HTTP verb 发出请求：

```python
r = http.request(
    'POST',
    'http://httpbin.org/post',
    fields={'hello': 'world'}
)
```

[Request Data] 部分包括发送其它类型的请求数据，包括 JSON，文件和二进制数据。

## Response Content

`HTTPResponse` 对象提供 `status`, `data` 和 `headers` 属性：

```python
>>> r = http.request('GET', 'http://httpbin.org/ip')
>>> r.status
200
>>> r.data
b'{\n  "origin": "104.232.115.37"\n}\n'
>>> r.headers
HTTPHeaderDict({'Content-Length': '33', ...})
```

### JSON Content

### 使用 io Wrapper

有时可能希望使用类似 CSV reader 的`io.TextIOWrapper` 对象直接处理 `HTTPReponse` 数据。要使者两个接口协调一致，需要设置属性 `auto_close=False`。因为 HTTP 响应在读取所有字节后默认关闭，设置后禁用该行为：

```python
>>> import io
>>> r = http.request('GET', 'https://example.com', preload_content=False)
>>> r.auto_close = False
>>> for line in io.TextIOWrapper(r):
>>>     print(line)
```



## Request Data

### Query 参数

对 `GET`, `HEAD` 和 `DELETE` 请求，可以参数可以直接以字典类型放在 `fields` 参数中：

```python
>>> r = http.request(
...     'GET',
...     'http://httpbin.org/get',
...     fields={'arg': 'value'}
... )
>>> json.loads(r.data.decode('utf-8'))['args']
{'arg': 'value'}
```

而 `POST` 和 `PUT` 请求，需要手动将查询参数编码到 URL 中：

```python
>>> from urllib.parse import urlencode
>>> encoded_args = urlencode({'arg': 'value'})
>>> url = 'http://httpbin.org/post?' + encoded_args
>>> r = http.request('POST', url)
>>> json.loads(r.data.decode('utf-8'))['args']
{'arg': 'value'}
```

## 参考

- https://urllib3.readthedocs.io/en/stable/user-guide.html
