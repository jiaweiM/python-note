# 软件分发

- [软件分发](#软件分发)
  - [简介](#简介)
  - [cx_Freeze](#cx_freeze)
    - [准备](#准备)
    - [冻结程序](#冻结程序)
    - [创建实例](#创建实例)
    - [运行 cxfreeze](#运行-cxfreeze)
    - [使用 setuptools 脚本](#使用-setuptools-脚本)
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

setup(name = "MyApp",
      version = "0.1",
      description = "My GUI App",
      executables = [Executable("hello.py")])
```



## 参考

- [Qt for Python Deployment](https://doc.qt.io/qtforpython/deployment.html#deployment-guides)
