import sys
from PySide6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

wid = QtWidgets.QWidget()
wid.resize(250, 150)
wid.setWindowTitle("Simple")
wid.show()

sys.exit(app.exec_())
