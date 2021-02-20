# 分发 Python 模块

- [分发 Python 模块](#分发-python-模块)
  - [简介](#简介)
  - [安装工具](#安装工具)

2020-04-18, 11:43
***

## 简介

Python 包索引（[Python Packaging Index](https://pypi.org/)）是一个开源软件包的公共仓库，供所有 Python 用户使用。

[Python Packaging Authority](https://www.pypa.io/en/latest/) 是一群负责维护和开发标准打包工具和相关元数据、文件格式标准的开发人员和文档维护人员。他们在 GitHub 和 Bitbucket 上维护各种工具、文档和问题跟踪。

[distutils](https://docs.python.org/3/library/distutils.html#module-distutils) 是1998年添加到 Python 标准库用来构建和分发的工具。虽然 distutils 很少直接使用，不过它依然是目前打包和分发系统的基础。

[setuptools](https://setuptools.readthedocs.io/en/latest/) 是 distutils 的替代品，2004 年首次发布。它最大的优点是新增了对其它软件包的依赖关系声明，是目前推荐的打包和分发系统。

[wheel](https://wheel.readthedocs.io/en/stable/) 将 `bdist_wheel` 命令添加到 `distutils/setuptools`。用于生成跨平台的二进制格式 wheel 文件（binary packaging format）。

## 安装工具

Python 标准库不包含现代 Python 打包标准的构建工具。使用 pip 安装当前推荐的构建和分发工具：

```py
python -m pip install setuptools wheel twine
```
