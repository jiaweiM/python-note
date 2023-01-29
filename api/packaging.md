# packaging

## 简介

为实现互操作性规范程序提供工具。

## 版本

处理 package 的一个核心需求是处理版本。

使用：

```python
>>> from packaging.version import Version, parse
>>> v1 = parse("1.0a5")
>>> v2 = Version("1.0")
>>> v1
<Version('1.0a5')>
>>> v2
<Version('1.0')>
>>> v1 < v2
True
>>> v1.epoch
0
>>> v1.release
(1, 0)
>>> v1.pre
('a', 5)
>>> v1.is_prerelease
True
>>> v2.is_prerelease
False
>>> Version("french toast")
Traceback (most recent call last):
    ...
InvalidVersion: Invalid version: 'french toast'
>>> Version("1.0").post
>>> Version("1.0").is_postrelease
False
>>> Version("1.0.post0").post
0
>>> Version("1.0.post0").is_postrelease
True
```

- 例如，确定 TensorFlow 版本不低于 2.8.0

```python
from packaging import version
import tensorflow as tf

assert version.parse(tf.__version__) >= version.parse("2.8.0")
```

## 参考

- https://packaging.pypa.io/en/stable/