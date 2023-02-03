# os.path

- [os.path](#ospath)
  - [简介](#简介)
  - [os.path.dirname](#ospathdirname)
  - [os.path.isfile](#ospathisfile)
  - [os.path.join](#ospathjoin)
  - [os.path.exists](#ospathexists)
  - [os.path.realpath](#ospathrealpath)
  - [参考](#参考)

2021-05-31, 09:52
***

## 简介

该模块包含路径操作的诸多函数。对文件读写，参考 [open()](python_io.md#open) 函数；若要访问文件系统，参考 [os](../api/os.md) 模块。path 参数可以为字符串或字节类型。推荐使用字符串（Unicode）表示文件名，然而：

- 在 Unix 上有些文件名不以字符串表示，所以在 Unix 系统上如果要支持以任意文件名，就需要使用字节表示文件名。
- 在 Windows 系统上部分文件名不能用字节表示，此时应该使用字符串表示所有文件名。

和 Unix shell 不同，Python 不执行任何自动路径扩展，如果需要类似 shell 的路径扩展，可以显示调用 `expanduser()`和 `expandvars()`之类的函数。

|方法|说明|
|---|---|
|os.path.abspath(path)|返回绝对路径|
|os.path.basename(path)|返回文件名|
|os.path.commonprefix(list)|返回list(多个路径)中，所有path共有的最长的路径|
|`os.path.dirname(path)`|返回 `path` 的目录名|
|os.path.exists(path)|如果路径 path 存在，返回 True；如果路径 path 不存在，返回 False。|
|os.path.lexists|路径存在则返回True,路径损坏也返回True|
|os.path.expanduser(path)|把path中包含的"~"和"~user"转换成用户目录|
|os.path.expandvars(path)|根据环境变量的值替换path中包含的"$name"和"${name}"|
|os.path.getatime(path)|返回最近访问时间（浮点型秒数）|
|os.path.getmtime(path)|返回最近文件修改时间|
|os.path.getctime(path)|返回文件 path 创建时间|
|os.path.getsize(path)|返回文件大小，如果文件不存在就返回错误|
|os.path.isabs(path)|判断是否为绝对路径|
|os.path.isfile(path)|判断路径是否为文件|
|os.path.isdir(path)|判断路径是否为目录|
|os.path.islink(path)|判断路径是否为链接|
|os.path.ismount(path)|判断路径是否为挂载点|
|`os.path.join(path, *paths)`|把目录和文件名合成一个路径|
|os.path.normcase(path)|转换path的大小写和斜杠|
|os.path.normpath(path)|规范path字符串形式|
|os.path.realpath(path)|返回path的真实路径|
|os.path.relpath(path[, start])|从start开始计算相对路径|
|os.path.samefile(path1, path2)|判断目录或文件是否相同|
|os.path.sameopenfile(fp1, fp2)|判断fp1和fp2是否指向同一文件|
|os.path.samestat(stat1, stat2)|判断stat tuple stat1和stat2是否指向同一个文件|
|os.path.split(path)|把路径分割成 dirname 和 basename，返回一个元组|
|os.path.splitdrive(path)|一般用在 windows 下，返回驱动器名和路径组成的元组|
|os.path.splitext(path)|分割路径，返回路径名和文件扩展名的元组|
|os.path.splitunc(path)|把路径分割为加载点与文件|
|os.path.walk(path, visit, arg)|遍历path，进入每个目录都调用visit函数，visit函数必须有3个参数(arg, dirname, names)，dirname表示当前目录的目录名，names代表当前目录下的所有文件名，args则为walk的第三个参数|
|os.path.supports_unicode_filenames|设置是否支持unicode路径名|

## os.path.dirname

```python
os.path.dirname(path)
```

返回路径 `path` 的目录名称。这是 `split()` 函数返回的 pair 的第一个元素。

## os.path.isfile

```python
os.path.isfile(path)
```

如果 `path` 是常规文件，返回 `True`。对符号链接也算，因此对相同路径，`islink()` 和 `isfile()` 都可能返回 `True`。

## os.path.join

```py
os.path.join(path, *paths)
```

连接一个或多个路径。将 `path` 和后面的所有 `*paths` 以目录分隔符 `os.sep` 分隔。如果其中有绝对路径，则舍弃该绝对路径前面的所有组分。

## os.path.exists

```py
os.path.exists(path)
```

检测 `path` 是否指向已有路径或打开的文件描述符。对断开的符号链接，返回 False。在一些平台上，如果没有在被请求的文件上执行 `os.stat()` 的权限，这个函数也可能返回 `False`，即时该路径物理上存在。

## os.path.realpath

```python
os.path.realpath(path, *, strict=False)
```

返回指定文件名的规范路径，消除路径中的符号链接。

如果路径不存在，或者遇到循环符号链接，并且 `strict` 为 `True`，则抛出 `OSError`。如果 `strict` 为 `False`，则尽可能解析路径，余下部分直接放在末尾，不检查路径是否存在。



## 参考

- https://docs.python.org/3/library/os.path.html
