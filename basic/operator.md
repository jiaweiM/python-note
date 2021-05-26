# Python 运算符

- [Python 运算符](#python-运算符)
  - [数学运算符](#数学运算符)
  - [比较运算符](#比较运算符)
  - [逻辑运算符](#逻辑运算符)
  - [位运算符](#位运算符)
  - [赋值运算符](#赋值运算符)
  - [识别操作符（Identity operators）](#识别操作符identity-operators)
  - [成员操作符](#成员操作符)
  - [运算符优先级](#运算符优先级)

2021-05-26, 09:59
@Jiawei Mao
***

## 数学运算符

| 运算符 | 说明 |
| --- | --- |
| + | 加法 |
| - | 减法 |
| * | 乘法 |
| / | 浮点除，结果为浮点数 |
| // | 整除，Floor division - 除后，取左边的整数 |
| % | 取模，获得余数 |
| ** | 指数 |

## 比较运算符

| 运算符 | 说明 |
| --- | --- |
| > | Greater than |
| < | Less than |
| == | Equal to |
| != | Not equal to |
| >= | Greater than or equal to |
| <= | Less than or equal to |
| <> |  |

## 逻辑运算符

| 运算符 | 说明 |
| --- | --- |
| and | True if bot the operands are true |
| or | True if either of the operands is True |
| not | True if operand is false |

## 位运算符

假定：

- `x = 10 (0000 1010)`
- `y = 4(0000 0100)`

| 运算符 | 说明 | 实例 |
| --- | --- | --- |
| & | Bitwise AND | x & y = 0 (0000 0000) |
|  |  | Bitwise OR |
| ~ | Bitwise NOT | ~x = -11 (1111 0101) |
| ^ | Bitwise XOR | x ^ y = 14 (0000 1110) |
| >> | Bitwise right shift | x >> 2 = 2 (0000 0010) |
| << | Bitwise left shift | x << 2 = 2 40 (0010 1000) |

## 赋值运算符

| 运算符 | Example | Equivalent to |
| --- | --- | --- |
| = | x=5 | x=5 |
| += | x += 5 | x = x + 5 |
| -= | x -= 5 | x = x - 5 |
| *= | x *= 5 | x = x * 5 |
| /= | x /= 5 | x = x / 5 |
| %= | x %= 5 | x = x % 5 |
| //= | x //= 5 | x = x // 5 |
| **= | x **= 5 | x = x ** 5 |
| &= | x &= 5 | x = x & 5 |
| `|=` | `x |= 5` | `x = x | 5` |
| ^= x | ^= 5 | x = x ^ 5 |
| >>= | x >>= 5 | x = x >> 5 |
| <<= | x <<= 5 | x = x << 5 |

## 识别操作符（Identity operators）

`is` 和 `is not` 为识别操作符，用于判断两个值或变量在内存中地址是否相同。

对 string 和 integer 值，因为是 immutable，所以当它们的值相等，内存地址就相同。

| 操作符 | 说明 |
| --- | --- |
| is | True if the operands are identical (refer to the same object) |
| is not | True if the operands are not identical (do not refer to the same object) |

## 成员操作符

`in` 和 `not in` 为成员操作符（Membership operators）。用于检测一个变量或值是否在一个序列中(string, list, tuple, set and dictionary).

在 dict 中，只能检查 key,不能检测 value.

| Operator | Meaning |
| --- | --- |
| in | True if value/variable is found in the sequence |
| not in | True if value/variable is not found in the sequence |

## 运算符优先级

以下运算符按照从高到低排序

| 运算符 | 描述 |
| --- | --- |
| ( ) | Parentheses (grouping) |
| f (args…) | Function call |
| x[index:index] | Slicing |
| x[index] | Subscription |
| x.attribute | Attribute reference |
| ** | Exponentiation |
| ~x | Bitwise not |
| +x, -x | Positive, negative |
| *,  /, //, % | Multiplication, division, remainder |
| +, - | Addition, subtraction |
| <<, >> | Bitwise shifts |
| & | Bitwise AND |
| ^ | Bitwise XOR |
| `|` | Bitwise OR |
| <=, <, >, >= | Comparison operators |
| <>, !=, == | Equality operators |
| is, is not | Identity operators |
| in, not in | Membership operators |
| not x | Boolean NOT |
| and | Boolean AND |
| or | Boolean OR |
| lambda | Lambda expression |

可以按首字母缩写 _PEMDAS_ 记忆：

- 括号（**P**arentheses）具有最高优先级；
- 乘方（**E**xponentiation）次之；
- 乘法（**M**ultiplication）和除法（**D**ivision）具有相同优先级；
- 加法（**A**ddition）和减法（**S**ubtraction）优先级最低。

相同优先级的运算，按照从左到右的顺序计算。
