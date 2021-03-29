import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QTextEdit, QApplication


class Ex(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction("Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(self.close)

        self.statusBar()
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar("Exit")
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle("Main Window")


def main():
    app = QApplication(sys.argv)
    ex = Ex()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
