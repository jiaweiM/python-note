# PyYAML 教程

- [PyYAML 教程](#pyyaml-教程)
  - [安装](#安装)
  - [设置](#设置)
  - [加载 YAML](#加载-yaml)

***

## 安装

- pip

```powershell
pip install pyyaml
```

如果想用 LibYAML bindings (比纯 Python 版本快很多)，则还需要安装 [LibYAML](https://pyyaml.org/wiki/LibYAML)。然后可以执行如下命令来构建和安装绑定：

```powershell
$ python setup.py --with-libyaml install
```

要使用基于 LibYAML 的解析器和发射器，使用 `CParser` 和 `CEmitter`。例如：

```python
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# ...

data = load(stream, Loader=Loader)

# ...

output = dump(data, Dumper=Dumper)
```

## 设置

导入 `yaml` 包：

```python
>>> import yaml
```

## 加载 YAML

> **WARNING:** 如果数据来源不可信，调用 `yaml.load` 不安全。`yaml.load` 和 `pickle.load` 一样强大，因此也可能包含 Python 函数。

- `yaml.load` 将 YAML 对象转换为 Python 对象

```python
yaml.load("""
- Hesperiidae
- Papilionidae
- Apatelodidae
- Epiplemidae
 """, Loader=yaml.FullLoader)
```

```txt
['Hesperiidae', 'Papilionidae', 'Apatelodidae', 'Epiplemidae']
```

`yaml.load` 支持 byte string, Unicode string, 打开的 binary file 或 text file。byte 字符串或文件支持编码 *utf-8*, *utf-16-be* 或 *utf-16-le*。`yaml.load` 通过检查字符串或文件开头的 BOM 序列来确定编码，如果不存在 BOM，则默认为 utf-8.

- `yaml.load` 返回 Python 对象

