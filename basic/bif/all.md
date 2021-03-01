# all

可迭代对象的所有值为 True 时，返回 True。

如果可迭代对象为空，也返回 True。

- list 实例：

```py
l = [1, 3, 4, 5]
assert all(l)

l.append('') # 空字符串为 false
assert not all(l)

# all values false
l = [0, False]
assert not all(l)

# one false value
l = [1, 3, 4, 0]
assert not all(l)

# one true value
l = [0, False, 5]
assert not all(l)

# empty iterable
assert all([])
```

- tuple 实例

```py
t = ('Tuple')
assert all(t)

t1 = ('Tuple', '')
assert not all(t1)
```
