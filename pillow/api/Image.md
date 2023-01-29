# Image

- [Image](#image)
  - [函数](#函数)
    - [构建图像](#构建图像)
    - [fromarray](#fromarray)
  - [Image 类](#image-类)
    - [Image.save](#imagesave)
  - [参考](#参考)

***

## 函数

### 构建图像

### fromarray

```python
PIL.Image.fromarray(obj, mode=None)
```

从数组对象创建图像。

如果 `obj` 不连续，则调用 `tobytes` 方法并使用 `frombuffer()`。

对 NumPy 格式图像：

```python
from PIL import Image
import numpy as np
im = Image.open("hopper.jpg")
a = np.asarray(im)
```

可以使用该方法转换为 Pillow 图像：

```python
im = Image.fromarray(a)
```

**参数：**

- **obj** 

数组对象。

- **mode**

读取 `obj` 使用的模式，`None` 表示根据类型确定。

模式用于改变读取数据的方式：

```python
from PIL import Image
import numpy as np
a = np.full((1, 1), 300)
im = Image.fromarray(a, mode="L")
im.getpixel((0, 0))  # 44
im = Image.fromarray(a, mode="RGB")
im.getpixel((0, 0))  # (44, 1, 0)
```

**返回：**

Pillow image 对象。

## Image 类

### Image.save

```python
Image.save(fp, format=None, **params)
```



## 参考

- https://pillow.readthedocs.io/en/stable/reference/Image.html
