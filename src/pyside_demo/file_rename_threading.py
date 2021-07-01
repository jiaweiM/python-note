import os
import sys
import time

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import (QWidget, QLabel, QProgressBar,
                               QLineEdit, QPushButton, QTextEdit, QComboBox, QFileDialog, QGridLayout, QApplication)

style_sheet = """
    QProgressBar{
        background-color: #C0C6CA;
        color: #FFFFFF;
        border: 1px solid grey;
        padding: 3px;
        height: 15px;
        text-align: center;
    }
    QProgressBar::chunk{
        background: #538DB8;
        width: 5px;
        margin: 0.5px
    }
"""


# 创建工作线程
class Worker(QThread):
    # 发出进度信号
    updateValueSignal = Signal(int)
    # 发出文本信号
    updateTextEditSignal = Signal(str, str)

    def __init__(self, dir, ext, prefix):
        super(Worker, self).__init__()
        self.dir = dir
        self.ext = ext
        self.prefix = prefix

    def run(self) -> None:
        """
        The thread begins running from here. run() is only called after start()
        """
        for (i, file) in enumerate(os.listdir(self.dir)):
            _, file_ext = os.path.splitext(file)
            if file_ext == self.ext:
                new_file_name = self.prefix + str(i) + self.ext
                src_path = os.path.join(self.dir, file)
                dst_path = os.path.join(self.dir, new_file_name)
                # os.rename(src, dst): src is original address of file to be renamed
                # and dst is destination location with new name.
                os.rename(src_path, dst_path)

                time.sleep(0.2)  # Uncomment if process is too fasta and want to see the updates
                self.updateValueSignal.emit(i + 1)
                self.updateTextEditSignal.emit(file, new_file_name)
            else:
                pass
        # 运行结束后重置值
        self.updateValueSignal.emit(0)  # reset the value of the progress bar


class RenameFilesGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setMinimumSize(600, 250)
        self.setWindowTitle("Change File Names GUI")
        self.directory = ""
        self.cb_value = ""
        self.setupWidgets()
        self.show()

    def setupWidgets(self):
        """
        Set up the widgets and layouts for interface.
        """
        dir_label = QLabel("Choose Directory:")
        self.dir_line_edit = QLineEdit()

        dir_button = QPushButton('...')
        dir_button.setToolTip("Select file directory.")
        dir_button.clicked.connect(self.setDirectory)

        self.change_name_edit = QLineEdit()
        self.change_name_edit.setToolTip(
            "Files will be appended with numerical values.For example: filename <b> 01 </b >.jpg")
        self.change_name_edit.setPlaceholderText("Change file names to...")

        rename_button = QPushButton("Rename Files")
        rename_button.setToolTip("Begin renaming files in directory.")
        rename_button.clicked.connect(self.renameFiles)

        file_exts = [".jpg", ".jpeg", ".png", ".gif", ".txt"]

        # Create combo box for selecting file extensions.
        ext_cb = QComboBox()
        self.cb_value = file_exts[0]
        ext_cb.setToolTip("Only files with this extension will be changed.")
        ext_cb.addItems(file_exts)
        ext_cb.currentTextChanged.connect(self.updateCbValue)

        # Text edit is for displaying the file names as they are updated.
        self.display_files_edit = QTextEdit()
        self.display_files_edit.setReadOnly(True)
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)

        # Set layout and widgets.
        grid = QGridLayout()
        grid.addWidget(dir_label, 0, 0)
        grid.addWidget(self.dir_line_edit, 1, 0, 1, 2)
        grid.addWidget(dir_button, 1, 2)
        grid.addWidget(self.change_name_edit, 2, 0)
        grid.addWidget(ext_cb, 2, 1)
        grid.addWidget(rename_button, 2, 2)
        grid.addWidget(self.display_files_edit, 3, 0, 1, 3)
        grid.addWidget(self.progress_bar, 4, 0, 1, 3)
        self.setLayout(grid)

    def setDirectory(self):
        """
        Choose the directory.
        """
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.Directory)
        self.directory = file_dialog.getExistingDirectory(self, "Open Directory", "", QFileDialog.ShowDirsOnly)
        if self.directory:
            self.dir_line_edit.setText(self.directory)
            # Set the max value of progress bar equal to max number of  files in the directory.
            num_of_files = len([name for name in os.listdir(self.directory)])
            self.progress_bar.setRange(0, num_of_files)

    def updateCbValue(self, text):
        """
        Change the combo box value. Values represent the different file extensions.
        """
        self.cb_value = text

    def renameFiles(self):
        """
        Create instance of worker thread to handle the file renaming process.
        """
        prefix_text = self.change_name_edit.text()
        if self.directory != "" and prefix_text != "":
            self.worker = Worker(self.directory, self.cb_value, prefix_text)
            self.worker.updateValueSignal.connect(self.updateProgressBar)
            self.worker.updateTextEditSignal.connect(self.updateTextEdit)
            self.worker.start()
        else:
            pass

    def updateProgressBar(self, value):
        self.progress_bar.setValue(value)

    def updateTextEdit(self, old_text, new_text):
        self.display_files_edit.append("[INFO] {} changed to{}.".format(old_text, new_text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = RenameFilesGUI()
    sys.exit(app.exec())
