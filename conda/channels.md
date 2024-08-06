# 镜像源

- [镜像源](#镜像源)
  - [简介](#简介)
  - [添加源](#添加源)
  - [国内源](#国内源)
  - [参考](#参考)

2022-06-07, 14:42
***

## 简介

conda 源（channels）是存储软件包的地方，是软件包托管和管理的基础。

|源|链接|说明|
|---|---|---|
|default|https://repo.anaconda.com/pkgs/|默认源，需要付费许可|
|conda-forge||免费|

如果仅使用默认源，则不会出现源冲突。

## 添加源

- 添加源 `new_channel`，`new_channel` 默认放在源列表开头，具有最高优先级

```sh
conda config --add channels new_channel
```

## 国内源

- 北京外国语大学镜像源

```sh
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/menpo/
```

配置文件：

```condarc
channels:
  - defaults
show_channel_urls: true
channel_alias: https://mirrors.bfsu.edu.cn/anaconda
default_channels:
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/main
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/free
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/r
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/pro
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.bfsu.edu.cn/anaconda/cloud
  msys2: https://mirrors.bfsu.edu.cn/anaconda/cloud
  bioconda: https://mirrors.bfsu.edu.cn/anaconda/cloud
  menpo: https://mirrors.bfsu.edu.cn/anaconda/cloud
  pytorch: https://mirrors.bfsu.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.bfsu.edu.cn/anaconda/cloud
```

- 上海交大镜像

```condarc
default_channels:
  - https://mirror.sjtu.edu.cn/anaconda/pkgs/r
  - https://mirror.sjtu.edu.cn/anaconda/pkgs/main
custom_channels:
  conda-forge: https://mirror.sjtu.edu.cn/anaconda/cloud/
  pytorch: https://mirror.sjtu.edu.cn/anaconda/cloud/
channels:
  - defaults
```

- 清华镜像

```
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  deepmodeling: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
```

## 参考

- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-channels.html
- https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html
