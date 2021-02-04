# Closure

- [Closure](#closure)
- [简介](#简介)
- [定义闭包函数（Closure Function）](#定义闭包函数closure-function)

# 简介

在说明闭包（closure）前，先解释一下嵌套函数和非本地变量。

函数内部定义的函数成为嵌套函数（nested function），嵌套函数可以访问其外部函数内的变量。

在 Python 中，非本地边（non-local）默认只读，如果想修改它们，必须显式声明为 non-cal。

下面是嵌套函数访问 non-local 变量的典型例子：
```py
def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    printer()

# We execute the function
# Output: Hello
print_msg("Hello")
```

可以看到内嵌函数 `printer()` 可以访问外部函数的 non-local 变量 `msg`。

# 定义闭包函数（Closure Function）

对前面的例子，如果最后不调用函数，函数返回 `printer()`函数：
```py
def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    return printer  # this got changed

# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()
```

