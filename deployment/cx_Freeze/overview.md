# 使用 cx_Freeze

使用 cx_Freeze 有三种方法：

1. 使用附带的 [cxfreeze 脚本](https://cx-freeze.readthedocs.io/en/latest/script.html#script)。
2. 创建 setup 脚本。如果需要额外选项，该方法最合适。
3. 直接调用 cx_Freeze 的类和模块。推荐只用于复杂脚本或扩展。

cx_Freeze 通常会生成一个文件夹，包含可执行文件和所需的共享库（DLL 或 .so 文件）。
