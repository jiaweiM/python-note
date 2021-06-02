import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox, QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")

        checkBox = QCheckBox("This is a checkbox")
        checkBox.setCheckable(Qt.Checked)
        checkBox.stateChanged.connect(self.show_state)

        self.setCentralWidget(checkBox)

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
