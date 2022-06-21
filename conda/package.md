# 包管理

- [包管理](#包管理)
  - [查看已安装包](#查看已安装包)
  - [检索包](#检索包)
    - [可更新包](#可更新包)
  - [安装包](#安装包)
    - [安装相似包](#安装相似包)
    - [从 Anaconda.org 安装](#从-anacondaorg-安装)
    - [安装 non-conda 包](#安装-non-conda-包)
  - [更新包](#更新包)
  - [删除包](#删除包)
  - [参考](#参考)

2022-01-13, 14:28
@author Jiawei Mao
***

## 查看已安装包

```bash
conda list
```

## 检索包

```sh
usage: conda search [-h] [--envs] [-i] [--subdir SUBDIR] [-c CHANNEL]
                    [--use-local] [--override-channels]
                    [--repodata-fn REPODATA_FNS] [-C] [-k] [--offline]
                    [--json] [-v] [-q]
```

- 检索 SciPy 包

```sh
conda search scipy
```

- 查看特定的软件包，如 SciPy，是否可以从 Anaconda.org 安装

```sh
conda search --override-channels --channel defaults scipy
```

- 查看特定软件包，如 iminuit，是否在特定通道存在，如 http://conda.anaconda.org/mutirri

```sh
conda search --override-channels --channel http://conda.anaconda.org/mutirri iminuit
```

### 可更新包

```sh
conda search --outdated
```

## 安装包

- 安装包如 SciPy 到指定环境 "myenv"

```sh
conda install --name myenv scipy
```

- 如果不指定环境名称，即 `--name myenv`，则会安装到当前环境

```sh
conda install scipy
```

- 安装特定版本的包

```sh
conda install scipy=0.15.0
```

- 同时安装多个包

```sh
conda install scipy curl
```

> **WARNING**:  最好一次安装所有所需的包，以便同时安装所有依赖项。

- 安装多个特定版本的包

```sh
conda install scipy=0.15.0 curl=7.26.0
```

- 为特定版本的 Python 安装包

```sh
conda install scipy=0.15.0 curl=7.26.0 -n py34_env
```

这里 `py34_env` 其实是包含特定版本 Python 的环境。

### 安装相似包

安装具有相似文件名或者类似用途的软件包时，可能会有意想不到的结果。如果两个软件包的名字不同，或者构建包的其它版本，需要在堆栈中排查其它软件，建议使用 Mutex metapackages.

### 从 Anaconda.org 安装

使用 `conda install` 无法获得的软件包可以从 Anaconda.org 获得，Anaconda.org 是一个软件包管理服务。

按如下流程从 Anaconda.org 安装包：

1. 打开网页：https://anaconda.org/
2. 搜索所需包，如 `bottleneck`
3. 找到所需的包，查看详细页面

详细页面显示有通道名称，例如 "pandas" channel

4. 知道通道名称后，就可以使用 `conda install` 安装软件包

```sh
conda install -c pandas bottleneck
```

5. 检查是否安装成功

```sh
conda list
```

### 安装 non-conda 包



## 更新包

Last updated: 2022-06-16, 14:27

使用 `conda update` 命令检查更新。如果 conda 发现有更新可用，会提示是否安装更新。

- 更新指定包

```sh
conda update biopython
```

- 更新 Python

```sh
conda update python
```

- 更新 conda 自身

```sh
conda update conda
```

> conda 只能更新到该系列的最高版本，因此，Python 3.8 智能更新到 3.x 系列的最高版本。

- 更新 Anaconda 元包

```powershell
conda update conda
conda update anaconda
```

不管需要更新哪个包，conda 都会比较版本，然后报告可安装版本。如果没有更新可用，conda 提示 "All requested packages are already installed."。

如果找到了新版本，并且你希望更新，输入 `y` 进行更新：

```powershell
Proceed ([y]/n)? y
```

## 删除包

```bash
conda remove numpy
```

## 参考

- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html
- https://docs.conda.io/projects/conda/en/latest/commands/search.html
