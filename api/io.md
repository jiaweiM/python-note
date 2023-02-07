# io

- [io](#io)
  - [概述](#概述)
    - [Text I/O](#text-io)
    - [Binary I/O](#binary-io)
  - [文本编码](#文本编码)
  - [模块接口](#模块接口)
  - [类](#类)
    - [I/O 基类](#io-基类)
      - [io.IOBase](#ioiobase)
    - [Raw File I/O](#raw-file-io)
      - [io.FileIO](#iofileio)
    - [Buffered Streams](#buffered-streams)
      - [io.BytesIO](#iobytesio)
      - [io.BufferedReader](#iobufferedreader)
      - [io.BufferedWriter](#iobufferedwriter)
      - [io.BufferedRandom](#iobufferedrandom)
      - [io.BufferedRWPair](#iobufferedrwpair)
    - [Text I/O](#text-io-1)
      - [io.TextIOBase](#iotextiobase)
      - [io.TextIOWrapper](#iotextiowrapper)
      - [io.StringIO](#iostringio)
  - [性能](#性能)
  - [参考](#参考)

***

## 概述

io 模块是 Python 处理各类 I/O 的主要工具。主要有三种类型的 I/O：text I/O, binary I/O 和 raw I/O。属于这些类别中任意具体对象称为文件，也称为流（stream）或类文件对象。

每个具体流对象具有各自功能，有只读的、只写的，或读写；有支持随机访问的，也有只能按顺序访问。

### Text I/O

Text I/O 处理 `str` 对象。由于文件总是以字节存储，文本 I/O 数据的编码和解码是透明的，还有特定于平台的换行符选项。

`open()` 是创建文本流的最简单方法，还可以指定编码：

```python
f = open("myfile.txt", "r", encoding="utf-8")
```

内存中的文本流使用 `StringIO` 对象：

```python
f = io.StringIO("some initial text data")
```

### Binary I/O

Binary I/O (也称为 buffered I/O) 处理 bytes 对象。

## 文本编码

## 模块接口

## 类

### I/O 基类

#### io.IOBase

```python
class io.IOBase
```

### Raw File I/O

#### io.FileIO

### Buffered Streams

缓冲 I/O 流，为 I/O 设备提供了比 raw I/O 更高级的接口。

#### io.BytesIO

#### io.BufferedReader

```python
class io.BufferedReader(raw, buffer_size=DEFAULT_BUFFER_SIZE)
```

缓冲二进制流，提供对可读、不可搜索的 `RawIOBase` 二进制流的高级访问。继承自 `BufferedIOBase`。

当从该对象读取数据时，它可能从底层 raw stream 请求更多数据，并保存在内部缓冲区中。缓冲的数据在后续读取时直接返回。

构造函数使用指定可读 *raw* stream 和 `buffer_size` 创建 `BufferedReader`。其中 `buffer_size` 默认为 `io.DEFAULT_BUFFER_SIZE`。

除了从 `BufferedIOBase` 和 `IOBase` 继承的方法，`BufferedReader` 提供或覆盖了如下方法：

- **peek(size=0, /)**

从流中返回字节，但不更新位置。返回的字节数可能比请求的多或少。

- **read(size=- 1, /)**

读取并返回 `size` 个字节，如果 `size` 为负数或未指定，则读取所有字节知道 EOF。

#### io.BufferedWriter

#### io.BufferedRandom

#### io.BufferedRWPair

### Text I/O

#### io.TextIOBase

```python
class io.TextIOBase
```

文本流的基类。该类为流 I/O 提供基于字符和行的接口。继承自 `IOBase`。

#### io.TextIOWrapper

#### io.StringIO

```python
class io.StringIO(initial_value='', newline='\n')
```

基于内存缓冲区的文本流。继承自 `TextIOBase`。

调用 `close()` 方法，文本缓冲区被丢弃。

缓冲区的初始值通过 `initial_value` 设置。

## 性能



## 参考

- https://docs.python.org/3/library/io.html