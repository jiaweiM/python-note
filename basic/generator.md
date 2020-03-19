- [简介](#%e7%ae%80%e4%bb%8b)
- [创建生成器](#%e5%88%9b%e5%bb%ba%e7%94%9f%e6%88%90%e5%99%a8)
- [生成器表达式](#%e7%94%9f%e6%88%90%e5%99%a8%e8%a1%a8%e8%be%be%e5%bc%8f)

# 简介
在 Python 中构建迭代器有许多开销，我们需要创建实现 `__iter__()` 和 `__next__()` 方法的类，还需要记录内部状态，在没有值的时候抛出 `StopIteration` 异常。这个过程即冗长又不够直观，生成器（generator）是用于创建迭代器的函数。

# 创建生成器
创建生成器和一般函数一样简单，只是将 `return` 语句替换为 `yield` 语句。不同点在于：
- 生成函数包含至少一个 `yield` 语句；
- 调用时创建迭代器对象，但是不立刻开始执行；
- `__iter__()` 和 `__next__()` 方法被自动实现，所以可以通过 `next()` 方法获得下一个元素；
- 生成器执行到 `yield` 语句时暂停执行，控制流转移到调用函数
- 对生成器，连续调用时其内存状态都被保存
- 函数结束时，自动抛出 `StopIteration`

如果一个函数包含至少一个 `yield` 语句，该函数就成为了**生成器**。`yield` 和 `return` 一样，都会从函数返回值，其差别在于，`return` 语句会直接结束函数的执行，而 `yield` 只是暂停执行，并记住函数当前状态，随后从暂停时的状态继续执行。

例：
```py
import pytest

def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

def test_gen():
    a = my_gen()
    n = next(a)
    assert n == 1
    n = next(a)
    assert n == 2
    n = next(a)
    assert n == 3
    with pytest.raises(StopIteration):
        next(a)
```

可以看到，每次调用 `next()` 都返回一个新的值，`my_gen()` 在连续调用过程中，其执行状态被保存。

当然，这个例子只是单纯的为了展示生成器，生成器大部分时候都应该在循环语句中，例如：
```py
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]
```
该生成器对输入的字符串参数，从后向前，依次返回对应位置的字符。

# 生成器表达式
对于一些简单的生成器，可以直接通过生成器表达式创建。就像 lambda 函数创建匿名函数，生成器表达式创建匿名生成器函数。

生成器表达式类似于 list，差别在于 generator 不一次返回所以值，所以内存暂用低，同时也无法用索引访问，只能通过 `next()` 或 for 循环访问。如下所示：
```py
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
[x**2 for x in my_list]

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
(x**2 for x in my_list)
```

可以看到，生成器并没有直接生成对应的值。
