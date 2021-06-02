# IDE

- [IDE](#ide)
  - [简介](#简介)
  - [文件类型](#文件类型)
    - [界面定义文件 .ui](#界面定义文件-ui)
    - [资源文件 qrc](#资源文件-qrc)
    - [Qt 建模语言文件 qml](#qt-建模语言文件-qml)
  - [载入 ui 文件](#载入-ui-文件)
  - [PyCharm](#pycharm)

## 简介

Qt for Python 可以在兼容 Python 的IDE 中使用，但不是所有都提供 Qt Creator 提供的功能。

将 `.ui` 文件转换为 Python 文件：

```bash
pyside6-uic -i form.ui -o ui_form.py
```

将 `.qrc` 文件转换为 Python 文件：

```
pyside6-rcc -i resources.qrc -o rc_resources.py
```

Qt Designer，用于编辑 `.ui` 文件：

```
pyside6-designer
```

## 文件类型

在使用 Qt for Python 时有多种文件类型，包括 `ui`, `qrc`, `qml`, `pyproject` 等。

### 界面定义文件 .ui

使用 Qt Designer 可以拖动定义界面，生产的界面文件是 XML 格式，以树形结构表示。例如，下面是一个 `.ui` 文件开头部分：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralWidget">
...
```

使用 `pyside6-uic` 可以将 `.ui` 文件转换为 Python 代码。

### 资源文件 qrc

应用所需的资源列表，也是 XML 格式：

```xml
<!DOCTYPE RCC><RCC version="1.0">
<qresource>
    <file>images/quit.png</file>
    <file>font/myfont.ttf</file>
</qresource>
</RCC>
```

*pyside6-rcc* 可以将 .qrc 文件转换为 Python 代码。

### Qt 建模语言文件 qml

图形化 QML 程序去 Qt Widgets 应用无关，

## 载入 ui 文件



`QUiLoader` 类可以载入 UI 文件创建用户界面。如果你有自定义组件，或者应用程序嵌入了 Qt Designer，还可以使用 QtDeisnger 模块提供的 `QFormBuiler` 类从 UI 文件创建用户界面。

使用 `QUiLoader` 类可以根据 UI 文件或指定插件路径中的信息创建控件。
## PyCharm

File > Settings > tools > PyCharm External Tools 配置。
