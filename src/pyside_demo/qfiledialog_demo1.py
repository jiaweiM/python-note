import sys

from PyQt6.QtCore import QDir
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit, QApplication


class FileDialogDemo(QWidget):
    def __init__(self, parent=None):
        super(FileDialogDemo, self).__init__(parent)
        layout = QVBoxLayout()

        self.button = QPushButton("加载图片")
        self.button.clicked.connect(self.get_file)
        layout.addWidget(self.button)

        self.le = QLabel("")
        layout.addWidget(self.le)

        self.button1 = QPushButton("加载文本文件")
        self.button1.clicked.connect(self.get_files)
        layout.addWidget(self.button1)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)
        self.setWindowTitle("File Dialog 实例")

    def get_file(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Open file", 'C:\\', 'Image files (*.jpg &.gif)')
        self.le.setPixmap(QPixmap(fname))

    def get_files(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        dialog.setFilter(QDir.Filter.Files)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            f = open(filenames[0], 'r')
            with f:
                data = f.read()
                self.contents.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileDialogDemo()
    ex.show()
    sys.exit(app.exec())
