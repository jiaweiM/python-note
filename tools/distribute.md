# Distributing Python Moduels

- [Distributing Python Moduels](#distributing-python-moduels)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [安装工具](#%e5%ae%89%e8%a3%85%e5%b7%a5%e5%85%b7)

2020-04-18, 11:43
***

## 简介

基本概念说明：

- [Python Packaging Index](https://pypi.org/)是开源软件包的公共仓库，供所有 Python 用户使用。
- [Python Packaging Authority](https://www.pypa.io/en/latest/)是负责标准打包工具即相关元数据、文件格式标准的一组开发人员和文档维护人员。他们在 GitHub 和 Bitbucket 上维护各种工具、文档和问题跟踪。
- [distutils](https://docs.python.org/3/library/distutils.html#module-distutils)是1998年加到 Python 标准库的原来的构建和分发系统。虽然 distutils 很少直接使用，不过它依然是目前打包和分发系统的基础。
- setuptools 是 distutils 的替代品，2004 年首次发布。它最大的优点是新增了堆其它软件包的依赖关系声明，是目前推荐的打包和分发系统。
- [wheel](https://wheel.readthedocs.io/en/stable/) 将 `bdist_wheel` 命令添加到 `distutils/setuptools`。用于生成跨平台的wheel 文件（binary packaging format）。

## 安装工具

Python 标准库不包含现代 Python 打包标准的工具。使用 pip 安装当前推荐的构建和分发工具：

```py
python -m pip install setuptools wheel twine
```
