# 软件分发

- [软件分发](#软件分发)
  - [简介](#简介)
  - [cx_Freeze](#cx_freeze)
    - [准备](#准备)
    - [冻结程序](#冻结程序)
    - [创建实例](#创建实例)
    - [运行 cxfreeze](#运行-cxfreeze)
    - [使用 setuptools 脚本](#使用-setuptools-脚本)
      - [distutils 命令](#distutils-命令)
      - [build](#build)
      - [build_exe](#build_exe)
      - [Executable](#executable)
    - [添加数据文件](#添加数据文件)
  - [参考](#参考)

2021-05-31, 18:22
@Jiawei Mao
***

## 简介

部署 Python 项目，需要打包程序所需的所有资源。但是大多数项目不止一个 Python 文件，因此分发应用程序本身也有难度。

分发选项有：

1. 包括程序内容的 ZIP 文件；
2. 构建 Python 包（wheel）；
3. 将程序构建为单个二进制文件或目录；
4. 提供本机安装程序（msi, dmg）。

如果使用第 3 种方式，可以使用下面任一工具：

- [fbs](https://build-system.fman.io/)
- [PyInstaller](https://www.pyinstaller.org/)
- [cx_Freeze](https://marcelotduarte.github.io/cx_Freeze/)
- [py2exe](http://www.py2exe.org/)
- [py2ap](https://py2app.readthedocs.io/en/latest/)
- [briefcase](https://briefcase.readthedocs.io/)

Qt for Python 是一个跨平台框架，下表总结了这些打包工具支持的平台：

|Name|License|Qt 6|Qt 5|Linux|macOS|Windows|
|---|---|---|---|---|---|---|
|fbs|GPL||yes|yes|yes|yes|
|PyInstaller|GPL|partial|yes|yes|yes|yes|
|cx_Freeze|MIT|yes|yes|yes|yes|yes|
|py2exe|MIT|partial|partial|no|no|yes|
|py2app|MIT|yes|yes|no|yes|no|
|briefcase|BSD3|no|yes|yes|yes|yes|

只有 *fbs*, *cx_Freeze*, *briefcase* 和 *PyInstaller* 满足跨平台要求。

由于这些是命令工具，因此需要使用特殊的脚本来处理图像、图标和原信息等资源。另外，这些工具不提供更新应用程序包的机制。

可以使用 [PyUpdater](https://www.pyupdater.org/) 创建更新包，这是一个围绕 PyInstaller 构建的工具。

fbs 为用户提供了一个友好的操作用户界面。

## cx_Freeze

cx_Freeze 可以将应用程序打包为可执行文件。支持 Linux, macOS, Windows, FreeBSD 等平台。

### 准备

使用 pip 安装 cx_Freeze:

```bash
pip install cx_freeze
```

如果使用的是虚拟环境，则记得在安装 cx_freeze 之前激活虚拟环境。

安装后，就能使用 *cxfreeze* 二进制文件部署程序。

### 冻结程序

使用 cx_Freeze 有三种选择：

1. 使用 cxfreeze 脚本；
2. 创建 setup.py 脚本构建项目；
3. 直接使用 module 类。

下面介绍前面两种选择。

### 创建实例

下面是一个简单的脚本 *hello.py*：

```py
import sys
import random
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget)
from PySide6.QtCore import Slot, Qt

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
            "Hola Mundo", "Привет мир"]

        self.button = QPushButton("Click me!")
        self.text = QLabel("Hello World")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        # Connecting the signal
        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
```

### 运行 cxfreeze

使用如下命令打包程序：

```bash
cxfreeze hello.py
```

该命令创建 *dist/* 目录，在其中包含可执行程序，其中的 lib/ 目录包含所有的共享库。

### 使用 setuptools 脚本

使用该方式，需要创建 *setup.py* 脚本：

```py
import sys
from cx_Freeze import setup, Executable

# 会自动检测依赖项，在这里可以微调
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "guifoo",
    version = "0.1",
    description = "My GUI application!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("guifoo.py", base=base)]
)
```

然后调用:

```shell
python setup.py build
```

该命令会创建 `build` 子目录，在其中包含打包的程序。

在 Windows 平台，还可以使用如下命令创建安装包：

```shell
python setup.py bdist_msi
```

#### distutils 命令

#### build

用来构建可执行文件。

#### build_exe

该命令用于构建可执行文件。

|选项|说明|
|---|---|
|include_files|复制到目标目录的文件列表，字符串列表或 2-tuple 列表，2-tuple 包含文件位置和目标位置；其中目标位置不能是绝对路径|

#### Executable

|参数|说明|
|---|---|
|script|包含待执行的脚本文件|
|target_name|可执行文件名称|

### 添加数据文件

除了代码，应用往往还需要额外的数据文件，如图标等。可以在 `build_exe` 的 `include_files` 选项中列出数据文件或目录，它们会自动复制到构建目录中。

setup.py 文件：

```py
# Let's start with some default (for me) imports...

from cx_Freeze import setup, Executable



# Process the includes, excludes and packages first

includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = []
path = []

# This is a place where the user custom code may go. You can do almost
# whatever you want, even modify the data_files, includes and friends
# here as long as they have the same variable name that the setup call
# below is expecting.

# No custom code added

# The setup for cx_Freeze is different from py2exe. Here I am going to
# use the Python class Executable from cx_Freeze


GUI2Exe_Target_1 = Executable(
    # what to build
    script = "simplewx.py",
    initScript = None,
    base = 'Win32GUI',
    targetDir = r"dist",
    targetName = "simplewx.exe",
    compress = True,
    copyDependentFiles = True,
    appendScriptToExe = False,
    appendScriptToLibrary = False,
    icon = None
    )


# That's serious now: we have all (or almost all) the options cx_Freeze
# supports. I put them all even if some of them are usually defaulted
# and not used. Some of them I didn't even know about.

setup(
    
    version = "0.1",
    description = "No Description",
    author = "No Author",
    name = "cx_Freeze Sample File",
    
    options = {"build_exe": {"includes": includes,
                             "excludes": excludes,
                             "packages": packages,
                             "path": path
                             }
               },
                           
    executables = [GUI2Exe_Target_1]
    )

# This is a place where any post-compile code may go.
# You can add as much code as you want, which can be used, for example,
# to clean up your folders or to do some particular post-compilation
# actions.

# No post-compilation code added


# And we are done. That's a setup script :-D
```

构建命令：

```shell
python setup.py build
```

## 参考

- [Qt for Python Deployment](https://doc.qt.io/qtforpython/deployment.html#deployment-guides)
- https://cx-freeze.readthedocs.io/en/latest/
