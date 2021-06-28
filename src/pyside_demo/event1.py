import sys

import PySide6.QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Reimplementing Events")
        self.setGeometry(300, 250, 300, 100)

        self.myLayout = QVBoxLayout()

        self.myLabel = QLabel("Press 'Esc' to close this App")
        self.infoLabel = QLabel()

        self.myLabel.setAlignment(Qt.AlignCenter)
        self.infoLabel.setAlignment(Qt.AlignCenter)

        self.myLayout.addWidget(self.myLabel)
        self.myLayout.addWidget(self.infoLabel)

        self.setLayout(self.myLayout)
        self.show()

    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key_Escape:
            self.close()

    def mouseDoubleClickEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        self.close()

    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent) -> None:
        self.infoLabel.setText("Window Resized to QSize(%d, %d)" % (event.size().width(), event.size().height()))


if __name__ == '__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myWidget = MyWidget()
        myApp.exec()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
