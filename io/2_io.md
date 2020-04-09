# File IO

- [File IO](#file-io)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [open](#open)
  - [返回值](#%e8%bf%94%e5%9b%9e%e5%80%bc)
  - [关闭文件](#%e5%85%b3%e9%97%ad%e6%96%87%e4%bb%b6)
  - [write](#write)
  - [read](#read)
  - [seek](#seek)
  - [tell](#tell)
  - [逐行读取](#%e9%80%90%e8%a1%8c%e8%af%bb%e5%8f%96)
  - [二进制读写](#%e4%ba%8c%e8%bf%9b%e5%88%b6%e8%af%bb%e5%86%99)
  - [读写文本数据](#%e8%af%bb%e5%86%99%e6%96%87%e6%9c%ac%e6%95%b0%e6%8d%ae)
  - [StringIO](#stringio)

## 简介

`io` 模块是 Python 处理 I/O 的主要模块。主要有三种类型的 I/O：text I/O, binary I/O 和 raw I/O。

Python 操作文件的步骤：

1. 打开文件
2. 读写操作
3. 关闭文件

| 函数                        | 说明                                                                   |
| --------------------------- | ---------------------------------------------------------------------- |
| close()                     | 关闭文件。如果文件已关闭，调用无效                                     |
| detach()                    | 将底层二进制缓冲区和 `TextIOBase` 分开并返回                           |
| fileno()                    | 返回文件的一个整数描述值                                               |
| flush()                     | flush 输出缓冲到文件流                                                 |
| isatty()                    | 如果文件流为交互式，返回True                                           |
| read([number])              | 读取指定数目的字符。如果无参数，则读取整个文件                         |
| readable()                  | 如果文件流可读，返回 True                                              |
| readline()                  | 读取下一行                                                             |
| readline(n=-1)              | 从文件中读取一行，如果指定了 n，则最多读取 n 个字节                    |
| readlines(n=-1)             | 读取所有行，以string 数组返回，如果指定了 n，则最多读取 n个字节        |
| seek(offset, from=SEEK_SET) | 参照 `from` 位置设置文件指针 `offset`                                  |
| seekable()                  | 如果文件支持随机访问，返回 True                                        |
| tell()                      | 返回当前指针位置                                                       |
| truncate(size=None)         | 将文件流大小调整为 `size` 个字节。如果 `size` 不指定，则设置到当前位置 |
| writable()                  | 如果文件流可写入，返回 True                                            |
| write(s)                    | 将字符串写入文件，返回写入的字符数                                     |
| writelines(lines)           | 写入多行文本到文件                                                     |

## open

```py
f = open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

打开文件，返回对应的文件对象。如果文件无法打开，抛出 `OSError`。

1. file

path-like 文件路径（绝对路径，或相对当前工作目录的相对路径），或者要包装文件的 integer 文件描述符。

如果使用文件描述符，当返回的 I/O 对象关闭，描述符也随之关闭，除非将 `closefd` 设置为 `False`。

2. mode

mode 为打开文件的模式。

| mode | 说明                                                   |
| ---- | ------------------------------------------------------ |
| 'r'  | 读，文本（default）                                    |
| 'w'  | 写，如果文件已在，则先清除文件内容                     |
| 'x'  | 创建并写入新文件，如果文件已存在，抛出 FileExistsError |
| 'a'  | append, 追加数据到文件末尾                             |
| 'b'  | binary mode, 用于处理二进制文件                        |
| 't'  | text mode, 作为文本文件操作(default)                   |
| '+'  | 更新 (reading and writing)                             |

| 组合模式 | 说明                                   |
| -------- | -------------------------------------- |
| wb       | 写 binary mode                         |
| rb       | 读 binary mode                         |
| rt       | open for reading text (default)        |
| w+b      | open and truncates the file to 0 bytes |
| r+b      | open the file without truncation       |

```py
f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode
```

Python 区别 binary 和 text I/O。

- 以 binary （`b`）模式打开的文件，不经过任何解码，直接返回 `bytes` 对象。
- 以 text (`t`) 模式打开的文件，文件内容以 `str` 形式打开，首先使用平台对应的编码或指定的编码解码 bytes。

3. buffering

可选的整数参数，用于设置缓存策略：

- 0, 关闭缓存（仅限 binary mode）
- 1, 行缓存（仅限 text mode）
- `>1`, 表示固定大小（fixed-size chunk）的缓存

默认策略：

- Binary 文件以固定大小进行缓存，如 4096 或 8192
- Text 文件一般以行缓存。

4. encoding

编码名，只用在 text 模式。默认是当前平台编码，最好不要依赖于默认编码。在 `codecs` 模块中可以看到支持的所有编码。

在文本模式，如果未指定编码，通过 `locale.getpreferredencoding(False)` 获得平台特异性的编码。在 windows 中为 `'cp1252'`，在 Linux 中为 `'utf-8'`。

对 binary 模式，不需要指定编码。

5. errors

编码错误处理方式;

处理编码错误的方式，binary 模式无需编码，所以不需要，只适用于 text 模式。

常见标准错误处理方式：

| 名称        | 描述                                                 |
| ----------- | ---------------------------------------------------- |
| `'strict'`  | 对编码错误抛出 `ValueError`，和默认的 `None`效果一样 |
| `'ignore'`  | 忽略错误                                             |
| `'replace'` | 对格式不对的地方用标记替换，如 '?'                   |
|`'surrogateescape'`|用 Unicode 专用区 (U+DC80-U+DCFF)编码替代不正确的 bytes；在写入数据时使用 `'surrogateescape'` 可以将其转换为原字节|
|`'xmlcharrefreplace'`|仅支持写模式。不支持的字符以 XML 字符引用替代|
|`'backslashreplace'`|错误数据以 Python 斜杠转移序列代替|
|`'namereplace'`|仅支持写模式，不支持的以 `\N{...}` 转移序列替代|

6. newline

换行符。

只用在 text mode。可选值有 `None`, `''`, '\n', '\r', '\r\n'.

默认为 `None`，即以统一模式处理换行符。

对输入：

- 如果 `newline` 为 `None`，开启统一换行模式 (universal newlines mode)，即 '\n', '\r', '\r\n' 均作为换行符处理，然后转换为 '\n' 返回。
- 如果 `newline` 为 `''`, 同上，但是不转换换行符。
- 如果是以上其他值，则只根据指定值换行。

对输出：

- 如果 `newline` 为 `None`, 则 '\n' 转换为 `os.linesep`
- 如果是 '' 或 '\n'，则不转换
- 如果是其他值，则 `'\n'` 转换为对应字符串。

7. closefd

关闭 file descriptor；默认为False。

## 返回值

`open()` 函数的返回值依赖于 mode。

对文本模式（'w', 'r', 'wt', 'rt'），返回 `io.TextIOBase` 的子类（特别是 `io.TextIOWrapper`）

## 关闭文件

```py
f = open("test.txt",encoding = 'utf-8')
# perform file operations
f.close()
```

这种关闭文件的方式，不是很保险。如果前面的代码抛出异常，代码运行不到这一步就退出，文件没有关闭。

更为安全的方式是使用 `try…finally` 语句：

```py
try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
```

这样就可以保证文件的关闭。

而最简单的方式，是使用 `with` 语句，`with` 语句能保证在代码运行完文件被关闭，即使发生异常：

```py
with open("test.txt",encoding = 'utf-8') as f:
   # perform file operations
```

## write

`w`, `a`, `x` 三种模式支持写操作。写入数据使用`write()` 函数

```py
f = open("myfile.txt", 'w') # 写模式
f.write('first line\n')
f.write('second line\n')
f.close()
```

## read

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

读取指定数目的字符：

```py
file = open('data.txt', encoding='utf-8')
a = file.read(3)
assert a == 'lin'
```

## seek

`seek` 设置读取位置。

例如：

```py
with open("helloworld.txt", encoding='utf-8') as file:
    a_string = file.read()
    assert a_string == 'Hello world'
    # 到文件末尾，就读取返回空字符串
    b_string = file.read()
    assert b_string == ''
    # 设置读取位置
    file.seek(0)
    b_string = file.read()
    assert b_string == 'Hello world'
```

## tell

`tell()` 返回当前位置。

```py
with open('helloworld.txt', encoding='utf-8') as file:
    assert file.tell() == 0
    assert file.read(1) == 'H'
    assert file.tell() == 1
```

## 逐行读取

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

## 读写文本数据

读写文本文件的方式是使用 `open()` 函数创建文本流，文本数据对应模式 `t`，读数据 `rt`：

```py
# Read the entire file as a single string
with open('somefile.txt', 'rt') as f:
    data = f.read()

# Iterate over the lines of the file
with open('somefile.txt', 'rt') as f:
    for line in f:
        # process line
        ...
```

写入文本数据 `wt`:

```py
# Write chunks of text data
with open('somefile.txt', 'wt') as f:
    f.write(text1)
    f.write(text2)
    ...

# Redirected print statement
with open('somefile.txt', 'wt') as f:
    print(line1, file=f)
    print(line2, file=f)
    ...
```

如果文件已存在，向其中添加模式，使用 `at` 模式。

对内存中文本流，可以使用 `StringIO` 对象：

## StringIO

`class io.StringIO(initial_value='', neline='\n')`
