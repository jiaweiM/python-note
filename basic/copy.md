# Copy

- [Copy](#copy)
- [概述](#概述)
- [Copy module](#copy-module)
  - [浅拷贝](#浅拷贝)
  - [深拷贝](#深拷贝)

# 概述
在 Python 中，我们使用 `=` 复制对象，但是并没有创建新的对象，而是创建了一个对原对象的引用。

而要深拷贝原对象，可以使用 `copy` 模块。

# Copy module
可以使用 `copy` 模块做浅拷贝和深拷贝。
- 浅拷贝创建一个对原对象里元素的引用，但是不会递归的去创建内嵌对象的拷贝，而仅仅是引用
- 

## 浅拷贝
`copy.copy()` 方法用于浅拷贝。例如：

```py
import copy
o_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n_list = copy.copy(o_list)

o_list.append([4, 4, 4])

assert len(o_list) == 4
assert len(n_list) == 3

o_list[0][0] = 0
assert n_list[0][0] == 0
```

由于是浅拷贝，所以 `n_list` 只是创建了对 `o_list` 内元素的引用即指向 `[1, 2, 3]`, `[4, 5, 6]` 和 `[7, 8, 9]` 的引用，所以在 `o_list` 添加新的列表时，由于复制时没有创建对应的引用，所以`n_list` 不改变。

也由于是浅拷贝，在修改已有内嵌元素的值 `o_list[0][0]` 时，`n_list` 也随之改变。

## 深拷贝
使用 `copy.deepcopy()` 方法可以进行深拷贝。

深拷贝会递归的进行拷贝，创建的对象完全独立于原来的对象。还是以上面的例子说明：
```py
o_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n_list = copy.deepcopy(o_list)

o_list[0][0] = 0
assert n_list[0][0] == 1
```

此时对原对象进行修改，对 `n_list` 没有影响。

