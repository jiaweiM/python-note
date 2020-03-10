# Content
- [Content](#content)
- [命名](#%e5%91%bd%e5%90%8d)
- [assert](#assert)
  - [浮点数对比](#%e6%b5%ae%e7%82%b9%e6%95%b0%e5%af%b9%e6%af%94)
- [pytest 运行后退出代码](#pytest-%e8%bf%90%e8%a1%8c%e5%90%8e%e9%80%80%e5%87%ba%e4%bb%a3%e7%a0%81)
- [抛出异常](#%e6%8a%9b%e5%87%ba%e5%bc%82%e5%b8%b8)
- [fixtures](#fixtures)
  - [setup](#setup)
  - [teardown](#teardown)
- [测试函数标记](#%e6%b5%8b%e8%af%95%e5%87%bd%e6%95%b0%e6%a0%87%e8%ae%b0)
  - [mark 参数化测试](#mark-%e5%8f%82%e6%95%b0%e5%8c%96%e6%b5%8b%e8%af%95)
  - [跳过测试](#%e8%b7%b3%e8%bf%87%e6%b5%8b%e8%af%95)
- [测试分组](#%e6%b5%8b%e8%af%95%e5%88%86%e7%bb%84)
- [捕获 stdout/stderr 输出](#%e6%8d%95%e8%8e%b7-stdoutstderr-%e8%be%93%e5%87%ba)
- [Reference](#reference)

# 命名
pytest 根据如下规则查找测试：

| scope | 规则                             |
| ----- | -------------------------------- |
| 模块  | `test_*.py` 或 `*_test.py`       |
| 类    | `Test`开头，不带 `__init__` 方法 |
| 函数  | `test_` 开头                     |


# assert
`pytest` 没有专门的 Assert 函数，所有断言都是通过 `assert` 执行。例如：
```py
# content of test_assert1.py
def f():
    return 3


def test_function():
    assert f() == 4
```

## 浮点数对比
通过 `approx` 函数比对：
```py
from pytest import approx

def test_simple():
    assert 0.1 + 0.2 == approx(0.3)

def test_seq():
    assert (0.1 + 0.2, 0.2 + 0.4) == approx((0.3, 0.6))

def test_dict():
    assert {'a': 0.1 + 0.2, 'b': 0.2 + 0.4} == approx({'a': 0.3, 'b': 0.6})
```

`approx` 函数的默认精度为 1e-6，如果需要调整精度，可以通过如下方式：
```py
assert 1.0001 == approx(1, rel=1e-3)
assert 1.0001 == approx(1, abs=1e-3)
assert 1 + 1e-8 == approx(1, rel=1e-6, abs=1e-12)
```
解释：
- `rel` 用于指定相对偏差
- `abs` 用于指定绝对偏差
- 同时指定 `rel` 和 `abs`，则取范围更大的一个。

其他对比浮点数的方法
```py
math.isclose(a,b,rel_tol=1e-9,abs_tol=0.0)`
numpy.isclose(a,b,rtol=1e-5,atol=1e-8)`
```

# pytest 运行后退出代码
| 代码 | 说明                   |
| ---- | ---------------------- |
| 0    | 所有测试运行通过       |
| 1    | 部分测试运行没通过     |
| 2    | 测试被用户打断         |
| 3    | 运行测试时发生内部错误 |
| 4    | pytest命令行使用错误   |
| 5    | 没有找到任何测试       |

# 抛出异常
通过 `pytest.raises` 抛出指定异常，例如：
```py
def test_raise_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

通过如下方式可以访问异常信息：
```py
def test_excep_info():
    with pytest.raises(RuntimeError) as expInfo:
        def f():
            f()

        f()
    assert "maximum recursion" in str(expInfo.value)
```
其中，`expInfo` 是 `ExceptionInfo` 实例，对抛出的异常进行了包装，主要包含 `.type`, `.value` 和 `.traceback` 这三个有用的属性。


# fixtures
fixture为测试提供可靠的重复运行的代码。用于执行测试前初始化和测试后的清理工作，类似于xUnit风格的setup/teaddown函数。包括如下类型：
- 测试模块代码运行前后
- 测试类运行前后
- 测试方法运行前后

## setup
下面演示测试方法运行前后的fixture：
```py
import pytest

@pytest.fixture
def empty_list():
    """Returns a list with length 0"""
    return []

@pytest.fixture
def long_list():
    return [1, 2, 3]

def test_empty_list(empty_list):
    assert len(empty_list) == 0

def test_long_list(long_list):
    assert len(long_list) == 3
```

说明：
- 上面定义了两个 fixture, `empty_list` 和 `long_list`
- fixture 通过参数的形式传递给测试函数，参数名和 fixture 名相同
- 优点，不用反复执行初始化工作
- 在测试类中定义方式相同


## teardown
pytest 支持在对应 fixture 运行出 scope，执行清理工作。使用 `yield` 而非 `return`，`yield` 之后的代码作为
teardown 执行。例：
```py
import smtplib
import pytest

@pytest.fixture(scope="module")
def smtp():
    smtp = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    yield smtp  # provide the fixture value
    print("teardown smtp")
    smtp.close()
```
`print` 和 `smtp.close()` 语句在模块最后一个测试结束后执行。

如果设置 `scope="function"`，则该 feature 在每个测试方法前后运行。

如果结合 `yield` 和 `with` 语句，则更为简洁：
```py
@pytest.fixture(scope="module")
def smtp():
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp:
        yield smtp  # provide the fixture value
```
在测试结束后，`smpt` 在 `with`语句结束后自动关闭。



# 测试函数标记
通过 `pytest.mark` 设置测试函数的元数据（metadata）。pytest 包含的内置标记有：

| mark          | 功能                                                    |
| ------------- | ------------------------------------------------------- |
| `skip`        | 跳过测试                                                |
| `skipif`      | 根据指定条件，跳过测试                                  |
| `xfail`       | 直接失败测试，如某个特性还没实现，或者某个 bug 还没修复 |
| `parametrize` | 参数化测试，mark 只作用于测试，对 fixture 无效          |


## mark 参数化测试
`pytest.mark.parametrize` 用于参数化测试，为单个测试提供多个测试参数。

```py
@pytest.mark.parametrize("va1,va2,sumValue", [
    (1, 2, 3),
    (4, 5, 9)
])
def test_sum(va1, va2, sumValue):
    assert va1 + va2 == sumValue
```
上面提供了两种参数，测试被运行两次，如下：

![](images/2019-09-04-21-23-30.png)

## 跳过测试
`pytest.mark.skip` 用于跳过测试。例：

```py
@pytest.mark.skip(reason="no way of currenly testing this")
def test_unknown():
    pass
```

根据满足条件，跳过测试：
```py
@pytest.mark.skipif(sys.version_info>(3,5))
```

pytest -k multiply
跳过命名包含 multiply 的测试

@pytest.mark.windows
@pytest.mark.mac
为方法设置标签

pytest -m mac 
运行包含 mac 标签的方法


# 测试分组
将测试放在类中：
```py
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
```

不需要扩展任何类，只需要测试类以 Test 开头，pytest就可以发现并运行该测试类。

# 捕获 stdout/stderr 输出
测试的 `stdout` 和 `stderr` 输出都被捕获。如果测试方法或 setup 方法失败，一般会输出捕获的输出和traceback。

# Reference
- [官方文档](https://docs.pytest.org/en/latest/contents.html)
- [简易教程](http://pythontesting.net/framework/pytest/pytest-introduction/)
- [Tutorial](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest)