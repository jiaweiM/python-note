import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        lineEdit = QLineEdit()
        lineEdit.setMaxLength(10)
        lineEdit.setPlaceholderText("Enter your text")

        lineEdit.returnPressed.connect()
    
