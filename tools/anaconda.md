# conda

- [conda](#conda)
  - [命令](#命令)
  - [Environment 管理](#environment-管理)
    - [创建环境](#创建环境)
    - [激活环境](#激活环境)
  - [包管理](#包管理)
    - [检索包](#检索包)
    - [安装包](#安装包)

## 命令

https://conda.io/docs/using/pkgs.html

|命令|说明|
|---|---|
|conda list|列出已安装的包|
|conda search beautiful-soup|搜索指定包是否安装|
|conda update biopython|更新包|
|conda search python|To list the versions of Python that are available to install|

## Environment 管理

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

## 包管理

### 检索包

检索包 SciPy：

```bash
conda search scipy
```

### 安装包

安装包如 SciPy 到指定环境 "myenv":

```bash
conda install --name myenv scipy
```

如果不指定环境名称，即 `--name myenv` ，包会包装到当前环境：

```bash
conda install scipy

```

安装指定版本的包：

```bash
conda install scipy=0.15.0
```

同时安装多个包：

```bash
conda install scipy curl
```

> **WARNING**:  最好一次安装所有的包，以便同时安装所有依赖项。

安装多个指定版本的包：

```bash
conda install scipy=0.15.0 curl=7.26.0
```
