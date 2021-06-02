import sys
from PySide6 import QtGui, QtCore, QtWidgets

class Example(QtWidgets.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_UI()

    def init_UI(self):
        lcd = QtWidgets.QLCDNumber(self)
        