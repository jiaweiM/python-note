# Python Function

- [Python Function](#python-function)
  - [简介](#%e7%ae%80%e4%bb%8b)
    - [创建函数](#%e5%88%9b%e5%bb%ba%e5%87%bd%e6%95%b0)
    - [函数返回值](#%e5%87%bd%e6%95%b0%e8%bf%94%e5%9b%9e%e5%80%bc)
    - [关于局部和全局变量](#%e5%85%b3%e4%ba%8e%e5%b1%80%e9%83%a8%e5%92%8c%e5%85%a8%e5%b1%80%e5%8f%98%e9%87%8f)
  - [参数](#%e5%8f%82%e6%95%b0)
    - [关键字参数](#%e5%85%b3%e9%94%ae%e5%ad%97%e5%8f%82%e6%95%b0)
    - [默认参数](#%e9%bb%98%e8%ae%a4%e5%8f%82%e6%95%b0)
    - [可变参数 *args](#%e5%8f%af%e5%8f%98%e5%8f%82%e6%95%b0-args)
    - [**kwargs](#kwargs)
  - [Lambda 函数](#lambda-%e5%87%bd%e6%95%b0)

***

## 简介

函数是可重复使用的代码片段。

形参：parameters  
实参：arguments

### 创建函数

语法：

```py
def function_name(arg1, arg2, arg3, … argN):
  # statement inside function
```

### 函数返回值

return 后不带任何值，则返回None.

可以一次返回多个值，值之间以逗号分开，为 tuple类型。

### 关于局部和全局变量

如果局部变量和全局变量同名，则全局变量被覆盖，如果要在函数内修改全局变量的值，需加 global：

```py
t = 1
def increment():
  global t   # now t inside the function is same as t outside the function
  t = t + 1
  print(t)   # Displays 2

increment()
print(t)  # Displays 2
```

声明的global 变量时不能赋值，下面的做法是错误的：

```py
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

甚至可以在函数内部声明全局变量：

```py
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
使用 `*args` 传递可变数目的参数给函数。例如，下面是包含两个参数的函数：

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

使用 `*args` 还可以将可迭代变量传递给函数，如：

```py
def my_three(a, b, c):
    print(a, b, c)

a = [1,2,3]
my_three(*a) # here list is broken into three elements
```

该方法只有在**参数和列表元素数目相同**时才可行。

### **kwargs

`**kwargs` 可用于传递可变数目的关键字参数。

方法调用中作为参数传递：

```py
def my_three(a, b, c):
    print(a, b, c)

a = {'a': "one", 'b': "two", 'c': "three" }
my_three(**a)
```

使用前提：

- 参数名和键名相同;
- 参数数目和字典大小相同。

## Lambda 函数

Lambda 语法创建的函数为匿名函数。一般用于创建简单函数，作为其它函数的参数。

例：

```py
def multiple(x, y):
  return x * y
```

其lambda 定义形式：

```py
r = lambda x, y: x * y
r(12, 3) # 调用 lambda 函数，返回36
```
