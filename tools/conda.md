# conda

- [conda](#conda)
  - [简介](#简介)
  - [基本概念](#基本概念)
    - [conda 命令](#conda-命令)
    - [conda package](#conda-package)
      - [.conda 文件格式](#conda-文件格式)
  - [镜像](#镜像)
    - [查看镜像](#查看镜像)
  - [环境](#环境)
    - [查看环境列表](#查看环境列表)
    - [回到默认环境](#回到默认环境)
    - [删除环境](#删除环境)
  - [Python 管理](#python-管理)
  - [命令](#命令)
    - [conda config](#conda-config)
    - [conda create](#conda-create)
    - [conda info](#conda-info)
    - [conda search](#conda-search)
    - [conda update](#conda-update)
      - [目标环境](#目标环境)
      - [输出、提示和流控制选项](#输出提示和流控制选项)
  - [参考](#参考)

2021-11-03, 13:17

## 简介

conda 是一个通用包管理系统，旨在构架和管理任何语言和任何类型的软件。

Anaconda 则是一个打包的集合，里面预装了 conda、某个版本的 Python、多个 packages 等，就是把许多常用的库以及 conda 都给装好了。

Minoconda，顾名思义，它只包含最基本的内容，Python 与 conda，以及相关的依赖项，对空间要求严格的用户，选择 Miniconda 比较合适。

## 基本概念

### conda 命令

`conda` 命令是管理各种包的安装与卸载的主要接口。支持：

- 查询和搜索 Anaconda package index 和当前 Anaconda 安装；
- 创建新的 conda 环境；
- 安装和更新包。

> 许多常用的命令可以用缩写形式，前面的双断线 `--` 可以只用一个 `-`，选项名称可以只用首字母，如 `--name` 可以缩写为 `-s`，`--envs` 缩写为 `-e`，效果一样。

完整命令可以参考 [Command reference](https://docs.conda.io/projects/conda/en/latest/commands.html)。

### conda package

conda 包是包含如下内容的 tarball 压缩文件（.tar.bz2）或 .conda 文件：

- 系统级库；
- Python 或其它模块；
- 可执行程序；
- `info/` 目录下的元数据；

conda 会跟踪包和平台之间的依赖关系，conda 包格式在不同平台上格式相同。

conda 包只包含文件（包括符号链接），目录不包括在内。

#### .conda 文件格式

.conda 文件格式是在 conda 4.7 引入的用于替换 tarball 的格式，更紧凑，因此更快。

.conda 文件格式由一个外部的、未压缩的 zip 格式和两个内部压缩的 .tar 文件组成。

## 镜像

### 查看镜像

```sh
(base) C:\Users\happy>conda config --show channels
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
```

```bash
# 添加Anaconda的TUNA镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
# TUNA的help中镜像地址加有引号，需要去掉

# 设置搜索时显示通道地址
conda config --set show_channel_urls yes
```

## 环境

### 查看环境列表

查看已有环境列表：

```bash
conda info --envs
```

或者：

```bash
conda env list
```

### 回到默认环境

```sh
conda activate
```

### 删除环境

```sh
conda remove -n environment --all
```

- `-n, --name` 后跟环境名称；
- `--all` 表示移除所有 packages，即删除环境。

## Python 管理

在创建环境时，conda 默认使用安装 conda 时对应的 python。如果要使用其它版本，只需要指定版本：

```sh
conda create --name snakes python=3.9
```

然后激活该环境：

```sh
conda activate snakes
```

查看、验证该环境已安装：

```sh
conda info --envs
```

## 命令

### conda config

该命令用于修改配置文件 .condarc。默认写入用户 .condarc 文件（/home/docs/.condarc）。

选项：

```sh
usage: conda config [-h] [--json] [-v] [-q] [--system | --env | --file FILE]
                    [--show [SHOW [SHOW ...]] | --show-sources | --validate |
                    --describe [DESCRIBE [DESCRIBE ...]] | --write-default]
                    [--get [KEY [KEY ...]] | --append KEY VALUE | --prepend
                    KEY VALUE | --set KEY VALUE | --remove KEY VALUE |
                    --remove-key KEY | --stdin]
```

**例1**，显示所有配置信息

```sh
conda config --show
```

**例2**，添加 `conda-canary` channel:

```sh
conda config --add channels conda-canary
```

### conda create

创建新的 conda 环境。

```sh
usage: conda create [-h] [--clone ENV] [-n ENVIRONMENT | -p PATH] [-c CHANNEL]
                    [--use-local] [--override-channels]
                    [--repodata-fn REPODATA_FNS] [--strict-channel-priority]
                    [--no-channel-priority] [--no-deps | --only-deps]
                    [--no-pin] [--copy] [-C] [-k] [--offline] [-d] [--json]
                    [-q] [-v] [-y] [--download-only] [--show-channel-urls]
                    [--file FILE] [--no-default-packages] [--dev]
                    [package_spec [package_spec ...]]
```

- `package_spec`

位置参数，指定要在 conda 环境中安装或更新的包。

- `-n, --name`

新创建的环境名称。

**例 1**，创建环境 `myenv`，其中包含 sqlite 包

```sh
conda create -n myenv sqlite
```

### conda info

显示当前 conda 的信息。

```sh
usage: conda info [-h] [--json] [-v] [-q] [-a] [--base] [-e] [-s]
                  [--unsafe-channels]
```

### conda search

搜索包，并显示相关信息。

```sh
usage: conda search [-h] [--envs] [-i] [--subdir SUBDIR] [-c CHANNEL]
                    [--use-local] [--override-channels]
                    [--repodata-fn REPODATA_FNS] [-C] [-k] [--offline]
                    [--json] [-v] [-q]
```

**例1**，搜索 'scikit-learn':

```sh

```

### conda update

更新 conda 包到最新的兼容版本。

该命令后可以跟着包命令列表，并将它们全部更新为与环境中其它包兼容的最新版本。

conda 视图安装所请求包的最新版本，为了实现这一点，它可能会更新一些已经安装的包，或者安装额外的包。要阻止现有包的更新，使用 `--no-update-deps` 选项，这可能强制 conda 安装所请求包的旧版本，并且不会组织安装额外的依赖包。

```sh
usage: conda update [-h] [-n ENVIRONMENT | -p PATH] [-c CHANNEL] [--use-local]
                    [--override-channels] [--repodata-fn REPODATA_FNS]
                    [--strict-channel-priority] [--no-channel-priority]
                    [--no-deps | --only-deps] [--no-pin] [--copy] [-C] [-k]
                    [--offline] [-d] [--json] [-q] [-v] [-y] [--download-only]
                    [--show-channel-urls] [--file FILE] [--force-reinstall]
                    [--freeze-installed | --update-deps | -S | --update-all | --update-specs]
                    [--clobber]
                    [package_spec [package_spec ...]]
```

- `package_spec`

位置参数，需要在 conda 环境中安装或更新的包。

**例1**，将 conda 更新到最新版本

```sh
conda update -n base conda
```

**例2**，更新所有包

将所有包更新到最新版本（只安装稳定、兼容的版本）。

```sh
conda update anaconda
```

#### 目标环境

- `-n, --name`

环境名称。

- `-p, --prefix`

环境的完整路径。

#### 输出、提示和流控制选项

`-y, --yes`

不要弹出确认选项，直接安装。

## 参考

- https://docs.conda.io/projects/conda/en/latest/user-guide/index.html
- https://docs.conda.io/projects/conda/en/latest/commands.html
