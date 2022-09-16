# HTTP 请求方法

|方法|说明|
|---|---|
|GET|从指定资源请求页面信息，并返回文档主体|
|HEAD|与 GET 相同，但只返回 HTTP 报头，不返回具体内容|
|POST|向指定资源提交要被处理的数据|
|PUT|从客户端向服务器传送的数据取代指定文档的内容|
|DELETE|删除指定资源|
|CONNECT|把请求连接转换到透明的 TCP/IP 通道|
|OPTIONS|返回服务器支持的 HTTP 方法|
|TRACE|沿着到目标资源的路径执行消息环回测试|
|PATCH|是对 PUT 方法的补充，用来对已知资源进行局部更新|

## RESTful APIs

RESTful 或 REST APIs 是目前使用最广泛的架构模式，是 **Re**presentational **S**tate **T**ransfer 的缩写。

REST APIs 使用 HTTP 的子集定义了 6 个约束准则，满足这些准则的 APIs 就称为  RESTful APIs。

REST APIs 通常只使用 4 种 HTTP 方法：GET, POST, PUT 和 DELETE，是构建网站和 Web API 的主要架构风格：

- GET：用于从服务器选择或检索数据
- POST：用于向服务器发送或写入数据。一般用于发送敏感信息，如凭证、财务数据或大型数据集，如文件。
- PUT：用于更新服务器上已有的数据，例如更新数据库条目，替换文件等。
- DELETE：用于删除服务器上已有数据。


