# PySide 和 PyQt 的差别

- [PySide 和 PyQt 的差别](#pyside-和-pyqt-的差别)
  - [API 差异](#api-差异)
    - [不同导入名称](#不同导入名称)
    - [PySide 只支持 PyQt 2](#pyside-只支持-pyqt-2)
    - [信号槽有少许差异](#信号槽有少许差异)

## API 差异

### 不同导入名称

PySide 的库名称和 PyQt 不同，PyQt 的为：

```py
from PyQt4.QtCore import *
```

或者

```py
import PyQt4.QtCore
```

在 PySide 中为：

```py
from PySide.QtCore import * 
# or 
import PySide.QtCore
```

### PySide 只支持 PyQt 2

PyQt 提供了两套 API，第一套提供了 Python 版本的 `QString`, `QVariant` 等。新版 API 2 提供 Qt 类和 Python 数据类型之间的自动转换。PyQt 在 Python 2.x 默认为 API 1，在 Python 3 默认为 API 2。

PySide 只支持 API 2。部分 Qt 类，如 `QStrings`, `QStringLists`以及 `QVariants` PySide 没有，而用 Python 原生数据类型代替。

如果需要从 PyQt 迁移代码到 PySide，首先要将 PyQt 代码修改为 API 2，然后把导入修改为 PySide。

> QFileDialog.getOpenFileName 在 PySide 中返回 tuple 类型。

### 信号槽有少许差异

对信号槽命名，PyQt 使用特定于实现的命名方案：

```py
trigger = QtCore.pyqtSignal()
```

对该差异，可以额外添加如下定义：

```py
QtCore.Signal = QtCore.pyqtSignal 
QtCore.Slot = QtCore.pyqtSlot 
```

