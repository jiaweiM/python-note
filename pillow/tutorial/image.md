# pillow 教程

- [pillow 教程](#pillow-教程)
  - [Image 类](#image-类)
  - [读写图像](#读写图像)
  - [参考](#参考)

2022-01-14, 10:15
***

## Image 类

`Image` 类是 PIL 包中最重要的类。创建该类实例的方式有多种：从文件加载图像、处理其它图像或者从头开始创建图像。

使用 `Image` 模块里的 `open()` 函数载入图像文件：

```python
>>> from PIL import Image
>>> im = Image.open("hopper.ppm")
```

如果没有出错，`open()` 函数会返回一个 `Image` 实例。通过 `Image` 实例可以查看图像属性：

```python
>>> print(im.format, im.size, im.mode)
PPM (512, 512) RGB
```

说明：

- `format` 属性标识图像来源，如果不是从文件读取的，该属性为 `None`；
- `size` 属性为 tuple 类型，标识图像的宽度和高度（in pixels）；
- `mode` 属性定义图像的通道
  - "L" 表示灰度图像
  - "RGB" 表示彩色图像
  - "CMYK" 表示 pre-press 图像

如果打开图像文件失败，抛出 `OSError`。

有了 `Image` 实例后，就可以使用其方法处理图像。例如，显示图像：

```python
>>> im.show()
```

> 标准 `show()` 方法效率不高，因为它将图像保存在一个临时文件，并调用工具显示图像。如果你恰好没有安装合适的工具，它就无法工作。不过当它能工作时，调试起来很方便。

## 读写图像

PIL 

## 参考

- https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
