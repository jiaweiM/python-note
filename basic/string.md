# String

- [String](#string)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [字符串操作](#%e5%ad%97%e7%ac%a6%e4%b8%b2%e6%93%8d%e4%bd%9c)
    - [切片](#%e5%88%87%e7%89%87)
    - [包含](#%e5%8c%85%e5%90%ab)
    - [index](#index)
    - [find](#find)

## 简介

Python 字符串不可变，即创建后，不能修改，只能复制。

例：

```py
str1 = "welcome"
str2 = "welcome"
```

str1 和 str2 引用相同字符串 "welcome"，使用 `id()` 函数，可以确认 str1 和 str2 引用相同对象。

每个 python 对象存储在内存中，使用 `id()` 可以获得内存地址。

Python 不支持字符类型，所有的字符都是字符串类型。

## 字符串操作

|函数|说明|
|---|---|

### 切片

- `[]`, 获得指定索引的字符
- `[:]`，范围切片，获得指定范围的字符。

### 包含

检查一个字符串是否包含另一个字符串。

使用关键字 `in` 可以检查一个字符串是否在另一个字符串中，使用 `not in` 可以执行相反检查。

例如：

```py
def test_in():
    assert 'a' in 'program'
    assert 'at' in 'battle'
    assert 'file' not in 'windows'
```

### index

### find

`str.find(sub[,start[,end]])`

在切片 `s[start:end]` 查找 `sub` 第一次出现的 index。可选的 `start` 和 `end` 参数为切片参数。

如果没有找到 `sub`，返回 -1.

> `find()` 仅在需要知道 `sub` 的位置时使用，如果只为了检查 `sub` 是否为子字符串，用 `in` 操作符。

