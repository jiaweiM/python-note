import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
