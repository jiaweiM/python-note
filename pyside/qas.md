# Questions and Answers

## QDesktopWidget

PySide6 中移除了 `QDesktopWidget`，使用 `QScreen` 代替，可以通过 `QWidget.screen()`, `QGuiApplication.primaryScreen()` 或 `QGuiApplication.screens()` 获得实例。
