# Button

- [Button](#button)
  - [QAbstractButton](#qabstractbutton)
    - [快捷键](#快捷键)
    - [按钮状态](#按钮状态)
    - [按钮信号](#按钮信号)
    - [扩展 `QAbstractButton`](#扩展-qabstractbutton)
  - [方法](#方法)
    - [setCheckable](#setcheckable)
  - [简介](#简介)
  - [参考](#参考)

2021-05-28, 17:24
***

## QAbstractButton

![](images/2021-05-28-17-26-34.png)

`QAbstractButton` 是 button 控件的抽象基类，提供了按钮的共有功能。而其子类对用户具体操作，已经按钮的绘制进行个性化定制。

`QAbstractButton` 同时支持 pushButton 和 checkableButton。`QRadioButton` 和 `QCheckBox` 实现了 checkableButton，`QPushButton` 和 `QToolButton` 实现了 pushButton。

每个按钮都可以显示文本和图标。用 `setText()` 设置文本，用 `setIcon()` 设置图标。如果禁用了按钮，按钮外观会随之改变。

### 快捷键

如果按钮的文本带有 `&` 符号，则 `QAbstractButton` 会自动创建快捷键。例如：

```cpp
button = QPushButton(tr("Rock and Roll"), self)
```

此时使用 `Alt+C` 快捷键触发调用 `animateClick()`。

也可以通过 `setShortcut()` 方法设置快捷键。这对没有显示文本的按钮十分有用：

```cpp
button.setIcon(QIcon(":/images/print.png"))
button.setShortcut(tr("Alt+F7"))
```

Qt 提供的所有按钮 `QPushButton`, `QToolButton`, `QCheckBox` 和 `QRadioButton` 都可以同时显示文本和图标。

通过 `setDefault()` 和 `setAutoDefault()` 方法可以设置按钮为对话框中的默认按钮。

### 按钮状态

`QAbstractButton` 提供了查询按钮状态的大多数方法：

- `isDown()` 按钮是否按下；
- `isChecked()` 按钮是否 checked。只有 checkable 按钮才有该状态；
- `isEnabled()` 按钮是否被按下；
- `setAutoRepeat()` 设置，如果用户按住按钮不放，按钮是否自动重复，通过 `autoRepeatDeley` 和 `autoRepeatInterval` 定义如何自动重复。

`isDown()` 和 `isChecked()` 的区别在于：用户点击 toggle 按钮，按钮首先进入 *pressed* 状态，，释放时进入 *checked* 状态；当用户再次点击，按钮先进入 *pressed* 状态，释放时进入 *unchecked* 状态。

### 按钮信号

`QAbstractButton` 提供了四种信号：

1. 鼠标光标在按钮内部时按钮鼠标左键触发；
2. 松开鼠标左键；
3. 按下鼠标左键后松开，按快捷键、调用 `click()` 或 `animateClick()`；
4. toggle 按钮状态改变触发 `toggled()`

### 扩展 `QAbstractButton`

要扩展 `QAbstractButton`，至少要重新实现按钮的绘制、文本以及像素图，通常还建议重新实现 `sizeHint()`，有时还需要重新实现 `hitButton()`，以确定是在按钮内部按下鼠标。

## 方法

### setCheckable


## 简介

![](images/2021-05-28-17-24-41.png)

`QPushButton` 提供了命令按钮功能。

## 参考

- https://doc.qt.io/qtforpython/PySide6/QtWidgets/QAbstractButton.html
