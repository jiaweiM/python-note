# venv

- [venv](#venv)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [创建虚拟环境](#%e5%88%9b%e5%bb%ba%e8%99%9a%e6%8b%9f%e7%8e%af%e5%a2%83)

2020-04-13, 05:58
***

## 简介

`venv` 模块支持使用自定义的 `site` 目录创建轻量型的虚拟焊接。

每个虚拟环境有子集的 Python （和创建该环境的 Python 版本一致），并且在其 site 目录拥有独立的 Python 工具包。

`venv` (Python >=3.6) `pyvenv` (Python 3.3, 3.4)和 `virtualenv` (Python 2) 用于创建虚拟环境，从而可以为不同项目安装不同的工具包。

在进行 Python 应用开发时，最好使用虚拟环境。创建虚拟环境是为了安装和管理第三方包。

## 创建虚拟环境

在项目目录，运行 `venv`，对 Python 2，替换为 `virtualenv`.

`python3 -m venv /path/to/new/virtual/environment`

- 运行该命令创建目标目录，并将 `pyvenv.cfg` 文件放入其中，该文件包含的 `home` key 指向运行该命令的目录。
- 目标目录通常为 `.venv`。
- 创建 `bin` 子目录（Windows 中为 `Scripts`），该目录包含指向 Python 的副本或符号链接，具体取决于创建虚拟环境的参数。
- 创建 `lib/pythonX.Y/site-packages` 子目录（Windows 中为 `Lib\site-packages`），初始为空。

在 macOS 和 Linux:

```cmd
python3 -m venv env
```

在 Windows:

```cmd
python -m venv c:\path\to\myenv
```

第二个参数是虚拟环境的位置。 venv 会在 `env` 目录创建一个虚拟的 Python 环境。

尽管一个虚拟环境看上去是 Python 安装的一个复制，不过它实际上只包含少量几个文件和一些符号链接。因此，创建虚拟环境很容易，并且几乎不会消耗多少电脑资源。

默认情况下，虚拟环境是空的，不包含任何额外的第三方库。如果你想将一个已经安装的包作为虚拟环境的一部分，可以使用 `-system-site-packages` 选项来创建虚拟环境。

> 虽然 Windows 支持符号链接，但不推荐使用。
