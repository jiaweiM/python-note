# QScrollArea

## 简介

`QScrollArea` 提供滚动显示子部件的区域。如果子控件尺寸超出 Frame 大小，则自动提供滚动条，以便查看子控件的整个区域。设置子控件方法：

```py
imageLabel = QLabel()
image = QImage("happyguy.png")
imageLabel.setPixmap(QPixmap.fromImage(image))
scrollArea = QScrollArea()
scrollArea.setBackgroundRole(QPalette.Dark)
scrollArea.setWidget(imageLabel)
```

