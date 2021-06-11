# conda

- [conda](#conda)
  - [安装](#安装)
    - [Linux 安装](#linux-安装)
    - [Linux 卸载](#linux-卸载)
  - [命令](#命令)
  - [镜像](#镜像)
  - [环境管理](#环境管理)
    - [创建环境](#创建环境)
    - [激活环境](#激活环境)
    - [查看环境列表](#查看环境列表)
  - [包管理](#包管理)
    - [查看已安装包](#查看已安装包)
    - [检索包](#检索包)
    - [安装包](#安装包)
    - [更新包](#更新包)
    - [删除包](#删除包)
  - [参考](#参考)

2021-06-09, 12:23
***

## 安装

### Linux 安装

下载后，直接执行程序安装：

```bash
./Anaconda3-2021.05-Linux-x86_64.sh
```

配置路径:

```bash
# 将anaconda的bin目录加入PATH，根据版本不同，也可能是~/anaconda3/bin
echo 'export PATH="~/anaconda2/bin:$PATH"' >> ~/.bashrc
# 更新bashrc以立即生效
source ~/.bashrc
```

### Linux 卸载

由于Anaconda的安装文件都包含在一个目录中，所以直接将该目录删除即可。

```bash
rm -rf anaconda
```

清理 .bashrc 中的路径，文件末尾用#号注释掉之前添加的路径或者直接删除该行：

```bash
# export PATH=/home/lq/anaconda3/bin:$PATH
```

使其立即生效：

```bash
source ~/.bashrc
```

## 命令

https://conda.io/docs/using/pkgs.html

|命令|说明|
|---|---|
|conda list|列出已安装的包|
|conda search beautiful-soup|搜索指定包是否安装|
|conda update biopython|更新包|
|conda search python|To list the versions of Python that are available to install|

## 镜像

```bash
# 添加Anaconda的TUNA镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
# TUNA的help中镜像地址加有引号，需要去掉

# 设置搜索时显示通道地址
conda config --set show_channel_urls yes
```


## 环境管理

可以使用 conda 创建、导出、列出以及更新环境。

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
conda create -n myenv python=3.6
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

```bash
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

## 参考

- [Command Reference](https://docs.conda.io/projects/conda/en/latest/commands.html)
