# 信号和槽

- [信号和槽](#信号和槽)
  - [概述](#概述)
  - [QPushButton 信号](#qpushbutton-信号)

2021-05-28, 17:11
***

## 概述

处理事件是 GUI 程序必需的功能，Qt 通过信号和槽（*signals and slots*）机制实现事件处理。

**信号**（signals）是控件发出的信息，如按下按钮会发出信号，文本框内容改变会发出信号。大多数信号是由用户操作产生。

**槽**（slots）用于接收信号。任何 Python 函数都可用作槽，即任何函数都可以接受信号，然后根据信号执行特定操作。

## QPushButton 信号

点击按钮，按钮 `QPushButton` 会产生信号。例如：

```py
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

说明：

- `clicked` 是按钮发出的一个信号
- 
