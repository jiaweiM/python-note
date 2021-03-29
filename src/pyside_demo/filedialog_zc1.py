import sys

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QTextEdit, QFileDialog, QApplication


class Ex(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.statusBar()

        openFile = QAction(QIcon('open.svg'), 'Open', self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("Open new File")
        openFile.triggered.connect(self.show_dialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')

    def show_dialog(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Open file", '/home')
        f = open(fname, 'r')
        with f:
            data = f.read()
            self.textEdit.setText(data)


def main():
    app = QApplication(sys.argv)
    ex = Ex()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
