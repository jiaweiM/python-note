import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

window = QWidget()
button1 = QPushButton("One")
button2 = QPushButton("Two")
button3 = QPushButton("Three")
button4 = QPushButton("Four")
button5 = QPushButton("Five")

layout = QGridLayout(window)
layout.addWidget(button1, 0, 0)  # 添加到 0 行 0 列
layout.addWidget(button2, 0, 1)  # 添加到 0 行 1 列
layout.addWidget(button3, 1, 0, 1, 2)  # 添加到 1 行 0 列，占据 1 行 2 列
layout.addWidget(button4, 2, 0)  # 添加到 2 行0列
layout.addWidget(button5, 2, 1)  # 添加到 2 行 1列

window.show()
app.exec()
