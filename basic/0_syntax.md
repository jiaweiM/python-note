# 基本语法

- [基本语法](#%e5%9f%ba%e6%9c%ac%e8%af%ad%e6%b3%95)
  - [简介](#%e7%ae%80%e4%bb%8b)
- [Python 控制语句](#python-%e6%8e%a7%e5%88%b6%e8%af%ad%e5%8f%a5)
- [注释](#%e6%b3%a8%e9%87%8a)
  - [单行注释](#%e5%8d%95%e8%a1%8c%e6%b3%a8%e9%87%8a)
- [包（package）](#%e5%8c%85package)
  - [导入包](#%e5%af%bc%e5%85%a5%e5%8c%85)
    - [导入模块](#%e5%af%bc%e5%85%a5%e6%a8%a1%e5%9d%97)
    - [导入具体模块](#%e5%af%bc%e5%85%a5%e5%85%b7%e4%bd%93%e6%a8%a1%e5%9d%97)
    - [导入模块具体对象](#%e5%af%bc%e5%85%a5%e6%a8%a1%e5%9d%97%e5%85%b7%e4%bd%93%e5%af%b9%e8%b1%a1)

## 简介

不同编程工具，有不同的定位，下面是 Python 的功能定位。
1. 网站业务逻辑的开发  
Python 有一个优良的网页开发框架 django， django 支持各种主流数据库，有好用的 orm 系统和模板系统，完善的第三方库能帮助解决遇到的大部分问题。并且支持各种操作系统。
2. 数据分析和科学计算  
Python 有 NumPy, SciPy 等一大批科学计算库，有 Pandas 数据分析库，还有 Matplotlib 等绘图库，在科学计算和数据分析领域已经成为主流语言。
3. 网络爬虫  
Scrapy 作为 Python 实现的爬虫库，被广泛使用，同时 Python 还拥有 beatifulsoup，pyquery 等 html 解析库，requests 网络库可以用来做爬取和分析用途。
4. 自动化运维  
主流的操作系统都集成有 Python，同时自动化运维领域主流技术栈 saltstack 和 ansible 也是基于 Python 技术开发。可以使用 Python 打造强大的自动化运维工具。

**Java能做什么？**  
1. 大数据分析  
Java 拥有完整的大数据技术体系，包括但不限于 Hadoop, hbase, spark, storm 用来处理海量数据。
2. 分布式集群  
Java 有大量功能完善的分布式服务中间件，避免重新开发此类服务。这些中间件包括 zookeeper, Kafka, hdfs 等等
3. 搜索引擎  
搜索引擎目前也是 Java 一家独霸， Java 的 elastic search 是目前最好的开源搜索引擎，此外围绕 elastic search 的 elk 日志分析工具也已经形成了生态链，发挥着越来越多的用途。

所以从上述分析可以看出，Python 更适合用在创业开发或者对业务变化需求非常高的公司。而 Java 更适合对业务要求稳定，并且有海量数据需要处理的公司！

# Python 控制语句
if … else …
if … elif … else

A if B else C
如果B为 True, 执行A，否则执行C。

`Switch`:Python 没有 switch 语句

# 注释
注释，是模块、函数、类或方法定义的第一行文本，为对象的 `__doc__` 属性值。

## 单行注释
```py
# a comment
```

# 包（package）
管理 Python 代码的方法有多种，从小到大分别为：
- 函数（functions）
- 类（classes）
- 模块（modules）
- 包（packages）

Python 模块，即一个Python 文件，里面包含函数、变量、类、常量等。模块方便代码的管理。

一个package 可以包含多个模块。每个 package 都包含一个 `__init__.py` 文件。`__init__.py` 文件可以为空，也可以通过设置 `__all__` 变量进行部分包的初始化工作。

## 导入包
语法：
`from package import item` 导入具体的子模块、包或者包中定义的函数、类和变量。

### 导入模块
语法：
```py
import sound.effects.echo
```
使用：
```py
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

一次导入多个模块：
```py
import module_name_1, module_name_2
```

### 导入具体模块
语法：
```py
from sound.effects import echo
```
使用：
```py
echo.echofilter(input, output, delay=0.7, atten=4)
```

### 导入模块具体对象
语法：
```py
from sound.effects.echo import echofilter
```
使用：
```py
echofilter(input, output, delay=0.7, atten=4)
```