import sys

from PySide6.QtWidgets import QApplication, QFontDialog, QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel


class Ex(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)
        vbox.addWidget(btn)

        btn.clicked.connect(self.show_dialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle("Font dialog")

    def show_dialog(self):
        ok, font = QFontDialog.getFont(self)
        if ok:
            self.lbl.setFont(font)


def main():
    app = QApplication(sys.argv)
    ex = Ex()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
