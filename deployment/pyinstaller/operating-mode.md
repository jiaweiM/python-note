# PyInstaller 原理

## 简介

PyInstaller 读取 Python 脚本，分析代码所需的其它模块和库，然后复制这些文件，包括 Python 解释器，将这些脚本放到一个目录，或者放到一个可执行文件。

对绝大多数程序，可以通过下面的命令完成：

```bash
pyinstaller myscript.py
```

或者添加一些选项，例如打包成单个窗口程序：

```bash
pyinstaller --onefile --windowed myscript.py
```

## 分析：查找程序所需文件

PyInstaller 分析脚本中所有 `import` 语句，查找导入的模块，然后在这些模块中继续找到 `import` 语句，递归执行，找到所有可能使用的模块。

PyInstaller 支持 Python 常用的 "egg" 包分发格式。如果脚本中包含从 "egg" 导入的模块，PyInstaller 会将 egg 及其依赖项添加到所需文件集。

PyInstaller 还支持许多主要的 Python 包，包括 GUI 包 Qt (PyQt 或 PySide)，WxPython, TkInter, matplotlib 等。支持包的[完整列表](https://github.com/pyinstaller/pyinstaller/wiki/Supported-Packages)。

