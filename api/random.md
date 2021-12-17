# random

- [random](#random)
  - [简介](#简介)
  - [管理函数](#管理函数)
    - [seed](#seed)
  - [Functions for integers](#functions-for-integers)
    - [randint](#randint)
  - [Functions for sequences](#functions-for-sequences)
    - [random.choice](#randomchoice)
    - [shuffle](#shuffle)
  - [实值分布](#实值分布)
    - [random.random](#randomrandom)
  - [参考](#参考)

2021-12-14, 19:14
***

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

## Functions for integers

### randint

```python
random.randint(a, b)
```

生成一个随机整数 N，使得 $a \le N \le b$。等价于 `randrange(a, b+1)`。

## Functions for sequences

### random.choice

```py
random.choice(seq)
```

从非空序列 `seq` 中随机返回一个元素。如果 `seq` 为空，抛出 `IndexError`。例如：

```py
a_list = ['apple', 'banana', 'cherry']
print(random.choice(a_list)) # 从上面三个元素随机返回一个
```

### shuffle

```python
random.shuffle(x[, random])
```

将序列 `x` 打乱。

可选参数 `random` 是一个 0 参数函数，返回 [0.0, 1.0) 之间的随机浮点数；默认为函数 `random()`。

## 实值分布

下面的函数生成特定的实值分布。函数参数是根据分布方程中相应的变量来命名的。

### random.random

```python
random.random()
```

返回 [0.0,1.0) 之间的下一个随机浮点数。

## 参考

- https://docs.python.org/3/library/random.html
- https://www.w3schools.com/python/default.asp
