# App

- [App](#app)
  - [简介](#简介)
  - [MainLoop](#mainloop)

2021-03-25, 09:08

## 简介

所有的 wxPython 程序都是 `wx.App` 实例。对简单的应用，可以直接使用 `wx.App`，对复杂的应用，则需要扩展 `wx.App` 实现更多功能。

`wx.App` 有四个可选关键字参数：

```py
wx.App(redirect=False, filename=None, useBestVisual=False,clearSigInt=True)
```

- `redirect`： 为 `True`表示将 `stdout` 重定向到 debug 窗口。
- `filename`：如果 `redirect=True` 并且该参数不是 `None`，则将 `stdout` 重定向该参数指定的文件。
- `useBestVisual`：是否尝试使用底层工具包提供的最佳视觉效果。（对大多数系统没用）
- `clearSigInt`：将此设置为 `True` 时，可以通过快捷键 `Ctrl+C` 终止程序。

## MainLoop

执行 GUI 事件循环。
