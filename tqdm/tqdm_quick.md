# tqdm 快速入门

- [tqdm 快速入门](#tqdm-快速入门)
  - [简介](#简介)
  - [基于迭代](#基于迭代)
  - [手动](#手动)
  - [模块](#模块)

***

## 简介

tqdm 是一个创建进度条的工具。主要提供了三种使用方法。

## 基于迭代

- 将迭代类型传入 `tqdm()`

```python
from tqdm import tqdm
from time import sleep

text = ""
for char in tqdm(["a", "b", "c", "d"]):
    sleep(0.25)
    text = text + char
```

```txt
100%|██████████| 4/4 [00:01<00:00,  3.89it/s]
```

- `trange(i)` 是 `tqdm(range(i))` 的优化形式

```python
from tqdm import trange

for i in trange(100):
    sleep(0.01)
```

- 在循环外实例化，可以手动控制 `tqdm()`

```python
pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    sleep(0.25)
    pbar.set_description("Processing %s" % char)
```

## 手动

使用 `with` 语句手动控制 `tqdm()` 更新：

```python
with tqdm(total=100) as pbar:
    for i in range(10):
        sleep(0.1)
        pbar.update(10)
```

也可以不用 `with` 语句，不过使用后需要调用 `del` 或 `close()`：

```python
pbar = tqdm(total=100)
for i in range(10):
    sleep(0.1)
    pbar.update(10)
pbar.close()
```

## 模块

tqdm 在脚本或命令行中使用最有意思。在管道之间插入 `tqdm` (或 `python -m tqdm`)会将所有 `stdin` 传递到 `stdout`，同时将进度打印到 `stderr`。

例如，计算当前目录中所有 Python 文件的行数：

```powershell
$ time find . -name '*.py' -type f -exec cat \{} \; | wc -l
857365

real    0m3.458s
user    0m0.274s
sys     0m3.325s

$ time find . -name '*.py' -type f -exec cat \{} \; | tqdm | wc -l
857366it [00:03, 246471.31it/s]
857365

real    0m3.585s
user    0m0.862s
sys     0m3.358s
```

