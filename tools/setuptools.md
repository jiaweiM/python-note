# setuptools

- [setuptools](#setuptools)
  - [简介](#简介)
  - [安装 setuptools](#安装-setuptools)
  - [使用](#使用)
  - [指定项目版本](#指定项目版本)
  - [版本编号方案](#版本编号方案)
    - [编号方案](#编号方案)
      - [语义版本（推荐）](#语义版本推荐)
      - [日期版本](#日期版本)
      - [序号版本（Serial）](#序号版本serial)
      - [混合方案](#混合方案)
    - [Pre-release 版本](#pre-release-版本)
    - [本地版本识别符](#本地版本识别符)
  - [setup() 参数](#setup-参数)
    - [name](#name)
    - [version](#version)
    - [description](#description)
    - [url](#url)
    - [author](#author)
    - [license](#license)
    - [classifiers](#classifiers)
    - [python_requires](#python_requires)
    - [packages](#packages)
  - [命令](#命令)
    - [卸载](#卸载)
  - [参考](#参考)

2020-04-17, 17:52
***

## 简介

setuptools 对 distutils 进行了增强，可以更轻松地构建和分发 Python 软件包，尤其是那些包含依赖项的软件包。

## 安装 setuptools

```py
pip install --upgrade setuptools
```

## 使用

对最简单的情况，使用 `setuptools` 导入所需内容即可，下面是最小的 `setup.py` 脚本：

```py
from setuptools import setup, find_packages

setup(
    name="HelloWorld",
    version="0.1",
    packages=find_packages(),
)
```

将该脚本和项目放在同一个目录，运行该脚本在同一目录生成软件包。例如，生成源码分发：

```py
setup.py sdist
```

也可以在其中添加更多信息，以帮助人们找到或了解你的项目。例如：

```py
from setuptools import setup, find_packages

setup(
    name="HelloWorld",
    version="0.1",
    packages=find_packages(),
    scripts=["say_hello.py"],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["docutils>=0.3"],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
        # And include any *.msg files found in the "hello" package, too:
        "hello": ["*.msg"],
    },

    # metadata to display on PyPI
    author="Me",
    author_email="me@example.com",
    description="This is an Example Package",
    keywords="hello world example examples",
    url="http://example.com/HelloWorld/",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://code.example.com/HelloWorld/",
    },
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ]

    # could also incl
```

下面我们会一一解释 `setup()` 的参数。

## 指定项目版本

项目版本由发行号（release number）和标签组成。

发行号由点分隔的数字组成，如 `2.4` 或 `0.5`。

在发行号后可以添加发行前或发行后标签：

- 发行前标签比发行号对应的版本要老，即 `2.4` 比 `2.4c1` 要新，而 `2.4c1` 又比 `2.4b1` 和 `2.4a1` 要新。
- 发行后标签比发行号对应的版本要新，即 `2.4-1` 要比 `2.4` 新。

发行前标签是一系列的字母，如 `alpha`, `beta`, `a`, `c`, `dev` 等，直到 `final`。在发行号和发行前标签之间可以添加 `.`, `-`，或什么都不加，即`2.4c1`, `2.3.c1` 和 `2.4-c1` 等价。

另外，`c` 表示 `pre`, `preview`, `rc`，这几种表示等价。所以 `2.4rc1`, `2.4pre1`, `2.4preview1` 和 `2.4c1` 等价。

发行后标签是 `final` 及其后的字母，或者断线 `-`。发行后标签一般用来分隔发行号和补丁号（patch numbers）、端口号（port numbers）、内部版本号（build numbers）、修订号（revision numbers）以及时间。例如 `2.4-r1263` 可能表示版本 `2.4` 后的修订版 `1263`。

## 版本编号方案

不同的 Python 项目根据需要可能采用不同的版本方案，但是都应该遵守 PEP 400 中的公共版本方案，以支持 pip 和 setuptools 等工具。

下面是一些兼容版本号：

```text
1.2.0.dev1  # Development release
1.2.0a1     # Alpha Release
1.2.0b1     # Beta Release
1.2.0rc1    # Release Candidate
1.2.0       # Final Release
1.2.0.post1 # Post Release
15.10       # Date based release
23          # Serial release
```

### 编号方案

#### 语义版本（推荐）

对新项目，推荐使用语义版本方案。

语义版本由三部分组成 `MAJOR.MINOR.MAINTENANCE`:

- MAJOR，主要版本，引入了不兼容 API
- MINOR，添加额外功能，向后兼容
- MAINTENANCE，添加了向后兼容的 bug fixes。

采用这种版本方案可以使用 "compatiable release" 说明符，`name ~= X.Y` 要求版本至少为 `X.Y`。

#### 日期版本

语义版本方案不适用于所有项目，例如那些定期发布的项目，或者在指定版本前持续提供警告的情况。

基于日期的版本方案一般采用 "YEAT.MONTH" 的格式，如 `12.04`。

#### 序号版本（Serial）

这是最简单的一种版本编号方案，仅包含一个数字，每次发行递增编号。

不过这类编号方案对用户不够友好，其中没有传递任何兼容性信息。

#### 混合方案

以上方案进行混合，如 `YEAR.SERIAL`。

### Pre-release 版本

不管基础版本方案是哪种，都可以添加 pre-releases 版本：

- 0 或多个 dev releases (".devN" 后缀)
- 0 或多个 alpha releases (".aN" 后缀)
- 0 或多个 beta releases (".bN" 后缀)
- 0 或多个 candidates (".rcN" 后缀)

`pip` 和其它现代的 Python 包安装器在查找依赖项版本时，默认忽略 pre-releases。

### 本地版本识别符

本地版本是不准备发行的版本，格式为 `<public version identifier>+<local version label>`。例如：

```text
1.2.0.dev1+hg.5.b11e5e6f0b0b  # 5th VCS commmit since 1.2.0.dev1 release
1.2.1+fedora.4                # Package with downstream Fedora patches applied
```

## setup() 参数

| 参数                 | 说明                                                     |
| -------------------- | -------------------------------------------------------- |
| maintainer           | 维护者                                                   |
| maintainer_email     | 维护者的邮箱地址                                         |
| project_urls         | 额外URL列表                                              |
| platforms            | 适用的平台列表，逗号分隔列表                             |
| keywords             | 关键字列表                                               |
| py_modules           | 需要打包的 Python 单文件列表                             |
| download_url         | 程序的下载地址                                           |
| cmdclass             | 添加自定义命令                                           |
| package_data         | 指定包内需要包含的数据文件                               |
| include_package_data | 自动包含包内所有受版本控制(cvs/svn/git)的数据文件        |
| exclude_package_data | 当 include_package_data 为 True 时该选项用于排除部分文件 |
| data_files           | 打包时需要打包的数据文件，如图片，配置文件等             |
| ext_modules          | 指定扩展模块                                             |
| scripts              | 指定可执行脚本,安装时脚本会被安装到系统 PATH 路径下      |
| package_dir          | 指定哪些目录下的文件被映射到哪个源码包                   |
| requires             | 指定依赖的其他包                                         |
| provides             | 指定可以为哪些模块提供依赖                               |
| install_requires     | 安装时需要安装的依赖包                                   |
| entry_points         | 动态发现服务和插件                                       |
| setup_requires       | 指定运行 setup.py 文件本身所依赖的包                     |
| dependency_links     | 指定依赖包的下载地址                                     |
| extras_require       | 当前包的高级/额外特性需要依赖的分发包                    |
| zip_safe             | 不压缩包，而是以目录的形式安装                           |

### name

`name='sample'`

项目名称。在 PyPI 中显示的名称。有效的名称：

- ASCII 字母、数字、下划线、断线 (`-`)和点号 (`.`)
- 以 ASCII 字母或数字开头和结尾

项目名称的比较不区分大小写，任意长度的 `_`, `-`, `.` 视为相同。例如，下面的项目名称等价：

```py
cool-stuff
Cool-Stuff
cool.stuff
COOL_STUFF
CoOl__-.-__sTuFF
```

### version

`version='1.2.0'`

项目当前版本。

如果项目本身需要访问版本号，最简单的方式是同时在 `setup.py` 和代码中维护版本号。

### description

```py
description='A sample Python project',
long_description=long_description,
long_description_content_type='f_text/x-rst',
```

`description` 是项目的一句话简短描述。

`long_description` 是详细描述。

如果将项目发布到 PyPI，这些信息会在对应的页面显示。

- `description` 在 PyPI 的灰色横条显示。
- `long_description` 在 "Project description" 部分显示。

还可以通过 `long_description_content_type` 参数指定内容类型，包括：

- `text/plain`，纯文本，无格式
- `text/x-rst`， reStructuredText
- `text/markdown`, Markdown

### url

`url='https://github.com/pypa/sampleproject',`

项目的主页。

### author

```py
author='The Python Packaging Authority',
author_email='pypa-dev@googlegroups.com',
```

项目作者的相关信息。

- `author`, 作者名
- `author_email`, 作者邮箱

### license

```py
license='MIT',
```

### classifiers

所属分类列表。

```py
classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish (should match "license" above)
     'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
],
```

完整的 [Classifiers 列表](https://pypi.org/classifiers/)。

### python_requires

python 版本要求，例如限于 Python 3+

```py
python_requires='>=3',
```

如果要求 Python 3.3 以上，但不能到 Python 4:

```py
python_requires='~=3.3',
```

如果限于 Python 2.6, 2.7以及 Python 3.3 之后的版本：

```py
python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
```

### packages

```py
packages=find_packages(include=['sample', 'sample.*']),
```

列出项目中的所有包。`setuptools.find_packages()` 会自动查看项目中的包。`include` 关键字参数指定查找的包，`exclude` 关键字参数用于忽略指定的包。

## 命令

### 卸载

使用 `setup.py install` 安装的包无法直接卸载，此时运行 `setup.py install --record files.txt` 记录所有安装的文件，查看 files.txt 文件，找到这些文件直接删除。

## 参考

- [setuptools' documentation](https://setuptools.readthedocs.io/en/latest/index.html)
- [Packaging and distributing projects](https://packaging.python.org/guides/distributing-packages-using-setuptools/#)
- [Distributing Python Modules](https://docs.python.org/3/distributing/index.html)
- [Python Packaging User Guide](https://packaging.python.org/tutorials/installing-packages/)