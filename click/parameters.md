# 参数

- [参数](#参数)
  - [简介](#简介)
  - [差别](#差别)
  - [参数类型](#参数类型)
    - [文件路径](#文件路径)
    - [Choice](#choice)
  - [参数名称](#参数名称)
  - [参考](#参考)

***

## 简介

Click 支持两种类型的参数（parameter）：选项（option）和参数（argument）。option 指可选参数，argument 也可以是可选的，但是选项往往限制较大。

建议对子命令或输入文件名、URL 之类的参数使用 argument，而其它内容使用 option。

## 差别

argument 的功能比 option 小。以下功能仅 option 有：

- 自动提示
- 作为 flag (boolean 值)
- 可以从环境变量提取 option 值，argument 不能
- option 在帮助页面有完整的温度，argument 没有

另外，与 option 不同，argument 可以接受任意数量的参数。option 严格来说只接受固定数量的参数（默认为 1）,或者使用多个 option 指定多次。

## 参数类型

- `str` / `click.STRING`

默认参数类型，unicode string。

- `int` / `click.INT`

整数。

- `float` / `click.FLOAT`

浮点数。

- `bool` / `click.BOOL`

布尔参数。对 boolean flag 自动使用。字符串值 “1”, “true”, “t”, “yes”, “y” 和 “on” 自动转换为 `True`；“0”, “false”, “f”, “no”, “n” 和 “off” 自动转换为 `False`.

- `click.UUID`

接受 UUID 参数。不是自动转换，必须表示为 [uuid.UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID)。

```python
class click.File(
    mode='r', 
    encoding=None, 
    errors='strict', 
    lazy=None, atomic=False)
```

将参数声明为文件。离开上下文后（命令执行完）文件会自动关闭。

可以打开文件进行读写，`-` 表示 stdin 或 stdout，根据文件模式 `mode` 进行确定。

默认打开文件读取文本数据，也支持二进制模式或写模式。`encoding` 指定文件编码。

`lazy` flag 指示是立刻打开文件，还是在执行 IO 时再打开。对 stdin 和 stdout 以及以只读模式打开的文件默认为 `non-lazy`，否则为 `lazy`。当以 lazy 模式打开文件进行读操作，会临时打开进行验证，但是在 IO 操作前不会保持打开状态。`lazy` 主要用于打开文件进行写操作。

从 Click 2.0 开始，也可以自动打开文件，此时所有内容写入同一个文件夹下的临时文件，完成后该临时文件移动原始位置。

详情可参考 [File Argument](https://click.palletsprojects.com/en/8.1.x/arguments/#file-args)。

**参数**：

- mode (str)
- encoding (Optional[str])
- errors (Optional[str])
- lazy (Optional[bool])
- atomic (bool)

### 文件路径

```python
class click.Path(
    exists=False, 
    file_okay=True, 
    dir_okay=True, 
    writable=False, 
    readable=True, 
    resolve_path=False, 
    allow_dash=False, 
    path_type=None, 
    executable=False)
```

`Path` 类型与 `File` 类型类似，但是返回的是文件名而不是打开的文件。可以启用各种检查来验证文件类型和权限。

**参数：**

- `exists` (bool) – 检查文件或目录是否存在。如果没有设置为 `True` 且该文件不存在，则跳过余下检查；
- `file_okay` (bool) – 允许参数为文件
- `dir_okay` (bool) – 允许参数为目录
- `readable` (bool) – 检查文件是否可读
- `writable` (bool) – 检查文件是否可以写入
- `executable` (bool) – 检查是否可执行
- `resolve_path` (bool) – 解析可能的符号链接，将路径转换为绝对路径。不解析 `~`，因为该符号一般由 shell 解析
- `allow_dash` (bool) – 是否支持单个破折号 `-`，表示标准流。使用 [open_file()](https://click.palletsprojects.com/en/8.1.x/api/#click.open_file) 处理该值。
- `path_type` (Optional[Type[Any]]) – 将传入路径转换为此类型，`None` 时为默认类型 `str`。用来转换为 `pathlib.Path` 很方便。

例如：

```python
@click.command()
@click.argument('f', type=click.Path(exists=True))
def touch(f):
    click.echo(click.format_filename(f))
```

```powershell
$ touch hello.txt
hello.txt

$ touch missing.txt
Usage: touch [OPTIONS] F

Error: Invalid value for "f": Path "missing.txt" does not exist.
```

### Choice

```python
class click.Choice(choices, case_sensitive=True)
```

该类型支持对一组预定义值进行检查。所有这些值都必须是字符串。

只能传入 list 或 tuple。其它可迭代对象可能出错。

**参数：**

- `case_sensitive` (bool) – 是否区分大小写，默认 true
- `choices` (Sequence[str])

## 参数名称

参数（option 和 argument）有个名称，在调用修饰函数时，该名称会作为 Python 参数名。

argument 只有一个位置名称。想在帮助文本中使用不同名称，可参考 [Truncating Help Texts](https://click.palletsprojects.com/en/8.1.x/documentation/#doc-meta-variables)。

option 可以有多个名称，这些名称可以以一个或两个破折号开头。带一个 `-` 称为短选项，带两个 `--` 称为长选项。没有 `-` 前缀的解析为 argument 名称。Click 将 `-` 转换为下划线来获得 Python 参数名称。

## 参考

- https://click.palletsprojects.com/en/8.1.x/parameters/
