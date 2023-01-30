# 实用工具

## 简介

Click 除了提供参数解析和处理接口的功能外，还提供了一系列插件功能，这些功能对于丰富命令行程序非常重要。

## 打印到 stdout

`echo()` 函数的功能与 `print` 类似，主要区别在于 `echo()` 在许多不同的终端环境中工作方式相同。例如：

```python
import click

click.echo('Hello World!')
```

`echo` 可以输出文本和二进制数据。默认在末尾加一行换行符，设置 `nl=False` 取消换行：

```python
click.echo(b'\xe2\x98\x83', nl=False)
```

另外，`echo()` 在 Windows console 上支持 Unicode 输出（对于能够显示哪些字符，取决于默认字体）。

设置 `err=True` 打印到 stderr：

```python
click.echo('Hello World!', err=True)
```

## ANSI 颜色

`echo()` 函数支持 ANSI 颜色和样式。在 Windows 上使用 [colorama](https://pypi.org/project/colorama/) 实现。

简而言之：

- 如果不是输出到终端。`echo()` 会自动剔除 ANSI 颜色代码；
- 如果输出到终端，`echo()` 会将 ANSI 颜色代码转换为终端 API 调用。

使用 `style()` 函数设置字符串样式：

```python
import click

click.echo(click.style('Hello World!', fg='green'))
click.echo(click.style('Some more text', bg='blue', fg='white'))
click.echo(click.style('ATTENTION', blink=True, bold=True))
```

`echo()` 和 `style()` 的

## 参考

- https://click.palletsprojects.com/en/8.1.x/utils/
