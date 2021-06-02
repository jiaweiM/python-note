import sys

from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        box = QComboBox()
        box.addItems(["One", "Two", "Three"])

        box.currentIndexChanged.connect(self.index_changed)
        box.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(box)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
