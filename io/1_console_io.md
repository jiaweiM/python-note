# 控制台 IO

- [控制台 IO](#%e6%8e%a7%e5%88%b6%e5%8f%b0-io)
  - [input](#input)
  - [print](#print)
    - [写入文件](#%e5%86%99%e5%85%a5%e6%96%87%e4%bb%b6)
    - [分隔符及终止符](#%e5%88%86%e9%9a%94%e7%ac%a6%e5%8f%8a%e7%bb%88%e6%ad%a2%e7%ac%a6)

## input

`input()` 函数用于从控制台读入。语法：

```py
input([prompy]) -> string
```

返回值为字符串，对特定类型需要转换。

## print

`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`

将 `objects` 输出到文本流 `file`，以 `sep` 分隔，末尾添加 `end`。

`sep`, `end`, `file` 和 `flush` 需以 keyword 参数形式提供。`sep` 和 `end` 必须为字符串，或者用 `None` 表示默认值。

所有的 non-keyword 参数转换为字符串写入输出流。如果 `objects` 为空，单纯输出 `end`。

`file` 参数必须是包含 `write(string)` 方法的对象；默认为 `sys.stdout`，使用 `None` 表示默认值。因为输出文本流，所以 `print()` 不能用在 binary mode 文件对象。

输出是否缓冲取决于 `file`，但是如果 `flush` 为 true，则强制刷新流。

`print()` 默认分隔符为 "\n"。
格式：

```py
print("my string", end="\n")
```

### 写入文件

通过指定 `file` 参数可以将 `print()` 的输出重定向到文件。例如：

```py
with open('d:/work/test.txt', 'wt') as f:
    print('Hello World!', file=f)
```

这里唯一需要注意的是，文件必须以 "wt" 模式打开。而二进制模式，打印会出错。

### 分隔符及终止符

通过 `print()` 函数的 `sep` 和 `end` 关键字参数，可以设置输出的分隔符和终止符。例如：

```py
>>> print('ACME', 50, 91.5)
ACME 50 91.5
>>> print('ACME', 50, 91.5, sep=',')
ACME,50,91.5
>>> print('ACME', 50, 91.5, sep=',', end='!!\n')
ACME,50,91.5!!
```

使用 `str.join()` 也能相同的任务：

```py
>>> print(','.join(('ACME','50','91.5')))
ACME,50,91.5
```

不过 `str.join()` 问题在于它仅适用于字符串。对非字符串要执行一些换行操作才能正常工作。例如：

```py
>>> row = ('ACME', 50, 91.5)
>>> print(','.join(row))
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: sequence item 1: expected str instance, int found
>>> print(','.join(str(x) for x in row))
ACME,50,91.5
```

而使用 `print()` 要简洁许多：

```py
>>> print(*row, sep=',')
ACME,50,91.5
```

通过 `end` 参数可以在输出中禁止换行。例如：

```py
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>> for i in range(5):
...     print(i, end=' ')
...
0 1 2 3 4
```
