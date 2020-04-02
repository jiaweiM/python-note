# List

- [List](#list)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [创建 List](#%e5%88%9b%e5%bb%ba-list)
    - [多维 list](#%e5%a4%9a%e7%bb%b4-list)
  - [函数](#%e5%87%bd%e6%95%b0)
  - [列表推导](#%e5%88%97%e8%a1%a8%e6%8e%a8%e5%af%bc)
  - [内嵌列表推导](#%e5%86%85%e5%b5%8c%e5%88%97%e8%a1%a8%e6%8e%a8%e5%af%bc)
  - [del](#del)
  - [List as Stack](#list-as-stack)
  - [List as Queue](#list-as-queue)

***

## 简介

List 为序列类型，可方便的执行添加、删除操作。List 为mutable 类型。

## 创建 List

创建类型相同的List

```py
l = [1, 2, 3, 4]
```

创建包含多种类型的List

```py
l2 = ["a string", 12]
```

其他创建list的方法

```py
list1 = list() # empty list
list2 = list([22, 31, 61])
list3 = list(["a", "b", "c"])
list5 = list("python") # Create a list with characters p, y, t, h, o, n
```

### 多维 list

你可能会尝试使用如下方式创建多维数组：

```py
>>> A = [[None] * 2] * 3
```

输出出来，貌似是对的：

```py
>>> A
[[None, None], [None, None], [None, None]]
```

但是当你赋值时，就发现不对劲了：

```py
>>> A[0][0] = 5
>>> A
[[5, None], [5, None], [5, None]]
```

在一个地方赋值，该值出现在多个地方。

其原因是使用 `*` 重复 list 并没有创建副本，而只是创建对当前对象的引用。`*3` 只是创建原 list 的三个引用。所以修改一个，其它两个也会随之改变。

创建多维 list 的推荐方式是依次创建一维和二维 list:

```py
A = [None] * 3
for i in range(3):
    A[i] = [None] * 2
```

也可以使用列表推断：

```py
w, h = 2, 3
A = [[None] * w for i in range(h)]
```

当然也能使用扩展包，比如著名的 NumPy。

## 函数

| 函数                               | 说明                                                       |
| ---------------------------------- | ---------------------------------------------------------- |
| list.append(x)                     | 添加 x 到列表末尾                                          |
| list.extend(`iterable`)            | 将 `iterable` 中的所有元素添加到列表末尾                   |
| list.insert(i, x)                  | 插入值到指定位置。第一个参数为插入的位置                   |
| list.remove(x)                     | 删除列表中第一个 `x` 元素，不含 `x` 抛出 `ValueError`      |
| list.pop([i])                      | 删除并返回指定位置的元素，如果不指定 `i`，默认为最后一个值 |
| list.clear()                       | 删除所有元素                                               |
| list.index(x[,start[,end]])        | 返回第一个 x 出现的索引，没有x抛出 `ValueError`            |
| list.count(x)                      | x 出现的次数                                               |
| list.sort(key=None, reverse=False) | list 原位排序，参数解释查看 `sorted()` 函数                |
| list.reverse()                     | 原位反向排序                                               |
| list.copy()                        | 浅复制，等价于 `a[:]`                                      |

函数说明：

- `insert`, `remove` 或 `sort` 等方法仅修改 list 而不返回值，即返回默认的 `None`。这是Python中所有 mutable 数据结构的设计原则。
- 有些数据无法排序或对比，如 `[None, 'hello', 10]`。

添加元素：

- 通过 `append()` 添加单个元素。append() 不返回值，而是修改原 list.
  - 通过 append() 添加list, 参数 list 被当做一个元素添加进来，构成嵌套 list。要将 list 的元素依次添加进来，用 `extend()`
- 通过 extend() 添加多个元素。
- 通过 + 连接两个 list，生成一个新的list。
- 通过 * 将一个 list 重复 n遍，生成一个新的 list.

## 列表推导

以一种简洁的方式创建List，在方括号中包含创建元素的表达式。例：

```py
list1 = [ x for x in range(10)]  # list in range [0, 9]
list2 = [ x +1 for x in range(10)] # list in range [1, 10]
list3 = [x for x in range(10) if x %2 == 0] # [0, 2, 4, 6, 8]
list4 = [x*2 for x in range(10) if x % 2 == 0]  # [0, 4, 8, 12, 16]
```

列表推导（List Comprehension）由包含表达式的方括号组成，其中后面跟着一个 for 自居，然后是零或多个 for 或 if 子句，返回一个列表。例如，返回 list 中不相等的元素对：

```py
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

等价于：

```py
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

可以发现，列表推导中 `for` 语句和 `if` 语句的顺序和下面相同。但是返回值放在了最开始。

> 如果返回多个值，一定要加括号。

```py
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

列表推导中也可以包含复杂的表达式和内嵌函数：

```py
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

## 内嵌列表推导

列表推导的初始表达式可以是任意表达式，当然也可以是另一个列表推导。

例如，对下面的 3x4 矩阵，即长度为 4 的 3 个 list 构成的一个 list:

```py
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```

下面的列表推导可以将其行和列转换：

```py
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

因为表达式是在 for 循环中求值，所以上例等价于：

```py
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

进一步：

```py
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

在实际应用中，使用内置函数更方便，此处使用 `zip()` 函数正好：

```py
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

## del

list 的方法只能通过值删除元素。而使用 `del` 语句，可以通过索引删除元素。

`del` 可删除列表切片，也可以清空整个列表。例如：

```py
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

`del` 甚至可以用来删除变量：

```py
>>> del a
```

在后面引用 `a` 会抛出错误。

## List as Stack

list 的方法使其很容易作为堆栈使用，使用 `append()` 方法添加元素到堆栈顶部，使用 `pop()` 方法获取堆栈顶部元素。例如：

```py
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
assert stack.pop() == 7
assert stack.pop() == 6
assert stack.pop() == 5
```

## List as Queue

List 也可以作为 Queue 使用（First in, first out），不过效率不是很高。从末尾添加删除很快，从开始插入和删除元素很慢（因为余下的元素都要随之便宜）。

如果要使用 queue功能，可以使用 [`collections.deque`](collect_deque.md)，该数据结构在两侧添加和删除元素都很快。
