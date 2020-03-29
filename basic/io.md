# Python IO

- [Python IO](#python-io)
  - [简介](#%e7%ae%80%e4%bb%8b)
- [函数](#%e5%87%bd%e6%95%b0)
- [控制台IO](#%e6%8e%a7%e5%88%b6%e5%8f%b0io)
  - [print()](#print)
  - [os.walk()](#oswalk)
- [文件 IO](#%e6%96%87%e4%bb%b6-io)
  - [打开文件](#%e6%89%93%e5%bc%80%e6%96%87%e4%bb%b6)
    - [模式](#%e6%a8%a1%e5%bc%8f)
    - [Buffering](#buffering)
  - [读写后，关闭文件：](#%e8%af%bb%e5%86%99%e5%90%8e%e5%85%b3%e9%97%ad%e6%96%87%e4%bb%b6)
  - [写操作](#%e5%86%99%e6%93%8d%e4%bd%9c)
  - [读操作](#%e8%af%bb%e6%93%8d%e4%bd%9c)
  - [循环读取数据](#%e5%be%aa%e7%8e%af%e8%af%bb%e5%8f%96%e6%95%b0%e6%8d%ae)
  - [二进制读写](#%e4%ba%8c%e8%bf%9b%e5%88%b6%e8%af%bb%e5%86%99)

## 简介

文件是磁盘上命名地址，用于存储相关信息，用于将数据永久存储在非易失性存储器中。随机存取存储器（random access memory, RAM）是易失性的，计算机关机后数据丢失，因此我们都是使用文件存储数据。

# 函数

|函数|功能|
|---|---|
|os.chdir(dir)	|修改当前工作目录为指定路径|
|os.getcwd()	|返回当前工作目录|
|os.getcwdb()	|以二进制对象的形式返回当前工作目录|
|os.mkdir(dir)	|创建一个新的文件夹|
|os.path.exists(a_path)	|检查文件是否存在|
|os.path.isfile(a_path)	|检查路径下是否是文件|
|os.path.isdir(a_path)	|检查路径下是否是目录|
|os.rename(old_name, new_name)	|重命名文件或目录|
|os.rmdir(dir)	|移除文件或目录。如果目录包含文件，则移除目录失败|
|os.rmtree(dir)	|移除目录及其内的所有文件|

# 控制台IO
`input()` 函数用于从控制台读入。语法：
```py
input([prompy]) -> string
```
返回值为字符串，对特定类型需要转换。

## print()
`print()` 默认分隔符为 "\n"。
格式：
```py
print("my string", end="\n")
```

## os.walk()
对目录下的所有文件夹，生成三项值的 tuple：dirpath, dirnames, filenames。

|返回值|说明|
|---|---|
|dirpath	|目录路径|
|dirnames	|子目录名称|
|filenames	|所有的文件名|

返回的名称仅仅包含名称，如果要获得完整路径：`os.path.join(dirpath, name)`

# 文件 IO
Python 操作文件的步骤：
1. 打开文件
2. 读写操作
3. 关闭文件

|函数|说明|
|---|---|
|open()	|根据指定路径的文件，返回流用于读写|
|close()	|关闭文件。如果文件已关闭，调用无效|
|detach()	|将底层二进制缓冲区和 `TextIOBase` 分开并返回|
|fileno()	|返回文件的一个整数描述值|
|flush()	|flush 输出缓冲到文件流|
|isatty()	|如果文件流为交互式，返回True|
|read([number])|读取指定数目的字符。如果无参数，则读取整个文件|
|readable()	|如果文件流可读，返回 True|
|readline()	|读取下一行|
|readline(n=-1)	|从文件中读取一行，如果指定了 n，则最多读取 n 个字节|
|readlines(n=-1)|	读取所有行，以string 数组返回，如果指定了 n，则最多读取 n个字节|
|seek(offset, from=SEEK_SET)	|参照 `from` 位置设置文件指针 `offset`|
|seekable()|如果文件支持随机访问，返回 True|
|tell()|返回当前指针位置|
|truncate(size=None)|将文件流大小调整为 `size` 个字节。如果 `size` 不指定，则设置到当前位置|
|writable()	|如果文件流可写入，返回 True|
|write(s)	|将字符串写入文件，返回写入的字符数|
|writelines(lines)|写入多行文本到文件|

## 打开文件
```py
f = open(filename, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
```
> filename

文件路径, 必选

> encoding

编码名，可选;只用在 text 模式。默认是当前平台编码，在 `codecs` 模块中可以看到所有支持的编码

> errors

编码错误，可选;

只用于 text mode。
- `strict` 碰到编码错误抛出 ValueError, 默认 None 效果等同。
- `ignore`, 忽略编码错误

> newline

换行符，可选。

只用在 text mode。可选值有 '', '\n', '\r', '\r\n'.

对输入：
- 如果 newline 为 None，开启 universal newlines mode，即 '\n', '\r', '\r\n' 均作为换行符处理，然后转换为 '\n' 返回。
- 如果 newline 为 '', 通上，但是不转换换行符。
- 如果是以上其他值，则只根据指定值换行。

对输出：
- 如果 newline 为 None, 则 '\n' 转换为 os.linesep
- 如果是 '' 或 '\n'，则不执行转换
- 如果是其他值，则 '\n' 转换为对应字符串。

> closefd

关闭 file descriptor；默认为False。

### 模式
|mode|说明|
|---|---|
|r|read, 读文本（default）|
|w|write, 写文本，如果文件已在，则先清除文件内容|
|x|创建并写入新文件，如果文件已存在，抛出 FileExistsError|
|a|append, 追加数据到文件末尾|
|b|binary mode, 用于处理二进制文件|
|t|text mode, 作为文本文件操作(default)|
|+|open a disk file for updating (reading and writing)|

如果未指定 encoding，则使用平台默认编码。

|组合模式|说明|
|---|---|
|wb	|写 binary mode|
|rb	|读 binary mode|
|rt|open for reading text (default)|
|w+b|open and truncates the file to 0 bytes|
|r+b|open the file without truncation|

### Buffering
可选的整数参数
- 0, 关闭缓存（只用在 binary mode）
- 1, 行缓存（只用在 text mode）
- `>1`, 表示固定大小（fixed-size chunk）的缓存

默认策略：
- Binary 文件以固定大小进行缓存，如 4096 或 8192
- Text 文件一般以行缓存。

## 读写后，关闭文件：
```py
f.close()
```

这种关闭文件的方式，不是很保险。如果前面的代码抛出异常，代码运行不到这一步，此时可以使用 `try…finally` 语句：
```py
try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
```
这样就可以保证文件的关闭。

而最简单的方式，是使用 `with` 语句，`with` 语句能保证在代码运行完其内部分，文件被关闭，即使发生异常：
```py
with open("test.txt",encoding = 'utf-8') as f:
   # perform file operations
```


## 写操作
`w`, `a`, `x` 三种模式支持写操作。写入数据使用`write()` 函数
```py
f = open("myfile.txt", 'w') # 写模式
f.write('first line\n')
f.write('second line\n')
f.close()
```

## 读操作
读取所有数据：
```py
f = open('myfile.txt', 'r')
f.read()  # read entire content of file at once
f.close()
```

以字符串数组形式返回读取所有行：
```py
f = open("myfile.txt", 'r')
f.readlines()  # read entire content of file at once
f.close()
```

## 循环读取数据
```py
f = open('myfile.txt', 'r')
for line in f:
	print(line)
f.close()
```

## 二进制读写
使用 `pickle` 模块读写二进制文件。

写入二进制数据：
```py
import pickle
f = open('pick.dat', 'wb')
pickle.dump(11, f)
pickle.dump("this is a line", f)
pickle.dump([1, 2, 3, 4], f)
f.close()
```

读取二进制数据：
```py
import pickle
f = open('pick.dat', 'rb')
pickle.load(f)
# 11
pickle.load(f)
# [1, 2, 3, 4]
f.close()
```