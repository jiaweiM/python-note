# fixtures

- [fixtures](#fixtures)
  - [请求 fixture](#请求-fixture)
  - [autouse fixture](#autouse-fixture)
  - [Scope](#scope)

2022-03-20, 00:59
***

## 请求 fixture

测试函数通过将 fixtures 声明为参数来请求 fixtures。

## autouse fixture

自动 fixture，不需要请求，所有测试自动拥有。这样可以避免大量冗余请求。

为 fixture 的装饰器设置 `autouse=True` 使其称为 autouse fixture。例如：

```python
# contents of test_append.py
import pytest


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return []


@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(order, first_entry):
    assert order == [first_entry]


def test_string_and_int(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2]
```

其中 `append_first` 是 autouse fixture。因为是自动指定的，所以两个测试都受它影响，即时两个测试没有请求它。

## Scope

