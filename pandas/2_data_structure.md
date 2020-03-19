# 数据结构

- [数据结构](#%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [查询 - position](#%e6%9f%a5%e8%af%a2---position)

## 简介

Pandas 包含三种类型数据：

- `Series`
- `DataFrame`
- `Panel`

分别对应一维、二维、三维数据。

它们在创建后，均可以动态修改数值，即是 value mutable。`Series`在创建后，长度不再改变。

`Panel` 在 0.25.0 移除。

## 查询 - position

Pandas 提供了基于索引的操作方法。

以 `.iloc` 属性开始，接收如下输入：
- 整数
- 整数列表，如 [4, 3, 0]
- 整数类型切片对象，如 1:7
- boolean 数组
- `callable`
