# Flask 安装

- [Flask 安装](#flask-安装)
  - [Python 版本](#python-版本)
  - [Dependencies](#dependencies)
    - [Optional dependencies](#optional-dependencies)
    - [greenlet](#greenlet)
  - [虚拟环境](#虚拟环境)
    - [创建环境](#创建环境)
    - [激活环境](#激活环境)
  - [安装 Flask](#安装-flask)
  - [参考](#参考)

Last updated: 2022-09-09, 21:55
@author Jiawei Mao
****

## Python 版本

建议使用最新版本的 Python。Flask 支持 Python 3.7+。

## Dependencies

以下软件包会在安装 Falsk 时自动安装：

- [Werkzeug](https://palletsprojects.com/p/werkzeug/) 实现了应用程序与服务器之间的标准 Python 接口 WSGI。
- [Jinja](https://palletsprojects.com/p/jinja/) 是一种模板语言，用来渲染网页。
- [MarkupSafe](https://palletsprojects.com/p/markupsafe/) 是 Jinja 附带的。在渲染模板时会避开不可信输入，以避免注入攻击。
- [ItsDangerous](https://palletsprojects.com/p/itsdangerous/) 对数据进行安全签名以确保其完整性。用于保护 Flask 的 session cookie。
- [Click](https://palletsprojects.com/p/click/) 是一个用户编写命令行应用的框架，它提供了 `flask` 命令，并可以添加自定义管理命令。

### Optional dependencies

以下软件包不会自动安装。如果安装了，Flask 会检测并使用。

- [Blinker](https://pythonhosted.org/blinker/) 提供对 [Signals](https://flask.palletsprojects.com/en/2.2.x/signals/) 的支持。
- [python-dotenv](https://github.com/theskumar/python-dotenv#readme) 为 `flask` 命令提供 dotenv 环境变量支持。
- [Watchdog](https://pythonhosted.org/watchdog/) 为开发服务器提供了更快、更有效的重载功能。

### greenlet

可以选择在程序中使用 gevent 或 eventlet。不过要求 greenlet>=1.0。当使用 PyPy，要求 PyPy>=7.3.7。

## 虚拟环境

在开发或者生产中使用虚拟环境管理项目的依赖性。

Python 项目越多，就越可能需要使用不同版本的 Python 库，甚至 Python 本身。一个项目的新版本可能打破另一个项目的兼容性。

虚拟环境就是一组 Python 库，一个项目一个虚拟环境，互相独立。为一个项目安装的软件包不影响其它项目。

Python 自带的 venv 模块用于创建虚拟环境。

### 创建环境

创建项目目录及 `venv` 子目录，在该目录下创建环境：

```powershell
> mkdir myproject
> cd myproject
> py -3 -m venv venv
```

### 激活环境

在处理项目前，激活相应的环境：

```powershell
> venv\Scripts\activate
```

## 安装 Flask

在激活的环境中，使用如下命令安装 Flask：

```powershell
pip install Flask
```

## 参考

- https://flask.palletsprojects.com/en/2.2.x/installation/
