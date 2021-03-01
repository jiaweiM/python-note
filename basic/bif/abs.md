# abs

如果 x 为整数或浮点数，返回数值的绝对值；若为复数，返回模。

例如：

```py
integer = -20
assert abs(integer) == 20

floating = - 30.33
assert abs(floating) == 30.33
```

对复数：

```py
complex = (3 - 4j)
assert abs(complex) == 5
```