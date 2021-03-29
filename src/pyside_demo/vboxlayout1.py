import sys

from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication

window = QWidget()
button1 = QPushButton("One")
button2 = QPushButton("Two")
button3 = QPushButton("Three")
button4 = QPushButton("Four")
button5 = QPushButton("Five")

layout = QVBoxLayout(window)
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)
layout.addWidget(button5)

app = QApplication(sys.argv)
window.show()
sys.exit(app.exec_())
