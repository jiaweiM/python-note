# Package

- [Package](#package)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [从包中导入模块](#%e4%bb%8e%e5%8c%85%e4%b8%ad%e5%af%bc%e5%85%a5%e6%a8%a1%e5%9d%97)

2020-04-12, 16:31
***

## 简介

我们通常不会将所有文件保存在一个目录，层次结构目录有助于查找和访问。

类似的，Python 中包（package）和目录对应，模块和文件对应。

随着项目的增大，模块越来越多，我们将类似的模块放在一个包中，将其它模块放在其它包中。从而方便项目的管理。

同理，目录可以有子目录，Python 包也可以有子包和模块。

一个目录中必须有 `__init__.py` 文件才算包。这个文件可以为空，不过我们一般将这个包的初始化代码放在其中。

假设我们开发一个游戏，包和模块一个可能组织结构如下：

![structure](images/2020-04-12-16-40-20.png)

## 从包中导入模块

通过 `.` 运算符可以从包中导入特定模块。

例如，导入上图中的 `start` 模块：

```py
import Game.Level.start
```

假设模块中包含 `select_difficulty()` 函数，此时可以使用完整名引用：

```py
Game.Level.start.select_difficulty(2)
```

还可以采用如下方式简化导入：

```py
from Game.Level import start
```

然后可以直接使用：

```py
start.select_difficulty(2)
```

还可以直接导入模块中的函数：

```py
from Game.Level.start import select_difficulty
```

然后就可以直接使用该函数：

```py
select_difficulty(2)
```

虽然这种更简单，但是不推荐如此。使用完整的命名空间可以很好的避免命名冲突。
