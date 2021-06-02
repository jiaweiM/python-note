import sys
from random import choice

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.n_times_clicked = 0
        self.setWindowTitle("My APp")
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print(f"Setting title: {new_window_title}")
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print(f"Window title changed: {window_title}")

        if window_title == 'Something went wrong':
            self.button.setDisabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
