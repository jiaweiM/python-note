# QApplication

## 简介

`QApplication` 为 `QGuiApplication` 提供基于 `QWidget` 的程序所需的一些功能。包括 widget 的初始化和终止等。

所有基于 Qt 的GUI程序，必然有且只有一个 `QApplication` 对象，不管该程序有0，1，2或更多的窗口。对非 QWidget 的 Qt 程序，使用 `QGuiApplication` 代替，它不依赖于 QtWidgets 库。
