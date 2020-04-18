# wheel

- [wheel](#wheel)
  - [Quickstart](#quickstart)
  - [构建 wheel](#%e6%9e%84%e5%bb%ba-wheel)
  - [在 wheel 文件中包含 license 文件](#%e5%9c%a8-wheel-%e6%96%87%e4%bb%b6%e4%b8%ad%e5%8c%85%e5%90%ab-license-%e6%96%87%e4%bb%b6)
  - [将 Eggs 转换为 Wheels](#%e5%b0%86-eggs-%e8%bd%ac%e6%8d%a2%e4%b8%ba-wheels)

2020-04-18, 11:04
***

## Quickstart

位基于 setuptools 的项目构建 wheel:

```py
python setup.py bdist_wheel
```

生成的wheel 文件位于 `dist/yourproject-<tags>.whl`。

如果想生成通用（兼容 Python 2/3）的 wheel，需要将以下部分添加到 `setup.cfg`:

```py
[bdist_wheel]
universal = 1
```

将 `.egg` 转换为 wheel:

```py
wheel convert youreggfile.egg
```

类似的，将 Windows installer (使用 `python setup.py bdist_wininst` 生成)转换为 wheel:

```py
wheel convert yourinstaller.exe
```

## 构建 wheel

通过基于 setuptools 的项目构建 wheel 很简单：

```py
python setup.py bdist_wheel
```

该命令会构建项目中的 C 扩展，并将其和纯 Python 代码打包为 `.whl` 文件，放在 `dist` 目录。

如果你的项目不包含C扩展，并且希望能兼容 Python 2 和 3，可以在 `setup.cfg` 文件中添加：

```py
[bdist_wheel]
universal = 1
```

## 在 wheel 文件中包含 license 文件

多个开源 licenses 都要求将 license 文本包含在项目的分发中。wheel 默认将包含如下 `glob` 模式的文件放在 `.dist-info` 目录：

- `AUTHORS*`
- `COPYING*`
- `LICEN[CS]E*`
- `NOTICE*`

可以在 `setup.cfg` 的 `[metadata]` 部分的 `license_files` 选项覆盖该设置：

```py
[metadata]
license_files =
   license.txt
   3rdparty/*.txt
```

不管文件路径，只要匹配的 license 文件都写入 wheel 的 `.dist-info` 目录。

通过指定空的 `license_files` 选项，可以完全禁用该功能。

## 将 Eggs 转换为 Wheels

wheel 可以将 eggs 转换为 wheel 格式。对 `.egg` 文件和 `.egg` 目录都可用，还可以一次命令转换多个 egg 文件：

```py
wheel convert blah-1.2.3-py2.7.egg foo-2.0b1-py3.5.egg
```

该命令支持通配符：

```py
wheel convert *.egg
```

生成的 wheels 默认写入当前工作目录。可以通过 `--dest-dir` 选项修改：

```py
wheel convert --dest-dir /tmp blah-1.2.3-py2.7.egg
```
