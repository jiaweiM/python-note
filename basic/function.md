# Python 函数

- [Python 函数](#python-函数)
  - [简介](#简介)
  - [创建函数](#创建函数)
  - [函数返回值](#函数返回值)
  - [局部变量和全局变量](#局部变量和全局变量)
  - [参数](#参数)
    - [关键字参数](#关键字参数)
    - [默认参数](#默认参数)
    - [可变参数 *args](#可变参数-args)
    - [**kwargs](#kwargs)
  - [Unpacking Argument Lists](#unpacking-argument-lists)
  - [Lambda 函数](#lambda-函数)

2021-06-02, 11:05
*****

## 简介

函数是可重复使用的代码片段。

形参：parameters
实参：arguments

## 创建函数

语法：

```python
def function_name(arg1, arg2, arg3, … argN):
  # statement inside function
```

## 函数返回值

return 后不带任何值，则返回 `None` .

可以一次返回多个值，值之间以逗号分开，为 tuple 类型。

## 局部变量和全局变量

如果局部变量和全局变量同名，则全局变量被覆盖，如果要在函数内修改全局变量的值，需加 `global` ：

```python
t = 1
def increment():
  global t   # now t inside the function is same as t outside the function
  t = t + 1
  print(t)   # Displays 2

increment()
print(t)  # Displays 2
```

声明的global 变量时不能赋值，下面的做法是错误的：

```python
t = 1
def increment():
  # global t = 1   # this is error
  global t
  t = 100   # this is okay
  t = t + 1
  print(t)  # Displays 101

increment()
print(t)  # Displays 101
```

可以在函数内部声明全局变量：

```python
def foo():
  global x  # x is declared as global so it is available outside the function
  x  = 100

foo()
print(x)
```

即，在函数内部访问全局变量，需要通过 `global` 关键字。

## 参数

### 关键字参数

给方法传递参数的方法有两种：根据位置和根据关键字。
关键字参数：

```py
def named_args(name, greeting):
  print(greeting + " " + name)
```

调用：使用关键字，参数的顺序无所谓

```py
named_args(name='jim', greeting='Hello')
# Hello jim

named_args(greeting = 'Hello', name='jim')
# Hello jim
```

可以混合使用基于位置和基于关键字的参数，不过基于位置的参数必须在基于关键字参数之前。

### 默认参数

在定义函数时给参数赋值即可：

```py
def func(i, j=100):
  print(i, j)
```

默认参数应该放在函数参数列表的末尾。

### 可变参数 *args

`*args` 和 `**kwargs` 在函数定义中将不定数目的参数传递给函数。

使用 `*args` 传递可变数目的非关键字参数给函数。例如，下面是包含两个参数的函数：

```py
def sum(a, b):
    print("sum is", a+b)
```

如果希望传递多个参数进去，此时可以用 `*args` 定义函数：

```py
def sum(*args):
    s = 0
    for i in args:
        s += i
    print("sum is", s)
```

> 注意：args 只是一个传统命名，此处可以使用任意有效的标识符，如 *myargs等。

- `*` 将序列/集合解压缩为位置参数

例如：

```py
def my_three(a, b, c):
    print(a, b, c)

a = [1,2,3]
my_three(*a) # here list is broken into three elements
```

该方法只有在**参数和列表元素数目相同**时才可行。

### **kwargs

`**kwargs` 可用于传递可变数目的关键字参数。

例如：

```py
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

>>> greet_me(name="yasoob")
name = yasoob
```

- 方法调用中作为参数传递

```py
def my_three(a, b, c):
    print(a, b, c)

a = {'a': "one", 'b': "two", 'c': "three" }
my_three(**a) # 关键字参数，其实就是字典
```

使用前提：

- 参数名和键名相同;
- 参数数目和字典大小相同。

如果要在函数中同时使用 `*args` 和 `**kwargs`，顺序如下：

```py
some_func(fargs, *args, **kwargs)
```

## Unpacking Argument Lists

如果参数已在 list 或 tuple 中，但是调用函数需要单独的位置参数。例如 `range()` 函数需要 `start` 和 `stop` 参数。如果两者是一起存在的，可以使用 `*` 运算符从 list 或 tuple 中 unpack 参数：

```py
args = [3, 6] # list
list(range(*args)) # 从 list unpack 参数
```

`range(*args)` 等价于 `range(3, 6)`。

类似的，字典可以通过 `**` 运算符传递关键字参数：

```py
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```

## Lambda 函数

Lambda 语法用于创建匿名函数。一般用于创建简单函数，作为其它函数的参数。例如：

```python
def multiple(x, y):
  return x * y
```

其lambda 定义形式：

```py
r = lambda x, y: x * y
r(12, 3) # 调用 lambda 函数，返回36
```
