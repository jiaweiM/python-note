import sys

from PySide6.QtWidgets import QWidget, QApplication, QLabel


class Ex(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        l1 = QLabel("Hello", self)
        l2 = QLabel("Hell", self)
        l3 = QLabel("Heaven", self)

        l1.move(15, 10)
        l2.move(35, 40)
        l3.move(55, 70)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle("Absolute layout")


def main():
    app = QApplication(sys.argv)
    ex = Ex()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
