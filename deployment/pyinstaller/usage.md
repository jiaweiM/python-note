# 使用 PyInstaller

## 简介

`pyinstaller` 命令为：

```bash
pyinstaller [options] script [script …] | specfile
```

最简单的情况，就工作目录设置为程序 `myscript.py` 的位置，然后执行：

```bash
pyinstaller myscript.py
```

PyInstaller 分析 `myscript.py` 脚本，并：

- 将 `myscript.spec` 写入和脚本相同的目录
- 在脚本目录下创建 `build` 子目录
- 在 `build` 目录写入日志文件和工作文件
- 在脚本目录下创建 `dist` 子目录里
- 在 `dist` 目录写入 `myscript` 可执行目录

在 `dist` 目录可以找到

## 选项



## 加密 Python Bytecode

使用 `--key=key-string` 选项加密。

## 参考

- https://pyinstaller.org/en/stable/index.html
