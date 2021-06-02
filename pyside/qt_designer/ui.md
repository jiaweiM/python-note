# UI 文件

- [UI 文件](#ui-文件)
  - [将 Form 转换为 Python 代码](#将-form-转换为-python-代码)
  - [UIC](#uic)

2021-06-01, 20:18
***

## 将 Form 转换为 Python 代码

下面用 easing 示例演示。该示例包含一个源码 easing.py，一个 UI 文件 form.ui，一个资源文件 easing.qrc 以及 YAML 格式的项目文件 easing.pyproject：

```json
{
    "files": ["easing.qrc", "ui_form.py", "easing.py", "easing_rc.py", "form.ui"]
}
```

使用 uic 将 UI 文件转换为 Python 代码：

```bash
uic -g python form.ui > ui_form.py
```

## UIC

用户界面编译器（User Interface Compiler, uic）读取Qt Designer 生成的 XML 格式的界面定义文件 `.ui`，将其转换为 Python 代码。

使用命令：

```bash
uic [options] <uifile>
```

|Option|说明|
|---|---|
|-g, --generator `<python|cpp>`|选择生成器|
