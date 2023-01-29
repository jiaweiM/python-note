# Click

## 文档

- [快速入门](quickstart.md)
- [Setuptools 集成](setuptools.md)

## 简介

Click 是一个命令行接口创建工具包，只需少量代码就能组合创建漂亮的命令行接口。

Click 支持：

- 命令的任意嵌套
- 自动生成帮助页面
- 支持在运行时延迟加载子命令

下面是一个简单示例：

```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
```

运行时的样子：

```powershell
$ python hello.py --count=3
Your name: John
Hello John!
Hello John!
Hello John!
```

自动生成格式良好的帮助页面：

```powershell
$ python hello.py --help
Usage: hello.py [OPTIONS]

  Simple program that greets NAME for a total of COUNT times.

Options:
  --count INTEGER  Number of greetings.
  --name TEXT      The person to greet.
  --help           Show this message and exit.
```

## 安装

```powershell
pip install click
```

## 参考

- https://click.palletsprojects.com/en/8.1.x/
