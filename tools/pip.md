# pip

- [pip](#pip)
  - [简介](#简介)
  - [更新 pip](#更新-pip)
  - [包管理](#包管理)
    - [安装包](#安装包)
    - [从 Wheels 安装](#从-wheels-安装)
    - [查看包](#查看包)
    - [卸载包](#卸载包)
    - [options](#options)
      - [`--user`](#--user)
  - [pip 镜像](#pip-镜像)
    - [临时使用镜像](#临时使用镜像)
    - [设置默认镜像](#设置默认镜像)
  - [Requirements Files](#requirements-files)
    - [Requirements 文件格式](#requirements-文件格式)
  - [Requirement Specifiers](#requirement-specifiers)
  - [ensurepip](#ensurepip)
    - [命令行接口](#命令行接口)
  - [参考](#参考)

2020-04-13, 05:42
****

## 简介

Python 打包系统的核心是 Python Packaging Index (PyPI)。PyPI 是一个庞大的公共资源库，其中大部分是可以免费使用的 Python 项目。

pip 是 Python 包管理工具。

Python 2>=2.7.9 和 Python 3 >= 3.4 自动安装了 pip，

## 更新 pip

- Linux 或 macOS

```bash
pip install --upgrade pip
```

- Windows

```bash
python -m pip install -U pip
```

## 包管理

### 安装包

pip 支持从 PyPI、版本控制、本地项目和分发文件安装包。安装命令：

```bash
pip install SomePackage # 默认安装最新版
pip install SomePackage==1.0.4 # 安装特定版本
pip install 'SomePackage>=1.0.4' # 执行最低版本
```

### 从 Wheels 安装

"Wheel" 是一种 Python 内置存档格式，与从源码构建、安装相比，使用 wheel 要快许多。

```bash
pip install SomePackage-1.0-py2.py3-none-any.whl
```

### 查看包

- 显示已安装包

```bash
pip list
```

- 显示可更新包

```bash
pip list --outdated
```

- 显示已安装包的详细信息

```bash
pip show 'package_name'
```

更新：`-U, --upgrade` 更新

```bash
pip install --upgrade packagename
```

### 卸载包

```bash
pip uninstall packagename
```

在更新时，pip会自动卸载旧版本、安装新版本。

### options

#### `--user`

安装到 Python 用户安装目录。在 Windows 上通常为 `~/.local/` 或者 `%APPDATA%Python`。

通常包会被安装到系统的 site-packages 目录，路径类似 “/usr/local/lib/python3.3/site-packages”。 不过，这样做需要有管理员权限并且使用sudo命令。 就算你有这样的权限去执行命令，使用sudo去安装一个新的，可能没有被验证过的包有时候也不安全。

安装包到用户目录中通常是一个有效的方案，它允许你创建一个自定义安装。

比如你想要安装一个第三方包，但是没有权限将它安装到系统Python库中去；或者，你想要安装一个供自己使用的包，而不是系统上面所有用户。

Python有一个用户安装目录，通常类似 `~/.local/lib/python3.3/site-packages`。要强制在这个目录中安装包，可使用安装选项“-–user”。例如：

```bash
python3 setup.py install --user
```

或者：

```bash
pip install --user packagename
```

在 sys.path 中用户的 “site-packages” 目录位于系统的 “site-packages” 目录之前。 因此，你安装在里面的包就比系统已安装的包优先级高 （尽管并不总是这样，要取决于第三方包管理器，比如distribute或pip）。

另外，你还可以创建一个虚拟环境。

## pip 镜像

pypi 镜像以固定时间间隔同步，比如清华大学镜像 5 分钟同步一次。

PyPI 官方源：[https://pypi.org/simple/](https://pypi.org/simple/)

|镜像|地址|
|---|---|
|北京外国语大学|https://mirrors.bfsu.edu.cn/pypi/|
|清华大学|https://pypi.tuna.tsinghua.edu.cn/simple/|
|豆瓣|https://pypi.doubanio.com/simple/|
|阿里云|https://mirrors.aliyun.com/pypi/simple/|

### 临时使用镜像

```bash
pip install some-package -i https://mirrors.aliyun.com/pypi/simple/
```

### 设置默认镜像

升级 pip 到最新版：

```bash
pip install pip -U
```

配置默认镜像：

```bash
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

## Requirements Files

"Requirements files" 包含需要使用 `pip install` 安装的包，例如：

```bash
py -m pip install -r requirements.txt
```

简而言之，requirements 文件包含需要通过 pip 安装的依赖包列表。

requirements 文件有以下 4 种常见用途：

1. requirements 文件保存 `pip freeze` 结果，以实现可重复安装。此时 requirements 文件包含 `pip freeze` 运行时所有包的指定版本。

```bash
py -m pip freeze > requirements.txt
py -m pip install -r requirements.txt
```

### Requirements 文件格式

需求文件每行列出一个需要安装的包，参数和 `pip install` 支持的参数类似，支持样式如下：

```bash
[[--option]...]
<requirement specifier> [; markers] [[--option]...]
<archive url/path>
[-e] <local project path>
[-e] <vcs project url>
```

## Requirement Specifiers

pip 支持使用**需求说明符**从 pypi 安装依赖项。

## ensurepip

ensurepip 包用于将 pip 程序安装到现有的 Python 版本或虚拟环境中。

在大多数情况，Python 终端用户不需要直接调用这个模块，因为默认会安装 pip。如果跳过了 pip 安装，或者不小心卸载了 pip（升级 pip 时，如果在卸载旧版 pip 后升级出错，也会导致该问题），就可以使用这个包安装 pip。

> ensurepip 运行不需要联网，安装 pip 所需的所有组件都内嵌在 ensurepip 包中。

### 命令行接口

使用Python 解释器的 `-m` 选项调用命令接口。最简单用法：

```shell
python -m ensurepip
```

如果没有安装 pip，该命令会安装 pip；如果已安装 pip，该命令不执行任何操作。

如果希望已安装的 `pip` 版本至少不低于 `ensurepip` 中内嵌的版本，可以使用 `--upgrade` 选项：

```shell
python -m ensurepip --upgrade
```

`pip` 默认被安装到当前虚拟环境（处于激活状态），如果无激活状态的虚拟环境，则安装到系统 Python 中。安装位置可以通过以下两个命令选项控制：

- `--root <dir>`：相对于给定的根目录安装 `pip`，而不是当前虚拟环境的根目录；
- `--user`：将 `pip` 安装到用户目录，而不是全局目录，该选项对虚拟环境无效。

另外，默认会安装 `pipX` 和 `pipX.Y` 两个脚本，其中 `X.Y` 表示当前 Python 版本。该行为可以通过如下两个命令选项控制：

- `--altinstall`：使用该选项表示不安装 `pipX` 脚本；
- `--default-pip`：使用该选项表示额外安装 `pip` 脚本。

## 参考

- [pip documentation](https://pip.pypa.io/en/stable/user_guide/)
- https://docs.python.org/3/library/ensurepip.html
