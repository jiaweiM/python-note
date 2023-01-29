# Options

- [Options](#options)
  - [简介](#简介)
  - [Option 命名](#option-命名)
  - [基本值 option](#基本值-option)
  - [多值 option](#多值-option)
  - [Tuple 类型 option](#tuple-类型-option)
  - [多次 Option](#多次-option)
  - [计数](#计数)
  - [Boolean Flag](#boolean-flag)
  - [特性切换](#特性切换)
  - [环境变量](#环境变量)
  - [多个环境变量](#多个环境变量)
  - [参考](#参考)

***

## 简介

option 使用 `option()` 装饰器添加。由于 option 有不同的版本，所以有大量的参数可以配置它们的行为。

## Option 命名

Option 包含一个名称，在调用修饰函数时用作 Python 参数名。该名称可以从 option 名称推断出来，也可以显式给出。

按如下顺序选择名称:

1. 如果包含无前缀名称，将其作为 Python 参数名，但不作为命令行中的 option 名称；
2. 如果包含以 `--` 开头的名称，则将第一个作为 option 名称；
3. 否则使用第一个以 `-` 开头的名称。

将选择的名称转换为小写，然后最多将前面两个 `-` 删除，其它 `-` 转换为下划线，就获得了 Python 参数名。

```python
@click.command()
@click.option('-s', '--string-to-echo')
def echo(string_to_echo):
    click.echo(string_to_echo)
```

```python
@click.command()
@click.option('-s', '--string-to-echo', 'string')
def echo(string):
    click.echo(string)
```

例如：

|选项|Python 参数名称|
|---|---|
|"-f", "--foo-bar"|`foo_bar`|
|"-x"|`x`|
|"-f", "--filename", "dest"|`dest`|
|"--CamelCase"|camelcase|
|"-f", "-fb"|f|
|"--f", "--foo-bar"|f|
|"---f"|_f|

## 基本值 option

对基本类型 option，如果没有指定类型，则使用默认值的类型。如果没有提供默认值，则默认为 `STRING`。

如果没有显式指定名称，参数名为定义的第一个长选项，否则使用第一个短选项。option 默认不是必需的，使用 `required=True` 设置为必需参数。

```python
@click.command()
@click.option('--n', default=1)
def dots(n):
    click.echo('.' * n)
```

```python
# How to make an option required
@click.command()
@click.option('--n', required=True, type=int)
def dots(n):
    click.echo('.' * n)
```

```python
# How to use a Python reserved word such as `from` as a parameter
@click.command()
@click.option('--from', '-f', 'from_')
@click.option('--to', '-t')
def reserved_param_name(from_, to):
    click.echo(f"from {from_} to {to}")
```

命令：

```powershell
$ dots --n=2
..
```

此时该选项的类型为 `INT`，因为默认值是整数。

- 使用 `show_default=True` 在帮助信息中显示默认值

```python
@click.command()
@click.option('--n', default=1, show_default=True)
def dots(n):
    click.echo('.' * n)
```

```powershell
$ dots --help
Usage: dots [OPTIONS]

Options:
  --n INTEGER  [default: 1]
  --help       Show this message and exit.
```

- 对单个 boolean flag，如果默认为 `False`，则隐藏该默认值

```python
@click.command()
@click.option('--n', default=1, show_default=True)
@click.option("--gr", is_flag=True, show_default=True, default=False, help="Greet the world.")
@click.option("--br", is_flag=True, show_default=True, default=True, help="Add a thematic break")
def dots(n, gr, br):
    if gr:
        click.echo('Hello world!')
    click.echo('.' * n)
    if br:
        click.echo('-' * n)
```

```powershell
$ dots --help
Usage: dots [OPTIONS]

Options:
  --n INTEGER  [default: 1]
  --gr         Greet the world.
  --br         Add a thematic break  [default: True]
  --help       Show this message and exit.
```

## 多值 option

option 支持固定数量的参数，使用 `nargs` 设置。这些值存储在 tuple 中。

```python
@click.command()
@click.option('--pos', nargs=2, type=float)
def findme(pos):
    a, b = pos
    click.echo(f"{a} / {b}")
```

```powershell
$ findme --pos 2.0 3.0
2.0 / 3.0
```

## Tuple 类型 option

使用 `nargs` 设置的多个参数，只能是相同类型。而使用 tuple 类型参数，则没有此限制：

```python
@click.command()
@click.option('--item', type=(str, int))
def putitem(item):
    name, id = item
    click.echo(f"name={name} id={id}")
```

```powershell
$ putitem --item peter 1338
name=peter id=1338
```

以 tuple 字面量为类型，会自动将 `nargs` 设置为 tuple 长度，并使用 `click.Tuple` 类型。上例等价于：

```python
@click.command()
@click.option('--item', nargs=2, type=click.Tuple([str, int]))
def putitem(item):
    name, id = item
    click.echo(f"name={name} id={id}")
```

## 多次 Option

多次提供一个参数，使用 `multiple` flag：

```python
@click.command()
@click.option('--message', '-m', multiple=True)
def commit(message):
    click.echo('\n'.join(message))
```

```powershell
$ commit -m foo -m bar
foo
bar
```

设置 `multiple=True` 提供 `default`，默认值类型必须是 list 或 tuple：

```python
@click.option("--format", multiple=True, default=["json"])
```

## 计数

极少数情况，使用重复选项来计数。这可以用来设置 verbose flag，例如：

```python
@click.command()
@click.option('-v', '--verbose', count=True)
def log(verbose):
    click.echo(f"Verbosity: {verbose}")
```

```powershell
$ log -vvv
Verbosity: 3
```

## Boolean Flag

布尔 flag 是可以开启或关闭的选项。这可以通过一次定义两个 flag 来实现，两个选项用 `/` 分开。如果 option 字符串中存在 `/`，Click 会将其识别为 boolean flag，隐式设置 `is_flag=True`。Click 推荐同时提供启用和关闭 flag，以便设置默认值。

```python
import sys

@click.command()
@click.option('--shout/--no-shout', default=False)
def info(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!111'
    click.echo(rv)
```

```powershell
$ info --shout
LINUX!!!!111
$ info --no-shout
linux
$ info
linux
```

- 如果确实不想要关闭 flag，则需要显式定义 `is_flag`

```python
import sys

@click.command()
@click.option('--shout', is_flag=True)
def info(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!111'
    click.echo(rv)
```

```powershell
$ info --shout
LINUX!!!!111
$ info
linux
```

- 如果 option 中已经有一个 `/`，还可以用 `;` 分隔

```python
@click.command()
@click.option('/debug;/no-debug')
def log(debug):
    click.echo(f"debug={debug}")

if __name__ == '__main__':
    log()
```

- 如果只想为第二个选项定义别名，则需要在前面加一个空格

```python
import sys

@click.command()
@click.option('--shout/--no-shout', ' /-S', default=False)
def info(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!111'
    click.echo(rv)
```

```powershell
$ info --help
Usage: info [OPTIONS]

Options:
  --shout / -S, --no-shout
  --help                    Show this message and exit.
```

## 特性切换

除了 boolean flag，还有一个特性切换功能。为同一个参数定义多个 option 并设置一个 flag 值。注意，设置 `flag_value` Click 会自动设置 `is_flag=True`。

```python
import sys

@click.command()
@click.option('--upper', 'transformation', flag_value='upper',
              default=True)
@click.option('--lower', 'transformation', flag_value='lower')
def info(transformation):
    click.echo(getattr(sys.platform, transformation)())
```

```powershell
$ info --upper
LINUX
$ info --lower
linux
$ info
LINUX
```

## 环境变量

除了常规参数，Click 还能接受来自环境变量的参数。Click 提供了两种方式，一种是自动构建环境变量，只支持 option。需要在脚本中传入 `auto_envvar_prefix` 参数启用该功能。然后每个命令和参数都以下划线分隔的大写变量形式添加。例如，如果你有一个名为 `run` 的子命令，它有一个 `reload` 选项，前缀是 `WEB`，那么变量为 `WEB_RUN_RELOAD`。

```python
@click.command()
@click.option('--username')
def greet(username):
    click.echo(f'Hello {username}!')

if __name__ == '__main__':
    greet(auto_envvar_prefix='GREETER')
```

```powershell
$ export GREETER_USERNAME=john
$ greet
Hello john!
```




## 多个环境变量

如果 `multiple` 和 `nargs` 不为 1，Click 会调用 `ParamType.split_envvar_value()` 来拆分环境变量。

所有类型默认使用空格拆分。`File` 和 `Path` 例外，它们根据操作系统的路径分隔规则进行拆分。

## 参考

- https://click.palletsprojects.com/en/8.1.x/options/
