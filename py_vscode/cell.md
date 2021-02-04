- [Jupyter](#jupyter)
  - [Jupyter 单元格](#jupyter-单元格)
  - [Python 交互窗口](#python-交互窗口)

# Jupyter

## Jupyter 单元格
定义 Jupyter 单元格，使用 `#%%` 注释，例如：
```py
#%%
msg = "Hello World"
print(msg)

#%%
msg = "Hello again"
print(msg)
```
文件后缀名为 `.py`.

`#%%` 注释开头的部分，下面对应一个Jupyter单元格。

Python 扩展程序会自动识别该单元格，在代码上面浮出运行单元格等各种选项，如下所示：

![](images/2019-09-20-13-56-55.png)

|选项|功能|
|---|---|
|**Run Cell**|运行当前单元格|
|**Run Below**|出现在第一个单元格，用于运行文件中所有的代码|
|**Run Above**|应用于单元格以上的所有单元格（不包括当前单元格）|


> NOTE: **Debug Cell** 默认只检测用户代码。如果要进入非用户代码，则需要取消Python 扩展（`Ctrl+,`）中的 **Data Science: Debug Just My Code** 勾选。

运行代码，例如点击 `Run Cell`，出现 Python 交互窗口，并显示运行结果：

![](images/2019-09-20-15-27-44.png)

也可以通过快捷键运行代码，`Ctrl+Enter` 运行当前单元格；`Shift+Enter`运行当前单元格，并移动到下一个单元格，如果处在最后一个单元格，则自动在后面插入 `#%%` 创建一个新的 Cell。

另外，还以通过点击行号左侧设置断点用于调试。

## Python 交互窗口
Python 交互窗口除了显示 Cell 的运行结果，还可以作为独立的控制台使用，在其中可以运行任意代码，不需要是 Cell。

如果交互窗口没打开，可以通过 **Show Python Interactive window** 命令打开。界面如下所示：

![](images/2019-09-20-16-09-14.png)

交互窗口分上下两个窗口，上面的窗口用于显示已执行的代码和输出结果；下面的窗口用于输入代码，按 `Enter` 键换行，按 `Shift+Enter` 运行代码。

已编码的文件也可以在交互窗口中执行，使用 **Run Current File in Python Interactive window** 命令，当前代码文件的代码被复制到交互窗口中执行。
