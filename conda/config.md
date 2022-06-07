# conda config

- [conda config](#conda-config)
  - [简介](#简介)
  - [输出、提示和控制选项](#输出提示和控制选项)
  - [配置文件位置选项](#配置文件位置选项)
  - [子命令](#子命令)
  - [命令修饰符](#命令修饰符)
  - [参考](#参考)

2022-06-07, 14:57
****

## 简介

该命令用于修改配置文件 .condarc。默认写入用户 .condarc 文件（/home/docs/.condarc）。

选项：

```sh
usage: conda config [-h] [--json] [-v] [-q] [--system | --env | --file FILE]
                    [--show [SHOW [SHOW ...]] | --show-sources | --validate |
                    --describe [DESCRIBE [DESCRIBE ...]] | --write-default]
                    [--get [KEY [KEY ...]] | --append KEY VALUE | --prepend
                    KEY VALUE | --set KEY VALUE | --remove KEY VALUE |
                    --remove-key KEY | --stdin]
```

## 输出、提示和控制选项

|选项|功能|
|---|---|
|`--json`|将输出报告为 JSON 格式，适合以编程方式使用 conda|
|`-v, --verbose`|使用一次表示 info, 两次表示 debug，三次表示 trace|
|`-q, --quiet`|不显示进度条|

## 配置文件位置选项

不使用下面的选项，默认使用 '/home/docs/.condarc'。

|选项|说明|
|---|---|
|`--system`|写入位于 '/home/docs/checkouts/readthedocs.org/user_builds/continuumio-conda/envs/latest/.condarc' 的系统 .condarc 文件|
|`--env`|写入激活环境的 .condarc 文件。如果无激活环境，写入用户配置文件 /home/docs/.condarc|
|`--file`|写入指定文件|

## 子命令

|子命令|功能|
|---|---|
|`--show`|显示配置值。如果没有指定参数，则显示所有配置值|
|`--show-sources`|显示所有已识别的配置源|
|`--validate`|验证所有配置源|
|`--describe`|描述指定的参数。如果没有指定参数，则显示所有参数的信息|
|`--write-default`|将默认配置写入文件。等价于 `conda config --describe > ~/.condarc`|

- 显示所有配置信息

```sh
conda config --show
```

## 命令修饰符

|修饰符|功能|
|---|---|
|`--get`|获取配置值|
|`--append`|添加一个配置到列表末尾|
|`--prepend, --add`|添加一个配置到列表开头|
|`--set`|设置 boolean 或字符串 key|
|`--remove`|删除配置值|
|`--remove-key`|删除配置 key 及其所有值|
|`--stdin`|通过 stdin 以 yam 格式传输配置信息|

- 添加 `conda-canary` 源

```sh
conda config --add channels conda-canary
```

- 对当前环境将 verbosity 设置为 3 级（最高级）

```sh
conda config --set verbosity 3 --env
```

- 添加 'conda-forge' 源作为 'defaults' 的备选

```sh
conda config --append channels conda-forge
```

## 参考

- https://docs.conda.io/projects/conda/en/latest/commands/config.html
- https://conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html
