# urllib3

## 发出请求

通过 `PoolManager` 实例发出请求，该类还处理连接池和线程安全等内容。使用 `request()` 发出请求，如下所示：

```py
import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')
assert r.data == b'User-agent: *\nDisallow: /deny\n'
```

`request()` 返回 `HTTPReponse` 对象，