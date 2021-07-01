import sys
import time

from PySide6.QtCore import QObject, QRunnable, QThreadPool, QTimer, Signal, Slot
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QProgressBar, QPushButton, QVBoxLayout, QWidget


class WorkerSignal(QObject):
    """
    进度信号
    """
    progress = Signal(int)


class Worker(QRunnable):
    """
    工作线程
    """

    def __init__(self):
        super(Worker, self).__init__()
        self.signals = WorkerSignal()

    def run(self):
        total_n = 1000
        for n in range(total_n):
            progress_pc = int(100 * float(n + 1) / total_n)
            self.signals.progress.emit(progress_pc)
            time.sleep(0.01)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()

        layout = QVBoxLayout()
        self.progress = QProgressBar()
        button = QPushButton("START IT UP")
        button.pressed.connect(self.execute)

        layout.addWidget(self.progress)
        layout.addWidget(button)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def execute(self):
        worker = Worker()
        worker.signals.progress.connect(self.update_progress)
        # Execute
        self.threadpool.start(worker)

    def update_progress(self, progress):
        self.progress.setValue(progress)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
