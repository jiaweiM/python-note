# unittest

- [unittest](#unittest)
  - [简介](#简介)
  - [基本示例](#基本示例)
  - [命令行接口](#命令行接口)
    - [命令行选项](#命令行选项)
  - [Test Discovery](#test-discovery)
  - [跳过测试](#跳过测试)
    - [预期失败](#预期失败)
  - [subtest](#subtest)
  - [类和函数](#类和函数)
    - [Test cases](#test-cases)
      - [常用 assert](#常用-assert)
      - [异常 assert](#异常-assert)
      - [具体检查 assert](#具体检查-assert)
      - [集合 assert](#集合-assert)
  - [Class and Module Fixtures](#class-and-module-fixtures)
  - [信号处理](#信号处理)
  - [参考](#参考)

Last updated: 2023-02-07, 16:58
****

## 简介

unittest 单元测试框架最初受 JUnit 启发，与其它语言的单元测试框架的风格类似。支持自动化测试、测试代码共享 setup 和 shutdown，以及独立于报告框架等。

unittest 以面向对象的方式支持如下概念：

| 概念 | 说明 |
|---|---|
| test fixture | 即 setUp 和 shutdown 方法，用于准备测试需要的资源和清理工作 |
| test case | 即测试类，uinittest 提供 TestCase 基类，用于创建新的测试类 |
| test suite | 包含多个 test case 和 test suites。用于将测试打包运行 |
| test runner | 管理测试，输出测试结果 |

## 基本示例

下面是一个简单的脚本，用来测试三个字符串方法：

```python
import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

unittest 测试通过继承 `unittest.TestCase` 创建。三个单独的测试方法以 `test` 开头。此命名约定用于标记哪些方法是测试方法。

每个测试的关键是用 `assertEqual()` 检查结果是否正确；`assertTrue()` 或 `assertFalse()` 检查条件；`assertRaises()` 验证是否引发特定异常。使用这些方法代替 `assert` 语句，方便 test runner 收集测试结果并生成报告。

`setUp()` 和 `tearDown()` 方法用于定义在每个测试方法之前和之后执行的代码

最下面一段是运行测试的简单方法，`unittest.main()` 为测试脚本提供了一个命令行界面，当从命令行运行时，上面的脚本输出如下：

```powershell
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

传入 `-v` 选项可以生成更详细的信息，如下：

```powershell
test_isupper (__main__.TestStringMethods.test_isupper) ... ok
test_split (__main__.TestStringMethods.test_split) ... ok
test_upper (__main__.TestStringMethods.test_upper) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

这就是 unittest 最常用的特性，这些特性足以满足大多数日常测试需求。

## 命令行接口

unittest 模块可以在命令行中使用，可以运行来自模块、类的测试甚至单个测试方法：

```powershell
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
```

可以传入包含模块名、完整类名或方法名任意组合的列表。

- 测试模块也可以通过文件路径指定：

```powershell
python -m unittest tests/test_something.py
```

指定的文件必须可以作为模块导入。通过删除 '.py' 后缀、将路径分隔符转换后为 `.` 将路径转换为模块。如果想执行一个不能作为模块导入的测试文件，那么只能直接执行该文件。

- 使用 `-v` 运行可以获得更相信的测试信息

```powershell
python -m unittest -v test_module
```

- 不带参数执行，或启动 Test Discovery

```powershell
python -m unittest
```

### 命令行选项

## Test Discovery

## 跳过测试

unittest 支持跳过单个测试方法或整个测试类。

使用 `skip()` 装饰器跳过测试；或者直接在 `setUp()` 或测试方法中调用 `TestCase.skipTest()`。

例如：

```python
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass
```

在 `-v` 模式下运行的输出：

```powershell
test_format (__main__.MyTestCase.test_format) ... skipped 'not supported in this library version'
test_nothing (__main__.MyTestCase.test_nothing) ... skipped 'demonstrating skipping'
test_maybe_skipped (__main__.MyTestCase.test_maybe_skipped) ... skipped 'external resource not available'
test_windows_support (__main__.MyTestCase.test_windows_support) ... skipped 'requires Windows'

----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK (skipped=4)
```

跳过类：

```python
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
```

也可以在 `TestCase.setUp()` 跳过类中所有测试，比如在需要的资源不可用时，该方法很有用。

### 预期失败

使用 `expectedFailure()` 装饰器标记预测失败测试：

```python
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
```


## subtest

当多个测试的差异非常小，例如某些参数，可以使用 `subText()` 上下文管理器在测试方法中区分它们。例如：

```python
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
```

会生成如下输出：

```powershell
======================================================================
FAIL: test_even (__main__.NumbersTest.test_even) (i=1)
Test that numbers between 0 and 5 are all even.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 11, in test_even
    self.assertEqual(i % 2, 0)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1 != 0

======================================================================
FAIL: test_even (__main__.NumbersTest.test_even) (i=3)
Test that numbers between 0 and 5 are all even.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 11, in test_even
    self.assertEqual(i % 2, 0)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1 != 0

======================================================================
FAIL: test_even (__main__.NumbersTest.test_even) (i=5)
Test that numbers between 0 and 5 are all even.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 11, in test_even
    self.assertEqual(i % 2, 0)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1 != 0
```

不使用 subtest，在第一次失败后测试就停止了，并且不容易诊断错误。

## 类和函数

### Test cases

```python
class unittest.TestCase(methodName='runTest')
```

- **setUp()**

测试 fixture。除了 `AssertionError` 和 `SkipTest`，该方法引发的任何异常都被认为是错误，而不是测试失败。

- **setUpClass()**

在运行测试之前调用的类方法。`setUpClass()` 只有 `cls` 一个参数，且必须修饰为 `@classmethod`：

```python
@classmethod
def setUpClass(cls):
    ...
```

#### 常用 assert

`TestCase` 类提供了几个断言方法。下表是最常用的方法：

| Method | Checks that | New in |
|---|---|---|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `bool(x) is True` |
| `assertFalse(x)` | `bool(x) is False` |
| `assertIs(a, b)` | `a is b` | 3.1 |
| `assertIsNot(a, b)` | `a is not b` | 3.1 |
| `assertIsNone(x)` | `x is None` | 3.1 |
| `assertIsNotNone(x)` | `x is not None` | 3.1 |
| `assertIn(a, b)` | `a in b` | 3.1 |
| `assertNotIn(a, b)` | `a not in b` | 3.1 |
| `assertIsInstance(a, b)` | `isinstance(a, b)` | 3.2 |
| `assertNotIsInstance(a, b)` | `not isinstance(a, b)` | 3.2 |

```python
assertIn(member, container, msg=None)
assertNotIn(member, container, msg=None)
```

检查 `member` 是否在 `container`。

#### 异常 assert

检查异常、警告和日志信息：

| Method | Checks that | New in |
|---|---|---|
| `assertRaises(exc, fun, *args, **kwds)` | `fun(*args, **kwds)` raises exc |
| `assertRaisesRegex(exc, r, fun, *args, **kwds)` | `fun(*args, **kwds)` raises exc and the message matches regex r | 3.1 |
| assertWarns(warn, fun, *args, **kwds) | fun(*args, **kwds) raises warn | 3.2 |
| assertWarnsRegex(warn, r, fun, *args, **kwds) | fun(*args, **kwds) raises warn and the message matches regex r | 3.2 |
| assertLogs(logger, level) | The with block logs on logger with minimum level | 3.4 |
| assertNoLogs(logger, level) | The with block does not log on logger with minimum level | 3.10 |

#### 具体检查 assert

执行更具体的检查的 assert，例如：

| Method | Checks that | New in |
|---|---|---|
| `assertAlmostEqual(a, b)` | `round(a-b, 7) == 0` |
| `assertNotAlmostEqual(a, b)` | `round(a-b, 7) != 0` |
| `assertGreater(a, b)` | `a > b` | 3.1 |
| `assertGreaterEqual(a, b)` | `a >= b` | 3.1 |
| `assertLess(a, b)` | `a < b` | 3.1 |
| `assertLessEqual(a, b)` | `a <= b` | 3.1 |
| `assertRegex(s, r)` | `r.search(s)` | 3.1 |
| `assertNotRegex(s, r)` | `not r.search(s)` | 3.2 |
| `assertCountEqual(a, b)` | a and b have the same elements in the same number, regardless of their order. | 3.2 |

```python
assertAlmostEqual(first, second, places=7, msg=None, delta=None)
assertNotAlmostEqual(first, second, places=7, msg=None, delta=None)
```

检查 `first` 和 `second` 是否近似相等（或不等）。计算它俩的差值，四舍五入到指定小数点位数（默认 7），然后将差值与 0 进行比较。

如果提供 `delta` 而非 `places`，那么差值必须小于等于 `delta`。

同时提供 `delta` 和 `places` 引发 `TypeError`。

```python
assertCountEqual(first, second, msg=None)
```

检查序列 `first` 和 `second` 是否包含相同元素（忽略顺序）。

不忽略重复元素，会验证两个序列每个元素的数目是否相同。等价于 `assertEqual(Counter(list(first)), Counter(list(second)))`，但也可用于不可哈希对象。

#### 集合 assert

下表总结了 `assertEqual()` 自动使用的特定于类型的 assert 方法。通常不需要直接调用这些方法。

| Method | Used to compare | New in |
|---|---|---|
| assertMultiLineEqual(a, b) | strings | 3.1 |
| assertSequenceEqual(a, b) | sequences | 3.1 |
| assertListEqual(a, b) | lists | 3.1 |
| assertTupleEqual(a, b) | tuples | 3.1 |
| assertSetEqual(a, b) | sets or frozensets | 3.1 |
| assertDictEqual(a, b) | dicts | 3.1 |

## Class and Module Fixtures

类和模块级别的 fixture 在 `TestSuite` 中实现。



## 信号处理

## 参考

- https://docs.python.org/3/library/unittest.html
