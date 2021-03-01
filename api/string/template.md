# 模板字符串

- [模板字符串](#模板字符串)
  - [模板字符串规则](#模板字符串规则)
  - [创建 Template](#创建-template)
  - [substitute](#substitute)
  - [safe_substitute](#safe_substitute)
  - [参考](#参考)

2021-02-24, 21:07
***

## 模板字符串规则

Python 的模板字符串提供了一种简单的字符串替换功能，支持基于 `$` 的替换，规则如下：

- `$$` 为转义符，表示 `$`
- `$identifier` 为替换占位符。
  - 识别符 "identifier" 默认只能包含 ASCII 字母、数字和下划线，以下划线或ASCII 字母开头，不区分大小写。
  - `$` 后的第一个非标识符终止标识符。
- `${identifier}` 和 `$identifier` 等价。如果识别符后面跟着其它有效识别符，例如 `${a}bc`，此时 `{}` 就是必需的。
- 其它格式的 `$` 会抛出 `ValueError`。

`string` 模块提供的 `Template` 类实现了上述规则。下面我们对 `Template` 类进行进行详细介绍。

## 创建 Template

`Template` 构造函数如下：

```py
class string.Template(template)
```

参数为模板字符串。

## substitute

```py
substitute(mapping={}, /, **kwds)
```

执行模板替换操作，返回一个新的字符串。

- `mapping` 为字典类对象，其键与模板中的占位符匹配。例如：

```py
template = Template("$who likes $what")
dct = {"who": "Lilei", "what": "apple"}
t = template.substitute(dct)
assert t == "Lilei likes apple"
```

- `**kwds` 参数表示可以提供关键字参数，此时关键字就是占位符。例如：

```py
from string import Template

s = Template("$who likes $what")
t = s.substitute(who='Lilei', what='apple')
assert t == "Lilei likes apple"
```

- 当同时提供 `mapping` 和 `kwds` 参数并且有重复时，优先使用 `kwds` 的关键字参数。


如果模板字符串中存在其他形式的 `$`，抛出 `ValueError`。例如：

```py
from string import Template

import pytest

d = dict(who='tim')
with pytest.raises(ValueError):
    Template('Give $who $100').substitute(d)
```

如果后面的 `mapping` 或 `kwds` 缺少占位符，抛出 `KeyError`。例如：

```py
with pytest.raises(KeyError):
    Template('$who likes $what').substitute(dict(who='tim'))
```

模板字符串中有两个占位符，而后面字典只有一个，所以抛出 `KeyError` 异常。

## safe_substitute

```py
safe_substitute(mapping={}, /, **kwds)
```

同 `substitute()`，但是如果 `mapping` 或 `kwds` 中缺少占位符，不抛出 `KeyError`，而是原占位符出现在结果字符串中。另外，如果模板字符串中有其它形式的 `$`，不会抛出 `ValueError`，而是直接返回 `$`。

不过该方法依然可能抛出其它异常，之所以称其为“安全”，是因为它总是尝试返回可用的字符串，而不是直接抛出异常。从某种意义上说，`safe_substitute` 是不安全的，因为它会忽略格式错误的模板。




## 参考

- [Python Documentation](https://docs.python.org/3/library/string.html#template-strings)
