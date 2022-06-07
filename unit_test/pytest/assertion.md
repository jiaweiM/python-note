# assertions

- [assertions](#assertions)
  - [使用 assert 语句](#使用-assert-语句)
  - [异常断言](#异常断言)

2022-03-19, 23:05
***

## 使用 assert 语句

pytest 支持标准的 Python `assert` 断言。例如：

```python
# content of test_assert1.py
def f():
    return 3


def test_function():
    assert f() == 4
```

断言函数返回某个值。如果断言失败，可以看到函数的返回值：

```sh
$ pytest test_assert1.py
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-7.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 1 item

test_assert1.py F                                                    [100%]

================================= FAILURES =================================
______________________________ test_function _______________________________

    def test_function():
>       assert f() == 4
E       assert 3 == 4
E        +  where 3 = f()

test_assert1.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_assert1.py::test_function - assert 3 == 4
============================ 1 failed in 0.12s =============================
```

pytest 支持显示常见的子表达式，包括调用、属性、比较、二元运算和一元运算。这样就省掉了样板代码，在不丢失内省信息的同时使用 Python 语法测试。

但是，如果指定了断言信息：

```python
assert a % 2 == 0, "value was odd, should be even"
```

此时不会执行断言内省，而单纯的显示上述信息。

## 异常断言

使用 `pytest.raises()` 作为 context manager 编写异常断言：

```python
import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

如果需要访问实际的异常信息：

```python
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)
```

`excinfo` 是 `ExceptionInfo` 实例，对引入的异常进行了包装。主要属性有 `.type`, `.value` 和 `.traceback`。

甚至可以使用 `match` 关键字将异常的字符串表示和正则表达式进行匹配：

```python
import pytest


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()
```

`match` 方法的 regexp 参数与 `re.search` 函数匹配，因为上面的 `match='123'` 也可以工作。

`pytest.raises()` 函数还有一种形式，传入以参数 `*args` 和 `**kwargs` 执行的函数，断言抛出给定异常：

```python
pytest.raises(ExpectedException, func, *args, **kwargs)
```

还可以将 "raises" 参数指定为 `pytest.mark.xfail`。

```python
@pytest.mark.xfail(raises=IndexError)
def test_f():
    f()
```
