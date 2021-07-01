import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QPushButton

global sec
sec = 0


def setTime():
    global sec
    sec += 1
    # LED 显示数字+1
    lcdNumber.display(sec)


def work():
    timer.start(1000)
    for i in range(2000000000):
        pass
    timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    top = QWidget()
    top.resize(300, 120)

    layout = QVBoxLayout(top)
    lcdNumber = QLCDNumber()
    layout.addWidget(lcdNumber)
    button = QPushButton("测试")
    layout.addWidget(button)

    timer = QTimer()
    # 每次计时结束，出发 setTime
    timer.timeout.connect(setTime)
    button.clicked.connect(work)

    top.show()
    sys.exit(app.exec())
