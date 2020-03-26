# MultiIndex / advanced indexing

- [MultiIndex / advanced indexing](#multiindex--advanced-indexing)
  - [分层索引（MultiIndex）](#%e5%88%86%e5%b1%82%e7%b4%a2%e5%bc%95multiindex)
    - [创建 MultiIndex 对象](#%e5%88%9b%e5%bb%ba-multiindex-%e5%af%b9%e8%b1%a1)

***

## 分层索引（MultiIndex）

分层/多层索引方便复杂数据的分析和操作，特别是高维数据。从本质上讲，分层索引技术可以用低维数据结构如 `Series` (1d) 和 `DataFrame` (2d) 存储和处理任意维度的数据。

下面将展示“分层”索引的含义，以及如何和 pandas 的索引功能集成。

### 创建 MultiIndex 对象

`MultiIndex` 存储 axis labels，可以将 `MultiIndex` 看作 tuple 数组，每个 tuple 都是 unique的。

可以使用多种对象创建 `MultiIndex`：

- 数组列表（`MultiIndex.from_arrays()`）
- tuple 数组（`MultiIndex.from_tuples()`）
- 交叉的可迭代对象（`MultiIndex.from_product()`）
- DataFrame （`MultiIndex.from_frame()`）

当将 tuples 列表传递给 `Index` 参数，会返回 `MultiIndex`。
