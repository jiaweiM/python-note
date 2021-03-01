# any

可迭代对象任何元素为 true，返回 true，否则返回 False.

如果可迭代对象为空，返回 False。

- list 实例

```py
# 空 list，或其中全是 0 或 False，返回 False
lst = ['', 0, False, 0.0, None]
assert not any(lst)

l = [1, 3, 4, 0]
assert any(l)

l = [0, False]
assert not any(l)

l = [0, False, 5]
assert any(l)

assert not any([])
```