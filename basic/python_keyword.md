# Python 关键字

- [Python 关键字](#python-关键字)
  - [简介](#简介)
  - [assert](#assert)
  - [del](#del)
  - [else](#else)
  - [pass](#pass)
  - [参考](#参考)

2018-06-30, 09:56
@author Jiawei Mao
***

## 简介

| False | class | finally | is | return |
| --- | --- | --- | --- | --- |
| None | continue | for | lambda | try |
| True | def | from | nonlocal | while |
| and | del | global | not | with |
| as | elif | if | or | yield |
| assert | else | import | pass |   |
| break | except | in | raise |   |

## assert

断言，确定某个返回 bool 值的代码语句一定返回 true：

- 如果返回 false，抛出 `AssertionError` 并结束程序；
- 如果返回 true，代码继续执行。

语法：

```py
assert <condition>
assert <condition>,<error message>
```

`assert` 使用语法有两种：

- 第一种判断条件是否正确，如果错误，中止程序并抛出 `AssertionError`；
- 第二种除了抛出 `AssertionError`，还会给出提供的错误信息。

例如：

```py
assert 0 != 0, "not right"
```

运行输出：

```py
AssertionError: not right
```

**总结**

- `assert` 后面包含一个 bool 表达式和可选的信息；
- `assert` 可以用于检查类型、参数值、函数输出等各种信息；
- `assert` 可作为 debug 工具使用。

## del

`del` 用于删除对象引用。在 Python 中一切都是对象。

例如，使用 del 删除集合中的元素：

```py
a = ['x','y','z']
del a[1]
```

## else

else 语句一般和 if一起用，还可以和 for 或 while 循环一起用。else 中的代码在 for 或 while 循环正常结束后执行。

else 和try/except 一起用，在无异常时执行。

## pass

pass 语句用于指示一个没有内容的语句块。

## 参考

- [https://www.programiz.com/python-programming/keyword-list](https://www.programiz.com/python-programming/keyword-list)
