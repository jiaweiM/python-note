# 正则表达式

- [正则表达式](#正则表达式)
  - [简介](#简介)
  - [元字符](#元字符)
    - [特殊字符](#特殊字符)
    - [预定义字符集](#预定义字符集)
    - [量词](#量词)
    - [匹配边界](#匹配边界)
  - [re 模块](#re-模块)
    - [re.compile](#recompile)
    - [re.findall](#refindall)
    - [re.search](#research)
  - [模式](#模式)
  - [Pattern](#pattern)
    - [search](#search)
  - [Match](#match)
  - [参考](#参考)

2021-06-02, 11:14
***

## 简介

正则表达式（RE）本质上是一种小型编程语言，在 Python 中以 `re` 模块的形式嵌入，主要用于字符串匹配和替换。

## 元字符

元字符使得正则表达式比一般的字符串方法更强大。

### 特殊字符

| 字符 | 功能 |
| --- | --- |
| \ | 转义字符。例如需要匹配 `*`，可以用 `\*` 或者字符串 `[*]`。<br>需转义字符：`. + * ? [] $ ^ () {} | \` |
| `.` | 匹配任意除换行符 `\n` 外的字符。在 DOTALL 模式中也能匹配换行符 |
| [...] | 字符集。匹配字符集中任意字符。字符集中的字符可以逐个列出，也可以给出范围，如 [abc] 或 [a-c]。<br>第一个字符如果是 `^` 表示取反。所有的特殊字符在字符集中都失去其特殊含义。在字符集中如果使用 `]`, `-` 或 `^`，可以在前面加上反斜杠，或把 `]`, `-` 放在第一个字符，把 ^ 放在非第一个字符。 |
| [3b-d] | 字符集，匹配 3 以及 'b', 'c', 'd' 中任意一个 |
| [^abc] | 匹配 abc 之外的其它字符 |
| `R | S` | 匹配 `R` 或 `S`，它先尝试匹配左边的表达式，一旦匹配成功就跳过右边的表达式。如果 `|` 没有放在 `()` 中，则它的范围是整个正则表达式 |
| (...) | 创建分组，从表达式左边开始每遇到一个分组的左括号 '('，编号+1.<br>另外，分组表达式作为一个整体，可以后接数量词。分组表达式中的 | 仅在该分组有效 |

### 预定义字符集

可以在 `[...]` 中使用。

| 字符 | 说明 |
| --- | --- |
| \d | 数字：[0-9] |
| \D | 非数字：[^\d] |
| \s | 空白字符：[<空格>\t\r\n\f\v] |
| \S | 非空白字符：[^\s] |
| \w | 单词字符：[A-Za-z0-9_] |
| \W | 非单词字符：[^\w] |

### 量词

用在字符或 `(...)` 之后。

| 字符 | 匹配次数 |
| --- | --- |
| * | [0, ∞) |
| + | [1, ∞) |
| ? | 0 或 1 |
| {m} | m 次 |
| {m ,n} | m 到 n次，m 默认0，n默认∞ |
| *?, =?, ??, {m, n}? | 使匹配成为非贪婪模式 |

### 匹配边界

| 字符 | 说明 |
| --- | --- |
| ^ | 匹配字符串开头。在多行模式中匹配每一行的开头 |
| $ | 匹配字符串末尾。在多行模式中匹配每一行的末尾 |
| \A | 匹配字符串开头 |
| \Z | 匹配字符串末尾 |
| \b | 匹配\w和\W之间的空白字符串，一般用于表示单词的边界 |
| \B | [^\b] |

## re 模块

`re` 模块定义了正则表达式相关的函数、常量和异常。

### re.compile

```py
re.compile(pattern, flags=0)
```

将正则表达式编译为 `Pattern` 对象，从而可以使用 `Pattern` 的 `match()` , `search()` 等方法。

表达式的行为可以通过 `flags` 值修改。多个 flag 可以使用 `|` 运算符合并使用。

方法：

```py
prog = re.compile(pattern)
result = prog.match(string)
```

等价于：

```py
result = re.match(pattern, string)
```

如果一个正则表达式要使用多次，那么使用 `re.compile()` 编译后保存，重用正则表达式效率更高。

> **Note**: 传递给 `re.compile()` 的最近使用的 pattern 的编译版本以及 module-level 的匹配函数会被缓存，因此，如果一次使用的正则表达式不多，就无需担心正则表达式编译对应的性能问题。

### re.findall

```py
re.findall(pattern, string, flags=0)
```

`findall()` 返回所有不重叠的匹配项。从左到右扫描 `string` 字符串，并按找到的顺序返回匹配项。例如：

```py
ptn = '\d+'
string = '123 hello 68. Old 88'
result = re.findall(ptn, string)
# ['123', '68', '88']
```

如果 `pattern` 中有多个 group，则返回 group 列表，多个 group 以元祖形式返回。

### re.search

```py
re.search(pattern, string, flags=0)
```

扫描字符串，找到匹配正则表达式的第一个位置，并返回 Match 对象。如果没有匹配，返回 `None` 。参数说明：

- `pattern` 是正则表达式
- `string` 是待查找的字符串。

首先看一个简单的例子：

```py
s = 'foo123bar'
m = re.search('123', s)
print(m)
# <re.Match object; span=(3, 6), match='123'>
```

在字符串 s 中查找正则表达式 '123'，返回的 `Match` 对象包含匹配的位置和内容:

- 'span=(3,6)' 是匹配上的位置
- match='123' 是匹配上的文本

`Match` 对象为 `True`，换句话说，可以在条件语句中对其进行判断：

```py
s = 'foo123bar'
m = re.search('123', s)
if m:
    print('Found')
else:
    print("Not found")
# Found
```

## 模式

| 短名 | 长名 | 功能 |
| --- | --- | --- |
| re.I | re.IGNORECASE |  |
|  |  |  |
|  |  |  |

## Pattern

编译后的正则表达式对象以 `Pattern` 类表示。

### search

## Match

## 参考

- [https://cuiqingcai.com/977.html](https://cuiqingcai.com/977.html)
- [https://www.programiz.com/python-programming/regex](https://www.programiz.com/python-programming/regex)
