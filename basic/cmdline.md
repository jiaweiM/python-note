# Python 命令和环境

- [Python 命令和环境](#python-命令和环境)
  - [命令](#命令)
    - [接口选项](#接口选项)
      - [`-m <module-name>`](#-m-module-name)
  - [环境](#环境)
  - [参考](#参考)

2021-10-11, 09:55
***

## 命令

调用 Python 时，可以指定以下选项中的任意一个：

```shell
python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]
```

调用执行脚本是最常见的用法：

```shell
python myscript.py
```

### 接口选项

Python 解释器命令接口类似于 UNIX shell，并提供了一些额外调用方法：

- 




#### `-m <module-name>`

在 `sys.path` 搜索指定名称的模块，并以 `__main__` 模块的形式执行其内容。

参数 `<module-name>` 是模块名称，记住不要加后缀 `.py`。

## 环境

## 参考

- https://docs.python.org/3.9/using/cmdline.html
