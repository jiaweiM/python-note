# Setuptools 集成

- [Setuptools 集成](#setuptools-集成)
  - [引言](#引言)
  - [简介](#简介)
  - [测试脚本](#测试脚本)
  - [Package 中的脚本](#package-中的脚本)
  - [参考](#参考)

Last updated: 2023-01-29, 11:11
****

## 引言

对命令行程序，建议将其编写为模块，并使用 setuptools 分发。

主要有以下几点原因：

1. 传统方法的一个问题是 Python 解释器加载的第一个模块名称有问题。

第一个模块不是通过它的实际名称来调用的，解释器将其重命名为 `__main__`。如果另一段代码想要从该模块导入，它会以真实名称第二次出发导入，即被导入两次。

2. 不是所有平台都容易执行。

在 Linux 和 OS X 上，在文件的开头添加注释 `#!/usr/bin/env python`，脚本就能以类似可执行文件的方式执行。但是在 Windows 不行。虽然可以将 `.py` 扩展文件与 Python 解释器关联，这样就能双击执行，但是无法放切换解释器，即无法在 virtualenv 中执行。

实时上，在 OS X 和 Linux 平台，在 virtualenv 运行脚本也有问题。使用传统方法，你需要激活整个 virtualenv 以确保使用正确的 Python 解释器。

## 简介

要将脚本与 setuptools 绑定，只需要配置好 `setup.py` 文件。

假设目录结构为：

```powershell
yourscript.py
setup.py
```

`yourscript.py` 的内容为：

```python
import click

@click.command()
def cli():
    """Example script."""
    click.echo('Hello World!')
```

`setup.py` 的内容为：

```python
from setuptools import setup

setup(
    name='yourscript',
    version='0.1.0',
    py_modules=['yourscript'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'yourscript = yourscript:cli',
        ],
    },
)
```

关键在于 `entry_points` 参数。在 `console_scripts` 下，每一行对应一个命令行脚本:

- 等号前面是应该生成的脚本名称;
- 等号后面是冒号分隔的 Click 命令。

## 测试脚本

可以创建一个虚拟环境来测试脚本：

```powershell
$ virtualenv venv
$ . venv/bin/activate
$ pip install --editable .
```

然后调用命令：

```powershell
$ yourscript
Hello World!
```

## Package 中的脚本

假设目录结构为：

```powershell
project/
    yourpackage/
        __init__.py
        main.py
        utils.py
        scripts/
            __init__.py
            yourscript.py
    setup.py
```

此时 `setup.py` 中不用 `py_modules` 参数，而是改用 `packages` 参数，然后用 setuptools 的自动查找 package 功能。

此时的 `setup.py`：

```python
setup(
    name='yourpackage',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'yourscript = yourpackage.scripts.yourscript:cli',
        ],
    },
)
```

## 参考

- https://click.palletsprojects.com/en/8.1.x/setuptools/