import sys

from PyQt6.QtCore import QTimer, QDateTime
from PyQt6.QtWidgets import QWidget, QListWidget, QLabel, QPushButton, QGridLayout, QApplication


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle("QTimer demo")
        self.listFile = QListWidget()
        self.label = QLabel("显示当前时间")
        self.startButton = QPushButton("开始")
        self.endButton = QPushButton("结束")
        layout = QGridLayout(self)

        # 初始化定时器
        self.timer = QTimer(self)
        # 显示时间
        self.timer.timeout.connect(self.showTime)  # timeout 信号连接到特定的槽，当定时器超时，发出 timeout 信号

        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.startButton, 1, 0)
        layout.addWidget(self.endButton, 1, 1)

        self.startButton.clicked.connect(self.start_timer)
        self.endButton.clicked.connect(self.end_timer)

        self.setLayout(layout)

    def showTime(self):
        # 获取当前系统时间
        time = QDateTime.currentDateTime()
        # 设置时间格式
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label.setText(timeDisplay)

    def start_timer(self):
        # 设置时间间隔并启动定时器
        self.timer.start(1000)  # start 内设置时间间隔，启动或重新启动计时器，如果计时器在运行，则重启
        self.startButton.setEnabled(False)
        self.endButton.setEnabled(True)

    def end_timer(self):
        self.timer.stop()  # 停止计时器
        self.startButton.setEnabled(True)
        self.endButton.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec())
