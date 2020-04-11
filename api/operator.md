# operator

- [operator](#operator)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [对象比较函数](#%e5%af%b9%e8%b1%a1%e6%af%94%e8%be%83%e5%87%bd%e6%95%b0)

## 简介

`operator` 模块定义了一系列和 Python 运算符对应的函数。例如 `operator.add(x, y)` 等效于 `x+y`。许多函数名是用于特殊方法的名称，没有双下划线。为了先后兼容，其中许多还保留双下划线版本。

推荐使用不带双下划线的版本。

`operators`函数按照功能可以分为对象比较、逻辑运算、数学运算和序列运算。

## 对象比较函数

| 功能          | 推荐方法            | 兼容方法                |
| ------------- | ------------------- | ----------------------- |
| less than     | `operator.lt(a, b)` | `operator.__lt__(a, b)` |
| less equal    | `operator.le(a, b)` | `operator.__le__(a, b)` |
| equal         | `operator.eq(a, b)` | `operator.__eq__(a, b)` |
| not equal     | `operator.ne(a, b)` | `operator.__ne__(a, b)` |
| greater equal | `operator.ge(a, b)` | `operator.__ge__(a, b)` |
| greater than  | `operator.gt(a, b)` | `operator.__gt__(a, b)` |

