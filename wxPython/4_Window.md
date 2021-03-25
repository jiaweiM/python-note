# Window

## Show

```py
Show(show=True)
```

显示或隐藏窗口。`show=True` 表示显示，`show=False` 表示隐藏。

如果需要窗口在顶层显示，可以调用 `Raise` 方法，但是如果是创建窗口后立刻调用 `Show`，则不需要。

新窗口的**顶层窗口**默认隐藏（扩展 `TopLevelWindow`），其它则默认显示。

