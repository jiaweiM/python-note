# QScreen

## 简介

`QScreen` 用于查询屏幕信息。

## 设置位置到中间

```py
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()
        self.setWindowTitle("Center")
        self.show()

    def center(self):
        qr = self.frameGeometry() # 主窗口位置
        cp = QGuiApplication.primaryScreen().availableGeometry().center() # 获得屏幕中心点位置
        qr.moveCenter(cp) # 
        self.move(qr.topLeft())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```