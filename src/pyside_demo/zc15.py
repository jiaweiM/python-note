import sys

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication


class Ex(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle("Signal & slot")
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Ex()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
