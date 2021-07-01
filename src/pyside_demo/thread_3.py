import sys

from PyQt6.QtCore import QThread, pyqtSignal, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QPushButton

global sec
sec = 0


class WorkThread(QThread):
    trigger = pyqtSignal()

    def __init__(self):
        super(WorkThread, self).__init__()

    def run(self) -> None:
        for i in range(2000000000):
            pass
        self.trigger.emit()


def countTime():
    global sec
    sec += 1
    # LED 显示数字 +1
    lcdNumber.display(sec)


def work():
    timer.start(1000)
    workThread.start()
    workThread.trigger.connect(timeStop)


def timeStop():
    timer.stop()
    print("运行结束时", lcdNumber.value())
    global sec
    sec = 0


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
    workThread = WorkThread()
    button.clicked.connect(work)
    timer.timeout.connect(countTime)

    top.show()
    sys.exit(app.exec())
