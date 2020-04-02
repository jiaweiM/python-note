# defaultdict

## 简介

`collections.defaultdict([default_factory[,...]])`

`defaultdict` 是内置 `dict` 的子类，覆盖了一个方法，添加了一个可写入实例变量，余下功能和 `dict` 完全一样。

第一个参数 `default_factory` 默认为 `None`，余下参数和 `dict`