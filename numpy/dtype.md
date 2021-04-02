# Data type (dtype)

- [Data type (dtype)](#data-type-dtype)
  - [简介](#简介)

## 简介

数据类型对象（`numpy.dtype`）描述了数据的字节大小。它包含了数据的如下内容：

1. 类型（integer, float, Python object 等）
2. 大小：数据类型包含的字节数
3. 字节序（little-endian 或 big-endian）。
4. 如果是结构化数据类型，即其它数据类型的组合：
   - 字段名称
   - 每个字段的数据类型
   - 每个字段占据内存大小
5. 如果是 sub-array，则包含 shape 和数据类型

