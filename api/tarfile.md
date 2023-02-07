# tarfile

- [tarfile](#tarfile)
  - [简介](#简介)
    - [tarfile.open](#tarfileopen)
    - [tarfile.is\_tarfile](#tarfileis_tarfile)
  - [TarFile](#tarfile-1)
    - [TarFile.getmembers](#tarfilegetmembers)
    - [TarFile.getnames](#tarfilegetnames)
    - [TarFile.extractall](#tarfileextractall)
    - [TarFile.extract](#tarfileextract)
    - [TarFile.extractfile](#tarfileextractfile)
  - [TarInfo](#tarinfo)
    - [属性](#属性)
    - [方法](#方法)
  - [命令行接口](#命令行接口)
  - [示例](#示例)
  - [支持的 tar 格式](#支持的-tar-格式)
  - [Unicode 问题](#unicode-问题)
  - [参考](#参考)

***

## 简介

`tarfile` 模块用于读写 tar 归档文件，包括 gzip, bz2 和 lzma 压缩文件。对 `.zip` 文件使用 `zipfile` 模块，或 `shutil` 中的高级函数。

主要功能：

- 支持 gzip, bz2 和 lzma 压缩格式；
- 支持 POSIX.1-1988 (ustar) 格式的读写；
- 支持 GNU tar 格式（包括 *longname* 和 *longlink* 扩展）的读写，对 `sparse` 扩展，支持读取；
- 支持 POSIX.1-2001 (pax) 格式的读写；
- 能处理目录、常规文件、硬链接、符号链接、fifos、字符设备和 block 设备，并能获取和恢复文件信息，如时间戳、访问权限和所有者。

### tarfile.open

```python
tarfile.open(name=None, 
    mode='r', 
    fileobj=None, 
    bufsize=10240, **kwargs)
```

根据路径名 `name` 创建 `TarFile` 对象。关键字参数可参考下面的 `TarFile` 对象。

`mode` 是 `'filemode[:compression]'` 格式的字符串，默认为 `'r'`。下表是完整的模式组合列表：

| 模式 | 行为 |
|---|---|
| `'r' or 'r:*'` | 读，透明压缩（推荐） |
| `'r:'` | 读，无压缩 |
| `'r:gz'` | 读，gzip 压缩 |
| `'r:bz2'` | 读，bzip2 压缩 |
| `'r:xz'` | 读，lzma 压缩 |
| `'x' or 'x:'` | 创建，无压缩，已有文件抛出 `FileExistsError` |
| `'x:gz'` | 创建，gzip 压缩，已有文件抛出 `FileExistsError` |
| `'x:bz2'` | 创建，bzip2 压缩，已有文件抛出 `FileExistsError` |
| `'x:xz'` | 创建，lzma 压缩，已有文件抛出 `FileExistsError` |
| `'a' or 'a:'` | 追加，无压缩，不存在则创建 |
| `'w' or 'w:'` | 写，无压缩 |
| `'w:gz'` | 写，gzip 压缩 |
| `'w:bz2'` | 写，bzip2 压缩 |
| `'w:xz'` | 写，lzma 压缩 |

> **NOTE**
> 'a:gz', 'a:bz2' 或 'a:xz' 这种组合不可能。如果 `mode` 不适合用来打开某个（压缩）文件，会引发 `ReadError`。使用 'r' 模式可避免该错误。对不支持的压缩方法，引发 `CompressionError`。 

如果指定 `fileobj` 

### tarfile.is_tarfile

```python
tarfile.is_tarfile(name)
```

如果 `name` 是 `tarfile` 支持的 tar 归档文件，返回 `True`。

`name` 可以是 str, file 对象。



## TarFile

`TarFile` 对象提供了 tar 文件接口。tar 文件包含 block 序列。而归档成员（存储的文件）由 header block 和 data block 组成。可以将一个文件多次存储在 tar 文件中。归档成员由 `TarInfo` 对象表示。

`TarFile` 可以在 `with` 语句中使用。当 block 完成时自动关闭。但也有例外，用于 write 的文件不会在出现异常时不会关闭，而仅仅关闭内部使用的文件对象。

```python
class tarfile.TarFile(name=None, 
    mode='r', 
    fileobj=None, 
    format=DEFAULT_FORMAT, 
    tarinfo=TarInfo, 
    dereference=False, 
    ignore_zeros=False, 
    encoding=ENCODING, 
    errors='surrogateescape', 
    pax_headers=None, 
    debug=0, 
    errorlevel=1)
```

### TarFile.getmembers

```python
TarFile.getmembers()
```

以 `TarInfo` 对象列表的形式返回归档文件的成员。

### TarFile.getnames

```python
TarFile.getnames()
```

返回压缩文件中的成员名称列表，顺序与 `getmembers()` 相同。

### TarFile.extractall

### TarFile.extract

```python
TarFile.extract(member, path='', set_attrs=True, *, numeric_owner=False)
```

### TarFile.extractfile

```python
TarFile.extractfile(member)
```

从归档文件中提取一个成员，以文件对象返回。

`member` 可以是文件名或 `TarInfo` 对象：

- 如果 `member` 是常规文件或链接，返回 `io.BufferedReader`
- 对其它成员，返回 `None` 

如果归档文件中没有 `member`，引发 `KeyError`。

## TarInfo

- **TarInfo.isfile()**

### 属性

- **TarInfo.name**

成员名称。

### 方法

- **TarInfo.isfile()**

如果 `Tarinfo` 对象是常规文件，返回 `True`。

- T**arInfo.isreg()**

同 `isfile()`。

## 命令行接口

## 示例

## 支持的 tar 格式

## Unicode 问题

## 参考

- https://docs.python.org/3/library/tarfile.html