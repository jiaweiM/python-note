# Python 集合

- [Python 集合](#python-集合)
  - [简介](#简介)
  - [序列](#序列)
  - [序列操作](#序列操作)
    - [in](#in)
    - [s + t](#s--t)
    - [s * n](#s--n)
    - [切片](#切片)
    - [s.index](#sindex)
  - [slice](#slice)
    - [indices](#indices)
    - [命名切片](#命名切片)
  - [解压](#解压)
    - [字符串解压](#字符串解压)
    - [部分解压](#部分解压)
    - [解压可迭代对象](#解压可迭代对象)
  - [应用](#应用)
    - [删除序列相同元素并保持顺序](#删除序列相同元素并保持顺序)
    - [序列过滤](#序列过滤)

2021-06-02, 11:28
***

## 简介

Python 内置集合类型包括：list, dict, set, tuple.

- [list](collect_list.md)
- [Tuple](collect_tuple.md)
- [set](collect_set.md)
- [dict](collect_dict.md)
- [deque](collect_deque.md)

## 序列

Python 有三种基本序列类型：list, tuple 和 range。在处理二进制数据和文本字符串中有专门的序列类型。包括：Unicode string, strings, Byte arrays, Buffers, Xrange 等。

## 序列操作

下面总结的操作大部分序列都支持，不管是 mutable 还是 immutable。

`collections.abc.Sequence` 辅助自定义实现序列类型。

在下表中，`s` 和 `t` 是相同类型的序列，`n`, `i`, `j`, `k` 为整数，`x` 是满足 `s` 类型和值的任意对象。

`in` 和 `not in` 和对比操作符具有相同的优先级。

`+` (串联)和 `*` (重复) 和对应的数学操作符有相同的优先级。

| **操作** | **结果** |
| --- | --- |
| `x in s` | 如果 s 中有元素等于 `x`，返回 `True`，否则 `False` |
| `x not in s` | 如果 s 中有元素等于 `x`，返回 `False`，否则 `True` |
| `s + t` | 返回 `s` 和 `t` 的串联结果 |
| `s * n` or `n * s` | 等价于将 `s` 相加 n 次 |
| `s[i]` | `s` 的第 i 个元素 |
| `s[i:j]` | 返回 i 到 j 的元素，不包含j，称为切片 |
| `s[:j]` | 返回前 j 个 元素 |
| `s[i:]` | 从第 i 个到结尾的所有元素 |
| `s[-3:]` | 最后3个元素 |
| `s[i:j:k]` | i 到 j step 为 k 的切片 |
| `s[::2]` | 偶数索引的所有元素 |
| `s[::-1]` | s 的反向 copy |
| `len(s)` | `s` 的长度 |
| `min(s)` | `s` 最小元素 |
| `max(s)` | `s` 最大元素 |
| `s.index(x[, i[, j]]]` | `x` 在 `s` 中第一次出现的位置（i, j 指定查找范围） |
| `s.count(x)` | `s` 中 `x` 出现的次数 |

相同类型的序列也支持对比。tuple 和 list 按照字典顺序比对每个元素。如果两个序列相等，那么它们必然有相同的长度和类型，且每个元素依次相等。

### in

`in` 和 `not in` 操作一般用于简单的包含测试操作，有些序列（如 `str`, `bytes`, `bytearray`）也使用它们进行子序列测试：

```py
>>> "gg" in "eggs"
True
```

### s + t

合并序列操作：返回 `s` 和 `t` 的合并序列。例如：

```py
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
assert c == [1, 2, 3, 4, 5, 6]
```

合并 immutable 序列总是返回一个新对象。这意味着通过合并序列获得重复串联序列的运行时消耗和总长度的二次方关系。要获得线性消耗，可以采用其它方法：

- 对 `str` 对象，可以先构建一个 list，然后使用 `str.join()` 合并；或者写入 `io.StringIO`，完成后读取。
- 对 `bytes` 对象，类似地可以使用 `bytes.join()` 或 `io.BytesIO`，或者使用 `bytearray` 对象之心原位合并。`bytearray` 是 mutable 对象，可以高效分配额外空间。
- 对 `tuple` 对象，可采用 `list` 对象

部分序列（如 `range`）不支持序列合并。

### s * n

语法：
`s * n` or `n * s`

序列重复：如果 `n` 值小于 0，当 0 处理，生成和 `s` 同类型的空序列。要注意 `s` 中的元素没有被复制，而是被引用多次。例如：

```py
>>> lists = [[]] * 3
>>> lists
[[], [], []]
>>> lists[0].append(3)
>>> lists
[[3], [3], [3]]
```

`[[]]` 包含一个空列表元素，所以 `[[]] * 3` 引用了三次包含一个空列表元素的列表。修改 `lists` 的任一元素都会修改整个引用。

所以还可以这样创建列表：

```py
>>> lists = [[] for i in range(3)]
>>> lists[0].append(3)
>>> lists[1].append(5)
>>> lists[2].append(7)
>>> lists
[[3], [5], [7]]
```

部分序列类型，例如 `range`，只支持特定模式的序列，不支持序列乘积。

### 切片

语法：

- `s[i]`
- `s[i:j]`
- `s[i:j:k]`

切片要点：

- 如果 `i` 或 `j` 为负值，则索引相对序列 `s` 末端定义，实际索引为 `len(s) + i` 或 `len(s) + j`，不过要注意，`-0` 依然为 0。
- `s` 从 `i` 到 `j` 的切片定义为索引 `[i,j)` 范围内的所有元素。
- 如果 i 或 j 大于 `len(s)`，则采用 `len(s)`。
- 如果不指定 `i` 或 `i` 为 `None`，`i` 为 `0`。
- 如果 `j` 未指定或为 `None`，`j` 为 `len(s)`
- 如果 `i` 大于等于 `j`，切片为空。
- 指定 `k` 的切片包含索引为 `x=i+n*k`的所有元素，其中 `0 <= n < (j-i)/k`。即包括 `i`, `i+k`, `i+2*k` 等。直到 `j`，但不包含 `j`。
  - 如果 k 为正数，i 和 j 最大为 `len(s)`，如果超过 `len(s)`，实际采用直仍是 `len(s) - 1`
  - 如果 k 为负数，i 和 j 最大为 `len(s) - 1`，如果超过 `len(s) - 1`，仍采用 `len(s) - 1`
  - 如果未指定 i, j 或为 `None`，以 1 处理

### s.index

语法：

```py
s.index(x,[, i[, j]])
```

返回 `x` 在 `s` 中第一次出现的地方（范围 $$[i, j)$$）。

如果 `s` 没有找到 `x`，抛出 `ValueError`。

使用 `i`, `j` 参数可以只检索部分序列，但并非所有序列实现支持该参数。使用 `i`, `j` 大致等效于 `s[i:j].index(x)`，但是不复制任何数据，索引也是相对于原序列的位置。

## slice

```py
class slice(stop)
class slice(start, stop[, step])
```

返回 `range(start, stop, step)` 对应索引的切片对象。

切片对象（slice）包含三个只读属性 `start`, `stop` 和 `step`。`start` 和 `step` 默认为 `None`。

```py
>>> a = slice(5, 50, 2)
>>> a.start
5
>>> a.stop
50
>>> a.step
2
```

默认值：

```py
a = slice(3)
assert a.start is None
assert a.step is None
assert a.stop == 3
```

**所有使用切片的地方都可以使用切片对象**。例如：

```py
>>> items = [0, 1, 2, 3, 4, 5, 6]
>>> a = slice(2, 4)
>>> items[2:4]
[2, 3]
>>> items[a]
[2, 3]
>>> items[a] = [10,11]
>>> items
[0, 1, 10, 11, 4, 5, 6]
>>> del items[a]
>>> items
[0, 1, 4, 5, 6]
```

### indices

调用切片的 `indices(size)` 方法可以将它映射到一个已知大小的序列上。这个方法返回一个三元组 `(start, stop, step)`，所有的值都会被调整以适合序列边界。这样就不会出现 `IndexError`。例如：

```py
s = 'HelloWorld'
a = slice(5, 50, 2)
b = a.indices(len(s))
assert b == (5, 10, 2)
```

### 命名切片

如果你的程序中包含大量无法直视的硬编码切片，此时可以考虑命名切片。例如，从一个记录（文件或其它类似格式）中的某些固定位置提取字段：

```py
######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
```

此时可以采用命名切片：

```py
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
```

这样避免了使用大量难以理解的硬编码下标，代码更加清晰。

## 解压

装箱：使用多个变量，创建 Tuple、List 等序列对象.

拆箱：使用序列给多个变量赋值。

任何序列（或可迭代对象）通过一个简单的赋值语句可以解压并赋值给多个变量，只要**变量数量和序列元素的数量相同**。如果变量个数和元素个数不匹配，抛出异常。

这种方式可以用于任何可迭代对象，包括列表、元祖、字符串、文件对象、迭代器和生成器等。

例如

```py
v = ('a', 2, True)
(x, y, z) = v
a, b, c, = v # 也可以不带括号
```

基于该原理，可以很容易的值互换：

```py
a, b = b, a
```

如果有个变量带 `*` 号，则多余的值全部给该变量。

### 字符串解压

这种解压方式可以用在任意可迭代对象上。例如字符串：

```py
s = 'hello'
a, b, c, d, e = s
assert a == 'h'
assert b == 'e'
assert c == 'l'
assert d == 'l'
assert e == 'o'
```

### 部分解压

有时候你只需要部分数据，Python 没有提供这种语法，但可以用占位符，丢掉这些变量即可。比如使用 `_` 或 `ign`（ignore）。

这里使用 `_` 占位，要保证该占位符没有用作其它变量名。

```py
>>> data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
>>> _, shares, price, _ = data
>>> shares
50
>>> price
91.1
```

### 解压可迭代对象

如果可迭代对象的元素个数超过变量数，抛出 `ValueError`，但是你确实不需要这么多数据怎么办?

可以用 Python 星号表达式解决这个问题。

- 星号在中间

比如，你在学习一门课程，在学期末的时候，你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。如果只有四个分数，你可能就直接去简单的手动赋值， 但如果有 24 个呢？这时候星号表达式就派上用场了：

```py
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)
```

- 星号在最后

另外一种情况，假设你现在有一些用户的记录列表，每条记录包含一个名字、邮件，接着就是不确定数量的电话号码。你可以像下面这样分解这些记录：

```py
>>> record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
>>> name, email, *phone_numbers = record
>>> name
'Dave'
>>> email
'dave@example.com'
>>> phone_numbers
['773-555-1212', '847-555-1212']
```

值得注意的是上面解压出的 `phone_numbers` 变量永远是列表类型，不管解压的电话号码有多少个（包括 0 个）。所以，任何使用到 phone_numbers 变量的代码不需要做多余的类型检查去确认它是否是列表类型了。

- 星号在开始

星号表达式也能用在列表的开始部分。比如，你有一个公司前 8 个月销售数据的序列，但是你想看下最近一个月数据和前面 7 个月的平均值的对比。你可以这样做：

```py
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
return avg_comparison(trailing_avg, current_qtr)
```

- 用于变成元祖

例如，下面是一个带标签的元祖序列：

```py
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
```

- 用于字符串分割

星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。

```py
>>> line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
>>> uname, *fields, homedir, sh = line.split(':')
>>> uname
'nobody'
>>> homedir
'/var/empty'
>>> sh
'/usr/bin/false'
```

- 解压后丢弃

有时候，你想解压一些元素后丢弃，此时不能简单用 `*`，因为解压时 `*` 后必须跟随名称，此时可以采用废弃名称，如 `_` 或 `ign`:

```py
>>> record = ('ACME', 50, 123.45, (12, 18, 2012))
>>> name, *_, (*_, year) = record
>>> name
'ACME'
>>> year
2012
```

- 类似列表功能

在很多函数式语言中，星号解压语法跟列表处理有许多相似之处。比如，如果你有一个列表，你可以很容易的将它分割成前后两部分：

```py
>>> items = [1, 10, 7, 4, 5, 9]
>>> head, *tail = items
>>> head
1
>>> tail
[10, 7, 4, 5, 9]
```

- 递归

解压分割语法甚至可以用来实现递归算法，例如：

```py
>>> def sum(items):
...     head, *tail = items
...     return head + sum(tail) if tail else head
...
>>> sum(items)
36
```

不过递归不是 Python 擅长的，此处仅用于演示。

## 应用

### 删除序列相同元素并保持顺序

删除重复元素，可以简单的构造集合，例如：

```py
>>> a
[1, 5, 2, 1, 9, 1, 5, 10]
>>> set(a)
{1, 2, 10, 5, 9}
```

但是这种方法不能维护元素的顺序，生成的结果中元素的位置被打乱。下面的方法可以维护元素顺序。

- 如果序列上的值都是 `hashable` 类型，那么可以使用集合或生成器来解决该问题。比如：

```py
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
```

下面是使用该函数的例子：

```py
>>> a = [1, 5, 2, 1, 9, 1, 5, 10]
>>> list(dedupe(a))
[1, 5, 2, 9, 10]
```

如果序列元祖不是 `hashable`，比如 `dict` 类型，需要稍微修改上述代码：

```py
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
```

这里的 key 参数指定一个函数，将序列元素转换为 `hashable` 类型。例如：

```py
>>> a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
>>> list(dedupe(a, key=lambda d: (d['x'],d['y'])))
[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
>>> list(dedupe(a, key=lambda d: d['x']))
[{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
```

上例中使用了生成器函数，使得函数更加通用，不仅仅局限于列表。设置可以用来读取文件、删除重复行：

```py
with open(somefile,'r') as f:
for line in dedupe(f):
    ...
```

上述的 key 函数参数模仿了 `sorted()`, `min()` 和 `max()` 等内置函数的功能。

### 序列过滤

过滤序列元素的最简单方法是使用序列推导：

```py
>>> mylist = [1, 4, -5, 10, -7, 2, 3, -1]
>>> [n for n in mylist if n > 0]
[1, 4, 10, 2, 3]
>>> [n for n in mylist if n < 0]
[-5, -7, -1]
```

使用列表推导的一个潜在缺陷是，如果输入非常大会产生一个非常大的结果集，占用大量内存。如果对内存比较敏感，可以使用生成器表达式迭代过滤后的元素：

```py
>>> pos = (n for n in mylist if n > 0)
>>> pos
<generator object <genexpr> at 0x1006a0eb0>
>>> for x in pos:
... print(x)
...
1
4
10
2
3
```

如果过滤规则比较复杂，不能简单的在列表推导或者生成器表达式中表达出来。比如，过滤的时候需要处理异常等情况。这时可以将过滤代码放到一个函数中，然后使用内置的 `filter()` 函数。比如：

```py
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)
# Outputs ['1', '2', '-3', '4', '5']
```

`filter()` 函数创建了一个迭代器，如果想得到列表，可以用 `list()` 转换。

- 过滤时转换数据

```py
>>> mylist = [1, 4, -5, 10, -7, 2, 3, -1]
>>> import math
>>> [math.sqrt(n) for n in mylist if n > 0]
[1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]
```

- 过滤并替代

将不符合条件的值用默认值替代。

```py
>>> clip_neg = [n if n > 0 else 0 for n in mylist]
>>> clip_neg
[1, 4, 0, 10, 0, 2, 3, 0]
>>> clip_pos = [n if n < 0 else 0 for n in mylist]
>>> clip_pos
[0, 0, -5, 0, -7, 0, 0, -1]
```

- `itertools.compress`

`itertools.compress()` 以一个 `iterable` 对象和一个对应的 `Boolean` 选择器序列作为输入参数。然后输出 `iterable` 对象中对应选择器为 `True` 的元素。

当你需要用另一个关联序列过滤某个序列时，这个函数非常有用。假设你有下面两列数据：

```py
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
```

现在你想要将那些 `count` 大于 5 的地址全部输出，你可以这么做：

```py
>>> from itertools import compress
>>> more5 = [n > 5 for n in counts]
>>> more5
[False, False, True, False, False, True, True, False]
>>> list(compress(addresses, more5))
['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']
```

这里关键是要先创建一个 `Boolean` 序列，指定那些元素符合条件。然后 `compress()` 函数根据这个序列去选择输出对应位置为 `True` 的元素。

和 `filter()` 函数类似，`compress()` 也返回一个迭代器。
