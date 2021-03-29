import sys

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow


class Ex(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon("exit.svg"), 'Exit', self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(self.close)

        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Toolbar")
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Ex()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
