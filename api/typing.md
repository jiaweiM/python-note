# typing

- [typing](#typing)
  - [简介](#简介)
  - [类型别名](#类型别名)
  - [NewType](#newtype)
  - [模块内容](#模块内容)
    - [特殊基础类型](#特殊基础类型)
      - [特殊类型](#特殊类型)
      - [特殊形式](#特殊形式)
        - [typing.Tuple](#typingtuple)
        - [typing.Union](#typingunion)
    - [Generic concrete collections](#generic-concrete-collections)
      - [对应内置类型](#对应内置类型)
        - [typing.List](#typinglist)
  - [参考](#参考)

Last updated: 2023-01-30, 10:55
***

## 简介

`typing` 模块用于支持运行时类型提示。支持的最基本类型包括 `Any`, `Union`, `Callable`, `TypeVar` 和 `Generic`。[PEP 484](https://peps.python.org/pep-0484/) 提供了完整规范，[PEP 483](https://peps.python.org/pep-0483/) 提供了简介。

加入 typing 后不会影响程序运行，也不会报正式的错误，只是提醒 pycharm 等支持 typing 的 IDE 参数类型有错误。

接受一个字符串参数、返回一个字符串的函数注释如下：

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```

在 `greeting` 函数中，要求参数 `name` 为 `str` 类型，返回值也是 `str` 类型，接受子类型实参。

`typing` 模块经常添加新特性，[typing-extensions](https://pypi.org/project/typing-extensions/) 为旧版本的 Python 提供这些新特性。

## 类型别名

例如，将 `Vector` 定义为 `list[float]` 的别名：

```python
Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
```

类型别名对于简化复杂类型的签名非常有用。例如：

```python
from collections.abc import Sequence

ConnectionOptions = dict[str, str]
Address = tuple[str, int]
Server = tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    ...

# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.
def broadcast_message(
        message: str,
        servers: Sequence[tuple[tuple[str, int], dict[str, str]]]) -> None:
    ...
```

> **NOTE:** `None` 是一种特殊的类型提示，被替换为 `type(None)`

## NewType

`NewType` 用来创建类型：

```python
from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)
```

静态类型检查器会将新类型看作原始类型的子类。这有助于捕获逻辑错误：

```python
def get_user_name(user_id: UserId) -> str:
    ...

# passes type checking
user_a = get_user_name(UserId(42351))

# fails type checking; an int is not a UserId
user_b = get_user_name(-1)
```

对 `UserId` 类型变量可以执行所有 `int` 操作，但是结果是 `int` 类型，不再是 `UserId`。

这样对需要 `int` 类型的地方，都可以传入 `UserId`，但可以避免创建无效的 `UserId`：

```python
# 'output' is of type 'int', not 'UserId'
output = UserId(23413) + UserId(54341)
```

这些检查仅由静态类型检查器执行。在运行时，语句 `Derived = NewType('Derived', Base)` 

## 模块内容

`typing` 模块定义了如下类、函数和装饰器。

> **NOTE:** 该模块定义了几个类型，这些类型扩展标准库中的已有类，同时扩展 `Generic` 以支持 `[]`。在 Python 3.9 中部分已有类被增强以支持 `[]`，对应类型就有些多余了。
> 在 Python 3.9 中不推荐使用这些冗余类型，但是解释器不会发出警告。
> 在 Python 3.9 发布 5 年后发布的第一个 Python 版本，会删除这些弃用类型。

### 特殊基础类型

#### 特殊类型

特殊类型可以作为类型注释使用，不支持 `[]`。

**typing.Any**

不限制类型：

- 每种类型都和 `Any` 兼容
- `Any` 与所有类型兼容

**typing.LiteralString**

**typing.Never**

**typing.NoReturn**

#### 特殊形式

它们可以作为 `[]` 的注释类型，每种都有独特语法。

##### typing.Tuple

`Tuple[X, Y]` 为 tuple 类型，且第一项为 X 类型，第二项为 Y 类型。empty tuple 类型可以写为 `Tuple[()]`。

例如：`Tuple[T1, T2]` 是包含两个元素的 tuple，对应类型变量 `T1` 和 `T2`。`Tuple[int, float, str]` 为 int, float 和 string 三元素 tuple。

指定同类型可变长的 tuple，用省略号 `Tuple[int, ...]`。一个纯 `Tuple` 等价于 `Tuple[Any, ...]`，并转换为 `tuple`。

##### typing.Union

Unionn 类型 `Union[X, Y]` 等价于 `X | Y`，表示 X 或 Y。

可以使用 `Union[int, str]` 或简写形式 `int | str` 定义，建议使用简写。

说明：

- 参数必须为 type，且至少一个；
- Union of unions 被展开，例如：

```python
Union[Union[int, str], float] == Union[int, str, float]
```

- 单个参数的 Union 被取消

```python
Union[int] == int  # The constructor actually returns int
```

- 冗余参数被跳过

```python
Union[int, str, int] == Union[int, str] == int | str
```

- 比较 Union 时，忽略参数顺序

```python
Union[int, str] == Union[str, int]
```

- 不能继承或实例化 `Union`
- 不能用 `Union[X][Y]`

### Generic concrete collections

#### 对应内置类型

##### typing.List

```python
class typing.List(list, MutableSequence[T])
```

泛型版本的 `list`。对注释返回类型非常有用。对注释参数，推荐使用抽象集合类型，如 `Sequence` 或 `Iterable`。

示例：

```python
T = TypeVar('T', int, float)

def vec2(x: T, y: T) -> List[T]:
    return [x, y]

def keep_positives(vector: Sequence[T]) -> List[T]:
    return [item for item in vector if item > 0]
```

## 参考

- https://docs.python.org/3/library/typing.html