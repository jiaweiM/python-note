# autoreload

```python
%autoreload
```

该扩展在执行用户代码前重新加载模块。

`autoreload` 在执行用户代码前自动重新加载模块。

以下面的工作流为例：

```python
%load_ext autoreload

%autoreload 2

from foo import some_function

some_function()
Out[4]: 42

# open foo.py in an editor and change some_function to return 43

some_function()
Out[6]: 43
```

|命令|说明|
|---|---|
|`%autoreload`|立刻自动重新加载所有模块（被 `%aimport` 排除的除外）|
|`%autoreload 0`|禁用自动加载|
|`%autoreload 1`|每次执行 Python 代码前，重新加载使用 `%aimport` 导入的所有模块|
|`%autoreload 2`|每次执行 Python 代码前，重新加载所有模块（被 `%aimport` 排除的除外）|
|`%autoreload 3`|每次执行 Python 代码前，重新加载所有模块并自动加载新添加的对象|
|`%aimport`|列出要自动导入或不导入的模块|
|`%aimport foo`|导入 "foo" 模块并将其标记为 `%autoreload 1`|
|`%aimport foo, bar`|导入 'foo' 和 'bar' 模块并将它们标记为 `%autoreload 1`|
|`%aimport -foo`|将 'foo' 模块标记为不自动加载|

## 参考

- https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html
