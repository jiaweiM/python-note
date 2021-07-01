import sys
import time

from PySide6 import QtCore, QtWidgets


class Worker(QtCore.QRunnable):
    """
    Worker thread
    """

    @QtCore.Slot
    def run(self):
        """
        your code goes in this function
        """
        print("Thread start")
        time.sleep(5)
        print("Thread complete")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.threadpool = QtCore.QThreadPool()
        print("Multireading with maximum %d threads" % self.threadpool.maxThreadCount())

    def oh_no(self):
        worker = Worker()
        self.threadpool.start(worker)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec()
