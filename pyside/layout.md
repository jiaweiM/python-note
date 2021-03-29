# Layout

- [Layout](#layout)
  - [QBoxLayout](#qboxlayout)
  - [QVboxLayout](#qvboxlayout)
    - [构造函数](#构造函数)
    - [使用](#使用)

2021-03-25, 15:08
***

## QBoxLayout

![](images/2021-03-25-15-08-36.png)

`QBoxLayout` 水平或垂直排列子部件。

`QBoxLayout` 将其从父布局或 `parentWidget()` 获得的空间划分为小框，然后每个框放置一个部件。

如果 `QBoxLayout` 的方向为 `Horizontal`，则方框以合适大小排成一行，每个部件至少获得 minimum size 空间，最多 maximum size 空间。额外空间根据 stretch 设置分配。

![](images/2021-03-25-15-11-19.png)

如果 `QBoxLayout` 是 `Vertical`，则方框垂直放置。

![](images/2021-03-25-15-14-27.png)

使用 `QBoxLayout` 最简单的方式是使用其子类 `QHBoxLayout` 创建水平布局，`QVBoxLayout` 创建垂直布局。也可以直接使用 `QBoxLayout` 创建，指定其方向为 `LeftToRight` , `RightToLeft` , `TopToBottom` 或 `BottomToTop` 。

如果 `QBoxLayout` 不是顶层布局，则必须先将其添加到另一个布局中才能对其进行操作。使用 `addLayout()` 添加。

添加部件方法：

- `addWidget()` 添加部件到 `QBoxLayout` 并设置 stretch 系数。
- `addSpacing()` 添加空部件，用于控制部件之间的距离。
- `addStretch()` 创建空的可伸缩的 box。
- `addLayout()` 添加另一个 `QLayout`。

使用 `insertWidget()`, `insertSpacing()`, `insertStretch()`, `insertLayout()` 在指定位置插入。

`QBoxLayout` 还包含两个边距设置选项：

- `setContentsMargins()` 设置 `QBoxLayout` 四个边的边距。
- `setSpacing()` 设置相邻空间之间的距离，还可以通过 `addSpacing()` 添加额外距离。

默认边距由样式确定，对 Qt 样式默认为 9，对 windows 样式默认为 11.

## QVboxLayout

`QVboxLayout` 用于创建垂直方框布局。

![](images/2021-03-25-15-07-37.png)

### 构造函数

```py
PySide6.QtWidgets.QVBoxLayout(parent)
```

- `parent`

`parent` 为父容器，即将该 `QVBoxLayout` 设置为 `parent` 的布局。

### 使用

```py
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication

window = QWidget()
button1 = QPushButton("One")
button2 = QPushButton("Two")
button3 = QPushButton("Three")
button4 = QPushButton("Four")
button5 = QPushButton("Five")

layout = QVBoxLayout(window)
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)
layout.addWidget(button5)

window.show()
```

