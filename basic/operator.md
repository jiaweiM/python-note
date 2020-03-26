# Python Operators

- [Python Operators](#python-operators)
  - [数学运算符](#%e6%95%b0%e5%ad%a6%e8%bf%90%e7%ae%97%e7%ac%a6)
  - [比较运算符](#%e6%af%94%e8%be%83%e8%bf%90%e7%ae%97%e7%ac%a6)
  - [逻辑运算符](#%e9%80%bb%e8%be%91%e8%bf%90%e7%ae%97%e7%ac%a6)
  - [位运算符](#%e4%bd%8d%e8%bf%90%e7%ae%97%e7%ac%a6)
  - [赋值运算符](#%e8%b5%8b%e5%80%bc%e8%bf%90%e7%ae%97%e7%ac%a6)
  - [识别操作符（Identity operators）](#%e8%af%86%e5%88%ab%e6%93%8d%e4%bd%9c%e7%ac%a6identity-operators)
  - [成员操作符（Membership operators）](#%e6%88%90%e5%91%98%e6%93%8d%e4%bd%9c%e7%ac%a6membership-operators)
  - [运算符优先级](#%e8%bf%90%e7%ae%97%e7%ac%a6%e4%bc%98%e5%85%88%e7%ba%a7)

***

## 数学运算符

| 运算符 | 说明                                      |
| ------ | ----------------------------------------- |
| +      | 加法                                      |
| -      | 减法                                      |
| *      | 乘法                                      |
| /      | 浮点除，结果为浮点数                      |
| //     | 整除，Floor division - 除后，取左边的整数 |
| %      | 取模，获得余数                            |
| **     | 指数                                      |

## 比较运算符

| 运算符 | 说明                     |
| ------ | ------------------------ |
| >      | Greater than             |
| <      | Less than                |
| ==     | Equal to                 |
| !=     | Not equal to             |
| >=     | Greater than or equal to |
| <=     | Less than or equal to    |
| <>     |                          |

## 逻辑运算符

| 运算符 | 说明                                   |
| ------ | -------------------------------------- |
| and    | True if bot the operands are true      |
| or     | True if either of the operands is True |
| not    | True if operand is false               |

## 位运算符

假定：  
`x = 10 (0000 1010)`,  
`y = 4(0000 0100)`

| 运算符 | 说明                | 实例                      |
| ------ | ------------------- | ------------------------- |
| &      | Bitwise AND         | x & y = 0 (0000 0000)     |
|        |                     | Bitwise OR                | x | y = 14 (0000 1110) |
| ~      | Bitwise NOT         | ~x = -11 (1111 0101)      |
| ^      | Bitwise XOR         | x ^ y = 14 (0000 1110)    |
| >>     | Bitwise right shift | x >> 2 = 2 (0000 0010)    |
| <<     | Bitwise left shift  | x << 2 = 2 40 (0010 1000) |

## 赋值运算符

| 运算符 | Example  | Equivalent to |
| ------ | -------- | ------------- |
| =      | x=5      | x=5           |
| +=     | x += 5   | x = x + 5     |
| -=     | x -= 5   | x = x - 5     |
| *=     | x *= 5   | x = x * 5     |
| /=     | x /= 5   | x = x / 5     |
| %=     | x %= 5   | x = x % 5     |
| //=    | x //= 5  | x = x // 5    |
| **=    | x **= 5  | x = x ** 5    |
| &=     | x &= 5   | x = x & 5     |
| `|=`   | `x |= 5` | `x = x | 5`   |
| ^= x   | ^= 5     | x = x ^ 5     |
| >>=    | x >>= 5  | x = x >> 5    |
| <<=    | x <<= 5  | x = x << 5    |

## 识别操作符（Identity operators）

`is` 和 `is not` 为识别操作符，用于判断两个值或变量在内存中地址是否相同。

对 string 和 integer 值，因为是 immutable，所以当它们的值相等，内存地址就相同。

| 操作符 | 说明                                                                     |
| ------ | ------------------------------------------------------------------------ |
| is     | True if the operands are identical (refer to the same object)            |
| is not | True if the operands are not identical (do not refer to the same object) |

## 成员操作符（Membership operators）

`in` 和 `not in` 为成员操作符。用于检测一个变量或值是否在一个序列中(string, list, tuple, set and dictionary).

在 dict 中，只能检查 key,不能检测 value.

| Operator | Meaning                                             |
| -------- | --------------------------------------------------- |
| in       | True if value/variable is found in the sequence     |
| not in   | True if value/variable is not found in the sequence |

## 运算符优先级

以下运算符按照从高到低排序

| 运算符         | 描述                                |
| -------------- | ----------------------------------- |
| ( )            | Parentheses (grouping)              |
| f (args…)      | Function call                       |
| x[index:index] | Slicing                             |
| x[index]       | Subscription                        |
| x.attribute    | Attribute reference                 |
| **             | Exponentiation                      |
| ~x             | Bitwise not                         |
| +x, -x         | Positive, negative                  |
| *,  /, //, %   | Multiplication, division, remainder |
| +, -           | Addition, subtraction               |
| <<, >>         | Bitwise shifts                      |
| &              | Bitwise AND                         |
| ^              | Bitwise XOR                         |
| `|`            | Bitwise OR                          |
| <=, <, >, >=   | Comparison operators                |
| <>, !=, ==     | Equality operators                  |
| is, is not     | Identity operators                  |
| in, not in     | Membership operators                |
| not x          | Boolean NOT                         |
| and            | Boolean AND                         |
| or             | Boolean OR                          |
| lambda         | Lambda expression                   |
