# pip

- [pip](#pip)
  - [简介](#%e7%ae%80%e4%bb%8b)
    - [更新 pip](#%e6%9b%b4%e6%96%b0-pip)
  - [包管理](#%e5%8c%85%e7%ae%a1%e7%90%86)
    - [安装包](#%e5%ae%89%e8%a3%85%e5%8c%85)
      - [从 Wheels 安装](#%e4%bb%8e-wheels-%e5%ae%89%e8%a3%85)
    - [查看已安装包](#%e6%9f%a5%e7%9c%8b%e5%b7%b2%e5%ae%89%e8%a3%85%e5%8c%85)
    - [更新包](#%e6%9b%b4%e6%96%b0%e5%8c%85)
    - [卸载包](#%e5%8d%b8%e8%bd%bd%e5%8c%85)
  - [pip 镜像](#pip-%e9%95%9c%e5%83%8f)
    - [临时使用镜像](#%e4%b8%b4%e6%97%b6%e4%bd%bf%e7%94%a8%e9%95%9c%e5%83%8f)
    - [设置默认镜像](#%e8%ae%be%e7%bd%ae%e9%bb%98%e8%ae%a4%e9%95%9c%e5%83%8f)
  - [创建虚拟环境](#%e5%88%9b%e5%bb%ba%e8%99%9a%e6%8b%9f%e7%8e%af%e5%a2%83)
  - [参考](#%e5%8f%82%e8%80%83)

## 简介

pip 是 Python 包管理工具。

Python 2>=2.7.9 和 Python 3 >= 3.4 自动安装了 pip，

### 更新 pip

- Linux 或 macOS

```cmd
pip install --upgrade pip
```

- Windows

```cmd
python -m pip install -U pip
```

## 包管理

### 安装包

pip 支持从 PyPI、版本控制、本地项目和分布文件安装包。
安装命令：

```cmd
pip install SomePackage # latest version
pip install SomePackage==1.0.4 # specific version
pip install 'SomePackage>=1.0.4' # minimum version
```

#### 从 Wheels 安装

"Wheel" 是一种内置的存档格式，与从源码构建、安装相比，使用 wheel 要快许多。

```cmd
pip install SomePackage-1.0-py2.py3-none-any.whl
```

### 查看已安装包

显示已安装的包：

```cmd
pip list
```

### 更新包

显示可更新的包：

```cmd
pip list --outdated
```

更新：`-U, --upgrade` 更新

```cmd
pip install --upgrade packagename
```

### 卸载包

```cmd
pip uninstall packagename
```

在更新时，pip会自动卸载旧版本，安装新版本。

## pip 镜像

国内的一些镜像：

- 豆瓣, [https://pypi.doubanio.com/simple/](https://pypi.doubanio.com/simple/)
- 阿里云, [https://mirrors.aliyun.com/pypi/simple/](https://mirrors.aliyun.com/pypi/simple/)
- 清华大学
  - [https://pypi.tuna.tsinghua.edu.cn/simple/](https://pypi.tuna.tsinghua.edu.cn/simple/)
  - [https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/](https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/)
- 中国科学技术大学, [http://pypi.mirrors.ustc.edu.cn/simple/](http://pypi.mirrors.ustc.edu.cn/simple/)
- 华中科学技术大学, [http://pypi.hustunique.com/](http://pypi.hustunique.com/)

### 临时使用镜像

```cmd
pip install some-package -i https://mirrors.aliyun.com/pypi/simple/
```

### 设置默认镜像

升级 pip 到最新版：

```cmd
pip install pip -U
```

配置默认镜像：

```cmd
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

## 创建虚拟环境

`venv` (Python 3) 和 `virtualenv` (Python 2) 用于创建虚拟环境，从而可以为不同项目安装不同的工具包。

在进行 Python 应用开发时，最好使用虚拟环境。

在项目目录，运行 `venv`，对 Python 2，替换为 `virtualenv`.

在 macOS 和 Linux:

```cmd
python3 -m venv env
```

在 Windows:

```cmd
py -m venv env
```

第二个参数是虚拟环境的位置。 venv 会在 `env` 目录创建一个虚拟的 Python 环境。

## 参考

- [Reference Guide](https://pip.pypa.io/en/stable/reference/)
