# 快速入门

- [快速入门](#快速入门)
  - [创建命令](#创建命令)
  - [Echo](#echo)
  - [嵌套命令](#嵌套命令)
  - [注册命令](#注册命令)
  - [添加参数](#添加参数)
  - [setuptools](#setuptools)
  - [参考](#参考)

Last updated: 2023-01-29, 10:51
****

## 创建命令

Click 通过装饰器声明命令，Click 也提供非装饰器接口，但不适合常规使用。

使用 `click.command()` 装饰函数，使其成为命令行工具。简而言之，只要用这个修饰器修饰一个函数，它就变成一个可调用的脚本，例如：

```python
import click

@click.command()
def hello():
    click.echo("Hello World!")

if __name__ == '__main__':
    hello()
```

运行效果：

```powershell
$ python hello.py
Hello World!
```

对应的帮助页面：

```powershell
$ python hello.py --help
Usage: hello.py [OPTIONS]

Options:
  --help  Show this message and exit.
```

## Echo

上面的 `echo()` 函数等价于跨平台的 `print()` 函数，使得 Click 再不同平台都能正常输出信息。

`echo` 还支持输出中不同颜色和样式。如果输出流为文件，则自动删除样式。在 Windows 中，会自动安装 colorama，详情可参考 [ANSI Colors](https://click.palletsprojects.com/en/8.1.x/utils/#ansi-colors)。

如果不需要这些功能，可以继续使用 `print() `函数。

## 嵌套命令

命令可以附加到 `Group` 类型的命令中，从而进行嵌套。例如，下面实现了两个用于管理数据库的命令：

```python
@click.group()
def cli():
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)
```

`group()` 装饰的使用与 `command()` 类似，但是 `Group` 对象支持多个子命令，用 `Group.add_command()` 添加这些子命令。

对简单的脚本，可以直接使用 `Group.command()` 装饰器来自动附加和创建命令。因此，上面的脚本可以修改为：

```python
@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo('Initialized the database')

@cli.command()
def dropdb():
    click.echo('Dropped the database')
```

然后在 setuptools 入口等地方调用 `Group`：

```python
if __name__ == '__main__':
    cli()
```

## 注册命令

除了使用 `@group.command()` 装饰器，也可以先用 `@click.command()` 装饰，然后再用 `group.add_command()` 注册子命令。这样便于将命令拆分为多个 Python 模块。

```python
@click.command()
def greet():
    click.echo("Hello, World!")
```

```python
@click.group()
def group():
    pass

group.add_command(greet)
```

## 添加参数

使用 `option()` 和 `argument()` 装饰器添加参数：

```python
@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")
```

命令形式：

```powershell
$ python hello.py --help
Usage: hello.py [OPTIONS] NAME

Options:
  --count INTEGER  number of greetings
  --help           Show this message and exit.
```

## setuptools

上面的示例在文件末尾都有一个 `if __name__ == '__main__':` 的代码块，在独立的 Python 脚本中经常使用，在 Click 中也可以使用，但是通过 setuptools 可以实现更好的方法。

主要原因有两个：

1. setuptools 可以为 Windows 生成可执行程序，这样命令行程序也能在 Windows 上运行
2. setuptools 脚本可以在 Unix 上使用 virtualenv，但是不用激活该环境

在阅读 余下教程之前，建议先看看 setuptools 集成这一章。

## 参考

- https://click.palletsprojects.com/en/8.1.x/quickstart/