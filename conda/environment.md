# 环境管理

- [环境管理](#环境管理)
  - [简介](#简介)
  - [创建环境](#创建环境)
  - [使用 environment.yml 文件创建环境](#使用-environmentyml-文件创建环境)
  - [激活环境](#激活环境)
  - [参考](#参考)

2022-01-13, 09:13
***

## 简介

使用 conda 可以创建、导出、列出、删除以及更新环境。在不同环境之间切换称为激活环境，也可以共享环境文件。

## 创建环境

> 创建的环境默认放在 conda 目录下的 `envs` 目录。

**例1**，创建环境

```sh
conda create --name myenv
```

其中 `myenv` 为环境名称，可替换为自定义名称。

当 conda 询问是否继续，输入 `y`

```sh
proceed ([y]/n)?
```

**例2**，创建指定 Python 版本的环境

```sh
conda create -n myenv python=3.8
```

**例3**，创建包含指定依赖项的环境

```sh
conda create -n myenv scipy
```

或者分两步进行：

```sh
conda create -n myenv python
conda install -n myenv scipy
```

**例4**，创建包含指定版本依赖项的环境

```sh
conda create -n myenv scipy=0.15.0
```

或者：

```bash
conda create -n myenv python
conda install -n myenv scipy=0.15.0
```

**例5**，创建包含指定版本 Python 及多个依赖项的环境

```sh
conda create -n myenv python=3.6 scipy=0.15.0 astroid babel
```

> 最好一次安装所需的所有程序。一次安装一个程序可能会导致依赖冲突。

要在每次创建新环境时自动安装 pip 或其它程序，可以将默认程序添加到 `.condarc` 配置文件的 `create_default_packages` 部分。这样每次创建新环境时，都会默认安装这些包。如果创建某个环境时不想安装这些包，可以添加 `--no-default-packages` 标签：

```sh
conda create --no-default-packages -n myenv python
```

## 使用 environment.yml 文件创建环境

## 激活环境

```sh
conda activate myenv
```

## 参考

- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
