# 初识 pytest

- [初识 pytest](#初识-pytest)
  - [安装 pytest](#安装-pytest)
  - [创建第一个 test](#创建第一个-test)
  - [运行多个测试](#运行多个测试)
  - [断言抛出指定异常](#断言抛出指定异常)
  - [多个 test 分组到同一个类](#多个-test-分组到同一个类)
  - [临时目录](#临时目录)

2022-03-19, 23:08
****

## 安装 pytest

1. 使用 pip 安装

```sh
pip install -U pytest
```

2. 验证安装

```sh
$ pytest --version
pytest 7.1.1
```

## 创建第一个 test

创建 test_sample.py 文件，其中包含一个函数和一个 test:

```python
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
```

运行 `test_answer` 测试，输出如下：

```sh
$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-7.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 1 item

test_sample.py F                                                     [100%]

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_sample.py::test_answer - assert 4 == 5
============================ 1 failed in 0.12s =============================
```

> 在 IDE 如 pyCharm 中运行，输出稍有不同。

`[100%]` 表示运行所有测试的总体进展。完成后，pytest 显示一个失败报告，因为 `func(3)` 不返回 5.

## 运行多个测试

pytest 会运行当前目录和子目录中所有 test_*.py 或 *_test.py 文件。

## 断言抛出指定异常

使用 `raises` 断言指定代码会抛出异常：

```python
# content of test_sysexit.py
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
```

使用 "quiet" 模型运行测试：

```sh
$ pytest -q test_sysexit.py
.                                                                    [100%]
1 passed in 0.12s
```

> `-q/--quiet` flag 表示在当前和后续测试中简洁输出。

## 多个 test 分组到同一个类

将多个 test 放到同一个类很简单：

```python
# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
```

pytest 会根据命名规则自动检测 test，所以会运行两个 `test_` 前缀测试函数。不需要继承任何类，不过类的名称要以 `Test` 开头。可以直接传入文件名运行：

```sh
$ pytest -q test_class.py
.F                                                                   [100%]
================================= FAILURES =================================
____________________________ TestClass.test_two ____________________________

self = <test_class.TestClass object at 0xdeadbeef0001>

    def test_two(self):
        x = "hello"
>       assert hasattr(x, "check")
E       AssertionError: assert False
E        +  where False = hasattr('hello', 'check')

test_class.py:8: AssertionError
========================= short test summary info ==========================
FAILED test_class.py::TestClass::test_two - AssertionError: assert False
1 failed, 1 passed in 0.12s
```

第一个测试通过，第二个失败。从信息中很容易看出失败位置。

将测试分组有以下好处：

- 更好分类
- 仅在该类中分析 fixture
- 在类中使用标记，隐式应用于其包含的所有测试

不过要注意，当将多个测试当到类中，每个测试都有一个类的实例。因为让每个测试共享同一个类实例不利于测试隔离。示例：

```python
# content of test_class_demo.py
class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1
```

```sh
============================= test session starts =============================
collecting ... collected 2 items

test_class_demo.py::TestClassDemoInstance::test_one 
test_class_demo.py::TestClassDemoInstance::test_two PASSED               [ 50%]FAILED               [100%]
pDeep\test\test_class_demo.py:8 (TestClassDemoInstance.test_two)
0 != 1

Expected :1
Actual   :0

self = <pDeep.test.test_class_demo.TestClassDemoInstance object at 0x0000017B6179CC10>

    def test_two(self):
>       assert self.value == 1
E       assert 0 == 1
E        +  where 0 = <pDeep.test.test_class_demo.TestClassDemoInstance object at 0x0000017B6179CC10>.value

test_class_demo.py:10: AssertionError

========================= 1 failed, 1 passed in 0.15s =========================
```

## 临时目录

pytest 提供内置的 fixtures/function 参数来请求任意资源，包括唯一的临时目录：

```python
# content of test_tmp_path.py
def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0
```

在测试函数签名中添加 `tmp_path` 参数，pytest 在执行测试前会查找并调用 fixture factory 创建该资源。在运行测试前，pytest 创建一个临时目录：

```sh
$ pytest -q test_tmp_path.py
F                                                                    [100%]
================================= FAILURES =================================
_____________________________ test_needsfiles ______________________________

tmp_path = PosixPath('PYTEST_TMPDIR/test_needsfiles0')

    def test_needsfiles(tmp_path):
        print(tmp_path)
>       assert 0
E       assert 0

test_tmp_path.py:3: AssertionError
--------------------------- Captured stdout call ---------------------------
PYTEST_TMPDIR/test_needsfiles0
========================= short test summary info ==========================
FAILED test_tmp_path.py::test_needsfiles - assert 0
1 failed in 0.12s
```
