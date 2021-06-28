# QTextEdit

- [QTextEdit](#qtextedit)
  - [简介](#简介)
  - [QPlainTextEdit](#qplaintextedit)
  - [参考](#参考)

2021-06-08, 09:58
***

## 简介

`QTextEdit`  用于编辑和显式纯文本及富文本，是一个高级的 WYSIWYG 编辑器，支持 HTML 和 Markdown 格式。`QTextEdit` 经过优化，对大型文档能快速响应。

`QTextEdit` 按段落和字符工作。段落是一个格式化字符串，根据控件宽度自动换行。对纯文本，一个换行符对应一个段落。段落中的词按照段落的对齐方式进行排列。段落中的每个字符都有自己的属性，包括字体、颜色等。

`QTextEdit` 可以显示图像、列表和表格。

## QPlainTextEdit

`QPlainTextEdit` 用于纯文本的编辑和显式。

![](images/2021-03-28-17-14-10.png)


## 参考

- https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTextEdit.html#PySide6.QtWidgets.PySide6.QtWidgets.QTextEdit
