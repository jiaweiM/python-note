import sys

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel('<font color=red size=128><b>Hello PyQt,窗口在 10 秒后消失</b></font>')
    label.show()

    QTimer.singleShot(10000, app.quit)
    sys.exit(app.exec())
