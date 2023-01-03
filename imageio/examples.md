# Imageio 使用示例

Last updated: 2022-12-13, 14:54
***

## 简介

部分示例使用 Visvis 可视化图像数据，也可以使用 Matplotlib。

Imageio 提供了一系列示例图像，可以使用类似 'imageio:chelsea.png' 的 URI 来使用。

## 读取猫的图像

```python
import imageio.v3 as iio

im = iio.imread('imageio:chelsea.png')
print(im.shape) # (300, 451, 3)
```

对 GIF 图像：

```python
# index=None 表示文件中的所有图像，并沿这一个轴堆叠
frames = iio.imread("imageio:newtonscradle.gif", index=None)
# ndarray (num_frames, height, width, channel)
print(frames.shape)  # (36, 150, 200, 3)
```

## 读取医疗数据（DICOM）

```python
import imageio.v3 as iio
dirname = 'path/to/dicom/files'

# 读取多个不同 shape 的图像
ims = [img for img in iio.imiter(dirname, plugin='DICOM')]
# Read as volume
vol = iio.imread(dirname, plugin='DICOM')
# 读取多个不同 shape 的 volumes
vols = [img for img in iio.imiter(dirname, plugin='DICOM')]
```

## 参考

- https://imageio.readthedocs.io/en/stable/examples.html
