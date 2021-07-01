import random
import sys
import time

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QWidget


class WorkerSignals(QtCore.QObject):
    """
    定义信号类型，包括：

    - finished
        No data
    - error
        `str` Exception string
    - result
        `dict` data returned from processing
    """
    finished = QtCore.Signal()
    error = QtCore.Signal(str)
    result = QtCore.Signal(dict)


class Worker(QtCore.QRunnable):
    """
    工作线程
   :param args: Arguments to make available to the run code
   :param kwargs: Keywords arguments to make available to the run code
    """

    def __init__(self, iterations=5):
        super(Worker, self).__init__()
        self.signals = WorkerSignals()
        self.iterations = iterations

    @QtCore.Slot()
    def run(self):
        """
        Initialize the runner function with passed self.args, self.kwargs.
        """
        try:
            for n in range(self.iterations):
                time.sleep(0.01)
                v = 5 / (40 - n)
        except Exception as e:
            self.signals.error.emit(str(e))  # 发出异常信号
        else:
            self.signals.finished.emit()
            self.signals.result.emit({"n": n, "value": v})  # 没有异常，执行结束，给出值信息


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.threadpool = QtCore.QThreadPool()  # 初始化线程池
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.counter = 0

        layout = QtWidgets.QVBoxLayout()

        self.l = QtWidgets.QLabel("Start")

        b = QtWidgets.QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def oh_no(self):
        worker = Worker(iterations=random.randint(10, 50))
        worker.signals.result.connect(self.worker_output)
        worker.signals.finished.connect(self.worker_complete)
        worker.signals.error.connect(self.worker_error)
        self.threadpool.start(worker)

    def worker_output(self, s):
        print("RESULT", s)

    def worker_complete(self):
        print("THREAD COMPLETE!")

    def worker_error(self, t):
        print("ERROR: %s" % t)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
