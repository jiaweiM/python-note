# QDialog

- [QDialog](#qdialog)
  - [QFontDialog](#qfontdialog)
  - [QFileDialog](#qfiledialog)
    - [创建 QFileDialog](#创建-qfiledialog)
    - [FileMode](#filemode)

## QFontDialog

`QFontDialog` 提供字体选择对话框。

![](images/2021-03-28-10-32-11.png)

通过静态方法 `getFont()` 创建对话框：

```cpp
bool ok;
QFont font = QFontDialog::getFont(
                &ok, QFont("Helvetica [Cronyx]", 10), this);
if (ok) {
    // the user clicked OK and font is set to the font the user selected
} else {
    // the user canceled the dialog; font is set to the initial
    // value, in this case Helvetica [Cronyx], 10
}
```

## QFileDialog

`QFileDialog` 提供选择文件或文件夹的对话框。

![](images/2021-03-28-12-32-09.png)

### 创建 QFileDialog

创建 `QFileDialog` 的最简单方式是使用静态方法：

```cpp
fileName = QFileDialog::getOpenFileName(this,
    tr("Open Image"), "/home/jana", tr("Image Files (*.png *.jpg *.bmp)"));
```

该对话框显示初始目录 "/home/jana" 中匹配 "Image Files (*.png *.jpg *.bmp)" 文件。对话框的父级为 `this`，窗口标题设置为 `"Open Image"`。

如果要使用多个过滤器，可以用两个分隔过滤器，例如：

```cpp
"Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml)"
```

也可以不使用静态函数创建，然后调用 `setFileMode()` 设置模式：

```cpp
QFileDialog dialog(this);
dialog.setFileMode(QFileDialog::AnyFile);
```

这里使用 `AnyFile` 模式，表示可以选择任意文件，包括不存在的文件，适合于保存文件。

### FileMode

`fileMode` 属性指定对话框的操作模式，即用户期望选择的对象类型。

`FileMode` 指定用户在文件对话框中可以选择的内容。 即用户点击 OK 时返回的内容：

|常量|描述|
|---|---|
|`QFileDialog.AnyFile`|任意文件，包括不存在的文件，适合于保存文件|
|`QFileDialog.ExistingFile`|已有文件|
|`QFileDialog.Directory`|目录|
|`QFileDialog.ExitingFiles`|多个文件|
