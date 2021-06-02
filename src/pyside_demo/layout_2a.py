import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        layout = QVBoxLayout()
        layout.addWidget(Color('red'))

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
