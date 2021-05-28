from PySide6.QtWidgets import QApplication, QWidget
import sys

# 对每个应用需要一个 QApplication 实例
app = QApplication(sys.argv)

# widget 作为窗口显示
window = QWidget()
# 默认隐藏，显示窗口
window.show()

# 开始事件循环
app.exec()
