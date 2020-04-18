# Packaging Python Projects

- [Packaging Python Projects](#packaging-python-projects)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [一个简单项目](#%e4%b8%80%e4%b8%aa%e7%ae%80%e5%8d%95%e9%a1%b9%e7%9b%ae)
    - [创建项目文件](#%e5%88%9b%e5%bb%ba%e9%a1%b9%e7%9b%ae%e6%96%87%e4%bb%b6)
    - [创建测试文件夹](#%e5%88%9b%e5%bb%ba%e6%b5%8b%e8%af%95%e6%96%87%e4%bb%b6%e5%a4%b9)
    - [创建 setup.py](#%e5%88%9b%e5%bb%ba-setuppy)
    - [创建 README.md](#%e5%88%9b%e5%bb%ba-readmemd)
    - [创建 LICENSE](#%e5%88%9b%e5%bb%ba-license)
    - [生成分发文件](#%e7%94%9f%e6%88%90%e5%88%86%e5%8f%91%e6%96%87%e4%bb%b6)
    - [上传分发文件](#%e4%b8%8a%e4%bc%a0%e5%88%86%e5%8f%91%e6%96%87%e4%bb%b6)
    - [安装新创建的包](#%e5%ae%89%e8%a3%85%e6%96%b0%e5%88%9b%e5%bb%ba%e7%9a%84%e5%8c%85)

2020-04-18, 11:55
***

## 简介

该教材引导你如何打包一个简单的 Python 项目。演示如何创建软件包，如何添加必要的文件，如何构建软件包，以及如何上传到 pypi。

## 一个简单项目

下面创建 `example_pkg` 项目，首先创建如下文件夹结构：

```text
packaging_tutorial/
  example_pkg/
    __init__.py
```

以下所有命令都是在 `packaging_tutorial` 目录执行。

### 创建项目文件

完整的项目结构如下：

```text
packaging_tutorial/
  example_pkg/
    __init__.py
  tests/
  setup.py
  LICENSE
  README.md
```

### 创建测试文件夹

`tests/` 文件单元测试文件夹，可以保持为空。

### 创建 setup.py

`setup.py` 时 setuptools 的构建脚本。

打开 setup.py 文件，在其中输入如下内容，并修改项目名称：

```py
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```

### 创建 README.md

打开 `README.md` 文件，输入如下内容：

```md
# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
```

### 创建 LICENSE

选择[合适的 license](https://choosealicense.com/)，打开 `LICENSE` 文件，输入对应的 LICENSE 文本。例如，输入 MIT license:

```text
Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### 生成分发文件

下一步生成分布包，该分发包可以上传到 pypi，也可以使用 pip 安装。

保证已安装最新的 `setuptools` 和 `wheel`：

```py
python3 -m pip install --user --upgrade setuptools wheel
```

然后在 `setup.py` 文件所在目录运行如下命令：

```py
python3 setup.py sdist bdist_wheel
```

这样就在 `dist` 目录生成两个文件：

```text
dist/
  example_pkg_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
  example_pkg_YOUR_USERNAME_HERE-0.0.1.tar.gz
```

其中 `tar.gz` 文件包含源码，`.whl` 文件是内置的分发文件。

### 上传分发文件

首先，你需要在 [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/) 注册一个 Test PyPI 账户，并验证邮箱。Test PyPI 是单独的 PypI，主要用于测试和试验。

然后在 Test PyPI 创建 API token，在[https://test.pypi.org/manage/account/#api-tokens](https://test.pypi.org/manage/account/#api-tokens)添加一个新的 API token。

pypi-AgENdGVzdC5weXBpLm9yZwIkZWQ4OTZjN2ItZWRhYS00ZDYxLTg2Y2QtMzM3NGZlYTUyNjgwAAIleyJwZXJtaXNzaW9ucyI6ICJ1c2VyIiwgInZlcnNpb24iOiAxfQAABiDH4Dstqgafnt2PRS4oQ89Cwpv4RypcvEoh5XIcbhNmBQ

然后用 `twine` 上传分发包。在 `dist` 目录运行：

```cmd
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

### 安装新创建的包

可以直接安装你上传的包：

```py
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-USERNAME-HERE
```
