import sys

from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QWidget, QListWidget, QPushButton, QGridLayout, QApplication


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setWindowTitle("QThread Demo")
        self.thread = Worker()
        self.listFile = QListWidget()
        self.buttonStart = QPushButton("开始")
        layout = QGridLayout(self)
        layout.addWidget(self.listFile, 0, 0, 1, 2)
        layout.addWidget(self.buttonStart, 1, 1)

        self.buttonStart.clicked.connect(self.slotStart)
        self.thread.sinOut.connect(self.slodAdd)

    def slodAdd(self, file_inf):
        self.listFile.addItem(file_inf)

    def slotStart(self):
        self.buttonStart.setEnabled(False)
        self.thread.start()


class Worker(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self) -> None:
        while self.working:
            file_str = 'File index {}'.format(self.num)
            self.num += 1
            # 发出信号
            self.sinOut.emit(file_str)
            # 线程休眠
            self.sleep(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MainWidget()
    demo.show()
    sys.exit(app.exec())
