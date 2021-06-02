import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QLineEdit, QFormLayout

app = QApplication(sys.argv)

window = QWidget()
button1 = QPushButton("One")
lineEdit1 = QLineEdit()
button2 = QPushButton("Two")
lineEdit2 = QLineEdit()
button3 = QPushButton("Three")
lineEdit3 = QLineEdit()

layout = QFormLayout(window)
layout.addRow(button1, lineEdit1)
layout.addRow(button2, lineEdit2)
layout.addRow(button3, lineEdit3)

window.show()
app.exec()
