# Frame

## 简介

`wx.Frame` 是顶层窗口，

## 构造函数

```py
Frame(parent, id=ID_ANY, title="", pos=DefaultPosition, size=DefaultSize, style=DEFAULT_FRAME_STYLE, name=FrameNameStr)
```

- `parent`

父窗口 `wx.Window`，通常为 `None`。如果不是 `None`，则 `Frame` 随着父窗口最小化或恢复。`Frame` 自带有最小化和恢复功能。

- `id`

`wx.WindowID`，窗口识别符，-1 表示采用默认值。

- `title`

`string`，frame 的标题。

- `pos`

`wx.Point`，窗口位置。`DefaultPosition` 表示默认位置。

- `size`

`wx.Size`，窗口大小。`DefaultSize` 表示默认尺寸。

- `style`

`long`，窗口风格。

- `name`

`string`，窗口名称，设置名称后可以通过名称设置 Motif 资源值。
