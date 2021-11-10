# conda

- [conda](#conda)
  - [简介](#简介)
  - [基本概念](#基本概念)
    - [conda 命令](#conda-命令)
    - [conda package](#conda-package)
      - [.conda 文件格式](#conda-文件格式)
  - [安装](#安装)
  - [镜像](#镜像)
    - [查看镜像](#查看镜像)
  - [环境](#环境)
    - [创建环境](#创建环境)
    - [激活环境](#激活环境)
    - [查看环境列表](#查看环境列表)
    - [回到默认环境](#回到默认环境)
    - [删除环境](#删除环境)
  - [Python 管理](#python-管理)
  - [包管理](#包管理)
    - [查看已安装包](#查看已安装包)
    - [检索包](#检索包)
    - [安装包](#安装包)
    - [更新包](#更新包)
    - [删除包](#删除包)
  - [命令](#命令)
    - [conda config](#conda-config)
    - [conda search](#conda-search)
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


## 安装

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

使用 conda 创建、导出、列出以及更新环境。

### 创建环境

创建的环境默认放在 conda 目录下的 `envs` 目录。

1. 创建环境

```bash
conda create --name myenv
```

其中 `myenv` 为环境名称，可替换为自定义名称。

2. 当 conda 询问是否继续，输入 `y`

```bash
proceed ([y]/n)?
```

3. 创建指定 Python 版本的环境

```bash
conda create -n myenv python=3.8
```

4. 创建包含指定依赖项的环境

```bash
conda create -n myenv scipy
```

或者：

```bash
conda create -n myenv python
conda install -n myenv scipy
```

5. 创建包含指定版本依赖项的环境

```bash
conda create -n myenv scipy=0.15.0
```

或者：

```bash
conda create -n myenv python
conda install -n myenv scipy=0.15.0
```

6. 创建包含指定版本 Python 及多个依赖项的环境

### 激活环境

```sh
conda activate myenv
```

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

## 包管理

### 查看已安装包

```bash
conda list
```

### 检索包

检索包 SciPy：

```bash
conda search scipy
```

### 安装包

- 安装包如 SciPy 到指定环境 "myenv":

```bash
conda install --name myenv scipy
```

- 如果不指定环境名称，即 `--name myenv` ，包会包装到当前环境：

```bash
conda install scipy
```

- 安装指定版本的包

```bash
conda install scipy=0.15.0
```

- 同时安装多个包

```bash
conda install scipy curl
```

> **WARNING**:  最好一次安装所有的包，以便同时安装所有依赖项。

安装多个指定版本的包：

```bash
conda install scipy=0.15.0 curl=7.26.0
```

### 更新包

```bash
# 更新conda，保持conda最新
conda update conda

# 更新anaconda
conda update anaconda

# 更新python
conda update python
# 假设当前环境是python 3.4, conda会将python升级为3.4.x系列的当前最新版本
```

### 删除包

```bash
conda remove numpy
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

## 参考

- https://docs.conda.io/projects/conda/en/latest/user-guide/index.html
- https://docs.conda.io/projects/conda/en/latest/commands.html
