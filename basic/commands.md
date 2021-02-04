# Commands

- [Commands](#commands)
  - [CMD](#cmd)
  - [Interface options](#interface-options)
    - [-m](#-m)
  - [Generic options](#generic-options)
  - [Miscellaneous options](#miscellaneous-options)
  - [References](#references)

2020-04-17, 13:16
***

## CMD

Python 命令：

```cmd
python  [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]
```

最常用的命令：

```cmd
python myscript.py
```

|命令|功能|
|---|---|
|`cd`|修改目录|
|`mkdir`|创建目录|
|`rmdir`|删除目录|
|`dir`|浏览目录|
|`ipconfig`|查看IP地址|
|`ping`|测试网络是否连通|

## Interface options

Python 解释器接口类似于 UNIX shell，并提供了一些额外方法。

### -m

`-m <module-name>`

在 `sys.path` 中搜索 `<module-name>`，将其内容以 `__main__` 模块运行。

`-m` 选项将当前运行命令的路径添加到 `sys.path`，而不加则将脚本所在目录添加到 `sys.path`。

`<module-name>` 是模块名称，不需要 `.py` 后缀。

也可以使用包名替代模块名。此时Python解释器将 `<pkg>.__main__` 作为 main 模块执行。

> `-m` 选项不能用于内置模块和C扩展模块，因为它们没有 Python 模块文件。不过可以用于预编译的模块，虽然原始的源文件不可用。

## Generic options

## Miscellaneous options

**-u**

强制取消对 stdout 和 stderr 流的缓冲。此选项对 stdin 流无效。

## References

- [https://docs.python.org/3/using/cmdline.html](https://docs.python.org/3/using/cmdline.html)
