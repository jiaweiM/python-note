# random

## 简介

该模块实现伪随机数生成器。

## 管理函数

### seed

```py
random.seed(a=None, version=2)
```

初始化随机数生成器。

参数 `a` 说明：

- 如果忽略 a 或者 a 为 None ，则使用当前系统时间。如果操作系统提供了随机源，则使用随机源而非系统时间。
- 如果 a 为整数，则直接使用。
- 在版本2 （默认）中

## 序列相关函数

### choice

```py
random.choice(seq)
```

从一个非空序列中随机返回一个元素。如果 `seq` 为空，抛出 `IndexError`。例如：

```py
a_list = ['apple', 'banana', 'cherry']
print(random.choice(a_list)) # 从上面三个元素随机返回一个
```

## 参考

- https://docs.python.org/3/library/random.html
- https://www.w3schools.com/python/default.asp
