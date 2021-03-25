# 安装 Python 包

- [安装 Python 包](#安装-python-包)
  - [从源码安装](#从源码安装)
  - [从本地压缩包安装](#从本地压缩包安装)

2021-03-23, 13:33
***

## 从源码安装

直接从源码安装包：

```
python -m pip install <path>
```

如果已开发模式（development mode）安装，则安装包之后，依然可以编辑源码：

```
python -m pip install -e <path>
```

## 从本地压缩包安装

例如：

```
python -m pip install ./downloads/SomeProject-1.0.4.tar.gz
```
