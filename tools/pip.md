# pip

- [pip](#pip)
  - [简介](#简介)
    - [更新 pip](#更新-pip)
  - [包管理](#包管理)
    - [安装包](#安装包)
      - [从 Wheels 安装](#从-wheels-安装)
    - [查看已安装包](#查看已安装包)
    - [更新包](#更新包)
    - [卸载包](#卸载包)
    - [options](#options)
      - [`--user`](#--user)
  - [pip 镜像](#pip-镜像)
    - [临时使用镜像](#临时使用镜像)
    - [设置默认镜像](#设置默认镜像)
  - [Requirements Files](#requirements-files)
    - [Requirements 文件格式](#requirements-文件格式)
  - [Requirement Specifiers](#requirement-specifiers)
  - [参考](#参考)

2020-04-13, 05:42
*** *

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

### options

#### `--user`

安装到 Python 用户安装目录。在 Windows 上通常为 `~/.local/` 或者 `%APPDATA%Python`。

通常包会被安装到系统的 site-packages 目录，路径类似 “/usr/local/lib/python3.3/site-packages”。 不过，这样做需要有管理员权限并且使用sudo命令。 就算你有这样的权限去执行命令，使用sudo去安装一个新的，可能没有被验证过的包有时候也不安全。

安装包到用户目录中通常是一个有效的方案，它允许你创建一个自定义安装。

比如你想要安装一个第三方包，但是没有权限将它安装到系统Python库中去；或者，你想要安装一个供自己使用的包，而不是系统上面所有用户。

Python有一个用户安装目录，通常类似 `~/.local/lib/python3.3/site-packages`。要强制在这个目录中安装包，可使用安装选项“-–user”。例如：

```console
python3 setup.py install --user
```

或者：

```console
pip install --user packagename
```

在 sys.path 中用户的 “site-packages” 目录位于系统的 “site-packages” 目录之前。 因此，你安装在里面的包就比系统已安装的包优先级高 （尽管并不总是这样，要取决于第三方包管理器，比如distribute或pip）。

另外，你还可以创建一个虚拟环境。

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

## Requirements Files

"Requirements files" 包含需要使用 `pip install` 安装的包：

```
py -m pip install -r requirements.txt
```


### Requirements 文件格式

需求文件每行列出一个需要安装的包，参数和 `pip install` 支持的参数类似，支持样式如下：

```
[[--option]...]
<requirement specifier> [; markers] [[--option]...]
<archive url/path>
[-e] <local project path>
[-e] <vcs project url>
```

## Requirement Specifiers

pip 支持使用**需求说明符**从 pypi 安装依赖项。



## 参考

- [Reference Guide](https://pip.pypa.io/en/stable/reference/)
