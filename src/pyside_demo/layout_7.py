import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        layout = QStackedLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        layout.setCurrentIndex(3)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
