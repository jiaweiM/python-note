# YAML 语法

- [YAML 语法](#yaml-语法)
  - [简介](#简介)
  - [Document](#document)
  - [Block sequences](#block-sequences)
  - [Block mappings](#block-mappings)
  - [Flow collections](#flow-collections)
  - [Scalars](#scalars)
  - [Aliases](#aliases)
  - [Tags](#tags)
  - [参考](#参考)

Last updated: 2023-01-28, 19:22
****

## 简介

下面介绍 YAML 最常见的结构以及相应的 Python 对象。

## Document

YAML stream 是包含 0 或多个文档的集合。空 stream 不包含文档。文档以 `---` 分隔，文档结尾可以加上 `...`。对单个文档 `---` 可有可无。

- 隐式文档示例：

```yml
- Multimedia
- Internet
- Education
```

- 显式文档示例：

```yml
---
- Afterstep
- CTWM
- Oroborus
...
```

- 同一流中多个文档示例：

```yml
---
- Ada
- APL
- ASP

- Assembly
- Awk
---
- Basic
---
- C
- C#    # Note that comments are denoted with ' #' (space then #).
- C++
- Cold Fusion
```

> 注释以 ' #' 标识，即空格加 #

## Block sequences

- 序列以 `- ` 标识 (注意空格)

```yml
# YAML
- The Dagger 'Narthanc'
- The Dagger 'Nimthanc'
- The Dagger 'Dethanc'
```

对应 Python 类型：

```python
["The Dagger 'Narthanc'", "The Dagger 'Nimthanc'", "The Dagger 'Dethanc'"]
```

- 序列可嵌入

```yml
-
  - HTML
  - LaTeX
  - SGML
  - VRML
  - XML
  - YAML
-
  - BSD
  - GNU Hurd
  - Linux
```

对应 Python 类型：

```python
[['HTML', 'LaTeX', 'SGML', 'VRML', 'XML', 'YAML'], ['BSD', 'GNU Hurd', 'Linux']]
```

- 对嵌入序列，可以不换行

```yml
# YAML
- 1.1
- - 2.1
  - 2.2
- - - 3.1
    - 3.2
    - 3.3
```

```python
[1.1, [2.1, 2.2], [[3.1, 3.2, 3.3]]]
```

- 序列可以嵌入到映射，此时不需要索引序列

```yml
# YAML
left hand:
- Ring of Teleportation
- Ring of Speed

right hand:
- Ring of Resist Fire
- Ring of Resist Cold
- Ring of Resist Poison
```

```python
# Python
{'right hand': ['Ring of Resist Fire', 'Ring of Resist Cold', 'Ring of Resist Poison'],
'left hand': ['Ring of Teleportation', 'Ring of Speed']}
```

## Block mappings

映射以冒号加空格 `: ` 分开：

```yml
# YAML
base armor class: 0
base damage: [4,4]
plus to-hit: 12
plus to-dam: 16
plus to-ac: 0
```

```python
# Python
{'plus to-hit': 12, 'base damage': [4, 4], 'base armor class': 0, 'plus to-ac': 0, 'plus to-dam': 16}
```

- 复杂的 key 用 `? `（问号+空格）标识：

```yml
# YAML
? !!python/tuple [0,0]
: The Hero
? !!python/tuple [0,1]
: Treasure
? !!python/tuple [1,0]
: Treasure
? !!python/tuple [1,1]
: The Dragon
```

```python
# Python
{(0, 1): 'Treasure', (1, 0): 'Treasure', (0, 0): 'The Hero', (1, 1): 'The Dragon'}
```

- 映射也可以嵌套

```yml
# YAML
hero:
  hp: 34
  sp: 8
  level: 4
orc:
  hp: 12
  sp: 0
  level: 2
```

```python
# Python
{'hero': {'hp': 34, 'sp': 8, 'level': 4}, 'orc': {'hp': 12, 'sp': 0, 'level': 2}}
```

- 映射可以嵌套到序列中

```yml
# YAML
- name: PyYAML
  status: 4
  license: MIT
  language: Python
- name: PySyck
  status: 5
  license: BSD
  language: Python
```

```python
# Python
[{'status': 4, 'language': 'Python', 'name': 'PyYAML', 'license': 'MIT'},
{'status': 5, 'license': 'BSD', 'name': 'PySyck', 'language': 'Python'}]
```

## Flow collections

YAML 的 flow 集合与 Python 的 list 和 dict 语法非常像：

```yml
# YAML
{ str: [15, 17], con: [16, 16], dex: [17, 18], wis: [16, 16], int: [10, 13], chr: [5, 8] }
```

```python
# Python
{'dex': [17, 18], 'int': [10, 13], 'chr': [5, 8], 'wis': [16, 16], 'str': [15, 17], 'con': [16, 16]}
```

## Scalars

YAML 有 5 种类型的标量：plain, single-quoted, double-quoted, literal 和 folded。

```yml
# YAML
plain: Scroll of Remove Curse
single-quoted: 'EASY_KNOW'
double-quoted: "?"
literal: |    # Borrowed from http://www.kersbergen.com/flump/religion.html
  by hjw              ___
     __              /.-.\
    /  )_____________\\  Y
   /_ /=== == === === =\ _\_
  ( /)=== == === === == Y   \
   `-------------------(  o  )
                        \___/
folded: >
  It removes all ordinary curses from all equipped items.
  Heavy or permanent curses are unaffected.
```

```python
# Python
{'plain': 'Scroll of Remove Curse',
'literal':
    'by hjw              ___\n'
    '   __              /.-.\\\n'
    '  /  )_____________\\\\  Y\n'
    ' /_ /=== == === === =\\ _\\_\n'
    '( /)=== == === === == Y   \\\n'
    ' `-------------------(  o  )\n'
    '                      \\___/\n',
'single-quoted': 'EASY_KNOW',
'double-quoted': '?',
'folded': 'It removes all ordinary curses from all equipped items. Heavy or permanent curses are unaffected.\n'}
```

- plain 标量的开始和结束都没有指示符，应用最受限，一般用于属性和参数名；
- single-quoted 标量可以表示任何没有特殊字符的值。除了相邻引号 `''` 被替换为单个引号 `'`，不发生转义；
- double-quoted 标量最强大，可以表示任意标量值。允许转义，通过 `\x*` 和 `\u***` 可以表示任何 ASCII 或 Unicode 字符；
- literal 和 folded 适合大量文本，如源代码。folded 样式与 literal 类似，但是两个相邻的非空行会被连接到一起，以空格分开。

## Aliases

YAML 可以表示任何类似 graph 的结果。如果要在文档的不同部分引用同一个对象，则需要使用锚点（anchor）别名（alias）。

锚点用 `&` 指示，别名用 `*` 表示。

```yml
left hand: &A
  name: The Bastard Sword of Eowyn
  weight: 30
right hand: *A
```

PyYAML 支持递归对象，例如：

```yml
&A [ *A ]
```

会生成一个 list 对象，包含其自身。

## Tags

Tags 用来表示 YAML 节点的类型。标准 YAXML tags 定义在 https://yaml.org/type/index.html 。

tags 可能是隐式的：

```yml
boolean: true
integer: 3
float: 3.14
```

```python
{'boolean': True, 'integer': 3, 'float': 3.14}
```

或显式的：

```yml
boolean: !!bool "true"
integer: !!int "3"
float: !!float "3.14"
```

```python
{'boolean': True, 'integer': 3, 'float': 3.14}
```

非显式定义 tags 的 plain 标量会按隐式 tag 解析。标量值对着一组正则表达式进行匹配。

## 参考

- https://pyyaml.org/wiki/PyYAMLDocumentation
- https://yaml.org/spec/1.1/#id857168
